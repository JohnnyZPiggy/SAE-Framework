# Research — Mathematics, Reuse and Learning (V3.4)

> English normative | [简体中文](../i18n/zh-CN/workflows/RESEARCH.md)

**Structure → equivalent tensor form → design → implementation → measured validation.** This is an evidence gate for *formal* claims, not a queue: reference code, tooling and `PROBE_ONLY` device checks may run alongside it, and a failed probe can reopen the mathematics.

## R1 — Understand the problem (Mentor)
Read the paper or reference algorithm: objective, dimensions, numerical contract, any existing code. Find the real operators: matvec/matmul, matrix-free `Ax`, contractions, batched independent instances, low-rank/sparse/Kronecker structure, JVP/VJP/HVP, reductions. Name the barriers too: sequential recurrences, data-dependent control flow, dynamic shapes, host syncs.

## R2 — Derive the tensor formulation
Write the original and the candidate side by side with explicit shapes. State the proof obligations: equality and its domain, stability, edge cases, any approximation. Compare three options: the **reference**, the **tensorized candidate** and a **fallback**. Estimate work, memory, data movement and compile barriers as hypotheses, never as measured speedups. "No useful tensorization" is a valid result.

## R3 — Decide and hand off
Write `docs/research/<algorithm>-tensorization.md` from the [template](../templates/TENSORIZATION_STUDY.md) and decide `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`. No Scientist signoff. Hand the Architect the independent oracle, the tolerance and the sizes/dtypes that matter. `RESEARCH_READY` allows a formal build and benchmark; it is not itself a correctness claim.

## Reuse before building (Architect, in parallel with R1–R2)
Check three places, briefly:
1. **PyTorch native:** `torch.linalg`, `torch.func`/`vmap`, `torch.sparse`, `torch.compile`.
2. **A maintained library**, only if native coverage is missing. Check its license, release activity and dependencies.
3. **Reference code** from the paper or upstream, usually as an *oracle* rather than a dependency.

Pick **REUSE / ADAPT / BUILD** and record it in one line in the Issue: source, version or SHA, license, and the gap your work fills. Shortlist at most three candidates. If you cannot inspect a package, mark it `UNVERIFIED` rather than guess.

## Learning
Learning runs alongside the engineering and is equally valued. For each milestone the Mentor:
1. picks one idea tied to the current work;
2. explains intuition → derivation → a falsifiable prediction;
3. lets the Scientist try an explanation or a small check;
4. compares the prediction with the measured result and explains the gap (numerics, implementation, hardware).

One question at a time. Notes are optional, and learning never replaces tests.
