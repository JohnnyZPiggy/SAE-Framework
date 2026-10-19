# GitHub 任务管理、PR 审核与交接

> [English（正式规范）](../../../workflows/TASK_MANAGEMENT.md) · 简体中文

**GitHub Issues 是正式任务队列，PR 和相互链接的研究报告是审查记录。** 聊天不能代替任务状态数据库；每次触发只推进一个有边界任务。

## 工作流程

1. **恢复状态：** 读取实际仓库、Issue/PR、固定项目协议。可选使用 `agent:codex`、`agent:architect`、`human:scientist` 和 `status:ready`、`in-progress`、`review`、`experiment`、`blocked`、`accepted`；没有标签时用 Issue 正文恢复任务，不丢单。
2. **数学前置：** 新算法/重大张量化重构先由 Mentor + Scientist 提交 `docs/research/<algorithm>-tensorization.md`，获得 `RESEARCH_READY` 或明确例外，才派给 Codex；基础设施搭建不强制数学研究。
3. **架构设计：** 先做 [生态评估](ECOSYSTEM_REVIEW.md)，把 Build-vs-Reuse、数学/数值 oracle、容差、CPU/CLI/Benchmark 的验收写入工程报告和 Codex Issue。
4. **工程证据：** Codex 认领 Issue，实际 CPU 测试、记录命令、SHA、错误和真实 `PASS/FAIL/NOT_RUN/BLOCKED`，提交关联 PR，**不得自我合并**。
5. **必要的 GPU：** 架构师审核 CPU 并标 `GPU_READY` 后 Scientist 运行固定 SHA 的 [Colab 三步](GPU_EXPERIMENT.md)，审核结果后可选提交报告 PR。
6. **架构师审核与最终决定：** 阅读**当前完整 Diff**、head SHA、测试证据、数学、相对链接、密钥、许可证、依赖和审查线程；按 [长期授权](../governance/STANDING_AUTHORIZATION.md)实时核实 owner/public、GitHub 工具及分支保护，留简短审计，自主决定 `MERGE_APPROVED` / `DO_NOT_MERGE` / `MERGE_BLOCKED` / `WAITING_FOR_SCIENTIST_DECISION`。合格才按**被审 head SHA** Squash Merge，并核验真实 merge SHA。
7. **交接：** 更新 Issue 和状态，按 [角色恢复](ROLE_RECOVERY.md)提供下一步准确口令。

## T1/T2/T3 审核门槛

- **T1 日常文档/小测试：** 审真实变更、链接/格式，并确认没有隐藏权限或安全规则修改。
- **T2 工程实现：** 必要的 Scientist 数学决定、Codex 实际 oracle/边界/回归、编译/干净安装/CLI 测试、许可证/安全和需求；GPU 为验收项或声称已提速时才要求对应 SHA 的 Scientist Colab 证据。纯 CPU 验收允许标 `GPU_NOT_RUN` 后合并，不能声称 GPU 已成功。
- **T3 科研、授权、安全、许可、删除和公开数据：** **变更内容本身**必须先有 Scientist 可核验的实质决定，随后仍由 Architect 自主判断 PR 是否合并，不需要重复询问“允许点合并吗”。

按实际最高风险分类，不根据标题降级；`NOT_RUN` 不等于 `PASS`。GPT 自己写的实质代码仍需独立测试；密钥泄露、缺少必要测试或权限、GitHub 阻塞评论都必须停止。

**审计一小段即可：** 仓库/PR、base/head SHA、等级、真实证据、Science 先决决定、理由、决策、已核验 merge SHA 或 NOT MERGED。不另造第四份报告，不使用 GitHub Actions、后台批量合并或强推。

[三份科研成果](THREE_ARTIFACT_HANDOFF.md) · [研究流程](RESEARCH_PIPELINE.md)
