# Agent Warm Start — Capability Verification (SAE V3.3)

> **Compute policy:** [Compute Throughput Policy](../governance/COMPUTE_THROUGHPUT_POLICY.md) governs GPU-first, high-throughput experiments for all roles. Use all scientifically useful Colab GPU types available under existing authorization; do not impose compute-saving quotas or speculative GPU gates. Provider limits, billing authorization, numerical evidence and session cleanup remain mandatory.


> Normative English | [简体中文](../i18n/zh-CN/workflows/AGENT_WARM_START.md)

Warm Start is an **optional, user-invoked bounded capability test after Cold Start**. It is not a new agent, authorization gate, recurring certification, or requirement before routine work. Reuse verified project/role/pin/context; test the actual role in the current environment rather than rereading every protocol.

## Modes
- **Standard (default):** One realistic, bounded role-specific check. No GPU allocation unless separately scoped.
- **Full (explicit):** Standard plus end-to-end evidence/agent handoff and, when the current Engineer has an authenticated supported GPU path and included entitlement, **one real bounded GPU probe**. No manual Scientist GPU approval step; retain actual provider/account/cleanup controls.

## Architect
Review one relevant real issue/PR at its exact head/base, diff, available math/test evidence and architectural risks. Deliver a concise accept/revise decision and executable Engineer task. For Full, verify evidence/merge criteria against Standing Authorization, **simulate** the merge decision, but do not merge merely as a capability demonstration. Read actual permissions when that operation is needed.

## Scientific Mentor
Choose one representative active algorithm identity: derive a meaningful identity/structure, state assumptions, dimensional shapes, error/stability bounds or failure cases; cross-check with a reliable mathematical source or a minimal independent numerical example. Design a small oracle with tolerances. Mark PROVED / OBSERVED / HYPOTHESIS accurately. Full includes an evidence-based Engineer experiment specification; no mandatory new study document.

## Software Engineer
Use the Scientist-designated workspace (including Dropbox-synced D:) as authoritative for scratch, tests, caches and artifacts. Identify the actual current filesystem, repository, Git/gh permissions, existing Python/PyTorch and task dependencies. Run one small CPU numerical test and prove output placement/cleanup in an isolated owned task directory. Keep scratch out of unintended Git tracking. Never delete user/other-task files. No automatic reinstallation, disk sweep or C:-hosted default scratch.

**Full GPU probe:** Prefer a supported GPU through the existing pinned SAE controller/Colab CLI. Immediately before allocation verify real authenticated usage, balance/session state, source pin, bounded runtime and existing entitlement. One active session; execute a small self-contained PyTorch numerical probe with CPU/reference comparison and actual device identification. Download and verify byte count, identity and SHA-256; stop and confirm remote session release even on errors. Use the chosen workspace for local evidence, clean owned disposable files. Mark PROBE_ONLY; it is not an algorithm benchmark or general GPU support certification. No new charges, account-permission changes, new credentials, or unmanaged GPU sessions. If a supported authenticated GPU path is unavailable, report the specific limitation and retain independent CPU readiness; **GPU-first never means GPU-blocked**.

## Shared handoff and result
Run each capability check once, reuse unchanged runtime evidence across roles; Architect/Mentor can inspect the **same** Engineer CPU/GPU evidence instead of duplicating compute. Recheck only materially changed source/runtime/permissions; live provider/session state refresh occurs at allocation. Write a single compact result in the current conversation or active Issue/PR when handoff needs persistence: role, actual environment, target/source SHA, checks with PASS/FAIL/NOT RUN/BLOCKED, evidence pointer, owned scratch residue and GPU cleanup, one next action. Do not create report files, Issues, PRs or extra checks solely for Warm Start.

## Invocation
- **Architect/Mentor:** “推进 SAE Full Warm Start，角色 Chief Architect + Scientific Mentor，目标 <repo>；从已完成 Cold Start 复用上下文，实审一项变更、推导一个真实数学结构、形成 Engineer CPU/GPU 验证任务；不为了热身合并。”
- **Engineer:** “推进 SAE Full Warm Start，角色 Software Engineer，目标当前 Git 项目；在用户指定 D 盘 Dropbox 工作区运行小型 CPU 测试，并在已有权益与真实技术条件允许时使用固定 SAE Colab CLI 执行一次有界 GPU 探针、哈希校验和零会话清理。报告实际证据与剩余阻断。”

Current project-pinned contracts and [Compute Experiment](GPU_EXPERIMENT.md), [Engineer Compute Discovery](ENGINEER_COMPUTE_DISCOVERY.md), [Standing Authorization](../governance/STANDING_AUTHORIZATION.md), and explicit Scientist instructions retain priority for their actual scope.
