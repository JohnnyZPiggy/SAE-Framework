# Compute — CPU and GPU Experiments (V3.4)

> English normative | [简体中文](../i18n/zh-CN/workflows/COMPUTE.md)

## Policy: use the compute you have
- **GPU first** for suitable tensor work. Plan GPU runs from the start and keep a CPU oracle for correctness. CPU-only work is never blocked waiting on a GPU.
- **Experiment by default.** Within existing Colab entitlements the Engineer runs CPU and GPU work directly. No Scientist approval, price estimate or per-run budget is needed.
- **No SAE-imposed quotas.** Size runs by the research question: try every GPU type the account actually offers and retry after a fixable failure. A small probe is a starting point, not a ceiling.
- **Real limits still apply:** provider quotas and availability, finite timeouts, cleanup, and **no new spending** (purchases, top-ups, pay-as-you-go) without explicit user approval. If a run might create charges outside existing entitlements, stop and ask.

## Running an experiment
1. **Pin the source.** Run the exact committed 40-character SHA. Report local uncommitted work as such; never present it as a pinned result.
2. **Run with the controller** ([tools/compute](../tools/compute/README.md)). It does one session at a time and checks for zero active sessions and a positive balance before allocating. It records the **observed** device and always stops the session and confirms assignments = 0, on success, failure or Ctrl-C. A project-committed driver does the science. The run itself makes no GitHub writes.
3. **Hand off.** Results go to a PR in the algorithm project. The Architect reviews and merges.

Before the first live run of a session, `--preflight-only` checks the setup locally without allocating. `PROBE_ONLY` device checks may precede `RESEARCH_READY`; they show the device works, not that the algorithm is correct or fast. TPU / PyTorch-XLA is **not implemented** here; a listed TPU option proves nothing.

## Evidence
Within the [Simplicity Contract caps](../governance/SIMPLICITY_CONTRACT.md#3-evidence-git-is-the-integrity-layer): at most 10 files per run, usually two.
- `summary.md` ([template](../templates/EXPERIMENT_REPORT.md)): source SHA, Issue/PR, observed device, a one-line environment, command, seed and dtype, correctness against the reference with tolerance, timing method (warmup, sync, repetitions, median), failures as `attempt — cause — fix`, and the cleanup readback.
- One results file (`results.json` or `.csv`) holding only the numbers the summary cites.

SHA-256 only for bytes downloaded from outside Git. No speedup claim without an equivalent baseline at the same accuracy.

## Statuses
`PASS` · `FAIL` · `NOT RUN` (not attempted, or hardware untested) · `BLOCKED` (real access, quota or billing boundary; source mismatch) · `CLEANUP_FAILED` (release unconfirmed, which is never a pass).

## Workspace
Scratch, builds and caches go in the Scientist-designated workspace; Dropbox-synced D: roots are fine. Use one task directory and delete only what you created. The controller's own temporary export (`--temp-root`) must sit outside the checkout and outside Dropbox, and off C: when another drive is available. Google Drive is optional notebook scratch only, never a results channel. Colab secrets stay in Colab Secrets and are never echoed into logs.
