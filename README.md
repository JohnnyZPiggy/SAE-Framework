# SAE Framework V3.3

> English normative | [简体中文](README.zh-CN.md)

**Scientist–Architect–Engineer** is a GitHub-first collaboration framework for mathematical algorithms, PyTorch scientific computing and ML engineering. It pursues **two equal goals**: reliable low-cost engineering and the Scientist's deeper mathematical/numerical/ML-systems learning.

```mermaid
flowchart TB
    G1["Engineering Productivity<br/>Reliable · Reproducible · Low Cost"]
    G2["Scientific Learning<br/>Mathematics · Numerics · ML Systems"]
    S["Scientist<br/>Research direction · Scientific decisions<br/>Compute budget authorization"]
    A["GPT · Chief Architect + Scientific Mentor<br/>Math · Design · Teaching · Review · Merge"]
    E["Codex · Engineer<br/>Implement · Test · Run experiments · Publish PRs"]
    H[("GitHub · Source of Truth<br/>Issues · Code · PRs · Scientific Evidence")]
    C["Colab CLI · Codex-operated<br/>CPU / GPU / TPU*"]
    P["Pinned SHA install → No-write benchmark<br/>→ Optional authorized evidence PR"]
    D["Google Drive · Optional scratch only"]

    G1 --> S
    G2 --> S
    S <-->|Research & decisions| A
    S -->|Device / time / quota approval| E
    A <-->|Specifications / review| H
    E <-->|Implementation / evidence PR| H
    A <-->|Iterative feedback| E
    E -->|Authorized execution| C
    C --> P
    P -->|Verified reports via PR| H
    D -.->|Temporary notebook files| C
    H -.->|New findings / next iteration| A

    classDef goal fill:#eaf4ee,stroke:#73a58b,color:#173b2b
    classDef human fill:#fff1d9,stroke:#d5a450,color:#53350b
    classDef agent fill:#eaf0ff,stroke:#7898d8,color:#203a72
    classDef hub fill:#f1eafa,stroke:#aa8cc8,color:#42265b
    classDef compute fill:#e9f7f8,stroke:#6faab1,color:#16464c
    class G1,G2 goal
    class S human
    class A,E agent
    class H hub
    class C,P,D compute
```

*Rendered natively by GitHub from editable Mermaid. TPU/PyTorch-XLA and automated publication remain unverified.*

## Who does what?
- **Scientist (human):** selects research problems, approves mathematical/scientific conclusions and compute hardware/session/time/quota limits; no routine notebook operation.
- **GPT Architect:** designs specifications and experiments, delegates via Issues, reviews evidence and independently decides eligible PR merges under [Standing Authorization](governance/STANDING_AUTHORIZATION.md).
- **GPT Mentor:** leads mathematical structure/tensorization research and explains numerical/experimental results.
- **Codex Engineer:** implements, tests and runs authorized local CPU and Colab CLI CPU/GPU/TPU experiments; verifies downloads and resource cleanup; submits evidence through GitHub branches/PRs without self-merging.

**GitHub** is the collaboration and evidence hub. **Colab CLI** supplies remote compute. **Drive** is an optional thin notebook workspace, not a sync/results transport.

## Workflow
Scientist-reviewed [mathematical study](workflows/MATHEMATICAL_RESEARCH.md) → Architect [Build-vs-Reuse](workflows/ECOSYSTEM_REVIEW.md) and engineering Issue → Codex implementation, numerical tests and authorized compute → GitHub evidence PR → Architect review/iteration/eligible merge. Multiple rounds can return to research.

Experiments have **three separate stages**: exact source-SHA install, benchmark **without GitHub writes**, and optional separately authorized safe report publication. See [Compute Experiment Protocol](workflows/GPU_EXPERIMENT.md); the [historically named compatibility file](workflows/COLAB_TWO_COMMAND.md) remains linked.

## Start
Read [AGENTS.md](AGENTS.md), then [Bootstrap V3.3](SAE_BOOTSTRAP.md). Adopt [project AGENTS](examples/project/AGENTS.md) and [sae.yaml](examples/project/sae.yaml) with a **real pinned framework commit SHA**; do not silently upgrade existing projects.

| Role command | Purpose |
| --- | --- |
| `推进导师工作` | Mathematical discovery and scientific learning |
| `推进架构师工作` | Design, delegate, review and decide merges |
| `推进工程师工作` | Implement, execute authorized experiments and submit PR evidence |

These are user-invoked bounded cycles, not a hosted autonomous agent. No default GitHub Actions/paid CI, secrets in reports, fabricated benchmarks or Drive sync.

## Verification status (2026-10-19)
The Scientist reported one successful Codex → WSL2 → Colab CLI T4 GPU smoke test with result integrity verification and zero active sessions after shutdown. **Not yet verified:** Colab CPU, TPU allocation/PyTorch-XLA, automatic GitHub publication, cross-project reuse and a complete SAE benchmark-to-PR workflow. Bootstrap/Publisher automation is not established by documentation alone.

## Documentation
[Architect](protocols/ARCHITECT.md) · [Engineer](protocols/ENGINEER.md) · [Mentor](protocols/MENTOR.md) · [Scientist](protocols/SCIENTIST.md) · [Role Recovery](workflows/ROLE_RECOVERY.md) · [Changelog](CHANGELOG.md) · [Chinese index](i18n/zh-CN/README.md)

**Version:** V3.3 architecture and protocol; existing pinned V3.2 project snapshots remain unchanged until explicitly upgraded. **License:** no repository license selected; public visibility alone is not a reuse grant.
