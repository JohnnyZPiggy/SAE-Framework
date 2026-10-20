# 研究先行、CPU 验证、获授权异构实验（V3.3）

> [English](../../../workflows/RESEARCH_PIPELINE.md) 为规范版本 | 简体中文译本

SAE 采用 **CPU-first**，不代表仅支持 CPU 或 GPU。三个阶段可以循环回退；GitHub 保存证据，不默认使用 GitHub Actions、Drive 同步或后台 Agent。

## I. 数学研究 — Mentor + Scientist
探索数学形式、参考算法、批量/张量算子、matrix-free 结构、稳定性与复杂度。保留既有 `docs/research/<algorithm>-tensorization.md`。Scientist 决定 `RESEARCH_READY`、`RESEARCH_BLOCKED` 或 `NOT_TENSORIZABLE`，可明确批准有限例外。

## II. 工程与 CPU 正确性 — Architect + Codex
Architect 评估生态复用、制定规格并派发 Issue。Codex 实现可安装 Python 模块，真实运行 CPU 参考/边界/随机/dtype 测试、适用时的 `torch.compile`、固定 SHA 干净安装及 Benchmark CLI 冒烟。工程报告记录真实源码 SHA、命令和结果。CPU compile 不证明 GPU/TPU 兼容或加速。

通过数学、数值、打包及实验准备关口后，Architect 才可标记 `ACCELERATOR_READY`（兼容旧 `GPU_READY`）；**准备就绪不等于硬件已验证**。

## III. 设备实验 — Codex 默认执行、Architect 审核
依[实验默认执行](../../../workflows/GPU_EXPERIMENT.md)，Codex 使用现有权益直接进行 CPU/GPU/TPU 实验，**不需要 Scientist 算力授权、常设授权检查或价格预测**。`PROBE_ONLY` 有界设备诊断可早于正式数学研究/Benchmark 准备，但正式性能结论仍需数学和数值验收。默认一个 Colab 活动会话、有限超时、固定 SHA、真实权限、证据校验及会话释放；用户最新停止指令与新增收费独立审批仍有效。TPU/XLA 必须真实测试，菜单选项不代表支持。

遵循[计算实验协议](../../../workflows/GPU_EXPERIMENT.md)：固定 SHA 安装 → **不写 GitHub** 的 Benchmark → 可选、单独授权且经过校验的 GitHub 证据分支/PR。Architect 按[常设授权](../../../governance/STANDING_AUTHORIZATION.md)审核并合并合格 PR；Codex 不自合并。只有真实 GitHub 回执才能称发布成功。

设备问题返回第二阶段，数学问题返回第一阶段。保留数学、工程、实验三份关联证据；如实区分 `PASS` / `FAIL` / `NOT RUN` / `BLOCKED`。Scientist 保留科研结论和重要治理决定，日常算力使用无需人工签批。旧项目 V3.2 固定快照不自动升级。
