---
name: SAE engineering task
about: Delegable numerical or PyTorch engineering work
title: "[SAE] "
labels: []
assignees: []
---

<!-- Optional labels: agent:codex, status:ready, kind:engineering, priority:p1 -->

**Scientific objective / linked Issue:**

**Scientist-approved mathematical study (RESEARCH_READY / scoped exception / N/A for scaffolding):**

**Build-vs-Reuse and dependency decision:** [Ecosystem Review](../../workflows/ECOSYSTEM_REVIEW.md)

**Numerical contract (inputs, shapes, dtype, precision, oracle and tolerances):**

**Expected .py modules, package and CLIs:**

**Acceptance evidence (actual CPU oracle/edge/regression, compile, clean pinned-SHA install, CLI tests):**

**Colab interface (if GPU relevant):** Follow [GPU three-step contract](../../workflows/GPU_EXPERIMENT.md): fixed-SHA pip install → independent benchmark `--out` (no GitHub write) → optional separate publisher `--report-dir` after Scientist reviews. `GITHUB_TOKEN` stays in Colab Secrets; real GPU/publisher runs remain NOT_RUN until tested.

**GPU Readiness / Scientist handoff (if relevant):**

**Dependencies, blocked decisions, risk and rollback:**
