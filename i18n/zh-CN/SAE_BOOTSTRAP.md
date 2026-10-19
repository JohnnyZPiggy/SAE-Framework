# SAE Bootstrap V3.2 — 项目初始化（中文）

> [英文正式规范](../../SAE_BOOTSTRAP.md) · 本文是目标工作流程，不代表 Bootstrap CLI 已经实现。

## 先检查，再修改

确定真实目标 `OWNER/REPO`、默认分支、可用工具、已有文件、算法目标和**固定的 SAE Framework 源码 SHA**。不可把 SAE 主仓库默认为算法仓库；不得直接覆盖原文件。

## 固定版本文档快照

1. 从**同一个 Framework SHA** 复制自包含 `.sae/`，包含 `AGENTS.md`、`protocols/`、`workflows/`、`governance/`、`templates/`、`docs/`、`examples/` 和 `i18n/zh-CN/` 等需要的规范及相关 Bootstrap/README。不能混用不同版本。
2. 使用 [算法项目 AGENTS 示例](../../examples/project/AGENTS.md) 填写目标仓库、固定 SHA 和正确链接；按 [sae.yaml 示例](../../examples/project/sae.yaml)填写配置。**复制后**检查到 `.sae/` 的相对链接、新会话 Role Recovery 与参数，而不仅是原始仓库里是否存在文件。
3. 必须能访问 [角色恢复](workflows/ROLE_RECOVERY.md)、[数学研究](workflows/MATHEMATICAL_RESEARCH.md)、[生态调查](workflows/ECOSYSTEM_REVIEW.md)、[Colab 三步](workflows/GPU_EXPERIMENT.md)、[任务管理](workflows/TASK_MANAGEMENT.md) 和 [三成果交接](workflows/THREE_ARTIFACT_HANDOFF.md)。
4. 中央 [长期授权](governance/STANDING_AUTHORIZATION.md)是科学家的可撤销人类指令；复制文件本身**不会创造 GitHub 工具权限**，也不会使私有或其他所有者仓库自动获得合并权限。不得擅自升级现有算法项目的固定 `.sae/` 流程。

## 数学审批、CPU 工程、Colab 实验

新算法/重大重构：Mentor 与 Scientist 先研究矩阵向量等数学结构，按 [数学模板](../../templates/TENSORIZATION_STUDY.md)提交 `docs/research/<algorithm>-tensorization.md`，Scientist 决定 `RESEARCH_READY`、`RESEARCH_BLOCKED`、`NOT_TENSORIZABLE` 或明确有限例外；未通过不得派发正式算法加速开发 Issue。

Codex 按需要实现可安装 `src/`、`tests/`、`benchmarks/`、`reports/`、`docs/`，真实执行 CPU oracle/边界/回归、适用时 `torch.compile`、CPU Benchmark、固定 SHA 干净 pip 安装与 CLI 测试；GitHub Issue/PR 记录证据。架构师在派单前做 Build-vs-Reuse，审核 GPU_READY，之后 Scientist 按 [三步 Colab 流程](workflows/GPU_EXPERIMENT.md)安装、Benchmark、可选上传。`GITHUB_TOKEN` 必须安全传递，Benchmark 不自动上传。

## 验收与边界

按 [项目采纳检查](docs/ADOPTION_SMOKE_TEST.md)核对 Git SHA、YAML、文件及相对链接、中英文镜像、角色加载、GitHub Issue/PR、测试与真实运行状态。区分 `PASS/FAIL/NOT_RUN/BLOCKED`；无运行不得宣称成功。架构师依据 [当前长期授权](governance/STANDING_AUTHORIZATION.md)真实审核后自主决定 PR 是否合并；科学家保留重要科研/安全内容决定。

重复初始化必须幂等；不能静默覆盖、删除、force-push、暴露 Token、绕过权限或升级快照。不启用 GitHub Actions、Drive 同步和后台执行。Bootstrap CLI / Publisher 仍在 [路线图](docs/ROADMAP.md)的实现范围。
