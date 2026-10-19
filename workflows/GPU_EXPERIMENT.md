# GPU Experiment and Three-Step Colab Contract

> English normative | [简体中文](../i18n/zh-CN/workflows/GPU_EXPERIMENT.md)

## Scope and readiness

**Scientist operates Colab.** Architect must first validate the mathematical study and Codex's actual CPU oracle/edge tests, `torch.compile` where applicable, reproducible CPU benchmark, pinned-SHA clean install and packaged CLI smoke run. Record `GPU_READY` only after reviewing those facts and [GPU Readiness](../templates/GPU_READINESS.md); do not equate CPU success with GPU verification.

## Three independent Colab cells — target, not proof of implementation

Use an enabled GPU runtime and a notebook-authorized Colab Secrets entry named **`GITHUB_TOKEN`**. Architect/Codex replace placeholders with the **actual package, tested full commit SHA and known report run path**:

```python
!pip install "git+https://github.com/OWNER/REPO.git@<EXACT_SOURCE_COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>
!python -m <package>.benchmarks.publish --report-dir reports/gpu/<run-id>
```

1. **Install** an exact immutable source SHA; no floating main/tag or unverified local code.
2. **Benchmark** numerical correctness first, then actual GPU timing with warmup and device synchronization as appropriate. Benchmark generates local reports only; **no GitHub token or write operation**. Run status is independent of publication.
3. **Publish (OPTIONAL)** only after Scientist reviews the accuracy, benchmark results, files and public-disclosure risks. Publisher consumes the **existing** selected report directory; it must **not rerun GPU**, cannot overwrite another run or write directly to main, and only creates a separate branch/PR. Architect later reviews the PR according to [Standing Authorization](../governance/STANDING_AUTHORIZATION.md); there is no automatic merge.

These are **contract examples**, not evidence that `benchmarks.run` or `benchmarks.publish` currently exists or has passed a real Colab integration test. Codex must implement and test both independently.

## Colab Secrets bridge — subprocess nuance

**The Secret name is `GITHUB_TOKEN`, not the token itself.** Enable this secret for the Colab notebook. A `!python` child process is *not guaranteed* to receive Colab Secrets as an environment variable. The one-line third command works **only after Scientist confirms a real integration path** (e.g. packaged publisher reads `google.colab.userdata.get("GITHUB_TOKEN")` securely from the subprocess).

If subprocess retrieval is unsupported, use **one Python upload cell** as the third step (not an extra stage):

```python
from google.colab import userdata
import os, subprocess
subprocess.run(
    ["python", "-m", "<package>.benchmarks.publish", "--report-dir", "reports/gpu/<run-id>"],
    env={**os.environ, "GITHUB_TOKEN": userdata.get("GITHUB_TOKEN")},
    check=True,
)
```

Never paste a token literal into code, URLs, shell strings, commands or logs; never print credentials or environment dumps. Use a fine-grained GitHub token limited to the chosen repository, with minimally required Contents and Pull requests write permissions. Public PR reports are visible even before merge. Publisher tests must safely redact all errors.

## Small, reproducible evidence contract

Each actual run uses a unique `reports/gpu/<run-id>/` with **only**:

| File | Purpose |
| --- | --- |
| `manifest.json` | Exact algorithm/source commit SHA, device, PyTorch/Python/version, dtype, seed, configuration, run ID |
| `correctness.json` | Numerical oracle, error metrics/tolerances, PASS/FAIL and failures |
| `benchmark.csv` | Observed timing samples and baselines, synchronization/warmup metadata |
| `summary.md` | Honest interpretation, limits, and reviewed experiment links |

Do not infer CUDA speedup from CPU tests, compare mismatched precision without disclosure, or report numerical mismatch as a verified speedup. The Publisher must validate this allowlist, schema, exact tested SHA, file size, secret/PII disclosure, run-unique branch, related Issue/PR and idempotency before opening a public experiment PR. Never force-push, auto-merge, re-run GPU, or secretly retry until a success appears.

**Separate status families:** `BENCHMARK_PASS / BENCHMARK_FAIL / NOT_RUN` and `PUBLISHED / PUBLISH_FAILED / PUBLISH_BLOCKED / NOT_REQUESTED`. Keep generated reports local if publication fails; failure must propagate and no GitHub success can be claimed before it is confirmed.

## Role acceptance

- **Mentor / Scientist:** mathematical formulation and oracle; Scientist runs and verifies real Colab results and chooses if/when to upload.
- **Architect:** supplies exact SHA, package/CLI, run path, oracle tolerances, device/dtype and measurement presets; checks CPU readiness, reviews returned evidence and the publication PR.
- **Codex:** implements independent packaged run/publish CLIs, deterministic CPU tests and mocked Publisher failure/idempotency/security tests. Real Colab Secret-subprocess and GPU behavior require Scientist integration evidence.

**No new standalone artifact beyond the three linked research outputs; no GitHub Actions; no Drive report synchronization or vendor-specific mandatory kernel.** See [Three-Artifact Handoff](THREE_ARTIFACT_HANDOFF.md) and [Task Management](TASK_MANAGEMENT.md).
