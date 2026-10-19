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
> **Needs Scientist:** <compute budget approval / scientific decision / choice / none>

- **Exactly one recommended action** when a feasible next action exists. If work is complete, blocked, or awaiting outside action, report **DONE / BLOCKED / WAITING_FOR_SCIENTIST** instead of manufacturing an action.
- **No more than three choices total**: one recommendation and at most two genuinely distinct alternatives. Prefer one choice if it is clear. Keep the footer mobile-readable, generally 4–6 short lines.
- Commands must be **copyable and specific**: `推进导师工作：<research question>`, `推进架构师工作：<review/dispatch target>`, `推进工程师工作：<Issue number / implementation target>`. Use `Scientist：<explicit action>` when the next step is human scientific or compute-budget approval. Do not imply GPT can directly run Codex or access a laptop unless connected tools actually permit it.
- Base the choice on the **actual project, latest verified GitHub state, priority, dependencies, phase gate and permissions**. Do not repeat a stale recommendation or loop between roles without progress. A recommendation is not evidence of a task having been started.
- For `RESEARCH_BLOCKED`, prefer Mentor + Scientist decision; for `RESEARCH_READY`, Architect handoff; for `CPU_IN_PROGRESS`, Codex; for `CPU_VALIDATED`, Architect GPU Readiness review; for `GPU_READY`, **Codex** authorized Colab execution after Scientist compute approval; for `GPU_BLOCKED`, Codex/Architect local investigation before asking for another GPU run. A higher-priority correctness/security blocker overrides these defaults.
- Cite or link the **source Issue/PR, commit SHA or report** behind the status. If GitHub cannot be read, mark status **UNVERIFIED** and suggest a permission/retrieval step; do not invent links or claim the task was completed.
- A client that supports **real, functional quick actions** may render one-tap options carrying the exact same command; text commands are always the fallback for Codex, terminals, mobile clients or unavailable UI controls. Never promise a button in a client that cannot render one.
- Do not prompt for GPU experiments before `GPU_READY`; no silent auto-merge, credential disclosure, or background execution. Scientist retains scientific and compute-budget authority.

## Next-Action Completion Gate — pre-send check (V3.3)

Before sending the **final user-facing reply** of every substantive Mentor, Architect or Codex cycle—including long research, code changes, experimental runs, failures and blocked work—perform this compact self-check. A substantive cycle is **not communicatively complete** until the footer is present; keep the footer even when shortening the rest of a long response.

1. **Status and evidence:** state what was actually completed versus NOT RUN / UNVERIFIED / BLOCKED, with verifiable Issue, PR, report or commit links when available. Never fabricate activity, approvals or progress.
2. **One recommended handoff:** when a feasible next step exists, provide **one full, stand-alone, immediately copyable Chinese command** naming its target and action: `推进架构师工作：…`, `推进导师工作：…`, `推进工程师工作：…`, or `Scientist：…`. No placeholders, ambiguous fragments or commands to an agent that cannot actually be invoked.
3. **Meaningful choices:** offer zero to two distinct, feasible alternatives only when there is a real fork in the workflow. Rank one as the recommendation; do not pad choices or repeat the same work with different wording.
4. **Resource and authority gate:** preserve required scientific/compute approvals, actual tool access and role boundaries. A handoff is not an instruction to allocate hardware, merge, or launch Codex automatically.
5. **Last visible section:** end the reply with **SAE · Next action** (including current state, evidence, recommendation/alternatives and Scientist requirements). Explicitly write DONE / BLOCKED / WAITING_FOR_SCIENTIST if there is no honest executable next action; when a safe recovery or approval step exists, make that the copyable recommendation.

### Copy/paste and interactive-choice fallback

- **Always expose complete command text**, even when the client also shows a working Copy / Continue control. If the client supports *real* copy and one-tap actions, associate each action with **exactly the same command** as its visible text; never draw pretend buttons or assert an external agent was invoked.
- **If controls are unavailable (Codex CLI/desktop, terminal, Markdown-only clients), put each recommended/alternative command in its own fenced plain-text block**, so the Scientist can copy and paste it without editing. Do not combine multiple commands in a single block.
- If no executable action exists, display the terminal/blocked status and needed external condition without inventing an actionable command. This protocol is a **response-level self-check**, not a machine-enforced output validator; context loss or interrupted execution can still prevent compliance.

## Example (illustrative only)

**SAE · Next action**  
**Current state:** CPU_VALIDATED *(example, not a real project claim)* · **Evidence:** example Issue #42  
**Recommended:** `推进架构师工作：审核 Issue #42 的 GPU Readiness` — verify the CPU evidence before Colab.  
**Alternative:** `推进工程师工作：复核 Issue #42 的 CPU 编译日志`  
**Needs Scientist:** None until Architect approves GPU_READY.

## Integration

The task-management workflow remains the canonical GitHub Issue/PR handoff; this protocol only standardizes **what the agent tells the Scientist after each cycle**. Root/project AGENTS and role protocols should point here. Never duplicate the entire protocol into every role file.

## Role recovery and integrity

Before each substantive work cycle, apply [Role Recovery & Integrity](ROLE_RECOVERY.md): restore the explicitly assigned role, read pinned project rules and live GitHub evidence, verify phase and actual tool permissions, and stop on role mismatch rather than silently changing identity. Keep the existing Next-Action handoff at the end.
