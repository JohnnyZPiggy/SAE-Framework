# SAE Framework V3.2 — Engineering Roadmap

> English normative | [简体中文](../i18n/zh-CN/docs/ROADMAP.md)

**Implemented here today:** SAE governance/roles, research and experiment protocol, linked artifact templates, pinned-snapshot examples. **Not an autonomous agent runner**; don't confuse a documented CLI target with an installed/testing-passed package.

## P0 — Bootstrap CLI (Codex, [Issue #2](https://github.com/JohnnyZPiggy/SAE-Framework/issues/2))

- Idempotent, dry-run-first project scaffold from an **immutable** Framework commit.
- Correct target-root AGENTS, `sae.yaml` and complete pinned `.sae/` snapshot with working English/Chinese relative links, protocols and governance.
- CPU tests for fresh/existing repository, absent permissions, malformed YAML, frozen SHA and re-entry. No silent overwrite or framework-version upgrade.

## P0 — Separate GitHub Publisher CLI (Codex, [Issue #3](https://github.com/JohnnyZPiggy/SAE-Framework/issues/3))

- Independent `benchmarks.publish --report-dir`, **not** a `--publish` flag inside `benchmarks.run`.
- Sanitize and validate `manifest.json`, `correctness.json`, `benchmark.csv`, `summary.md` with tested source SHA, file size and data safeguards.
- Secure runtime `GITHUB_TOKEN` access (actual Colab subprocess test or safe Python-cell injection), branch/PR creation, idempotent retries and honest permission/error states; no direct main push/auto-merge.
- Mock/offline test first. Scientist authorizes any real public report upload after reviewing results.

## P1 — Three-cell Colab workflow (Architect specification + Codex packaged CLI)

1. Pinned-SHA pip install.
2. Independent `benchmarks.run --device cuda --out ...`: verify correctness before GPU timings, write **local** report, **never** publish automatically.
3. **Optional** `benchmarks.publish --report-dir ...`: the Scientist deliberately uploads an already reviewed report; third cell may be a secure Python subprocess fallback.

See the sole [GPU Experiment / Colab Contract](../workflows/GPU_EXPERIMENT.md). Codex tests clean install and CPU behavior; real GPU and Secret access only pass after Scientist Colab evidence. Current CLIs remain **NOT_IMPLEMENTED / NOT_VERIFIED** unless a concrete project provides actual tested commands.

## P1 — Lightweight local validation

- YAML/JSON schema checking and Markdown relative-link verification in Codex/local environment, **without GitHub Actions**.
- Validate template instantiation in a fresh repository and preserve pinned adoption compatibility.

## P2 — Optional quality of life

- Small Issue/PR status summary, learning-note tooling and explicit opt-in snapshot migration.

Only mark an item complete after inspecting real PR and actual test evidence. Keep the [Agent Constitution](../AGENTS.md), [Standing Authorization](../governance/STANDING_AUTHORIZATION.md) and [Role Recovery](../workflows/ROLE_RECOVERY.md) as single sources.
