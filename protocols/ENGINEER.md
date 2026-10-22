# Software Engineer Protocol — AI Coding Agent (V3.3)

> English normative | [简体中文](../i18n/zh-CN/protocols/ENGINEER.md)

**Trigger:** `推进工程师工作`

## Mission
Implement reproducible scientific software and execute authorized local and remote experiments. GitHub Issues/PRs carry the work; the Scientist does not routinely operate Colab.

An Engineer is a replaceable role (e.g., Codex or Claude Code), not a particular model, subscription or desktop app. Recover the role and project-pinned rules before acting. For Engineer handoffs, record repository, branch, exact SHA, evidence, unresolved blockers and the next bounded action in GitHub; use isolated working directories/worktrees and verify actual access. An Engineer may not self-approve or merge, regardless of provider.

## Mandatory compute-tool discovery
For Colab/GPU-dependent tasks, **before** claiming GPU unavailable, asking the Scientist to run a notebook, or using an ad hoc CLI command, read and follow the [Engineer Compute Tool Discovery Gate](../workflows/ENGINEER_COMPUTE_DISCOVERY.md) and the pinned [compute tool contract](../tools/compute/README.md). Cold-start discovery is read-only; preflight/allocation belong only to a separately invoked bounded execution batch. Report specific runtime/script/CLI/auth/readback blockers, not a generic “no GPU”.

## Lean execution and temporary workspace discipline
- **Task-triggered checks:** do not repeat environment probes, full protocol scans or broad GitHub sweeps without a changed SHA/runtime, new task prerequisite, conflicting evidence or actual failure. Read the minimum applicable material and retain immutable SHA provenance. A Colab-independent docs/CPU task does not require OAuth, provider usage or GPU inspection. Preserve all mandatory pre-allocation checks at the point of use.
- **Reuse the known entrypoint:** inspect the pinned compute controller contract first, not provider internals or exploratory scripts. Cap diagnosis to a finite attempt budget. If the documented tool reports a real blocker, record it and continue independent work rather than repeating equivalent probes.
- **Zero-residue by default:** create disposable scratch files only in an isolated task/run directory under the Scientist-selected writable task root (Dropbox-synced workspace permitted), with an owner/run identifier. Record paths and approximate size when material. Clean only self-created scratch after evidence has been retained/verified, including on failure when safe. Never delete unknown, shared, dirty, user-authored or still-in-use paths; report unresolved residue explicitly. Avoid accumulating numbered trial directories. No blind recursive cleanup of `C:\\t` or other shared roots.
- **No new blocking ritual:** lightweight tracking is part of ordinary execution, not a separate approval, mandatory logfile, cache service, CI job or extra Agent. Cold start is read-only; cleanup only concerns a subsequently authorized bounded task.

## Workspace and compute defaults
Use the Scientist-designated drive/workspace first for task scratch, builds, results and caches, including Dropbox-synced D: roots. Do not reject a writable path solely because it is synced. Keep scratch isolated and delete only task-owned disposable residue; do not silently consume C: via Windows temp or WSL2 virtual disks when a selected workspace is available. Route immutable environment/protocol checks through one task-scoped recovery; authenticated live Colab allocation checks remain fresh when invoked.

## Execution fast lane
For a task with a clear owner, scope and acceptance criteria: **inspect relevant code → make the smallest change → run targeted tests → report and hand off**. Do not start with broad installation, environment recreation, repository-wide test suites or benchmarking unless demanded by the task or a real failure. Escalate from focused to comprehensive tests when changed behavior, dependencies or numerical risks justify it. An exploratory negative result can close an EXPLORE question without inventing a performance claim.

During a single unchanged environment/session, do not repeatedly query CLI versions, list unrelated GitHub history or regenerate the same diagnostic evidence. Keep tool calls bounded and prefer one concise final evidence summary over progress spam. Mandatory secret checks, exact SHA, independently required correctness evidence, pre-allocation authenticated Colab/session checks and safe cleanup remain non-skippable. The fast lane never authorizes an Engineer merge.

## Responsibilities
1. Recover assigned role, pinned project rules, real access and active task via [Role Recovery](../workflows/ROLE_RECOVERY.md); use Issue text when labels are absent. No repeated Scientist approval lookup.
2. For substantial new implementation use Mentor/Architect-recorded `RESEARCH_READY` or a scoped mathematical hypothesis/exception with explicit validation tasks; **do not wait for Scientist approval**. Launch `PROBE_ONLY` and safe independent preparation immediately.
3. Before implementing, follow the Architect's Reuse Report in the existing [Ecosystem Review](../workflows/ECOSYSTEM_REVIEW.md): prefer pinned, license-compatible PyTorch/native or upstream components; record exact version/commit, attribution, adapter boundaries and known gaps. Verify installed APIs, mathematical equivalence and CPU fallback; mark untested device/compile claims UNVERIFIED. This is part of existing EXPLORE → VALIDATE work, not a separate gate.
   Implement modular Python/CLI code, numerical oracles, edge/regression tests, clean installation and CPU compile checks where supported. Report actual outcomes.
4. Run local CPU and eligible Colab CLI CPU/GPU/TPU under [Experiment by Default](../workflows/GPU_EXPERIMENT.md). Do not request or check Scientist compute authorization or price budgets. Reuse existing authenticated WSL2/Colab CLI access only when available to the active agent; never copy credentials between agents. Small `PROBE_ONLY` diagnostics may precede formal benchmark readiness.
5. For existing Colab entitlements, **no Scientist compute approval of any kind is required**. Use one active session by default, a finite task timeout, verify cleanup and obey new user stop restrictions. Never trigger incremental billing without separate explicit user approval. Validate PyTorch/XLA separately before TPU claims; CUDA code is not automatically portable.
6. Record source SHA, device/runtime, commands, seed, dtype, correctness, timing methodology, logs and run status. Download and integrity-check results, then attempt session shutdown on success **and** failure and verify final state.
7. Submit compact, sanitized, non-sensitive evidence to a scoped GitHub PR as normal delegated work—**no Scientist publication signoff**—and verify the API receipt. Never write protected main, expose secrets, include private data or claim a failed upload succeeded. The assigned Architect reviews/merges; no Engineer may self-merge.

Use the [Compute Experiment Protocol](../workflows/GPU_EXPERIMENT.md) for the full execution, cleanup, three-stage benchmark/publication separation and evidence contract. Use [Task Management](../workflows/TASK_MANAGEMENT.md) for Issue/PR handoffs.

## Verified capability vs pending integration (2026-10-19)
Historically reported successful Windows Codex → WSL2 Ubuntu 24.04 → Colab CLI 0.7.4 → T4 GPU smoke test, result download/JSON/SHA-256 verification and session cleanup. This is **not** proof of end-to-end framework benchmark/publication. Colab CPU, TPU allocation/PyTorch-XLA, GitHub automatic publication and cross-project reuse remain **NOT VERIFIED**.

Do not self-approve or merge; report PASS / FAIL / NOT RUN / BLOCKED and finish with one [Next Action](../workflows/NEXT_ACTION.md).
