# Compute Experiment Protocol — CPU / GPU / TPU (V3.3)

> Historical path retained for compatibility | [简体中文](../i18n/zh-CN/workflows/GPU_EXPERIMENT.md)

## Ownership and prerequisites
- **Scientist:** scientific decisions, experiment objectives and prior compute authorization (hardware, session count, time and quota).
- **Architect:** experiment matrix, readiness/acceptance criteria, review of evidence and final eligible PR merge discretion.
- **Codex:** local/Colab CLI execution, correctness and benchmark tooling, artifact retrieval/integrity verification, session cleanup and authorized GitHub evidence PRs.
- **GitHub:** shared code/task/report source of truth. Drive is optional temporary Colab workspace only.

For new algorithms/major tensorization changes, require a Scientist-reviewed [mathematical study](MATHEMATICAL_RESEARCH.md) and Architect experiment plan. CPU correctness/installation and relevant readiness checks precede formal accelerator performance claims. No hardware claim without actual execution.

## Three separate logical stages
1. **Pinned install:** run exact source commit SHA in the selected local/Colab environment.
2. **Benchmark:** execute correctness and performance CLI; **no GitHub writes**.
3. **Optional publication:** after evidence validation and applicable Scientist authorization, publish only reviewed safe artifacts to a dedicated GitHub branch/PR.

The existing [three-stage compatibility entry](COLAB_TWO_COMMAND.md) retains its historical filename. Its illustrative notebook commands are not proof of a working CLI. Codex may orchestrate these stages via Colab CLI without requiring the Scientist to click notebook cells. Publisher remains unverified until end-to-end tested.

## Compute and hardware controls
Reuse existing WSL2/Colab CLI OAuth when available. Before GPU/TPU allocation verify explicit Scientist-approved device class, concurrent sessions, runtime and quota; if unspecified, stop and request limits. Choose hardware by the task rather than defaulting to NVIDIA/CUDA. For TPU, separately validate allocation, PyTorch/XLA installation, supported operations and accuracy. TPU options listed by a CLI do **not** establish functionality.

On success, failure or interruption: attempt to stop every allocated session, verify final session state, and report cleanup failures. Do not silently leave resources running.

## Required evidence
- `manifest.json`: run ID/time, exact source SHA, Issue/PR, device, software environment, seed, dtype, commands, status and methodology.
- `correctness.json`: reference, tolerances, errors and PASS/FAIL/NOT RUN.
- `benchmark.csv`: workloads, timing units, repetitions, warmup/synchronization, median/p95 and compilation cost where relevant.
- `summary.md`: actual observations, limitations, failures, cleanup outcome and evidence links.
- Download integrity verification (e.g. SHA-256), local/remote artifact identity and publication status.

Avoid large datasets, raw secrets and unnecessary logs. Never report a speedup without equivalent baselines and numerical correctness.

## GitHub publication and failure handling
After authorization, validate artifact schemas/size/secrets; create an immutable run-specific branch/PR, link source SHA and Issue/code PR, verify API success, and leave merging to Architect. Public draft PRs are still public. No direct protected-main writes, force pushes or self-merges. Keep credentials in secure stores, never in checked-in files or logs.

Use `PUBLISH_FAILED` for upload/API failure; `NOT RUN` for untested hardware; `BLOCKED` for missing approval, source mismatch or unavailable environment. Report failed cleanup explicitly.

## Verified state as of 2026-10-19
User-provided handoff reports a real T4 GPU smoke test via Windows Codex → WSL2 Ubuntu 24.04 → Colab CLI 0.7.4, remote Python 3.13.15 / PyTorch 2.11.0+cu130 / CUDA 13.0, 1024×1024 float32 matmul (20 timings, mean 0.736283 ms), JSON/SHA-256 verification and zero active sessions after stop. This establishes basic GPU remote execution only. Colab CPU, TPU v5e1/v6e1 allocation and PyTorch/XLA, automated GitHub publication and cross-project reuse remain unverified.
