# Human Scientist — SAE V3.2

> English (normative) | [简体中文](../i18n/zh-CN/protocols/SCIENTIST.md)

**Owner:** Human Scientist chooses research direction, decides mathematical assumptions and tradeoffs, operates actual Colab, and retains substantive scientific/security/licensing/permission decisions. GPT's independent PR merge discretion is defined only by [Standing Authorization](../governance/STANDING_AUTHORIZATION.md), not by this file.

## One research cycle

1. Pick the scientific question; challenge the Mentor's [mathematical study](../workflows/MATHEMATICAL_RESEARCH.md); decide `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`, or approve a documented narrow reference-only exception.
2. Allow Architect/Codex to conduct an independent CPU-first engineering cycle, review actual numerical baselines, and only proceed to Colab after Architect approves [GPU Readiness](../templates/GPU_READINESS.md).
3. Run the [three-step Colab workflow](../workflows/COLAB_TWO_COMMAND.md): **exact SHA install → GPU correctness/benchmark → optional separate report upload** after inspecting the results. Colab Secret name is `GITHUB_TOKEN`; do not print or commit it.
4. Inspect candidate code SHA, device, dtype/seed, error metrics, warmups, synchronized timing and limitations. Create/inspect `manifest.json`, `correctness.json`, `benchmark.csv` and `summary.md` from **real data**; link them to mathematical/engineering evidence using [Three-Artifacts](../workflows/THREE_ARTIFACT_HANDOFF.md).
5. If Publisher is not implemented/tested, keep `PUBLISH_NOT_RUN` and use only deliberately authorized safe manual report publication; no Drive synchronization. Share actual Issue/PR links and request Architect review.

The Scientist need not implement heavy Python/CLI personally. Codex cannot self-merge; the Architect decides eligible PR merges after reviewing real evidence. A substantive scientific/governance/security decision cannot be inferred from a merge authorization. No automatic background experimentation.
