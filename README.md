# SAE Framework V3.2

> English | [简体中文](README.zh-CN.md)

**Scientist–Architect–Engineer** — a GitHub-first collaboration protocol for mathematics, PyTorch algorithm engineering and scientific learning.

**One Project, Two Outcomes: Better Software, Better Scientist.**

![SAE Framework V3.2 architecture](docs/figures/SAE_Framework_V3.2.en.svg)

[中文架构图](docs/figures/SAE_Framework_V3.2.zh-CN.svg) · [Architecture details](docs/ARCHITECTURE.md)

## How it works

**Research first → verified CPU engineering → Architect GPU_READY review → Scientist-run Colab.** Mentor identifies mathematical matrix/vector/tensor structure; Architect designs and reviews; Codex implements and runs actual CPU tests; Scientist conducts real GPU experiments. The outputs are [three linked artifacts](workflows/THREE_ARTIFACT_HANDOFF.md): mathematical study, engineering report and experiment report. See [Research Pipeline](workflows/RESEARCH_PIPELINE.md).

| Trigger | Role | One bounded cycle |
| --- | --- | --- |
| `推进导师工作` | GPT Mentor | Research mathematics, derive tensorization, teach and hand off |
| `推进架构师工作` | GPT Architect | Review GitHub, make engineering decisions, check PR evidence, independently merge when eligible |
| `推进工程师工作` | Codex Engineer | Implement, run real CPU tests, open an evidence-backed PR, never self-merge |

The commands are instructions to the agents, **not running background services**. Tools and account permissions must be connected separately.

## Colab: three steps, not two

1. Install the package from an **exact source commit SHA**.
2. Run the packaged benchmark and inspect correctness/performance evidence.
3. **Optionally**, after inspection, run a separate GitHub report Publisher using Colab Secret `GITHUB_TOKEN`.

See the [authoritative Colab contract](workflows/COLAB_TWO_COMMAND.md); its historical filename is retained for older links. The benchmark does **not** publish. Publisher/Bootstrap target CLIs are **not implemented or verified merely by these docs**. Scientist operates Colab; there is no GitHub Actions requirement or Drive report synchronization.

## Start a project

1. Read [AGENTS.md](AGENTS.md) (shared agent entry).
2. Read [SAE_BOOTSTRAP.md](SAE_BOOTSTRAP.md) (inspect first, copy **one immutable, self-contained** SAE revision into `.sae/`, preserve existing files).
3. Adapt the [project AGENTS example](examples/project/AGENTS.md) and [`sae.yaml`](examples/project/sae.yaml).
4. Connect the relevant GitHub tools and run the [adoption smoke test](docs/ADOPTION_SMOKE_TEST.md). **A link to a repository does not mean the agent read it.**

## Single sources of truth

| Concern | Authoritative source |
| --- | --- |
| Project roles and common limits | [AGENTS](AGENTS.md) · [role protocols](protocols/) |
| Mathematics / CPU / GPU phase gates | [Research Pipeline](workflows/RESEARCH_PIPELINE.md) |
| Role recovery and next-action messages | [Role Recovery](workflows/ROLE_RECOVERY.md) · [Next Action](workflows/NEXT_ACTION.md) |
| PyTorch ecosystem Build-vs-Reuse | [Ecosystem Review](workflows/ECOSYSTEM_REVIEW.md) |
| Three-cell Colab / safe secret transfer | [Colab Contract](workflows/COLAB_TWO_COMMAND.md) |
| GitHub task workflow and PR review | [Task Management](workflows/TASK_MANAGEMENT.md) · [Code Review](workflows/CODE_REVIEW.md) |
| Final merge authority | [Standing Authorization](governance/STANDING_AUTHORIZATION.md) |

**Standing authorization:** GPT Architect has indefinite, revocable final merge discretion for reviewed PRs in **all current/future public GitHub repositories owned by `JohnnyZPiggy`**, without per-repository registration. Actual GitHub permissions, branch rules, independent evidence and Scientist-owned substantive decisions remain mandatory. Codex never self-merges.

## Current implementation status and boundaries

This is a **documented operating framework**, not a hosted autonomous agent or fully implemented Python package. CPU is the default, GPU the exception; no unexecuted test is a PASS. No token in a repo/log, force push, automatic sweeping or unattended background work. English protocols are normative; [Chinese index](i18n/zh-CN/README.md) and [Language Policy](docs/LANGUAGE_POLICY.md) describe mirrors.

[Roadmap](docs/ROADMAP.md) · [Integrations](docs/INTEGRATIONS.md) · [Templates](templates/) · [Changelog](CHANGELOG.md)

**License:** No repository license is selected yet; public visibility alone does not grant third-party reuse rights.
