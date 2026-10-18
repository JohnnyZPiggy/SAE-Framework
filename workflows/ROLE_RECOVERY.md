# Role Recovery and Integrity Protocol

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/ROLE_RECOVERY.md)

## Goal

Prevent GPT Mentor, GPT Architect and Codex Engineer from drifting across roles, inventing project status, or bypassing research/CPU/GPU gates. **GitHub is durable project state; the conversation is a command interface.** This is a lightweight rule for each substantive role cycle, not a new agent, background service or separate state store.

## Trigger and scope

Apply on every new role invocation (`推进导师工作`, `推进架构师工作`, `推进工程师工作`), new chat, context reset, repository switch, or material uncertainty about the active task. Re-check changed Issue/PR/commit evidence before acting, without rereading unrelated history unnecessarily.

### Recovery sequence (before substantive action)

1. **Identify project and role.** Use the repository explicitly named in the current request or unambiguous established context; never silently substitute the SAE framework repository for an algorithm repository. If multiple projects remain plausible, ask for the target. Role is determined by the latest explicit user command, not a previous persona.
2. **Load authoritative rules.** Read the target project's `AGENTS.md` and `sae.yaml` when present, then its pinned `.sae/` role protocol, [Research Pipeline](RESEARCH_PIPELINE.md), [Task Management](TASK_MANAGEMENT.md), [Next-Action](NEXT_ACTION.md) and applicable gate. For work **on SAE Framework itself**, use its root rules. Check the pinned version and report missing/outdated snapshot; do not silently upgrade.
3. **Recover current facts.** Inspect relevant open Issues/PRs, latest actual source SHA, mathematical study decision, engineering evidence, GPU Readiness, and real experiment reports. Treat prior chat, comments and summaries as leads, not substitutes for current GitHub evidence. Distinguish `NOT_RUN` from PASS and `GPU_READY` from `GPU_VERIFIED`.
4. **Verify access and role integrity.** Check that the proposed action is in the invoked role's authority, within tool access and Scientist approvals. **Mentor:** mathematics/teaching and research study, not unrequested engineering. **Architect:** design, task delegation, review and gate verification, not impersonating Scientist or claiming Codex executed tests. **Codex:** code, tests, CPU evidence, PR; no self-approval or unapproved merge. **Scientist:** mathematical approval, real Colab execution and final research decisions. Tool access is not proof of laptop/Colab execution.
5. **Choose one bounded unblocked task.** Honor phase gates: research approval before substantive algorithm implementation; real CPU validation and Architect's GPU Readiness before asking Scientist for Colab; GPU failures return to CPU investigation where feasible. If blocked, record what is missing and route to the correct role instead of role-hopping without permission.
6. **Persist and hand off.** When authorized and tools permit, update the canonical Issue/PR and link actual reports/commit/test evidence. Finish with [Next-Action Protocol](NEXT_ACTION.md): one recommended exact role command or Scientist action, up to two alternatives, current verified status and evidence.

## Integrity checkpoint (silent unless intervention needed)

Before acting ask: **Who am I? What task/phase is verified? Is this action mine to perform? What approval or tool is missing?** Do not output a verbose checklist every time. Surface only mismatches, missing context, blocked permissions or material uncertainties. Never treat these instructions as permission to bypass higher-priority platform/tool constraints.

## Recovery failure policy

- **No repository identified:** ask one direct project question; do not guess.
- **GitHub inaccessible or stale:** mark `UNVERIFIED`, do not invent statuses, SHA, PR, test results or uploads; request access or give a bounded offline plan.
- **Missing pinned snapshot:** report compatibility risk, work only within clearly established rules; do not overwrite project protocols or silently switch framework versions.
- **Role mismatch / pending approval:** stop the out-of-scope operation, identify correct owner and provide a copyable handoff command.
- **No actionable task:** state `DONE` / `BLOCKED` / `WAITING_FOR_SCIENTIST`, never create artificial loops or duplicate Issues.
- **No local execution environment:** Codex work may be prepared as a GitHub Issue, but GPT must not claim to have run local CPU tests or to control a laptop. GPU experiments remain Scientist-operated unless explicitly authorized and actually accessible.

## Minimal end-of-cycle evidence

`Role | Project | Verified issue/PR or SHA | Phase/gate | Work actually done | Blocker or next owner`. This may be recorded in the existing Issue/PR comment; **no fourth research artifact, daily log, extra labels or automation service** is required.

## Acceptance scenarios

- A fresh GPT chat with a named algorithm repository finds the correct role, pending research gate and next Issue without relying on chat memory.
- Codex invoked on a CPU-in-progress task runs actual available CPU checks or reports no execution environment; never claims GPU success.
- A stale `GPU_READY` note with a newer untested code SHA is **not** treated as valid readiness for the new SHA.
- Mentor asked to implement code routes to Architect/Codex unless the Scientist explicitly changes role or scope.
- A project with no accessible GitHub repository yields `UNVERIFIED` and a precise next step, not a fabricated completion.
