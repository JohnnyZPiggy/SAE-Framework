# 人类科学家协议（V3.3）

> [English](../../../protocols/SCIENTIST.md) 为规范版本 | 简体中文译本

Scientist 是项目负责人和最终科学决策者，**不再是日常 Colab 操作者**。

## 保留的决定权
- 选择科研问题，批准数学假设、研究关口（`RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`）及科学结论。
- 与 GPT Mentor/Architect 制定实验问题、精度/性能取舍、基线和验收标准。
- 已授予可撤销的 [No Price Gate Colab 常设计算授权](../../../workflows/GPU_EXPERIMENT.md)，覆盖现有账户权益内的 CPU/GPU/TPU；不再逐次审批价格、金额、时长和额度。默认最多一个并发会话、由任务设定有限超时；Scientist 可设更严格限制或随时撤销。充值、新订阅及新增按量收费须另获明确批准。
- 保留重要治理、安全、许可、破坏性变更和敏感对外发布的实质决策。GPT Architect 依[常设授权](../../../governance/STANDING_AUTHORIZATION.md)独立决定最终 PR 合并。

## 委托执行
Codex 执行本地 CPU 与获授权的 Colab CLI CPU/GPU/TPU 实验，下载和校验结果，释放会话，并通过 GitHub 分支/PR 提交证据。Scientist 审核科研意义，可要求重跑或解释，无需日常操作 Notebook 或搬运文件。

参见[计算实验](../../../workflows/GPU_EXPERIMENT.md)、[数学研究](../../../workflows/MATHEMATICAL_RESEARCH.md)和[三文档交接](../../../workflows/THREE_ARTIFACT_HANDOFF.md)。Drive 仅为可选 Notebook/临时工作空间，不作为结果交换层。

只有真实测试后才能标记硬件或发布能力为已验证。截至 2026-10-19，TPU/PyTorch-XLA 和 GitHub 自动发布端到端仍未验证。
