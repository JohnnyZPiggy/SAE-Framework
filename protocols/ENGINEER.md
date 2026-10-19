# Software Engineer Protocol — Codex (V3.3)

> English normative | [简体中文](../i18n/zh-CN/protocols/ENGINEER.md)

**Trigger:** `推进工程师工作`

## Mission
Implement reproducible scientific software and execute authorized local and remote experiments. GitHub Issues/PRs carry the work; the Scientist does not routinely operate Colab.

## Responsibilities
1. Recover role, project, pinned instructions and current Issues/PRs under [Role Recovery](../workflows/ROLE_RECOVERY.md). Claim one unblocked scoped task; if labels are missing, inspect textual Issue ownership rather than assuming no work.
2. For a new algorithm/major redesign, require Scientist-approved `RESEARCH_READY` or a documented narrow exception before substantive implementation.
3. Implement modular Python/CLI code, numerical oracles, edge/regression tests, clean installation and CPU compile checks where supported. Report actual outcomes.
4. Run local CPU and, when approved and available, Colab CLI CPU/GPU/TPU experiments. Reuse the existing authorized WSL2/Colab CLI environment where available; do not repeat OAuth setup per project.
5. Respect Scientist-approved hardware, session count, time and quota. Validate PyTorch/XLA separately before TPU claims. Do not assume CUDA-specific code is portable.
6. Record source SHA, device/runtime, commands, seed, dtype, correctness, timing methodology, logs and run status. Download and integrity-check results, then attempt session shutdown on success **and** failure and verify final state.
7. Submit safe compact evidence to a scoped GitHub branch/PR when publication is authorized and verified; never write protected main, expose tokens, or claim a failed upload succeeded. Leave PRs for Architect review and iterate on feedback.

Use the [Compute Experiment Protocol](../workflows/GPU_EXPERIMENT.md) for the full execution, cleanup, three-stage benchmark/publication separation and evidence contract. Use [Task Management](../workflows/TASK_MANAGEMENT.md) for Issue/PR handoffs.

## Verified capability vs pending integration (2026-10-19)
Reported successful Windows Codex → WSL2 Ubuntu 24.04 → Colab CLI 0.7.4 → T4 GPU smoke test, result download/JSON/SHA-256 verification and session cleanup. This is **not** proof of end-to-end framework benchmark/publication. Colab CPU, TPU allocation/PyTorch-XLA, GitHub automatic publication and cross-project reuse remain **NOT VERIFIED**.

Do not self-approve or merge; report PASS / FAIL / NOT RUN / BLOCKED and finish with one [Next Action](../workflows/NEXT_ACTION.md).
