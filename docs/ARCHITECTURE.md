# SAE V3.3 Architecture and Boundaries

> English normative | [简体中文](../i18n/zh-CN/docs/ARCHITECTURE.md)

![SAE V3.3 native card-style organization architecture (English)](figures/SAE_Framework_V3.3.en.svg)

[View high-resolution vector SVG](figures/SAE_Framework_V3.3.en.svg)

[Editable Mermaid source (.mmd)](figures/SAE_Framework_V3.3.en.mmd)

<details>
<summary>Show editable Mermaid architecture diagram</summary>

```mermaid
flowchart TB
    subgraph OBJECTIVES["01 · Two Equal Objectives"]
      direction LR
      O1["Engineering Productivity<br/>Correct · Reproducible · Low Cost"]
      O2["Scientific Learning<br/>Math · Numerics · ML Systems"]
    end

    S["Scientist · Human<br/>Research direction · Scientific decisions · Compute budgets"]

    subgraph PEOPLE["02 · Research and Engineering Roles"]
      direction LR
      G["GPT · Chief Architect + Scientific Mentor<br/>Math / Tensorization · Design / Delegation<br/>Teaching / Review / Eligible PR Merges"]
      E["Codex · Engineer<br/>Implement / Test · Local CPU<br/>Authorized Colab CPU / GPU / TPU"]
    end

    H[("GitHub · Single Collaboration and Evidence Hub<br/>Issues · Code · PRs · Source SHA · Reports")]

    subgraph COMPUTE["03 · Codex Execution / Evidence Loop"]
      direction LR
      L["Local CPU<br/>Install · Numerical correctness · Regression tests"]
      C["Colab CLI / WSL2<br/>CPU · GPU · TPU*<br/>Run / Integrity check / Session cleanup"]
    end

    P["Pinned source SHA → No-GitHub-write benchmark<br/>→ Optional, separately authorized evidence PR"]
    D["Google Drive<br/>Optional notebook scratch"]

    O1 --> S
    O2 --> S
    S <-->|Research exchange / Scientific approval| G
    S -->|Device / Time / Quota approval| E
    G <-->|Issues / Review feedback| H
    E <-->|Code / Evidence PR| H
    G <-->|Iterative collaboration| E
    E --> L
    E -->|Authorized compute| C
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

The standalone SVG is the designed native-card presentation of V3.3; the collapsible Mermaid remains the editable logical diagram. Both preserve role authority and experiment verification boundaries. Keep bilingual SVGs and Mermaid counterparts synchronized when architecture rules change.

[Current role contracts](../AGENTS.md)

## Two equal outcomes
**Engineering Productivity:** reproducible, correct, maintainable algorithm packages at low coordination and compute cost.

**Scientific Learning:** deepen the Scientist's understanding of mathematical structure, numerical methods, PyTorch, device execution and performance interpretation.

## Authority and execution
- **Scientist:** chooses research direction, approves mathematical/scientific decisions and authorizes GPU/TPU device, session/time/quota budgets. Not the routine Colab operator.
- **GPT Architect + Mentor:** explores mathematics and tensorization, designs interfaces/experiments, assigns GitHub Issues, reviews real evidence, mentors the Scientist and decides eligible PR merges under [Standing Authorization](../governance/STANDING_AUTHORIZATION.md).
- **Codex Engineer:** writes and tests code, runs local CPU and authorized Colab CLI CPU/GPU/TPU experiments, verifies downloaded artifacts and resource cleanup, opens evidence PRs; never self-merges.
- **GitHub:** only durable task and evidence hub (Issues, PRs, source SHAs and the three linked scientific reports).
- **Colab CLI:** compute execution surface, not the report exchange layer. Google Drive is optional temporary notebook scratch, not synchronization.

## Iterative operating loop
Scientist-approved mathematical research → Architect design and Build-vs-Reuse review → Codex implementation/CPU correctness → Architect readiness review → authorized Codex device experiments → GitHub evidence PR → Architect review/eligible merge → Mentor interpretation. Numerical or mathematical failures return to earlier stages; this is not a linear waterfall.

Experiments separate **(1)** exact SHA installation, **(2)** correctness/benchmark without GitHub writes, **(3)** optional separately authorized and validated report branch/PR publication. TPU requires separately verified PyTorch/XLA support. No GitHub Actions or mandatory paid CI.

## Evidence and capability honesty
A 2026-10-19 handoff reports Windows Codex → WSL2 → Colab CLI → T4 GPU smoke test, SHA-256 checking and runtime cleanup. Colab CPU, TPU/PyTorch-XLA, automated GitHub publication and full cross-project workflow remain **NOT VERIFIED** until actual tests establish them.

See [Research Pipeline](../workflows/RESEARCH_PIPELINE.md), [Three Artifacts](../workflows/THREE_ARTIFACT_HANDOFF.md) and [Compute Experiments](../workflows/GPU_EXPERIMENT.md). Existing pinned project snapshots do not upgrade automatically.
