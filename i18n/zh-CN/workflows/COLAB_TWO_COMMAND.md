# Colab 三步契约：安装、Benchmark、可选上传

> [English 正式规范](../../../workflows/COLAB_TWO_COMMAND.md) | 简体中文

**兼容：** 历史路径 `COLAB_TWO_COMMAND.md` 暂不更改，以免旧链接和固定快照失效。**现行操作是三个独立 Cell，第三步可选**。以下是将由 Codex 实现和验证的目标 CLI，不能当作工具已可运行的证据。

## 科学家的三个 Cell（填写真实参数）

```python
!pip install "git+https://github.com/OWNER/REPO.git@EXACT_SOURCE_COMMIT_SHA"
!python -m PACKAGE_NAME.benchmarks.run --device cuda --out reports/gpu/RUN_ID
!python -m PACKAGE_NAME.benchmarks.publish --report-dir reports/gpu/RUN_ID
```

1. **安装：** 用不可变、准确的源码 SHA，不依赖漂移分支。
2. **Benchmark：** 检查源码与数值基线、运行设备、正确性和预热/同步计时，生成唯一目录的本地报告；**不要求 GitHub Token、不自动上传**。
3. **可选上传：** 科学家先阅读误差、测速与文件，再自主运行第三步；Publisher 只读取**已有目录**，不重新跑 GPU，只创建清理后的实验分支与 PR，不写主分支，也不自动合并。

报告包含 `manifest.json`、`correctness.json`、`benchmark.csv`、`summary.md`，准确记录被测 SHA。Benchmark 状态（`BENCHMARK_PASS`/`BENCHMARK_FAIL`/`NOT_RUN`）与上传状态（`PUBLISHED`/`PUBLISH_FAILED`/`PUBLISH_BLOCKED`/`NOT_REQUESTED`）严格分开。拒绝含凭据、隐私、超大或格式异常的报告；上传必须幂等且由 GitHub 确认成功。

## Colab Secrets：`GITHUB_TOKEN`

已配置的 **`GITHUB_TOKEN` 是 Secret 名称**，不是明文值，需给 Notebook 开通读取权限。**`!python` 子进程不保证自动继承 Colab Secrets**；必须实际测试成功才能使用上面简洁的第三行。如果不行，**第三个上传 Cell** 使用安全备用代码：

```python
from google.colab import userdata
import os, subprocess
subprocess.run(
    ["python", "-m", "PACKAGE_NAME.benchmarks.publish",
     "--report-dir", "reports/gpu/RUN_ID"],
    env={**os.environ, "GITHUB_TOKEN": userdata.get("GITHUB_TOKEN")},
    check=True,
)
```

不可显示 Secret，也不可把 Token 拼进 `!export`、shell 字符串、命令行参数、Git URL 或报告。建议细粒度仓库 Token：目标仓库 Contents 与 Pull requests 读写最小权限。公开 PR 的报告也是公开的。

## 责任与验收

**架构师**定义 CLI、版本/运行路径、正确性基线与验收条件；**Codex**实现独立 run/publish 模块，真实运行 CPU、固定 SHA 安装/CLI 测试以及 Mock 上传异常和幂等测试；**Scientist**在真实 Colab 运行 GPU，检查证据，单独决定是否上传，并验证 Secret 子进程与 PR。没有真实对应 SHA 的证据不可宣称 `GPU_VERIFIED` 或 `PUBLISHED`。

[GPU 实验流程](GPU_EXPERIMENT.md)负责实验阶段和证据，本文负责三步接口与 Secret。无需 GitHub Actions、Drive 同步或 Notebook 数值内核。
