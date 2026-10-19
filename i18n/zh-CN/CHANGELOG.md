# 变更记录（中文）

> 语言：[English](../../CHANGELOG.md) | **简体中文**


## V3.3 — Codex 接管计算实验与宪章精简（2026-10-19）

- 精简中英文 AGENTS，保留双目标、角色边界与长期合并授权。
- 将获授权的本地/Colab CPU/GPU/TPU 执行、结果校验、资源释放及证据 PR 交由 Codex；Scientist 保留科研决策与计算预算。
- 计算细则统一到 GPU_EXPERIMENT.md（保留历史路径）。
- 根据 Scientist 交接仅确认 T4 smoke test；Colab CPU、TPU/PyTorch-XLA、GitHub 自动发布和跨项目复用仍未验证。
- 本轮为文档迁移；其他 V3.2 协议与模板仍待后续同步，不能声称 V3.3 已全量迁移。

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