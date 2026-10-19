# SAE Algorithm Project — AGENTS.md (copy to TARGET repository root)

> This file is a **template**, not the live rules of SAE-Framework. On adoption fill every placeholder, copy a self-contained snapshot and validate links in the **target root**.

**Repository:** `<OWNER>/<PROJECT>`  
**Research goal / algorithm:** `<PAPER_OR_ALGORITHM>`  
**Python import package:** `<PACKAGE_NAME>`  
**SAE version:** V3.2 · Framework `JohnnyZPiggy/SAE-Framework`  
**Immutable pinned snapshot:** `.sae/` from `<ACTUAL_40_CHARACTER_FRAMEWORK_SHA>`

## Role and state recovery (mandatory)

At the start of **every substantive task**, read in order:
1. This project-root `AGENTS.md` and `sae.yaml`.
2. Pinned `.sae/AGENTS.md` and the current role file `.sae/protocols/{MENTOR,ARCHITECT,ENGINEER,SCIENTIST}.md`.
3. [Role Recovery / Next Action](.sae/workflows/ROLE_RECOVERY.md), related pinned workflow and **real GitHub Issues, PRs and evidence**. A repository URL alone is not proof the agent read anything.

Use `推进导师工作` / `推进架构师工作` / `推进工程师工作` as assigned. Do one bounded, role-appropriate cycle, then provide verified status and one next step. Do not silently change pinned policy or invent laptop/GPU access.

## Scientific and engineering gates

- **Research first:** before new algorithm implementation or formal acceleration, Mentor and Scientist review [mathematical structure](.sae/workflows/MATHEMATICAL_RESEARCH.md), write `docs/research/<algorithm>-tensorization.md`, and record `RESEARCH_READY` or a Scientist-authorized narrow exception.
- **Architecture:** GPT Architect checks [Ecosystem Review](.sae/workflows/ECOSYSTEM_REVIEW.md) for native PyTorch and suitable maintained libraries, then dispatches an Issue with an oracle, exact tolerances and CPU/CLI acceptance.
- **CPU first:** Codex implements modules, runs actual oracle/edge/regression tests, relevant CPU `torch.compile`, clean pinned pip install and packaged CLI smoke/benchmark, and submits a PR **without self-merging**.
- **GPU by exception:** Architect reviews [GPU Readiness](.sae/templates/GPU_READINESS.md). Only then Scientist runs the pinned [three-step Colab workflow](.sae/workflows/GPU_EXPERIMENT.md): install → independent benchmark → optional stand-alone Publisher after reviewing outputs. Colab Secret name is `GITHUB_TOKEN`; Publisher CLI remains unverified until tested.
- **Three linked artifacts:** mathematical study, engineering report and actual experiment report; see [handoff](.sae/workflows/THREE_ARTIFACT_HANDOFF.md).

## Owner-level merge delegation and limitations

Consult the [current central Standing Authorization](https://github.com/JohnnyZPiggy/SAE-Framework/blob/main/governance/STANDING_AUTHORIZATION.md). The Scientist's **indefinite, revocable** grant covers qualifying PRs in **all current/future public repositories actually owned by `JohnnyZPiggy`**, without per-repository registration. This template or its copied snapshot **does not create GitHub API rights**. Architect must verify live owner/public visibility, connected tool merge capability, full PR diff/test evidence and Scientist-owned substantive science/security decisions before independently choosing MERGE/DO_NOT_MERGE; respect stricter project constraints. Private/other-owner repos require different explicit authority. Codex never self-merges.

No GitHub Actions, unpaid-test claims, Drive sync, notebook numerical kernels, force push, leaked credentials, or unattended work. All important operations and failures belong in GitHub Issues/PRs.
