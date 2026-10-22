# Project Agent Entry Point — SAE V3.3

> Copy to the adopting project's root. Replace placeholders and verify pinned links.

**Project:** `<OWNER>/<PROJECT>`  
**Scientific objective:** `<ALGORITHM_OR_PAPER>`  
**SAE pin:** `<ACTUAL_40_CHARACTER_FRAMEWORK_SHA>`; optional full `.sae/` snapshot for offline use

## Before work
Read this file and `sae.yaml`, then load the actual pinned SAE constitution, assigned role and task-relevant workflow from the immutable SHA (or optional matching local snapshot). Inspect the current task Issue/PR only as needed. Never silently upgrade the pin or assume a link was read.

## Pinned references
For minimal adoption, relative `.sae/` links below are examples for an optional full snapshot; replace them with immutable GitHub URLs at the recorded SHA, or retain them only if that snapshot is present. Keep roles and acceptance conditions identical.

## Project roles
- **Scientist:** sets/changes research objectives and can stop work; no routine scientific/engineering/compute signoff.
- **GPT Architect/Mentor:** autonomously decides mathematical research, `RESEARCH_READY`, specifications, acceptance, iteration and eligible PR merges under [pinned governance](.sae/governance/STANDING_AUTHORIZATION.md) and current owner authorization.
- **Codex:** implementation, local CPU and eligible existing-account Colab CLI CPU/GPU/TPU experiments, artifact verification, session cleanup and GitHub branch/PR evidence. No self-merge or protected-main writes.

## Workflow
Use the pinned [Lean Lab](.sae/workflows/LEAN_RESEARCH_LAB.md) when available: `EXPLORE` uses one bounded Codex batch and compact observation record; `VALIDATE` requires GPT-reviewed math, exact source SHA and real correctness/benchmark evidence. New algorithm/major redesign: GPT-decided concise [mathematical study](.sae/workflows/MATHEMATICAL_RESEARCH.md) + parallel [Build-vs-Reuse](.sae/workflows/ECOSYSTEM_REVIEW.md), reference code and `PROBE_ONLY` device readiness → Codex tests/experiments → GPT evidence review/merge; **no Scientist stage approval**. Use [Compute Experiment](.sae/workflows/GPU_EXPERIMENT.md) for the three separate install/benchmark/optional-publication stages. If the pinned snapshot includes [Experiment by Default](.sae/workflows/GPU_EXPERIMENT.md), GPT makes science/engineering decisions without Scientist signature; Codex needs **no human compute approval** for existing entitlements. Only new monetary commitments, nonpublic sensitive release or external account/security/destructive actions need separate user instruction. Do not silently upgrade older snapshots. Device support, Publisher and speedups require actual evidence. No GitHub Actions, Drive sync or new billable commitments without explicit user consent.

## Role commands
`推进架构师工作` / `推进导师工作` / `推进工程师工作`.

Apply [Role Recovery](.sae/workflows/ROLE_RECOVERY.md) before work. Before the final reply, apply the pinned [Next-Action Completion Gate](.sae/workflows/NEXT_ACTION.md): record actual source SHA and PASS/FAIL/NOT RUN/BLOCKED evidence, end with one complete copyable handoff command when feasible, and give at most two meaningful alternatives. Use genuine interactive controls only where supported; otherwise use a separate plain-text code block for each command. Report DONE/BLOCKED/WAITING_FOR_EXTERNAL_ACTION honestly when no action exists. Never silently replace this project's pinned `.sae/` snapshot.
