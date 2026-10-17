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
- `experiments.drive_sync: false`：Drive 不参与跨 Agent 文件同步。
- `objectives.*: true`：同时追求工程生产力与科学学习。

**重要：** 中文仅用于解释，正式校验工具只读取标准 YAML 配置。