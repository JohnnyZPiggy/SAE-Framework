# sae.yaml 配置说明

> [标准 YAML 示例](../../../../examples/project/sae.yaml) · 不翻译配置键名或布尔值。

请先替换项目 `owner/repo`、包名、数学问题，以及**固定的 40 位** `framework.commit_sha`；`main` 不可代替不可变快照。`.sae` 必须是同一个 Framework SHA 的文档，不能悄悄升级。

## 关键配置

- `roles` 与 `objectives`：Scientist、GPT Mentor/Architect、Codex；追求工程质量与科研学习双目标。
- `research_gate`：新算法实现前完成数学与张量化研究，Scientist 选择 `RESEARCH_READY` 或记录限制/例外。
- `collaboration.actions_enabled: false`：不启用 GitHub Actions；`merge_authority_source` 表示仅当仓库实际是 `JohnnyZPiggy` 本人公开仓库且拥有工具权限时，才可依据 [当前常设授权](../../../../governance/STANDING_AUTHORIZATION.md)审核合格 PR 并决定是否合并；其他仓库需另行授权。`scientist_substantive_approval_for_t3` 保留重大科学/安全变更前置批准。
- `experiments.notebook_style: three_step_separate_optional_publish` / `notebook_command_count: 3`：固定 SHA 安装、独立 Benchmark、**可选**第三步上传。
- `benchmark_cli` 只生成本地报告，**不含 `--publish`**；`publisher_invoked_inside_benchmark_cli: false`。`publisher_cli` 独立读取已有报告，`publisher: manual_until_implemented` 表示目前没有验收过的自动上传器。
- `colab_secret_name: GITHUB_TOKEN`：Colab Secrets 中的名称，而不是 token 值；子进程读取必须实际验证或安全注入。参见 [Colab 三步](../workflows/GPU_EXPERIMENT.md)。
- `google_drive_role` / `drive_sync: false`：Drive 只是可选临时 Notebook 工作区，不做跨 Agent 同步。

**此 YAML 是目标配置，不表示对应 CLI 已经实现。**
