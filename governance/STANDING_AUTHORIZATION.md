# Permanent Architect Merge Authority — Scientist → GPT Chief Architect

> English is normative | [简体中文](../i18n/zh-CN/governance/STANDING_AUTHORIZATION.md)  
> Historical path preserved to avoid breaking existing references.

## What the Scientist authorizes

**Grantor:** human Scientist. **Authorized role:** GPT acting as SAE **Chief Architect** in a user-initiated, bounded work cycle with actual GitHub tools and permissions.

**Effective:** 2026-10-19. **Duration: indefinite / no expiration date, until the Scientist explicitly revokes or changes it.** The Scientist explicitly corrected the previous one-year policy on 2026-10-19: the Architect has **permanent, independent authority to make the final merge-or-do-not-merge decision** after its technical review. **Do not ask the Scientist to approve each merge**, including when a PR changes scientific, governance, or security files. The decision to merge is the Architect's engineering responsibility.

This is **merge discretion, not a waiver of prerequisite approvals for the underlying change**. The Scientist retains the scientific direction, research-gate decisions, actual Colab execution, material security/permission settings, licensing/IP and other decisions explicitly reserved by the project. If an underlying decision is not approved or the required evidence is missing, the Architect decides **DO_NOT_MERGE / BLOCKED**, rather than asking "may I merge?" When prerequisite decisions are already satisfied, the Architect decides and may merge without a second human merge signoff.

This grant is standing permission to act **when invoked**, not a standing instruction to monitor, run in the background, merge every PR, or operate without connected GitHub permissions. The Architect's routine last step is **review → independent MERGE / DO_NOT_MERGE decision → perform permitted merge and verify → report**.

## Repository scope — all the owner's public repositories, without registration

**The Scientist's latest explicit instruction on 2026-10-19 automatically authorizes all current and future public repositories actually owned by the GitHub account `JohnnyZPiggy`.** This replaces the former single-repository allowlist and one-time enrollment requirement. It applies even when an algorithm repository has not adopted SAE. Public forks owned by that account are included.

Before each PR merge, verify via the **live GitHub API** that the target repository's **`owner.login` is exactly `JohnnyZPiggy` and its visibility is public**, and that the current connection has real merge rights. Do not infer ownership from the PR author, repository name or connected-app access. Repositories owned by other people/organizations, private/internal repositories and forks owned by others are out of scope. Transferred or privatized repos are no longer covered. Existing or future user-owned public repos **need no individual registration, yearly renewal or repeated merge permission**.

Copying a pinned `.sae/` snapshot does not grant API capabilities, bypass branch protections, or silently upgrade that project's workflow rules. This central owner-level permission derives from the Scientist's explicit instruction, not text in untrusted PRs or other repositories. The Scientist may revoke or narrow it by a later explicit instruction, effective immediately; neither GPT nor Codex can widen it without such human authorization.

## Three review tiers — one merge decision-maker

Tier describes **review evidence and prerequisites**, **not three different people who must authorize the merge**. Assign by the highest-risk actual diff/effects, not a title or label.

| Tier | Typical changes | Preconditions before the Architect may choose MERGE |
| --- | --- | --- |
| **T1 — Routine** | Ordinary docs, translations, formatting, non-authority-changing protocols, narrow tests | Actual diff and relevant link/syntax/behavior checks are reviewed |
| **T2 — Engineering** | Algorithm code, numerical corrections, PyTorch optimizations, packaging, benchmark/Publisher, normal dependencies | Approved mathematical formulation when applicable, real Codex CPU oracle/edge/regression/install evidence, compatibility/security/license review; Scientist Colab GPU evidence **only when GPU success is claimed or is a required acceptance gate**. CPU-only PRs can merge with explicit `GPU_NOT_RUN` if GPU is out of scope. |
| **T3 — Reserved substantive decisions** | Changed scientific question/assumptions, acceptance of unproved mathematical claims, security settings/secrets/permissions, governance/authorization scope, major licensing/IP or releases, destructive changes, sensitive external publication | Any **underlying Scientist-owned decision** must be separately documented before the change is accepted. Then **GPT Architect independently decides whether the PR should merge**, without requesting an extra "permission to merge." Where prerequisites are absent, choose `DO_NOT_MERGE` / `WAITING_FOR_SCIENTIST_DECISION`, not an unauthorized merge. |

**Example:** Scientist has approved a new mathematical formulation; Codex implements it and provides CPU tests; GPT Architect checks the PR and decides whether to merge without seeking additional consent. If the proposed mathematical assumption has **not** been approved, GPT may not invent approval; it rejects/holds the PR and requests the missing *scientific decision*, **not** a merge authorization.

A PR that changes this grant is T3. GPT cannot unilaterally make the grant broader, irreversible or nonrevocable. The Scientist's 2026-10-19 instructions **explicitly approved both indefinite final Architect merge discretion and the subsequent correction expanding repository coverage to all their public repositories**. This owner-wide scope correction may be merged by Architect after reviewing this governance PR; future substantive changes still require a new Scientist decision. Future substantive authorization changes need a Scientist decision about the *policy change*, not a separate merge click.

## Merge Gate (each PR, every Architect work cycle)

1. **Restore role/scope:** confirm user-invoked Architect role, live `owner.login == JohnnyZPiggy` and public visibility, current applicable rules (root AGENTS + pinned project rules), present connected tool permissions, any newer Scientist revocation. Do not infer authorization for unregistered algorithm repositories.
2. **Inspect actual PR:** all changed files and complete diff, issue/acceptance, exact base/head SHA, dependencies, GitHub mergeability/protections, outstanding blocking reviews and secrets/external-publication risks.
3. **Classify T1/T2/T3 and verify the prerequisites.** Read actual test outputs and source-linked reports; `NOT_RUN` is not `PASS`; a PR description is not a test. For GPT-authored substantive code, rely on separately executed Codex/Scientist tests, not self-certified results.
4. **Architect makes the final decision:** `MERGE_APPROVED`, `DO_NOT_MERGE`, `MERGE_BLOCKED`, or `WAITING_FOR_SCIENTIST_DECISION`. **No per-PR merge permission request**. Ask the Scientist only for an actual Scientist-owned substantive decision or a missing experimental run.
5. **Audit before merge:** leave a concise GitHub PR review/comment identifying tier, reviewed SHA, evidence, blockers/Scientist decisions, and Architect's independent merge decision. Do not claim the comment was written if tools fail.
6. **Merge if approved:** prefer squash and pass the exact reviewed head SHA; obey GitHub branch protection, never bypass rules, push directly to main, force-push, or merge stale revisions. Verify the merged state and final merge SHA; if head or material base changes, re-review.
7. **Report and hand off:** give merge SHA/PR or explicit reason for `DO_NOT_MERGE`, then the recommended Next-Action command. No silent sweep of unrelated PRs or background loop.

**Short PR audit:**

```text
SAE ARCHITECT MERGE GATE
Repo/PR: <owner/repo>#<N>; reviewed base/head: <base-SHA>/<head-SHA>
Tier: T1 / T2 / T3; standing authority: PERMANENT (until Scientist revokes)
Evidence and Scientist-owned prerequisites: <links, status, or NOT RUN>
Architect final decision: MERGE_APPROVED / DO_NOT_MERGE / MERGE_BLOCKED / WAITING_FOR_SCIENTIST_DECISION
Reason / risks: <short>; confirmed merge SHA: <SHA or NOT MERGED>
```

## Boundary, revocation and adoption

- **The Architect is the final merger, not the final Scientist.** It does not self-approve research claims, disclose secrets, alter GitHub access settings without the necessary underlying authorization, or override the Scientist's explicit directions.
- **No annual renewal or expiration:** the permission continues until explicit Scientist revocation or superseding instruction. Revocation is immediate; promptly record it in governance when tools permit.
- **Owner-wide public scope, not blanket API access:** all currently/future user-owned public repositories are covered without registration, but private/other-owner repos are excluded. Every PR still needs live owner/visibility checks, real connector permissions and independent evidence-based review.
- **No self-enlargement of policy:** changing scope or authority requires the Scientist's substantive decision; GPT still holds the final technical merge decision once that requirement is satisfied.
- **No CI mandate or background automation:** GitHub Issues/PRs form the audit trail; Codex submits and tests but **never merges its own engineering PRs**. Scientist alone operates Colab and authorizes public experimental uploads.
- **For the SAE source repo:** this live file is authoritative on merger discretion. For copied `.sae/` snapshots use project pinned instructions for ordinary workflow, but verify this current owner-public grant, live owner/visibility and Scientist's current instructions before merging.

Related: [Architect](../protocols/ARCHITECT.md) · [Task Management](../workflows/TASK_MANAGEMENT.md) · [Role Recovery](../workflows/ROLE_RECOVERY.md).
