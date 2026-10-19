# Next-Action Handoff — One Useful Command

> English (normative) | [简体中文](../i18n/zh-CN/workflows/NEXT_ACTION.md)

At the end of each **substantive Mentor, Architect or Codex work cycle**, present a compact, evidence-based handoff. This is a communication contract, **not** a scheduler or permission for the next step to run in the background.

## Footer

- **Project + verified state:** exact repo and Issue/PR/head SHA or report. If not accessible, state `UNVERIFIED`.
- **What happened:** action, real PASS/FAIL/NOT_RUN/BLOCKED checks and remaining blocker; do not mistake planned work for executed work.
- **One recommended next step:** exact copyable role command (e.g. `推进工程师工作：<Issue #>`) or a specific Scientist research/Colab action. At most **two genuine alternatives**, not a recursive list of roles.
- **Approval/permission dependency:** ask only for a Scientist-owned *substantive scientific/security/publication decision* not yet made. Do **not** request another per-PR merge permission if standing authorization already applies. No GPU request before `GPU_READY`.

## Compact example (illustrative, not evidence)

> **SAE · Next action**  
> **State:** CPU_IN_PROGRESS · linked Issue / tested SHA (if verified)  
> **Done:** actual evidence or NOT_RUN  
> **Recommended:** `推进工程师工作：修复 Issue #N 的 CPU oracle 测试`  
> **Blocker:** none / exact Scientist decision required

Always apply [Role Recovery](ROLE_RECOVERY.md) before acting; choose the next step based on actual GitHub task/phase state. Offer a client one-tap command only if the UI truly supports it. Mark DONE/BLOCKED/WAITING instead of inventing work when none is feasible.
