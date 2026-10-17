# Colab GPU 实验与 GitHub 结果发布协议

> 语言：[English](../../../workflows/GPU_EXPERIMENT.md) | **简体中文**

## 职责分工
- **GPT / Architect：** 明确实验问题、参数矩阵、验收条件，设计薄 Notebook 调度。
- **Codex / Engineer：** 实现并验证算法、测试 CLI、Benchmark CLI 和未来的 Publisher。
- **Scientist：** 配置 Colab/私人的轻量 Drive 工作空间、GPU 和认证；亲自运行并审查结果。
- **GitHub：** 持久保存经过复核的小型实验报告，让 GPT、Codex 可以直接读取。

**Drive 不是结果传输层。** Drive 只存 Notebook 或临时文件，实验共享由 GitHub PR 完成。

## 薄 Notebook 四阶段
1. **准备：** 选择 CPU/GPU，安装指定 PR 对应的**精确源码 SHA**，检查环境与驱动/PyTorch/CUDA。
2. **设参：** 选择 workload、dtype、容差、参考基线、种子、重复次数和独立 run ID。
3. **执行：** 调用经 Codex 测试的 Python CLI，例如 `python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>`；先看正确性，再分析速度。示例命令的包名**不是已实现接口**。
4. **发布：** 验证后调用 Publisher，例如 `python -m <package>.tools.publish_results --run-dir reports/gpu/<run-id> --issue <N>`。**未开发与测试之前这只是接口契约。**

## 必须保存的轻量证据
- `manifest.json`：run ID、UTC 时间、**被测源码 SHA**、关联 Issue/PR、设备与软件版本、随机种子、精度、完整命令、计时方法和执行状态。
- `correctness.json`：参考基线、误差、容差、失败数、通过/失败/未运行状态。
- `benchmark.csv`：设备、方法、规模、dtype、重复次数、计时单位、median/p95、编译成本和加速比的比较依据。
- `summary.md`：真实结论、失败、局限及 Issue/PR 链接。
- 小图片可以入库；大张量、权重、冗长原始日志及任何秘密都不应公开提交。

## GitHub 发布流程
1. 科学家先确认实验输出；Publisher 核验 schema、密钥和文件大小。
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