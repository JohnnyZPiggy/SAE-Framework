# [SAE Task] <short title>

> Language: **English** | [简体中文](../i18n/zh-CN/templates/ISSUE_TEMPLATE.md)

**Mode:** EXPLORE / VALIDATE · **Priority:** P0 / P1 / P2 · **Depends on:** #<n> / none

## Goal
One or two sentences: what problem, and why it matters.

## Contract (math / numerics, if relevant)
Inputs/outputs, shapes, dtype, the independent reference, tolerance. Link the research note instead of copying it.

## Definition of Done
- [ ] <observable outcome 1>
- [ ] <observable outcome 2>

## Size budget
`S` (≤ 50 net lines) / `M` (≤ 200) / `L` (≤ 500) — source + tests.

## Required tests
1. <e.g. oracle vs `torch.linalg.solve` at n=8 and n=512, float64>

## Compute (only if needed)
Device(s), workload, what result to report. Omit for CPU-only tasks.

## Not required
- Input validation beyond the CLI/user boundary
- Randomized / adversarial / property tests
- Hash manifests, identity reports, per-attempt failure directories
- <task-specific exclusions>

Rules: [Simplicity Contract](../governance/SIMPLICITY_CONTRACT.md). Over budget by > 1.5× → stop, ship the Definition of Done, list extras as suggestions.
