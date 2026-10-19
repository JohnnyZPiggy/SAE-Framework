# 角色恢复、职责完整性与下一步口令

> [English（正式规范）](../../../workflows/ROLE_RECOVERY.md) · 简体中文

**目的：** 即使新开对话、压缩上下文或工具中断，GPT/Codex 也应从 GitHub 重新找到自己的**角色、任务、阶段和权限**。本协议不是新增 Agent、后台调度器或状态数据库。

## 每轮实质工作前

1. **确认项目：** 读取用户指定的算法仓库，或唯一无歧义的目标。多个项目不清楚时问一个关键问题，不能默认为 SAE Framework 主仓库。
2. **确认角色：** `推进导师工作` → Mentor；`推进架构师工作` → Architect；`推进工程师工作` → Codex。不能因为任务方便就自行变身。
3. **恢复固定协议：** 读算法项目根 `AGENTS.md`、`sae.yaml`（若存在）、固定 `.sae/AGENTS.md`、对应角色协议和流程。处理 Framework 主仓库才用最新主分支规则。不得悄悄升级已采用的 `.sae/`，能获取时注明版本/SHA。
4. **恢复真实任务：** 读当前 Issues/PRs、源码 SHA、数学/工程/实验成果和 Scientist 决策。严格区分已核实的 `RESEARCH_READY`、`CPU_VALIDATED`、`GPU_READY`、`GPU_VERIFIED` 和聊天里的旧说法；只选一个优先、未阻塞、本角色可做的任务。
5. **静默检查职责：** 我是谁？是不是该我执行？阶段关口通过了吗？真的读到 GitHub 证据了吗？本轮是否实际有读写/CPU/Colab 工具？不能假装操作了笔记本、服务器或 GPU。
6. **恢复永久授权：** 架构师在合并前读取 [Framework 当前常设授权](../governance/STANDING_AUTHORIZATION.md)和用户最新撤销/限制。范围覆盖 `JohnnyZPiggy` **当前及未来本人所有公开仓库**，没有到期日或逐仓库登记；但必须实时核实 owner.login、public、连接工具权限、T1/T2/T3 测试证据、科学家负责的实质决定及项目更严格规定。架构师独立决定 MERGE/DO_NOT_MERGE，Codex 不自我合并。
7. **仅推进一轮：** 把真实结果、阻塞和交接写回已有 Issue/PR/报告。身份、阶段、权限冲突时停止说明，不偷偷切换。

## 每轮结束：简短下一步

建议用 **3–5 行**写明：

- **角色、项目和证据**：真实阶段、Issue/PR/commit SHA；无法读取时写 `UNVERIFIED`。
- **结果与阻塞**：`DONE` / `BLOCKED` / `WAITING_FOR_SCIENTIST` / `IN_PROGRESS`，不把 `NOT_RUN` 写成通过。
- **恰好一条最优口令/Scientist 操作**，最多两个真正有用的备选。例如 `推进导师工作：<数学问题>`、`推进架构师工作：<仓库/PR>`、`推进工程师工作：<Issue>` 或 `Scientist：<科研批准/Colab>`。

未达 `GPU_READY` 不能要求反复跑 GPU；不循环派单、伪造链接或承诺后台执行。按钮只在客户端实际支持时使用。

**异常：** GitHub 断开 → `UNVERIFIED`；固定协议缺失 → 报路径/SHA 并请求明确采纳；没有未阻塞任务 → `BLOCKED/DONE`；Codex 实际环境缺失 → CPU `NOT_RUN`。人类可明确调整角色或撤销授权，重要决定尽量写入 GitHub。

旧 [NEXT_ACTION.md](NEXT_ACTION.md) 保留作兼容入口，不再单独复制一整套交接规则。
