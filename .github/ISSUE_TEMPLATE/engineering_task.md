---
name: SAE engineering task
about: Delegable mathematical or PyTorch engineering work
title: "[SAE] "
labels: []
assignees: []
---

<!-- Apply labels manually if available: agent:codex, status:ready, kind:engineering, priority:p1 -->

**Scientist objective:**

**Pre-engineering tensorization study link and status (RESEARCH_READY / explicit exception / N/A for scaffolding):**

**Mathematical/numerical contract:**

**Inputs/outputs and precision:**

**Deliverables:**

**Acceptance tests (actual evidence required):**

**Colab three-step contract (algorithm tasks):** pinned GitHub SHA install → standalone packaged `benchmarks.run --device cuda --out reports/gpu/RUN_ID` → **optional separate** `benchmarks.publish --report-dir reports/gpu/RUN_ID` after Scientist inspects results. Benchmark does not publish; Publisher uses Colab Secret `GITHUB_TOKEN` with verified secure subprocess access. Codex runs real CPU oracle, packaging and CLI tests; Scientist GPU/upload is NOT_RUN until observed.

**Candidate GPU experiment (if needed):**

**Dependencies / blockers:**
