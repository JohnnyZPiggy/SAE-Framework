# Research-First, CPU-Validated, GPU-Finalized Pipeline

> English | [简体中文](../i18n/zh-CN/workflows/RESEARCH_PIPELINE.md)

## Normative default

**CPU by Default. GPU by Exception.** SAE projects follow three phases, with the Scientist's GPU time concentrated **after** mathematics and CPU engineering are ready. This is a workflow rule, not a claim that CPU performance predicts GPU performance. Keep GitHub as the durable source of truth; no GitHub Actions, mandatory Drive sync or automatic background agents.

### Phase I — Mathematical research (Mentor + Scientist)

Investigate mathematical formulation, oracle, tensor/batch structure, complexity, stability, JVP/VJP and sequential dependencies. Produce the existing `docs/research/<algorithm>-tensorization.md` mathematical study. Scientist reviews it. Transition to Phase II only on **RESEARCH_READY**. `RESEARCH_BLOCKED` returns to research; `NOT_TENSORIZABLE` may lead to a reasoned no-go or explicitly approved non-tensor approach.

### Phase II — CPU engineering and validation (Architect + Codex)

Architect specifies interfaces, numerical tolerances, performance methodology, packaging and the three-step Colab contract. Codex implements standalone, pip-installable Python modules and **runs real CPU tests**: reference/oracle comparison, randomized/edge tests, dtype/shape behavior, CPU eager execution, CPU `torch.compile` (where supported), optional `fullgraph=True` diagnostics, graph breaks, CPU benchmark, clean pip install and CLI smoke test. Record actual outputs, environment and tested source SHA in `docs/engineering/<algorithm>-engineering.md`. **CPU compilation does not prove GPU compilation or speedup.**

Codex completes [GPU Readiness](../templates/GPU_READINESS.md). Architect reviews evidence and labels **GPU_READY** only when required gates pass. A test that could not run must be marked **NOT_RUN**, never PASS. No need to invoke Scientist for every CPU iteration.

### Gate — GPU readiness

Required: Scientist-approved math study; real CPU correctness tests; CPU `torch.compile` evidence or explicit justified waiver; pip-installed packaged benchmark CLI; reproducible workload/preset; accurate source SHA; GPU device, error handling and report schema designed; minimal Notebook commands prepared. GPU Readiness is an **engineering readiness claim**, **not** a GPU-tested claim. Any waiver requires reason and Architect approval. Unmet criteria mean **CPU_BLOCKED** and a Codex Issue.

### Phase III — GPU experiment and performance engineering (Scientist + Architect + Codex)

Scientist batches **GPU_READY** projects into a manual GitHub Issue-based queue and runs real Colab experiments at a convenient time. Target Notebook: **pinned SHA install → packaged benchmark → optional separate publish**; see [Three-Step Contract](COLAB_TWO_COMMAND.md). **Until the CLI/Publisher is implemented and verified, use an honest manual fallback.** Validate GPU accuracy before timing; record device, compiler backend, synchronization, warmup, repetitions, compiled/eager timings, tested SHA and raw results. Preserve unique run IDs and link the existing Experimental Report.

If GPU reveals numerical/compilation issues, return to Phase II with a reproducible Issue; if a mathematical premise fails, return to Phase I. Do not ask Scientist to repeat GPU runs before the local reproducible problem is fixed. After verified measurements, record **GPU_VERIFIED**; it is not synonymous with a speedup.

## Resume and handoff

Restore role/project/permissions from the pinned [Role Recovery](ROLE_RECOVERY.md); complete one scoped cycle and recommend the [Next Action](NEXT_ACTION.md). Do not infer access to local CPUs, Colab or background jobs.

## Evidence and status

Statuses: `RESEARCH_READY`, `RESEARCH_BLOCKED`, `CPU_IN_PROGRESS`, `CPU_BLOCKED`, `CPU_VALIDATED`, `GPU_READY`, `GPU_IN_PROGRESS`, `GPU_VERIFIED`, `GPU_BLOCKED`. Keep the canonical status in an Issue/PR, with links to the three existing artifacts. A GPU queue needs only GitHub Issues/labels; do not build queue software.

## Acceptance and compatibility

- The Architect must verify source SHA, actual CPU outputs and GPU Readiness before inviting the Scientist to Colab.
- Existing mathematical, engineering and experimental templates remain authoritative; GPU Readiness is a small **gate record**, not a fourth long research report.
- Project adoption requires a **pinned SAE framework version** containing this protocol; existing projects do not silently upgrade.
- No unreviewed direct pushes of experiment results to main; an optional Publisher may create a report PR only, subject to Scientist review.
