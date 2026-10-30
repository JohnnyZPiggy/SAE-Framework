# 运行摘要——<run-id>

> 语言：[English](../../../templates/EXPERIMENT_REPORT.md) | **简体中文**
> 在算法项目中保存为 `reports/<run-id>/summary.md`，旁边放一个结果文件。证据上限见[简洁契约 §3](../governance/SIMPLICITY_CONTRACT.md#3-证据git-就是完整性层)。

**Issue / PR：** #<编号> / #<编号> · **源码 SHA：** `<40 位>` · **状态：** PASS / FAIL / NOT RUN / BLOCKED

## 环境
实际观测设备（型号、显存、计算能力）；驱动 / CUDA / PyTorch 版本写一行；dtype；种子；命令。

## 正确性
参考、容差、最大绝对 / 相对误差、失败数。

## 计时（仅在声称速度时）
规模、预热、同步、重复次数、中位数（必要时加 p95）、编译时间、同精度基线。

## 结果
| 配置 | 指标 | 数值 |
|---|---|---|
| | | |

完整数字：`results.json` / `results.csv`。

## 失败与清理
- `尝试 — 原因 — 修复`（或"无"）
- 清理：活动会话 前 → 后，`cleanup_confirmed`。
