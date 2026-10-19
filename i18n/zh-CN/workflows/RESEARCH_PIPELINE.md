# 研究先行、CPU 验证、获授权异构实验（V3.3）

> [English](../../../workflows/RESEARCH_PIPELINE.md) 为规范版本 | 简体中文译本

SAE 采用 **CPU-first**，不代表仅支持 CPU 或 GPU。三个阶段可以循环回退；GitHub 保存证据，不默认使用 GitHub Actions、Drive 同步或后台 Agent。

## I. 数学研究 — Mentor + Scientist
探索数学形式、参考算法、批量/张量算子、matrix-free 结构、稳定性与复杂度。保留既有 `docs/research/<algorithm>-tensorization.md`。Scientist 决定 `RESEARCH_READY`、`RESEARCH_BLOCKED` 或 `NOT_TENSORIZABLE`，可明确批准有限例外。

## II. 工程与 CPU 正确性 — Architect + Codex
Architect 评估生态复用、制定规格并派发 Issue。Codex 实现可安装 Python 模块，真实运行 CPU 参考/边界/随机/dtype 测试、适用时的 `torch.compile`、固定 SHA 干净安装及 Benchmark CLI 冒烟。工程报告记录真实源码 SHA、命令和结果。CPU compile 不证明 GPU/TPU 兼容或加速。

通过数学、数值、打包及实验准备关口后，Architect 才可标记 `ACCELERATOR_READY`（兼容旧 `GPU_READY`）；**准备就绪不等于硬件已验证**。

## III. 设备实验 — Codex 执行、Scientist 授权、Architect 审核
Scientist 事先批准 GPU/TPU 的设备类型、最大并发会话、时长及额度。Codex 执行获授权的本地/Colab CLI CPU/GPU/TPU 测试，先核实精度再宣称性能；记录 SHA、dtype、设备/环境、预热/同步/编译方法，下载并校验结果，关闭会话并确认资源释放。TPU 须单独验证 PyTorch/XLA 与算子；菜单选项不等于支持。

遵循[计算实验协议](../../../workflows/GPU_EXPERIMENT.md)：固定 SHA 安装 → **不写 GitHub** 的 Benchmark → 可选、单独授权且经过校验的 GitHub 证据分支/PR。Architect 按[常设授权](../../../governance/STANDING_AUTHORIZATION.md)审核并合并合格 PR；Codex 不自合并。只有真实 GitHub 回执才能称发布成功。

设备问题返回第二阶段，数学问题返回第一阶段。保留数学、工程、实验三份关联证据；如实区分 `PASS` / `FAIL` / `NOT RUN` / `BLOCKED`。Scientist 保留科学结论、资源预算及重要治理决定。旧项目 V3.2 固定快照不自动升级。
