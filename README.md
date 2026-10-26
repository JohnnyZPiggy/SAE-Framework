# SAE Framework V3.3

> **Compute policy:** [Compute Throughput Policy](governance/COMPUTE_THROUGHPUT_POLICY.md) governs GPU-first, high-throughput experiments for all roles. Use all scientifically useful Colab GPU types available under existing authorization; do not impose compute-saving quotas or speculative GPU gates. Provider limits, billing authorization, numerical evidence and session cleanup remain mandatory.


> English normative | [简体中文](README.zh-CN.md)

**Scientist–Architect–Engineer** is a GitHub-first collaboration framework for mathematical algorithms, PyTorch scientific computing and ML engineering. It pursues **two equal goals**: reliable low-cost engineering and the Scientist's deeper mathematical/numerical/ML-systems learning.

## Provider-neutral roles

SAE roles are **capability and authority contracts, not product bindings**: **Scientist** (human), **Architect** (AI agent, e.g., GPT), **Mentor** (AI agent, e.g., GPT), and **Engineer** (AI coding agent, e.g., Codex or Claude Code). One agent may fill Architect and Mentor; multiple Engineers can take turns using separate workspaces and a GitHub Issue/PR + exact-SHA + evidence handoff. Reassignment never transfers credentials, approvals or unverified capabilities. The Engineer never self-merges; the Architect retains the independent review gate. Existing project-pinned snapshots remain unchanged.

## Architecture

Reusable [local preflight and bounded Colab transport](tools/compute/README.md) tools are available for future projects: **SCOPED LIVE_READY (Colab CLI 0.7.4, T4-requested transport-only)** based on [SAE PR #48](https://github.com/JohnnyZPiggy/SAE-Framework/pull/48). Actual device identity was not observed in that transport test. Project-owned drivers/manifests keep scientific code separate; existing pinned snapshots are not migrated.

![SAE V3.3 — native card-style research and engineering architecture (English)](docs/figures/SAE_Framework_V3.3.en.svg)

[Open the full-resolution SVG](docs/figures/SAE_Framework_V3.3.en.svg)

[Editable Mermaid source (.mmd)](docs/figures/SAE_Framework_V3.3.en.mmd)

<details>
<summary>Editable Mermaid architecture diagram</summary>

```mermaid
flowchart TB
    subgraph OBJECTIVES["01 · Two Equal Objectives"]
      direction LR
      O1["Engineering Productivity<br/>Correct · Reproducible · Low Cost"]
      O2["Scientific Learning<br/>Math · Numerics · ML Systems"]
    end

    S["Scientist · Human<br/>Set Goals · Redirect / Stop"]

    subgraph PEOPLE["02 · Research and Engineering Roles"]
      direction LR
      G["Architect + Mentor · AI Agent (e.g., GPT)<br/>Autonomous Math / Research Decisions · Fast Dispatch<br/>Evidence Review · Eligible PR Merges"]
      E["Engineer · AI Agent (e.g., Codex / Claude Code)<br/>Implement / Test · Local CPU<br/>Default Colab CPU / GPU / TPU"]
    end

    H[("GitHub · Single Collaboration and Evidence Hub<br/>Issues · Code · PRs · Source SHA · Reports")]

    subgraph COMPUTE["03 · Engineer Execution / Evidence Loop"]
      direction LR
      L["Local CPU<br/>Install · Numerical correctness · Regression tests"]
      C["Colab CLI / WSL2<br/>CPU · GPU · TPU*<br/>Run / Integrity check / Session cleanup"]
    end

    P["Pinned source SHA → No-GitHub-write benchmark<br/>→ Optional, Architect-reviewed safe evidence PR"]
    D["Google Drive<br/>Optional notebook scratch"]

    O1 --> S
    O2 --> S
    S <-->|Set goals / Feedback / Stop| G
    S -.->|No routine approval queue| E
    G <-->|Issues / Review feedback| H
    E <-->|Code / Evidence PR| H
    G <-->|Iterative collaboration| E
    E --> L
    E -->|Default eligible compute| C
    L --> P
    C --> P
    P -.->|Verified reports via PR| H
    D -.->|Temporary files only| C
    H -.->|New evidence / Next research cycle| G

    classDef goal fill:#EFF5FC,stroke:#9EB9D8,color:#243F5B,stroke-width:1.5px
    classDef human fill:#FFF4E2,stroke:#DDB875,color:#6E4820,stroke-width:2px
    classDef agent fill:#EEF2FF,stroke:#9FA8E7,color:#2D3D73,stroke-width:1.5px
    classDef engineer fill:#EAF8F5,stroke:#78B8AD,color:#164E4B,stroke-width:1.5px
    classDef github fill:#F3EDFB,stroke:#B19ACF,color:#4E3974,stroke-width:2px
    classDef compute fill:#F2F7FA,stroke:#B1C6D4,color:#274659,stroke-width:1.5px
    classDef scratch fill:#F7F7F9,stroke:#C8CBD0,color:#66717D,stroke-dasharray:5 4
    class O1,O2 goal
    class S human
    class G agent
    class E engineer
    class H github
    class L,C,P compute
    class D scratch
```

</details>

The bilingual SVG cards above illustrate the **current provider-neutral SAE roles**: two equal objectives → human Scientist → Architect and Mentor (AI agents, e.g., GPT) → interchangeable Engineers (e.g., Codex and Claude Code) → shared GitHub evidence and local/remote execution. The artwork uses self-contained vector shapes, icons and labels (no raster assets, scripts, external fonts or network dependencies). The embedded Mermaid is an alternate **logical** view; the linked `.mmd` retains the historical diagram source for reference and is not the source of the new card SVGs. Diagram artwork does not itself validate experiments.

*TPU/PyTorch-XLA and automated report publication remain unverified.*

## Who does what?
- **Scientist (human):** sets/changes research goals and can stop work; **no routine mathematical, experimental, resource, T3 or PR approvals**.
- **Architect (AI agent; e.g., GPT):** autonomously decides science, mathematical readiness, engineering/experimental acceptance, iterations and eligible PR merges under [Standing Authorization](governance/STANDING_AUTHORIZATION.md).
- **Mentor (AI agent; e.g., GPT):** leads mathematical structure/tensorization research and explains numerical/experimental results.
- **Engineer (AI coding agent; e.g., Codex or Claude Code):** implements, tests and runs eligible existing-account local CPU and Colab CLI CPU/GPU/TPU experiments by default; verifies outputs and resource cleanup; submits safe evidence through GitHub branches/PRs without self-merging.

**GitHub** is the collaboration and evidence hub. **Colab CLI** supplies remote compute. **Drive** is an optional thin notebook workspace, not a sync/results transport.

## Workflow
Mentor/Architect-decided concise [mathematical study](workflows/MATHEMATICAL_RESEARCH.md) + parallel [Build-vs-Reuse](workflows/ECOSYSTEM_REVIEW.md), reference work and `PROBE_ONLY` device checks → Engineer implementation, correctness and eligible compute → GitHub evidence PR → Architect review/iteration/eligible merge. **No Scientist stage signoffs.** Multiple rounds can return to research.

Experiments have **three separate stages**: exact source-SHA install, benchmark **without GitHub writes**, and optional Architect-reviewed, sanitized report publication (separate user permission remains required for sensitive release or new billing). See [Compute Experiment Protocol](workflows/GPU_EXPERIMENT.md); the [historically named compatibility file](workflows/COLAB_TWO_COMMAND.md) remains linked.

## Optional one-click continuation
When the ChatGPT client supports native actions, each completed Architect/Mentor cycle may end with 2–3 clickable **SAE · Next Action** choices that submit a complete instruction in the same conversation. This does not operate an external Engineer desktop window or change SAE authorization. See [Scientist One-Click Next Actions](workflows/SCIENTIST_ONE_CLICK_NEXT_ACTIONS.md); ordinary concise commands remain the fallback.

## Start
Read [AGENTS.md](AGENTS.md), then [Bootstrap V3.3](SAE_BOOTSTRAP.md). Adopt [project AGENTS](examples/project/AGENTS.md) and [sae.yaml](examples/project/sae.yaml) with a **real pinned framework commit SHA**; do not silently upgrade existing projects.

| Role command | Purpose |
| --- | --- |
| `推进导师工作` | Mathematical discovery and scientific learning |
| `推进架构师工作` | Design, delegate, review and decide merges |
| `推进工程师工作` | Implement, execute authorized experiments and submit PR evidence |

These are user-invoked bounded cycles, not a hosted autonomous agent. No default GitHub Actions/paid CI, secrets in reports, fabricated benchmarks or Drive sync.

## Verification status (2026-10-20)
- **Real Colab transport verified:** [SAE PR #48](https://github.com/JohnnyZPiggy/SAE-Framework/pull/48) is merged (merge SHA `c0cb3c1c59073e61bd8f12e54f9e05eaea7bf2e7`). Pinned tool/source `8081b6e02eee0754903898d5afe5b112f1bb23d0` with Colab CLI 0.7.4 passed one genuine T4-requested allocation, kernel probe, driver execution, artifact SHA-256 and authenticated zero-session cleanup. **SCOPED LIVE_READY applies to transport only**; the hardware identity was not observed in this smoke.
- **First scientific CPU/GPU pilot verified:** [TorchYAND PR #22](https://github.com/JohnnyZPiggy/TorchYAND/pull/22) is merged (merge SHA `1ee2a100db61bc3be62ced9cc7923f261b512b35`). Independent Autograd oracle/gradient and a limited simplex/KKT case passed on CPU and a **verified Tesla T4**, with representative eager MVSK `value_grad` CPU/GPU benchmarks. This is one project-specific scientific pilot, not a blanket full-solver or universal speedup claim.
- **Not established:** generic automatic Colab-to-GitHub publisher, bootstrap CLI, multi-project reuse, TPU/PyTorch-XLA and general cross-device readiness. Independent Colab CPU allocation has not been verified in these two PRs. Project-owned Codex publication of evidence via GitHub PR is demonstrated but does **not** establish the generic Publisher.

## Documentation
[Architect](protocols/ARCHITECT.md) · [Engineer](protocols/ENGINEER.md) · [Mentor](protocols/MENTOR.md) · [Scientist](protocols/SCIENTIST.md) · [Role Recovery](workflows/ROLE_RECOVERY.md) · [Changelog](CHANGELOG.md) · [Chinese index](i18n/zh-CN/README.md)

**Version:** V3.3 architecture and protocol; existing pinned V3.2 project snapshots remain unchanged until explicitly upgraded. **License:** [MIT License](LICENSE) · Copyright © 2026 JohnnyZPiggy. The MIT grant covers original content in this repository; any third-party materials retain their own license terms.

## GPT + Codex deployment: quick start

Use **GPT (ChatGPT + connected GitHub)** as Chief Architect + Scientific Mentor, and **Codex (local coding agent)** as Software Engineer. ChatGPT's GitHub connection does not automatically access Codex's local machine or credentials; share tasks and test evidence through GitHub Issues/PRs and exact commit SHAs.

### Local installation and workspace

Install Git, Python/PyTorch, Codex and optional GitHub CLI by their supported installation methods only if missing. Select your own **D: Dropbox-synced workspace**; this is explicitly allowed, including per-task scratch and cache directories. Example PowerShell commands (replace the placeholder path and repo):

~~~powershell
$Workspace = 'D:\Dropbox\SAE-Work'
New-Item -ItemType Directory -Force $Workspace | Out-Null
Set-Location $Workspace
git clone https://github.com/JohnnyZPiggy/TorchXXX.git
Set-Location .\TorchXXX
git status --short
gh auth status
python -c "import torch; print(torch.__version__)"
~~~

Open the checked-out Torch project in your installed Codex app/CLI. Ask the Engineer to keep task-owned outputs under the user-selected workspace, with isolated Git-ignored scratch (e.g. a project-specific scratch directory). Only clear disposable files created by that task. On WSL2 verify that scratch points to the D: mount (usually /mnt/d/...), not default Linux temp/home inside a C:-backed virtual disk. A project location alone cannot redirect every third-party cache; pass the explicit scratch/cache root to tools that support it. Dropbox sync overhead is an advisory, **not a reason to refuse the workspace**.

### GPT — Architect + Mentor

Connect GitHub to ChatGPT and authorize repository access. In the GPT conversation, replace TorchXXX:

**Cold Start (read-only)**

~~~text
Read https://github.com/JohnnyZPiggy/SAE-Framework Universal Agent Cold Start.
Act as Chief Architect + Scientific Mentor for
https://github.com/JohnnyZPiggy/TorchXXX.
Recover project-pinned SAE rules, task-related Issues/PRs, actual SHA and
mathematical context. First pass read-only; report evidence and next action.
~~~

**Warm Start (Full, or replace with Standard)**

~~~text
Run SAE Full Agent Warm Start as Chief Architect + Scientific Mentor for
https://github.com/JohnnyZPiggy/TorchXXX. Reuse completed Cold Start.
Review one real change, verify one meaningful mathematical identity and
numerical oracle, and specify a bounded Engineer CPU/GPU test.
Report real evidence; do not merge merely to demonstrate readiness.
~~~

### Codex — Software Engineer

Run the installed Codex agent **inside the Torch project directory**.

**Cold Start (read-only)**

~~~text
Read https://github.com/JohnnyZPiggy/SAE-Framework Universal Agent Cold Start.
Act as Software Engineer for the Git repository in the current directory.
Read project-pinned SAE rules, inspect git/gh, branch SHA and relevant
Issue/PR. First pass read-only. Report actual tool access and next action.
~~~

**Warm Start (Full, or replace with Standard for no-GPU check)**

~~~text
Run SAE Full Agent Warm Start as Software Engineer. Reuse Cold Start.
Use my designated D: Dropbox workspace for isolated CPU PyTorch smoke tests,
temporary files and results; verify their location and safe owned cleanup.
If existing authenticated supported Colab CLI and entitlement permit,
run one bounded GPU PROBE_ONLY with observed device identity, CPU oracle,
artifact SHA-256 and confirmed remote session release. No new billing.
Report PASS/FAIL/NOT RUN/BLOCKED, actual paths and next action.
~~~

**GPU-first:** prefer available, supported GPUs for suitable tensor workloads; keep a CPU numerical oracle in parallel. GPU absence never blocks independent CPU/math work. Each actual Colab allocation still needs live authentication, entitlement/session checks and verified cleanup. The generic controller's demonstrated scope is T4-requested transport, not universal GPU/TPU support.

**Daily loop:** GPT scopes mathematics/architecture in an existing Issue → Codex implements and tests in the project workspace → Codex submits SHA-linked code/evidence PR → GPT independently reviews and decides eligible merges. Warm Start is optional and not repeated for every task. Existing projects keep their pinned SAE revisions until intentionally updated. See [Cold Start](workflows/UNIVERSAL_COLD_START.md), [Warm Start](workflows/AGENT_WARM_START.md) and [Standing Authorization](governance/STANDING_AUTHORIZATION.md).

## Universal agent cold start and warm start

For any Torch project, start with [Universal Agent Cold Start](workflows/UNIVERSAL_COLD_START.md) ([中文](i18n/zh-CN/workflows/UNIVERSAL_COLD_START.md)): GPT acts as **Chief Architect + Scientific Mentor** for the target GitHub repository; Codex/Claude Code acts as **Software Engineer** in the project workspace. The first pass is read-only, recovering the project-pinned SAE rules, live task state and exact SHA. **Then optionally invoke [Agent Warm Start](workflows/AGENT_WARM_START.md) ([中文](i18n/zh-CN/workflows/AGENT_WARM_START.md))**: Standard performs a small role-specific capability check; Full adds end-to-end role evidence and a bounded GPU probe for an Engineer when existing authenticated Colab resources are available. Reuse the recovered context, prefer the Scientist-designated workspace (including Dropbox-synced D:), and report actual PASS/FAIL/NOT RUN/BLOCKED. Warm Start is not a recurring gate. Existing project pins are **not** automatically upgraded.
