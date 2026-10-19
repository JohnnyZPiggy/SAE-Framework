# 永久性架构师合并授权 — Scientist → GPT Chief Architect

> [English（正式规范）](../../../governance/STANDING_AUTHORIZATION.md) | **简体中文**  
> 为兼容既有项目链接，保留历史文件名 `STANDING_AUTHORIZATION.md`。

## 科学家究竟授权了什么

**授权人：** 人类 Scientist；**被授权角色：** 由用户触发一个有边界工作周期、且当次具备真实 GitHub 工具权限的 GPT **Chief Architect**。

**生效：** 2026-10-19。**期限：永久有效（无到期日），直到科学家明确撤销或修改。** 科学家于 2026-10-19 纠正之前一年期设计：架构师在审查后，**独立作出合并或不合并的最终决定**。**不必为每个 PR 再请科学家批准合并操作**，即使 PR 涉及科研、治理或安全文件，合并的工程决定仍由架构师承担。

但这**不等于免除变更内容本身所需的科学家决定**。研究方向、数学研究关口、实际 Colab、重要安全/权限设置、许可证/IP 及项目已明确保留的实质决策仍属于 Scientist。若变更内容本身尚未批准或证据不足，架构师直接作出 **DO_NOT_MERGE / BLOCKED** 决定；不是询问“我能合并吗”。如果实质前置条件已满足，GPT 独立决定并合并，**不需要第二次人工点头**。

永久授权不是后台常驻任务：只有用户主动触发并实际连接 GitHub 的工作周期才执行。架构师正常的最后步骤是 **审查 → 自主决定 MERGE / DO_NOT_MERGE → 符合条件则合并并核验 → 汇报**。

## 精确仓库范围（一次登记不等于每次批准）

| 已登记仓库 | 权限 | 依据 |
| --- | --- | --- |
| `JohnnyZPiggy/SAE-Framework` | **PERMANENT_ARCHITECT_MERGE**（受审查关口约束） | 科学家 2026-10-19 明确指令 |

**其他仓库（包括算法仓库）尚未登记。** 科学家需要**一次性**明确指定准确 `owner/repo` 并授予该仓库常设合并权，再把它登记到当前列表。这是新增仓库范围的一次性科学家决定，**不是每次合并都请示**。复制 `.sae/` 固定快照、或者工具能访问某个仓库，都不自动赋予该仓库权限。新增仓库和扩大范围不能由 Agent 自己批准；范围决定获科学家认可后，架构师可以独立审核、决定是否合并对应的治理 PR。

科学家可随时通过新指令撤销或缩小权限，新指令优先于仓库旧文本。GPT/Codex 不得自行增加仓库、扩大权限。

## 三级审查，不是三级合并授权人

**T1/T2/T3 是审核证据与前置条件分级，最后是否合并统一由 GPT Architect 决定。** 以真实 Diff 的最高风险分类，不能只看 PR 标题。

| 级别 | 典型内容 | 架构师作出 MERGE 前需要检查 |
| --- | --- | --- |
| **T1 日常** | 普通文档、翻译、格式、不改变权限的协议说明、针对性测试 | 审查真实 Diff、链接、语法与相关检查 |
| **T2 工程** | 算法、数值修复、PyTorch 优化、打包、Benchmark/Publisher、一般依赖 | 适用时已通过数学研究关口、Codex 真实 CPU/oracle/边界/回归/打包证据、许可和安全审核。只有在声称 GPU 成功或 GPU 为明确验收项时要求 Scientist Colab 证据；CPU-only PR 若 GPU 非验收条件可合并，但必须注明 `GPU_NOT_RUN`。 |
| **T3 科学家保留的实质决策** | 科学问题/数学假设、接纳未证明结论、安全设置/Secrets/权限、治理授权范围、重大许可/IP/发版、破坏性修改、敏感数据对外公布 | **变更内容本身**如需科学家决定，必须先有明确可核实的批准；然后由 **GPT Architect 自主决定是否合并 PR，不额外请示合并许可**。若实质决策缺失，则决定 `DO_NOT_MERGE / WAITING_FOR_SCIENTIST_DECISION`，不能猜测批准。 |

**例如：** 科学家已批准数学公式；Codex 实现并运行 CPU 测试；GPT 审查 PR 并自行决定是否合并，**不再问“可以合并吗”**。如果数学假设尚未由科学家确认，GPT 应拒绝/搁置并请求**科学判断**，而不是请求一次合并授权。

修改本永久授权属于 T3。GPT 不得自行把授权扩大成不可撤销、无限仓库或绕过科研关口。科学家**本次 2026-10-19 指令已明确批准**将期限从一年改成永久、把合并最终决定交给架构师，因此这次治理 PR 可以在架构师审核后自主合并。未来权限范围或规则的实质修改仍要科学家批准**改动内容**，但合并动作不用再授权一次。

## 每个 PR 的 Merge Gate

1. **恢复角色与范围：** 核对本轮用户主动触发 Architect、仓库已准确登记、当前 AGENTS 和固定项目协议、真实 GitHub 权限、科学家是否有更新的撤销指令。未登记算法仓库不能自动纳入。
2. **查看真实 PR：** 完整 Diff/文件表、Issue、验收条件、base/head SHA、阻塞评论、可合并状态、分支保护、Secrets 或外部公布风险。
3. **按 T1/T2/T3 检查前置条件与证据：** `NOT_RUN` 不是 `PASS`，PR 自述不算执行证据；GPT 自己写的实质代码需 Codex/Scientist 独立运行证据。
4. **架构师最终决定：** `MERGE_APPROVED`、`DO_NOT_MERGE`、`MERGE_BLOCKED`、`WAITING_FOR_SCIENTIST_DECISION`。**不得再要求科学家逐 PR 授予合并权**；只在真正缺少科学家负责的科研/安全等实质决定时请求相关决定。
5. **合并前审计：** PR 留精简评论/审查，写明级别、被审 SHA、证据、科学家前置决策、风险及最终决定。工具失败则如实说明，不伪造留痕。
6. **符合条件则合并并核实：** 默认 Squash Merge，使用精确的已审 head SHA，遵守 GitHub 分支保护，不能绕过规则、直接推 main、强推或合并过期代码。合并回执和 merge SHA 核实后才写 `MERGED`。
7. **完成汇报与交接：** 给出 PR/merge SHA 或不合并的具体理由，以及下一条口令。不后台无限循环处理其他 PR。

**最小 PR 审计格式：**

```text
SAE ARCHITECT MERGE GATE
Repo/PR: <owner/repo>#<N>; reviewed base/head: <base-SHA>/<head-SHA>
Tier: T1 / T2 / T3; standing authority: PERMANENT (until Scientist revokes)
Evidence / Scientist-owned prerequisites: <真实链接、状态或 NOT RUN>
Architect final decision: MERGE_APPROVED / DO_NOT_MERGE / MERGE_BLOCKED / WAITING_FOR_SCIENTIST_DECISION
Reason / risks: <简述>; confirmed merge SHA: <SHA 或 NOT MERGED>
```

## 边界、撤销与新仓库

- **GPT 是最终合并决策者，不是最终科学决策者。** 不能自认科研批准、泄露 Secrets、未经必要授权修改 GitHub 安全权限，或否定 Scientist 新指令。
- **不再年度续期、不再到期：** 权限持续生效，直到科学家明确撤销或被新指令取代；撤销立即生效，应尽快同步仓库文件。
- **不无限扩展仓库：** 只限准确登记仓库；算法仓库由 Scientist 一次授权加入后，GPT 即可自主决定后续 PR 合并，不必次次问。
- **不能自行扩大授权：** 仓库范围/权限变化须科学家批准具体内容，之后 GPT 仍拥有合并时的最终技术决定。
- **不启用后台自动执行或强制 CI：** GitHub Issue/PR 是审计轨迹；Codex 提交并测试但**不能自行合并**。Scientist 负责 Colab 和公开实验资料上传。
- SAE 主仓库以上述**最新在线文件**为合并裁量权依据。算法项目应遵守固定快照的日常规则，但合并时仍须核实此处的现行登记表与 Scientist 授权。

相关：[架构师协议](../protocols/ARCHITECT.md) · [任务管理](../workflows/TASK_MANAGEMENT.md) · [角色恢复](../workflows/ROLE_RECOVERY.md)。
