# SAE Framework Roadmap

> Language: **English** | [简体中文](../i18n/zh-CN/docs/ROADMAP.md)


This repository currently provides **architecture, role instructions, onboarding steps, and templates**. The following automation components are proposed, **not yet implemented/tested**:

## P0 — Bootstrap helper (Codex)
- Safe, idempotent project scaffolder from a pinned SAE commit.
- Dry-run and clear diff; no overwrite by default.
- Generates project AGENTS/config, frozen policy snapshot, Issue/PR templates.
- Unit tests for existing/empty repos, missing permissions and malformed config.

## P0 — Experiment Publisher CLI (Codex)
- Validate report manifest/schema, redact potential secrets, enforce size limits.
- Commit reports to `experiment/<run-id>` branch, propose PR and link originating Issue/implementation PR.
- Report success only after GitHub API confirms commit and PR; retry safely with idempotency key.
- Test publisher offline/mock first; execute integration test only with explicitly granted scope.

## P1 — Two-command Colab interface (GPT design + Codex implementation)

- **Exactly two executable Notebook command cells** after one-time GPU/credential setup: pinned GitHub pip install → single packaged `python -m <package>.benchmarks.run --device cuda --publish`.
- GPT specifies defaults, mathematical oracle, CLI, device checks, experiment evidence and acceptance; Codex implements/test-packages all algorithms, correctness, benchmarking, reporting and Publisher integration **outside Notebook**.
- Device/env checks, correctness before timing and source-SHA provenance are performed inside the single CLI; no manual third publish command in the **final design**.
- CPU clean pip/CLI smoke tests by Codex; real GPU + optional PR upload Colab acceptance by Scientist. Current state is **not implemented**. See [Two-Command Contract](../workflows/COLAB_TWO_COMMAND.md).

## P1 — Optional machine validation (Codex)
- Local Python schema validation for `sae.yaml` and experiment JSON.
- Run via Codex terminal/Colab; no GitHub Actions.

## P2 — Quality of life
- Issue/PR status report CLI; simple learning note templates.
- Version migration guide with reviewed updates and backwards compatibility.

All roadmap items require an Issue, an owner, acceptance criteria and real test evidence before marking complete.
