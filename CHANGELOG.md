# Changelog

> Language: **English** | [简体中文](i18n/zh-CN/CHANGELOG.md)


## V3.4 — Repository cleanup: one page per concept (2026-10-30)

- **README** rewritten (~205 → ~70 lines): what SAE is, the roles table, a V3.4 flow diagram, a repository map and status. The outdated GPT deployment guide was removed. The architecture figures in `docs/figures/` stay; their agent names are examples.
- **17 workflows → 4:**
  - [Start](workflows/START.md): cold start, role recovery, warm start only on change, compute-tool discovery, end-of-turn handoff, project adoption and ready-to-paste prompts;
  - [Tasks](workflows/TASKS.md): Issues, EXPLORE/VALIDATE, where results live, review;
  - [Research](workflows/RESEARCH.md): R1–R3, reuse first, learning;
  - [Compute](workflows/COMPUTE.md): the throughput policy plus the experiment procedure.
- **Governance:** Standing Authorization shortened and now includes the security rules; the Compute Throughput Policy moved into Compute; the Simplicity Contract is unchanged.
- **Protocols:** Scientist and Mentor rewritten; all four now point to the new workflows; "GPT decides" wording removed throughout.
- **Removed:**
  - `docs/` text pages (architecture, integrations, roadmap, language policy, adoption smoke test; their content is folded into README and Start);
  - `reports/` (V3.3 evidence directories);
  - `SAE_BOOTSTRAP.md` (now Start § Adopt);
  - Engineering Report and GPU Readiness templates;
  - `examples/colab`, `examples/reports`;
  - `tools/compute/diagnostics/` (CLI 0.7.4 one-off scripts).

  All of it remains in Git history and at older pins.
- **Templates:** the research note and run summary were cut to their fields. **Examples:** the project `AGENTS.md` carries the "Simplicity first" section; a new `sae-README.md` provides the `.sae/README.md` template; `sae.yaml` was trimmed.
- **Compute tools:** README reduced from 106 to ~50 lines with no dead links. Code is unchanged.
- **Projects pinned to older SAE commits are unaffected.** When bumping a pin, update the project's `.sae/README.md` links to the new file names (see `examples/project/sae-README.md`).

## V3.4 — Simplicity Contract: less defensive code, Claude as default Architect (2026-10-30)

- **Problem:** under V3.3, Engineer agents (Codex) produced far more code, tests and evidence than the science needed — hand-written JSON/ASCII validators, `ast` parsing of driver files, test files longer than the code under test, ~17k lines of evidence for a 25-line criterion. Root cause was the framework: defensive requirements repeated in every document, test checklists that demanded every category, no size budget in dispatches, and reviews that could only ask for more.
- **New [Simplicity Contract](governance/SIMPLICITY_CONTRACT.md)** (binding, overrides older text that asks for more): validate only at trust boundaries and trust internal code; banned-pattern table; one test per changed behavior plus an independent oracle for numerical claims; Git as the integrity layer with evidence file caps (absorbs the lean-evidence rules proposed in PR #70); dispatches carry Definition of Done, S/M/L size budget, required tests and a *Not required* list; Engineers stop at 1.5× budget; new review outcome `REQUEST_SIMPLIFY`. Non-negotiables (SHA, honest status, oracle, observed device, cleanup, secrets, no self-merge, no new spending) are now stated once.
- **Engineer protocol rewritten** around a six-step loop; Architect protocol owns the size budget; Code Review checks size before correctness; Issue/PR templates (repo and `.github/`) slimmed to the fields that steer effort; GPU evidence reduced to `summary.md` + one results file; Standing Authorization T2 evidence points to the Issue's required tests.
- **Claude is the default Architect + Mentor** (role remains provider-neutral). Repeated compute-policy banners removed from individual documents; the policy itself is unchanged.
- Example `sae.yaml` bumped to `3.4` with a `simplicity` block. Existing project pins are **not** upgraded automatically. `tools/compute` code is unchanged in this release.

## V3.3 — Lean Research Lab Phase 1: Explore / Validate and one Codex batch (2026-10-20)

- Fix the new-project `sae.yaml` template: GPT decides research, prior Scientist science/GPU-budget approval defaults are false, Architect evidence review replaces ambiguous per-PR authorization, and extra billing still requires explicit user consent. Preserve existing V3.3 schema version and immutable project snapshots.
- Introduce bilingual Lean Lab (now part of `workflows/TASKS.md`): EXPLORE uses a bounded testable hypothesis and compact batch log; VALIDATE requires justified math, exact source SHA, numerical correctness and reproducible performance evidence. A `PROBE_ONLY` check is not proof of speedup/TPU support.
- One existing/new GitHub Issue can hold a finite Codex implementation→test→repair→rerun batch, with default one active Colab session, a task-defined timeout, bounded repair attempts and one consolidated outcome rather than PR/report spam.
- Align bilingual new-project bootstrap, adoption smoke test, GPU Readiness, PR and task/three-artifact/research templates. No algorithm-project migration, extra agent, background service, Actions, purchased compute or claimed end-to-end runtime validation.

## V3.3 — Bilingual native-card architecture SVG refresh (2026-10-20)

- Replaced the English and Chinese `docs/figures/SAE_Framework_V3.3.*.svg` diagrams with vector-only reproductions of the confirmed ChatGPT Native UI card organization: equal engineering/science goals, Scientist goal setting, GPT Architect/Mentor delegated authority, Codex direct execution, CPU/GPU/TPU and GitHub feedback.
- Verified local SVG parsing and rendered previews, and updated both README embeds/architecture descriptions. Existing SVG paths remain stable; `.mmd` and README Mermaid are logical companion sources rather than the exact card artwork.
- Diagram reflects post-PR #33 authority; it does not imply unverified TPU, Publisher or agent-autonomy E2E tests have passed.

## V3.3 — GPT autonomous decision Fast Lane (2026-10-20)

- Scientist explicitly delegates in-scope **scientific, R1–R3 research-gate, acceptance, engineering and T1/T2/T3 PR decisions** to GPT Architect/Mentor; the Scientist sets/redirects goals but has **no routine approval role**. Replaces earlier reserved-science and Scientist-stage-approval language while preserving the revocable user direction and owner-public merge scope.
- Run fast: GPT may record `RESEARCH_READY / RESEARCH_BLOCKED / NOT_TENSORIZABLE` or a scoped hypothesis directly; overlap math, Build-vs-Reuse, CPU reference/package preparation and finite `PROBE_ONLY` Colab device diagnostics. Codex executes and provides verifiable evidence, GPT reviews/merges. No mandatory Scientist approvals or repeated multi-agent signoff.
- Retain real numeric correctness and formal-benchmark proof, exact tested SHA, actual GitHub/device permissions, sanitized public evidence, session timeouts/cleanup and no invented execution. New billable commitments, nonpublic/sensitive releases, external account/security-permission changes and irreversible external destructive actions require distinct explicit user instructions. No background scheduler, GitHub Actions or automatic upgrades of pinned project snapshots.
- Synchronized normative bilingual roles, governance, research/compute/review workflows, task/report templates, bootstrap, README Mermaid and documentation. Existing illustrative SVG artwork predates this role-decision update and is non-normative; render a new visual in a separate cosmetic update if desired.

## V3.3 — Experiment by Default: remove Scientist compute permission gate (2026-10-20)

- User-directed T3 simplification supersedes the earlier No Price Gate standing-approval mechanism: Codex directly performs bounded existing-account CPU/GPU/TPU runs with **no Scientist compute authorization/grant lookup**. Architect dispatches/reviews; Scientist keeps scientific conclusions and substantive decisions.
- Short environment/GPU/TPU-XLA `PROBE_ONLY` diagnostics may start before formal mathematical/CPU benchmark readiness; they are never accepted as numerical correctness or performance evidence.
- Keep actual tool/account permission checks, pinned SHA, task-defined finite timeout, default single session, artifact evidence and session cleanup; new monetary commitments and sensitive/public publication require distinct user/security approval. No silent upgrades of pinned algorithm snapshots, no new background scheduler or CI.
- Align bilingual protocols, governance cross-references, task lifecycle, role recovery, experimental evidence and Issue/PR templates.

> Historical note: superseded by the 2026-10-20 Experiment by Default amendment above.

## V3.3 — No Price Gate standing Colab compute authorization (2026-10-20)

- Scientist expressly grants revocable standing authorization for Codex to use existing Colab account entitlements/prepaid Compute Units for scoped CPU/GPU/TPU work without new per-run price estimates, quotas or budget approvals. Existing credits may be consumed to exhaustion.
- Keep math/CPU-readiness/source SHA and actual access checks, one active session by default, finite task timeout, cleanup and honest device evidence. New subscriptions, top-ups, pay-as-you-go or other incremental billing remain separately authorized.
- Align English/Chinese role recovery, Architect/Engineer/Scientist, research pipeline, Next-Action and merge-governance references; no compute run, new CI, background scheduler or silent pinned snapshot upgrade.

## V3.3 — Protocol consistency and documentation cleanup (2026-10-19)

- Aligned historical Scientist-operated Colab wording to V3.3: Codex executes only approved local/Colab experiments; Scientist retains resource/scientific/publication decisions. No allocation or experimental claims.
- Updated outdated benchmark/publisher and PR/Issue templates, placed Ecosystem Review section 2a before implementation in both engineering templates, removed duplicated embedded Mermaid blocks from bilingual architecture pages while preserving README diagrams and `.mmd` sources.
- Preserved research gates, numerical evidence, three artifacts, standing merge scope, Next-Action completion, pinned project snapshots and GitHub Actions-free workflow.

## V3.3 — Next-Action Completion Gate (2026-10-19)

- Make end-of-cycle status/evidence/one-command handoff a pre-send self-check for GPT Mentor, GPT Architect and Codex Engineer, including long or blocked cycles.
- Provide up to two genuine alternative commands and separate copyable plain-text blocks when the client lacks working interactive controls; never pretend a button invokes Codex.
- Documentation-only, without an output validator, background runner, compute allocation, CI or silent updates to pinned algorithm-project snapshots.

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
