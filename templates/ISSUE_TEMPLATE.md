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

## Colab delivery gate (algorithm implementation tasks)
- [ ] Clean environment can `pip install` package from a pinned exact GitHub commit SHA
- [ ] Packaged `python -m <package>.benchmarks.run --device cuda --publish` CLI exists with tested defaults and no notebook-side engineering
- [ ] Codex actually ran CPU packaging, CLI and numerical smoke tests
- [ ] Scientist Colab GPU run and PR publication: **NOT RUN** until actual verification (Publisher may be manual until implemented)
- [ ] Include real CLI output / test SHA and explicit failures, not assumed success

## Acceptance criteria
- [ ] Spec and reference baseline agree
- [ ] Correctness/edge-case checks specified
- [ ] Actual CPU validation recorded
- [ ] If GPU-relevant, exact candidate SHA tested in Colab
- [ ] No GitHub Actions and no secret leakage

## Handoff
Target branch, linked PR/report, open questions, known blockers.
