# 变更记录（中文）

> 语言：[English](../../CHANGELOG.md) | **简体中文**


## V3.4 — 仓库整理：一个概念一页（2026-10-30）

- **README 重写**（约 205 → 约 70 行）：SAE 是什么、角色表、V3.4 流程图、仓库地图和状态。删除了过时的 GPT 部署指南。`docs/figures/` 里的架构图保留，图中的 Agent 名称只是举例。
- **17 个 workflow 合并为 4 个：**
  - [启动](workflows/START.md)：冷启动、角色恢复、仅在变化时热启动、计算工具发现、每轮结尾交接、项目采用和可直接粘贴的口令；
  - [任务](workflows/TASKS.md)：Issue、EXPLORE/VALIDATE、结果存放位置、审查；
  - [研究](workflows/RESEARCH.md)：R1–R3、复用优先、学习；
  - [计算](workflows/COMPUTE.md)：算力吞吐政策加实验流程。
- **治理：** 常设授权精简，并入安全规则；算力吞吐政策并入"计算"；简洁契约不变。
- **协议：** 重写 Scientist 和 Mentor 协议；四个协议都改为指向新 workflow；全文删除"GPT 决定"的措辞。
- **删除：**
  - `docs/` 下的文字页面（架构、集成、路线图、语言政策、采用冒烟测试；内容已并入 README 和"启动"）；
  - `reports/`（V3.3 证据目录）；
  - `SAE_BOOTSTRAP.md`（现为"启动 § 在项目中采用 SAE"）；
  - 工程报告和 GPU 就绪模板；
  - `examples/colab`、`examples/reports`；
  - `tools/compute/diagnostics/`（CLI 0.7.4 一次性诊断脚本）。

  这些内容都仍保留在 Git 历史和旧的固定版本中。
- **模板：** 研究笔记和运行摘要只保留必要字段。**示例：** 项目 `AGENTS.md` 带 "Simplicity first" 一节；新增 `sae-README.md` 作为 `.sae/README.md` 模板；`sae.yaml` 精简。
- **计算工具：** README 从 106 行缩到约 50 行，没有失效链接。代码未改动。
- **固定在旧 SAE 版本的项目不受影响。** 升级固定版本时，按 `examples/project/sae-README.md` 把项目 `.sae/README.md` 的链接更新为新文件名。

## V3.4 — 简洁契约：减少防御性代码，Claude 成为默认 Architect（2026-10-30）

- **问题：** V3.3 下 Engineer Agent（Codex）产出的代码、测试和证据远超科研需要——手写 JSON/ASCII 校验器、用 `ast` 解析驱动脚本、测试文件比被测代码还长、为 25 行验收标准提交约 1.7 万行证据。根源在框架：每份文档重复防御性要求、测试清单要求覆盖所有类别、派活没有规模预算、审查只能要求"更多"。
- **新增[简洁契约](governance/SIMPLICITY_CONTRACT.md)**（有约束力，覆盖要求更多的旧文字）：只在信任边界校验、信任内部代码；禁用模式表；每个改动行为一个测试，数值结论加独立 oracle；Git 作为完整性层，证据文件设上限（吸收 PR #70 提出的精简证据规则）；派活附完成标准、S/M/L 规模预算、必需测试和"不需要做"清单；Engineer 超出预算 1.5 倍即停止；新增审查结论 `REQUEST_SIMPLIFY`。底线（SHA、如实状态、oracle、实际观测设备、清理、密钥、不自合并、不新增支出）只陈述一次。
- **重写 Engineer 协议**为六步循环；Architect 协议负责规模预算；代码审查先看规模再看正确性；Issue/PR 模板（仓库内及 `.github/`）精简为引导工作量的字段；GPU 证据缩减为 `summary.md` + 一个结果文件；常设授权 T2 证据改为 Issue 的必需测试。
- **Claude 成为默认 Architect + Mentor**（角色仍与模型无关）。删除各文档重复的算力政策横幅，政策本身不变。
- 示例 `sae.yaml` 升至 `3.4` 并新增 `simplicity` 配置块。已有项目固定版本**不会**自动升级。本次未改动 `tools/compute` 代码。

## V3.3 — Lean Research Lab 第一阶段：Explore / Validate 双模式与 Codex 单批次（2026-10-20）

- 修正新项目 `sae.yaml`：科研决定属于 GPT，不再要求 Scientist 数学/GPU 额度签批，PR 需 Architect 证据审核而非逐次人工授权；新增付费仍需用户同意。保持 V3.3 配置版本，不自动升级旧项目快照。
- 新增双语 Lean Lab（现并入 `workflows/TASKS.md`）：EXPLORE 是有界、可检验假设与简短批次记录，VALIDATE 才要求数学推导、精确 SHA、真实数值及公平性能证据；`PROBE_ONLY` 不代表加速或 TPU 通过。
- 一个现有或新建 Issue 可承载 Codex 有限的实现→测试→修复→复测，默认单 Colab 会话、任务有限超时、有界修复尝试和一次汇总交付；不为每次探索生成新 PR/报告。
- 同步中英文初始化、采用冒烟、GPU Readiness、PR/任务/三文档/研发流程模板。不修改旧算法项目、不增加 Agent、后台服务、Actions、收费资源，也不虚报真实端到端执行。

## V3.3 — 中英文原生卡片式 SVG 架构更新（2026-10-20）

- 原路径替换中英文 `docs/figures/SAE_Framework_V3.3.*.svg`：直接用矢量卡片、图标和箭头还原已确认的 ChatGPT 原生 UI 布局，包含双重目标、Scientist 目标设定、GPT 双重自主决策、Codex 直接执行、CPU/GPU/TPU 及 GitHub 证据回流。
- 本地 SVG XML 解析和渲染预览检查通过，已同步 README 图片展示及架构说明；`.mmd` 与 README Mermaid 仍是逻辑图，不是卡片艺术源文件。
- 显示 PR #33 后最新职责，但不虚报 TPU、Publisher 或跨应用自动闭环已经验证。

## V3.3 — GPT 自主决策快速通道（2026-10-20）

- Scientist 明确将范围内**数学 R1–R3、科研关口、科研结论、工程验收及 T1/T2/T3 PR 决定权**全面委托 GPT Mentor/Architect；Scientist 只设定/调整目标、随时停止，不再承担常规审批。替代此前保留科研/逐环节签核的旧规则，但不扩大本人公开仓库合并范围。
- 快速执行：GPT 自行记录 `RESEARCH_READY / RESEARCH_BLOCKED / NOT_TENSORIZABLE` 或有界假设；数学研究、生态复用、CPU 基准/打包和有界 `PROBE_ONLY` Colab 设备探针可并行。Codex 实测并提交真实证据，GPT 自主验收/合并，不设人类签字及重复 Agent 审批。
- 仍要求真实数值正确性、正式 Benchmark、公平计时、源码 SHA、GitHub/设备权限、非敏感结果、有限会话超时和资源释放，不得虚报。新增收费、非公开敏感披露、外部账户安全权限改变及外部不可逆破坏须用户另外明确指令。不引入后台调度、GitHub Actions 或旧项目固定快照静默升级。
- 已同步中英文角色、治理、研究/计算/评审、任务模板、项目初始化及 README Mermaid；旧 SVG 属此前角色示意图，不作为现行授权规范，如需更新外观另行处理。

## V3.3 — Experiment by Default：取消 Scientist 算力审批（2026-10-20）

- 按用户 T3 明确决定，取代此前 No Price Gate 的“常设授权核验”流程：Codex 在现有账户内直接执行有界 CPU/GPU/TPU 实验，**无须 Scientist 算力许可或查验授权记录**；Architect 派单审核，Scientist 保留科研结论和实质决定。
- 有界的 GPU/TPU-XLA/环境 `PROBE_ONLY` 探针可先于正式数学及 CPU Benchmark 准备开展，但不得冒充数值正确性或正式性能证据。
- 保留真实工具/账户权限、固定 SHA、有限超时、默认单会话、结果证据与会话释放；新增收费及敏感对外发布遵守独立用户/安全审批。旧算法项目固定快照不自动升级，不增加后台调度或 CI。
- 同步中英文角色、治理引用、任务管理、角色恢复、实验报告及 Issue/PR 模板。

> Historical note: superseded by the 2026-10-20 Experiment by Default amendment above.

## V3.3 — No Price Gate 常设 Colab 计算授权（2026-10-20）

- Scientist 明确授予 Codex 使用现有 Colab 账户权益及预付 Compute Units 的可撤销常设授权，用于有范围的 CPU/GPU/TPU 实验；不再要求逐次价格预测、预算数字与额度审批，允许使用既有额度直至实际耗尽。
- 保留数学/CPU 准备、固定 SHA、真实权限检查、默认一个活动会话、有限任务超时、会话清理及诚实设备证据。新订阅、充值、按量计费或其他新增账单须另获授权。
- 同步中英文科研/工程角色、角色恢复、Next-Action 和治理引用；不启动计算、不新增 CI/后台调度、不自动升级算法仓库固定协议快照。

## V3.3 — 协议一致性与文档去重（2026-10-19）

- 把旧版“Scientist 操作 Colab”统一为 V3.3 职责：Codex 仅执行获授权实验，Scientist 保留科研、计算预算与公开发布的实质决定；不分配资源，不宣称实验完成。
- 修正过时的 Benchmark/Publisher 与 Issue/PR 模板；将工程报告第 2a 节移至实现记录之前；删除架构说明中重复内嵌的 Mermaid，保留 README 图和 `.mmd` 源码。
- 完整保留数学研究关口、数值证据、三份科研成果、常设合并范围、交接口令、固定快照及不启用 GitHub Actions 的限制。

## V3.3 — Next-Action Completion Gate（2026-10-19）

- 将 GPT 导师、GPT 架构师与 Codex 工程师每轮结束的状态、证据及一条推荐口令，明确为最终回复前自检项，深度研究或阻塞时也不能忽略。
- 仅在确有不同路线时最多提供两条备选；无真实交互控件时各选项使用独立、可复制的纯文本代码块，不伪装按钮可控制 Codex。
- 仅更新文档；不引入强制输出校验器、后台 Agent、计算资源分配、CI，也不自动更新已固定版本的算法项目。

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