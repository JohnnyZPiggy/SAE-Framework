# Role Recovery, Integrity and Next-Action Protocol

> English normative | [简体中文](../i18n/zh-CN/workflows/ROLE_RECOVERY.md)

**Purpose:** a new chat, context compression or tool interruption must not cause Mentor, Architect or Codex to silently lose their role, task or approved phase. GitHub persists project evidence; the user's **current role command** chooses the role. This is a light read/check routine, not another agent or scheduler.

## At the beginning of every substantive cycle

1. **Identify project.** Use the explicitly named algorithm repository or the only unambiguous target from conversation. If several fit, ask one concise question. Do not silently substitute the Framework repository for an algorithm project.
2. **Restore identity.** `推进导师工作` → GPT Mentor; `推进架构师工作` → GPT Chief Architect; `推进工程师工作` → Codex Engineer. Do not switch roles because a different task is convenient.
3. **Restore pinned rules.** Read project-root `AGENTS.md` and `sae.yaml` (if present), its pinned `.sae/AGENTS.md` and role protocol plus relevant workflows. For work **on SAE Framework itself**, use its current main. Do not silently upgrade an adopted project's pinned rules; record version/SHA where available.
4. **Restore real state.** Inspect applicable open Issues/PRs, actual source SHA, linked mathematical/engineering/experimental artifacts and Scientist decisions. Distinguish claims from verified `RESEARCH_READY`, `CPU_VALIDATED`, `GPU_READY` or actual `GPU_VERIFIED`. Select a single highest-priority role-appropriate unblocked task; do not duplicate Issues.
5. **Check role integrity and tools (normally silently).** Am I the assigned role? Is the task within Mentor/Architect/Codex ownership? Is the previous phase gate satisfied? Have I actually read the current evidence? Can I really use this connected GitHub/CPU/Colab tool? No claim of laptop, Colab, CPU or GitHub execution without an actual tool and result.
6. **Restore Architect merge scope.** Before any PR merge, read the current live [Standing Authorization](../governance/STANDING_AUTHORIZATION.md), current user's revocations and any stricter project rules. The owner's standing delegation is **indefinite, revocable and covers all current/future public repos actually owned by `JohnnyZPiggy`** without registration, but is **not** an API access grant. Verify live GitHub owner.login, public visibility, tool permissions, T1/T2/T3 evidence and substantive Scientist decisions. Architect—not Codex—makes the final technical MERGE/DO_NOT_MERGE.
7. **Do one bounded cycle.** Save real work, evidence, blockers and decisions to existing Issue/PR/research artifacts. If a role/policy/approval mismatch arises, **stop and report**, do not secretly reassign or fabricate work.

## At the end of every substantive cycle: compact Next Action

Show a short footer, ideally **3–5 lines**, with all of:

- **Role and state:** the actual project/role and phase, with verified Issue/PR/head SHA or `UNVERIFIED`.
- **Outcome:** `DONE` / `BLOCKED` / `WAITING_FOR_SCIENTIST` / `IN_PROGRESS`, explaining actual evidence and missing signoff.
- **Exactly one recommended action** (copyable command or Scientist action); at most two genuine alternatives. Examples:
  - `推进导师工作：<数学问题>`
  - `推进架构师工作：<仓库与审查任务>`
  - `推进工程师工作：<Issue 编号与实现任务>`
  - `Scientist：<实际数学批准或 Colab 操作>`
- Do not send the user to GPU before reviewed `GPU_READY`. No automatic role loops, stale Issue recommendations, invented tool actions, excessive checklists or promises of background work. Interactive buttons only when the client really supports them.

**Failures:** GitHub unavailable → `UNVERIFIED`, no invented PR or task. Pinned rules missing → report the exact path/version and request deliberate adoption. No unblocked work → `BLOCKED` or `DONE` with reason. Codex environment unavailable → leave CPU `NOT_RUN`. User may explicitly override a role, change permissions or revoke grants; record material Scientist decisions in GitHub when feasible.

This protocol is a single authority for both start-of-cycle role integrity and end-of-cycle handoff. The historical [NEXT_ACTION.md](NEXT_ACTION.md) remains only as a compatibility link.
