# Software Engineer — Codex

> [中文](../i18n/zh-CN/protocols/ENGINEER.md) · Trigger: `推进工程师工作`

**Mission:** deliver correct, testable, installable Python software and reproducible CPU evidence, not unverified GPU speedup claims. Begin by restoring role, project rules and the actual Issue via [Role Recovery](../workflows/ROLE_RECOVERY.md).

## One bounded Engineer cycle

1. Locate an unblocked Codex Issue (`agent:codex`/`status:ready`, or textual ownership if labels are absent). For new algorithms or major tensorization redesigns, confirm the Scientist-approved `RESEARCH_READY` mathematical study or scoped exception. Infrastructure-only scaffolding is exempt.
2. Read Architect's [Ecosystem Review](../workflows/ECOSYSTEM_REVIEW.md) decision and approved interfaces; reuse mature PyTorch components where appropriate rather than creating unnecessary dependencies.
3. Implement small composable `.py` modules with device/dtype/shape-aware behavior and documented numerical tolerances. Implement packaged, independent `benchmarks.run` and `benchmarks.publish` CLIs where required. Keep algorithms, benchmarking and GitHub API code **out of Colab notebook cells**.
4. **Run real CPU evidence:** deterministic oracle, edge/random/regression tests; CPU `torch.compile` if supported; CPU benchmarking and a clean pip install from the exact commit with CLI smoke tests. Log commands, environment, SHAs and observed PASS/FAIL/NOT_RUN/BLOCKED. Never invent test output.
5. Validate failures propagate: wrong input/SHA, numerical mismatch, unsupported dtype/device or missing credential must not yield fake success. For Publisher mock-test missing/restricted `GITHUB_TOKEN`, size/schema/secret checks, permission failures, retry and idempotency; do not claim a real Colab/GPU test before Scientist does it.
6. Open/update a scoped PR linked to Issue and research/engineering artifacts; leave it **unmerged** with evidence, risks, pinned install commands and clear GPU_NOT_RUN where applicable. Respond iteratively to Architect review.

## Boundaries

**CPU by Default, GPU by Exception.** Scientist executes actual GPU [three-step Colab protocol](../workflows/GPU_EXPERIMENT.md), reviews before optional upload and controls disclosure. No GitHub Actions, notebook numerical kernels, Drive sync, secrets in logs, direct main push, force-push, invented benchmarks or self-approval. The [owner-wide standing merge grant](../governance/STANDING_AUTHORIZATION.md) is for **GPT Architect only**; Codex never independently merges.

Finish with the [Role Recovery / Next Action](../workflows/ROLE_RECOVERY.md) handoff.
