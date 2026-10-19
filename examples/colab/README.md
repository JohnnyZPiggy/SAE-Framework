# Thin Colab — Three-Cell Interface Example

> English | [简体中文](../../i18n/zh-CN/examples/colab/README.md)

**Illustrative target only**; these are not implemented benchmark/Publisher modules and do not prove a Colab run occurred. Fill in the actual project/repo/package/run ID.

```python
!pip install "git+https://github.com/OWNER/REPO.git@EXACT_SOURCE_COMMIT_SHA"
!python -m PACKAGE_NAME.benchmarks.run --device cuda --out reports/gpu/RUN_ID
!python -m PACKAGE_NAME.benchmarks.publish --report-dir reports/gpu/RUN_ID
```

The Scientist executes cell 1 and 2; after checking numerical results, **optionally** executes cell 3. Benchmark does **not** upload or need GitHub access. The Publisher uses a Colab Secret called `GITHUB_TOKEN`, and a `!python` subprocess **may not inherit the Secret**. Use the one-cell safe Python `subprocess.run` fallback from the [authoritative contract](../../workflows/COLAB_TWO_COMMAND.md) until subprocess Secret retrieval is verified. Never print or paste the token. Notebook remains thin; Codex implements real CLI packages, numerical tests and Publisher separately.
