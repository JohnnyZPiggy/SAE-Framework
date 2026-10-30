# 任务——Issue、PR、模式与审查（V3.4）

> [English](../../../workflows/TASKS.md) 为规范版本 | 简体中文译本

GitHub Issue 放任务，PR 放代码和证据。除此之外没有其他共享状态。

## 一个 Issue → 一个有界的 Engineer 批次
Architect 用[模板](../templates/ISSUE_TEMPLATE.md)写一个 Issue：目标、数学契约、完成标准、规模预算、必需测试、设备和"不需要做"清单。在这个 Issue 内，Engineer 可以反复 实现 → 测试 → 修复 → 重跑，无需新的批准，每类失败最多修复三次。然后开**一个 PR**（`feat/<issue>-<slug>`；完成时写 `Closes #N`，否则写 `Refs #N`），附**一条交接评论**。

- 标签和认领评论都是可选的。只有两个 Agent 可能冲突时才认领。
- 后续工作放在**同一个 Issue** 里，不新建规划 Issue 或状态报告。
- 重要写操作之后重新获取 GitHub 状态，API 调用可能静默失败。
- 不同代码版本的数字不要混用；必须混用时要说明。

## 两种模式，按你想做的结论选择
| | `EXPLORE`——快速证伪 | `VALIDATE`——验收 |
|---|---|---|
| 开始条件 | 一个可检验的假设和最小 oracle | Mentor 给出 `RESEARCH_READY`（或写明的有界假设） |
| 证据 | Issue/PR 里一段简短记录：源码、命令、结果 | 最终 SHA、必需测试、独立 oracle；声称加速时需公平 benchmark |
| 结论 | `HYPOTHESIS` / `PROBE_ONLY`，永远不是正式结果 | Architect 只接受实测结果 |

Architect 根据证据切换模式，不需要额外批准。

## 结果放在哪里（在算法项目中）
- 数学：`docs/research/<algorithm>-tensorization.md`（[模板](../templates/TENSORIZATION_STUDY.md)）。
- 工程：PR 和它的交接评论。不另写工程报告。
- GPU 运行：`reports/<run-id>/summary.md` 加一个结果文件（[模板](../templates/EXPERIMENT_REPORT.md)），不超过[证据上限](../governance/SIMPLICITY_CONTRACT.md#3-证据git-就是完整性层)。

彼此用链接引用，不要互相复制数字。

## 审查
Architect 在精确 head SHA 上一次审完，顺序如下：
1. **规模。** 净增行数对照预算；只在信任边界校验；没有[禁用模式](../governance/SIMPLICITY_CONTRACT.md#禁用模式除非-issue-写明风险)；测试行数 ≲ 源码行数。问一句：哪些可以删？
2. **正确性。** 必需测试在最终 SHA 上通过。数值结论要有独立参考，容差有依据。
3. **设备。** GPU 结论需要在精确 SHA 上跑过，记录实际观测设备，并确认已清理。加速结论要求规模、dtype 和精度相同，并披露预热、同步和编译时间。
4. **诚信与安全。** 只用真实测量；不含密钥和原始 CLI 输出。

| 结论 | 含义 |
|---|---|
| `ACCEPTED` | 证据满足 Issue；符合条件就合并（[常设授权](../governance/STANDING_AUTHORIZATION.md)） |
| `REQUEST_CHANGES` | 有缺陷、结论不准确，或缺少必需测试 |
| `REQUEST_SIMPLIFY` | 正确但比需要的大；指明删什么 |
| `CONDITIONALLY_READY` | 只差一次必需的 GPU 运行；Engineer 去跑，无需 Scientist |

每个 head 只审一次，只有实质改动才重审。报告每个 PR 的净增行数和测试/源码比例。没有 Actions 时写 `CI: NOT CONFIGURED`，这永远不等于通过。
