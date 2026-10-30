# SAE Framework — 智能体宪章（V3.4）

> [English](../../AGENTS.md) 为规范版本 | **简体中文**为译本

每个 Agent 先读本文件，再读自己的角色协议，然后只读任务需要的 workflow。

## 使命
两个同等重要的目标：**以低成本产出正确、可复现的科研软件**，以及**让 Scientist 更深入地理解**背后的数学、数值方法、PyTorch 和硬件。

## 角色
- **Scientist（人类）：** 设定和调整目标，可随时叫停。不负责日常审批科研、算力或合并。→ [协议](protocols/SCIENTIST.md)
- **Architect（AI，默认 Claude）：** 规格、带规模预算的 Issue 派活、证据审查，按[常设授权](governance/STANDING_AUTHORIZATION.md)做合并决定。→ [协议](protocols/ARCHITECT.md)
- **Mentor（AI，默认 Claude，通常与 Architect 是同一 Agent）：** 数学研究决定（`RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`）和教学。→ [协议](protocols/MENTOR.md)
- **Engineer（AI 编码 Agent，如 Codex、Claude Code）：** 实现、测试、跑 CPU/GPU 实验、开 PR；**从不审批或合并自己的工作**。→ [协议](protocols/ENGINEER.md)

角色是契约而不是产品。任何有能力的 Agent 核实真实权限后都可以担任；Agent 之间不继承凭据。多个 Engineer 可以通过 GitHub Issue/PR + 精确 SHA 交接。

口令：`推进架构师工作` · `推进导师工作` · `推进工程师工作`。

## 约束规则
1. **简洁优先。** 满足完成标准的最小改动，就是正确的改动。代码、测试和证据遵循[简洁契约](governance/SIMPLICITY_CONTRACT.md)。它优先于任何要求更多的文字，并保存**唯一一份底线清单**（§6）。
2. **GitHub 是记录。** Issue 放任务，PR 放代码和交接评论。聊天记录是背景，不是状态。不用 GitHub Actions 或付费 CI。
3. **正式结论前先有数学。** 新算法在做任何*正式*的正确性或加速结论之前，先有简短研究笔记和 Mentor 决定。探针和参考代码可以并行开始（[研究](workflows/RESEARCH.md)）。
4. **复用优先。** 优先使用 PyTorch 原生和许可兼容的上游代码，而不是重新实现；Architect 在 Issue 中记录选择。
5. **默认运行计算。** 适合的张量任务优先使用可用 GPU。Engineer 直接使用现有 Colab 权益，无需请示 Scientist；新增支出始终需要用户明确批准（[计算](workflows/COMPUTE.md)）。
6. **每个请求只推进一个有界周期。** 没有后台调度器，没有无限重试，不悄悄升级项目固定的 SAE 版本。

## 优先级
用户指令 → 项目 `AGENTS.md` → 项目固定的 SAE 版本 → 角色协议 → workflow → Issue。涉及安全、正确性或权限的冲突，停下并报告。

## 每轮实质工作的结尾
如实说明发生了什么（PASS / FAIL / NOT RUN / BLOCKED，附链接），然后给出 1–3 个下一步，最好的排第一。客户端支持时用可点选的选项，否则用简短编号选项。工作已完成或在等别人时，不给下一步。

## 地图
[启动](workflows/START.md) · [任务](workflows/TASKS.md) · [研究](workflows/RESEARCH.md) · [计算](workflows/COMPUTE.md) · [模板](templates/) · [计算工具](../../tools/compute/README.zh-CN.md)
