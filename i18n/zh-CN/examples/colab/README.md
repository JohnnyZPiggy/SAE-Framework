# 薄 Colab Notebook 示例说明

> 语言：[English](../../../../examples/colab/README.md) | **简体中文**

**这里只说明四个 cell 的设计，并不是可执行的 Notebook 或已经实现的 Publisher。** GPT 负责 Notebook 调度设计，Codex 负责可测试 Python 模块/CLI，科学家在 Colab 真实运行。

1. **Cell 1 环境：** 连接 runtime、选择 CPU/GPU、安装**指定 commit SHA**（也可指定 PR head），记录 PyTorch/CUDA/GPU。
2. **Cell 2 参数：** dtype、种子、规模、基线、容差、run ID、输出目录。
3. **Cell 3 实验：** 通过 `--device cpu|cuda` 调用经测试的项目专属 Python CLI；先核验数学正确性，再测性能。
4. **Cell 4 发布：** 从 Colab Secrets 读取 GitHub 凭证，调用测试过的 Publisher 创建报告分支/PR，获得验证过的 URL。

不要在 Notebook 中放数值 kernel、完整计时循环、Git API 凭证处理或虚构结果。Google Drive 只使用一个无需同步的轻量工作目录。