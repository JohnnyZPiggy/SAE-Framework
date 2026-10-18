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

针对新算法或重大张量化改写，首先形成**由 GPT 科学导师负责的数学结构研究任务/记录**，而不是立即创建交给 `agent:codex` 的实现任务。在标记算法实现 Issue 为 `status:ready` 前，必须链接科学家批准的 `docs/research/<algorithm>-tensorization.md` 与 `RESEARCH_READY` 结论。之后总架构师设计模块、正确性基线和正式实验。报告缺失或阻塞则先返回导师/科学家。仓库初始化等基础设施任务可独立进行。详见 [数学研究关口](MATHEMATICAL_RESEARCH.md)。

## Issue/PR 与三文档关联

经科学家审查的数学报告、架构师/Codex 的工程报告、科学家实际 Colab 运行的实验报告构成可追溯的证据链。见 [三文档交接协议](THREE_ARTIFACT_HANDOFF.md)。工程 Issue/PR 链接数学与工程文档；实验 PR 链接被测源码 SHA 及前两份文档。无需额外建立第四份相互冲突的状态日报，模板也不能充当完成证据。

## 生命周期
1. **GPT 创建 Issue：** 写出数学契约、接口、输入输出、CPU/GPU 验收条件、参考资料和依赖，合适时标记给 Codex。
2. **Codex 领取任务：** 在 Issue 留下接受评论并改为 in-progress，同一项任务只允许一个当前负责人。
3. **实现与 PR：** 使用 `feat/<issue-number>-<slug>` 分支。仅在全部条件已完成时使用 `Closes #N`；GPU 仍待验证时使用 `Refs #N`。
4. **GPT 审查：** 查看真实代码变更和 CPU 证据；若涉及 GPU，指定候选源码 SHA 进入实验阶段。
5. **科学家运行 Colab：** 提交准确对应候选 SHA 的报告 PR/评论，失败则将最小可复现案例交回 Codex。
6. **GPT 验收：** 达到约定条件且获得授权后合并，更新 Issue 与下一项任务。
7. **GPT 导师总结：** 可选记录相关数学/工程学习要点，不能用学习笔记替代测试。

## 状态一致性
GitHub API 写入可能失败、标签缺失、PR 评论可能过时；关键操作后重新读取状态。引用 Issue、PR、run ID 和源码 SHA 交接；不能未经说明混用不同版本 Benchmark。组织流程是可反复交替的迭代，而不是固定流水线。
## 每轮结束的下一步口令

每次完成实质性工作，按照 [下一步口令协议](NEXT_ACTION.md) 给科学家一个最优、可复制的角色口令或人工操作，最多两项备选，并说明已核实状态、GitHub 证据和是否需要科学家批准。GPU_READY 前不得建议科学家重复 GPU 实验；无权限或受阻时如实说明。交互按钮仅在客户端真实支持时使用。
