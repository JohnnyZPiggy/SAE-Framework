# 性能补丁——`torch.compile` 之后的 Triton（V3.4）

> [English](../../../workflows/PERFORMANCE.md) 为规范版本 | 简体中文译本

适用于任何 PyTorch 项目的可选维护环节。它**只**加速 `torch.compile` 之后仍然慢的热点：手写一个小的 GPU kernel 作为**补丁**加进去，绝不重写。"没有收益"也是有效结果，同样要记录。

## 何时启动
三条同时满足：
1. **代码已稳定。** 功能已合并且稳定，通常在里程碑结束时。功能开发进行中不启动。
2. **热点有实测。** 在目标 GPU 上、精确 SHA、真实规模下跑一次 `torch.profiler`，指出具体算子或区域及其占端到端时间的比例。
3. **先试过 compile。** 该区域已经在 `torch.compile`（默认模式和 `max-autotune`）下运行过，仍然是热点。

然后 Architect **每个算子派一个 Issue**，使用 `VALIDATE` 模式（[任务](TASKS.md)），通常规模为 `M`。如果加速需要对算法本身重新表述，而不只是给同一算法写更快的 kernel，先走[研究](RESEARCH.md)流程。

## 补丁规则
- **PyTorch 实现保留。** 它是 oracle，也是 fallback。kernel 是现有公开函数内部的快速路径：设备为 CUDA 且能导入 Triton 时走 kernel，否则走 PyTorch 路径。
- **Triton 是可选依赖**（例如 `[triton]` extra）。CPU、Mac 和无 GPU 的用户感觉不到任何变化。
- **一个补丁只换一个算子，签名不变。** 调用方不改。
- **Triton 优先。** 只有 Issue 写明 Triton 不够用的原因时才用 CUDA C++。
- 只有 kernel 必须与 `torch.compile` 或 autograd 组合时，才通过 `torch.library`（例如 `triton_op`）注册。如果算子需要梯度，补丁要么提供 backward，要么只用于 no-grad 路径，按 Issue 的规定。

## 验收（写在 Issue 里，Engineer 不得修改）
1. **Oracle。** 在随机输入上、小规模和真实规模各一组、每个发布的 dtype，都与 PyTorch 参考实现一致，误差在 Issue 规定的容差内。*额外加一个规模的具体风险：* kernel 常在规模不是 block 大小整数倍时出错，所以要包含一个这样的规模。
2. **Benchmark。** 使用项目里唯一一个由 Architect 编写或批准的 benchmark 脚本：预热、CUDA 同步（或 `triton.testing.do_bench`）、多次重复取中位数、至少三个规模、记录实际观测的 GPU 型号。**基线是经过 `torch.compile` 的 PyTorch 路径**，不是 eager，dtype 和精度相同。编译时间单独报告。
3. **阈值。** 在剖析所用的工作负载上，至少一种目标 GPU 端到端提速 **≥ 1.3×**，且测试的任何规模都不比基线慢。如果某些规模更慢，公开函数按规模分派；否则不合并。

证据不超过[计算的上限](COMPUTE.md#证据)。

## 每次尝试都记录
无论是否合并，都在项目的 `docs/performance.md` 追加一行：

`日期 · 算子 · GPU · compile 基线 → 补丁（中位数）· ACCEPTED / NO_GAIN · PR`

标为 `NO_GAIN` 的算子不再重试，除非 GPU 代际、PyTorch/Triton 版本或算法本身有实质变化。
