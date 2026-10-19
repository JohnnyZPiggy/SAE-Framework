# SAE Framework — 简体中文文档导航

> 语言：[English](../../README.md) | **简体中文**

主入口：[**README 中文首页**](../../README.zh-CN.md)。本目录中的文件是与根目录英文规范对应的**中文阅读版本**，用于方便使用者选择阅读语言。

## 快速导航
- **[数学结构探索与张量化研究关口](workflows/MATHEMATICAL_RESEARCH.md)**
- [张量化研究模板](templates/TENSORIZATION_STUDY.md)
- **[Colab CLI 三阶段兼容入口](workflows/COLAB_TWO_COMMAND.md)**
- [初始化协议](SAE_BOOTSTRAP.md)
- [智能体共同规则](AGENTS.zh-CN.md)
- [角色协议：GPT 架构师 / Codex 工程师 / GPT 导师 / 科学家](protocols/)
- [流程：任务 / 审查 / GPU 实验 / 学习 / 安全](workflows/)
- [架构与 Mermaid](docs/ARCHITECTURE.md)
- [工具集成与路线图](docs/INTEGRATIONS.md)
- [模板](templates/)
- [Colab 示例](examples/colab/README.md)
- [项目 AGENTS 示例](examples/project/AGENTS.zh-CN.md)
- [YAML 配置说明](examples/project/SAE_CONFIG.md)

## V3.3 执行职责

Codex 执行获授权的本地及 Colab CLI CPU/GPU/TPU 实验，Scientist 负责科研决策和计算预算；[计算实验协议](workflows/GPU_EXPERIMENT.md)是执行细则。T4 smoke test 已由用户报告验证，TPU、自动发布等尚未验证。

## 哪个语言版本具有执行效力？
**英文根目录是机器读取的规范版本**。保留 `AGENTS.md`、`SAE_BOOTSTRAP.md`、`sae.yaml`、CLI 参数与状态名的真实英文标识。中文文件用于理解与教学，不在缺乏验证的情况下修改实际协议语义。

如中英文产生冲突，请在 GitHub 创建 Issue，并以英文规范文件及科学家的明确授权作为执行依据。
## 本人全部公开仓库的无限期架构师合并裁量权

Scientist 已把 `JohnnyZPiggy` **现有和未来本人全部公开仓库**中合格 PR 的最终 **MERGE / DO_NOT_MERGE** 决定权永久、可撤销地授予 GPT 架构师，**无需逐仓库登记、年度续期或每次再问合并许可**。每个 PR 仍需按照 [常设授权](governance/STANDING_AUTHORIZATION.md) 审查 T1/T2/T3、实际测试和科学家保留的科研/安全实质变更决定。真实 GitHub 权限与分支规则必须遵守；Codex 不自我合并，也无后台操作。
