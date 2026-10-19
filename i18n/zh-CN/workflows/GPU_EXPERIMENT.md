# GPU 实验与证据协议

> [English](../../../workflows/GPU_EXPERIMENT.md)（正式规范） | 简体中文

**执行者：** 科学家在架构师审核 `GPU_READY` 后，亲自运行 Colab GPU 实验。Codex 提供可安装的数值与 Benchmark 模块，架构师定义 workload、数学 oracle 和容差。数学和 CPU 关口见 [三阶段流程](RESEARCH_PIPELINE.md)。

## 操作

Colab 使用三个独立 Cell：固定 SHA 安装、Benchmark、**科学家审核后可选上传**。唯一的命令、Secret 与 Publisher 说明位于 [三步契约](COLAB_TWO_COMMAND.md)，这里不重复。Notebook 不放计算循环或 GitHub API；`GITHUB_TOKEN` 由科学家保管，Benchmark 无需 Token。

## 四个轻量报告文件

- `manifest.json`：真实**被测源码 SHA**、run ID/UTC、Issue/PR、软件/设备版本、seed/dtype、完整命令和状态；
- `correctness.json`：数学参考基线、容差、误差与 PASS/FAIL/NOT_RUN；
- `benchmark.csv`：等价工作规模、设备、dtype、预热/同步、编译开销、重复次数、单位与 median/p95；
- `summary.md`：真实结果、局限、数值判断、合理时加速比依据和链接。

不上传大型张量/模型/日志、密钥或隐私数据。`GPU_VERIFIED` 只表示 GPU 真实测量/正确性证据，**不代表必然加速**。

## 发布与 PR

科学家检查报告后，通过独立 Publisher 操作**授权该次上传**。Publisher 校验格式和 SHA，清理风险，从指定分支创建不可变 `experiment/<run-id>` 报告分支与 PR，核实 GitHub 链接；**不重跑 GPU、不覆盖、不强推、不直接合并**。报告 PR 和代码 PR 分别验收。公开仓库的 Draft PR 也是公开资料，科学家上传前必须审核内容。

## 失败与反馈

数值失败不得声称加速通过，创建可复现 Issue；SHA 不匹配不能验证代码 PR；GPU 不可用标 `NOT_RUN`；发布失败标 `PUBLISH_FAILED` 并保存本地报告。架构师在下一次 GPU 前先让 Codex 修复 CPU 能复现的问题；数学矛盾则回到 [数学研究](MATHEMATICAL_RESEARCH.md)。

不使用 GitHub Actions、Drive 报告同步或未经验证的后台上传。
