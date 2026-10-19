# SAE Framework V3.2 工程路线图

> [English](../../../docs/ROADMAP.md) · 简体中文

**目前实际具备：** 角色、治理协议、研究/Colab 契约、三成果模板和固定 `.sae/` 快照示例。**尚不是实际部署的后台 Agent 或已经验收的 CLI**。

## P0：Bootstrap CLI（Codex，[Issue #2](https://github.com/JohnnyZPiggy/SAE-Framework/issues/2)）

- 由固定 Framework SHA 安全、幂等地初始化项目，支持 dry-run、diff、不静默覆盖；
- 生成目标根 AGENTS、`sae.yaml` 和完整固定 `.sae/` 中英文与治理快照；
- 真实验证相对链接、初次/重复初始化、权限不足、配置异常和版本一致性。

## P0：独立 GitHub Publisher（Codex，[Issue #3](https://github.com/JohnnyZPiggy/SAE-Framework/issues/3)）

- 独立 `benchmarks.publish --report-dir`；`benchmarks.run` **不能再内置 `--publish`**；
- 校验四份小报告格式、被测 SHA、体积及秘密/个人信息，安全创建报告分支与 PR，支持幂等和诚实失败状态；
- `GITHUB_TOKEN` 安全从 Colab Secrets 获取，子进程需实测，必要时单 Python Cell 注入 `env`；先完成离线 Mock；
- 不直接写 main、不自动合并或重跑 GPU，Scientist 审核后决定公开实验报告。

## P1：Colab 三个 Cell（Architect 设计 + Codex 打包）

1. 固定 Git SHA pip 安装。
2. 独立 `benchmarks.run --device cuda --out ...`：数值先验验证与真实 GPU 计时，仅生成本地报告。
3. **可选** `benchmarks.publish --report-dir ...`：Scientist 查看结果后自主上传；必要时一个 Python 上传 Cell 安全传 Secret。

权威契约：[GPU 实验与 Colab 三步](../workflows/GPU_EXPERIMENT.md)。CPU 测试属于 Codex，真实 Colab GPU 与 Secret 集成属于 Scientist；实测前保留 `NOT_IMPLEMENTED / NOT_VERIFIED`。

## P1：轻量本地验证

Codex 本地检查 YAML/JSON、Markdown 链接和新项目快照，**不使用 GitHub Actions**。

## P2：可选体验

Issue/PR 状态摘要、科研学习笔记、显式采用的新固定版本迁移。

真正完成 Issue/PR 与测试后才标成功。角色宪章、授权和会话恢复分别只在各自权威文件维护完整规则。
