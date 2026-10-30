# 研究——数学、复用与学习（V3.4）

> [English](../../../workflows/RESEARCH.md) 为规范版本 | 简体中文译本

**结构 → 等价张量形式 → 设计 → 实现 → 实测验证。** 这是*正式*结论的证据关口，不是排队审批：参考代码、工具和 `PROBE_ONLY` 设备检查可以同时进行；探针失败也可以让数学重新打开。

## R1——理解问题（Mentor）
读论文或参考算法：目标、维度、数值契约、已有代码。找出真正的算子：matvec/matmul、matrix-free `Ax`、张量收缩、批量独立实例、低秩/稀疏/Kronecker 结构、JVP/VJP/HVP、归约。同时指出障碍：顺序递推、依赖数据的控制流、动态形状、主机同步。

## R2——推导张量形式
把原始形式和候选形式并排写出，标明形状。写出需证明的内容：等价性及其成立范围、稳定性、边界情况、所做的近似。比较三种方案：**参考**、**张量化候选**和**回退**。工作量、内存、数据搬运和编译障碍只能作为假设估计，不能当作实测加速。"没有有用的张量化"也是有效结果。

## R3——决定并交接
用[模板](../templates/TENSORIZATION_STUDY.md)写 `docs/research/<algorithm>-tensorization.md`，决定 `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`，无需 Scientist 签字。交给 Architect：独立 oracle、容差、关键的规模和 dtype。`RESEARCH_READY` 允许正式构建和 benchmark，它本身不是正确性结论。

## 先复用再构建（Architect，与 R1–R2 并行）
简要查三个地方：
1. **PyTorch 原生：** `torch.linalg`、`torch.func`/`vmap`、`torch.sparse`、`torch.compile`。
2. **维护中的库**，只在原生不够用时才查。检查许可、发布活跃度和依赖。
3. **论文或上游的参考代码**，通常作为 *oracle* 而不是依赖。

选 **REUSE / ADAPT / BUILD**，在 Issue 里写一行：来源、版本或 SHA、许可，以及本工作填补的空白。候选最多三个。查不了的包标 `UNVERIFIED`，不要猜。

## 学习
学习与工程并行，同样重要。每个里程碑，Mentor：
1. 挑一个与当前工作相关的概念；
2. 讲解 直觉 → 推导 → 可证伪的预测；
3. 让 Scientist 尝试解释或做一个小检查；
4. 对照预测和实测结果，解释差异（数值、实现、硬件）。

一次只问一个问题。笔记可选，学习永远不能代替测试。
