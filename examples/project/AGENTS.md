# Project Agent Entry Point (copy to your project root)

Project: `<OWNER>/<PROJECT>`
SAE Framework: `JohnnyZPiggy/SAE-Framework`, version V3.2
Pinned framework snapshot: `.sae/` at commit `<REPLACE_WITH_ACTUAL_FRAMEWORK_SHA>`

## Read before work
1. This file and `sae.yaml`.
2. `.sae/AGENTS.md` (shared rules).
3. Your role: `.sae/protocols/ARCHITECT.md`, `ENGINEER.md` or `MENTOR.md`.
4. Applicable `.sae/workflows/*.md` and Issue/PR specifications.

**Do not assume a URL automatically loads instructions.** Check that the snapshot exists. If not, stop and request bootstrap.

## Project-specific notes
- Scientific objective: `<PAPER_OR_ALGORITHM>`
- Python package: `<PACKAGE_NAME>`
- Scientist runs Colab GPU experiments; Codex runs CPU tests; GPT reviews and mentors.
- GitHub Issues/PRs are the only shared task/evidence channel. No GitHub Actions, no Drive syncing.
- Core calculations and publishing live in tested Python modules; Notebooks orchestrate only.
- Never overwrite files or publish secrets; no self-merges.

## Invocations
`推进架构师工作` / `推进工程师工作` / `推进导师工作`.
