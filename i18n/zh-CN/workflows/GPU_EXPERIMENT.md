# 计算实验协议 — CPU / GPU / TPU（V3.3）

> 历史文件路径保留兼容 | [English](../../../workflows/GPU_EXPERIMENT.md) 为规范版本

## 职责与前置条件
- **Scientist：** 科研决策、实验目标，以及事先批准硬件、会话数、时长和额度。
- **Architect：** 实验矩阵、准备/验收条件、证据审核及合格 PR 最终合并裁量。
- **Codex：** 本地/Colab CLI 实验、正确性与性能工具、结果下载校验、会话释放和获授权的 GitHub 证据 PR。
- **GitHub：** 共享代码、任务与报告。Drive 仅为可选临时 Notebook 空间。

新算法或重大张量化改造须有 Scientist 审核的[数学研究](../../../workflows/MATHEMATICAL_RESEARCH.md)和 Architect 实验计划。正式加速结论前需完成相关 CPU 正确性/安装及准备检查；未实测的硬件不得宣称验证。

## 三个独立逻辑阶段
1. **固定 SHA 安装：** 在选定本地/Colab 环境安装精确源码版本。
2. **Benchmark：** 运行正确性与性能 CLI，**不写 GitHub**。
3. **可选发布：** 校验结果并满足 Scientist 的相关授权后，只通过独立 GitHub 分支/PR 发布已审查的安全文件。

[三步兼容入口](../../../workflows/COLAB_TWO_COMMAND.md)保留历史文件名。示例 Notebook 命令不代表 CLI 已实现。Codex 可经 Colab CLI 调度上述步骤，无需 Scientist 手动点击。Publisher 在端到端实测前仍为未验证。

## 计算资源与设备
可用时复用 WSL2/Colab CLI OAuth。GPU/TPU 分配前核实 Scientist 批准的设备类型、并发会话、时长及额度；未明确则先请求限制。按任务选 CPU/GPU/TPU，不默认绑定 NVIDIA/CUDA。TPU 须单独验证分配、PyTorch/XLA、算子与数值正确性；CLI 出现 TPU 选项不代表可用。

无论成功、失败或中断，均须尝试停止所有已分配会话、核实最终状态并报告释放失败；不得悄悄留下运行资源。

## 证据
- `manifest.json`：run ID/时间、源码 SHA、Issue/PR、设备、环境、种子、精度、命令、状态与方法。
- `correctness.json`：参考基线、容差、误差及 PASS/FAIL/NOT RUN。
- `benchmark.csv`：规模、单位、重复、预热/同步、median/p95 和适用时的编译开销。
- `summary.md`：真实观察、限制、失败、资源释放与证据链接。
- 下载完整性（如 SHA-256）、本地/远端文件一致性及发布状态。

不提交大型数据、密钥或无必要的日志；数值正确性与公平基线不满足时不得声称加速。

## GitHub 发布与失败
授权后先校验文件结构、大小和秘密信息，创建不可变的独立实验分支/PR，关联源码 SHA、Issue/代码 PR 并核实 API 成功；由 Architect 决定合并。公开仓库的 Draft PR 仍公开。禁止直接写受保护主分支、强推和自合并。凭据仅存安全位置。

上传/API 失败标记 `PUBLISH_FAILED`；未测试硬件标记 `NOT RUN`；缺授权、SHA 不一致或环境不可用标记 `BLOCKED`。资源释放失败必须明确报告。

## 截至 2026-10-19 的验证状态
据用户交接记录，Windows Codex → WSL2 Ubuntu 24.04 → Colab CLI 0.7.4 已完成 T4 GPU smoke test：远端 Python 3.13.15、PyTorch 2.11.0+cu130、CUDA 13.0、1024×1024 float32 matmul（20 次计时，平均 0.736283 ms），JSON/SHA-256 校验通过，停止后活动会话为零。仅证明基本 GPU 远程执行。Colab CPU、TPU v5e1/v6e1 与 PyTorch/XLA、GitHub 自动发布及跨项目复用仍未验证。
