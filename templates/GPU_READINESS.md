# GPU Readiness Gate — <algorithm>

> English | [简体中文](../i18n/zh-CN/templates/GPU_READINESS.md)

**Project / Issue:** <URL>  
**Source commit tested:** <FULL_SHA>  
**Reviewer:** GPT Architect  
**Decision:** CPU_BLOCKED / GPU_READY  
**GPU experiments:** NOT_RUN (until real Colab execution)

| Gate | Status: PASS / FAIL / NOT_RUN / WAIVED | Evidence (command, real output, link) |
| --- | --- | --- |
| Scientist-reviewed mathematical research | | |
| CPU oracle, randomized and edge correctness | | |
| CPU eager + `torch.compile` execution | | |
| CPU fullgraph/graph-break diagnostics if relevant | | |
| CPU benchmark and numerical tolerance | | |
| Clean pinned-SHA pip install and packaged CLI | | |
| GPU workload defaults, device failure and report design | | |
| Codex-operated Colab CLI plan, three separate stages and source SHA | | |

**Waivers (reason + Architect approval):** <none or detail>  
**Outstanding blockers:** <none or Issue URLs>  
**GPU queue Issue:** <URL or NOT_QUEUED>  
**Decision evidence:** <short justification>

Do not set GPU_READY if any mandatory gate failed or was not run without an approved waiver. **GPU_READY does not assert GPU correctness, GPU compilation or speedup.** The actual GPU run and its experimental report are separate.
