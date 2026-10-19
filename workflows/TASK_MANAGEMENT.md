# GitHub Task Management, PR Review and Handoff

> English normative | [简体中文](../i18n/zh-CN/workflows/TASK_MANAGEMENT.md)

**GitHub Issues are the task queue; PRs and linked reports are the review record.** Agent chat is not a parallel task database. Prefer one scoped task per invocation and cross-link the actual source SHA and three research artifacts.

## Small task lifecycle

1. **Discover:** reload repository, issues, PRs and pinned project policy before choosing a task. Suggested optional labels: `agent:codex` / `agent:architect` / `human:scientist`; `status:ready` / `in-progress` / `review` / `experiment` / `blocked` / `accepted`. Without configured labels use explicit Issue text; do not drop tasks.
2. **Research:** new algorithm or major tensorization task first belongs to Mentor/Scientist. Link `docs/research/<algorithm>-tensorization.md` and the Scientist's `RESEARCH_READY` decision or scoped exception. Ordinary bootstrap/setup tasks need no research study.
3. **Architecture:** Architect checks [Ecosystem Review](ECOSYSTEM_REVIEW.md), writes design in the existing engineering report, defines measurable oracle, tolerances, CPU/CLI/benchmark acceptance and the Codex Issue.
4. **Engineering:** Codex claims the Issue, implements and actually tests CPU in its environment, logs exact commands, tested SHA and failure states, opens an evidence-backed PR; **Codex does not merge**.
5. **GPU where necessary:** Architect reviews CPU facts and gates `GPU_READY`. Scientist executes a pinned candidate in [Colab](GPU_EXPERIMENT.md), then optionally publishes four sanitized small report files in a separate report PR.
6. **Architect review and decision:** review the *current full PR diff*, head SHA, actual tests/commit, mathematics, links, secrets, dependencies, license, review threads and GitHub branch protections. Use [Standing Authorization](../governance/STANDING_AUTHORIZATION.md) for live owner/public scope and merge discretion. Record a concise audit; then independently `MERGE_APPROVED` / `DO_NOT_MERGE` / `MERGE_BLOCKED` / `WAITING_FOR_SCIENTIST_DECISION`. Only after passing applicable gates, squash merge with **expected reviewed head SHA** and verify GitHub's merged SHA.
7. **Close the loop:** update the Issue, report what actually happened, select one next role command via [Role Recovery](ROLE_RECOVERY.md).

## Review levels and non-negotiable evidence

| Level | Examples | Required checks |
| --- | --- | --- |
| **T1** | Routine docs, translations, formatting, narrow tests | Actual diff; link/syntax correctness where applicable; no covert policy/security changes |
| **T2** | Algorithm Python, numerical fixes, PyTorch optimization, packaging, benchmark/publisher code | Scientist-reviewed math where relevant; independently executed Codex oracle/edge/regression, CPU compile/install/CLI checks; dependency/license/security review; matching-SHA Scientist GPU evidence *only* if GPU is a PR acceptance requirement or success claim |
| **T3** | Mathematical assumptions, scientific conclusions, standing authorization, GitHub security, licenses/IP, destructive changes, public data disclosure | Record the Scientist's substantive decision **before** accepting the change. Once the decision is made, Architect still determines the *technical merge*; do not ask for a second merge-click approval |

Use the **highest-risk actual effect**, not the PR title. `NOT_RUN` is never `PASS`. CPU-only acceptance may merge with `GPU_NOT_RUN` when GPU is not claimed or required. Reject leaks, missing critical tests, unapproved T3 substance, unresolved blocking reviews, unsupported permissions and unverified repository ownership. For GPT-authored substantive code insist on independent test evidence.

**Small PR audit:** repository/PR · base/head SHA · tier · actual tests/links · Scientist prerequisite (if any) · decision/reason · verified merge SHA or NOT MERGED. No extra standalone report, no mandatory GitHub Actions, no bulk branch merging or force-push.

More detail: [three research artifacts](THREE_ARTIFACT_HANDOFF.md), [Research Pipeline](RESEARCH_PIPELINE.md), [Role Recovery](ROLE_RECOVERY.md).
