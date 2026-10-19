# Changelog

> Language: **English** | [简体中文](i18n/zh-CN/CHANGELOG.md)


## V3.2 canonical-contract consolidation (2026-10-19)

- Replaced the earlier annual / repository-allowlist merge policy with the Scientist's **indefinite, revocable owner-public repository authorization**; GPT Architect retains final reviewed PR merge discretion, not Scientist's substantive decision-making.
- Changed the Scientist's target from two combined commands to **three independent Colab steps**: pinned install, benchmark without publication, and optional separately authorized report upload using Colab Secret `GITHUB_TOKEN`.
- Shortened AGENTS, README, Bootstrap, bilingual role and session/workflow prose; each rule now has a clear canonical source instead of repeated update appendices.
- Updated roadmap, integration docs, `sae.yaml`, issue templates, engineering report order, project/Colab examples, bilingual relative links and CPU/GPU readiness references.
- Preserved historical file paths and the research/CPU/GPU gates; **no existing algorithm project's pinned `.sae/` snapshot was changed**, no Actions were added, and no CLI/CPU/GPU execution is claimed by these documentation changes.

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
