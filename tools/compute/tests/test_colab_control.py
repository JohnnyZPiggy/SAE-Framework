# SPDX-License-Identifier: MIT
# Copyright (c) 2026 JohnnyZPiggy
"""Deterministic local fake CLI; no provider requests or real allocations."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import colab_control as control
from environment_preflight import PreflightError

SHA = 'a' * 40
ZERO = 'No active sessions found on server.'
REAL_RUN = subprocess.run


def identity(name='NVIDIA T4'):
    return {'nvidia_smi':[{'name':name,'memory_total_mib':15360,'driver_version':'580.82.07'}],
            'torch':{'status':'NOT_IMPORTABLE'}}


class Clock:
    def __init__(self):
        self.now = 0

    def __call__(self):
        return self.now


class FakeCLI:
    def __init__(self, clock, failure=None):
        self.clock, self.failure = clock, failure
        self.calls = []
        self.usage_calls = 0
        self.active = False
        self.requested = 'T4'
        self.artifacts = {name: (json.dumps({'source_sha': SHA, 'status': 'PASS',
                            'kind': 'fake-test-only'})+'\n').encode()
                          for name in ('measurement.json',)}
        if failure in ('source', 'status'):
            self.artifacts['measurement.json'] = json.dumps({
                'source_sha': 'b'*40 if failure == 'source' else SHA,
                'status': 'FAIL' if failure == 'status' else 'PASS'}).encode()

    def __call__(self, argv, **kwargs):
        cmd = argv[argv.index('--auth=oauth2') + 1:]
        op = cmd[0]
        self.calls.append((cmd, kwargs['timeout']))
        self.clock.now += min(.1, kwargs['timeout'])
        code, output = 0, ''
        stderr = 'secret path /home/private/oauth https://private.invalid token=secret'
        if op == 'sessions':
            output = 'unrelated active session' if self.failure == 'existing' or self.active else ZERO
        elif op == 'usage':
            self.usage_calls += 1
            balance = '0.00' if self.failure == 'quota' else '10.00'
            if self.failure == 'post-balance' and self.usage_calls > 1:
                balance = '9.75'
            count = 1 if self.failure == 'existing' or self.active else 0
            output = f'Current balance: {balance} compute units\nUsage rate: 0.00/hr\nActive assignments: {count}'
            failure = self.failure or ''
            if failure == 'post-unverified' and self.usage_calls >= 3:
                output = ''
            if failure.startswith('readback-') or (failure.startswith('cleanup-') and self.usage_calls > 1):
                kind = failure.split('-', 1)[1]
                if kind in ('auth', 'unauthorized'):
                    code = 1
                elif kind in ('empty', 'stop-and-empty'):
                    output = ZERO  # swallowed auth can print this with exit 0
                elif kind == 'timeout':
                    self.clock.now += kwargs['timeout']
                    raise subprocess.TimeoutExpired(argv, kwargs['timeout'], output='https://secret.invalid/?token=private')
                elif kind == 'nonempty':
                    output = output.replace('Active assignments: 0', 'Active assignments: 1')
                elif kind == 'duplicate':
                    output += '\nActive assignments: 0'
        elif op == 'new':
            assert not self.active, 'overlapping sessions'
            self.requested = cmd[cmd.index('--gpu')+1]
            self.active = True
            if self.failure == 'refuse-'+self.requested:
                code = 1
                stderr = (f"[colab] Backend rejected accelerator '{self.requested}'. You may not have quota or entitlement for this accelerator on your account. Try a different one (e.g. --gpu T4) or omit --gpu/--tpu for a CPU runtime.")
            if self.failure == 'allocation-timeout':
                self.clock.now += kwargs['timeout']
                raise subprocess.TimeoutExpired(argv, kwargs['timeout'], output='https://secret.invalid/?token=private')
            if self.failure == 'allocation':
                code = 1  # partial allocation must still stop
        elif op == 'exec':
            probe = cmd[cmd.index('-f') + 1].endswith('kernel_smoke.py')
            if (probe and self.failure in ('probe', 'budget', 'probe-timeout')) or (not probe and self.failure == 'hang'):
                if self.failure in ('budget', 'probe-timeout', 'hang'):
                    self.clock.now += kwargs['timeout']
                    raise subprocess.TimeoutExpired(argv, kwargs['timeout'], output='https://secret.invalid/?token=private')
                code = 1
            elif not probe and self.failure == 'interrupt':
                raise KeyboardInterrupt()
            elif probe:
                name = 'NVIDIA A100' if self.failure == 'mismatch' else 'NVIDIA '+self.requested
                output = 'KERNEL_REACHABLE\nDEVICE_OBSERVED '+json.dumps(identity(name))+'\n'
                if self.failure == 'missing-identity':
                    output = 'KERNEL_REACHABLE\n'
            else:
                output = '\n'.join(f'ARTIFACT {n} {len(raw)} {hashlib.sha256(raw).hexdigest()}'
                                   for n, raw in self.artifacts.items())
        elif op == 'download':
            name = Path(cmd[-2]).name
            Path(cmd[-1]).write_bytes(b'bad' if self.failure == 'hash' else self.artifacts[name])
        elif op == 'stop':
            if self.failure in ('cleanup-stop', 'cleanup-stop-and-empty'):
                self.active = self.failure != 'cleanup-stop'
                return subprocess.CompletedProcess(argv, 1, '', 'token=secret')
            if self.failure == 'cleanup':
                self.clock.now += kwargs['timeout']
                raise subprocess.TimeoutExpired(argv, kwargs['timeout'])
            self.active = False
        else:
            raise AssertionError(op)
        if self.failure == 'readback-stderr' and op == 'usage':
            return subprocess.CompletedProcess(argv, 0, '', output + '\n')
        return subprocess.CompletedProcess(argv, code, output + '\n', stderr)


class ControllerTests(unittest.TestCase):
    def run_fake(self, failure=None, extra=(), cli_version='0.7.4', driver=b'print(1)'):
        with tempfile.TemporaryDirectory() as temp:
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp, '--run-id', 'test-run',
                 '--out', str(Path(temp) / 'new-run'), '--driver', 'driver.py', '--artifacts', 'artifacts.json', '--task-seconds', '100',
                 '--allocation-seconds', '80', '--cleanup-seconds', '20',
                 '--work-timeout', '100', *extra])
            clock = Clock()
            fake = FakeCLI(clock, failure)
            ready = {'status': 'PASS', 'cli_version': cli_version, 'events': {'snapshot_extraction': None, 'wheel_pip_install': None}}
            with patch.object(control, 'resolve_cli', return_value='/verified/colab'), \
                 patch.object(control, 'preflight', return_value=ready), \
                 patch.object(control, 'load_adapter', return_value=(driver, ['measurement.json'], 'b'*64)), \
                 patch.object(control.subprocess, 'run', side_effect=fake), \
                 patch.object(control.time, 'monotonic', side_effect=clock):
                result = control.run(args)
            if (args.out/'colab-control.json').exists():
                saved = json.loads((args.out / 'colab-control.json').read_text())
                self.assertEqual(saved, result)
            else:
                self.assertEqual(fake.calls, [])
            for call in result['commands']:
                self.assertGreater(call['timeout_seconds'], 0)
                self.assertGreaterEqual(call['elapsed_seconds'], 0)
            public = json.dumps(result)
            for secret in ('secret.invalid', '/home/private', 'token=secret', '/verified/colab'):
                self.assertNotIn(secret, public)
            return result, fake

    def test_success_defaults_to_probe_before_work_and_download(self):
        r, fake = self.run_fake()
        self.assertEqual(r['status'], 'PASS')
        execs = [c for c, _ in fake.calls if c[0] == 'exec']
        self.assertTrue(execs[0][execs[0].index('-f') + 1].endswith('kernel_smoke.py'))
        self.assertTrue(execs[1][execs[1].index('-f') + 1].endswith('driver.py'))
        self.assertTrue(r['cleanup_confirmed'])
        self.assertEqual([b['status'] for b in r['readbacks']], ['AUTHENTICATED_ZERO']*3)
        self.assertIsNone(r['events']['github_publication'])
        self.assertIsNone(r['events']['first_cpu_pass'])

    def test_probe_failure_skips_work_and_cleans_up(self):
        r, fake = self.run_fake('probe')
        self.assertEqual(r['error'], 'KERNEL_PROBE_FAILED')
        self.assertEqual(sum(c[0] == 'exec' for c, _ in fake.calls), 1)
        self.assertTrue(r['cleanup_confirmed'])
        self.assertEqual(r['events']['kernel_probe']['status'], 'FAIL')

    def test_probe_timeout_has_short_bound(self):
        r, fake = self.run_fake('probe-timeout')
        self.assertEqual(r['error'], 'KERNEL_PROBE_FAILED')
        self.assertLessEqual(next(t for c, t in fake.calls if c[0] == 'exec'), 35)
        self.assertTrue(r['cleanup_confirmed'])

    def test_work_hang_preserves_cleanup_reserve(self):
        r, fake = self.run_fake('hang')
        self.assertEqual(r['error'], 'WORK_EXEC_FAILED')
        self.assertTrue(r['cleanup_confirmed'])
        self.assertLessEqual(r['allocation_lifecycle_seconds'], 80)
        self.assertTrue(any(c['status'] == 'TIMEOUT' for c in r['commands']))

    def test_expired_work_budget_still_stops(self):
        r, fake = self.run_fake('budget', ['--allocation-seconds', '21'])
        self.assertTrue(r['cleanup_confirmed'])
        self.assertIn('stop', [c[0] for c, _ in fake.calls])

    def test_hash_mismatch(self):
        r, _ = self.run_fake('hash')
        self.assertEqual(r['error'], 'ARTIFACT_INTEGRITY_FAILED')
        self.assertTrue(r['cleanup_confirmed'])

    def test_artifact_source_and_status_mismatch(self):
        for failure in ('source', 'status'):
            with self.subTest(failure=failure):
                r, _ = self.run_fake(failure)
                self.assertEqual(r['error'], 'ARTIFACT_SOURCE_OR_STATUS_FAILED')
                self.assertTrue(r['cleanup_confirmed'])

    def test_partial_new_failure_stops(self):
        r, _ = self.run_fake('allocation')
        self.assertEqual(r['error'], 'ALLOCATION_FAILED')
        self.assertEqual(r['allocation_failure_scope'], 'CLI_COMMAND_FAILED')
        self.assertEqual(r['allocation_http_phase'], 'UNKNOWN')
        self.assertTrue(r['cleanup_confirmed'])

    def test_allocation_timeout_is_outer_scope_not_http_diagnosis(self):
        r, fake = self.run_fake('allocation-timeout')
        self.assertEqual(r['error'], 'ALLOCATION_FAILED')
        self.assertEqual(r['allocation_failure_scope'], 'CLI_SUBPROCESS_TIMEOUT')
        self.assertEqual(r['allocation_http_phase'], 'UNKNOWN')
        self.assertTrue(r['cleanup_confirmed'])
        self.assertEqual([c[0] for c, _ in fake.calls], ['usage', 'new', 'stop', 'usage', 'usage'])
        self.assertLessEqual(r['allocation_lifecycle_seconds'], 80)

    def test_interrupt_stops(self):
        r, _ = self.run_fake('interrupt')
        self.assertEqual(r['error'], 'INTERRUPTED')
        self.assertTrue(r['cleanup_confirmed'])

    def test_failed_cleanup_never_passes(self):
        r, fake = self.run_fake('cleanup')
        self.assertEqual(r['status'], 'CLEANUP_FAILED')
        self.assertEqual(sum(c[0] == 'stop' for c, _ in fake.calls), 2)
        self.assertFalse(r['cleanup_confirmed'])
        self.assertLessEqual(r['allocation_lifecycle_seconds'], 80)

    def test_existing_sessions_not_touched(self):
        r, fake = self.run_fake('existing')
        self.assertEqual(r['error'], 'EXISTING_OR_UNKNOWN_SESSIONS')
        self.assertEqual([c[0] for c, _ in fake.calls], ['usage'])

    def test_quota_blocks_allocation(self):
        r, fake = self.run_fake('quota')
        self.assertEqual(r['error'], 'ENTITLEMENT_NOT_ESTABLISHED')
        self.assertNotIn('new', [c[0] for c, _ in fake.calls])

    def test_untrusted_preallocation_readbacks_never_allocate(self):
        for kind in ('empty', 'auth', 'unauthorized', 'timeout', 'duplicate', 'stderr'):
            with self.subTest(kind=kind):
                r, fake = self.run_fake('readback-' + kind)
                self.assertEqual(r['error'], 'READBACK_UNVERIFIED')
                self.assertFalse(r['created'])
                self.assertFalse(r['cleanup_confirmed'])
                self.assertEqual([c[0] for c, _ in fake.calls], ['usage'])
                self.assertEqual(r['readbacks'][0]['status'], 'READBACK_UNVERIFIED')

    def test_untrusted_cleanup_readback_or_failed_stop_never_passes(self):
        for kind in ('empty', 'auth', 'unauthorized', 'timeout', 'nonempty', 'stop', 'stop-and-empty'):
            with self.subTest(kind=kind):
                r, fake = self.run_fake('cleanup-' + kind)
                self.assertEqual(r['status'], 'CLEANUP_FAILED')
                self.assertFalse(r['cleanup_confirmed'])
                self.assertEqual(sum(c[0] == 'new' for c, _ in fake.calls), 1)
                self.assertEqual(sum(c[0] == 'stop' for c, _ in fake.calls), 2)
                self.assertNotIn('sessions', [c[0] for c, _ in fake.calls])
                self.assertNotIn('status', [c[0] for c, _ in fake.calls])
                self.assertLessEqual(r['allocation_lifecycle_seconds'], 80)
                expected = ('AUTHENTICATED_ZERO' if kind == 'stop' else
                            'ACTIVE_ASSIGNMENTS' if kind == 'nonempty' else 'READBACK_UNVERIFIED')
                self.assertEqual(r['readbacks'][-1]['status'], expected)

    def test_unreviewed_cli_version_blocks_before_provider(self):
        for version in (None, '0.7.5'):
            with self.subTest(version=version):
                r, fake = self.run_fake(cli_version=version)
                self.assertEqual(r['error'], 'READBACK_UNVERIFIED')
                self.assertEqual(fake.calls, [])

    def test_authenticated_usage_rejects_partial_ambiguous_or_nonfinite_text(self):
        good = 'Current balance: 10.00 compute units\nUsage rate: 0.00/hr\nActive assignments: 0\n'
        self.assertEqual(control.authenticated_usage(good), {'balance': 10.0, 'assignments': 0})
        self.assertEqual(control.authenticated_usage(good.replace('\n', '\r\n'))['assignments'], 0)
        self.assertEqual(control.authenticated_usage(good.replace('10.00', '-1.00'))['assignments'], 0)
        for text in ('', ZERO, good + good, 'warning\n' + good, good + 'warning',
                     good.replace('10.00', 'nan'), good.replace('0.00/hr', 'inf/hr'),
                     good.replace('assignments: 0', 'assignments: -1'),
                     good.replace('assignments: 0', 'assignments: 0 extra'), '9'*10000):
            with self.subTest(text=text[:40]):
                self.assertIsNone(control.authenticated_usage(text))

    def test_preflight_only_never_calls_provider(self):
        r, fake = self.run_fake(extra=['--preflight-only'])
        self.assertEqual(r['status'], 'PREFLIGHT_PASS')
        self.assertEqual(fake.calls, [])

    def test_existing_output_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            original = out / 'colab-control.json'
            original.write_text('historical')
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp, '--run-id', 'existing', '--out', str(out)])
            with patch.object(control, 'resolve_cli') as resolver:
                r = control.run(args)
            resolver.assert_not_called()
            self.assertEqual(r['status'], 'FAIL')
            self.assertEqual(original.read_text(), 'historical')

    def test_unavailable_cli_blocks_before_provider(self):
        with tempfile.TemporaryDirectory() as temp:
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp, '--run-id', 'absent', '--out', str(Path(temp)/'run')])
            with patch.object(control, 'resolve_cli', side_effect=PreflightError('CLI_UNAVAILABLE')), \
                 patch.object(control.subprocess, 'run') as runner:
                r = control.run(args)
            self.assertEqual(r['error'], 'CLI_UNAVAILABLE')
            runner.assert_not_called()

    def test_real_local_child_timeout_still_cleans_up(self):
        # Execute only a sleeping local Python, never the installed Colab CLI.
        with tempfile.TemporaryDirectory() as temp:
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp, '--run-id', 'child-timeout',
                '--out', str(Path(temp)/'run'), '--driver', 'driver.py', '--artifacts', 'artifacts.json', '--kernel-timeout', '.01'])
            fake = FakeCLI(Clock())
            def subprocess_cli(argv, **kwargs):
                if 'exec' in argv:
                    return REAL_RUN([sys.executable, '-c', 'import time; time.sleep(30)'], **kwargs)
                return fake(argv, **kwargs)
            ready = {'status': 'PASS', 'cli_version': '0.7.4', 'events': {'snapshot_extraction': None, 'wheel_pip_install': None}}
            with patch.object(control, 'resolve_cli', return_value='fake-colab'), \
                 patch.object(control, 'preflight', return_value=ready), \
                 patch.object(control, 'load_adapter', return_value=(b'print(1)', ['measurement.json'], 'b'*64)), \
                 patch.object(control.subprocess, 'run', side_effect=subprocess_cli):
                r = control.run(args)
            self.assertEqual(r['error'], 'KERNEL_PROBE_FAILED')
            self.assertTrue(r['cleanup_confirmed'])
            probe = next(c for c in r['commands'] if c['operation'] == 'exec')
            self.assertEqual(probe['status'], 'TIMEOUT')
            self.assertGreater(probe['elapsed_seconds'], 0)

    def test_real_local_allocation_child_timeout_without_status_polling(self):
        # Only the sleeping Python child is real; every provider operation is fake.
        with tempfile.TemporaryDirectory() as temp:
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp,
                '--run-id', 'allocation-child-timeout', '--out', str(Path(temp)/'run'),
                '--driver', 'driver.py', '--artifacts', 'artifacts.json',
                '--task-seconds', '20', '--allocation-seconds', '4', '--cleanup-seconds', '3'])
            fake = FakeCLI(Clock())
            def subprocess_cli(argv, **kwargs):
                if 'new' in argv:
                    return REAL_RUN([sys.executable, '-c', 'import time; time.sleep(30)'], **kwargs)
                return fake(argv, **kwargs)
            ready = {'status': 'PASS', 'cli_version': '0.7.4', 'events': {'snapshot_extraction': None, 'wheel_pip_install': None}}
            with patch.object(control, 'resolve_cli', return_value='fake-colab'), \
                 patch.object(control, 'preflight', return_value=ready), \
                 patch.object(control, 'load_adapter', return_value=(b'print(1)', ['measurement.json'], 'b'*64)), \
                 patch.object(control.subprocess, 'run', side_effect=subprocess_cli):
                r = control.run(args)
            self.assertEqual(r['allocation_failure_scope'], 'CLI_SUBPROCESS_TIMEOUT')
            self.assertEqual(r['allocation_http_phase'], 'UNKNOWN')
            self.assertEqual([c['operation'] for c in r['commands']], ['usage', 'new', 'stop', 'usage', 'usage'])
            self.assertTrue(r['cleanup_confirmed'])
            self.assertFalse(r['created'])
            self.assertIsNone(r['events']['kernel_probe'])
            self.assertIsNone(r['events']['remote_workload'])

    def test_preflight_failure_keeps_timed_child_report(self):
        with tempfile.TemporaryDirectory() as temp:
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp, '--run-id', 'preflight-fail',
                                                '--out', str(Path(temp)/'run')])
            detail = {'status': 'FAIL', 'events': {'cli_version': {'status': 'FAIL', 'elapsed_seconds': 1}}}
            with patch.object(control, 'resolve_cli', return_value='fake'), \
                 patch.object(control, 'preflight', side_effect=PreflightError('PREFLIGHT_TIMEOUT', detail)):
                r = control.run(args)
            self.assertEqual(r['preflight'], detail)
            self.assertEqual(r['events']['environment_preflight']['status'], 'FAIL')
            self.assertEqual(r['commands'], [])

    def test_each_verified_type_requested_and_observed(self):
        for device in control.SUPPORTED_DEVICES:
            with self.subTest(device=device):
                r, fake = self.run_fake(extra=['--device',device])
                self.assertEqual(r['status'],'PASS')
                self.assertEqual(r['device_requested'],device)
                self.assertEqual(r['device_observed']['nvidia_smi'][0]['name'],'NVIDIA '+device)
                new = next(c for c,_ in fake.calls if c[0]=='new')
                self.assertEqual(new[new.index('--gpu')+1],device)

    def test_unknown_device_never_reaches_cli_fallback(self):
        r,fake=self.run_fake(extra=['--device','UNKNOWN'])
        self.assertEqual(r['error'],'UNSUPPORTED_DEVICE')
        self.assertEqual(fake.calls,[])

    def test_mismatch_requires_committed_literal_opt_in(self):
        r,fake=self.run_fake('mismatch')
        self.assertEqual(r['classification'],'DEVICE_MISMATCH')
        self.assertEqual(r['error'],'DEVICE_MISMATCH')
        self.assertEqual(sum(c[0]=='exec' for c,_ in fake.calls),1)
        self.assertTrue(r['cleanup_confirmed'])
        r,_=self.run_fake('mismatch',driver=b'SAE_ALLOW_DEVICE_MISMATCH = True\nprint(1)')
        self.assertEqual(r['status'],'PASS')
        self.assertEqual(r['classification'],'DEVICE_MISMATCH')
        self.assertEqual(r['device_observed']['nvidia_smi'][0]['name'],'NVIDIA A100')
        self.assertFalse(control.driver_allows_mismatch(b"print('SAE_ALLOW_DEVICE_MISMATCH = True')"))
        self.assertFalse(control.driver_allows_mismatch(b'SAE_ALLOW_DEVICE_MISMATCH = 1'))

    def test_strict_identity_and_optional_torch(self):
        data=identity()
        data['torch']=dict(status='AVAILABLE',version='2.11.0+cu130',cuda='13.0',name='Tesla T4',capability=[7,5])
        text='DEVICE_OBSERVED '+json.dumps(data)
        self.assertEqual(control.observed_device(text),data)
        for bad in ('',text+'\n'+text,'DEVICE_OBSERVED {}',
                    'DEVICE_OBSERVED {"nvidia_smi":[],"torch":{"status":"NOT_IMPORTABLE"}}'):
            with self.subTest(bad=bad),self.assertRaises(PreflightError):
                control.observed_device(bad)
        r,_=self.run_fake('missing-identity')
        self.assertEqual(r['error'],'DEVICE_IDENTITY_UNVERIFIED')
        self.assertTrue(r['cleanup_confirmed'])

    def test_kernel_script_reads_real_command_schema_without_torch_requirement(self):
        import kernel_smoke
        result=subprocess.CompletedProcess([],0,'Tesla T4, 15360 MiB, 580.82.07\n','')
        torch=SimpleNamespace(__version__='2.11.0',version=SimpleNamespace(cuda='13.0'),
            cuda=SimpleNamespace(is_available=lambda:True,get_device_name=lambda _: 'Tesla T4',
                                 get_device_capability=lambda _:(7,5)))
        with patch.object(kernel_smoke.subprocess,'run',return_value=result) as command, \
             patch.dict(sys.modules,{'torch':torch}):
            observed=kernel_smoke.observe()
        self.assertIn('--query-gpu=name,memory.total,driver_version',command.call_args.args[0])
        self.assertEqual(command.call_args.kwargs['timeout'],10)
        self.assertEqual(observed['torch']['capability'],[7,5])
        with patch.object(kernel_smoke.subprocess,'run',return_value=result),patch.dict(sys.modules,{'torch':None}):
            self.assertEqual(kernel_smoke.observe()['torch'],{'status':'NOT_IMPORTABLE'})

    def test_research_timeout_edges_and_nonfinite_values(self):
        r,_=self.run_fake(extra=['--task-seconds','14400','--allocation-seconds','10800',
            '--cleanup-seconds','60','--work-timeout','3600','--kernel-timeout','60','--preflight-only'])
        self.assertEqual(r['status'],'PREFLIGHT_PASS')
        for flag,value in (('--task-seconds','14401'),('--allocation-seconds','10801'),
                           ('--work-timeout','3601'),('--task-seconds','inf'),
                           ('--cleanup-seconds','nan'),('--kernel-timeout','0')):
            with self.subTest(flag=flag,value=value):
                r,fake=self.run_fake(extra=[flag,value])
                self.assertEqual(r['error'],'INVALID_TIMEOUT_BOUNDS')
                self.assertEqual(fake.calls,[])

    def test_post_cleanup_consumption_and_failed_readback(self):
        r,_=self.run_fake('post-balance')
        self.assertEqual(r['balance_before'],10.)
        self.assertEqual(r['balance_after'],9.75)
        self.assertEqual(r['balance_delta'],.25)
        self.assertEqual(r['assignments_after'],0)
        self.assertEqual(r['readbacks'][-1]['phase'],'post_cleanup')
        r,_=self.run_fake('post-unverified')
        self.assertEqual(r['status'],'POST_RUN_READBACK_FAILED')
        self.assertTrue(r['cleanup_confirmed'])
        self.assertNotIn('balance_after',r)

    def test_multiple_types_refusal_continues_but_uncertain_cleanup_stops(self):
        for failure in ('refuse-L4','cleanup','interrupt'):
            with self.subTest(failure=failure),tempfile.TemporaryDirectory() as temp:
                args=control.parser().parse_args(['--source-sha',SHA,'--repo-path',temp,'--run-id','multi',
                    '--out',str(Path(temp)/'runs'),'--driver','driver.py','--artifacts','artifacts.json',
                    '--devices','T4,L4,A100','--task-seconds','100','--allocation-seconds','80','--cleanup-seconds','20'])
                clock=Clock(); fake=FakeCLI(clock,failure)
                ready={'status':'PASS','cli_version':'0.7.4','events':{'snapshot_extraction':None,'wheel_pip_install':None}}
                with patch.object(control,'resolve_cli',return_value='fake'), \
                     patch.object(control,'preflight',return_value=ready), \
                     patch.object(control,'load_adapter',return_value=(b'print(1)',['measurement.json'],'b'*64)), \
                     patch.object(control.subprocess,'run',side_effect=fake), \
                     patch.object(control.time,'monotonic',side_effect=clock):
                    result=control.run_many(args)
                if failure=='refuse-L4':
                    self.assertEqual(result['status'],'PARTIAL')
                    self.assertEqual(len(result['runs']),3)
                    self.assertTrue(result['runs'][1]['classification'].startswith('BLOCKED_PROVIDER:L4:'))
                    self.assertTrue(all(r['cleanup_confirmed'] for r in result['runs']))
                    self.assertEqual(result['runs'][2]['status'],'PASS')
                elif failure=='cleanup':
                    self.assertEqual(result['status'],'CLEANUP_OR_READBACK_FAILED')
                    self.assertEqual(len(result['runs']),1)
                    self.assertEqual(result['not_run'],['L4','A100'])
                else:
                    self.assertEqual(result['status'],'INTERRUPTED')
                    self.assertEqual(len(result['runs']),1)
                    self.assertTrue(result['runs'][0]['cleanup_confirmed'])
                    self.assertEqual(result['not_run'],['L4','A100'])


if __name__ == '__main__':
    unittest.main()
