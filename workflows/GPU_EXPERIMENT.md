# GPU Experiment and Evidence Protocol

> English (normative) | [简体中文](../i18n/zh-CN/workflows/GPU_EXPERIMENT.md)

**Owner:** Human Scientist runs actual Colab GPU experiments after Architect has reviewed `GPU_READY`. The Engineer owns packaged numerical and benchmark code; Architect defines workloads, oracle, error tolerances and interpretation. Mathematics and CPU test evidence must come first; see [Research Pipeline](RESEARCH_PIPELINE.md).

## Operation

Colab has three separate notebook cells: pinned-SHA package install, benchmark, **optional report upload after Scientist inspection**. **The sole command, Secret-handling and Publisher CLI specification is the [Three-Step Colab Contract](COLAB_TWO_COMMAND.md)**. Do not duplicate its commands or implement numerical loops/API calls in Notebook. The `GITHUB_TOKEN` Secret belongs to Scientist, and the benchmark does not require it.

## Four compact report files

- `manifest.json`: immutable *tested source* commit SHA, run ID/UTC, Issue/PR, package and environment versions, device, seed/dtype, full commands and status.
- `correctness.json`: mathematical oracle, tolerances, errors/mismatches, PASS/FAIL/NOT_RUN.
- `benchmark.csv`: comparable workloads, dtype, device, warmup, synchronization, compilation overhead, repetitions, units and timing distribution (e.g. median/p95).
- `summary.md`: actual observations, limitations, numerical verdict, speedup basis if justified, and linked PR/Issue.

Never upload huge arrays, models, logs, secrets or private datasets. Compare identical problems at equivalent correctness; `GPU_VERIFIED` means real GPU correctness/measurement evidence, **not necessarily a speedup**.

## Publication / PR

Scientist **separately authorizes an upload** by executing the Publisher against an already inspected run directory. Publisher validates schema/source SHA, sanitizes payload, creates a new `experiment/<run-id>` branch from a known base with immutable reports, opens a PR and returns the verified GitHub link. It may not overwrite, force-push, merge or rerun GPU. A report PR and a code PR can be reviewed independently. Public/draft PRs are public; the Scientist reviews report content before publication.

## Failures and feedback

A failing oracle invalidates an acceleration PASS and should be linked to a reproducible Issue. A mismatched tested SHA does not validate the candidate code PR. Unavailable GPU is `NOT_RUN`; publication failure is `PUBLISH_FAILED` with local artifacts preserved. Architect reviews actual evidence and dispatches CPU/algorithm fixes to Codex before another Scientist GPU run. Numerical or mathematical contradictions return to the [mathematical research gate](MATHEMATICAL_RESEARCH.md).

No Github Actions, no Drive report sync, no fabricated benchmarking or automatic background publishing.
