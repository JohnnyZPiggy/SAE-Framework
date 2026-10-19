# [SAE Engineering Task] <short title>

> Language: **English** | [简体中文](../i18n/zh-CN/templates/ISSUE_TEMPLATE.md)


**Owner:** Codex / Architect / Scientist
**Priority:** P0 / P1 / P2
**Status:** ready / in-progress / review / experiment / blocked / accepted
**Kind:** math / engineering / experiment / learning
**Depends on:** #<issue-number> (or none)

## Scientific purpose
What problem does this solve, and why does it matter?

## Pre-engineering mathematical research gate
**Approved structure/tensorization study:** `docs/research/<algorithm>-tensorization.md` / link  
**Scientist decision:** RESEARCH_READY / approved narrow exception  
**Matrix-vector / tensor structure and limitations:** <summary>  
*Repository scaffolding-only issues can mark this as not applicable.*

## Mathematical / numerical contract
Definitions, assumptions, reference baseline, invariants, input/output shapes, dtype/device constraints, tolerance policy.

## Deliverables
- [ ] Scoped Python modules, CLI or design artifact
- [ ] Tests/benchmark source
- [ ] Documentation and reproduction commands

## Colab delivery gate (algorithm tasks)
- [ ] Exact pinned-SHA pip install and independent packaged benchmark CLI
- [ ] Independent optional Publisher CLI accepts existing run directory, never reruns GPU
- [ ] Codex ran actual CPU numerical, package/CLI and Publisher mock tests
- [ ] Scientist GPU experiment and optional upload: **NOT_RUN** until actually observed
- [ ] Source SHA, failure modes and secret `GITHUB_TOKEN` access validated (no plain tokens)

## Acceptance criteria
- [ ] Spec and reference baseline agree
- [ ] Correctness/edge-case checks specified
- [ ] Actual CPU validation recorded
- [ ] If GPU-relevant, exact candidate SHA tested in Colab
- [ ] No GitHub Actions and no secret leakage

## Handoff
Target branch, linked PR/report, open questions, known blockers.
