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
New algorithm implementations and substantial tensorization rewrites require a Scientist-approved `RESEARCH_READY` study (`docs/research/<algorithm>-tensorization.md`) or documented narrow exception **before** a Codex implementation Issue becomes `status:ready`. Missing/blocked studies return to Mentor/Scientist; repository scaffolding is exempt. Full criteria: [Mathematical Research](MATHEMATICAL_RESEARCH.md).

## Linked artifacts in Issue/PR handoffs
Link the approved mathematical study, Engineering Report and Codex-executed experimental evidence following [Three-Artifact Handoff](THREE_ARTIFACT_HANDOFF.md). Experiment PRs identify the exact tested source SHA and upstream Issue/PRs; do not create duplicate status reports or treat templates as proof of execution.

## Lifecycle
1. **Architect creates Issue** with mathematics/interfaces, inputs/outputs, acceptance criteria, CPU/GPU test requirements, references, target milestone; label ready for Codex if applicable.
2. **Engineer claims Issue** by explicit comment and status update to in-progress; one owner at a time.
3. **Engineer implements** on `feat/<issue-number>-<slug>` and opens PR with `Closes #N` only if issue is truly satisfied. For GPU-gated work prefer `Refs #N` until GPU validation.
4. **Architect reviews** diff + real CPU evidence. If accepted provisionally, move to experiment and provide exact candidate SHA.
5. **Codex runs existing-account Colab CLI by default** on the pinned candidate SHA, checks results and session cleanup, and submits report PR/comment only under separate publication rules. No Scientist compute consent or cost gate; genuine correctness/permission failures return to Engineer with a reproducible case.
6. **Architect independently decides MERGE / DO_NOT_MERGE** after technical review and any required Scientist substantive decision, without seeking separate merge permission; update Issue and next task.
7. **Mentor may summarize** a learning insight, but learning never replaces engineering checks.

## State consistency
- GitHub API writes can fail, labels can be unavailable, PR comments can become stale. Always refetch state after critical mutations.
- Do not auto-claim overlapping Issues; link dependencies; stay inside a bounded cycle.
- Use linked Issues/PRs, run IDs and commit SHAs for all handoffs.
- Never mix numeric performance claims from different code versions without disclosure.

## Required next-action handoff
Before the final response of each substantive cycle, apply the [Next-Action Completion Gate](NEXT_ACTION.md) with verified status/evidence and one complete copyable recommendation (up to two meaningful alternatives).

## Role recovery and integrity
At cycle start apply [Role Recovery](ROLE_RECOVERY.md): check role, pinned project rules, live evidence and actual permissions. Stop on role mismatch.

## Indefinite owner-wide Architect merge decision
For eligible PRs in the owner's public repositories, GPT Architect makes the independent final MERGE / DO_NOT_MERGE decision **only** under [Standing Authorization](../governance/STANDING_AUTHORIZATION.md), after live ownership/visibility/permissions, diff/SHA/evidence and Scientist-owned substantive-decision checks. No per-PR merge permission, Codex self-merge or unattended PR sweep. The linked governance document alone defines the full scope, tiers and merge gate.

