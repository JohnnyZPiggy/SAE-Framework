# Project Agent Entry Point (copy to your project root)

> Language: **English** | [简体中文](../../i18n/zh-CN/examples/project/AGENTS.zh-CN.md)


Project: `<OWNER>/<PROJECT>`
SAE Framework: `JohnnyZPiggy/SAE-Framework`, version V3.2
Pinned framework snapshot: `.sae/` at commit `<REPLACE_WITH_ACTUAL_FRAMEWORK_SHA>`

## Read before work
1. This file and `sae.yaml`.
2. `.sae/AGENTS.md` (shared rules).
3. Your role: `.sae/protocols/ARCHITECT.md`, `ENGINEER.md` or `MENTOR.md`.
4. Applicable `.sae/workflows/*.md` and Issue/PR specifications.

**Do not assume a URL automatically loads instructions.** Check that the snapshot exists. If not, stop and request bootstrap.

## Pre-engineering math discovery
Before algorithm implementation/benchmarks, read `.sae/workflows/MATHEMATICAL_RESEARCH.md` and have GPT Mentor + Scientist produce and review `docs/research/<algorithm>-tensorization.md`. Architect dispatches Codex work only with `RESEARCH_READY` or a documented Scientist-authorized exception. Tensorization is a mathematical research outcome, not guaranteed speedup.

## Linked math, engineering and experimental records
Use `.sae/workflows/THREE_ARTIFACT_HANDOFF.md` to keep a mathematical study in `docs/research/<algorithm>-tensorization.md`, a milestone implementation/CPU validation record in `docs/engineering/<algorithm>-engineering.md`, and actual Scientist-run experiment summaries in `reports/gpu/<run-id>/summary.md`. Reference Issues/PRs and tested SHA; no duplicate performance claims or invented tests.

## Project-specific notes
- Scientific objective: `<PAPER_OR_ALGORITHM>`
- Python package: `<PACKAGE_NAME>`
- Scientist runs Colab GPU experiments; Codex runs CPU tests; GPT reviews and mentors.
- GitHub Issues/PRs are the only shared task/evidence channel. No GitHub Actions, no Drive syncing.
- Core calculations and publishing live in tested Python modules; Notebooks orchestrate only.
- Never overwrite files or publish secrets; no self-merges.

## Invocations
`推进架构师工作` / `推进工程师工作` / `推进导师工作`.
