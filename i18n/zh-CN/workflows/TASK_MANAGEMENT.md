# GitHub 任务管理与交接

> [English](../../../workflows/TASK_MANAGEMENT.md)（正式规范） | 简体中文

**GitHub Issues/PR 是唯一持久任务与证据队列**，不增加状态数据库、后台调度、GitHub Actions 或 Drive 同步。

标签**仅在实际存在时**使用：`agent:codex` / `agent:architect` / `human:scientist`；`status:ready` / `status:in-progress` / `status:review` / `status:experiment` / `status:blocked` / `status:accepted`；可选 `priority:p0/p1/p2`。没有标签时使用 Issue 正文的 Owner/Status/Priority；避免重复认领和工单。

## 可反复回到早期阶段的生命周期

1. **数学：** 新算法先有导师 `docs/research/<algorithm>-tensorization.md`、Scientist `RESEARCH_READY` 或明确例外，见 [研发流程](RESEARCH_PIPELINE.md)。
2. **架构师：** 研究接口与验收、执行 [生态调查](ECOSYSTEM_REVIEW.md)，建立有来源 SHA、范围与验收条件的 Codex Issue。
3. **Codex：** 认领 Issue，真实运行 CPU/oracle/打包/CLI 测试，更新 `docs/engineering/<algorithm>-engineering.md`，提交可审核 PR；没跑写 NOT_RUN。
4. **架构师：** 根据真实 Diff 和 [技术审核](CODE_REVIEW.md)，必要时审核 [GPU_READY](../templates/GPU_READINESS.md)。
5. **Scientist：** 运行真实 Colab，阅读结果后可选发布报告 PR，见 [三步契约](COLAB_TWO_COMMAND.md)。
6. **架构师：** 按 [常设授权](../governance/STANDING_AUTHORIZATION.md)独立决定 MERGE/DO_NOT_MERGE，留证据、核实 SHA；重要科研/安全**实质决定**仍属于科学家，Codex 不能自我合并。

交接只使用[三份科研成果](THREE_ARTIFACT_HANDOFF.md)，不新增第四份报告。问题允许返回数学/CPU 阶段；每轮遵守 [角色恢复](ROLE_RECOVERY.md)与[下一步口令](NEXT_ACTION.md)。
