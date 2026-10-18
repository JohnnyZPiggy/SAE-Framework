# SAE Framework 工程路线图

> 语言：[English](../../../docs/ROADMAP.md) | **简体中文**

**现状：** 本仓库已提供组织架构、角色协议、启动说明和模板。以下工具属于**计划开发**，未完成验收前不得称为已实现。

## P0：安全项目初始化工具（Codex）
- 从母仓库固定 commit 为目标项目生成可审查的初始化结构；
- 支持 dry-run、diff、不会覆盖现有代码；
- 配置项目 AGENTS、sae.yaml、固定协议快照、Issues/PR 模板；
- 对空仓库、已有仓库、权限不足和配置错误进行测试。

## P0：实验结果 Publisher CLI（Codex）
- 验证 report manifest/schema、过滤秘密、控制上传体积；
- 创建 `experiment/<run-id>` 分支、commit 报告、提交 PR 并关联 Issue；
- 只有 GitHub API 确认才宣称成功，支持安全幂等重试；
- 先做离线/mocked CPU 测试，再在明确授权下集成验证。

## P1：双命令 Colab Notebook（GPT 设计 + Codex 封装）

- 首次 GPU/凭证设置后，仅需**两条可执行命令**：从指定 GitHub SHA 运行 pip 安装，再执行 `python -m <package>.benchmarks.run --device cuda --publish`。
- GPT 设计默认参数、参考数值算法、CLI、验证及报告要求；Codex 实现并在本地测试打包、正确性、Benchmark、报告和安全上传，所有逻辑在 `.py` 内部。
- 同一 CLI 内完成设备检查、精度先验验证、同步计时、源码 SHA 溯源及可选 PR 上传，正式版本无需第三条上传命令。
- Codex 提供干净 CPU pip/CLI 测试，科学家提供真实 Colab GPU 与授权上传验证。**目前尚未实现完整功能**。详见 [双命令规范](../workflows/COLAB_TWO_COMMAND.md)。

## P1：机器可验证配置（Codex）
- `sae.yaml`、JSON 实验报告的 Python schema 验证；
- 在 Codex 执行环境/Colab 本地运行，不使用 GitHub Actions。

## P2：体验优化
- Issue/PR 状态摘要 CLI、简洁学习笔记模板；
- 新版本协议升级及兼容性指南。

所有路线图事项需要独立 Issue、负责人、明确验收条件和真实测试结果后才可标记已完成。