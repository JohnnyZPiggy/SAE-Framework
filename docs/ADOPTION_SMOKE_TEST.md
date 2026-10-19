# SAE Project Adoption Smoke Test (No GitHub Actions)

> Language: **English** | [简体中文](../i18n/zh-CN/docs/ADOPTION_SMOKE_TEST.md)

**Purpose:** confirm the **copied** SAE Framework is usable inside a target project, not merely that links work in this documentation repository. A protocol file alone does not make an autonomous agent, and this checklist does not claim tests were executed.

## Test 1 — Inspect before any write
1. Pick a disposable or explicitly authorized target repository and record its default branch and current files.
2. Fix the SAE framework at a **real commit SHA** (or immutable release). Avoid a floating reference to `main`.
3. Prepare a proposed patch/branch; do not overwrite an existing project's `AGENTS.md` or other data without review.

## Test 2 — Make the snapshot self-contained
Confirm the target project contains:

```text
<project>/
  AGENTS.md                       # project-specific, usable from THIS root
  sae.yaml                        # includes actual framework SHA
  .sae/
    AGENTS.md                     # shared SAE agent rules
    README.md / README.zh-CN.md   # documentation landing pages
    SAE_BOOTSTRAP.md / CHANGELOG.md
    docs/                         # architecture, figures and links
    examples/                     # template references
    protocols/                    # role instructions
    workflows/                    # including MATHEMATICAL_RESEARCH.md
    templates/                    # including TENSORIZATION_STUDY.md
    i18n/zh-CN/                   # matching bilingual navigation
```

All files under `.sae/` must come from **the same pinned revision**. Check that copied Markdown links resolve within `.sae/` and do not unintentionally escape into missing directories. The root `AGENTS.md` is a **generated/adapted** entry point: its language notice, paths, owner/repository placeholders and SHA must be correct for its new location. Do not assume the raw example's original relative links remain valid.

## Test 3 — Verify protocol behavior
- **Mentor:** with `推进导师工作` on a new algorithm, check that it proposes a mathematical structure study and tensorization research before Codex algorithm implementation.
- **Architect:** with `推进架构师工作`, check the math research gate and Scientist decision before implementation Issue dispatch. Repository scaffolding can proceed separately.
- **Engineer:** with `推进工程师工作`, locate real ready Issues. If `agent:codex` and `status:ready` labels do not exist, **fall back to title/body status** and claim work through a real Issue comment. Never invent a claim or test result.
- **Colab:** the Scientist owns runtime setup. Until Publisher is implemented/tested, mark publication **manual**, and never report GPU success without running it.

## Test 4 — Evidence and security
- Actual Python/CPU tests: `PASS/FAIL/NOT RUN/BLOCKED` with commands, not guessed results.
- No `.github/workflows/` GitHub Actions, no Drive sync, no committed secrets/tokens.
- Changes proposed in a reviewable PR, never force-pushed or silently merged.

## Expected output
A short pass/fail checklist with actual project paths and commits, real Issue/PR links, missing prerequisites, and Scientist actions needed.

**Status:** This document defines a smoke-test procedure; it is **not** evidence that a target project passed the test.


## Test 5 — Three-step Colab configuration and owner-wide grant

- Check target `sae.yaml` has `notebook_command_count: 3`, `publisher_invoked_inside_benchmark_cli: false`, separate run/publish CLIs, and Secret **name** `GITHUB_TOKEN` (never a credential literal).
- Verify pinned `.sae/workflows/GPU_EXPERIMENT.md` resolves **after copying** and describes install → benchmark (local only) → optional separate publish. The old `COLAB_TWO_COMMAND.md` URL may be a compatibility pointer.
- Confirm **live repository ownership and public visibility** and actual GitHub write rights before assuming the owner's [standing grant](../governance/STANDING_AUTHORIZATION.md) applies; this policy does not auto-upgrade existing pinned snapshots or grant tool permissions.
- Benchmark/Publisher are NOT_IMPLEMENTED/NOT_RUN until Codex and Scientist supply real evidence; do not run a tokened upload just to pass a documentation smoke test.
