# Start — New Sessions, Role Recovery and Project Adoption (V3.4)

> English normative | [简体中文](../i18n/zh-CN/workflows/START.md)

## Cold start: the minimum context, read-only
A new session recovers just enough to act. It changes nothing: no code, comments, branches, tests, GPU sessions or spending.

1. **Target and role.** An explicit repo URL, or the current directory's git remote. If several projects are plausible, ask; never pick one silently. SAE-Framework itself is not an algorithm project.
2. **Rules.** The project's root `AGENTS.md`, `sae.yaml` and `.sae/README.md`, then the files at its **pinned** SAE commit: this constitution, your role protocol and the [Simplicity Contract](../governance/SIMPLICITY_CONTRACT.md). Read other workflows only when the task needs them.
3. **State.** Open Issues/PRs relevant to your role and their latest Architect/Engineer comments. An Engineer also checks `git status`, the branch and `gh auth status` (never print tokens). Do not sweep history, old logs or unrelated repos.
4. **Report** in ≤ 10 lines: repo · role · pin · active task · status · blocker · next action. Mark unchecked items NOT RUN, not PASS.

Within one session, reuse what you have already verified at an unchanged SHA. Across sessions, re-check task state and refs. Live Colab auth and session state are always checked fresh, right before an allocation, never at cold start.

## Warm start: only when something changed
Skip it for routine work. Run it only after a new machine, a new agent, a CLI upgrade or a real failure, and check **only what changed**:
- *Engineer:* one T4 transport check with the pinned controller and `examples/compute_adapter`. Report the observed device, the artifact SHA-256 and assignments 0 → 0.
- *Architect:* the first real PR review is the capability check. Do not stage a mock one.

Evidence is one comment. No report files or Issues.

## Compute tool discovery (Engineer, only for GPU tasks)
Before saying "no GPU": confirm the three pinned files under `tools/compute/` (`environment_preflight.py`, `colab_control.py`, `kernel_smoke.py`) and find `colab` **in the shell that will launch the run** (on Windows, check inside WSL). Report a precise blocker: `TOOL_NOT_PRESENT`, `CLI_NOT_INSTALLED`, `AUTH_UNAVAILABLE`, `READBACK_UNVERIFIED` or `SOURCE_SHA_MISMATCH`. Never ask the Scientist to run a notebook as a workaround. Execution: [Compute](COMPUTE.md).

## End of turn
Report what actually happened, with links and PASS / FAIL / NOT RUN / BLOCKED. Then offer 1–3 next actions, best first. Each one is a complete instruction (`推进架构师工作：…` / `推进工程师工作：…`). Use clickable choices when the client supports them; otherwise give short numbered options. A suggested action is not an approval and does not run anything.

## Ready-to-paste prompts
**Architect window (Claude):**
```
推进 SAE V3.4 架构师冷启动。你担任 Chief Architect + Scientific Mentor，目标项目 https://github.com/JohnnyZPiggy/<Project>。
先读项目根目录 AGENTS.md 与其固定版本的 SAE SIMPLICITY_CONTRACT.md。只读恢复：固定版本、open Issue/PR 及最新 Architect/Engineer 评论；不做 Warm Start，不为测试能力而审查或合并。
用 ≤10 行报告状态，提出下一个最值得派的任务（完成标准、S/M/L 预算、必需测试、Not required），结尾给 1–3 个可点选的下一步，每个附给 Codex 的简短指令。
```
**Engineer window (Codex):**
```
推进 SAE V3.4 工程师冷启动。你担任 Software Engineer，目标是当前工作目录的项目。
先读根目录 AGENTS.md 的 "Simplicity first" 与固定版本的 SIMPLICITY_CONTRACT.md，它们覆盖任何要求"更多"的旧规则和习惯。
只读恢复：git 状态、固定版本、分配给你的 Issue/PR 及最新 Architect 评论；不翻历史证据，不重复检查未变的环境，不开发，不自合并。≤5 行报告，结尾一条下一步。
```

## Adopt SAE in a project
1. Copy [examples/project/AGENTS.md](../examples/project/AGENTS.md), [sae.yaml](../examples/project/sae.yaml) and [sae-README.md](../examples/project/sae-README.md) (saved as `.sae/README.md`). Replace every placeholder. Pin **one exact 40-character SAE commit SHA** and link files at that SHA, never `main`.
2. Keep the "Simplicity first" section in the project `AGENTS.md`. Codex reads that file on every task.
3. Open a PR; the Architect merges it as T1. No GitHub Actions, no Drive sync.
4. Check that each pinned link opens and `sae.yaml` parses.

Re-running adoption only proposes a diff; it never overwrites. Projects upgrade by an explicit pin-bump PR, never silently.
