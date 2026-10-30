# Run Summary — <run-id>

> Language: **English** | [简体中文](../i18n/zh-CN/templates/EXPERIMENT_REPORT.md)
> Save as `reports/<run-id>/summary.md` in the algorithm project, next to one results file. Evidence caps: [Simplicity Contract §3](../governance/SIMPLICITY_CONTRACT.md#3-evidence-git-is-the-integrity-layer).

**Issue / PR:** #<n> / #<n> · **Source SHA:** `<40-hex>` · **Status:** PASS / FAIL / NOT RUN / BLOCKED

## Setup
Observed device (name, memory, capability); driver / CUDA / PyTorch versions in one line; dtype; seed; command.

## Correctness
Reference, tolerance, max abs / rel error, failure count.

## Timing (only if speed is claimed)
Sizes, warmup, synchronization, repetitions, median (and p95 if relevant), compile time, same-accuracy baseline.

## Results
| Config | Metric | Value |
|---|---|---|
| | | |

Full numbers: `results.json` / `results.csv`.

## Failures and cleanup
- `attempt — cause — fix` (or "none")
- Cleanup: assignments before → after, `cleanup_confirmed`.
