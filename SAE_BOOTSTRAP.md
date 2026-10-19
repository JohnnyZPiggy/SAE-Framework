# SAE Bootstrap — Project Adoption Protocol (V3.3)

> English normative | [简体中文](i18n/zh-CN/SAE_BOOTSTRAP.md)

**Command:** `按照 SAE Framework V3.3 初始化这个项目`

## Inputs and preflight
Confirm target `owner/repo`, default branch, scientific goal, actual tool permissions, existing AGENTS/config, Issues/PRs and a **real immutable SAE commit SHA**. Read the selected framework revision rather than assuming a URL loads it. Do not silently overwrite existing content or upgrade a project's pinned snapshot.

## Adopt a self-contained pinned snapshot
1. Create or update project-root `AGENTS.md` using [project template](examples/project/AGENTS.md) and `sae.yaml` using [config](examples/project/sae.yaml), replacing every placeholder.
2. Copy **one pinned SAE commit** into project `.sae/`, including constitution, bootstrap, protocols, workflows, templates, governance, documentation, examples and bilingual mirrors. Preserve working relative links and record the exact source SHA. This is a documentation snapshot, not a runtime or credential grant.
3. Propose changes on a new branch/PR. Do not install GitHub Actions, paid hosted CI, or a Google Drive synchronization layer.
4. Verify pinned links and config in the **target project layout**, not just this source repository. Use [Adoption Smoke Test](docs/ADOPTION_SMOKE_TEST.md) for manual checks; an automatic bootstrap tool is not assumed to exist.

## Research and engineering initialization
- For new algorithms/major tensorization redesigns, GPT Mentor prepares a [mathematical study](workflows/MATHEMATICAL_RESEARCH.md), reviewed by Scientist (`RESEARCH_READY` or explicit narrow exception) before substantive implementation.
- Architect performs brief [Ecosystem Review](workflows/ECOSYSTEM_REVIEW.md), defines the mathematical/engineering contract and creates scoped GitHub Issues.
- Codex implements the Python package, CPU reference/edge tests and portable benchmark CLI, and executes authorized local and Colab CLI CPU/GPU/TPU experiments. The Scientist approves scientific conclusions and GPU/TPU hardware, concurrent sessions, time and quota **before allocation**, but does not routinely run notebooks.
- Use [Compute Experiment Protocol](workflows/GPU_EXPERIMENT.md): pinned source SHA install → benchmark without GitHub writes → optional separately authorized safe report publication to a GitHub branch/PR. No claim of working Publisher, TPU/PyTorch-XLA or automatic cross-project execution without real tests.
- GitHub holds task and report evidence. Drive, if used, is only a lightweight Colab notebook/temporary workspace.

## Acceptance and failure
Check root AGENTS, `sae.yaml`, complete pinned `.sae/` snapshot, bilingual relative links, role recovery, research gate, initial Issue queue, PR review and explicit experiment/resource plan. Codex records actual CPU/accelerator outcomes; Architect reviews and exercises eligible final merge discretion under [Standing Authorization](governance/STANDING_AUTHORIZATION.md), subject to Scientist substantive decisions and actual permissions.

Re-running bootstrap is **idempotent**: inspect and propose a diff, never silently replace user work, force-push, expose secrets, publish data or merge without applicable authority. Report COMPLETED / NOT RUN / BLOCKED and next action. Existing projects opt into V3.3 through a reviewed pinned-snapshot update; do not change them implicitly.
