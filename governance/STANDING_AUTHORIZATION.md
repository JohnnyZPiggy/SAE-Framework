# Standing Merge Authorization — Scientist → GPT Chief Architect

> Normative: **English** | [简体中文](../i18n/zh-CN/governance/STANDING_AUTHORIZATION.md)

## Grant and expiry

**Grantor:** Human Scientist; **delegate:** GPT Chief Architect during a user-triggered SAE work cycle, using currently authorized GitHub tools. This initial grant and its initial PR merge were explicitly requested by the Scientist on **2026-10-19**. A copied policy file or an agent-authored statement is not proof of any *additional* grant.

**Effective UTC:** 2026-10-19 00:00:00 through **2027-10-18 23:59:59 inclusive**. **Automatically expires 2027-10-19 00:00:00 UTC.** No silent renewal. If the date or current authorization cannot be established, stop and ask.

### Exact repository allowlist

| Repository | Standing merge authority | Basis |
| --- | --- | --- |
| `JohnnyZPiggy/SAE-Framework` | **ACTIVE** during the term, subject to gates below | Scientist's explicit instruction on 2026-10-19 |

**All other repositories are NOT AUTHORIZED**, including algorithm repositories that GPT/Codex can access. An algorithm repository becomes eligible **only** when the Scientist explicitly specifies its exact `owner/repo` and grants standing merge authority, *and* a separately Scientist-approved governance PR adds it to this live register. A copied or pinned `.sae/` snapshot is never by itself an authorization. For algorithm repositories check both the up-to-date Framework register, the specific Scientist authorization and the project's pinned rules. Agents cannot add repositories, broaden powers, renew dates or self-approve governance changes under this standing grant.

The grant allows review and merge of qualifying PRs during **bounded, user-initiated Architect cycles**. It does **not** grant new GitHub permissions, unattended/background execution, direct pushes, force-push, deletions, automatic releases or public experimental-data publication. The Scientist can narrow/revoke this delegation immediately by explicit instruction; newer revocation overrides stale repository text.

## Three-tier merge authority

Classify from the **full diff and highest-risk actual effects**, not the PR title; mixed-risk PRs take the strictest tier.

| Tier | Examples | Architect authority |
| --- | --- | --- |
| **T1 — Routine** | Documentation/translation, non-governance protocol clarification, formatting, narrowly scoped tests, small non-behavior-changing fixes | May autonomously merge **after real diff review and applicable syntax/link/test checks** |
| **T2 — Engineering** | Algorithm code under approved research, numerical corrections, PyTorch optimization, ordinary packaging, benchmark/Publisher code, compatible low-risk dependencies | May merge **only with applicable Scientist mathematical approval, real Codex CPU/oracle/regression and packaging evidence, safety/license checks, and satisfied Issue acceptance**. GPU evidence is essential **if GPU correctness/performance is claimed or is an explicit acceptance gate**; CPU-only changes can merge with clear `GPU_NOT_RUN` when GPU is not a gate. |
| **T3 — Scientist-reserved** | Scientific objectives/assumptions or unproven mathematical acceptance; this grant, scope, expiry, authorizations or governance/security policy; GitHub permissions, branch protection, secrets; license/IP decisions, high-risk dependencies, releases, destructive changes, data deletion, force-push, unapproved external publication | **Not covered.** Requires a **fresh, explicit Scientist approval identifying that PR and intended scope**, plus ordinary GitHub enforcement. |

If tier or evidence is ambiguous, use `SCIENTIST_APPROVAL_REQUIRED` / `MERGE_BLOCKED` rather than downgrade risk. Publishing Colab reports to a public repository requires Scientist's separate, deliberate authorization; this grant does not authorize that publication.

## Merge Gate — every PR, every time

1. **Authority:** verify current UTC term, exact registered repository, valid Scientist grant, active Architect role and user-triggered bounded cycle, connected write tools, applicable project-root `AGENTS.md` and pinned `.sae/`. No silent upgrade of project snapshots.
2. **Actual diff:** inspect all changed files, base/head SHA, Issue, outstanding review threads, GitHub mergeability and branch protections. Never trust only a PR description, labels or another agent's summary.
3. **Tier:** determine highest-risk category. T3 requires PR-specific Scientist approval; an AI comment saying "approved" is not Scientist approval.
4. **Evidence:** for T1 verify applicable docs/links/syntax or tests; for T2 verify Scientist-approved math (or explicit narrow exception), actual Codex CPU numerical/oracle, edge/regression, install and `torch.compile` where supported, license/security/dependencies, and actual Scientist Colab evidence when GPU-gated. `NOT_RUN` is not `PASS`. A GPT-authored substantive code change still needs independently executed Codex/Scientist evidence—no self-certified tests.
5. **Blockers:** do not merge secrets, unexpected public data, unapproved scientific changes, unresolved blocking review, missing required checks, or bypassed branch rules. Confirm the tested source SHA corresponds to the reviewed PR head.
6. **Audit:** write a concise traceable review/comment on the PR **before merge**, listing tier, standing or explicit authorization, exact reviewed head SHA, evidence, risk and decision. If the comment tool is unavailable, use a permitted Issue/PR update or report the audit gap; do not pretend it was written.
7. **Merge and verify:** only on `MERGE_APPROVED`, prefer **squash**, pass the exact reviewed head SHA as the expected head, refetch mergeability, obey GitHub rules, verify success and the resulting merge SHA. If head/base changed materially, re-review. Never force-push or directly push main.

**Statuses:** `MERGE_APPROVED`, `MERGED`, `MERGE_BLOCKED`, `SCIENTIST_APPROVAL_REQUIRED`, `AUTH_SCOPE_MISSING`, `AUTH_EXPIRED`, `UNVERIFIED`.

**Compact PR audit example:**

```text
SAE MERGE GATE
Repo/PR: <owner/repo>#<N>; base/head: <base-sha>/<reviewed-head-sha>
Tier: T1/T2/T3; authority: standing 2026-10-19..2027-10-18 or Scientist approval <link>
Diff and evidence: <real links/commands/status, or NOT RUN>
Decision: MERGE_APPROVED / MERGE_BLOCKED / SCIENTIST_APPROVAL_REQUIRED
Risk: <brief>; outcome: <verified merge SHA or NOT MERGED>
```

No extra artifact or mandatory GitHub Actions; PR/Issue history is the audit trail.

## Non-self-amendment, revocation and adoption

- This file and its Chinese mirror are **T3 governance-controlled**, even if labeled documentation. Scope, dates, tiers, permissions, renewal, or approval gates cannot be amended/renewed by GPT under this authorization.
- **Exception for initial installation only:** Scientist explicitly instructed, on 2026-10-19, to create, review and merge the initial authorization PR. This single instruction does not authorize later changes.
- Revocation by a current explicit Scientist instruction takes effect at once; reflect it in GitHub governance and access settings when feasible. A policy file itself provides no technical access.
- GitHub branch protection (PR-only, prevent force-push) is recommended but **not automatically configured** by this document; changing repository security settings remains Scientist-reserved.
- Bootstrap may copy the governance text into an algorithm project's pinned snapshot for **reference**, but must never register/authorize that algorithm repository automatically.
- **No blanket merge of all branches:** each PR must clear the gate individually; Codex cannot approve or merge its own implementation PR; Scientist owns scientific approval and actual Colab. One invocation is one bounded cycle, never 24/7 monitoring.

Related: [Architect](../protocols/ARCHITECT.md) · [Task Management](../workflows/TASK_MANAGEMENT.md) · [Role Recovery](../workflows/ROLE_RECOVERY.md).
