# Tasks — Issues, PRs, Modes and Review (V3.4)

> English normative | [简体中文](../i18n/zh-CN/workflows/TASKS.md)

GitHub Issues hold tasks and PRs hold code and evidence. Nothing else is shared state.

## One Issue → one bounded Engineer batch
The Architect writes one Issue with the [template](../templates/ISSUE_TEMPLATE.md): goal, math contract, Definition of Done, size budget, required tests, devices and the *Not required* list. Inside that Issue the Engineer may implement → test → fix → rerun as often as needed without new approval, up to three repair attempts per failure class. It then opens **one PR** (`feat/<issue>-<slug>`, `Closes #N` when done, else `Refs #N`) with **one handoff comment**.

- Labels and claim comments are optional. Use a claim only when two agents could collide.
- Follow-ups go on the **same Issue**, not new planning Issues or status reports.
- Refetch GitHub state after important writes; API calls can fail silently.
- Never mix numbers from different code versions without saying so.

## Two modes, chosen by the claim you want to make
| | `EXPLORE` — fast falsification | `VALIDATE` — acceptance |
|---|---|---|
| Start | A testable hypothesis and the smallest oracle | Mentor `RESEARCH_READY` (or a stated bounded assumption) |
| Evidence | A short note in the Issue/PR: source, command, result | Final SHA, required tests, independent oracle, fair benchmark if speed is claimed |
| Claim | `HYPOTHESIS` / `PROBE_ONLY`: never a formal result | Architect accepts only measured results |

The Architect switches modes on evidence; there is no extra approval.

## Where results live (in the algorithm project)
- Math: `docs/research/<algorithm>-tensorization.md` ([template](../templates/TENSORIZATION_STUDY.md)).
- Engineering: the PR and its handoff comment. No separate engineering report.
- GPU runs: `reports/<run-id>/summary.md` plus one results file ([template](../templates/EXPERIMENT_REPORT.md)), within the [evidence caps](../governance/SIMPLICITY_CONTRACT.md#3-evidence-git-is-the-integrity-layer).

Link these; don't copy numbers between them.

## Review
The Architect does one pass at the exact head SHA, in this order:
1. **Size.** Net lines against the budget; validation only at trust boundaries; no [banned patterns](../governance/SIMPLICITY_CONTRACT.md#banned-patterns-unless-the-issue-names-the-risk); test lines ≲ source lines. Ask what can be deleted.
2. **Correctness.** The required tests on the final SHA. For numerical claims, an independent reference with a justified tolerance.
3. **Devices.** A GPU claim needs a run on the exact SHA with the observed device and confirmed cleanup. A speedup needs the same sizes, dtype and accuracy, and must disclose warmup, synchronization and compile time.
4. **Integrity and security.** Real measurements only; no secrets or raw CLI output.

| Outcome | Meaning |
|---|---|
| `ACCEPTED` | Evidence meets the Issue; merge if eligible ([Standing Authorization](../governance/STANDING_AUTHORIZATION.md)) |
| `REQUEST_CHANGES` | A defect, an inaccurate claim or a missing required test |
| `REQUEST_SIMPLIFY` | Correct but bigger than needed; name what to delete |
| `CONDITIONALLY_READY` | Only a required GPU run is missing; the Engineer runs it, no Scientist step |

Review once per head. Re-review only material changes. Report each PR's net lines and test/source ratio. With Actions disabled, write `CI: NOT CONFIGURED`; that is never a pass.
