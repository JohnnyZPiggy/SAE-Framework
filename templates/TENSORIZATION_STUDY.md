# Research Note — <algorithm>

> Language: **English** | [简体中文](../i18n/zh-CN/templates/TENSORIZATION_STUDY.md)
> Save as `docs/research/<algorithm>-tensorization.md` in the algorithm project. Keep it short.

**Issue:** #<n> · **Source:** <paper / reference code> · **Decision:** RESEARCH_READY / RESEARCH_BLOCKED / NOT_TENSORIZABLE

## 1. Problem
Inputs, shapes, domain, assumptions, target quantity; the reference algorithm (equations or citation).

## 2. Structure
| Candidate structure | Equation and shapes | Parallelism | Obstacle |
|---|---|---|---|
| e.g. batched matvec, matrix-free `Ax`, low rank, Kronecker | | | |

What is **not** tensorizable, and why.

## 3. Tensor formulation
Original → candidate, with indices and shapes. Proof obligations, valid domain, any approximation. Fallback if the candidate fails.

## 4. Oracle and tolerance
The independent reference, the error metric, the tolerance and its reason, the sizes and dtypes that matter, and any degenerate regime worth one edge test.

## 5. Cost hypotheses (not measured)
Work, memory, data movement, compile barriers. Measured results are linked here later, never copied in.

## 6. Decision
- **Proved:** …
- **Hypothesized:** …
- **Unverified:** …
- **Handoff Issue:** #<n>
