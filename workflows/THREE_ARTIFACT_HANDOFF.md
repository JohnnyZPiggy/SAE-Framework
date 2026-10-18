# Three Research Artifacts — Mathematics, Engineering, Experiment

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/THREE_ARTIFACT_HANDOFF.md)

## Purpose
SAE coordinates work through **three linked scientific artifacts**, rather than relying on chat history or generating unnecessary status paperwork. They live in each **algorithm project repository**, **not** in the SAE Framework repository itself. GitHub Issues and PRs remain the coordination and review system.

| Deliverable and target-project path | Owner / decision authority | Question answered | When updated |
| --- | --- | --- | --- |
| **Mathematical Research** — `docs/research/<algorithm>-tensorization.md` | GPT Scientific Mentor drafts with Scientist; **Scientist decides** | What is the mathematical structure? Which matvec/matrix-free/tensor formulations are justified, and when? | New algorithm, significant redesign, or new mathematical finding |
| **Engineering Report** — `docs/engineering/<algorithm>-engineering.md` | GPT Chief Architect defines specification & acceptance; **Codex owns implementation/test evidence**; Architect reviews | What interfaces/algorithms were implemented, where is the code, and what actually passed? | Architect handoff; then significant engineering PR/revision |
| **Experimental Report** — `reports/gpu/<run-id>/summary.md`, with small machine-readable results | **Scientist runs/approves** Colab experiment; GPT assists design and interpretation | On which source SHA, device, dtype and workload were correctness and performance actually measured? | **Each actual experiment run**; do not overwrite old runs |

## Contract: one question, one authority, connected evidence
- **Math → Engineering:** the Scientist-approved research study supplies equations, assumptions, tensor shapes, reference oracle, limits and `RESEARCH_READY` (or an explicitly documented exception). An unapproved study does not silently authorize optimization engineering.
- **Engineering → Experiment:** the Architect's acceptance criteria and Codex's exact candidate **source commit SHA**, CLI, correctness evidence and reproducible commands define the experiment. CPU verification is **not** GPU verification.
- **Experiment → Research/Engineering:** measured failures and bottlenecks link back to the responsible code PR and mathematical study; GPT and Scientist decide whether to revise math or implementation.
- **No second source of truth:** do not re-copy benchmark numbers into multiple reports. Use links and SHAs. A GitHub Issue/PR records work status; documents record *scientific reasoning and evidence*.
- **Scientific learning:** Mentor explains the math and observations during these handoffs. Important learned facts can be incorporated in the relevant document without forcing a separate learning log.

## Templates (in this Framework repo)
- [Mathematical Research template](../templates/TENSORIZATION_STUDY.md) — already established as the required research gate.
- [Engineering Report template](../templates/ENGINEERING_REPORT.md) — new engineering interface, implementation and CPU evidence record.
- [Experimental Report template](../templates/EXPERIMENT_REPORT.md) — human-operated Colab experiment narrative; complements `manifest.json`, `correctness.json` and `benchmark.csv`.

## Minimal lifecycle
1. **Mentor:** proposes/updates mathematical study; Scientist approves the scientific formulation. Small exploratory checks may be recorded but do not count as production acceptance.
2. **Architect:** specifies software contract, acceptance and formal experiment plan in the Engineering Report or linked Issue; submits a scoped Codex task referencing the mathematical study.
3. **Codex:** implements on branch, **runs actual CPU tests**, updates the Engineering Report with tested commit and commands, and opens a PR. Never self-merges or invents a passing status.
4. **Scientist:** runs pinned candidate in Colab, reviews the actual outputs, publishes small per-run evidence to GitHub when authorized (manual PR until Publisher is implemented); GPT interprets it.
5. **Architect + Scientist:** inspect cross-document links, accept/request revisions; return to Mentor mathematics whenever the evidence challenges assumptions.

## Lightweight rules
- A document is a **living milestone record**; don't create new copies for every minor edit or chat. GPU runs are inherently immutable run-by-run records.
- Not every project needs elaborate prose. Short exact equations, code paths, links, commands and statuses beat lengthy claims.
- Missing evidence is **NOT RUN**, never `PASS`; a planned run is not an executed experiment.
- No automatic writes merely because a role command is invoked; respect tool permissions, explicit authorization and reviewable PRs.
- No GitHub Actions; the Scientist operates Colab and Drive is optional Notebook workspace only.

## Handoff integrity check
The research study, engineering report and experiment summary must cross-reference the same algorithm/Issue and **the actual relevant commits**. Record separate **implementation source SHA** and **report publication SHA** where applicable; do not confuse them.
