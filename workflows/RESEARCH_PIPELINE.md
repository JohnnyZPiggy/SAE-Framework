# SAE Research-First Pipeline — CPU by Default, GPU by Exception

> English normative | [简体中文](../i18n/zh-CN/workflows/RESEARCH_PIPELINE.md)

A three-phase **scientific gate**, not a linear, unattended agent pipeline. GitHub Issues/PRs and [three linked artifacts](THREE_ARTIFACT_HANDOFF.md) record evidence; blocked projects return to the appropriate prior phase. No GitHub Actions or Drive synchronization.

## Phase I — Mathematical research (Mentor + Scientist)

Study original and tensorized mathematical formulations, matrix/vector or matrix-free structure, shapes, accuracy guarantees, oracle, stability, sparsity/low rank, batching and remaining sequential dependencies. Produce `docs/research/<algorithm>-tensorization.md` following [Mathematical Research](MATHEMATICAL_RESEARCH.md).

**Scientist controls the gate:** `RESEARCH_READY` to proceed, `RESEARCH_BLOCKED` for more research, `NOT_TENSORIZABLE` for reasoned no-go or an explicit narrow exception. Do not start full algorithm-acceleration engineering from unexamined loops.

## Phase II — Architecture and actual CPU engineering

Architect performs the [Ecosystem Review](ECOSYSTEM_REVIEW.md), specifies interfaces, oracle/tolerances, dependency/build decision, benchmarking and independent packaged run/publish CLIs. Codex implements testable Python modules and **actually executes** reference/edge/random/regression tests, CPU eager and applicable `torch.compile`, CPU benchmark, clean exact-SHA pip install and CLI smoke test. Record real outputs, tested SHA, environment and known failures in `docs/engineering/<algorithm>-engineering.md`.

**GPU Readiness gate:** Architect reviews the [small checklist](../templates/GPU_READINESS.md) and only then grants `GPU_READY`. Require approved math, real CPU correctness, relevant CPU compilation or justified waiver, package and CLI, pinned tested source, dataset/preset, device/error handling and report format. A missing test is `NOT_RUN`; `GPU_READY` means readiness only, **not** GPU success. Routine CPU fixes do not need repeated Scientist GPU runs.

## Phase III — Scientist-operated GPU experiment

Scientist batches ready experiments when convenient, with no unattended Colab execution. Use the [three-step Colab contract](GPU_EXPERIMENT.md): pinned-SHA pip install → independent `benchmarks.run --device cuda --out ...` (local report, no GitHub write) → **optional** separate `benchmarks.publish --report-dir ...` *after* inspecting accuracy/performance and public-disclosure safety. Both CLIs are targets until actually implemented. Secure Secret named `GITHUB_TOKEN`; subprocess reading must be verified or safely bridged.

Record device/backend, source SHA, dtype, seeds, oracle errors and warmup/synchronized timings in the actual `reports/gpu/<run-id>/` artifact. `GPU_VERIFIED` means real compatible-device correctness was checked, **not automatically a speedup**. GPU failure → return reproducible Issue to Phase II; invalid mathematics → Phase I.

## State and resume

Use relevant `RESEARCH_READY/RESEARCH_BLOCKED`, `CPU_IN_PROGRESS/CPU_BLOCKED/CPU_VALIDATED`, `GPU_READY/GPU_IN_PROGRESS/GPU_VERIFIED/GPU_BLOCKED` with real Issue/PR evidence. For the user's `推进导师工作`/`推进架构师工作`/`推进工程师工作`, [Role Recovery](ROLE_RECOVERY.md) handles pinned rule loading and next action; this file defines **only stage gates**.

Adopted algorithm projects retain their pinned version until explicitly migrated.
