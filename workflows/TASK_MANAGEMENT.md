# GitHub Tasks and Handoff — One Shared Queue

> English (normative) | [简体中文](../i18n/zh-CN/workflows/TASK_MANAGEMENT.md)

**GitHub Issues and PRs are the only durable multi-agent task/evidence queue.** No additional status service, unattended scheduler, GitHub Actions or Drive synchronization.

## Minimal task metadata

Labels **when supported** (do not assume they exist):
- owner: `agent:codex` / `agent:architect` / `human:scientist`
- state: `status:ready` / `status:in-progress` / `status:review` / `status:experiment` / `status:blocked` / `status:accepted`
- optional priority: `priority:p0` / `priority:p1` / `priority:p2`

If labels are unavailable, use explicit Owner/Status/Priority in Issue text. One active owner, explicit next task, stable Issue/PR references, no duplicate tasks.

## Lifecycle (may iterate)

1. **Math gate:** for new/major algorithms, Mentor's `docs/research/<algorithm>-tensorization.md` and Scientist `RESEARCH_READY` (or documented narrow exception) must precede Codex implementation Issues. [Research Pipeline](RESEARCH_PIPELINE.md).
2. **Architect:** design interfaces/tests, [Ecosystem Review](ECOSYSTEM_REVIEW.md), create scoped Codex Issue with acceptance conditions and relevant source SHA.
3. **Codex:** claim the Issue, run actual CPU/oracle/packaging/CLI tests, write `docs/engineering/<algorithm>-engineering.md`, open reviewable PR and mark missing evidence honestly.
4. **Architect:** inspect real PR diff and [Code Review](CODE_REVIEW.md); if applicable approve GPU_READY after the [gate](../templates/GPU_READINESS.md).
5. **Scientist:** execute real Colab and optionally publish report PR after inspecting results; [Colab Contract](COLAB_TWO_COMMAND.md).
6. **Architect:** apply the [Standing Authorization](../governance/STANDING_AUTHORIZATION.md), decide final MERGE / DO_NOT_MERGE, audit evidence and verify merge SHA. Scientific/security **content approvals** remain Scientist-owned; Codex does not self-merge.

Link the [three existing artifacts](THREE_ARTIFACT_HANDOFF.md); don't add a fourth report. A new review/GPU failure can return to earlier steps, not blindly continue. Finish with one [Next Action](NEXT_ACTION.md) after [Role Recovery](ROLE_RECOVERY.md).
