# SPDX-License-Identifier: MIT
# Copyright (c) 2026 JohnnyZPiggy
"""Exact project adapter and safe manifest tests, with local Git only."""
import json
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from colab_control import load_adapter
from environment_preflight import PreflightError


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'core.autocrlf', 'false')
        (self.repo/'driver.py').write_bytes(b"print('PROJECT_FIXTURE')\n")
        self.pin({'artifacts': [{'name': 'measurement.json'}]})

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args],
                              capture_output=True, check=True).stdout.decode().strip()

    def pin(self, data):
        (self.repo/'artifacts.json').write_bytes(json.dumps(data).encode())
        self.git('add', 'driver.py', 'artifacts.json')
        self.git('-c', 'user.name=Local test', '-c', 'user.email=test@example.invalid',
                 'commit', '-qm', 'adapter', '--allow-empty')
        self.sha = self.git('rev-parse', 'HEAD')

    def load(self, driver='driver.py', manifest='artifacts.json', sha=None):
        return load_adapter(self.repo, sha or self.sha, driver, manifest)

    def test_pinned_files_ignore_dirty_adapter_and_manifest(self):
        (self.repo/'driver.py').write_bytes(b'changed\r\n')
        (self.repo/'artifacts.json').write_bytes(b'not JSON')
        driver, names = self.load()
        self.assertEqual(driver, b"print('PROJECT_FIXTURE')\n")
        self.assertEqual(names, ['measurement.json'])

    def test_unsafe_adapter_paths_rejected(self):
        for name in ('../driver.py', '/tmp/driver.py', 'C:/driver.py', 'dir\\driver.py'):
            with self.subTest(name=name), self.assertRaisesRegex(PreflightError, 'UNSAFE_ADAPTER_PATH'):
                self.load(driver=name)

    def test_symlink_blob_is_not_an_executable_adapter(self):
        blob = subprocess.run(['git', '-C', str(self.repo), 'hash-object', '-w', '--stdin'],
                              input=b'driver.py', capture_output=True, check=True).stdout.decode().strip()
        self.git('update-index', '--add', '--cacheinfo', '120000,' + blob + ',link.py')
        self.git('-c', 'user.name=Local test', '-c', 'user.email=test@example.invalid',
                 'commit', '-qm', 'symlink fixture')
        self.sha = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(PreflightError, 'ADAPTER_BLOB_INVALID'):
            self.load(driver='link.py')

    def test_example_runs_locally_without_provider(self):
        example = Path(__file__).resolve().parents[3] / 'examples/compute_adapter/driver.py'
        target = self.repo / 'local-artifacts'
        result = subprocess.run([sys.executable, str(example)], capture_output=True, text=True, check=True,
                                env=dict(os.environ, SAE_CANDIDATE_SHA=self.sha, SAE_ARTIFACT_DIR=str(target)), timeout=10)
        raw = (target / 'transport-check.json').read_bytes()
        data = json.loads(raw)
        self.assertEqual(data['source_sha'], self.sha)
        self.assertEqual(data['live_gpu'], 'NOT_RUN')
        self.assertIn(hashlib.sha256(raw).hexdigest(), result.stdout)


if __name__ == '__main__':
    unittest.main()
