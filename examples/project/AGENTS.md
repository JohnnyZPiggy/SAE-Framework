## Integrated algorithm-project operating contract

Use the pinned `.sae/` snapshot. Follow research → CPU engineering/`torch.compile` → Architect-reviewed GPU_READY → Scientist-run Colab. Maintain linked mathematical, engineering and experimental artifacts. A clean pinned-SHA pip install and one packaged benchmark CLI are the target Colab interface. Do not ask Scientist for repeated GPU runs before CPU-local fixes; do not claim Publisher implemented without real tests. See `.sae/workflows/RESEARCH_PIPELINE.md`, `.sae/workflows/THREE_ARTIFACT_HANDOFF.md`, `.sae/workflows/COLAB_TWO_COMMAND.md`.

# Project Agent Entry Point (copy to your project root)

> Language: **English** (canonical). After installation, the Chinese reference is available at `.sae/i18n/zh-CN/examples/project/AGENTS.zh-CN.md`. This is a **copyable project-root template**; source-repository relative links must not be carried into a different root unchanged.


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

## Project-specific notes
- Scientific objective: `<PAPER_OR_ALGORITHM>`
- Python package: `<PACKAGE_NAME>`
- Scientist runs Colab GPU experiments; Codex runs CPU tests; GPT reviews and mentors.
- GitHub Issues/PRs are the only shared task/evidence channel. No GitHub Actions, no Drive syncing.
- Core calculations and publishing live in tested Python modules; Notebooks orchestrate only.
- Never overwrite files or publish secrets; no self-merges.

## Invocations
`推进架构师工作` / `推进工程师工作` / `推进导师工作`.

## Mandatory next-action handoff

After each substantive role cycle, recommend one next command and up to two alternatives with evidence and required Scientist approval. Follow the pinned [Next-Action Protocol](.sae/workflows/NEXT_ACTION.md). Do not imply local execution or GPU readiness without actual evidence.

## Recover role and state first

Before each substantive role cycle, follow the pinned [Role Recovery & Integrity Protocol](.sae/workflows/ROLE_RECOVERY.md). Verify the user's role command, current project Issues/PRs, phase gate and actual tools; do not silently switch roles, assume laptop access or upgrade the pinned `.sae/` snapshot. End with the pinned [Next-Action](.sae/workflows/NEXT_ACTION.md) footer.

## Ecosystem review at architecture time

Before Codex implementation dispatch, Architect follows the pinned [Ecosystem Review](.sae/workflows/ECOSYSTEM_REVIEW.md): review native PyTorch, third-party and reference implementations; document a concise Build-vs-Reuse decision in the engineering report, favoring CPU-first portability and limited dependencies. No automatic upgrades to pinned SAE snapshots.

## Permanent Architect merge decision for owner's public repositories

The project adopts its pinned [governance reference](.sae/governance/STANDING_AUTHORIZATION.md) and consults the [current owner-level Standing Authorization](https://github.com/JohnnyZPiggy/SAE-Framework/blob/main/governance/STANDING_AUTHORIZATION.md). **The Scientist has already granted GPT Architect indefinite final MERGE / DO_NOT_MERGE discretion for all current and future public repositories actually owned by `JohnnyZPiggy`; no separate algorithm-repo registration is required.** Verify via GitHub's live owner.login/public visibility and actual merge tools: copying `.sae/` does not itself grant credentials, and another owner's repo is excluded. Observe project-specific stricter review gates and Scientist-owned substantive decisions. Architect audits and merges qualifying PRs; Codex never self-merges or auto-upgrades pinned rules.
