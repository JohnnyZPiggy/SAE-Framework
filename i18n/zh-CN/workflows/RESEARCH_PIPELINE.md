# SAE 科研先行流程：CPU 优先、GPU 按需

> [English（正式规范）](../../../workflows/RESEARCH_PIPELINE.md) · 简体中文

三阶段是**科研验收关口**，不是自动后台流水线；可按真实阻塞迭代回前一阶段。GitHub Issues/PR 和 [三份成果](THREE_ARTIFACT_HANDOFF.md)保存证据，无 GitHub Actions 或 Drive 同步。

## 第一阶段：数学研究（Mentor + Scientist）

分析原始算法、矩阵向量与 matrix-free、batch、形状、oracle、条件数/稳定性、稀疏/低秩和无法并行的依赖。按 [数学研究流程](MATHEMATICAL_RESEARCH.md)写 `docs/research/<algorithm>-tensorization.md`。

Scientist 决定 `RESEARCH_READY`、`RESEARCH_BLOCKED`、`NOT_TENSORIZABLE` 或明确的有限例外；未经审核不得直接派正式算法加速工程。

## 第二阶段：架构 + Codex 真实 CPU 工程

Architect 先做 [生态评估](ECOSYSTEM_REVIEW.md)，设计数学接口、数值 oracle/容差、依赖取舍和独立 run/publish CLI。Codex 在真实环境执行参考/随机/边界/回归、CPU eager、适用的 `torch.compile`、CPU Benchmark、固定 SHA 干净 pip 安装及 CLI 冒烟，记录被测 SHA、环境和 `PASS/FAIL/NOT_RUN/BLOCKED` 于 `docs/engineering/<algorithm>-engineering.md`。

Architect 按 [GPU Readiness](../templates/GPU_READINESS.md)审核数学、CPU、打包、数据集/预设与 GPU 错误处理，之后才标 `GPU_READY`；**这只是可跑 GPU，不是已验证 GPU**。CPU 可复现的故障先由 Codex 修复，不要求 Scientist 反复测试。

## 第三阶段：Scientist Colab GPU

Scientist 在方便时集中运行，通过 [三步协议](GPU_EXPERIMENT.md)固定 SHA pip 安装 → 独立 Benchmark（数值检查、真实 GPU 计时、只写本地报告）→ **可选独立 Publisher**（审核结果后上传 GitHub PR）。`GITHUB_TOKEN` 是 Colab Secret 名称，子进程路径须真实测试/安全传递。CLI 未实现时标 NOT_IMPLEMENTED/NOT_RUN，不谎称可用。

`reports/gpu/<run-id>/`保存真实 SHA、设备、dtype、随机种子、误差、预热同步和计时。`GPU_VERIFIED` 是实际完成验证，**不等于保证加速**。GPU 问题回第二阶段；数学前提失效回第一阶段。

阶段状态以 GitHub Issue/PR 为准；恢复角色、固定协议和下一步口令统一归 [角色恢复](ROLE_RECOVERY.md)。旧项目固定 `.sae/` 不自动升级。
