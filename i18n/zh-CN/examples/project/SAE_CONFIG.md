# sae.yaml 项目配置说明（中文）

> 语言：[English](../../../../examples/project/sae.yaml) | **简体中文**

`sae.yaml` 是**机器可读取的配置文件**，因此键名、布尔值、状态标识应保持英文与原样，不要把 `actions_enabled` 之类键名翻译成中文。

初始化项目时，请复制 [规范示例](../../../../examples/project/sae.yaml)，替换以下占位符：

- `project.repository`：真实 `owner/repo`。
- `project.name`：项目名称。
- `project.package`：Python 导入包名。
- `project.scientific_goal`：实际研究问题与算法。
- `framework.repository`：母仓库地址。
- `framework.commit_sha`：实际 40 位 Git commit SHA；**不能使用占位符或漂移的 main**。
- `framework.local_snapshot`：项目保存固定版协议的 `.sae` 目录。
- `roles`：Scientist、GPT Architect/Mentor、Codex Engineer。
- `collaboration.actions_enabled: false`：默认不启用 GitHub Actions。
- `experiments.publisher: manual_until_implemented`：上传器开发验收前只允许手动发布。
- `experiments.notebook_style: two_command_orchestrator` 与 `notebook_command_count: 2`：核心 Colab Notebook 两行可执行命令。
- `experiments.install_source: pinned_github_commit_via_pip`：从不可变 Git SHA 通过 pip 安装。
- `experiments.benchmark_cli`：打包好的 Benchmark Python CLI 目标形态（不是保证已实现）。
- `experiments.benchmark_in_pip_package: true`：安装后必须可运行，不能依赖 clone 工作目录。
- `experiments.publisher_invoked_inside_benchmark_cli: true`：最终可选安全 PR 上传内嵌在第二条命令，Publisher 实现前仍手动上传。
- `experiments.drive_sync: false`：Drive 不参与跨 Agent 文件同步。
- `objectives.*: true`：同时追求工程生产力与科学学习。
- `research_gate.required_before_algorithm_engineering: true`：新算法必须先研究数学结构与张量化方案。
- `research_gate.study_path_template`：研究报告应在项目中保存的位置。
- `research_gate.scientist_review_required: true`：科学家审查研究结论后才可派发工程。

**重要：** 中文仅用于解释，正式校验工具只读取标准 YAML 配置。