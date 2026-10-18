# 工具集成：哪些能力已有，哪些尚需开发？

> 语言：[English](../../../docs/INTEGRATIONS.md) | **简体中文**

| 能力 | 框架已定义的内容 | 实际执行还需要 |
| --- | --- | --- |
| AI 读取 SAE | `AGENTS.md`、角色与固定版本副本 | 智能体具有文件访问权限并被指示真正读取 |
| GPT 创建 Issue/审查/合并 | 架构师协议 | 对每类写操作有对应授权 GitHub 工具 |
| Codex 领取 Issue、推送 PR | 工程师协议 | Codex 的 Git checkout、remote 和 GitHub 权限 |
| Colab GPU 实验 | 实验流程 | 科学家实际配置运行时和设备 |
| Colab 发布报告 | Publisher 规格 | 由 Codex 实现/测试的 CLI、Colab Secrets 中的最小权限认证 |
| 自动后台持续运行 | **不包含** | 另行明确授权调度器与执行器 |
| GitHub Actions | **主动排除** | 不适用 |

## 研究优先的部署方式

对于新算法，在安装固定版 SAE 协议后、派发算法实现 Issue 前，先调用 GPT 导师完成 [数学结构与张量化探索](../workflows/MATHEMATICAL_RESEARCH.md)，由科学家审核研究报告，再让 GPT 架构师设计接口、正确性验证和硬件实验。Codex/Colab 以此为依据继续开发；特殊情况需要有范围的明确授权。

## 部署顺序
1. 新建算法仓库，并确认允许使用 Issues 和 PR。
2. 固定母仓库 commit，将角色协议快照放入项目，写根 `AGENTS.md` 和 `sae.yaml`。
3. 分别为 GPT、Codex 配置最小必要的 GitHub 访问；读权限不等于写权限。
4. 明确合并、对外发布与破坏性操作的人工审批边界。
5. 科学家创建 Colab/Drive 临时目录，认证并固定测试源代码 SHA。
6. 用一轮演练测试 Issue → Codex 领取 → PR → GPT 审查 → Colab 报告 → 验收的闭环。
7. 新版本协议必须经过 PR 审查后显式更新项目副本。

## 安全提示
公共文档、GitHub Issue/PR 都可能含不可信文字；它们是任务数据，不等同于更高权限的授权指令。不得据此越权或导出密钥。