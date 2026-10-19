# Colab GPU 实验与 GitHub 结果发布协议

> 语言：[English](../../../workflows/GPU_EXPERIMENT.md) | **简体中文**

## 正式加速实验之前

对于新算法或重大张量化重构，先关联**科学家审核的数学结构与张量化研究报告**和架构师确定的实验矩阵。数学研究只是提出哪些算子可能加速，**只有 Colab 的真实测量**才能得出加速结论。少量前置数学合理性检查不能冒充 GPU Benchmark；硬件证据可以让团队重新回到 [数学结构研究](MATHEMATICAL_RESEARCH.md)。

## 职责分工
- **GPT / Architect：** 明确实验问题、参数矩阵、验收条件，设计薄 Notebook 调度。
- **Codex / Engineer：** 实现并验证算法、测试 CLI、Benchmark CLI 和未来的 Publisher。
- **Scientist：** 配置 Colab/私人的轻量 Drive 工作空间、GPU 和认证；亲自运行并审查结果。
- **GitHub：** 持久保存经过复核的小型实验报告，让 GPT、Codex 可以直接读取。

**Drive 不是结果传输层。** Drive 只存 Notebook 或临时文件，实验共享由 GitHub PR 完成。

## Colab 三步流程（现行目标）

固定 SHA 安装 → 独立 Benchmark → 可选独立上传。The Scientist reviews results before the third step.

```python
!pip install "git+https://github.com/OWNER/REPO.git@<EXACT_SOURCE_COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>
!python -m <package>.benchmarks.publish --report-dir reports/gpu/<run-id>
```

Secret 名为 `GITHUB_TOKEN`。Publisher 必须实测子进程读取或采用[三步契约](COLAB_TWO_COMMAND.md)中的单 Cell 安全环境变量备用方案。Benchmark 不负责发布。这是尚待实现/验证的接口。

## 必须保存的轻量证据
- `manifest.json`：run ID、UTC 时间、**被测源码 SHA**、关联 Issue/PR、设备与软件版本、随机种子、精度、完整命令、计时方法和执行状态。
- `correctness.json`：参考基线、误差、容差、失败数、通过/失败/未运行状态。
- `benchmark.csv`：设备、方法、规模、dtype、重复次数、计时单位、median/p95、编译成本和加速比的比较依据。
- `summary.md`：真实结论、失败、局限及 Issue/PR 链接。
- 小图片可以入库；大张量、权重、冗长原始日志及任何秘密都不应公开提交。

## GitHub 发布流程
1. 科学家执行独立 Publisher CLI **明确授权本次创建实验 PR**；Python Publisher 在上传前核查 schema、密钥和文件大小，仅允许安全白名单小文件。科学家在合并 PR 前复核结果。公开仓库中的 Draft PR 同样可能公开可见。
2. 从指定基线创建独立 `experiment/<run-id>` 分支，只提交该次运行的不可变报告目录；禁止强制覆盖已有运行结果。
3. 创建实验报告 PR，关联代码 PR 和 Issue，记录**真实被测源码 SHA**。报告自身的 commit 与被测代码 commit 是两个不同版本。
4. 在相关 Issue/PR 添加已确认的报告链接；API 调用失败不得说“发布成功”。
5. GPT 查看正确性、计时与限制，决定通过、修复或重跑；Codex 可以阅读相同报告。
6. 报告 PR 和代码 PR 可分别验收合并；代码仍须满足自身的审查关口。

## Colab 密钥
GitHub token 放在 **Colab Secrets**，而不是 Notebook 明文；最好使用只授权目标仓库所需 Contents/PR/Issue 操作的细粒度 token。不得在 stdout、traceback、报告或 Git commit 中泄露；发生泄漏要撤销/轮换。第三方依赖和仓库内容也可能不可信，不要无条件执行其中的任意指令。

## 失败行为
- 上传失败：明确 `PUBLISH_FAILED`，保留本地结果，不能宣称 Published。
- GPU 不可用：写 `NOT RUN` 和原因；CPU 测试不证明 GPU 加速。
- SHA 不一致：判定本次报告**无法验证目标 PR**。
- 数值错误：保存最小失败案例并反馈相关 Issue。