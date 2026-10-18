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
Create or update a compact, reviewable `docs/research/<algorithm>-tensorization.md` in the **target project**, using [TENSORIZATION_STUDY.md](../templates/TENSORIZATION_STUDY.md).

Required contents:
- Source problem, assumptions, reference and target operator;
- discovered algebraic structures and data-dependency graph;
- original → transformed equations, shapes/dtypes and proof/approximation boundaries;
- correctness oracle, counterexamples, tolerance rationale and numerical risks;
- theoretical compute/memory estimates and hardware-portability hypotheses;
- proposed experiment questions (not measured outcomes), alternatives and blockers;
- **decision: RESEARCH_READY / RESEARCH_BLOCKED / NOT_TENSORIZABLE**, rationale and Scientist review.

**`RESEARCH_READY` means a mathematically specified, plausibly implementable plan exists; it does not certify numerical correctness or measured acceleration.** If `RESEARCH_BLOCKED` or `NOT_TENSORIZABLE`, do not silently dispatch performance engineering. Scientist may choose a different structure, a limited reference implementation, or explicit exception, recorded in an Issue.

## Gate to Architect and Engineer
1. Scientist reviews research outcome and selects target mathematical formulation.
2. GPT switches to **Chief Architect** to refine software interfaces, correctness gates, experiment matrix and the Codex Issue using the research study as input.
3. Engineering Issue must link the approved study and state what is **proved**, **hypothesized**, and **not yet tested**.
4. Codex then implements reference + tensorized forms and runs CPU tests. Scientist later runs Colab GPU/other hardware tests of the pinned commit; results can return to R1/R2.
5. No fake experimental evidence. Small *mathematical sanity checks* during exploration may be used to falsify a derivation, but must be labeled exploratory, not treated as formal engineering/GPU benchmark acceptance.

## Mentor invocation behavior
With `推进导师工作`, **if the project lacks an accepted research study**, prioritize R1–R3 before general learning or performance discussions. In an ongoing project with an approved study, Mentor can teach or investigate newly revealed structure. One user invocation may cover one bounded research subproblem; ask for scientific approval if decisions are needed.
