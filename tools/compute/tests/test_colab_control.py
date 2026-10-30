# SPDX-License-Identifier: MIT
# Copyright (c) 2026 JohnnyZPiggy
"""Required controller behavior, using a local FakeCLI only."""
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
SHA = 'a' * 40


class FakeCLI:
    def __init__(self, failure=None, name='NVIDIA T4'):
        self.failure, self.name = failure, name
        self.calls, self.active = [], False
        self.raw = json.dumps(dict(source_sha=SHA, status='PASS')).encode()

    def __call__(self, argv, **kwargs):
        cmd = argv[argv.index('--auth=oauth2') + 1:]
        self.calls.append(cmd)
        op, code, output = cmd[0], 0, ''
        if op == 'usage':
            count = int(self.active or self.failure == 'existing')
            output = ('Current balance: 10.00 compute units\nUsage rate: 0.00/hr\n'
                      f'Active assignments: {count}\n')
        elif op == 'new':
            assert not self.active, 'overlapping sessions'
            self.active = True
        elif op == 'exec':
            if cmd[cmd.index('-f')+1].endswith('kernel_smoke.py'):
                observed = dict(nvidia_smi=[dict(name=self.name)], torch=dict(status='NOT_IMPORTABLE'))
                output = 'KERNEL_REACHABLE\nDEVICE_OBSERVED '+json.dumps(observed)+'\n'
            elif self.failure == 'interrupt':
                raise KeyboardInterrupt()
            elif self.failure == 'work':
                code = 1
        elif op == 'download':
            Path(cmd[-1]).write_bytes(self.raw)
        elif op == 'stop':
            self.active = False
        else:
            raise AssertionError(op)
        return subprocess.CompletedProcess(argv, code, output, 'token=secret https://private.invalid')


class ControllerTests(unittest.TestCase):
    def run_fake(self, failure=None, name='NVIDIA T4', extra=()):
        with tempfile.TemporaryDirectory() as temp:
            args = control.parser().parse_args(['--source-sha', SHA, '--repo-path', temp,
                '--run-id', 'test-run', '--out', str(Path(temp)/'run'), '--driver', 'driver.py',
                '--artifacts', 'artifacts.json', *extra])
            fake = FakeCLI(failure, name)
            with patch.object(control, 'resolve_cli', return_value='/verified/colab'), \
                 patch.object(control, 'preflight', return_value=dict(cli_version='0.7.4')), \
                 patch.object(control, 'load_adapter', return_value=(b'print(1)', ['measurement.json'])), \
                 patch.object(control.subprocess, 'run', side_effect=fake):
                result = control.run(args)
            self.assertEqual(json.loads((args.out/'colab-control.json').read_text()), result)
            self.assertNotIn('secret', json.dumps(result))
            self.assertNotIn('private.invalid', json.dumps(result))
            return result, fake

    def test_happy_path(self):
        r, fake = self.run_fake()
        self.assertEqual(r['status'], 'PASS')
        self.assertTrue(r['cleanup_confirmed'])
        self.assertEqual(r['assignments_after'], 0)
        self.assertEqual([c[0] for c in fake.calls],
                         ['usage', 'new', 'exec', 'exec', 'download', 'stop', 'usage'])
        self.assertTrue(fake.calls[2][fake.calls[2].index('-f')+1].endswith('kernel_smoke.py'))
        work = fake.calls[3]
        for value in ('SAE_CANDIDATE_SHA='+SHA, 'SAE_DEVICE_REQUESTED=T4'):
            self.assertIn(value, work)
        self.assertTrue(any(x.startswith('SAE_DEVICE_OBSERVED=') for x in work))
        self.assertEqual(r['artifact_sha256']['measurement.json'], hashlib.sha256(fake.raw).hexdigest())

    def test_work_failure_cleans_up(self):
        r, fake = self.run_fake('work')
        self.assertEqual(r['error'], 'WORK_EXEC_FAILED')
        self.assertEqual(r['status'], 'FAIL')
        self.assertTrue(r['cleanup_confirmed'])
        self.assertEqual([c[0] for c in fake.calls][-2:], ['stop', 'usage'])

    def test_existing_assignment_blocks_allocation(self):
        r, fake = self.run_fake('existing')
        self.assertEqual(r['error'], 'EXISTING_OR_UNKNOWN_SESSIONS')
        self.assertEqual([c[0] for c in fake.calls], ['usage'])

    def test_interrupt_cleans_up(self):
        r, fake = self.run_fake('interrupt')
        self.assertEqual(r['error'], 'INTERRUPTED')
        self.assertTrue(r['cleanup_confirmed'])
        self.assertEqual([c[0] for c in fake.calls][-2:], ['stop', 'usage'])

    def test_device_families_and_explicit_override(self):
        for name, extra, status in (
            ('NVIDIA RTX PRO 6000 Blackwell', ('--device', 'G4'), 'PASS'),
            ('NVIDIA A100', (), 'BLOCKED'),
            ('NVIDIA A100', ('--allow-device-mismatch',), 'PASS')):
            with self.subTest(name=name, extra=extra):
                r, fake = self.run_fake(name=name, extra=extra)
                self.assertEqual(r['status'], status)
                self.assertTrue(r['cleanup_confirmed'])
                self.assertEqual(r['device_observed']['nvidia_smi'][0]['name'], name)
                if status == 'BLOCKED':
                    self.assertEqual(sum(c[0] == 'exec' for c in fake.calls), 1)


if __name__ == '__main__':
    unittest.main()
