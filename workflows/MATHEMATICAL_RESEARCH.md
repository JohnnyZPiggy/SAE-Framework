# Mathematical Structure Discovery & Tensorization Research Gate

> Language: **English** | [简体中文](../i18n/zh-CN/workflows/MATHEMATICAL_RESEARCH.md)

**Primary owner: GPT — Scientific Mentor; scientific approval: Human Scientist.**  
**Position:** mandatory scientific research phase for a **new algorithmic implementation or substantial tensorization redesign**, before implementation assignments and formal hardware benchmarks.

## Research-first principle

**Mathematical structure → equivalent tensor formulation → architecture and experiment design → engineering implementation → evidence-driven CPU/GPU validation.**

This is a **gate**, not a rigid linear pipeline. Findings from Codex or Colab can trigger a return to mathematical research. Repository/bootstrap setup is infrastructure and may happen before this research gate; do **not** begin substantive algorithm reimplementation or claim hardware acceleration before the gate has been addressed.

## Stage R1 — Examine the mathematical problem (Mentor + Scientist)
1. Read the paper/reference algorithm, mathematical definitions, objective, dimensions, input distributions, numerical contract and current implementation (if any).
2. Identify data dependencies and actual operators: linear and affine maps, matrix–vector/matrix–matrix products, tensor contractions, separability, batched independent instances, matrix-free `Ax` or `Aᵀx`, Jacobian-vector / vector-Jacobian products, Hessian-vector products, low-rank/sparse/block/Kronecker structures, reductions and scans.
3. Locate *non-tensorizable* barriers: sequential recurrences, branches, irregular memory access, host sync, graph breaks, dynamic shapes, unavoidable data-dependent control flow.
4. Distinguish mathematical opportunity from implementation assumptions; do not promise speedups or equivalence without support.

## Stage R2 — Derive an equivalent tensor formulation
1. Derive the transformation from the reference algorithm **step by step**. Write both original and candidate mathematical forms with explicit shape and index notation.
2. State proof obligations: equality, valid domain and differentiability (where relevant), numerical and stability assumptions, boundary cases, precision requirements, and limits of approximation.
3. Investigate vectorization, batching, broadcasting, contraction/einsum, linear operator application, `vmap`, batched factorizations, and appropriate functional control-flow primitives—not blindly forcing every loop into a dense tensor.
4. Evaluate asymptotic work, arithmetic intensity, intermediate memory, parallel depth, data movement, compilation overhead, dtype/device portability, and likely CPU/GPU/TPU constraints.
5. Compare at least the **reference**, a **tensorized mathematical candidate**, and a **fallback** if the candidate is unproven or inefficient. If no useful tensorization exists, document this as a valid scientific outcome.

## Stage R3 — Produce a research handoff
Create/update `docs/research/<algorithm>-tensorization.md` in the **algorithm project** using the canonical [Tensorization Study template](../templates/TENSORIZATION_STUDY.md). Record source/assumptions, original-to-tensor equations and shapes, proof or approximation limits, reference oracle/tolerances, dependencies and nonparallelizable barriers, numerical risks, complexity/device hypotheses, alternatives, and **untested** experiment questions. Conclude with **RESEARCH_READY / RESEARCH_BLOCKED / NOT_TENSORIZABLE**, rationale and Scientist decision.

`RESEARCH_READY` permits design, **not** claimed correctness or acceleration. For `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`, hold performance implementation unless Scientist documents a limited exception or selects an alternative.

## Mathematics → Engineering → Experiment artifact link
The Scientist-approved study is the first of [Three Research Artifacts](THREE_ARTIFACT_HANDOFF.md); Architect/Codex use the linked [Engineering Report](../templates/ENGINEERING_REPORT.md), while independently verified runs get separate [Experimental Reports](../templates/EXPERIMENT_REPORT.md). Do not copy measured performance into mathematical hypotheses.

## Gate to Architect and Engineer
1. Scientist approves a formulation or documented narrow exception; Architect designs software, correctness checks, experiment matrix and an Issue linked to the study, distinguishing **proved / hypothesized / NOT RUN**.
2. Codex implements reference/tensorized forms, verifies CPU correctness and executes any GPU/TPU experiment **only after** Scientist hardware/session/time/quota approval and readiness checks, on the exact pinned SHA. Failures may reopen R1/R2.
3. Exploratory mathematical sanity checks may falsify a derivation, but are **not** formal engineering validation or GPU benchmarks. Never invent evidence.

## Mentor invocation behavior
With `推进导师工作`, **if the project lacks an accepted research study**, prioritize R1–R3 before general learning or performance discussions. In an ongoing project with an approved study, Mentor can teach or investigate newly revealed structure. One user invocation may cover one bounded research subproblem; ask for scientific approval if decisions are needed.
