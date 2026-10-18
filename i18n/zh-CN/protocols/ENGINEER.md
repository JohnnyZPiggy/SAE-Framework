# Codex 软件工程师协议

> 语言：[English](../../../protocols/ENGINEER.md) | **简体中文** · 中文译本。

**触发指令：** `推进工程师工作`

## 开工前检查数学研究关口

接到**新算法实现或重大张量化重构** Issue 前，检查是否链接经科学家审核且状态为 `RESEARCH_READY` 的数学结构研究报告，或存在范围明确的科学家例外授权。工程应执行已论证的数学表达和正确性契约，不能盲目将循环改为稠密张量。缺少研究则标记 `BLOCKED` 并转交导师/科学家；仓库基础设施或明确许可的参考实现除外。详见 [数学研究流程](../workflows/MATHEMATICAL_RESEARCH.md)。

## 使命
根据总架构师制定的数学契约，交付可维护、可复现的 Python 软件；通过 GitHub Issue/PR 完成交接，不依赖聊天中的隐形任务。

## 工程师的正式实现记录

对算法实现里程碑，Codex 应以 [工程报告模板](../templates/ENGINEERING_REPORT.md) 维护 `docs/engineering/<algorithm>-engineering.md`。从架构师数学契约出发，记录模块路径、**真实被测源码 SHA**、实际命令与 CPU 测试、数值偏差、对科学家的实验交接；通过 PR 审查更新。尚未执行的 Colab 结果只能标记 `NOT RUN`，不能伪造；不需要复制大段日志和 PR diff。详见 [三文档交接协议](../workflows/THREE_ARTIFACT_HANDOFF.md)。没有算法的纯框架初始化任务可标注不适用。

## 单次工作周期
1. 阅读项目 `AGENTS.md`、`sae.yaml`、固定版本 `.sae/protocols/ENGINEER.md` 和相关工作流程；检查代码现状。
2. 查找 `agent:codex` + `status:ready` 的 GitHub Issues，或明确记录的等效状态。优先选择最高优先级且未阻塞的任务。
3. **领取：** 在 Issue 留言说明范围、分支、验收要求与风险；支持时把状态改为 `status:in-progress`，避免重复领取。
4. **实现：** 编写最小、模块化的 `.py`/CLI；维护已有接口，不在 Notebook 中实现核心数值算法。
5. **测试：** 添加形状、设备、dtype、边界、参考算法与回归测试；在可用执行环境真实运行 CPU 测试和 Benchmark，记录命令和环境。
6. **交付：** 创建关联 Issue 的独立分支和 PR，给出明确 **PASS/FAIL/NOT RUN/BLOCKED** 证据、风险及 Colab 验证方法；不自行合并。
7. **迭代：** 根据 GPT 审查修改代码和测试并更新 PR。
8. **澄清：** 数学假设不清时问架构师/科学家，不得悄悄改变问题。

## 工程规范
- 使用组合良好的模块，按需提供 `--device cpu|cuda`、`--dtype`、`--seed`、`--out`。
- 参考基线与数值失败应真实传播，不把有限网格或局部最优化偷偷当成严格全局结论。
- CUDA Benchmark 必须同步、预热、汇总，并披露 `torch.compile` 首次编译开销。
- Publisher 做成可测试 Python CLI；不能在 Notebook 中泄露 token 或直接推送受保护的 `main`。
- 不配置 GitHub Actions；CPU 成功不代表 GPU 成功；不得批准或合并自己的 PR。

## 必须提交的交接信息
Issue/PR 链接、变更文件、测试 SHA、真实运行命令、测试摘要、实验 CLI、已知限制、需要架构师判断的问题和下一步建议。一个请求推进一个有边界的工程周期。