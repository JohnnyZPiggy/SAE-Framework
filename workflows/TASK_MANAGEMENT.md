# GitHub Task Management and Handoff

**Canonical task source:** GitHub Issues, not private chat histories.

## Minimal label vocabulary
- Ownership: `agent:codex`, `agent:architect`, `human:scientist`
- State: `status:ready`, `status:in-progress`, `status:review`, `status:experiment`, `status:blocked`, `status:accepted`
- Work type: `kind:math`, `kind:engineering`, `kind:experiment`, `kind:learning`
- Priority: `priority:p0`, `priority:p1`, `priority:p2`

If labels cannot be created, write the exact intended state into an Issue comment; do not pretend labels were applied. `Assignee` must be a real GitHub username, not an imaginary bot account.

## Lifecycle
1. **Architect creates Issue** with mathematics/interfaces, inputs/outputs, acceptance criteria, CPU/GPU test requirements, references, target milestone; label ready for Codex if applicable.
2. **Engineer claims Issue** by explicit comment and status update to in-progress; one owner at a time.
3. **Engineer implements** on `feat/<issue-number>-<slug>` and opens PR with `Closes #N` only if issue is truly satisfied. For GPU-gated work prefer `Refs #N` until GPU validation.
4. **Architect reviews** diff + real CPU evidence. If accepted provisionally, move to experiment and provide exact candidate SHA.
5. **Scientist runs Colab** with pinned candidate SHA; post experiment report PR/comment. If failed, return to Engineer with a specific reproducible failure case.
6. **Architect accepts/merges** with explicit authorization and evidence; update Issue and next task.
7. **Mentor may summarize** a learning insight, but learning never replaces engineering checks.

## State consistency
- GitHub API writes can fail, labels can be unavailable, PR comments can become stale. Always refetch state after critical mutations.
- Do not auto-claim overlapping Issues; link dependencies; stay inside a bounded cycle.
- Use linked Issues/PRs, run IDs and commit SHAs for all handoffs.
- Never mix numeric performance claims from different code versions without disclosure.
