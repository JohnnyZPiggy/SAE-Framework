# Research Pipeline — Scientific Gate, CPU Validation, Authorized Accelerators (V3.3)

> English normative | [简体中文](../i18n/zh-CN/workflows/RESEARCH_PIPELINE.md)

SAE is **CPU-first**, not CPU-only or GPU-only. Its phases are iterative; experimental failures may return to engineering or mathematical research. GitHub remains the evidence hub; no default GitHub Actions, Drive sync or background agent.

## I. Mathematical research — Mentor + Scientist
Explore formulations, oracles, tensor/batched operators, matrix-free structure, stability and complexity. Record the existing `docs/research/<algorithm>-tensorization.md`. Scientist decides `RESEARCH_READY`, `RESEARCH_BLOCKED` or `NOT_TENSORIZABLE`; a narrow explicit exception may permit nonstandard engineering.

## II. Engineering and CPU correctness — Architect + Codex
Architect reviews ecosystem Build-vs-Reuse, sets specifications and dispatches Issues. Codex implements installable Python modules and runs actual CPU oracle/edge/randomized/dtype tests, supported `torch.compile`, clean pinned-SHA installation and benchmark CLI smoke tests. Record source SHA, actual commands and results in the engineering report. CPU compile does **not** establish GPU/TPU compatibility or speedup.

Architect marks `ACCELERATOR_READY` (or historical `GPU_READY`) only after relevant mathematical, numerical, package and experiment readiness gates pass. Readiness is **not** hardware verification.

## III. Device experiments — Codex executes by default, Architect reviews
Under [Experiment by Default](GPU_EXPERIMENT.md), Codex executes existing-account CPU/GPU/TPU without any Scientist compute authorization gate, grant check or price forecast. Bounded `PROBE_ONLY` device diagnostics can precede formal research/benchmark readiness; formal performance claims still require mathematical and numerical acceptance. Use one active Colab session by default, finite timeout, exact SHA, real access, evidence validation and session cleanup. User stop instructions and separate new-billing approval remain effective. TPU/XLA capability requires actual tests, not menu entries.

Use [Compute Experiment](GPU_EXPERIMENT.md): exact-SHA install → benchmark **without GitHub writes** → optional separately authorized validated GitHub report branch/PR. Architect reviews evidence and merges only eligible PRs under [Standing Authorization](../governance/STANDING_AUTHORIZATION.md). Codex never self-merges. Publisher success requires real GitHub verification.

On device failure return to Phase II; on flawed math return to Phase I. Preserve linked mathematical, engineering and experimental artifacts, with honest `PASS` / `FAIL` / `NOT RUN` / `BLOCKED` statuses. The Scientist retains scientific conclusions and substantive governance decisions; routine compute needs no human signoff. Existing pinned V3.2 projects are not silently upgraded.
