# Algorithm Project AGENTS — Copy to Target Repository Root

> English (normative). [Chinese reference in Framework](../../i18n/zh-CN/examples/project/AGENTS.zh-CN.md). This is a **copyable template**; paths prefixed `.sae/` are intended to resolve **after** copying to the *target repository*, not within this source example folder.

**Project:** `<OWNER>/<PROJECT>`  
**Scientific objective:** `<PAPER_OR_ALGORITHM>`  
**Python package:** `<PACKAGE_NAME>`  
**SAE Framework:** `JohnnyZPiggy/SAE-Framework` V3.2; pinned immutable source SHA: `<ACTUAL_FRAMEWORK_SHA>`  
**Local frozen protocol:** `.sae/`

## Read in this order, before substantive work

1. This project `AGENTS.md` and `sae.yaml`.
2. The real pinned `.sae/AGENTS.md` and role file (`.sae/protocols/MENTOR.md` / `ARCHITECT.md` / `ENGINEER.md`).
3. Required `.sae/workflows/` documents, the current GitHub Issue/PR, exact code SHA and actual evidence.

**Do not silently upgrade `.sae/` or assume a repository URL automatically loads rules.** If snapshot or tool access is missing, report UNVERIFIED and request Bootstrap/permissions.

## Project lifecycle

- New algorithms/major rewrites require `docs/research/<algorithm>-tensorization.md` and Scientist's `RESEARCH_READY` or a documented narrow exception **before** Codex implementation.
- Architect performs a brief PyTorch ecosystem REUSE/ADAPT/BUILD check; Codex runs actual CPU oracle/edge/regression/`torch.compile` (where supported), clean pinned install and CLI tests; Architect alone approves GPU_READY.
- Scientist runs **three separate Colab cells**: pinned source install → packaged benchmark → **optional separate GitHub report upload** after inspecting results. Secret name `GITHUB_TOKEN`. Follow the pinned `.sae/workflows/COLAB_TWO_COMMAND.md` (historical filename). No fabricated tests, GPU claims from CPU or notebook kernels.
- Link research, engineering and experiment reports through GitHub Issue/PR; no GitHub Actions or Drive results sync.

## Commands and merge policy

`推进导师工作` / `推进架构师工作` / `推进工程师工作` trigger **one bounded cycle**, following `.sae/workflows/ROLE_RECOVERY.md` and `NEXT_ACTION.md`.

For **public repositories actually owned by `JohnnyZPiggy`**, Scientist's [current central Standing Authorization](https://github.com/JohnnyZPiggy/SAE-Framework/blob/main/governance/STANDING_AUTHORIZATION.md) gives GPT Architect **indefinite final MERGE/DO_NOT_MERGE discretion after review**, no per-repository enrollment or repeated merge consent. Verify live owner/public visibility, actual tool rights, PR evidence and Scientist-owned substantive decisions. This reference does not create credentials or override stronger project rules; Codex never self-merges. No force-push or background merge sweeps.

**Before adopting this file**, fill placeholders and test all relative paths in the **actual target project**. Do not overwrite an existing project `AGENTS.md` without review.
