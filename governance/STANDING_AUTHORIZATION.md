# Permanent Architect Merge Authority — Scientist → GPT Chief Architect

> English is normative | [简体中文](../i18n/zh-CN/governance/STANDING_AUTHORIZATION.md)  
> Historical path preserved to avoid breaking existing references.

## What the Scientist authorizes

**Grantor:** human Scientist. **Authorized role:** GPT acting as SAE **Chief Architect** in a user-initiated, bounded work cycle with actual GitHub tools and permissions.

**Effective:** 2026-10-19. **Duration: indefinite / no expiration date, until the Scientist explicitly revokes or changes it.** The Scientist explicitly corrected the previous one-year policy on 2026-10-19: the Architect has **permanent, independent authority to make the final merge-or-do-not-merge decision** after its technical review. **Do not ask the Scientist to approve each merge**, including when a PR changes scientific, governance, or security files. The decision to merge is the Architect's engineering responsibility.

This is **merge discretion, not a waiver of prerequisite approvals for the underlying change**. The Scientist retains the scientific direction, research-gate decisions, actual Colab execution, material security/permission settings, licensing/IP and other decisions explicitly reserved by the project. If an underlying decision is not approved or the required evidence is missing, the Architect decides **DO_NOT_MERGE / BLOCKED**, rather than asking "may I merge?" When prerequisite decisions are already satisfied, the Architect decides and may merge without a second human merge signoff.

This grant is standing permission to act **when invoked**, not a standing instruction to monitor, run in the background, merge every PR, or operate without connected GitHub permissions. The Architect's routine last step is **review → independent MERGE / DO_NOT_MERGE decision → perform permitted merge and verify → report**.

## Exact repository scope (registration is separate from merge approval)

| Registered repository | Authority | Evidence |
| --- | --- | --- |
| `JohnnyZPiggy/SAE-Framework` | **PERMANENT_ARCHITECT_MERGE**, subject to gates | Scientist instruction on 2026-10-19 |

All other repositories, **including algorithm repositories**, are **NOT REGISTERED** unless the Scientist explicitly authorizes their exact `owner/repo` and has that repository added to this current register. Registration is a **one-time scope decision**, **not** a repeated per-PR or per-merge request. Register additions and material changes to this permission are Scientist-owned decisions; after their approval, the Architect may independently decide whether the corresponding governance PR passes review and is merged. A copied `.sae/` snapshot does not enroll a project. Reading a repo or holding GitHub write permission does not establish registration.

The Scientist may revoke/narrow this permission through a new explicit instruction at any time; the latest instruction controls even if this repository is not yet updated. Neither the Architect nor Codex may self-register repos or silently broaden the granted scope.

## Three review tiers — one merge decision-maker

Tier describes **review evidence and prerequisites**, **not three different people who must authorize the merge**. Assign by the highest-risk actual diff/effects, not a title or label.

| Tier | Typical changes | Preconditions before the Architect may choose MERGE |
| --- | --- | --- |
| **T1 — Routine** | Ordinary docs, translations, formatting, non-authority-changing protocols, narrow tests | Actual diff and relevant link/syntax/behavior checks are reviewed |
| **T2 — Engineering** | Algorithm code, numerical corrections, PyTorch optimizations, packaging, benchmark/Publisher, normal dependencies | Approved mathematical formulation when applicable, real Codex CPU oracle/edge/regression/install evidence, compatibility/security/license review; Scientist Colab GPU evidence **only when GPU success is claimed or is a required acceptance gate**. CPU-only PRs can merge with explicit `GPU_NOT_RUN` if GPU is out of scope. |
| **T3 — Reserved substantive decisions** | Changed scientific question/assumptions, acceptance of unproved mathematical claims, security settings/secrets/permissions, governance/authorization scope, major licensing/IP or releases, destructive changes, sensitive external publication | Any **underlying Scientist-owned decision** must be separately documented before the change is accepted. Then **GPT Architect independently decides whether the PR should merge**, without requesting an extra "permission to merge." Where prerequisites are absent, choose `DO_NOT_MERGE` / `WAITING_FOR_SCIENTIST_DECISION`, not an unauthorized merge. |

**Example:** Scientist has approved a new mathematical formulation; Codex implements it and provides CPU tests; GPT Architect checks the PR and decides whether to merge without seeking additional consent. If the proposed mathematical assumption has **not** been approved, GPT may not invent approval; it rejects/holds the PR and requests the missing *scientific decision*, **not** a merge authorization.

A PR that changes this grant is T3. GPT cannot unilaterally make the grant broader, irreversible or nonrevocable. The Scientist's current 2026-10-19 request **does explicitly approve changing its duration from one year to indefinite and assigning final merge discretion to Architect**; this PR may therefore be merged by the Architect after review. Future substantive authorization changes need a Scientist decision about the *policy change*, not a separate merge click.

## Merge Gate (each PR, every Architect work cycle)

1. **Restore role/scope:** confirm user-invoked Architect role, exact registered repository, current applicable rules (root AGENTS + pinned project rules), present connected tool permissions, any newer Scientist revocation. Do not infer authorization for unregistered algorithm repositories.
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
- **No blanket repository access:** only registered repositories; adding a new algorithm repo needs the Scientist's one-time named authorization, then the Architect can decide all subsequent eligible PR merges without human reauthorization.
- **No self-enlargement of policy:** changing scope or authority requires the Scientist's substantive decision; GPT still holds the final technical merge decision once that requirement is satisfied.
- **No CI mandate or background automation:** GitHub Issues/PRs form the audit trail; Codex submits and tests but **never merges its own engineering PRs**. Scientist alone operates Colab and authorizes public experimental uploads.
- **For the SAE source repo:** this live file is authoritative on merger discretion. For copied `.sae/` snapshots use project pinned instructions for ordinary workflow, but verify this current registry and Scientist consent before merging.

Related: [Architect](../protocols/ARCHITECT.md) · [Task Management](../workflows/TASK_MANAGEMENT.md) · [Role Recovery](../workflows/ROLE_RECOVERY.md).
