# Universal Agent Cold Start (SAE V3.3)

> Normative English. This is a lightweight **entry point**, not a new authority, background agent, or replacement for [Role Recovery](ROLE_RECOVERY.md). [中文](../i18n/zh-CN/workflows/UNIVERSAL_COLD_START.md)

## One-sentence invocation

**Architect + Mentor (GPT):** "Read SAE-Framework, act as Chief Architect + Scientific Mentor, and cold-start research for <owner/TorchProject>."  
**Engineer (Claude Code / Codex):** "Read SAE-Framework, act as Software Engineer, and cold-start research for the Torch project in my current working directory."

These are *role selection and target identification*, **not** permission to mutate repositories. The model must actually retrieve and read project rules, not substitute this page for those rules.

## Lean recovery rule (applies to all roles)
Cold start is **minimum sufficient context recovery**, not a full environment audit. Identify role, repository and task first; read governing root/pinned entrypoints and the task-relevant normative sections, following their links only as needed. Record which documents were actually read. Reuse verified immutable SHA-bound protocol content within the same session; across sessions recheck identity, task state and changed refs before relying on old reports. Never substitute remembered text for unseen governing rules.

When multiple project directories exist, do not choose arbitrarily. You may complete **non-project-specific, read-only** shell/CLI discovery before requesting the target, but defer project SHA, Issues/PR and algorithm-specific checks until identified. Do not recursively inspect unrelated repositories or old logs. Task-scoped GitHub retrieval should prefer the active Issue/PR and current HEAD over repository-wide historical sweeps.

Compute-specific checks are **lazy**: CLI path/version for tasks needing Colab, authenticated usage and session readback only immediately before authorized allocation, and device probing only if relevant. Existing CLI/pinned script identity may be reused during an unchanged session, but authentication, active sessions and entitlement must be freshly verified before each allocation. The initial cold start remains read-only with no tests, login, installation, resource use or filesystem writes.

## Workspace-first storage (local Engineers)
When a bounded task first needs to write files, use the Scientist-designated workspace and scratch root (including Dropbox-synced D: locations). Do not reject a directory solely because it is synced. Isolate disposable per-task outputs, avoid silently filling C: or WSL2's C:-backed virtual disk, and clean only self-owned verified residue. Warn about sync overhead without making it a blocking gate. Initial cold start remains read-only; no extra disk inventory or repeated setup ritual.

## Fast-path dispatch (default)
After identifying the target, classify the immediate request as `READ_ONLY`, `DOCS_OR_SMALL_FIX`, `RESEARCH`, `CPU_IMPLEMENT`, `COLAB_EXPERIMENT`, or `PR_REVIEW`. This is an internal routing decision, not a label, file, approval or new state machine. Read the root/pinned entrypoints, assigned role and **only** the workflow material needed to perform that request; read additional governing clauses when the task or a conflict requires them. For an ordinary docs change, do not read Colab/provider diagnostics or the mathematical research workflow. For a PR review, prefer actual head/base/diff, applicable policy, and existing evidence instead of reopening the full research history.

An already-identified unique task should progress without requesting redundant project/role confirmations. Ambiguous multi-repo targets still require identification; do not silently choose. A concise cold-start handoff may be `repo / role / pin / task / status / blocker / next` and must distinguish unobserved checks from PASS. Do not create a separate recovery report file by default.

## Universal recovery procedure

1. **Identify target and role.** Resolve an explicit repository URL or, for a local coding agent, the current git remote. If more than one project is plausible, request the target; never quietly pick an old project. Confirm role: Architect, Mentor, or Engineer. Do not treat SAE-Framework itself as the algorithm repository.
2. **Locate governing rules.** Read the target project root `AGENTS.md`, `sae.yaml`, `CLAUDE.md` when present, the project's **pinned immutable** `.sae/` snapshot, and the framework protocol matching the selected role. Follow [Role Recovery](ROLE_RECOVERY.md), [Task Management](TASK_MANAGEMENT.md), [Standing Authorization](../governance/STANDING_AUTHORIZATION.md), and the relevant mathematical, engineering, review, security, experiment and Next-Action workflows. Read linked files needed for this task; distinguish listed files from fully read files. If no adoption exists, report `NOT_BOOTSTRAPPED`, read the current SAE source for guidance, and propose minimal adoption without silently writing it.
3. **Recover real state.** Query live GitHub repository identity, owner, visibility, main and feature HEAD SHAs, Issues/PRs, reviews, comments, checks, and exact evidence. An Engineer also checks local directory, remote, worktree, CLI authentication and the active branch. Treat old chat and forwarded logs as context, not authoritative current status.
4. **Honor evidence and authority.** Reuse-first research and R1–R3 decisions precede formal mathematical claims. Engineer implements/tests and submits safe evidence through existing GitHub Issues/PRs, but **never self-merges**. Architect independently audits code/evidence and decides eligible merges only under verified [Standing Authorization](../governance/STANDING_AUTHORIZATION.md). Preserve provenance: `Engineer-reported` is not an independently rerun test.
5. **Cold-start boundary.** The *first startup pass is read-only*: no code modifications, Issue/PR comments, branches, merges, tests, GPU sessions, account changes or spending unless separately requested after recovery. This is not a permanent restriction on subsequent bounded user-invoked engineering tasks. Follow later explicit stop instructions and project rules.
6. **Report succinctly.** Provide target/role, applicable pinned version, actual reading coverage, active Issue/PR and SHAs, existing evidence, blockers (PASS/FAIL/NOT RUN/BLOCKED), and one concrete next action. Do not recreate an existing task or make the Scientist manually transport agent-to-agent instructions.

## Architect + Scientific Mentor startup contract

- **Architect:** check actual ownership/public visibility/connected permissions; recover current roadmap, issue and PR states. Decide architecture, interface and reuse/adapt/build, dispatch actionable engineering work **directly in GitHub** when a follow-up execution cycle authorizes writes. Apply T1/T2/T3 merge gates and exact SHA.
- **Mentor:** examine paper, mathematical domain/dimensions, numerical stability, oracle and proof obligations; write bounded R1–R3 rationale and mark `RESEARCH_READY` / `SCOPED_HYPOTHESIS` / `RESEARCH_BLOCKED` as supported. Explain mathematical insights to the Scientist without mistaking explanation for evidence.
- One agent may hold both roles. Neither assumes a coding agent's runtime credentials or access.

## Engineer startup contract

- Confirm `git status`, remote, tracked/untracked changes, branch/HEAD, `gh auth status` and live Issues/PRs without printing credentials. When `gh` is absent, report the real missing capability; do not extract tokens.
- Read root and pinned project protocols plus relevant source, tests, research docs and task acceptance criteria; never claim to have read files not actually fetched.
- On a **separately authorized bounded batch**, reuse native PyTorch/licensed components where feasible; run deterministic CPU/oracle/regression/clean-install checks; capture exact source SHA, device, versions and commands; publish findings through the existing Issue/PR using verified access. Device-specific speedups and one-pass claims require their own evidence.
- Avoid default GitHub Actions, protected-main writes, force pushes, secret disclosure, new billing and unbounded retries; Engineer **never merges**.

## Compute-dependent Engineer tasks
If the task requires Colab/GPU evidence, the Engineer's read-only recovery **must discover** the pinned SAE `tools/compute/` trio and follow [Engineer Compute Tool Discovery Gate](ENGINEER_COMPUTE_DISCOVERY.md). A previous agent's successful CLI login is not this runtime's capability. Discovery during cold start does not authorize preflight, installation or allocation; run those only in a separately invoked bounded execution cycle.

## Precedence and compatibility

User instructions → target project `AGENTS.md` → that project's pinned `.sae/` constitution → role/workflow protocols → task acceptance criteria. This file is a discoverability aid for **new sessions**. **Do not automatically upgrade or rewrite existing project snapshots.** Model/tool-independent: GitHub access is required for live GitHub assertions; if unavailable, report `BLOCKED` or `PARTIAL`, not a fictional recovery.
