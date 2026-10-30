# Lean Evidence Policy (SAE V3.3)

> English is normative | [简体中文](../i18n/zh-CN/governance/LEAN_EVIDENCE_POLICY.md)

Evidence exists so an independent reviewer can trust a result. It should be **proportional to risk**, and it should reuse what Git already guarantees. Defensive extras do not add trust; they cost Engineer time, tokens and reviewer attention, and they bury the few facts that matter. Example: on 2026-10-30, one 25-line criterion shipped with about 17k lines of evidence.

This policy **lowers evidence volume, not evidence quality**. The non-negotiables in §8 are unchanged.

## 1. Git is the integrity layer
- An exact commit SHA identifies every tracked byte.
- **Do not** create SHA-256 manifests of Git-tracked files.
- **Do not** create "tested-vs-final blob identity" reports.
- Hash only bytes that live outside Git, and record each one's SHA-256 and byte count in the handoff or summary. Examples: downloaded remote artifacts, built wheels, external datasets, provider outputs.

## 2. Test the final HEAD
- Run the authoritative validation on the PR's final source commit.
- Put evidence in the PR **handoff comment**, plus at most the files allowed by §3.
- If a later commit touches only docs or evidence, say so in one sentence. The reviewer checks it with `git diff --stat <tested>..<head>`.

## 3. Evidence budget by tier
| Tier | Required | Repository evidence files (cap) |
|---|---|---|
| T1 docs / config | Diff, plus the output of the one command that exercises the change (if any) | none |
| T2 code | Test command, pass/fail/skip counts, one-line environment, final SHA | ≤ 3 files, ≤ 200 KB (e.g. `summary.json`, JUnit) |
| Compute / GPU experiment | T2, plus observed device identity, the result data that the conclusions cite, and the session-cleanup readback | ≤ 10 files; raw data only if cited by a conclusion |
| T3 | As the Architect specifies in the Issue, with justification | as specified |

## 4. Failures are a list, not a directory
Report failed attempts in the handoff as `attempt — cause — fix`. Commit failure logs or directories only when the failure is itself a scientific result, for example a falsified hypothesis or a reproducible numerical breakdown.

## 5. Reuse environment checks
- Do not repeat Cold or Warm Start for an unchanged machine, toolchain and pin. Write one line: "environment unchanged since <PR/SHA>".
- Re-check only what changed, plus live account/session state right before a compute allocation.

## 6. No defensive extras
Extra probes, snapshots, backups, dry-runs, smoke tests, baselines, fixtures or gates are added only when:
- **(a)** the Issue requires them, or
- **(b)** they directly test a risk that this specific change introduces.

"Just in case" work is not evidence. When an instruction is ambiguous, take the **lighter reading** and state that choice in one line.

## 7. Architect dispatch duty
- Every dispatch states a short **Definition of Done** and a **Not required** list.
- An Architect may exceed the §3 budget only with a one-sentence justification that names the risk.
- Architect reviews rely on the Git SHA, the test results and independent recomputation, not on manifest volume.

## 8. Unchanged non-negotiables
- Exact source SHA.
- Honest PASS / FAIL / NOT_RUN / BLOCKED.
- Independent oracles for numerical claims.
- Real observed device identity for device claims.
- Confirmed remote-session cleanup.
- No secrets in logs.
- No fabricated or relabelled results.
- No self-merge.

## Precedence
This policy overrides conflicting evidence-volume instructions in project Issues, dispatches and templates **unless** the Issue explicitly justifies the extra evidence under §7. It never relaxes security, correctness, billing or cleanup requirements.
