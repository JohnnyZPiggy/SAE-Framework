## 项目初始化后的统一验收

固定 SAE 快照必须包含 [三阶段协议](workflows/RESEARCH_PIPELINE.md)、[GPU Readiness](templates/GPU_READINESS.md)、[三文档交接](workflows/THREE_ARTIFACT_HANDOFF.md)、[工程报告模板](templates/ENGINEERING_REPORT.md) 和 [双命令 Colab 契约](workflows/COLAB_TWO_COMMAND.md) 及中英文镜像。复制到项目外部的模板须重写相对链接。Codex 在本地 CPU 真实完成安装、正确性、`torch.compile`、CLI 验收后才允许 GPU_READY。Colab 目标两行命令；Publisher 未实现前上传仍需人工处理。保留自包含 Bootstrap 快照要求。

# SAE V3.2：新项目初始化协议（中文）

> 语言：[English](../../SAE_BOOTSTRAP.md) | **简体中文** · 英文是机器执行规范。

**入口指令：** `按照 SAE Framework V3.2 初始化这个项目`

## 必须确认的输入
- 目标仓库：准确的 `owner/repo` 与默认分支。
- 科学目标：论文/算法、预期 PyTorch 产物（可暂定）。
- 框架来源：`JohnnyZPiggy/SAE-Framework`，必须固定到**实际 release tag 或 commit SHA**，不使用漂移的 `main`。
- 权限：对目标仓库的明确读写授权；Colab 凭证仍由科学家保管。
- 现有文件：除非用户针对具体修改批准，否则全部保留。

## 阶段 0：启动前检查
1. 检查仓库、已有 README/AGENTS、默认分支、Issues/PR、打包与测试结构，以及工具权限。
2. 读取固定版本的框架 `AGENTS.md`、相关角色/流程文档和本初始化文件。**仅提供 URL 不等于已读取。**
3. 明确缺失的先决条件、计划改动与外部副作用；不可凭空假设 GitHub 写入可用。

## 阶段 1：安装固定版本协议
1. 使用 [项目 AGENTS 示例](../../examples/project/AGENTS.md) 创建/更新项目根 `AGENTS.md`。
2. 使用 [配置示例](../../examples/project/sae.yaml) 写入 `sae.yaml`，填上**真实 SHA**、角色及禁用 Actions 规则。
3. 从**同一个固定的母仓库 commit**，把 `AGENTS.md`、`SAE_BOOTSTRAP.md`、`README.md`、`README.zh-CN.md`、`CHANGELOG.md`、`protocols/`、`workflows/`、`templates/`、`docs/`（含架构图）、`examples/`、`i18n/zh-CN/` 作为**完整的轻量文档快照**复制到项目 `.sae/`。不复制并执行 `.github/workflows/`，也不混用不同 commit；不要只留外部链接。
4. 确认 Codex 实际读取项目内的 AGENTS，GPT 通过 GitHub 工具显式读取相应文件。
5. 保留已有内容，在**新分支 + PR** 中提出变更。

## 阶段 1.5：数学结构探索与张量化研究（必需）

对于新算法或实质性张量化重构，在初步搭建仓库/协议之后、给 Codex 派发**算法实现和性能测试任务之前**：
1. 科学家提供或确认论文、参考算法与数学研究目标。
2. GPT 切换**科学导师**模式，按 [数学结构研究流程](workflows/MATHEMATICAL_RESEARCH.md) 找到矩阵向量等算子并推导数学等价、可检验的张量重构。
3. 在目标项目形成 `docs/research/<algorithm>-tensorization.md`（使用 [研究模板](../../templates/TENSORIZATION_STUDY.md) 或 [中文版](templates/TENSORIZATION_STUDY.md)），记录数值判据、算法复杂度、硬件假设、替代方案及不确定性。
4. 科学家审查并决定 `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`，必要时明确批准有限的参考实现例外。
5. GPT 再以总架构师身份设计实现接口、验收测试与 Colab 实验矩阵。**未完成研究关口时不能默认派发重构任务或启动正式性能测试。** 基础设施搭建不受限，后续结果可以返回研究。

## 阶段 2：工程骨架（交给 Codex）
可按需建立 `src/`、`tests/`、`benchmarks/`、`tools/`、`notebooks/`、`reports/`、`docs/`（空目录不受 Git 追踪）。
- 与算法相匹配的 Python 打包/导入结构；
- 实际 CPU 数值正确性、边界和回归测试；
- 支持设备选择、随机种子、结构化输出的实验 CLI；
- **薄 Colab Notebook**：安装指定源码 SHA、设参、调用已测试 CLI、发布报告；Notebook 由 GPT 设计，Python 实现由 Codex 负责；
- 按 [GPU 实验协议](workflows/GPU_EXPERIMENT.md) 设计上传工具；未实现并测试前不得宣称可用；
- 不配置 GitHub Actions、托管 CI 或付费自动化。

## 阶段 3：GitHub 协作配置
- 在权限允许时配置 Issue/PR 模板；不能操作的明确汇报。
- 按 [任务管理协议](workflows/TASK_MANAGEMENT.md) 定义状态、优先级、交接和审核。
- 建立初始 Issues：数学规格、参考基线、CPU 正确性、PyTorch 优化、Colab 实验、结果发布与学习目标。

## 阶段 4：验收和交接
- 在**目标项目的实际目录结构中**检查链接，确认 `.sae/AGENTS.md`、角色、流程、模板、中文镜像及根目录 AGENTS 的路径都可访问；验证 `sae.yaml` 能解析且指向真实不可变版本。可按 [手工初始化验收清单](../../docs/ADOPTION_SMOKE_TEST.md) 检查。
- Codex 跑 CPU 检查并记录真实输出；GPU 留给科学家后续在 Colab 执行。
- 通过 PR 提供审查，合并权限由科学家决定。
- 报告 **已完成 / 未运行 / 被阻塞**、对应 SHA、Issue/PR 链接、尚需的认证步骤。
- 下一阶段使用三条推进指令。

## 幂等与失败
重新初始化必须先检查差异，不能静默覆盖已有文件。删除、force-push、暴露秘密、合并、对外发布均不能凭“默认权限”执行。缺少写权限时，应提供待应用的补丁和清单，并标记尚未提交。

## 初始化成功标准
项目具有项目根 AGENTS、合法 `sae.yaml`、可读取且**固定版本**的协议副本、清晰责任与验收标准、初始 Issue 队列、可审查的工程骨架 PR、Colab/GitHub 报告计划，而且没有 GitHub Actions。

**注意：** 这是一份操作协议，不是自动运行服务。
## Bootstrap 快照中的角色恢复

固定版本的 `.sae/workflows/` 快照必须包含 [角色恢复协议](workflows/ROLE_RECOVERY.md) 与中英文镜像。算法项目 `AGENTS.md` 必须指向 `.sae/workflows/ROLE_RECOVERY.md`。Bootstrap 实现需要检查新对话能恢复角色与任务，不得悄悄升级既有项目。

## 项目固定快照中的生态调查

新算法项目的 `.sae/workflows/` 快照必须包含 [ECOSYSTEM_REVIEW.md](workflows/ECOSYSTEM_REVIEW.md) 和 [中文镜像](i18n/zh-CN/workflows/ECOSYSTEM_REVIEW.md)，固定版本架构师协议和工程报告需包含简短 Build-vs-Reuse 关口；复制后检查相对链接。既有项目不得悄悄自动升级。
