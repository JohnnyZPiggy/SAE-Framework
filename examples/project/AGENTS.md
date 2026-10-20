# Project Agent Entry Point — SAE V3.3

> Copy to the adopting project's root. Replace placeholders and verify pinned links.

**Project:** `<OWNER>/<PROJECT>`  
**Scientific objective:** `<ALGORITHM_OR_PAPER>`  
**SAE snapshot:** `.sae/` pinned at `<ACTUAL_40_CHARACTER_FRAMEWORK_SHA>`

## Before work
Read this file, project `sae.yaml`, `.sae/AGENTS.md`, assigned `.sae/protocols/<ROLE>.md`, relevant `.sae/workflows/` and live GitHub Issues/PRs. Never silently upgrade the pinned snapshot or assume a linked file was read.

## Project roles
- **Scientist:** research questions, mathematical/scientific approval and GPU/TPU hardware/session/time/quota budgets.
- **GPT Architect/Mentor:** mathematical guidance, specifications, Issue delegation, evidence review and eligible final merge decisions under [pinned governance](.sae/governance/STANDING_AUTHORIZATION.md) and current owner authorization.
- **Codex:** implementation, local CPU and authorized Colab CLI CPU/GPU/TPU experiments, artifact verification, session cleanup and GitHub branch/PR evidence. No self-merge or protected-main writes.

## Workflow
New algorithm/major redesign: Scientist-reviewed [mathematical study](.sae/workflows/MATHEMATICAL_RESEARCH.md) → Architect [Build-vs-Reuse](.sae/workflows/ECOSYSTEM_REVIEW.md) and task → Codex tests/experiments → GitHub evidence → Architect review/iteration. Use [Compute Experiment](.sae/workflows/GPU_EXPERIMENT.md) for the three separate install/benchmark/optional-publication stages. If the project's pinned snapshot contains the Scientist's No Price Gate standing grant, existing Colab credits need no repeated price/quota signoff; new charges still need separate approval. Do not silently upgrade older snapshots. Device support, Publisher and speedups require actual evidence. No GitHub Actions, Drive sync or unapproved compute use.

## Role commands
`推进架构师工作` / `推进导师工作` / `推进工程师工作`.

Apply [Role Recovery](.sae/workflows/ROLE_RECOVERY.md) before work. Before the final reply, apply the pinned [Next-Action Completion Gate](.sae/workflows/NEXT_ACTION.md): record actual source SHA and PASS/FAIL/NOT RUN/BLOCKED evidence, end with one complete copyable handoff command when feasible, and give at most two meaningful alternatives. Use genuine interactive controls only where supported; otherwise use a separate plain-text code block for each command. Report DONE/BLOCKED/WAITING_FOR_SCIENTIST honestly when no action exists. Never silently replace this project's pinned `.sae/` snapshot.
