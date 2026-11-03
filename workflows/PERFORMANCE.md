# Performance Patch — Triton after `torch.compile` (V3.4)

> English normative | [简体中文](../i18n/zh-CN/workflows/PERFORMANCE.md)

An optional maintenance phase for any PyTorch project. It speeds up **only** the hotspots that remain slow after `torch.compile`, with a small hand-written GPU kernel added as a **patch**, never as a rewrite. "No gain" is a valid, recorded result.

## When to start
All three must hold:
1. **Stable code.** The feature is merged and stable, usually at the end of a milestone. Never during active feature work.
2. **A measured hotspot.** A `torch.profiler` run on the target GPU, at the exact SHA and a realistic size, names the op or region and its share of end-to-end time.
3. **Compile was tried first.** The region was run under `torch.compile` (default and `max-autotune`) and is still a hotspot.

The Architect then dispatches **one Issue per op**, in `VALIDATE` mode ([Tasks](TASKS.md)), usually size `M`. If the speedup needs a new formulation of the algorithm rather than a faster kernel for the same one, it goes through [Research](RESEARCH.md) first.

## Patch rules
- **The PyTorch implementation stays.** It is the oracle and the fallback. The kernel is a fast path chosen inside the existing public function, when the device is CUDA and Triton is importable; otherwise the PyTorch path runs.
- **Triton is an optional dependency** (e.g. a `[triton]` extra). CPU, Mac and no-GPU users see no change.
- **One op per patch, same signature.** No caller changes.
- **Triton first.** CUDA C++ only when the Issue names why Triton is insufficient.
- Register the kernel through `torch.library` (e.g. `triton_op`) only when it must compose with `torch.compile` or autograd. If the op needs gradients, the patch either provides a backward or is limited to the no-grad path, as the Issue says.

## Acceptance (fixed in the Issue; the Engineer does not change it)
1. **Oracle.** Matches the PyTorch reference on random inputs at a small and a realistic size, in each shipped dtype, within the Issue's tolerance. *Named risk for one extra size:* kernels fail at sizes that are not a multiple of the block size, so include one such size.
2. **Benchmark.** One project benchmark script, written or approved by the Architect: warmup, CUDA synchronization (or `triton.testing.do_bench`), median of repeated runs, at least three sizes, observed GPU name. **The baseline is the `torch.compile`d PyTorch path**, not eager, at the same dtype and accuracy. Compile time is reported separately.
3. **Threshold.** End-to-end speedup **≥ 1.3×** on the profiled workload on at least one target GPU, and no tested size slower than the baseline. If some sizes are slower, the public function dispatches by size, or the patch is not merged.

Evidence stays within the [Compute caps](COMPUTE.md#evidence).

## Record every attempt
Append one line to the project's `docs/performance.md`, whether or not the patch merged:

`date · op · GPU · compiled baseline → patch (median) · ACCEPTED / NO_GAIN · PR`

A `NO_GAIN` op is not retried unless the GPU generation, the PyTorch/Triton version or the algorithm changes materially.
