# Scientist Protocol — Human Research Owner (V3.3)

> English normative | [简体中文](../i18n/zh-CN/protocols/SCIENTIST.md)

The Scientist is the principal investigator and final scientific decision-maker, **not the routine Colab operator**.

## Reserved decisions
- Select research problems and approve mathematical assumptions, research gates (`RESEARCH_READY`, `RESEARCH_BLOCKED`, `NOT_TENSORIZABLE`) and scientific conclusions.
- Specify experimental questions, accuracy/performance trade-offs, baselines and acceptance criteria with GPT Mentor/Architect.
- **No compute-approval role:** under [Experiment by Default](../workflows/GPU_EXPERIMENT.md), Codex directly executes existing-account CPU/GPU/TPU work with real access and technical readiness. Do not request or validate any Scientist compute approval, including a standing-grant record. Scientist may stop/narrow future work at any time; new purchases/pay-as-you-go charges still require explicit user approval.
- Approve substantive governance, security, licensing, destructive changes and sensitive external publication decisions. GPT Architect retains independent final PR merge discretion under [Standing Authorization](../governance/STANDING_AUTHORIZATION.md).

## Delegated operations
Codex handles local CPU and eligible Colab CLI CPU/GPU/TPU execution, artifact download/integrity checks, session shutdown and GitHub branch/PR evidence submission. Scientist reviews the scientific meaning and may request reruns or clarification, without routinely running notebooks or transferring files.

See [Compute Experiment Protocol](../workflows/GPU_EXPERIMENT.md), [Mathematical Research](../workflows/MATHEMATICAL_RESEARCH.md) and [Three-Artifact Handoff](../workflows/THREE_ARTIFACT_HANDOFF.md). Google Drive is optional notebook/temporary workspace only, not a results exchange layer.

Hardware support and publication must be marked verified only after real tests. TPU/PyTorch-XLA and end-to-end automatic GitHub publishing were not verified as of 2026-10-19.
