# Role Recovery & Integrity Protocol (V3.3)

> English normative | [简体中文](../i18n/zh-CN/workflows/ROLE_RECOVERY.md)

## Purpose
GitHub holds persistent project state. A fresh chat or interrupted session must recover the explicit role, target, pinned instructions, task evidence and actual permissions; this is a read/check routine, not a background agent or state database.

## Recovery checklist
1. Resolve the user's explicit target repository; if ambiguous, ask rather than treating the SAE Framework source repository as an algorithm project.
2. Honor explicit role commands: `推进导师工作` → GPT Mentor; `推进架构师工作` → GPT Architect; `推进工程师工作` → Codex Engineer. Do not silently switch roles.
3. Read project `AGENTS.md`, `sae.yaml`, pinned `.sae/` protocols and relevant workflow. Do not silently upgrade a pinned V3.2 project to V3.3.
4. Read current Issues/PRs, exact candidate source SHA, math/engineering/experiment reports and Scientist decisions. Distinguish research approval, CPU validation, accelerator readiness and **actual device-specific verification**; do not infer GPU/TPU support from CPU or CLI options.
5. Check actual connected GitHub/CLI/runtime permissions and Scientist-approved compute hardware, session/time/quota bounds before GPU/TPU use. No access or approval means BLOCKED, not implied authorization.
6. Perform one bounded role-appropriate cycle: Mentor researches/teaches; Architect designs/reviews/decides merges; Codex implements, runs authorized local/Colab CPU/GPU/TPU experiments, retrieves/verifies results, releases sessions and submits PR evidence; Scientist retains substantive science and compute-budget decisions.
7. Report observed actions, PASS/FAIL/NOT RUN/BLOCKED, source and report links, remaining blockers and one [Next Action](NEXT_ACTION.md).

Use [Compute Experiment Protocol](GPU_EXPERIMENT.md) for execution/publication and [Standing Authorization](../governance/STANDING_AUTHORIZATION.md) for merge discretion. No fabricated execution, silent role substitution, unbounded retries, GitHub Actions or self-merged Codex PRs.
