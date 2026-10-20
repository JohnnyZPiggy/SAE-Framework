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
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import colab_control as control
from environment_preflight import PreflightError

SHA = 'a' * 40
ZERO = 'No active sessions found on server.'
REAL_RUN = subprocess.run


class Clock:
    def __init__(self):
        self.now = 0

    def __call__(self):
        return self.now


class FakeCLI:
    def __init__(self, clock, failure=None):
        self.clock, self.failure = clock, failure
        self.calls = []
        self.active = False
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
        if op == 'sessions':
            output = 'unrelated active session' if self.failure == 'existing' or self.active else ZERO
        elif op == 'usage':
            output = ('Current balance: 0 compute units\nActive assignments: 0' if self.failure == 'quota'
                      else 'Current balance: 10 compute units\nActive assignments: 0')
        elif op == 'new':
            self.active = True
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
                output = 'KERNEL_REACHABLE\n'
            else:
                output = '\n'.join(f'ARTIFACT {n} {len(raw)} {hashlib.sha256(raw).hexdigest()}'
                                   for n, raw in self.artifacts.items())
        elif op == 'download':
            name = Path(cmd[-2]).name
            Path(cmd[-1]).write_bytes(b'bad' if self.failure == 'hash' else self.artifacts[name])
        elif op == 'stop':
            if self.failure == 'cleanup':
                self.clock.now += kwargs['timeout']
                raise subprocess.TimeoutExpired(argv, kwargs['timeout'])
            self.active = False
        else:
            raise AssertionError(op)
        return subprocess.CompletedProcess(argv, code, output + '\n', 'secret path /home/private/oauth https://private.invalid token=secret')


class ControllerTests(unittest.TestCase):
    def run_fake(self, failure=None, extra=()):
        with tempfile.TemporaryDirectory() as temp:
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp, '--run-id', 'test-run',
                 '--out', str(Path(temp) / 'new-run'), '--driver', 'driver.py', '--artifacts', 'artifacts.json', '--task-seconds', '100',
                 '--allocation-seconds', '80', '--cleanup-seconds', '20',
                 '--work-timeout', '100', *extra])
            clock = Clock()
            fake = FakeCLI(clock, failure)
            ready = {'status': 'PASS', 'events': {'snapshot_extraction': None, 'wheel_pip_install': None}}
            with patch.object(control, 'resolve_cli', return_value='/verified/colab'), \
                 patch.object(control, 'preflight', return_value=ready), \
                 patch.object(control, 'load_adapter', return_value=(b'print(1)', ['measurement.json'], 'b'*64)), \
                 patch.object(control.subprocess, 'run', side_effect=fake), \
                 patch.object(control.time, 'monotonic', side_effect=clock):
                result = control.run(args)
            saved = json.loads((args.out / 'colab-control.json').read_text())
            self.assertEqual(saved, result)
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
        self.assertEqual([c[0] for c, _ in fake.calls], ['sessions', 'usage', 'new', 'stop', 'sessions'])
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
        self.assertEqual([c[0] for c, _ in fake.calls], ['sessions'])

    def test_quota_blocks_allocation(self):
        r, fake = self.run_fake('quota')
        self.assertEqual(r['error'], 'ENTITLEMENT_NOT_ESTABLISHED')
        self.assertNotIn('new', [c[0] for c, _ in fake.calls])

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
            ready = {'status': 'PASS', 'events': {'snapshot_extraction': None, 'wheel_pip_install': None}}
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
            ready = {'status': 'PASS', 'events': {'snapshot_extraction': None, 'wheel_pip_install': None}}
            with patch.object(control, 'resolve_cli', return_value='fake-colab'), \
                 patch.object(control, 'preflight', return_value=ready), \
                 patch.object(control, 'load_adapter', return_value=(b'print(1)', ['measurement.json'], 'b'*64)), \
                 patch.object(control.subprocess, 'run', side_effect=subprocess_cli):
                r = control.run(args)
            self.assertEqual(r['allocation_failure_scope'], 'CLI_SUBPROCESS_TIMEOUT')
            self.assertEqual(r['allocation_http_phase'], 'UNKNOWN')
            self.assertEqual([c['operation'] for c in r['commands']], ['sessions', 'usage', 'new', 'stop', 'sessions'])
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


if __name__ == '__main__':
    unittest.main()
