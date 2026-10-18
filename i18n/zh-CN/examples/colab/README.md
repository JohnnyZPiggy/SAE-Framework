# 薄 Colab Notebook 示例说明

> 语言：[English](../../../../examples/colab/README.md) | **简体中文**

**这里只说明四个 cell 的设计，并不是可执行的 Notebook 或已经实现的 Publisher。** GPT 负责 Notebook 调度设计，Codex 负责可测试 Python 模块/CLI，科学家在 Colab 真实运行。

首次选择 Colab GPU runtime、按需配置 Colab Secrets 授权后，**核心 Notebook 只有两个可执行 Cell**：

```python
!pip install "git+https://github.com/OWNER/REPO.git@<COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --publish
```

第一行通过 pip 安装固定源码 SHA 的算法包，第二行调用**已经打包的 Benchmark Python 模块**，在内部完成设备检查、数学正确性、GPU 同步计时、报告生成及获得明确授权后的 GitHub PR 上传。真实仓库、源码 SHA、包名和 CLI 由 GPT 设计、Codex 实现与测试。无需额外参数或发布 Cell。

这是**最终目标接口**，不是已经实现的命令；Publisher 完成前上传仍为手动。详见 [双命令执行契约](../../../../workflows/COLAB_TWO_COMMAND.md)。

不要在 Notebook 中放数值 kernel、完整计时循环、Git API 凭证处理、明文 token 或虚构结果。Colab Secrets 的读取必须由 Codex 在真实子进程环境中验证，不能仅因为 Notebook Cell 能读取就假设 CLI 也能读取。Google Drive 只使用一个无需同步的轻量工作目录。