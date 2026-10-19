# Technical PR Review — Evidence Gate

> English (normative) | [简体中文](../i18n/zh-CN/workflows/CODE_REVIEW.md)

**Architect reviews actual latest PR diff, changed files, head SHA and Issue acceptance**, not a PR author's summary.

## Evidence checklist

- **Math:** Scientist-approved assumptions and compatible objective/oracle; no silent change to derivations.
- **API/numerics:** shapes, dtype/device, stability, tolerances, edge/regression/reference cases, memory effects.
- **CPU:** real Codex commands/results, relevant `torch.compile` behavior and clean pip/CLI smoke tests. `NOT_RUN` is not `PASS`.
- **GPU:** matching-source-SHA Scientist Colab accuracy and synchronized, warmed-up timing **when GPU verification is claimed or required**. CPU is not GPU evidence.
- **Safety:** no secrets or private data, license/dependency risk checked, no GitHub Actions or unexpected deployment.
- **Platform:** actual GitHub access, branch rules, conflicts, required checks/review threads; `CI: NOT CONFIGURED` must not be called `CI: PASS`.

## Review outcomes

`REQUEST_CHANGES` for defects; `CONDITIONALLY_READY` when an explicit prerequisite remains; `MERGE_APPROVED` or `DO_NOT_MERGE` after complete review; `MERGED` **only after GitHub confirms the merge SHA**.

**Merge authority / T1-T2-T3 scope / auditing is defined only in [Standing Authorization](../governance/STANDING_AUTHORIZATION.md).** GPT Architect makes the final engineering merge decision for eligible PRs; Scientist retains substantive math/security/governance decisions. Codex never self-merges. Use normal PRs and exact head SHA, not direct pushes or force pushes.

For benchmark claims compare equivalent problems, precision and accuracy; show compilation, warmup, synchronization, repetitions, distribution and uncertainty.
