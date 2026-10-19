# GPU 实验与 Colab 三步执行规范

> [English（正式规范）](../../../workflows/GPU_EXPERIMENT.md) · 简体中文

## GPU 关口

**Scientist 亲自在 Colab 操作。** 数学方案已经批准、Codex 真实完成 CPU oracle/边界/回归、适用时 `torch.compile`、Benchmark、固定 SHA 干净 pip 安装和 CLI 冒烟之后，Architect 审核 [GPU Readiness](../templates/GPU_READINESS.md) 才能标 `GPU_READY`。CPU 通过不等于 GPU 验证。

## 三个独立 Colab Cell（目标接口，非已实现证明）

提前选择 GPU runtime，并在 Colab Secrets 设置、启用 Notebook 可访问的 **`GITHUB_TOKEN`**。实际执行要替换完整被测 SHA、真实包名与报告目录：

```python
!pip install "git+https://github.com/OWNER/REPO.git@<EXACT_SOURCE_COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>
!python -m <package>.benchmarks.publish --report-dir reports/gpu/<run-id>
```

1. **安装：** 精确源码 commit，不能用浮动 main 代替。
2. **Benchmark：** 先数值正确性，再做实际 GPU 预热/同步计时，只生成本地报告，**不用 GitHub token、不自动上传**。
3. **上传（可选）：** Scientist 自己检查误差、性能和隐私后，才选择第三步；Publisher 只读取已有报告，不重新执行 GPU，不直接写 main 或自动合并，仅创建分支/PR，之后由 Architect 审核。

以上只是**待 Codex 实现/测试的 CLI 契约**，不能凭文档宣称已运行。

## GITHUB_TOKEN 与子进程

Colab Secrets 中已经使用名称 **`GITHUB_TOKEN`**，不是把 token 值写进 Notebook。`!python` 子进程**不保证**直接继承 Secret 环境变量。只有真实 Colab 验证 Publisher 能安全通过 `google.colab.userdata.get("GITHUB_TOKEN")` 读取后，才采用简洁的一行上传命令。

否则第三步改为**一个 Python 上传 Cell**，安全注入进程环境，绝不拼接 Shell 字符串：

```python
from google.colab import userdata
import os, subprocess
subprocess.run(
    ["python", "-m", "<package>.benchmarks.publish", "--report-dir", "reports/gpu/<run-id>"],
    env={**os.environ, "GITHUB_TOKEN": userdata.get("GITHUB_TOKEN")},
    check=True,
)
```

不得回显 Secret、拼进 URL/命令行、打印环境变量或上传含密钥的报告。Token 应只授权目标仓库最小所需 Contents / Pull requests 写入权限。公开 PR 即使未合并，别人也可能看到。

## 四个小文件与诚实状态

每次实际运行形成唯一的 `reports/gpu/<run-id>/`：

- `manifest.json`：完整源码 SHA、设备、环境、dtype、随机种子和配置。
- `correctness.json`：oracle、容差、误差与真实 PASS/FAIL。
- `benchmark.csv`：实际计时样本、基线及预热/同步说明。
- `summary.md`：结果解释、限制及相关 Issue/PR。

Publisher 必须校验被测 SHA、格式、文件白名单与体积、秘密/隐私、重复 run ID 与幂等重试，成功创建 GitHub PR 后才报告已发布。不得强推、覆盖旧报告、自动合并或以数值失败宣称提速。

**分别记录：** `BENCHMARK_PASS / BENCHMARK_FAIL / NOT_RUN` 和 `PUBLISHED / PUBLISH_FAILED / PUBLISH_BLOCKED / NOT_REQUESTED`；上传失败仍保留本地报告。

Mentor/Scientist 负责数学与真正实验，Architect 指定验收基线并评审证据，Codex 实现独立 run/publish CLI、CPU 测试和 Publisher 模拟异常测试。没有实测不得声称 Colab 凭证传递已成功。不使用 GitHub Actions、Drive 同步或强制 CUDA 内核。

参见 [三成果交接](THREE_ARTIFACT_HANDOFF.md)、[任务管理](TASK_MANAGEMENT.md)和 [常设合并授权](../governance/STANDING_AUTHORIZATION.md)。
