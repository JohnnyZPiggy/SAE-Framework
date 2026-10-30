# SPDX-License-Identifier: MIT
# Copyright (c) 2026 JohnnyZPiggy
"""Bounded existing-CLI orchestration; imports never allocate a session."""
import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import time

from environment_preflight import PreflightError, preflight, resolve_cli

# Verified CLI0.7.4 commands/session.py resolve_runtime_options mapping, not guesses.
SUPPORTED_DEVICES = ('T4', 'L4', 'G4', 'H100', 'A100')


def observed_device(output):
    lines = re.findall(r'^DEVICE_OBSERVED (.+)$', output, re.MULTILINE)
    if len(lines) != 1 or len(lines[0]) > 8192:
        raise PreflightError('DEVICE_IDENTITY_UNVERIFIED')
    try:
        data = strict_json(lines[0])
        if set(data) != {'nvidia_smi', 'torch'} or not isinstance(data['nvidia_smi'], list) or not 1 <= len(data['nvidia_smi']) <= 16:
            raise ValueError()
        def text(value):
            return isinstance(value, str) and 0 < len(value) <= 256 and all(32 <= ord(c) < 127 for c in value)
        for device in data['nvidia_smi']:
            if (set(device) != {'name', 'memory_total_mib', 'driver_version'} or not text(device['name'])
                    or not text(device['driver_version']) or type(device['memory_total_mib']) is not int
                    or device['memory_total_mib'] <= 0):
                raise ValueError()
        torch = data['torch']
        if torch == {'status': 'NOT_IMPORTABLE'}:
            return data
        if set(torch) != {'status','version','cuda','name','capability'} or not text(torch['version']):
            raise ValueError()
        if torch['status'] == 'AVAILABLE':
            if (not text(torch['cuda']) or not text(torch['name']) or not isinstance(torch['capability'], list)
                    or len(torch['capability']) != 2 or any(type(x) is not int or not 0 <= x <= 99 for x in torch['capability'])):
                raise ValueError()
        elif torch['status'] != 'CUDA_UNAVAILABLE' or torch['name'] is not None or torch['capability'] is not None or torch['cuda'] is not None and not text(torch['cuda']):
            raise ValueError()
        return data
    except (ValueError, TypeError, KeyError):
        raise PreflightError('DEVICE_IDENTITY_UNVERIFIED') from None


def driver_allows_mismatch(code):
    """Only a literal top-level declaration in the committed driver opts in."""
    try:
        declarations = [node.value for node in ast.parse(code).body if isinstance(node, ast.Assign)
                        and any(isinstance(target, ast.Name) and target.id == 'SAE_ALLOW_DEVICE_MISMATCH'
                                for target in node.targets)]
    except (SyntaxError, ValueError):
        raise PreflightError('ADAPTER_SYNTAX_INVALID') from None
    return len(declarations) == 1 and isinstance(declarations[0], ast.Constant) and declarations[0].value is True


def provider_refusal(stdout, stderr, device):
    """Return only exact trusted CLI0.7.4 messages; never log arbitrary stderr."""
    candidates = [
        '[colab] Allocation refused (precondition failed). This can mean too many active sessions, or a temporary usage or capacity limit for the requested runtime. Run `colab stop` to free up a session, wait and retry, or try a different accelerator.',
        f"[colab] Backend rejected accelerator '{device}'. You may not have quota or entitlement for this accelerator on your account. Try a different one (e.g. --gpu T4) or omit --gpu/--tpu for a CPU runtime.",
    ]
    output = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', stdout+'\n'+stderr)
    return next((message for message in candidates if message in output), None)


def strict_json(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise PreflightError('DUPLICATE_JSON_KEY')
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=unique)


def authenticated_usage(output):
    """CLI 0.7.4 prints this only after authenticated, schema-validated ccu-info."""
    if len(output) > 1024:
        return None
    match = re.fullmatch(r'Current balance: (-?\d+\.\d{2}) compute units\r?\n'
                        r'Usage rate: (\d+\.\d{2})/hr\r?\n'
                        r'Active assignments: (0|[1-9]\d*)\r?\n?', output)
    if not match or not all(math.isfinite(float(match[i])) for i in (1, 2)):
        return None
    return {'balance': float(match[1]), 'assignments': int(match[3])}


def load_adapter(repo, sha, driver, manifest, deadline):
    """Read project-owned adapter files from exact Git blobs, never dirty paths."""
    if not re.fullmatch(r'[0-9a-f]{40}', sha):
        raise PreflightError('INVALID_SOURCE_SHA')
    def blob(name, suffix, limit):
        path = PurePosixPath(name)
        if not name or path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name or path.suffix != suffix:
            raise PreflightError('UNSAFE_ADAPTER_PATH')
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise PreflightError('TIME_BUDGET_EXPIRED')
        git = [resolve_cli('git'), '-C', str(repo)]
        tree = subprocess.run([*git, 'ls-tree', '-z', sha, '--', name],
                              stdin=subprocess.DEVNULL, capture_output=True, timeout=min(10, remaining))
        if tree.returncode or tree.stdout.split(b' ', 1)[0] not in (b'100644', b'100755'):
            raise PreflightError('ADAPTER_BLOB_INVALID')
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise PreflightError('TIME_BUDGET_EXPIRED')
        result = subprocess.run([*git, 'show', sha + ':' + name], stdin=subprocess.DEVNULL,
                                capture_output=True, timeout=min(10, remaining))
        if result.returncode or not 0 < len(result.stdout) <= limit:
            raise PreflightError('ADAPTER_BLOB_INVALID')
        return result.stdout
    code = blob(driver, '.py', 1024 * 1024)
    raw = blob(manifest, '.json', 65536)
    data = strict_json(raw)
    if not isinstance(data, dict) or set(data) != {'artifacts'} or not isinstance(data['artifacts'], list) or not 1 <= len(data['artifacts']) <= 16:
        raise PreflightError('ARTIFACT_MANIFEST_INVALID')
    names = []
    for entry in data['artifacts']:
        if not isinstance(entry, dict) or set(entry) != {'name'} or not isinstance(entry['name'], str):
            raise PreflightError('ARTIFACT_MANIFEST_INVALID')
        name = entry['name']
        if (not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,95}\.json', name)
                or name.casefold() == 'colab-control.json'
                or name.split('.')[0].upper() in {'CON', 'PRN', 'AUX', 'NUL', *('COM'+str(i) for i in range(1,10)), *('LPT'+str(i) for i in range(1,10))}
                or name.casefold() in {n.casefold() for n in names}):
            raise PreflightError('UNSAFE_ARTIFACT_NAME')
        names.append(name)
    return code, names, hashlib.sha256(raw).hexdigest()


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-sha', required=True)
    p.add_argument('--repo-path', type=Path, required=True)
    p.add_argument('--driver', help='Project-relative committed self-contained Python driver')
    p.add_argument('--artifacts', help='Project-relative committed JSON artifact manifest')
    p.add_argument('--run-id', required=True)
    p.add_argument('--out', required=True, type=Path)
    p.add_argument('--cli', default='colab', help='Executable verified in this shell context')
    group = p.add_mutually_exclusive_group()
    group.add_argument('--device', default='T4', help='Verified CLI0.7.4 types: '+','.join(SUPPORTED_DEVICES))
    group.add_argument('--devices', help='Comma-separated verified types; complete cleanup before next type')
    p.add_argument('--task-seconds', type=float, default=5400)
    p.add_argument('--allocation-seconds', type=float, default=600)
    p.add_argument('--cleanup-seconds', type=float, default=60)
    p.add_argument('--kernel-timeout', type=float, default=30)
    p.add_argument('--work-timeout', type=float, default=240)
    p.add_argument('--temp-root', type=Path)
    p.add_argument('--preflight-only', action='store_true', help='Never invoke sessions/new/exec')
    p.add_argument('--install-local', action='store_true', help='Explicit no-deps install of exact export in temp')
    return p


def utc():
    return datetime.now(timezone.utc).isoformat()


def run(args):
    start = time.monotonic()
    task_deadline = start + args.task_seconds
    report = {'status': 'FAIL',
              'source_sha': args.source_sha if re.fullmatch(r'[0-9a-f]{40}', args.source_sha) else None,
              'run_id': args.run_id if re.fullmatch(r'[a-z0-9][a-z0-9-]{0,39}', args.run_id) else None,
              'created': False, 'cleanup_confirmed': False, 'utc_start': utc(), 'commands': [], 'readbacks': [],
              'device_requested': args.device if args.device in SUPPORTED_DEVICES else None,
              'device_observed': None,
              'classification': 'PREFLIGHT_ONLY' if args.preflight_only else 'TRANSPORT_ONLY_SCIENCE_UNREVIEWED',
              'events': {name: None for name in ('cli_resolution', 'environment_preflight', 'adapter_validation', 'snapshot_extraction',
                         'wheel_pip_install', 'first_cpu_pass', 'exact_pinned_cpu_test',
                         'kernel_probe', 'remote_workload', 'artifact_download',
                         'github_publication', 'cleanup')},
              'per_attempt_approvals_actual': None, 'api_escalation_requests_actual': None,
              'handoffs_actual': None}
    attempted, owns_out = False, False
    allocation_start = None
    work_deadline = task_deadline - args.cleanup_seconds
    cleanup_deadline = task_deadline
    session = 'sae-' + args.run_id
    cli_path, transport = None, None
    scripts = Path(__file__).resolve().parent

    def cli(*cmd, timeout=30, cleanup=False, slots=1):
        remaining = (cleanup_deadline if cleanup else work_deadline) - time.monotonic()
        if remaining <= 0:
            raise PreflightError('CLEANUP_BUDGET_EXPIRED' if cleanup else 'TIME_BUDGET_EXPIRED')
        timeout = min(timeout, remaining / slots)
        tick = time.monotonic()
        code, output, status = -1, '', 'FAIL'
        try:
            prefix = [cli_path]
            result = subprocess.run([*prefix, '--auth=oauth2', *map(str, cmd)],
                                    stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=timeout)
            code, output = result.returncode, result.stdout
            status = 'PASS' if code == 0 else 'FAIL'
            if cmd[0] == 'new' and code:
                reason = provider_refusal(output, result.stderr, args.device)
                report['provider_error_sha256'] = hashlib.sha256((output+'\n'+result.stderr).encode()).hexdigest()
                if reason:
                    report['provider_reason'] = reason
                    report['classification'] = 'BLOCKED_PROVIDER:'+args.device+':'+reason
                    report['status'] = 'BLOCKED'
        except subprocess.TimeoutExpired:
            status = 'TIMEOUT'
        except OSError:
            status = 'EXECUTABLE_FAILED'
        finally:
            # Raw output/argv may contain credentials, session URLs or private paths.
            report['commands'].append({'operation': cmd[0], 'status': status, 'exit_code': code,
                                       'timeout_seconds': timeout, 'elapsed_seconds': time.monotonic() - tick})
        return code, output

    def readback(phase, **bounds):
        code, output = cli('usage', **bounds)
        info = authenticated_usage(output) if code == 0 else None
        record = {'phase': phase, 'method': 'CLI_074_AUTHENTICATED_CCU_INFO',
                  'status': 'READBACK_UNVERIFIED' if info is None else (
                      'AUTHENTICATED_ZERO' if info['assignments'] == 0 else 'ACTIVE_ASSIGNMENTS')}
        if info is not None:
            record['assignments'] = info['assignments']
        report['readbacks'].append(record)
        return info

    def step(name, action):
        tick = time.monotonic()
        report['events'][name] = {'utc_start': utc(), 'status': 'FAIL'}
        try:
            value = action()
            report['events'][name]['status'] = 'PASS'
            return value
        finally:
            report['events'][name].update(utc_end=utc(), elapsed_seconds=time.monotonic() - tick)

    try:
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,39}', args.run_id):
            raise PreflightError('INVALID_RUN_ID')
        if not re.fullmatch(r'[0-9a-f]{40}', args.source_sha):
            raise PreflightError('INVALID_SOURCE_SHA')
        if args.device not in SUPPORTED_DEVICES:
            raise PreflightError('UNSUPPORTED_DEVICE')
        if not (all(math.isfinite(x) for x in (args.cleanup_seconds,args.allocation_seconds,args.task_seconds,args.kernel_timeout,args.work_timeout))
                and 0 < args.cleanup_seconds < args.allocation_seconds <= 10800
                and args.allocation_seconds <= args.task_seconds <= 14400
                and 0 < args.kernel_timeout <= 60 and 0 < args.work_timeout <= 3600):
            raise PreflightError('INVALID_TIMEOUT_BOUNDS')
        args.out.mkdir(parents=True, exist_ok=False)
        owns_out = True
        cli_path = step('cli_resolution', lambda: resolve_cli(args.cli))
        report['tool_script_sha256'] = {name: hashlib.sha256((scripts / name).read_bytes()).hexdigest()
            for name in ('colab_control.py', 'environment_preflight.py', 'kernel_smoke.py')}
        report['preflight'] = step('environment_preflight', lambda: preflight(
            args.repo_path.resolve(), args.source_sha, cli_path, args.temp_root, args.install_local,
            deadline=work_deadline))
        for key in ('snapshot_extraction', 'wheel_pip_install'):
            report['events'][key] = report['preflight']['events'][key]
        if args.preflight_only:
            report['status'] = 'PREFLIGHT_PASS'
            return report
        if not args.driver or not args.artifacts:
            raise PreflightError('PROJECT_ADAPTER_REQUIRED')
        code, names, manifest_hash = step('adapter_validation', lambda: load_adapter(
            args.repo_path.resolve(), args.source_sha, args.driver, args.artifacts, work_deadline))
        allows_mismatch = driver_allows_mismatch(code)
        report['driver_allows_device_mismatch'] = allows_mismatch
        report['driver_transport_sha256'] = hashlib.sha256(code).hexdigest()
        report['artifact_manifest_sha256'] = manifest_hash
        transport = tempfile.TemporaryDirectory(prefix='sae-driver-', dir=args.temp_root)
        driver_path = Path(transport.name) / 'driver.py'
        driver_path.write_bytes(code)
        if report['preflight'].get('cli_version') != '0.7.4':
            raise PreflightError('READBACK_UNVERIFIED')
        info = readback('preallocation')
        if info is None:
            raise PreflightError('READBACK_UNVERIFIED')
        if info['assignments'] != 0:
            raise PreflightError('EXISTING_OR_UNKNOWN_SESSIONS')
        if info['balance'] <= 0:
            raise PreflightError('ENTITLEMENT_NOT_ESTABLISHED')
        report['balance_before'] = info['balance']
        (args.out / 'allocation_attempted.lock').touch(exist_ok=False)
        attempted = True
        allocation_start = time.monotonic()
        cleanup_deadline = min(task_deadline, allocation_start + args.allocation_seconds)
        work_deadline = cleanup_deadline - args.cleanup_seconds
        code, _ = cli('new', '-s', session, '--gpu', args.device, timeout=120)
        if code:
            report['allocation_failure_scope'] = ('CLI_SUBPROCESS_TIMEOUT'
                if report['commands'][-1]['status'] == 'TIMEOUT' else 'CLI_COMMAND_FAILED')
            report['allocation_http_phase'] = 'UNKNOWN'
            raise PreflightError('ALLOCATION_FAILED')
        report['created'] = True

        def probe():
            code, output = cli('exec', '-s', session, '-f', scripts / 'kernel_smoke.py',
                               '--timeout', args.kernel_timeout, timeout=args.kernel_timeout + 5)
            if code or not re.search(r'^KERNEL_REACHABLE\s*$', output, re.MULTILINE):
                raise PreflightError('KERNEL_PROBE_FAILED')
            observed = observed_device(output)
            report['device_observed'] = observed
            names = [device['name'] for device in observed['nvidia_smi']]
            if observed['torch']['status'] == 'AVAILABLE':
                names.append(observed['torch']['name'])
            matches = all(re.search(r'\b'+re.escape(args.device)+r'\b', name, re.IGNORECASE) for name in names)
            if not matches:
                report['classification'] = 'DEVICE_MISMATCH'
                if not allows_mismatch:
                    report['status'] = 'BLOCKED'
                    raise PreflightError('DEVICE_MISMATCH')
        step('kernel_probe', probe)

        def workload():
            code, output = cli('exec', '-s', session, '-f', driver_path,
                               '--timeout', args.work_timeout, '--env', 'SAE_CANDIDATE_SHA=' + args.source_sha,
                               '--env', 'SAE_DEVICE_REQUESTED='+args.device,
                               '--env', 'SAE_DEVICE_OBSERVED='+json.dumps(report['device_observed'],separators=(',',':')),
                               timeout=args.work_timeout + 5)
            if code:
                raise PreflightError('WORK_EXEC_FAILED')
            return output
        execution = step('remote_workload', workload)

        def download():
            for name in names:
                code, _ = cli('download', '-s', session, '/content/' + name, args.out / name)
                if code:
                    raise PreflightError('DOWNLOAD_FAILED')
                path = args.out / name
                if path.is_symlink() or not 0 < path.stat().st_size <= 1024 * 1024:
                    raise PreflightError('ARTIFACT_SIZE_OR_PATH_INVALID')
                raw = path.read_bytes()
                matches = re.findall(r'^ARTIFACT ' + re.escape(name) + r' (\d+) ([0-9a-f]{64})\s*$', execution, re.MULTILINE)
                if len(matches) != 1 or len(raw) != int(matches[0][0]) or hashlib.sha256(raw).hexdigest() != matches[0][1]:
                    raise PreflightError('ARTIFACT_INTEGRITY_FAILED')
                data = strict_json(raw)
                if not isinstance(data, dict) or data.get('source_sha') != args.source_sha or data.get('status') != 'PASS':
                    raise PreflightError('ARTIFACT_SOURCE_OR_STATUS_FAILED')
                report.setdefault('artifact_sha256', {})[name] = hashlib.sha256(raw).hexdigest()
        step('artifact_download', download)
        report['status'] = 'PASS'
    except BaseException as exc:
        report['error'] = exc.code if isinstance(exc, PreflightError) else (
            'INTERRUPTED' if isinstance(exc, KeyboardInterrupt) else 'LOCAL_OPERATION_FAILED')
        if isinstance(exc, PreflightError) and exc.report:
            report['preflight'] = exc.report
            for key in ('snapshot_extraction', 'wheel_pip_install'):
                report['events'][key] = exc.report['events'].get(key)
    finally:
        tick = time.monotonic()
        if attempted:
            report['events']['cleanup'] = {'utc_start': utc(), 'status': 'FAIL'}
            for attempt in range(2):
                try:
                    code, _ = cli('stop', '-s', session, timeout=15, cleanup=True, slots=4 - attempt * 2)
                    info = readback('cleanup', timeout=15, cleanup=True, slots=3 - attempt * 2)
                    if code == 0 and info is not None and info['assignments'] == 0:
                        report['cleanup_confirmed'] = True
                        report['utc_cleanup_verified'] = utc()
                        report['events']['cleanup']['status'] = 'PASS'
                        break
                except (PreflightError, OSError, KeyboardInterrupt):
                    continue
            report['allocation_lifecycle_seconds'] = time.monotonic() - allocation_start
            report['events']['cleanup'].update(utc_end=utc(), elapsed_seconds=time.monotonic() - tick)
            if not report['cleanup_confirmed']:
                report['status'] = 'CLEANUP_FAILED'
            else:
                try:
                    info = readback('post_cleanup', timeout=15, cleanup=True)
                    if info is None:
                        raise PreflightError('POST_RUN_READBACK_UNVERIFIED')
                    report['balance_after'] = info['balance']
                    report['assignments_after'] = info['assignments']
                    report['balance_delta'] = report['balance_before']-info['balance']
                    if info['assignments'] != 0:
                        raise PreflightError('POST_RUN_ACTIVE_ASSIGNMENTS')
                except (PreflightError, OSError, KeyboardInterrupt) as exc:
                    report['status'] = 'POST_RUN_READBACK_FAILED'
                    report['post_run_error'] = exc.code if isinstance(exc,PreflightError) else 'POST_RUN_READBACK_UNVERIFIED'
        if transport is not None:
            try:
                transport.cleanup()
                report['transport_cleanup_confirmed'] = True
            except OSError:
                report['transport_cleanup_confirmed'] = False
                report['status'] = 'CLEANUP_FAILED'
        report.update(cleanup_seconds=time.monotonic() - tick,
                      total_seconds=time.monotonic() - start, utc_end=utc())
        if owns_out:
            with (args.out / 'colab-control.json').open('x', encoding='utf-8', newline='\n') as handle:
                json.dump(report, handle, indent=2)
                handle.write('\n')
    return report


def run_many(args):
    """Finite per-device cycles; never advance past uncertain account/session state."""
    summary = dict(status='FAIL', source_sha=args.source_sha if re.fullmatch(r'[0-9a-f]{40}',args.source_sha) else None,
                   classification='PREFLIGHT_ONLY' if args.preflight_only else 'TRANSPORT_ONLY_SCIENCE_UNREVIEWED',
                   runs=[], not_run=[])
    owns_out = False
    try:
        devices = args.devices.split(',')
        if not re.fullmatch(r'[0-9a-f]{40}',args.source_sha):
            raise PreflightError('INVALID_SOURCE_SHA')
        if not devices or len(set(devices)) != len(devices) or any(d not in SUPPORTED_DEVICES for d in devices):
            raise PreflightError('UNSUPPORTED_DEVICE')
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,34}', args.run_id):
            raise PreflightError('INVALID_RUN_ID')
        args.out.mkdir(parents=True, exist_ok=False)
        owns_out = True
        for index, device in enumerate(devices):
            single = argparse.Namespace(**vars(args))
            single.device, single.devices = device, None
            single.run_id, single.out = args.run_id+'-'+device.lower(), args.out/device
            result = run(single)
            summary['runs'].append(result)
            attempted = result.get('events',{}).get('cleanup') is not None
            if attempted and (not result.get('cleanup_confirmed') or result.get('assignments_after') != 0):
                summary['status'] = 'CLEANUP_OR_READBACK_FAILED'
                summary['not_run'] = devices[index+1:]
                break
            if not attempted and result.get('status') != 'PREFLIGHT_PASS':
                summary['status'] = 'PREALLOCATION_BLOCKED'
                summary['not_run'] = devices[index+1:]
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
