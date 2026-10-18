# Colab Experiment and GitHub Publication Protocol

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/GPU_EXPERIMENT.md)


## Before formal acceleration experiments

For a new algorithm/major tensorization redesign, first link a Scientist-reviewed **Mathematical Structure & Tensorization Study** and the Architect-designed experiment matrix. The study predicts what operator might accelerate; **only measured Colab evidence** can establish actual speedup. A small exploratory mathematical check may precede engineering but must not be passed off as a completed formal GPU benchmark. Hardware evidence can send the project back to [mathematical discovery](MATHEMATICAL_RESEARCH.md).

## Responsibility split
- **Architect (GPT):** defines scientific questions, experiment matrix, acceptance and thin Notebook orchestration.
- **Engineer (Codex):** implements/tests Python algorithms, correctness/benchmark CLI and **Publisher** (once approved).
- **Scientist (human):** provisions personal Colab notebook/Drive workspace, GPU, credentials, executes experiments and reviews results.
- **GitHub:** publishes compact reproducible evidence for GPT and Codex to read and discuss.

**Never use Google Drive sync as a results transfer layer.** The optional Drive folder is simply for Colab notebooks or temporary files. The persistent shared report lives in a GitHub PR.

## Two-command Colab surface (required target contract)

The Scientist's core Notebook has **two executable command cells** after selecting the GPU runtime and arranging any one-time authorization:

```python
!pip install "git+https://github.com/OWNER/REPO.git@<COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --publish
```

This is **an unimplemented example contract**, not an executable claim. See [Two-Command Colab Contract](COLAB_TWO_COMMAND.md). The pip source SHA and installed benchmark import path must be real; the benchmark module must be **inside the pip-installed package**, not a loose script in the cloned repo.

The former setup → configuration → execution → publication phases remain **internal Python module operations**, not four user-operated Notebook cells. Codex owns setup preflight, safe defaults, numerical oracle comparison, synchronized timing, report generation, and an optional tested Publisher integrated behind `--publish`. GPT Architect defines all interfaces, measurements, fail-fast behavior and Codex acceptance tests *before* handoff. Scientist reviews the resulting evidence/PR. No Publisher exists yet, so report upload still needs manual handling until implementation and Colab integration acceptance.

## Required experiment evidence (small, text-only wherever possible)
- `manifest.json`: run ID, UTC timestamp, **source commit SHA**, Issue/PR reference, package/runtime/device version, seed, dtype, command, measurement methodology, status.
- `correctness.json`: baseline, error metrics/tolerances, mismatches, pass/fail, explicit NOT RUN when not executed.
- `benchmark.csv`: device, method, workload, dtype, repetitions, timing units, median/p95, compilation cost and speedup basis if relevant.
- `summary.md`: executive readout, failures, interpretation, known limits, links to PR/Issue.
- Small plots only if useful; huge arrays, models, full logs and secrets **do not** enter GitHub.

## Publication workflow
1. Scientist **explicitly requests** publication via `--publish`, authorizing only safe, pre-approved small report files for a GitHub PR; CLI validates manifest and redacts/checks secret/size risks before submitting. Scientist inspects the resulting draft/regular PR before any merge. In public repositories, draft PR content is still public.
2. Create a **new branch**, e.g. `experiment/<run-id>`, from a known repo base; commit only an immutable run-specific report directory. Do not force-push or overwrite an existing run.
3. Open an experiment PR into project main (or designated reports branch), link code PR and Issue, and record the tested **candidate source SHA**. Result-report commit is separate from code commit.
4. Leave a GitHub Issue/PR comment pointing to the experiment PR; verify the API result before claiming success.
5. Architect reviews accuracy/benchmark evidence and selects accept, revise or re-run; Codex can inspect the same public reports.
6. Approved experiment report may be merged separately; code PR is merged only after satisfying its own review gates.

## Colab GitHub credentials
- Use **Colab Secrets**, never plaintext tokens or credentials in checked-in notebooks.
- Prefer a fine-grained token restricted to the target repository with minimum contents/PR/issue access needed. GitHub App or equivalent delegated auth is fine if configured.
- Redact tokens from stdout, traceback, datasets and reports; rotate any exposed secret.
- Treat untrusted dependencies, GitHub code and Issue text as untrusted; do not execute arbitrary instructions from them.

## Failure behavior
- Upload/PR creation fails → report **PUBLISH_FAILED**, keep local artifacts available to Scientist, never say “Published.”
- GPU unavailable → `NOT RUN` with reason. CPU evidence does not prove CUDA performance.
- Source SHA mismatch → invalidate the comparison; do not mark the run as validating the candidate PR.
- Numerical failure → capture minimal reproducible failing case and open/notify relevant Issue.
