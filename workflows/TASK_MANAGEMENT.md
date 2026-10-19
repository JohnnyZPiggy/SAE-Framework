# GitHub Task Management and Handoff

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/TASK_MANAGEMENT.md)


**Canonical task source:** GitHub Issues, not private chat histories.

## Minimal label vocabulary
- Ownership: `agent:codex`, `agent:architect`, `human:scientist`
- State: `status:ready`, `status:in-progress`, `status:review`, `status:experiment`, `status:blocked`, `status:accepted`
- Work type: `kind:math`, `kind:engineering`, `kind:experiment`, `kind:learning`
- Priority: `priority:p0`, `priority:p1`, `priority:p2`

If labels cannot be created, write the exact intended state into an Issue comment; do not pretend labels were applied. `Assignee` must be a real GitHub username, not an imaginary bot account.

## Pre-engineering research gate

For a new algorithm or significant tensorization rewrite, the first scientific Issue/record is a **Mentor-owned mathematical structure study**; it is **not** yet an `agent:codex` implementation task. Link the Scientist-reviewed `docs/research/<algorithm>-tensorization.md` and its `RESEARCH_READY` decision before marking any algorithm implementation Issue `status:ready`. Architect then prepares interfaces/tests and formal Colab experiment questions. A missing or blocked study must be routed to Mentor/Scientist, not silently handed to Codex. Basic repository bootstrap work is exempt; see [the research gate](MATHEMATICAL_RESEARCH.md).

## Linked artifacts in Issue/PR handoffs

The Scientist-reviewed mathematical study, the Architect/Codex engineering record, and the Scientist-operated Colab run report form one traceable evidence chain; see [Three-Artifact Handoff](THREE_ARTIFACT_HANDOFF.md). A Codex implementation Issue/PR links the mathematical study and engineering record; the actual experiment PR points to the tested implementation SHA and both earlier documents. Do not create a fourth competing status document or pretend a template proves work was done.

## Lifecycle
1. **Architect creates Issue** with mathematics/interfaces, inputs/outputs, acceptance criteria, CPU/GPU test requirements, references, target milestone; label ready for Codex if applicable.
2. **Engineer claims Issue** by explicit comment and status update to in-progress; one owner at a time.
3. **Engineer implements** on `feat/<issue-number>-<slug>` and opens PR with `Closes #N` only if issue is truly satisfied. For GPU-gated work prefer `Refs #N` until GPU validation.
4. **Architect reviews** diff + real CPU evidence. If accepted provisionally, move to experiment and provide exact candidate SHA.
5. **Scientist runs Colab** with pinned candidate SHA; post experiment report PR/comment. If failed, return to Engineer with a specific reproducible failure case.
6. **Architect independently decides MERGE / DO_NOT_MERGE** after technical review and any required Scientist substantive decision, without seeking separate merge permission; update Issue and next task.
7. **Mentor may summarize** a learning insight, but learning never replaces engineering checks.

## State consistency
- GitHub API writes can fail, labels can be unavailable, PR comments can become stale. Always refetch state after critical mutations.
- Do not auto-claim overlapping Issues; link dependencies; stay inside a bounded cycle.
- Use linked Issues/PRs, run IDs and commit SHAs for all handoffs.
- Never mix numeric performance claims from different code versions without disclosure.

## Required next-action handoff

At the end of each substantive work cycle, follow the [Next-Action Protocol](NEXT_ACTION.md): recommend one specific, copyable role command or Scientist action, at most two useful alternatives, verified GitHub evidence, and any approval needed. Do not request repeated Colab runs before GPU_READY or pretend a command has executed. Offer one-tap actions only where the client actually supports them.

## Role recovery and integrity

Before each substantive work cycle, apply [Role Recovery & Integrity](ROLE_RECOVERY.md): restore the explicitly assigned role, read pinned project rules and live GitHub evidence, verify phase and actual tool permissions, and stop on role mismatch rather than silently changing identity. Keep the existing Next-Action handoff at the end.

## Indefinite owner-wide Architect merge decision

At the end of a relevant user-invoked cycle GPT independently decides **MERGE / DO_NOT_MERGE** for each reviewed PR under [Standing Authorization](../governance/STANDING_AUTHORIZATION.md), across **all current/future public GitHub repositories owned by `JohnnyZPiggy`**. No repository registration, time limit or per-PR Scientist merger authorization. T1/T2/T3 remain *evidence and underlying Scientist-owned substantive-decision gates*, not distinct merge authorities. Confirm live GitHub owner/public status, tool permissions, full diff, tested SHA, relevant math/CPU/GPU evidence, safety and branch rules. Record pre-merge audit, exact-head squash-merge if accepted and verify response. If scientific/security decisions are missing, hold and ask about the underlying change, not merge permission. Codex cannot self-merge; no unattended branch sweep.
