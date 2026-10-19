# Colab Three-Step Contract — Install, Benchmark, Optional Publish

> English (normative) | [简体中文](../i18n/zh-CN/workflows/COLAB_TWO_COMMAND.md)

**Compatibility:** the historical file name `COLAB_TWO_COMMAND.md` remains for existing links and pinned project snapshots. The **current workflow has three independent notebook cells**, the third optional. This defines a future packaged CLI interface; it does **not** prove that the commands or Publisher already exist.

## Scientist's three cells (illustrative; replace placeholders)

```python
!pip install "git+https://github.com/OWNER/REPO.git@EXACT_SOURCE_COMMIT_SHA"
!python -m PACKAGE_NAME.benchmarks.run --device cuda --out reports/gpu/RUN_ID
!python -m PACKAGE_NAME.benchmarks.publish --report-dir reports/gpu/RUN_ID
```

- **Install:** pin exact immutable source SHA, not a floating branch; use the real pip-installable import package.
- **Benchmark:** verify source SHA, runtime and reference correctness; perform accurate warmup/synchronized timings; save locally to a unique path. **Never require a GitHub token or publish from benchmark.**
- **Publish, optional:** Scientist first inspects numerical evidence, timings, and selected path; third cell reads **only that existing report**, never reruns GPU. It may create a sanitized, allowlisted experiment branch/PR but never push to main or auto-merge.

The Publisher must support the explicit `--report-dir` argument. The run directory must contain `manifest.json`, `correctness.json`, `benchmark.csv`, `summary.md`, with matching full tested SHA. Benchmark status (`BENCHMARK_PASS`/`BENCHMARK_FAIL`/`NOT_RUN`) and publication status (`PUBLISHED`/`PUBLISH_FAILED`/`PUBLISH_BLOCKED`/`NOT_REQUESTED`) are independent; a failure cannot be reported as success. Reject oversized, private, secret-containing or malformed reports; publishing is idempotent and verifies the returned PR. Failure must preserve local reports.

## `GITHUB_TOKEN` in Colab Secrets (not a token value)

The Scientist has configured a Colab Secret named **`GITHUB_TOKEN`**; notebook access must be enabled. **`!python` subprocesses are not guaranteed to inherit Colab Secrets.** The short third line is only valid once real Colab subprocess retrieval is verified. Otherwise replace that **one third cell** with:

```python
from google.colab import userdata
import os, subprocess
subprocess.run(
    ["python", "-m", "PACKAGE_NAME.benchmarks.publish",
     "--report-dir", "reports/gpu/RUN_ID"],
    env={**os.environ, "GITHUB_TOKEN": userdata.get("GITHUB_TOKEN")},
    check=True,
)
```

Never print a token or interpolate it into `!export`, shell commands, process arguments, Git URLs or reports. The Publisher should prefer least-privilege fine-grained **Contents / Pull requests read-write** access to the **target repository**. A public PR is publicly visible.

## Acceptance and ownership

**Architect** writes exact CLI, version, run-ID, oracle/benchmark spec and acceptance tests into an Issue. **Codex** implements independent packaged run/publish modules, offline Publisher failure/idempotency tests, real CPU/clean-install CLI smoke tests and honest error propagation. **Scientist** runs GPU experiments and separately authorizes a specific report upload; checks real Secret accessibility and report PR in Colab. No role may claim `GPU_VERIFIED` or `PUBLISHED` without the actual source-matched evidence.

See [GPU Experiment](GPU_EXPERIMENT.md) for experiment gates and report evidence. No GitHub Actions, no Drive report sync, no notebook numerical kernel, no CPU-to-GPU shortcut.
