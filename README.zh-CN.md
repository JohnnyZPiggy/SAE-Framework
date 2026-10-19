# SAE Framework V3.2（中文）

**One Project, Two Outcomes: Better Software, Better Scientist.**

SAE 是一个 **Scientist–Architect–Engineer** 科研协作工作流，目标是数学上可靠、工程上可复现、可以利用 PyTorch 张量运算跨硬件加速的仿真与优化算法。GPT Mentor 研究数学，GPT Architect 设计与审核，Codex 工程实现并实测 CPU，Scientist 负责科研判断与真实 Colab GPU 实验。

![SAE 中文架构图](docs/figures/SAE_Framework_V3.2.zh-CN.svg)

## 如何使用

1. 阅读 [AGENTS（中文）](i18n/zh-CN/AGENTS.zh-CN.md) 和 [初始化说明](i18n/zh-CN/SAE_BOOTSTRAP.md)；新算法仓库固定一份 `.sae/` 快照。
2. 在明确的项目上使用 `推进导师工作`、`推进架构师工作` 或 `推进工程师工作`。每次执行前从 GitHub 恢复身份、任务与阶段。
3. **先数学 → Codex CPU 正确性与打包 → 架构师 GPU_READY → Scientist Colab GPU**。数学报告、工程报告、真实实验报告三份相互关联。

## Colab 三个操作 Cell（目前是目标接口）

```python
!pip install "git+https://github.com/OWNER/REPO.git@<EXACT_SOURCE_COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>
!python -m <package>.benchmarks.publish --report-dir reports/gpu/<run-id>
```

第三步是**审核后自愿上传**，不能自动并入 Benchmark。凭证在 Colab Secrets 中命名为 **`GITHUB_TOKEN`**；`!python` 子进程不保证直接读取 Secret，必要时使用 [GPU 实验规范](i18n/zh-CN/workflows/GPU_EXPERIMENT.md)的安全单 Cell Python 备用方式。

**重要：** 本仓库目前主要是文档和模板；Bootstrap、Benchmark/Publisher 的目标命令不等于已实现并测试通过。

## 主要规范入口

| 主题 | 权威文件 |
| --- | --- |
| 角色与共同规则 | [AGENTS](i18n/zh-CN/AGENTS.zh-CN.md) · [角色协议](i18n/zh-CN/protocols/ARCHITECT.md) |
| 恢复身份、GitHub 状态与下一步口令 | [角色恢复](i18n/zh-CN/workflows/ROLE_RECOVERY.md) |
| 数学到 CPU/GPU 研究流程 | [研究管线](i18n/zh-CN/workflows/RESEARCH_PIPELINE.md) |
| Build-vs-Reuse | [生态评估](i18n/zh-CN/workflows/ECOSYSTEM_REVIEW.md) |
| 任务、PR 与审核 | [任务管理](i18n/zh-CN/workflows/TASK_MANAGEMENT.md) |
| Colab、证据与报告上传 | [GPU 实验规范](i18n/zh-CN/workflows/GPU_EXPERIMENT.md) |
| 所有本人公开仓库、无限期可撤销合并授权 | [治理协议](i18n/zh-CN/governance/STANDING_AUTHORIZATION.md) |

**工程原则：** CPU 优先、GPU 按需、尽量用 PyTorch 原生生态、无 GitHub Actions、不伪造结果、不绑定单一 GPU 厂商。科学家保留数学与重要安全决策权，架构师独立做技术合并决定，Codex 不自我合并。

[路线图](i18n/zh-CN/docs/ROADMAP.md) · [英文规范](README.md) · [语言政策](docs/LANGUAGE_POLICY.md)

*尚未选定总体 LICENSE，公开可见不等于允许他人任意再分发。*
