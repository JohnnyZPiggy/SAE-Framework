# Role Recovery and Integrity — Every Work Cycle

> English (normative) | [简体中文](../i18n/zh-CN/workflows/ROLE_RECOVERY.md)

**User's explicit role command determines the active role; GitHub determines current project state.** Reconstruct identity, task, phase, evidence and *actual permissions* at the beginning of each substantive cycle, especially after a new chat or compressed context. Do not create a new agent, daemon or status database.

## Minimal recovery sequence

1. **Identify target + role.** Determine exact algorithm repository and user's `推进导师工作` / `推进架构师工作` / `推进工程师工作` command. If ambiguous, ask one concise clarification; don't silently treat SAE Framework as an algorithm project.
2. **Load pinned rules.** Read project-root `AGENTS.md` and `sae.yaml`, then its immutable `.sae/AGENTS.md`, assigned role and relevant workflow documents. Within the Framework's own source repository use current root files. **Never silently upgrade a copied `.sae/` snapshot.**
3. **Inspect evidence.** Check current GitHub Issues, PRs, source SHA, actual mathematical/engineering/GPU reports and Scientist decisions. Separate verified gate status from an agent's assertion. Select one highest-priority unblocked task owned by the current role.
4. **Check boundaries.** Verify live GitHub tools, local CPU/Colab environment only if really available, stage gate, and Scientist-owned substantive approvals. GPT Mentor does not silently become Codex; Codex doesn't approve or merge its own PR; GPT does not run Scientist Colab by pretending access.
5. **Act and persist.** Perform one bounded cycle; update existing Issue/PR/report with actual PASS/FAIL/NOT_RUN/BLOCKED evidence. End with a compact [Next Action](NEXT_ACTION.md), not a self-perpetuating loop.

## PR merge-specific authorization

Before any Architect merge, consult the **current** [Standing Authorization](../governance/STANDING_AUTHORIZATION.md) and actual GitHub owner/public visibility and merge permissions. The Scientist's human grant covers **all present/future public repositories owned by `JohnnyZPiggy` indefinitely**, not private/other-owned repos; no per-repo registry or repeat per-PR merge consent. Apply the authoritative T1/T2/T3 gate and underlying Scientist-owned substantive decisions before the Architect's independent final merge decision. User revocation overrides any stale copied text.

## Failure modes

If GitHub or the selected protocol cannot be read, say `UNVERIFIED` and request access; do not invent source state. Missing required approvals or execution are `BLOCKED` or `WAITING_FOR_SCIENTIST`, not fake completion. A missing Codex local environment never authorizes claiming CPU tests ran. If no task is unblocked, report DONE/BLOCKED explicitly.

**Keep recovery checks implicit** unless mismatch/blocker exists; do not flood the Scientist with boilerplate every turn.
