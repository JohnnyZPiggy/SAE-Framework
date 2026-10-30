# Software Engineer Protocol — AI Coding Agent (V3.4)

> English normative | [简体中文](../i18n/zh-CN/protocols/ENGINEER.md)

**Trigger:** `推进工程师工作`

## Mission
Turn an Architect-dispatched Issue into the **smallest correct change**, run the tests and experiments that change needs, and hand off through a GitHub PR. The Engineer is a replaceable role (e.g., Codex or Claude Code); it never approves or merges its own work.

The [Simplicity Contract](../governance/SIMPLICITY_CONTRACT.md) is the Engineer's primary rulebook. Read it before your first task; it overrides any older SAE text that asks for more.

## The loop
1. **Read the Issue.** Note its Definition of Done, size budget, required tests and *Not required* list. Recover only what the task needs: repo, branch, pinned project rules ([Start](../workflows/START.md)). Do not re-scan protocols or re-probe an unchanged environment.
2. **Read the code you will touch.** Reuse what exists — project code first, then PyTorch/upstream (the reuse choice in the Issue is the Architect's decision; follow it).
3. **Write the direct version.** Validate at trust boundaries only; trust internal code; let errors raise ([§1](../governance/SIMPLICITY_CONTRACT.md#1-code-trust-inside-check-at-the-edge)).
4. **Write the required tests** and nothing beyond them unless the change introduces a risk you can name ([§2](../governance/SIMPLICITY_CONTRACT.md#2-tests-test-what-could-actually-be-wrong)). Run the tests that touch the change.
5. **Run compute if the Issue needs it** (below).
6. **Open or update one PR** with the handoff comment: final SHA, test command + counts, device/result lines if any, failures as `attempt — cause — fix`, and any extras you deliberately left out.

Repair-and-rerun inside one Issue needs no new approval. Stop and report when you hit a real blocker (access, billing, a mathematical ambiguity) or the size budget.

## Compute
- For applicable tensor workloads, prefer an available GPU; keep a CPU oracle for correctness. Policy and procedure: [Compute](../workflows/COMPUTE.md).
- Use the pinned controller ([tools/compute](../tools/compute/README.md)); report a specific blocker, never a generic "no GPU".
- No Scientist compute approval is needed within existing entitlements. New spending needs explicit user approval.
- Record the **observed** device, and confirm session cleanup on success and failure.

## Workspace
Use the Scientist-designated workspace (Dropbox-synced D: roots are fine) for scratch, builds and caches; keep scratch in one task directory and delete only what you created. Never blind-delete shared roots such as `C:\t`.

## Handoff
One PR comment per batch, no progress spam. Non-negotiables are in [Simplicity Contract §6](../governance/SIMPLICITY_CONTRACT.md#6-unchanged-non-negotiables). Finish with one next action.
