# Changelog

> Language: **English** | [简体中文](i18n/zh-CN/CHANGELOG.md)


## V3.3 — Codex-operated compute and constitution simplification (2026-10-19)

- Re-rendered the bilingual V3.3 architecture diagrams as self-contained, ChatGPT-native-card-style SVGs; updated both READMEs and architecture pages. Retained Mermaid as an editable logical diagram and preserved all unverified execution caveats.

- Updated bilingual V3.3 architecture diagrams: high-resolution SVG, GitHub-rendered editable Mermaid, README and architecture docs; historical V3.2 SVGs retained.

- Simplified bilingual AGENTS constitution; preserved two objectives, role boundaries and standing merge authorization.
- Delegated authorized local/Colab CPU/GPU/TPU execution, artifact integrity checks, cleanup and evidence PRs to Codex; Scientist retains scientific decisions and compute budgets.
- Consolidated compute execution rules in GPU_EXPERIMENT.md (historical path retained).
- Verified only a T4 smoke test from the Scientist's handoff; Colab CPU, TPU/PyTorch-XLA, automated GitHub publication and cross-project reuse remain unverified.
- This is a documentation migration; older V3.2 references in other protocols/templates require follow-up alignment before V3.3 can be considered fully migrated.


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
