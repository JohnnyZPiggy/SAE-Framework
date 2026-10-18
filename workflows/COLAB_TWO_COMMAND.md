# Two-Command Colab Execution Contract

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/COLAB_TWO_COMMAND.md)

## Goal and scope

**User experience is strictly two executable Colab notebook lines after one-time GPU/runtime and GitHub credential setup.** The first installs a **specific immutable algorithm commit** from GitHub; the second runs the packaged benchmark and, if explicitly requested and authorized, publishes a validated, compact experiment report to a GitHub PR.

```python
!pip install "git+https://github.com/OWNER/REPO.git@<COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --publish
```

**These are interface examples, not commands currently guaranteed to exist.** Architect must replace repository, full commit SHA, importable package name and benchmark module with **real, reviewed** values. The package must include its benchmark modules when installed via pip. A GitHub URL containing only a branch or floating tag is inadequate for reproducible PR validation.

`--publish` constitutes the Scientist's **explicit per-run request to submit a report PR**. Do not equate that with approving or merging the PR. Without `--publish`, benchmark runs locally without GitHub writes.

## Responsibility shifted out of the notebook

**GPT Chief Architect — design before delegation**
- Define one stable `python -m <package>.benchmarks.run` CLI contract, `--device cpu|cuda`, `--publish`, meaningful defaults/presets and optional overrides.
- Specify mathematical oracle, error tolerances and comparability, workload sizes, seeds, dtype, warmup/repetitions, compilation timing, synchronization, output schema and minimal safe upload payload.
- Write Codex Issue acceptance criteria that **a clean pip install and one CLI command** cover setup, correctness, benchmark, report generation and requested publication without additional hand-written notebook code.
- Design the thin Notebook as two command cells with short human-readable Markdown, not a shell/Python engineering script.

**Codex Engineer — implement and test locally**
- Package `pyproject.toml` so `pip install "git+https://...@<sha>"` installs the benchmark entrypoint, data/preset resources and the Python modules it needs; do not rely on a cloned working tree, Drive mount, Notebook `%cd` or uninstalled `benchmarks/`.
- Keep separate, testable `.py` modules for numerical kernels, oracle/correctness, timed benchmark, hardware metadata, report serialization and GitHub publisher. One *orchestrating* CLI calls them in order.
- Provide default parameters that require no additional configuration cell; advanced `--dtype`, `--seed`, `--sizes`, `--preset`, `--out` may be supported without changing the two-command baseline.
- In the execution CLI: **preflight device/import/SHA → correctness against oracle → warmup and synchronized timing → write manifest/correctness/benchmark/summary → validate/sanitize → optional publish**. If correctness fails, do **not** claim speedup; preserve diagnostic results.
- Auto-detect the actual installed source commit (e.g. from pip VCS `direct_url.json`) and compare with requested/recorded source SHA; do not invent one from repository `main` or from a report-branch commit.
- Test packaging/install from a clean CPU environment, `python -m` entrypoint, subprocess exit statuses, missing GPU, wrong SHA, precision failure, publication idempotency, restricted token and GitHub API failures using mocks. Do **not** claim GPU tested locally when only CPU was available.

**Human Scientist — own actual Colab execution**
- One-time steps outside the two command cells: choose Colab GPU runtime; make an approved minimum-scope GitHub credential available via **Colab Secrets** to the Publisher when publishing.
- Run the two commands and inspect status, numerical correctness, environment, timing statistics and any **verified experiment PR URL**.
- Review the proposed public report before final merge. Drive is an optional Notebook/temporary workspace only; it is not a data exchange channel.

**GPT Scientific Mentor** explains the relevant math/accuracy/performance conclusions from the GitHub report and can return to structure research. Mentor does not create fake benchmark results.

## Publication safety and exact behavior

- `--publish` can create an **experiment branch and PR only**, not push directly to protected `main` or merge. Prefer a draft PR if supported; the Scientist must approve publication scope and review before merge. For a public repo, even a draft PR is visible: **publish only pre-approved, sanitized, small allowlisted output files**.
- Support Colab Secrets retrieval **inside the tested Python Publisher module**, or accept a scoped environment credential. Never require a notebook cell containing a token, never echo it and never transmit to another host. Confirm Colab-secret access actually works **from the CLI subprocess**, not merely inside an interactive cell.
- Define explicit outcomes: `BENCHMARK_PASS / BENCHMARK_FAIL / NOT_RUN` and independently `PUBLISHED / PUBLISH_BLOCKED / PUBLISH_FAILED / NOT_REQUESTED`; GitHub PR URL is reported as published only after API confirmation.
- No token or unverified Publisher: complete the local benchmark if possible, keep the reports locally and show `PUBLISH_BLOCKED` or `PUBLISH_FAILED` with actionable next steps. No third user-run publishing command is *required by the final design*, but **until Publisher is implemented** publishing remains manual.
- If CUDA is unavailable, mark GPU benchmark `NOT_RUN` with a clear error; never silently benchmark CPU while labeling it GPU. If installing a VCS source fails, do not proceed and do not claim tested SHA.
- If a numerical test fails or configuration is invalid, do not publish a misleading performance success; return a nonzero status and preserve the diagnostic files. If failure reports are published, status must remain FAIL.
- No GitHub Actions, provider-specific CUDA kernels as a mandatory user API, Colab Drive sync, or notebook-embedded benchmark loops.

## Required reproducibility evidence
- `manifest.json`: actual installed code SHA, runtime, Python/PyTorch/GPU, dtype, seed, preset/parameters, command, timing methodology, status and linked Issue/PR.
- `correctness.json`: oracle, accuracy metrics, tolerance, failing cases, PASS/FAIL/NOT RUN.
- `benchmark.csv`: same-workload measurements and units, synchronization/warmup/repeats, aggregation, compilation cost.
- `summary.md`: measured facts, known limits, paths, SHA and publish status.
- Preserve output from every run in unique `reports/gpu/<run-id>/` directories and do not overwrite previous runs or leak large datasets.

## Acceptance gate for an algorithm project

1. **Codex CPU evidence:** `pip install` from a pinned Git SHA works from a clean environment; invoking packaged benchmark succeeds on CPU with small smoke workload; offline/mocked publication and failure cases pass.
2. **Scientist Colab integration:** from a freshly restarted GPU runtime, the exact **two commands** work for a reviewed candidate SHA, validate accuracy before measuring, and produce truthful GPU environment/timings.
3. **Publisher E2E only after implementation:** `--publish` works with a separately authorized GitHub credential and creates the **verified experiment PR**, without additional Notebook setup code. Before this passes, report `PUBLISH: NOT IMPLEMENTED`.
4. **Review:** GPT Architect checks the real tested SHA, Issue/PR evidence, flags, failure propagation and no notebook logic leakage. Do not mark this requirement achieved merely because this protocol exists.

See [GPU Experiment Protocol](GPU_EXPERIMENT.md) and [Example Notebook Contract](../examples/colab/README.md).
