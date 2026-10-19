# Changelog

> Language: **English** | [简体中文](i18n/zh-CN/CHANGELOG.md)


## V3.2 single-source consolidation (2026-10-19)

- The Scientist's corrected **indefinite owner-public** merge authorization for all current/future `JohnnyZPiggy`-owned public repositories was reviewed and merged in PR #21. Superseded duplicate PR #20 and role-recovery PR #14 were closed; the [live governance file](governance/STANDING_AUTHORIZATION.md) is the sole grant definition.
- **Three separate Colab cells** supersede the historical two-command design: exact-SHA pip install → independent local benchmark → optional report Publisher after Scientist review. `GITHUB_TOKEN` is a Colab Secret; subprocess inheritance requires actual validation or secure Python upload fallback.
- Consolidated duplicated role, Bootstrap, task-management, PR review, session recovery and experiment documentation. Retained historical `CODE_REVIEW.md`, `NEXT_ACTION.md`, `COLAB_TWO_COMMAND.md`, and Issue/PR template paths as short compatibility links, with canonical definitions elsewhere.
- Updated `sae.yaml`, GitHub Issue templates, roadmap and bilingual mirrors; placed engineering Ecosystem Review section before implementation. No automatic rewrite of already-adopted projects' pinned `.sae/` snapshots.
- **Documentation-only:** Bootstrap, Benchmark and Publisher runtime implementations or real CPU/GPU integration are not implied; no GitHub Actions.

## Colab two-command execution interface (2026-10-18)

- Defined a strict end-user target of **two executable Colab command cells**: pip-install an immutable GitHub source SHA; run one packaged Python benchmark that handles correctness, GPU timing, reports, and **optional authorized** GitHub PR publication.
- Moved four logical stages inside Codex-tested Python modules; GPT Architect owns CLI spec and acceptance tests, Scientist runs the actual Colab GPU integration.
- Added bilingual `COLAB_TWO_COMMAND.md`, updated GPU workflows, Colab examples, roles, bootstrap, configuration examples and roadmap.
- Publisher automation remains **not implemented**; no CLI/GPU performance or upload functionality is claimed until real tests pass.

## Research-first scientific workflow amendment (2026-10-18)

- GPT Scientific Mentor now leads **pre-engineering mathematical structure discovery and tensorization research** (matvec, matrix-free operators, batched tensor contractions and non-parallelizable barriers).
- Scientist reviews a `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE` mathematical study before Architect specifies algorithm implementation tasks or formal GPU benchmarks.
- New bilingual research workflow, template and GitHub Issue forms; architecture diagrams and bootstrap/role/task protocols updated.
- Downstream CPU/GPU findings can iterate back to structure discovery; no automatic speedup claims.
- Project config example adds a `research_gate` section. Existing deployments should explicitly update their **pinned framework snapshot**.

## Framework V3.2 — Initial public protocol package
- Two equal objectives: **Engineering Productivity** and **Scientific Learning**.
- GPT serves as **Chief Architect** and **Scientific Mentor**.
- Codex owns Python modules, CPU testing, benchmarks and PR engineering.
- Human Scientist operates Colab and holds scientific authority.
- GitHub Issues, PRs and compact GPU reports are the shared coordination and evidence center.
- Google Drive is an optional small Colab workspace, never a sync layer.
- No GitHub Actions/paid hosted CI; thin Notebooks; no unverified execution claims.
- Role commands, safe bootstrap, review/publish handoffs, templates and project config included.

**Compatibility note:** V3.2 is the architecture label, not a guarantee that an autonomous runner or a GPU publisher binary already exists. Project integrations must be implemented and validated separately.
