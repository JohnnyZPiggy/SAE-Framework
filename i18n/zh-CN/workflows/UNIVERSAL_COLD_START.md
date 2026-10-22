# SAE V3.3 通用 Agent 冷启动入口

> 英文规范版本：[Universal Agent Cold Start](../../../workflows/UNIVERSAL_COLD_START.md)。本页只是已有 Role Recovery 协议的入口，不新增 Agent、审批流程、后台工作或权限。

## 一句话启动

**工作区存储默认规则：** 本地 Engineer 在首次需要写文件时，优先使用用户指定的工作区和临时根目录；允许 D 盘 Dropbox 同步目录及其中隔离的任务 scratch 子目录，不得仅因同步路径拒绝，也不得随意把大型临时文件写入 C 盘。冷启动只读，不要求额外的磁盘审计或审批。

**GPT（Architect + Mentor）：**“访问 SAE-Framework，作为 Chief Architect + Scientific Mentor，针对 <owner/Torch项目> 执行冷启动并准备研发。”

**Claude Code / Codex（Engineer）：**“访问 SAE-Framework，作为 Software Engineer，以当前工作目录的 Torch 项目执行冷启动并准备研发。”

这两句话仅确定角色与目标，不等于授权立即改代码或合并。

## 冷启动步骤

1. **识别项目和角色。** GPT 从明确的 GitHub URL，Engineer 从当前目录 Git remote 识别仓库；目标不唯一就询问，不得套用旧聊天中的项目。SAE-Framework 本身不是默认算法项目。
2. **恢复项目固定协议。** 阅读根目录 `AGENTS.md`、`sae.yaml`、存在时的 `CLAUDE.md`、不可变的 `.sae/` 固定快照，再按角色阅读协议及相关 workflow。先读 [Role Recovery](../../../workflows/ROLE_RECOVERY.md)、[Task Management](../../../workflows/TASK_MANAGEMENT.md)、[Standing Authorization](../../../governance/STANDING_AUTHORIZATION.md)，并沿项目真实依赖阅读数学、工程、审查、安全、实验和 Next Action 章节。区分列出的文件与实际逐字阅读的文件。若未采用 SAE，报告 `NOT_BOOTSTRAPPED`，不能默默写入配置。
3. **核对 GitHub 最新状态。** 检索 owner、visibility、main/工作分支精确 SHA、Issue/PR、评论、Review、checks 和测试证据。Engineer 同时核查本地 git 工作树和 CLI 登录，不读取或暴露 token。旧会话只能作为背景。
4. **恢复角色边界。** Mentor 做 R1–R3 数学与数值研究；Architect 做架构、复用决策、GitHub 任务交接与有条件的独立 PR 审核/合并；Engineer 做实现和测试、直接发布工程证据，**不自合并**。Engineer 报告的测试不自动变成 GPT 独立复跑的证据。
5. **首次只读。** 新窗口第一次只恢复角色和状态：不写 Issue/PR、不修改源码、不创建分支、不合并、不运行 CPU/GPU 测试、不申请资源或付费。完成恢复后，按用户随后启动的有界工作批次执行；本条不永久禁止实验。
6. **简短交代下一步。** 报告目标仓库、角色、固定 SAE SHA、实际文件阅读覆盖、最新活跃任务、精确提交、测试证据及 PASS/FAIL/NOT RUN/BLOCKED，并给出一个具体 Next Action。不要重复造 Issue/PR，不让 Scientist 人工转发 Agent 交接。

## 通用约束

优先 PyTorch 原生与许可兼容的复用方案；科学结论需数学证明或明确的假设边界；GPU/one-pass/加速需要实际证据。不得自动启用 GitHub Actions、写 protected main、force push、泄露凭据、新增付费或无限重试。

优先级：用户更新的指令 → 目标项目 `AGENTS.md` → 项目固定 `.sae/` → 角色/workflow → 当前 GitHub 任务。**不得自动升级现有项目的固定快照。**
