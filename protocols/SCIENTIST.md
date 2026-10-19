# Human Scientist — Owner and Research Decision-Maker

> [中文](../i18n/zh-CN/protocols/SCIENTIST.md)

The Scientist owns the research question, assumptions, mathematical acceptance, personal GPU execution and important governance/security/publication choices; GPT and Codex provide technical work and evidence.

## Required decisions and actions

1. For every new algorithm or major tensorization redesign, discuss mathematical operators, numerical risks and potential CPU/GPU mapping with Mentor. Review [the mathematical study](../workflows/MATHEMATICAL_RESEARCH.md); choose `RESEARCH_READY`, `RESEARCH_BLOCKED`, `NOT_TENSORIZABLE` or a documented narrow exception.
2. Ask Architect to specify reusable tools, interfaces and numerical acceptance; Codex must run actual CPU tests and pinned package/CLI smoke checks. Do not accept CPU compile results as GPU evidence.
3. Only after Architect `GPU_READY`, select a Colab device, install the **exact candidate commit**, run the independent benchmark and inspect `manifest.json`, `correctness.json`, `benchmark.csv` and `summary.md`. Compare errors and times against documented baselines; record runtime and failure evidence.
4. **Optionally** publish only the reviewed, sanitized GPU report through a separate Publisher step using the Colab Secret named `GITHUB_TOKEN`. This is a deliberate public-data decision; the benchmark itself does not publish or require the Secret. See [GPU Experiment](../workflows/GPU_EXPERIMENT.md).
5. Approve substantive scientific decisions, material security/governance/licensing changes or destructive/public disclosures when needed; **do not repeat a technical merge approval** once such prerequisites are satisfied. GPT Architect independently reviews/merges qualifying PRs under the [indefinite owner-public Standing Authorization](../governance/STANDING_AUTHORIZATION.md); the Scientist can revoke it at any time.

No obligation to implement heavy Python modules, manage GitHub Actions or synchronize Drive with GitHub. Maintain the [three connected research artifacts](../workflows/THREE_ARTIFACT_HANDOFF.md) and use [Role Recovery / Next Action](../workflows/ROLE_RECOVERY.md) to resume.
