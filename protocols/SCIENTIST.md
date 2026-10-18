# Scientist Protocol — Human Project Owner

> Language: **English** | [简体中文](../i18n/zh-CN/protocols/SCIENTIST.md)


The human Scientist is the **principal investigator**, final scientific decision-maker and actual Colab operator.

## First decision for each new algorithm

Before substantive engineering or GPU benchmarking, work with GPT in **Scientific Mentor** mode to discover mathematical structure and evaluate matrix–vector / matrix-free and other tensor formulations. Read the mathematical study, challenge the derivation and assumptions, and select **RESEARCH_READY / RESEARCH_BLOCKED / NOT_TENSORIZABLE** (or approve a narrowly scoped reference-only exception). Then ask GPT Architect to turn the chosen mathematics into implementable tasks and an experiment plan.

## Scientist-owned experimental deliverable

After the mathematical research decision and Codex's documented engineering validation, the Scientist operates a **pinned source commit** in Colab and reviews the measured results. One actual run produces `reports/gpu/<run-id>/summary.md` (using [EXPERIMENT_REPORT.md](../templates/EXPERIMENT_REPORT.md)) with `manifest.json`, `correctness.json` and `benchmark.csv` where measured. Link back to the mathematical and engineering documents; keep the source SHA distinct from the report-publication SHA. Until Publisher exists, GitHub publication is **manual**, not automatic. See [Three-Artifact Handoff](../workflows/THREE_ARTIFACT_HANDOFF.md).

## Responsibilities
- Select research problems and papers; decide what is scientifically worth implementing.
- Ask GPT Mentor to teach mathematical assumptions, algorithms and GPU experimental principles.
- Decide the accuracy/performance trade-off, baseline and reporting priorities.
- Prepare a small personal Google Drive folder for Colab Notebooks and temporary files only; **no desktop sync, no GitHub/Drive result exchange**.
- Mount/import environment, install pinned repository/PR commit, run thin notebook cells.
- Check the actual device and results, run CPU/GPU experiments, and review warnings.
- Publish small, non-sensitive correctness/performance reports back to GitHub through a tested Publisher CLI (or manual PR until available).
- Approve exceptional or destructive repository actions and retain final authority.

## Scientist experiment checklist
1. Verify tested candidate SHA, installed package SHA, device, package versions and seed.
2. Execute correctness first; treat unexpected errors as blockers.
3. Run warmups, synchronized timing and appropriate repetitions; preserve precision and workload parity.
4. Confirm summary report matches observed output before authorizing publication.
5. Post report-PR/Issue link for GPT review and Codex diagnosis if necessary.
6. Ask Mentor to explain surprising results; decide next scientific direction.

The Scientist need not write the heavy Python code. The AI team should minimize required manual steps without overstating autonomous capabilities.

## Required next-action handoff

At the end of each substantive work cycle, follow the [Next-Action Protocol](../workflows/NEXT_ACTION.md): recommend one specific, copyable role command or Scientist action, at most two useful alternatives, verified GitHub evidence, and any approval needed. Do not request repeated Colab runs before GPU_READY or pretend a command has executed. Offer one-tap actions only where the client actually supports them.
