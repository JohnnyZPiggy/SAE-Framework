# SAE 新项目初始化协议（V3.3）

> [English](../../SAE_BOOTSTRAP.md) 为规范版本 | 简体中文译本

**指令：** `按照 SAE Framework V3.3 初始化这个项目`

## 输入与检查
确认目标 `owner/repo`、默认分支、科研目标、真实工具权限、现有 AGENTS/配置、Issue/PR 及**真实不可变 SAE commit SHA**。必须实际读取指定版本，不能假设 URL 会自动加载。不得覆盖已有内容或悄悄升级固定快照。

## 固定协议快照
1. 用[项目模板](../../examples/project/AGENTS.md)与[配置](../../examples/project/sae.yaml)建立项目根 `AGENTS.md`、`sae.yaml`，替换全部占位符。
2. 从**同一个固定 SAE commit**复制宪章、Bootstrap、角色、流程、模板、治理、文档、示例和中文镜像至项目 `.sae/`，保留可用相对链接并记录源码 SHA。快照不是执行程序，也不授予凭据。
3. 通过独立分支/PR 提交，不添加 GitHub Actions、付费托管 CI 或 Drive 同步层。
4. 在**目标项目目录**检查固定版本链接及配置，按[初始化验收清单](../../docs/ADOPTION_SMOKE_TEST.md)手动检查；不假设自动 Bootstrap CLI 已实现。

## 研究与工程
- 新算法/重大张量化改造先由 GPT Mentor 完成[数学研究](../../workflows/MATHEMATICAL_RESEARCH.md)，Scientist 审核为 `RESEARCH_READY` 或批准有限例外。
- Architect 进行简短[生态评估](../../workflows/ECOSYSTEM_REVIEW.md)，制定数学/工程契约并建立 GitHub Issue。
- Codex 实现 Python 包、CPU 参考/边界测试和跨设备 Benchmark CLI，并执行获授权的本地及 Colab CLI CPU/GPU/TPU 实验。Scientist 事先批准科学结论与 GPU/TPU 的硬件、并发会话、时长、额度，**不再日常手动跑 Notebook**。
- 按[计算实验协议](../../workflows/GPU_EXPERIMENT.md)执行：固定 SHA 安装 → 不写 GitHub 的 Benchmark → 可选、单独授权的安全报告分支/PR 发布。未实测前不宣称 Publisher、TPU/PyTorch-XLA 或跨项目自动执行可用。
- GitHub 保存任务和证据；Drive 仅为可选 Notebook/临时工作空间。

## 验收与失败
检查根 AGENTS、`sae.yaml`、完整固定 `.sae/` 快照、中英文相对链接、角色恢复、研究关口、初始 Issue、PR 审核和实验/资源计划。Codex 如实记录 CPU/加速器结果；Architect 按[常设授权](../../governance/STANDING_AUTHORIZATION.md)在 Scientist 实质决定与真实权限边界内审核并决定合并。

重复初始化须**幂等**：先检查差异，不静默覆盖、强推、泄密、发布或越权合并。报告 COMPLETED / NOT RUN / BLOCKED 与下一步。旧项目仅通过经审查的固定快照更新选择升级 V3.3。
