# Thin Colab Notebook — illustrative cell plan

> Language: **English** | [简体中文](../../i18n/zh-CN/examples/colab/README.md)


**This directory is documentation, not a working notebook or Publisher.** GPT designs orchestration; Codex implements tested Python modules/CLI. The Scientist runs Colab and reviews results.

1. **Cell 1 — Setup:** connect runtime, choose CPU/GPU, install **exact source commit SHA** (including PR head if testing before merge), inspect PyTorch/CUDA/GPU.
2. **Cell 2 — Parameters:** dtype, seed, size, baseline, tolerance, run ID and output directory.
3. **Cell 3 — Experiment:** invoke tested project-specific Python CLI with `--device cpu|cuda`; inspect correctness first; then benchmark.
4. **Cell 4 — Publish:** retrieve GitHub credential securely from Colab Secrets and invoke tested Publisher CLI to create a report branch/PR; capture verified link.

The notebook should **not** contain numerical kernels, benchmark loops, direct git credential logic or invented results. Keep the Google Drive folder small and unsynchronized.
