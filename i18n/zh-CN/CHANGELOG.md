# 变更记录（中文）

> 语言：[English](../../CHANGELOG.md) | **简体中文**

## V3.2 单一权威协议精简整合（2026-10-19）

- 科学家明确纠正了永久合并授权范围：`JohnnyZPiggy` 现在与未来全部本人拥有的公开仓库，无到期日；PR #21 已审核合并，重复的 #20 与早已被 #15 覆盖的 #14 已关闭。合并权的唯一正式定义为[当前治理文件](governance/STANDING_AUTHORIZATION.md)。
- 科学家的 Colab 改为**三个独立步骤**：固定源码 SHA 安装、独立 Benchmark、审核后可选 Publisher。Token 在 Colab Secrets 中命名 `GITHUB_TOKEN`；子进程读取或安全传递必须真实测试。
- 精简和整合角色、Bootstrap、任务管理、PR 审核、会话恢复、实验协议与中英镜像；`CODE_REVIEW.md`、`NEXT_ACTION.md`、`COLAB_TWO_COMMAND.md` 和旧模板路径保留短兼容入口。
- 同步 `sae.yaml`、GitHub Issue 模板、路线图，把工程报告的 Ecosystem Review 调回实现记录之前。不擅自升级已采用算法项目的固定 `.sae/` 快照。
- **仅文档更新：** 未声称 Bootstrap/Publisher CLI 或 CPU/GPU 测试已经实现；不使用 GitHub Actions。

## Colab 双命令执行契约（2026-10-18）

- 规定科学家 Colab 核心实验 **只有两条可执行命令**：pip 安装固定 Git SHA 的算法包；运行一条包含精度检查、GPU 计时、实验报告和按授权上传 GitHub PR 的打包 Python Benchmark 命令。
- 将原来四个逻辑实验阶段封装到 Codex 实现和测试的 Python 模块内；GPT 架构师负责 CLI 设计、派发与验收，科学家做真实 Colab 集成实验。
- 新增中英文 `COLAB_TWO_COMMAND.md`，同步实验协议、Notebook 示例、角色、项目配置和路线图。
- **自动 Publisher 仍未实现**；未真实运行不得声称两行程序/上传已经成功。

## 研究先于工程的流程增强（2026-10-18)

- GPT 科学导师新增**工程前数学结构探索与张量化研究**，重点寻找矩阵向量积、matrix-free、批处理/张量缩并等数学性质，分析顺序依赖。
- 科学家审核 `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE` 研究成果后，总架构师再设计工程与正式实验任务。
- 增加中英双语数学研究流程、模板和 GitHub Issue 表单，更新初始化、角色、交接协议及架构图。
- CPU/GPU 实验可把问题重新送回数学研究；没有实验时不得承诺加速。
- 项目配置增加 `research_gate`；旧算法仓库应明确更新固定版本的 SAE 协议副本。

## SAE Framework V3.2 — 初始公开协议包
- 两个同等重要的目标：**工程生产力**与**科学学习**。
- GPT 同时担任**总架构师**与**科学导师**。
- Codex 负责 Python 模块、CPU 测试、Benchmark 与工程 PR。
- 人类科学家负责 Colab 实验并拥有最终科学决策权。
- 以 GitHub Issues、PR 和简洁 GPU 实验报告作为协作与证据中心。
- Drive 仅为可选 Colab Notebook 临时工作空间；不进行同步。
- 不使用 GitHub Actions/付费托管 CI；采用薄 Notebook；未执行测试不算通过。
- 提供角色指令、安全初始化流程、审核/发布交接规范、模板和项目配置示例。

**兼容性：** V3.2 是组织架构版本，并不表示自动运行服务或 GPU Publisher 已经实现。实际集成仍需工程开发和测试。

## 双语文档更新
README 支持 English / 简体中文选择，并提供中文镜像文档与本地化架构图。**执行规范仍以根目录英文版本为准**。