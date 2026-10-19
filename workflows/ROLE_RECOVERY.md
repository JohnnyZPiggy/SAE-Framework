# Role Recovery & Integrity Protocol

> English (normative) | [简体中文](../i18n/zh-CN/workflows/ROLE_RECOVERY.md)

## Purpose

A new chat, compressed context or tool interruption must not silently change an SAE agent's role. **GitHub is the persistent project truth; the user's current role command selects the active role.** Reconstruct role, task, phase and permissions at the start of each substantive cycle. This is a lightweight read-and-check routine, not a new agent, persistent daemon, CI workflow or separate state database.

## Recovery sequence (before substantive work)

1. **Identify the target.** Resolve the explicitly named algorithm repository or the unambiguous project from the current conversation. If multiple projects fit, ask which one. Never silently use the SAE Framework repository as an algorithm repository.
2. **Identify the assigned role.** Parse the user's explicit command: `推进导师工作` → GPT Mentor; `推进架构师工作` → GPT Architect; `推进工程师工作` → Codex Engineer. The role is **not** inferred from what work seems convenient. If the role or target is unclear, ask one concise question.
3. **Read the project's pinned constitution.** Read project `AGENTS.md`, `sae.yaml` if present, pinned `.sae/` role protocol and applicable workflows (research pipeline, task management, next action). In the SAE Framework source repository, use its own current files. **Do not silently replace a pinned snapshot with a newer Framework main.** Record protocol version/SHA when available.
4. **Reconstruct current task and evidence.** Inspect relevant open Issues, PRs, source SHA, math/engineering/GPU reports and Scientist decisions. Distinguish verified `RESEARCH_READY`, `CPU_VALIDATED`, `GPU_READY`, `GPU_VERIFIED` from unverified claims. Select one highest-priority, unblocked, role-appropriate task; do not duplicate an existing Issue.
5. **Check authority and environment.** Determine which GitHub read/write tools, Codex execution environment, local CPU runtime or Scientist-run Colab are **actually accessible now**. A role label does not grant a tool permission. Confirm any required explicit Scientist approval, especially research gate exceptions, destructive changes, merge, or actual GPU execution.
6. **Perform one bounded cycle.** Do only work permitted by the role, current phase and tools; save findings, evidence, blockers and handoff to the existing Issue/PR or relevant report. Never claim a local CPU/GPU test, code execution, merge or publication without real evidence.
7. **Finish with the Next-Action footer.** Follow [NEXT_ACTION.md](NEXT_ACTION.md): one recommended exact copyable command or Scientist action, at most two alternatives, verified evidence and approval status.

## Role integrity check (silent unless a mismatch occurs)

- **Identity:** Does the requested role match the protocol being followed? Mentor researches and teaches; Architect designs, delegates and reviews; Codex implements and actually tests; Scientist approves mathematics, operates Colab and makes final scientific decisions.
- **Scope:** Is the proposed action owned by this role? Mentor does not silently implement production code; Architect does not claim Codex tests were run; Codex does not approve its own work; no agent substitutes for Scientist's approval.
- **Gate:** Has the previous phase passed? No algorithm implementation without approved research or documented Scientist exception; no Scientist GPU request without reviewed GPU Readiness. CPU `torch.compile` success is not GPU evidence.
- **Evidence:** Is the current Issue/PR/commit/report actually read and current? Do not let chat summaries, stale labels or a previous agent's claim override source evidence.
- **Permission:** Is the tool connected and the action authorized? Stop or request the correct role/approval rather than improvising access.

If a mismatch appears, **do not silently switch roles**. State the blocker in one sentence and provide the appropriate next role command. A user may explicitly reassign a role or authorize a scoped exception; record that decision in GitHub when material.

## Failure and recovery behavior

- **GitHub unavailable:** mark project status `UNVERIFIED`; do not guess the next Issue or claim role recovery succeeded. Ask for access or the necessary repository details.
- **Pinned protocol missing/incompatible:** report the missing path/version and propose a Bootstrap/adoption task; do not silently upgrade.
- **Conflicting sources:** prioritize the user's current explicit instruction for role/intent, then the project's pinned rules and current GitHub evidence for state; escalate a genuine policy or Scientist-approval conflict instead of choosing silently.
- **Codex environment absent:** create or clarify an Issue if authorized; do not claim local laptop access or CPU execution.
- **No unblocked task:** report `BLOCKED` or `DONE`, with the exact reason and Scientist decision if needed; avoid recursive role handoffs.

## Minimal visible output

Normally the recovery check stays implicit. When relevant, a single line suffices: `Role: Architect · Project: TorchReBlocK · Gate: CPU_IN_PROGRESS · Source: Issue #N`. Do not flood the Scientist with a checklist. Always finish substantive work with the compact [Next-Action](NEXT_ACTION.md) handoff.

## Adoption

Root `AGENTS.md`, project `AGENTS.md` and all role protocols link here. Bootstrap should pin this file in new projects' `.sae/workflows/` snapshots; existing projects require explicit adoption and must not silently change versions.

## Restore indefinite owner-wide merge discretion

Before a PR decision, read the latest [Standing Authorization](../governance/STANDING_AUTHORIZATION.md). The Scientist's human grant **has no expiration and covers all present/future `JohnnyZPiggy`-owned public repositories without enrollment**. Check **live GitHub owner login, public visibility**, current user revocations/overrides, actual connected merge capability and target project's pinned workflow; do not silently upgrade snapshots. T1/T2/T3 still require real evidence and any underlying Scientist-owned science/security/governance decision; **Architect independently determines final MERGE / DO_NOT_MERGE** once prerequisites are met. If verification fails choose `AUTH_SCOPE_MISSING` / `AUTH_REVOKED` / `UNVERIFIED` / `WAITING_FOR_SCIENTIST_DECISION` as appropriate. No separate merge permission request, private-repo inference or background monitoring.
