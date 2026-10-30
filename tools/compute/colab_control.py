# SPDX-License-Identifier: MIT
# Copyright (c) 2026 JohnnyZPiggy
"""Bounded existing-CLI orchestration; imports never allocate a session."""
import argparse
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import time
from environment_preflight import PreflightError, preflight, resolve_cli
SUPPORTED_DEVICES = ('T4', 'L4', 'G4', 'H100', 'A100')
def authenticated_usage(output):
    match = re.fullmatch(r'Current balance: (-?\d+\.\d{2}) compute units\r?\n'
                        r'Usage rate: (\d+\.\d{2})/hr\r?\n'
                        r'Active assignments: (0|[1-9]\d*)\r?\n?', output)
    if not match or not all(math.isfinite(float(match[i])) for i in (1, 2)):
        return None
    return {'balance': float(match[1]), 'assignments': int(match[3])}
def load_adapter(repo, sha, driver, manifest, deadline):
    def blob(name, suffix):
        path = PurePosixPath(name)
        if not name or path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name or path.suffix != suffix:
            raise PreflightError('UNSAFE_ADAPTER_PATH')
        git = [resolve_cli('git'), '-C', str(repo)]
        tree = subprocess.run([*git, 'ls-tree', '-z', sha, '--', name],
                              stdin=subprocess.DEVNULL, capture_output=True, timeout=10)
        if tree.returncode or tree.stdout.split(b' ', 1)[0] not in (b'100644', b'100755'):
            raise PreflightError('ADAPTER_BLOB_INVALID')
        result = subprocess.run([*git, 'show', sha + ':' + name], stdin=subprocess.DEVNULL,
                                capture_output=True, timeout=10)
        if result.returncode:
            raise PreflightError('ADAPTER_BLOB_INVALID')
        return result.stdout
    entries = json.loads(blob(manifest, '.json'))['artifacts']
    if not isinstance(entries, list) or any(set(e) != {'name'} for e in entries):
        raise PreflightError('ARTIFACT_MANIFEST_INVALID')
    names = [entry['name'] for entry in entries]
    if any(not n.endswith('.json') or '/' in n or '\\' in n for n in names):
        raise PreflightError('UNSAFE_ARTIFACT_NAME')
    return blob(driver, '.py'), names
def parser():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('source-sha', 'run-id'):
        p.add_argument('--'+name, required=True)
    for name in ('repo-path', 'out'):
        p.add_argument('--'+name, required=True, type=Path)
    for name in ('driver', 'artifacts'):
        p.add_argument('--'+name, help='Project-relative committed adapter file')
    p.add_argument('--cli', default='colab', help='Executable verified in this shell context')
    group = p.add_mutually_exclusive_group()
    group.add_argument('--device', default='T4', help='Verified CLI0.7.4 types: '+','.join(SUPPORTED_DEVICES))
    group.add_argument('--devices', help='Comma-separated verified types; complete cleanup before next type')
    for name, default in (('task-seconds', 5400), ('allocation-seconds', 600),
                          ('cleanup-seconds', 60), ('kernel-timeout', 30), ('work-timeout', 240)):
        p.add_argument('--'+name, type=float, default=default)
    p.add_argument('--temp-root', type=Path)
    for name in ('preflight-only', 'install-local', 'allow-device-mismatch'):
        p.add_argument('--'+name, action='store_true')
    return p
def run(args):
    start = time.monotonic()
    task_deadline = start + args.task_seconds
    work_deadline, cleanup_deadline = task_deadline - args.cleanup_seconds, task_deadline
    report = dict(status='FAIL', error=None, source_sha=args.source_sha, run_id=args.run_id,
                  created=False, cleanup_confirmed=False, commands=[], device_requested=args.device,
                  device_observed=None, assignments_before=None, assignments_after=None,
                  balance_before=None, balance_after=None, artifact_sha256={}, classification='TRANSPORT_ONLY_SCIENCE_UNREVIEWED')
    attempted, owns_out, transport = False, False, None
    session = 'sae-' + args.run_id
    scripts = Path(__file__).resolve().parent
    def cli(*cmd, timeout=30, cleanup=False, slots=1):
        remaining = (cleanup_deadline if cleanup else work_deadline) - time.monotonic()
        if remaining <= 0:
            raise PreflightError('CLEANUP_BUDGET_EXPIRED' if cleanup else 'TIME_BUDGET_EXPIRED')
        code, output, status = -1, '', 'FAIL'
        try:
            result = subprocess.run([cli_path, '--auth=oauth2', *map(str, cmd)],
                stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=min(timeout, remaining / slots))
            code, output = result.returncode, result.stdout
            status = 'PASS' if code == 0 else 'FAIL'
        except subprocess.TimeoutExpired:
            status = 'TIMEOUT'
        except OSError:
            status = 'EXECUTABLE_FAILED'
        finally:
            # Raw output/argv may contain credentials, session URLs or private paths.
            report['commands'].append(dict(operation=cmd[0], status=status, exit_code=code))
        return code, output
    def readback(**bounds):
        code, output = cli('usage', **bounds)
        return authenticated_usage(output) if code == 0 else None
    try:
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,39}', args.run_id):
            raise PreflightError('INVALID_RUN_ID')
        if not re.fullmatch(r'[0-9a-f]{40}', args.source_sha):
            raise PreflightError('INVALID_SOURCE_SHA')
        if args.device not in SUPPORTED_DEVICES:
            raise PreflightError('UNSUPPORTED_DEVICE')
        if not all(math.isfinite(x) and x > 0 for x in (args.task_seconds, args.allocation_seconds,
                args.cleanup_seconds, args.kernel_timeout, args.work_timeout)):
            raise PreflightError('INVALID_TIMEOUT_BOUNDS')
        args.out.mkdir(parents=True, exist_ok=False)
        owns_out = True
        cli_path = resolve_cli(args.cli)
        ready = preflight(args.repo_path.resolve(), args.source_sha, cli_path,
                                       args.temp_root, args.install_local, deadline=work_deadline)
        if args.preflight_only:
            report['status'] = 'PREFLIGHT_PASS'
            return report
        code, names = load_adapter(args.repo_path.resolve(), args.source_sha, args.driver, args.artifacts, work_deadline)
        transport = tempfile.TemporaryDirectory(prefix='sae-driver-', dir=args.temp_root)
        driver_path = Path(transport.name) / 'driver.py'
        driver_path.write_bytes(code)
        if ready.get('cli_version') != '0.7.4':
            raise PreflightError('READBACK_UNVERIFIED')
        info = readback()
        if info is None:
            raise PreflightError('READBACK_UNVERIFIED')
        report.update(assignments_before=info['assignments'], balance_before=info['balance'])
        if info['assignments'] != 0:
            raise PreflightError('EXISTING_OR_UNKNOWN_SESSIONS')
        if info['balance'] <= 0:
            raise PreflightError('ENTITLEMENT_NOT_ESTABLISHED')
        attempted = True
        cleanup_deadline = min(task_deadline, time.monotonic() + args.allocation_seconds)
        work_deadline = cleanup_deadline - args.cleanup_seconds
        code, _ = cli('new', '-s', session, '--gpu', args.device, timeout=120)
        if code:
            raise PreflightError('ALLOCATION_FAILED')
        report['created'] = True
        code, output = cli('exec', '-s', session, '-f', scripts / 'kernel_smoke.py',
                           '--timeout', args.kernel_timeout, timeout=args.kernel_timeout + 5)
        if code or not re.search(r'^KERNEL_REACHABLE\s*$', output, re.MULTILINE):
            raise PreflightError('KERNEL_PROBE_FAILED')
        observed = report['device_observed'] = json.loads(re.search(r'^DEVICE_OBSERVED (.+)$', output, re.MULTILINE)[1])
        gpu_names = [d['name'] for d in observed['nvidia_smi']]
        if observed['torch']['status'] == 'AVAILABLE':
            gpu_names.append(observed['torch']['name'])
        family = r'RTX\s+PRO\s*6000' if args.device == 'G4' else r'\b'+args.device+r'\b'
        if not gpu_names or not all(re.search(family, n, re.IGNORECASE) for n in gpu_names):
            report['classification'] = 'DEVICE_MISMATCH'
            if not args.allow_device_mismatch:
                report['status'] = 'BLOCKED'
                raise PreflightError('DEVICE_MISMATCH')
        code, _ = cli('exec', '-s', session, '-f', driver_path,
            '--timeout', args.work_timeout, '--env', 'SAE_CANDIDATE_SHA='+args.source_sha,
            '--env', 'SAE_DEVICE_REQUESTED='+args.device,
            '--env', 'SAE_DEVICE_OBSERVED='+json.dumps(observed, separators=(',', ':')),
            timeout=args.work_timeout + 5)
        if code:
            raise PreflightError('WORK_EXEC_FAILED')
        for name in names:
            code, _ = cli('download', '-s', session, '/content/'+name, args.out / name)
            if code:
                raise PreflightError('DOWNLOAD_FAILED')
            path = args.out / name
            raw = path.read_bytes()
            data = json.loads(raw)
            if data.get('source_sha') != args.source_sha or data.get('status') != 'PASS':
                raise PreflightError('ARTIFACT_SOURCE_OR_STATUS_FAILED')
            report['artifact_sha256'][name] = hashlib.sha256(raw).hexdigest()
        report['status'] = 'PASS'
    except BaseException as exc:
        report['error'] = exc.code if isinstance(exc, PreflightError) else (
            'INTERRUPTED' if isinstance(exc, KeyboardInterrupt) else 'LOCAL_OPERATION_FAILED')
    finally:
        if attempted:
            for attempt in range(2):
                try:
                    code, _ = cli('stop', '-s', session, timeout=15, cleanup=True, slots=4-attempt*2)
                    info = readback(timeout=15, cleanup=True, slots=3-attempt*2)
                    if code == 0 and info is not None and info['assignments'] == 0:
                        report.update(cleanup_confirmed=True, assignments_after=0, balance_after=info['balance'])
                        break
                except (PreflightError, OSError, KeyboardInterrupt):
                    continue
            if not report['cleanup_confirmed']:
                report['status'] = 'CLEANUP_FAILED'
        if transport is not None:
            try:
                transport.cleanup()
            except OSError:
                report['status'] = 'CLEANUP_FAILED'
        report['total_seconds'] = time.monotonic() - start
        if owns_out:
            (args.out / 'colab-control.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    return report
def run_many(args):
    summary = dict(status='FAIL', source_sha=args.source_sha, runs=[], not_run=[])
    owns_out = False
    try:
        devices = args.devices.split(',')
        if not devices or len(set(devices)) != len(devices) or any(d not in SUPPORTED_DEVICES for d in devices):
            raise PreflightError('UNSUPPORTED_DEVICE')
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,34}', args.run_id):
            raise PreflightError('INVALID_RUN_ID')
        args.out.mkdir(parents=True, exist_ok=False)
        owns_out = True
        for index, device in enumerate(devices):
            single = argparse.Namespace(**(vars(args) | dict(device=device, devices=None,
                run_id=args.run_id+'-'+device.lower(), out=args.out/device)))
            result = run(single)
            summary['runs'].append(result)
            attempted = any(c['operation'] == 'new' for c in result['commands'])
            halt = None
            if attempted and (not result['cleanup_confirmed'] or result['assignments_after'] != 0):
                halt = 'CLEANUP_OR_READBACK_FAILED'
            elif result.get('error') == 'INTERRUPTED':
                halt = 'INTERRUPTED'
            elif not attempted and result['status'] != 'PREFLIGHT_PASS':
                halt = 'PREALLOCATION_BLOCKED'
            if halt:
                summary.update(status=halt, not_run=devices[index+1:])
                break
        else:
            summary['status'] = 'PASS' if all(r['status'] in ('PASS','PREFLIGHT_PASS') for r in summary['runs']) else 'PARTIAL'
    except (PreflightError, OSError) as exc:
        summary['error'] = exc.code if isinstance(exc,PreflightError) else 'LOCAL_OPERATION_FAILED'
    finally:
        if owns_out:
            (args.out/'colab-devices.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    return summary
if __name__ == '__main__':
    args = parser().parse_args()
    result = run_many(args) if args.devices is not None else run(args)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['status'] in ('PASS', 'PREFLIGHT_PASS') else 1)
