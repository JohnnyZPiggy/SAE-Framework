# SAE Framework V3.2

> [English](README.md) | 简体中文

**Scientist–Architect–Engineer（SAE）**：服务于数学算法研究、PyTorch 工程化和科学学习的 GitHub-first 多 Agent 协作规范。

**一个项目，两项成果：更好的软件，更强的科学家。**

![SAE Framework V3.2 中文架构图](docs/figures/SAE_Framework_V3.2.zh-CN.svg)

[英文架构图](docs/figures/SAE_Framework_V3.2.en.svg) · [中文架构说明](i18n/zh-CN/docs/ARCHITECTURE.md)

## 默认研发流程

**先研究数学 → Codex 真实 CPU 测试 → 架构师审核 GPU_READY → 科学家 Colab GPU 实验。** 导师发现矩阵/张量结构，架构师设计工程并审核，Codex 实现与 CPU 验证，科学家完成数学和 GPU 科研决定。每个项目关联 [数学研究、工程报告和实验报告](i18n/zh-CN/workflows/THREE_ARTIFACT_HANDOFF.md) 三份成果。完整要求见 [研发流程](i18n/zh-CN/workflows/RESEARCH_PIPELINE.md)。

| 一句话口令 | 角色 | 有边界的一轮工作 |
| --- | --- | --- |
| `推进导师工作` | GPT Mentor | 推导张量化数学、讲解、交接 |
| `推进架构师工作` | GPT Architect | 恢复 GitHub 状态、设计/审查、证据符合后自主决定合并 |
| `推进工程师工作` | Codex Engineer | 实现、真实 CPU 测试、提交 PR，不能自我合并 |

口令不是后台常驻进程，实际操作需工具权限。

## Colab 改为三个独立步骤

1. 用不可变 Git commit SHA 安装算法包；
2. 独立运行 Benchmark，检查数值正确性与性能；
3. **可选：** 确认结果后，使用名为 `GITHUB_TOKEN` 的 Colab Secret 单独上传报告至 GitHub PR。

细节只以 [三步 Colab 协议](i18n/zh-CN/workflows/COLAB_TWO_COMMAND.md) 为准。历史文件名暂不更换，以免破坏引用。默认 Benchmark **不自动上传**；Bootstrap、Publisher CLI 尚不能仅凭协议存在就视为已实现。不使用 GitHub Actions 或 Drive 报告同步。

## 使用入口

1. [共同 AGENTS](AGENTS.md) 与 [中文说明](i18n/zh-CN/AGENTS.zh-CN.md)；
2. [初始化协议](SAE_BOOTSTRAP.md) 与 [中文说明](i18n/zh-CN/SAE_BOOTSTRAP.md)；
3. [项目入口模板](examples/project/AGENTS.md)、[`sae.yaml`](examples/project/sae.yaml) 和 [初始化验收](docs/ADOPTION_SMOKE_TEST.md)；
4. 确保实际连接 GitHub 并读取目标仓库。新项目复制**同一固定 SHA 的完整 `.sae/` 快照**，既有项目不得悄悄升级。

## 各规范的唯一权威来源

| 内容 | 正式文档 |
| --- | --- |
| 角色职责与边界 | [AGENTS](AGENTS.md) · [角色协议](i18n/zh-CN/protocols/) |
| 数学 → CPU → GPU 关口 | [研发流程](i18n/zh-CN/workflows/RESEARCH_PIPELINE.md) |
| 角色恢复与下一步口令 | [角色恢复](i18n/zh-CN/workflows/ROLE_RECOVERY.md) · [下一步](i18n/zh-CN/workflows/NEXT_ACTION.md) |
| PyTorch 生态复用 | [生态调查](i18n/zh-CN/workflows/ECOSYSTEM_REVIEW.md) |
| Colab 和 Secret | [三步协议](i18n/zh-CN/workflows/COLAB_TWO_COMMAND.md) |
| GitHub Issue/PR | [任务管理](i18n/zh-CN/workflows/TASK_MANAGEMENT.md) |
| 合并最终决定权 | [常设授权](i18n/zh-CN/governance/STANDING_AUTHORIZATION.md) |

**常设授权：** 对 `JohnnyZPiggy` **现有和未来全部本人拥有的公开 GitHub 仓库**，GPT Architect 经真实审核后拥有**无限期、可撤销**的最终合并裁量权，不需逐仓库登记或逐 PR 再请示；实际平台权限、严格审查和科学家保留的实质决定仍有效。Codex 不得自我合并。

## 当前状态

本仓库主要是**组织和协作规范**，不是已部署的自动化执行器。没有真实 CPU/GPU 证据不能宣称成功。无后台自动扫仓库、强推、密钥公开或绕过 GitHub 保护。英文文件为机器执行的正式规范，中英文参照 [语言策略](docs/LANGUAGE_POLICY.md)。

[路线图](i18n/zh-CN/docs/ROADMAP.md) · [工具集成](i18n/zh-CN/docs/INTEGRATIONS.md) · [模板](i18n/zh-CN/templates/) · [中文文档索引](i18n/zh-CN/README.md)

**许可：** 仓库当前未指定 LICENSE；公开可见不代表其他人可以任意复制/再分发。
