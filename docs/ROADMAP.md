# SAE Framework V3.2 — Implementation Roadmap

> English | [简体中文](../i18n/zh-CN/docs/ROADMAP.md)

**Current:** SAE has policies, role protocols and templates. **Do not confuse an interface contract with an implemented CLI.** GitHub Issues and actual tests determine completion.

## P0 — Bootstrap CLI (Codex; [Issue #2](https://github.com/JohnnyZPiggy/SAE-Framework/issues/2))

- Read the target repository first; dry-run and review a patch without overwriting files.
- Install a **self-contained snapshot from one immutable Framework commit SHA**, including bilingual role/workflow/governance documents and project-root `AGENTS.md` / `sae.yaml`.
- Verify copied relative links, config schema, missing permissions and repeated initialization. Do not use GitHub Actions or silently upgrade existing algorithm projects.

## P0 — Independent Benchmark and Publisher CLI (Codex; [Issue #3](https://github.com/JohnnyZPiggy/SAE-Framework/issues/3))

- Package installable `PACKAGE_NAME.benchmarks.run` and **separate** `PACKAGE_NAME.benchmarks.publish`; benchmark never publishes.
- Publisher validates allowlisted experiment files, exact tested SHA, report size/privacy, idempotency and a verified GitHub PR. Mock-test failures and authenticate via Colab Secret `GITHUB_TOKEN` or a tested secure process-environment bridge.
- Actual CPU CLI and clean-install tests by Codex; actual GPU/Secret/PR integration by Scientist. Publication is **NOT IMPLEMENTED / NOT RUN** until verified.

## P1 — Three-cell Colab usability

**Pinned source install → GPU benchmark → optional separate GitHub upload after inspecting results.** The normative interface, secure fallback and status mapping live **only** in the [Colab Contract](../workflows/COLAB_TWO_COMMAND.md), historical path preserved. Avoid introducing old benchmark `--publish` integrations or a mandatory GPU rerun.

## P1/P2 — Optional quality improvements

- Local schema/link checking by Codex; do **not** require GitHub Actions.
- Compact Issue/PR status summaries and reviewed protocol migration guides; no new agent/database.

Advance a task only with assigned Issue, scoped PR, real evidence and Architect review.
