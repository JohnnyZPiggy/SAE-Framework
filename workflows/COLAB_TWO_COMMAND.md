# Three-Step Colab Contract — Install, Benchmark, Publish

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/COLAB_TWO_COMMAND.md)  
> Compatibility note: this file keeps its historical path so existing links and pinned snapshots do not break. The current contract is **three independent steps**, not two commands.

## Scientist's approved notebook workflow

After selecting a GPU runtime and enabling a Colab Secret named **`GITHUB_TOKEN`** (one-time), the notebook has **three separate execution cells**:

```python
!pip install "git+https://github.com/OWNER/REPO.git@<EXACT_SOURCE_COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>
!python -m <package>.benchmarks.publish --report-dir reports/gpu/<run-id>
```

These are **target CLI examples, not evidence of currently implemented commands**. The Architect/Codex must supply a real importable package, pinned 40-character source SHA and deterministic run path (or the explicit path returned by the benchmark). The third command is **optional**: the Scientist inspects the generated accuracy/performance report first and runs publish only if they choose to upload. Benchmark runs with **no GitHub token requirement** and **no GitHub writes**. The explicit publish command authorizes creating a sanitized report **branch and PR**, not merging to main. Do not mix publishing into the benchmark command or require `--publish` in the default path.

## Secure Colab Secret bridge — crucial subprocess rule

The Scientist has named the **Colab Secrets** entry `GITHUB_TOKEN`. It is a *name*, not a token value; never print, copy or commit the secret. Give the notebook access to this secret in Colab's key sidebar.

**Colab Secrets are not guaranteed to be inherited as process environment variables by `!python` subprocesses.** Codex must implement and test a safe bridge for the publish step:

- Preferred *only if proven in a real Colab subprocess*: the packaged publisher retrieves `google.colab.userdata.get("GITHUB_TOKEN")` securely at runtime, without echoing the value.
- **Required fallback** if subprocess retrieval is unavailable: use one small Python upload cell (still the **third step**) to inject the Secret into the child process environment **without shell interpolation**:

```python
from google.colab import userdata
import os, subprocess
subprocess.run(
    ["python", "-m", "<package>.benchmarks.publish", "--report-dir", "reports/gpu/<run-id>"],
    env={**os.environ, "GITHUB_TOKEN": userdata.get("GITHUB_TOKEN")},
    check=True,
)
```

Never use `!export GITHUB_TOKEN=...`, `!echo`, token literals in shell command strings, printed environment dumps, or tokens in URL arguments. Treat the multiline fallback as **one publication cell**, not additional user-operated workflow stages. Do not promise the shorter `!python` line works until actually verified.

## Clear separation and report contract

- **Install:** fail fast if the exact candidate source commit cannot be installed. A floating branch/tag is not a reproducible benchmark target.
- **Benchmark:** preflight GPU/device and source SHA → oracle correctness → warmup/synchronized timings → write `manifest.json`, `correctness.json`, `benchmark.csv`, `summary.md` in a unique `reports/gpu/<run-id>/`. Never automatically publish or retry GPU experiments.
- **Publish:** read exactly the Scientist-selected existing report directory; do **not rerun benchmarks**. Validate schema, tested SHA and allowlisted files; reject secrets/oversize/private data; create an idempotent experiment branch and GitHub PR. Never force-push, auto-merge, overwrite a prior run or push reports directly to main.
- Record **separate states**: `BENCHMARK_PASS / BENCHMARK_FAIL / NOT_RUN` and `PUBLISHED / PUBLISH_FAILED / PUBLISH_BLOCKED / NOT_REQUESTED`. A failed correctness check is never described as a successful speedup, even if diagnostic reporting is intentionally authorized. A returned URL alone is not proof of PR creation until GitHub confirms it.
- The publisher should require a **fine-grained token scoped to the chosen repository**, with the least permissions needed (typically repository Contents: read/write and Pull requests: read/write; Issues only if commenting is part of the approved workflow). A public repository's draft PR is still public. Keep the token private and rotate it if exposed.

## Responsibilities and acceptance

**Architect:** specify package/CLIs, run path, numerical oracle/tolerances, CPU/GPU presets, evidence schema, selected publish payload, failure propagation and GitHub rights in the Codex Issue. Align Notebook instructions to three steps; keep the benchmark independent of publication.

**Codex:** implement and package the independent `benchmarks.run` and `benchmarks.publish` Python modules. Validate clean pinned-SHA pip install, CPU oracle/edge tests and CLI smoke runs; offline/mocked Publisher tests for token missing, refusal/permissions, retries/idempotence, invalid report and no unexpected network writes; then request Scientist's real Colab integration check. Never claim a GPU or Colab-secret subprocess test was run without evidence.

**Scientist:** manually selects GPU, launches benchmark, checks numerical/performance evidence, then **optionally** runs the third upload cell with the Colab `GITHUB_TOKEN` Secret. Reviews the report PR before any merge.

**Status until implemented/tested:** `PUBLISHER_NOT_IMPLEMENTED` or `PUBLISH_UNVERIFIED`; defining a protocol does not enable upload. No GitHub Actions, Drive report syncing, notebook numerical kernels or machine-specific mandatory CUDA implementation.

See [GPU Experiment](GPU_EXPERIMENT.md) and [Thin Colab Example](../examples/colab/README.md).
