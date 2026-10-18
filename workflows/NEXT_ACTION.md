# Next-Action Protocol — Agent Handoff and One-Tap Continuation

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/NEXT_ACTION.md)

## Purpose

At the end of **each substantive SAE Mentor, Architect or Codex Engineer work cycle**, provide the Scientist with a short, actionable next step. This is a presentation and handoff contract, **not** an autonomous scheduler, new agent, extra task database, or permission to execute future work without a new instruction.

## Mandatory compact footer

Use this structure, adapted to the actual situation:

> **SAE · Next action**  
> **Current state:** <verified phase/status or UNKNOWN> · **Evidence:** <GitHub Issue/PR/report link, or NOT_VERIFIED>  
> **Recommended:** <exact copyable Chinese role command or human action> — <one short reason>  
> **Alternatives:** <zero to two exact copyable commands, only when meaningful>  
> **Needs Scientist:** <approval / Colab execution / choice / none>

- **Exactly one recommended action** when a feasible next action exists. If work is complete, blocked, or awaiting outside action, report **DONE / BLOCKED / WAITING_FOR_SCIENTIST** instead of manufacturing an action.
- **No more than three choices total**: one recommendation and at most two genuinely distinct alternatives. Prefer one choice if it is clear. Keep the footer mobile-readable, generally 4–6 short lines.
- Commands must be **copyable and specific**: `推进导师工作：<research question>`, `推进架构师工作：<review/dispatch target>`, `推进工程师工作：<Issue number / implementation target>`. Use `Scientist：<explicit action>` when the next step is human approval or real Colab execution. Do not imply GPT can directly run Codex or access a laptop unless connected tools actually permit it.
- Base the choice on the **actual project, latest verified GitHub state, priority, dependencies, phase gate and permissions**. Do not repeat a stale recommendation or loop between roles without progress. A recommendation is not evidence of a task having been started.
- For `RESEARCH_BLOCKED`, prefer Mentor + Scientist decision; for `RESEARCH_READY`, Architect handoff; for `CPU_IN_PROGRESS`, Codex; for `CPU_VALIDATED`, Architect GPU Readiness review; for `GPU_READY`, **Scientist** Colab execution; for `GPU_BLOCKED`, Codex/Architect local investigation before asking for another GPU run. A higher-priority correctness/security blocker overrides these defaults.
- Cite or link the **source Issue/PR, commit SHA or report** behind the status. If GitHub cannot be read, mark status **UNVERIFIED** and suggest a permission/retrieval step; do not invent links or claim the task was completed.
- A client that supports **real, functional quick actions** may render one-tap options carrying the exact same command; text commands are always the fallback for Codex, terminals, mobile clients or unavailable UI controls. Never promise a button in a client that cannot render one.
- Do not prompt for GPU experiments before `GPU_READY`; no silent auto-merge, credential disclosure, or background execution. Scientist retains approval and experimental authority.

## Example (illustrative only)

**SAE · Next action**  
**Current state:** CPU_VALIDATED *(example, not a real project claim)* · **Evidence:** example Issue #42  
**Recommended:** `推进架构师工作：审核 Issue #42 的 GPU Readiness` — verify the CPU evidence before Colab.  
**Alternative:** `推进工程师工作：复核 Issue #42 的 CPU 编译日志`  
**Needs Scientist:** None until Architect approves GPU_READY.

## Integration

The task-management workflow remains the canonical GitHub Issue/PR handoff; this protocol only standardizes **what the agent tells the Scientist after each cycle**. Root/project AGENTS and role protocols should point here. Never duplicate the entire protocol into every role file.

## Role recovery and integrity

On each role invocation, new chat or material context uncertainty, follow [Role Recovery](ROLE_RECOVERY.md): verify role, target repository, pinned SAE rules, current GitHub Issues/PRs, mathematical/CPU/GPU phase gates and actual tool permissions before taking one bounded action. Surface mismatches or inaccessible evidence; never fabricate local execution. Finish with the Next-Action handoff.
