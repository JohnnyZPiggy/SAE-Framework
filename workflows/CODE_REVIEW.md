# Technical Review and Merge Gates

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/CODE_REVIEW.md)


## Architect review is evidence-driven — and size-aware
Apply the [Simplicity Contract](../governance/SIMPLICITY_CONTRACT.md). Check first whether the diff is the smallest change that meets the Issue's Definition of Done; then check correctness.

- **Mathematics:** objective, assumptions, invariant, oracle/baseline, proof or counterexample as relevant.
- **Size and simplicity:** net lines vs the Issue budget; validation only at trust boundaries; no banned patterns; test lines ≲ source lines. Ask what can be deleted.
- **API/code:** dtype/device handling at the public API, shape contracts, memory behavior, readability.
- **Correctness:** the Issue's required tests, and an independent reference comparison for numerical claims, with a justified tolerance. Randomized/adversarial suites only when the Issue names the risk.
- **CPU evidence:** actual test commands, results, environment and failing logs where applicable.
- **GPU evidence:** exact tested commit, Colab environment, correctness and performance; **required for any CUDA speedup claim**.
- **Integrity:** real measurements only; distinguish partial tests, unavailable tooling and skipped checks.
- **Security:** no leaked PATs, tokens, private files, fake data or unrestricted publisher scopes.
- **Process:** no GitHub Actions/paid CI, Issue link, coherent PR diff, Architect owner-public merge delegation and real tool permissions; no per-PR Scientist signoff.

## Decision outcome
- **REQUEST_CHANGES:** defects, ambiguities, inaccurate claims or missing required tests.
- **REQUEST_SIMPLIFY:** correct, but larger than needed. Name what to delete (defensive checks, unused abstractions, extra tests, evidence files). A valid outcome in its own right, not a nitpick.
- **CONDITIONALLY_READY:** evidence for a required GPU/formal acceptance condition is NOT RUN; Codex may execute without Scientist approval. CPU-only scope can merge if GPU is not required.
- **ACCEPTED:** required evidence complete; Architect records rationale in one short comment.
- **MERGED:** only after authorized action succeeds. A review comment does not mean merged.

## Merge policy
- The Engineer never self-merges.
- The Architect independently decides eligible T1/T2/T3 PR merges under [Standing Authorization](../governance/STANDING_AUTHORIZATION.md) without Scientist approval; verify real owner/public access, diff/tested SHA, evidence and merge protections.
- Prefer reviewable PR over direct `main` edits, including experiment reports.
- Never force-push protected branches or overwrite others' history.
- If GitHub checks are unavailable because Actions are disabled, display `CI: NOT CONFIGURED (by design)`; this is **not** a passed test.

## Performance gates
Compare identical problem sizes, dtype, correctness level, device, clock/setup and data transfers consistently. Disclose compilation cost, warmup, GPU synchronization, repetitions, distribution and variability. Avoid interpreting raw speedup as numerical quality.
