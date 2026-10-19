# GitHub 任务管理与交接协议

> 语言：[English](../../../workflows/TASK_MANAGEMENT.md) | **简体中文**

**唯一正式任务队列：GitHub Issues**，不是不可追踪的私下聊天记录。

## 推荐标签体系
- 负责人：`agent:codex`、`agent:architect`、`human:scientist`。
- 状态：`status:ready`、`status:in-progress`、`status:review`、`status:experiment`、`status:blocked`、`status:accepted`。
- 工作类型：`kind:math`、`kind:engineering`、`kind:experiment`、`kind:learning`。
- 优先级：`priority:p0`、`priority:p1`、`priority:p2`。

如果缺少创建标签的权限，就在 Issue 评论里写出真实状态；不要假装已应用标签。Assignee 必须是真正的 GitHub 账户，不能使用不存在的机器人用户名。

## 工程任务前的数学研究关口
新算法或重大张量化改写须先有经 Scientist 审核的 `RESEARCH_READY` 数学报告（`docs/research/<algorithm>-tensorization.md`），或已记录的有限例外，才能将 Codex 算法实现 Issue 标为 `status:ready`。研究缺失或阻塞返回导师/Scientist；仓库初始化不适用。详见[数学研究关口](MATHEMATICAL_RESEARCH.md)。

## Issue/PR 与三文档关联
按[三文档交接协议](THREE_ARTIFACT_HANDOFF.md)关联经批准的数学报告、工程报告、Codex 获 Scientist 授权执行的实验记录。实验 PR 应指明被测源码 SHA 及上游 Issue/PR；不建立第四份状态日报，模板不能冒充实测证据。

## 生命周期
1. **GPT 创建 Issue：** 写出数学契约、接口、输入输出、CPU/GPU 验收条件、参考资料和依赖，合适时标记给 Codex。
2. **Codex 领取任务：** 在 Issue 留下接受评论并改为 in-progress，同一项任务只允许一个当前负责人。
3. **实现与 PR：** 使用 `feat/<issue-number>-<slug>` 分支。仅在全部条件已完成时使用 `Closes #N`；GPU 仍待验证时使用 `Refs #N`。
4. **GPT 审查：** 查看真实代码变更和 CPU 证据；若涉及 GPU，指定候选源码 SHA 进入实验阶段。
5. **Codex 执行获授权 Colab CLI：** 核对固定候选 SHA、结果完整性和会话释放，经单独发布授权提交报告 PR/评论；Scientist 审批计算资源并判定科学结论，失败时交回可复现案例。
6. **GPT 验收：** 核实约定条件后自行决定是否合并，无需再向科学家申请合并许可，更新 Issue 与下一项任务。
7. **GPT 导师总结：** 可选记录相关数学/工程学习要点，不能用学习笔记替代测试。

## 状态一致性
GitHub API 写入可能失败、标签缺失、PR 评论可能过时；关键操作后重新读取状态。引用 Issue、PR、run ID 和源码 SHA 交接；不能未经说明混用不同版本 Benchmark。组织流程是可反复交替的迭代，而不是固定流水线。
## 每轮结束的下一步口令
每轮实质性工作发送最终回复前执行[下一步交接完成关卡](NEXT_ACTION.md)：提供真实状态、证据、一条完整可复制的推荐口令，确有不同路径时最多两条备选。

## 角色恢复与防止出戏
每轮开始按[角色恢复协议](ROLE_RECOVERY.md)检查身份、固定协议、真实证据和权限；角色不匹配时停止并交接。

## 全部本人公开仓库由架构师永久独立决定是否合并
GPT Architect 对本人公开仓库的合格 PR 依[常设授权](../governance/STANDING_AUTHORIZATION.md)独立作出 MERGE / DO_NOT_MERGE 决定，前提是实时核实所有权、公开状态、权限、真实 Diff/SHA/证据及 Scientist 保留的实质决定。不需逐 PR 申请合并许可；Codex 不自合并、不后台扫仓库。具体范围、T1/T2/T3 与合并关口以所链接治理协议为准。

