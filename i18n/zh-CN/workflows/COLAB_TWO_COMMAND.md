# Colab 双命令执行契约

> 语言：[English](../../../workflows/COLAB_TWO_COMMAND.md) | **简体中文**

## 最终目标：Notebook 只运行两条命令

在一次性选择好 Colab GPU runtime、配置好需要使用的 GitHub 凭证之后，每次实验**只运行两行**：

```python
!pip install "git+https://github.com/OWNER/REPO.git@<COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --publish
```

**这是待实现的统一接口契约，不表示现在已经能够执行。** GPT 必须填写真实仓库、不可变完整源码 SHA 和已经打包、验证的 Python 模块路径。`--publish` 表示科学家主动请求本次实验提交 GitHub 报告 PR，而非同意自动合并。若去掉该参数，Benchmark 只保存本地结果。

## 工程复杂度必须提前封装

**GPT 总架构师（先设计再派发）：**
- 规定统一的 `python -m <package>.benchmarks.run` CLI、`--device cpu|cuda`、`--publish` 以及无须单独参数 Cell 的默认 workload、dtype、seed、容差和测量方法。
- 指定参考正确性 oracle、数值误差上限、GPU 计时的同步与预热、`torch.compile` 成本披露、结构化实验输出和发布的安全范围。
- 为 Codex 派发能够独立验收的封装任务：干净 pip 安装后，单条 Python 命令完成**设备检查 → 数值测试 → 预热计时 → 生成报告 → 按授权上传 PR**。
- GPT 编写的 Colab Notebook 除两条命令 Cell 和极简文字外，不应有安装脚本、GPU 计算循环、直接 GitHub API 操作或额外参数 Cell。

**Codex 软件工程师（本地实现、验证）：**
- 正确配置 `pyproject.toml` 打包算法、Benchmark 模块及默认 presets，确保 **pip 安装后**可以直接运行 `python -m`；不得依赖 Git clone 后的工作目录、Drive 挂载或 Notebook `%cd`。
- 核心数学算子、参考算法、正确性验证、benchmark、实验报告、GitHub 发布器全部实现为可测试的 `.py` 模块；CLI 只负责串联。
- 默认参数可直接运行，高级配置以可选 `--dtype`、`--seed`、`--sizes`、`--preset`、`--out` 提供，不增加基本 Notebook 的命令行数。
- 能识别/记录 **真正 pip 安装的源码 SHA**（例如基于 pip VCS `direct_url.json`），并能发现 SHA 不匹配；不能将当前 `main` 或实验报告 commit 当作被测源码版本。
- 在本地真实执行 CPU 安装/正确性/CLI 测试，并 mock 测试无 GPU、错误 SHA、数值失败、GitHub 拒绝/上传重试/重复上传等；没有 GPU 的测试不能写成 Colab 成功。

**科学家（你）：**
- 首次使用 Colab 时选择 GPU runtime，按需在 Colab Secrets 中授权**最小权限**的 GitHub token。
- 运行两行命令；检查实际 GPU、误差、测速和**经过 GitHub 确认的 PR 链接**；最终是否合并由你决定。
- 不需要自己编写 GPU kernel、Benchmark、API 上传代码，也不需要通过 Drive 同步结果。

**GPT 科学导师** 负责用真实实验结果解释数值误差、算法瓶颈及硬件行为，并在必要时重新研究数学结构。

## 结果自动上传：有条件，不能假装成功

- `--publish` 至多自动创建实验分支、GitHub PR（支持时优先草稿 PR），**不会自动合并或直接推送 main**。公共仓库的草稿 PR 也可被外界看到，所以只允许上传经事先确定、安全检查过的小型报告文件。
- 发布模块应在**经过 Colab 子进程集成测试**的前提下从 Colab Secrets 中安全获取凭证，或使用安全注入的环境变量；不得要求 Notebook 明文写 token，也不得在日志打印它。
- Benchmark 状态与上传状态**分别报告**：如 `BENCHMARK_PASS / BENCHMARK_FAIL / NOT_RUN` 和 `PUBLISHED / PUBLISH_BLOCKED / PUBLISH_FAILED / NOT_REQUESTED`。只有 GitHub API 确认成功才显示 PUBLISHED 和有效 PR URL。
- 凭证或 Publisher 缺失时保留本地文件、明确 `PUBLISH_BLOCKED`；**目前 Publisher 尚待 Codex 实现**，自动上传依旧是目标，不是现有能力。
- GPU 不可用则不能偷偷转 CPU 并自称 GPU。数值正确性失败不得继续宣称速度优势；错误需要写入真实诊断文件并由程序返回失败。

## 实验文件

CLI 应自动保存 `reports/gpu/<run-id>/` 下的 `manifest.json`、`correctness.json`、`benchmark.csv` 和 `summary.md`，包含真正的源码 SHA、GPU/Python/PyTorch/CUDA、随机种子、dtype、参考误差、计时/编译方法、运行命令、对应 Issue/PR。不得上传私密数据、超大张量或凭证。

## 分级验收

1. **Codex 本地 CPU：** 能在干净环境安装指定 SHA 的 PyTorch 算法包，真正运行打包的 CLI，并完成关键失败分支/mock 发布测试。
2. **科学家真实 Colab GPU：** 从新 runtime 按两行指令运行指定源码 SHA，先验证精度，再同步、预热与测量。
3. **Publisher 完成后：** 在明确授权的 GitHub 连接下，`--publish` 无须额外 Notebook 命令即可提交并确认报告 PR。
4. **GPT 复核：** 核对实际安装 SHA、数学数值约束、测试与上传状态。不把“协议已经定义”说成“自动流程已经实现”。

参见 [GPU 实验协议](GPU_EXPERIMENT.md) 和 [Colab 示例](../../../examples/colab/README.md)。
