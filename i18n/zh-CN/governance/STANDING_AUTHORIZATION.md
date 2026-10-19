# 年度常设合并授权 — Scientist → GPT 总架构师

> [English（正式规范）](../../../governance/STANDING_AUTHORIZATION.md) | **简体中文**

## 授权与有效期

**授权人：** 人类 Scientist；**被授权角色：** 在用户主动触发的一轮 SAE 工作中担任 Chief Architect、且本轮实际有 GitHub 权限的 GPT。科学家于 **2026-10-19** 明确指令落实、审查和合并本次初始授权；授权来自科学家而非 AI 的自我声明或复制的文档。

**UTC 有效期：** 2026-10-19 00:00:00 至 **2027-10-18 23:59:59（含）**；于 **2027-10-19 00:00:00** 自动失效，不得自动续期。无法核验日期或真实授权时停止并请科学家确认。

### 精确仓库登记表

| 仓库 | 常设合并权限 | 依据 |
| --- | --- | --- |
| `JohnnyZPiggy/SAE-Framework` | **有效**（须满足下述验收条件） | 科学家 2026-10-19 明确指令 |

**其他仓库全部未授权**，即使 GPT 或 Codex 已连接并有 GitHub 写入权限。未来新增算法仓库必须由科学家明确给出完整 `owner/repo` 并单独授予年度合并权限，再通过**科学家审批的治理 PR**加入上述实时登记表。复制项目的固定 `.sae/` 快照本身**不授予权限**；对算法仓库须核对 Framework 最新登记表、科学家单独授权与算法项目固定协议。Agent 不能自行增加仓库、修改范围、降低审查标准或续期。

本授权仅允许 **用户触发、有边界的架构师工作周期** 内审核并合并合格 PR；**不授予后台执行、额外 GitHub 工具权限、Token、直接 push、force push、删除分支、自动发版或公开实验资料上传权**。科学家可随时明确撤销或缩小范围，新指令优先于旧文件。

## 三级合并权限

按**PR 真实 Diff 中最高风险**分类，而不是标题、标签或作者陈述；混合 PR 取最严格一级。

| 级别 | 典型内容 | GPT 权限 |
| --- | --- | --- |
| **T1 日常** | 文档、翻译、非治理协议澄清、格式、针对性测试、小型不改变行为的修复 | 审核真实 Diff、链接和适用语法/测试证据后**可自主合并** |
| **T2 工程** | 已批准数学方案下的算法实现、数值修复、PyTorch 优化、普通打包、Benchmark、Publisher、低风险兼容依赖 | 数学关口、Codex 真实 CPU 数值/oracle/回归和打包证据、许可安全与 Issue 验收全部通过后**有条件自主合并**。若声明 GPU 已通过或 GPU 是该 PR 明确验收条件，须有科学家 Colab 真实证据；只验收 CPU 的改动可以在 GPU 非必要时合并，但标记 `GPU_NOT_RUN`，不得宣称 GPU 已通过。 |
| **T3 科学家保留** | 科学目标/假设或未验证数学结论；本授权、仓库范围、期限或治理安全策略；GitHub 权限、分支保护、Secrets；重要许可证/IP、高风险依赖、发布版本、破坏性变更、删除、强制推送、未经批准的对外公开 | **年度授权不覆盖。** 必须获得科学家**针对这个 PR 和具体变更范围**的新的明确批准，并遵守 GitHub 实际保护规则。 |

分级或证据不确定则标记 `SCIENTIST_APPROVAL_REQUIRED` 或 `MERGE_BLOCKED`，不得降级风险。Colab 实验报告上传公开仓库仍须科学家单独主动授权，不得用合并授权替代。

## Merge Gate：每个 PR 重新检查

1. **验证授权：** 核验 UTC 日期、精确登记仓库、科学家当前授权、本轮 Architect 身份和用户触发、实际 GitHub 权限、项目 AGENTS 和固定 `.sae/`；不得悄悄升级快照。
2. **读取真实 Diff：** 全部变更文件、base/head SHA、Issue、未解决审查评论、可合并状态、分支保护；不只看 PR 描述或旧消息。
3. **判定风险：** T3 必须有科学家对该 PR 的明确批准；GPT 自己写的“Approved”不算。
4. **核验实际证据：** T1 检查链接、语法和适用测试；T2 检查科学家数学批准或有限例外、Codex 真实运行 CPU oracle/边界/回归、干净安装和适用时 `torch.compile`、许可证/安全，以及 GPU 为验收条件时科学家真实 Colab。**NOT_RUN 不是 PASS**。GPT 自己编写的实质代码也需要 Codex/科学家独立测试，不能自证。
5. **排查阻塞：** Token 泄露、未批准公开数据、科学决策越界、未解决审查、缺少必要测试、不当依赖或绕过 GitHub 保护都必须阻止合并；测试源码 SHA 对应被审 head。
6. **合并前留审计记录：** 在 PR 评论/审查中记录级别、授权、被审核 head SHA、证据、风险和决定。工具不支持就如实说明，必要时写入允许的 Issue/PR 记录，不得假装已留痕。
7. **合并后验证：** 只有 `MERGE_APPROVED` 才执行，默认 **Squash Merge**，使用预期的精确 PR head SHA；合并前再次核查，遵守所有保护规则；GitHub 确认成功并核实合并 SHA 才报 `MERGED`，head/base 变化需重新审核。禁止直接 push 或 force push。

**状态：** `MERGE_APPROVED`、`MERGED`、`MERGE_BLOCKED`、`SCIENTIST_APPROVAL_REQUIRED`、`AUTH_SCOPE_MISSING`、`AUTH_EXPIRED`、`UNVERIFIED`。

**简短 PR 审计模板：**

```text
SAE MERGE GATE
Repo/PR: <owner/repo>#<N>; base/head: <base-sha>/<reviewed-head-sha>
Tier: T1/T2/T3; authority: standing 2026-10-19..2027-10-18 或 Scientist 单次批准 <链接>
Diff/evidence: <实际链接、命令、状态或 NOT RUN>
Decision: MERGE_APPROVED / MERGE_BLOCKED / SCIENTIST_APPROVAL_REQUIRED
Risk: <说明>; result: <已核验合并 SHA 或 NOT MERGED>
```

审计存 GitHub PR/Issue，不增加第四份科研报告，也不强制使用 GitHub Actions。

## 禁止自行修改授权、撤销与新项目

- **本文件及中英文镜像均是 T3 治理内容**。未来修改期限、范围、级别、角色权限和审查条件都必须由科学家另行审批；“仅修改文档”的标题也不能绕过。
- **仅本次初始落地例外：** 科学家 2026-10-19 已明确要求创建、审查并合并本次初始授权 PR；这个指令不能用于未来治理变更。
- 科学家任何时候发出新的明确撤销指令即生效；随后有权限时同步文件与 GitHub 设置。仓库文档不会自动赋予永久连接权。
- 建议在 GitHub 设置保护 `main`，只允许 PR 并禁止强制推送；**这份文档不会自动启用保护**，配置变更本身仍需科学家批准。
- Bootstrap 可以将治理文件放进算法项目的固定快照供**参考**，但不能自动登记或启用算法仓库年度合并授权。
- **不能无条件批量合并所有分支**：每个 PR 单独审核。Codex 不准自行审批或合并自己的工程 PR，科学决策与真实 Colab 仍归科学家。每次用户指令只推进有限工作，不代表 24/7 自动监控。

详见：[架构师](../protocols/ARCHITECT.md) · [任务管理](../workflows/TASK_MANAGEMENT.md) · [角色恢复](../workflows/ROLE_RECOVERY.md)。
