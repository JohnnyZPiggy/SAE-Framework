# 薄 Colab 示例：三 Cell 接口

> [English](../../../../examples/colab/README.md) | 简体中文

**这里只说明目标接口**，不代表 Benchmark/Publisher 已实现或 GPU 已跑。实际运行时填写准确仓库、固定 SHA、包名和 run ID。

```python
!pip install "git+https://github.com/OWNER/REPO.git@EXACT_SOURCE_COMMIT_SHA"
!python -m PACKAGE_NAME.benchmarks.run --device cuda --out reports/gpu/RUN_ID
!python -m PACKAGE_NAME.benchmarks.publish --report-dir reports/gpu/RUN_ID
```

科学家先运行安装与 Benchmark、检查真实数值/性能，再**可选执行第三个上传 Cell**。Benchmark 不上传、不需要 GitHub Token；Publisher 从 Colab Secret `GITHUB_TOKEN` 安全读取凭证。`!python` 子进程**不保证自动继承 Secret**，实测未通过时用 [正式三步契约](../../../../workflows/COLAB_TWO_COMMAND.md)中的单 Cell `subprocess.run` 备用方案，不显示 Token。Notebook 只调度，数值和上传实现由 Codex 打包测试。
