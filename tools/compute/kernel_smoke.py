# SPDX-License-Identifier: MIT
# Copyright (c) 2026 JohnnyZPiggy
"""Observe hardware only; no install, tensor workload or provider API."""
import csv
import io
import json
import re
import subprocess


def observe():
    result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total,driver_version',
                             '--format=csv,noheader'], capture_output=True, text=True,
                            check=True, timeout=10)
    devices = []
    for row in csv.reader(io.StringIO(result.stdout)):
        if len(row) != 3:
            raise ValueError('NVIDIA_SMI_SCHEMA_INVALID')
        name, memory, driver = (value.strip() for value in row)
        match = re.fullmatch(r'(\d+) MiB', memory)
        if not name or not driver or not match:
            raise ValueError('NVIDIA_SMI_SCHEMA_INVALID')
        devices.append(dict(name=name, memory_total_mib=int(match[1]), driver_version=driver))
    info = {'status': 'NOT_IMPORTABLE'}
    try:
        import torch
    except ImportError:
        pass
    else:
        info = dict(status='AVAILABLE' if torch.cuda.is_available() else 'CUDA_UNAVAILABLE',
                    version=str(torch.__version__), cuda=torch.version.cuda,
                    name=torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
                    capability=list(torch.cuda.get_device_capability(0)) if torch.cuda.is_available() else None)
    return dict(nvidia_smi=devices, torch=info)


if __name__ == '__main__':
    print('KERNEL_REACHABLE', flush=True)
    print('DEVICE_OBSERVED '+json.dumps(observe(), separators=(',', ':'), allow_nan=False), flush=True)
