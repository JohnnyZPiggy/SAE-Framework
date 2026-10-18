# Thin Colab Notebook — illustrative cell plan

> Language: **English** | [简体中文](../../i18n/zh-CN/examples/colab/README.md)


**This directory is documentation, not a working notebook or Publisher.** GPT designs orchestration; Codex implements tested Python modules/CLI. The Scientist runs Colab and reviews results.

**After one-time GPU runtime selection and optional Colab Secrets authorization, the core notebook has only two executable cells:**

```python
!pip install "git+https://github.com/OWNER/REPO.git@<COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --publish
```

The first cell installs a pinned source SHA via pip. The second uses a **packaged benchmark Python module** to perform device checks, numerical correctness, synchronized benchmark, report generation and optional GitHub PR publication. Real repository, SHA, import path, presets and CLI contract are supplied by GPT Architect **after Codex implements and tests them**.

No third executable Notebook cell is required by the **target design**. `--publish` is an explicit per-run request to create a validated report PR (not auto-merge). Until Publisher exists and has passed integration tests, that portion remains **manual**; don't claim publication from running illustrative commands. Details and acceptance: [two-command contract](../../workflows/COLAB_TWO_COMMAND.md).

The notebook should **not** contain numerical kernels, benchmark loops, direct git credential logic, token literals, temporary Drive sync, or invented results. The CLI may securely access pre-authorized Colab Secrets only after this path has been tested from a Python subprocess. Keep the Google Drive folder small and unsynchronized.
