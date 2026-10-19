## Integrated project acceptance

The pinned SAE snapshot must include [research pipeline](workflows/RESEARCH_PIPELINE.md), [GPU readiness](templates/GPU_READINESS.md), [three-artifact handoff](workflows/THREE_ARTIFACT_HANDOFF.md), [engineering template](templates/ENGINEERING_REPORT.md) and [two-command Colab contract](workflows/COLAB_TWO_COMMAND.md), including bilingual mirrors and working relative links. Project-specific templates copied outside the snapshot must have relative links rewritten. Codex must prove clean CPU install, correctness and CPU compile before GPU_READY. Scientist's target Notebook runs pinned-SHA pip install and one packaged benchmark CLI; optional publication remains manual until the Publisher passes real Colab integration. Preserve the self-contained snapshot requirements of PR #7.

# SAE Bootstrap — AI-Executable Initialization Protocol (V3.2)

> Language: **English** | [简体中文](i18n/zh-CN/SAE_BOOTSTRAP.md)


**Command:** `按照 SAE Framework V3.2 初始化这个项目`

## Inputs (collect or infer only from inspected environment)
- **Target repository:** exact `owner/repo` and current default branch.
- **Scientific target:** algorithm/paper and intended PyTorch deliverable (may be TBD).
- **Framework source:** `JohnnyZPiggy/SAE-Framework`, **pinned to a release tag or commit SHA**, not a floating `main`.
- **Access:** explicit read/write for target repo; Colab experiment credentials remain under Scientist control.
- **Existing content:** preserve everything unless user approves a specific change.

## Phase 0 — Preflight (mandatory)
1. Inspect repository, current README/AGENTS, default branch, open Issues and PRs, current packaging/tests, and effective access.
2. Read framework `AGENTS.md`, each applicable protocol and workflow, and this file from a fixed revision. A mention or URL alone **does not mean the files were read**.
3. State absent prerequisites, proposed files and side effects. Refuse to claim GitHub actions are available until tools/permissions are confirmed.

## Phase 1 — Install a pinned policy snapshot
1. Write project-root `AGENTS.md` (use `examples/project/AGENTS.md` as a starting point).
2. Write project-root `sae.yaml` (use `examples/project/sae.yaml`) with target, roles, no-Actions policy and a **real SHA**.
3. Copy a self-contained **documentation snapshot** from **one immutable framework revision** into `.sae/`: `AGENTS.md`, `SAE_BOOTSTRAP.md`, `README.md`, `README.zh-CN.md`, `CHANGELOG.md`, `protocols/`, `workflows/`, `templates/`, `docs/` (including figures), `examples/` and `i18n/zh-CN/`, including `governance/` and its Chinese mirror. Keep relative links working; do **not** install `.github/workflows/` or treat the snapshot as a runtime. Avoid copying an unversioned mix of folders. Do not simply leave external links.
4. Ensure agent sessions actually open the root `AGENTS.md` and their assigned `.sae/protocols/*.md`. Codex discovers in-repo AGENTS rules; GPT must be explicitly directed to read them through its available GitHub tools.
5. Preserve all pre-existing content. Stage additions/changes on a **new branch and PR**.

## Phase 1.5 — Mentor-led mathematical research before algorithm engineering (mandatory gate)

For a **new scientific algorithm or major tensorization rewrite**, after repository/protocol scaffolding and before issuing substantive implementation or benchmark tasks:
1. Scientist supplies or confirms the reference algorithm, mathematics and research goal.
2. GPT switches to **Scientific Mentor** and follows [workflows/MATHEMATICAL_RESEARCH.md](workflows/MATHEMATICAL_RESEARCH.md): inspect matrix–vector/matrix-free and other tensor-friendly operators; derive and critique mathematically equivalent batched/tensor formulations.
3. Write a reviewable project `docs/research/<algorithm>-tensorization.md` following [templates/TENSORIZATION_STUDY.md](templates/TENSORIZATION_STUDY.md), including evidence gaps, oracle and hardware hypotheses.
4. Scientist reviews and chooses `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`, or explicitly authorizes a narrow exception.
5. Architect may then design the engineering Issue, reference oracle and experiment plan. **Do not dispatch algorithm rewrites or formal GPU benchmarks before the gate.** Basic infrastructure setup can proceed independently; feedback may reopen this phase.

## Phase 2 — Project engineering skeleton (delegate to Codex)
Expected folders as appropriate: `src/`, `tests/`, `benchmarks/`, `tools/`, `notebooks/`, `reports/`, `docs/`. Directories only exist in Git after at least one tracked file.
- Python packaging and import layout tailored to the algorithm.
- Tested CPU numerical correctness and regression tests.
- A device-selectable CLI for experiments (`--device cpu|cuda`), deterministic seeds and structured outputs.
- A **thin** Colab notebook composed of environment setup, pinned repo/commit install, CLI run and report publish steps. Architect owns notebook orchestration; Codex owns Python implementations.
- Publisher contract specified in `workflows/GPU_EXPERIMENT.md`; **do not mark publisher available before it is implemented and tested**.
- Never configure GitHub Actions, hosted CI or other default billable automation.

## Phase 3 — GitHub collaboration setup
- Configure Issue/PR templates or ask for repository setup permissions if unavailable.
- Use the task states, labels, ownership and handoff contract in `workflows/TASK_MANAGEMENT.md`.
- Create initial backlog Issues: math/specification, reference baseline, CPU correctness, optimized PyTorch implementation, Colab experiment, publication validation, learning milestones.
- Distinguish unavailable label creation/UI configuration from completed actions.

## Phase 4 — Verify, present, hand off
- Validate links and local relative paths **after copying to the target project's layout**, not only inside this Framework repository. Check `.sae/AGENTS.md`, `.sae/protocols/`, `.sae/workflows/`, `.sae/templates/`, `.sae/i18n/zh-CN/` and root `AGENTS.md`; confirm `sae.yaml` parses and pins a real revision. Use the [manual adoption smoke test](docs/ADOPTION_SMOKE_TEST.md) until the bootstrap CLI is implemented.
- Codex runs available CPU tests and logs actual results; Scientist runs Colab tests later.
- Review proposed PR and agree merge permissions with Scientist. No automatic self-approval.
- Report **completed / not run / blocked**, links, exact commit and outstanding credential/environment steps.
- Next explicit instructions: `推进架构师工作`, `推进工程师工作`, `推进导师工作`.

## Idempotency and failure policy
Re-running bootstrap must inspect and *update deliberately*, not overwrite user files. Never delete, force-push, rotate secrets, merge, or publish under an implied permission. If write access is missing, generate a proposed patch/checklist and clearly mark it uncommitted.

## Acceptance criteria
A newly initialized project has an accessible, version-pinned SAE snapshot; root `AGENTS.md`; validated `sae.yaml`; owner/acceptance definitions; an initial issue queue; reviewable engineering scaffolding PR; explicit Colab and GitHub report plan; and no GitHub Actions. These files are the protocol, **not an execution engine**.

## Role recovery in the pinned Bootstrap snapshot

Include [ROLE_RECOVERY.md](workflows/ROLE_RECOVERY.md) and its [Chinese mirror](i18n/zh-CN/workflows/ROLE_RECOVERY.md) in the self-contained `.sae/workflows/` snapshot. Project `AGENTS.md` must link `.sae/workflows/ROLE_RECOVERY.md`. The Bootstrap implementation must preserve pinned-version behavior and check that role restoration works in a fresh chat, without silently upgrading existing projects.

## Ecosystem Review in project snapshots

New project `.sae/workflows/` snapshots must also pin [ECOSYSTEM_REVIEW.md](workflows/ECOSYSTEM_REVIEW.md), with its [Chinese mirror](i18n/zh-CN/workflows/ECOSYSTEM_REVIEW.md). Ensure the pinned Architect protocol and engineering report include the brief Build-vs-Reuse gate; verify relative links in the copied snapshot. Existing projects must opt into updates rather than silently upgrading.

## Colab three-step update (current contract)

The Scientist now uses **three independent notebook steps**: pinned-SHA install, packaged benchmark (no GitHub writes), then **optional explicit report upload** after reviewing results. The Colab Secret is named **`GITHUB_TOKEN`**; Codex must test Publisher subprocess Secret access or provide the secure single-Python-cell environment bridge. Update all implementations and tests to follow [the current three-step contract](workflows/COLAB_TWO_COMMAND.md) (historical filename retained for link stability). No `--publish` in the benchmark default. This supersedes older two-command descriptions above; it is a target until implemented and tested.

## Governance snapshot and owner-wide standing merge authority

Include the `governance/` directory and Chinese mirror in the **version-pinned, self-contained** `.sae/` documentation snapshot. Project `AGENTS.md` should link `.sae/governance/STANDING_AUTHORIZATION.md`, but copied files never grant connector permissions or silently upgrade an existing project. Per the Scientist's later explicit global instruction, **all current and future public GitHub repositories actually owned by `JohnnyZPiggy` are in standing review-and-merge scope without an allowlist or expiration**. Bootstrap does not grant access, enroll a repo, or waive the per-PR T1/T2/T3 merge gate. Check live GitHub owner/visibility, real tool permission and protected branches; private/third-party repos remain out of scope. See [Standing Authorization](governance/STANDING_AUTHORIZATION.md).
