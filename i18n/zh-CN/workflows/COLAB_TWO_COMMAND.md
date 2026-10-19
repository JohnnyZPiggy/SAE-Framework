# Colab 三步执行契约：安装、Benchmark、上传

> 语言：[English](../../../workflows/COLAB_TWO_COMMAND.md) | **简体中文**  
> 为避免旧链接失效，沿用 `COLAB_TWO_COMMAND.md` 历史路径；**现行规范为三步**，不再是两条命令。

## 科学家操作流程

首次选择 GPU runtime，并在 Colab Secrets 设置名称为 **`GITHUB_TOKEN`** 的凭证、启用 Notebook 访问权限之后，每次实验有**三个独立步骤**：

```python
!pip install "git+https://github.com/OWNER/REPO.git@<EXACT_SOURCE_COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>
!python -m <package>.benchmarks.publish --report-dir reports/gpu/<run-id>
```

**以上仍是目标接口，并不表示 Publisher 或 Benchmark CLI 已经实现。** 架构师/Codex 必须填写实际包名、完整固定源码 SHA，以及 Benchmark 返回/使用的明确运行目录。第三步**由科学家决定是否运行**；先检查数值和计时，再上传。Benchmark **无需 GitHub token，也不得写入 GitHub**。执行第三条才明确授权创建已清理的实验结果分支与 PR，**并非授权自动合并**。默认 Benchmark 不再添加 `--publish`。

## Colab Secret 传递给子进程：必须验证

`GITHUB_TOKEN` 是已经设好的 **Secret 名称**，不是 token 值。务必在 Colab Secrets 侧栏给 Notebook 授权，不能在 Notebook、命令行、日志或报告中明文展示。

**Colab Secrets 不保证自动成为 `!python` 子进程的环境变量。** Codex 必须实现并真实测试安全获取方式：

- 优选：在实际 Colab 子进程证实可用后，由 Python Publisher 直接安全调用 `google.colab.userdata.get("GITHUB_TOKEN")`，绝不打印。
- **备用方案：** 如子进程无法直接读取，第三步改为**一个 Python 上传 Cell**，通过环境变量安全传给子进程，**不拼接 shell 命令**：

```python
from google.colab import userdata
import os, subprocess
subprocess.run(
    ["python", "-m", "<package>.benchmarks.publish", "--report-dir", "reports/gpu/<run-id>"],
    env={**os.environ, "GITHUB_TOKEN": userdata.get("GITHUB_TOKEN")},
    check=True,
)
```

不得使用 `!echo`、`!export GITHUB_TOKEN=明文`、把 token 放进 URL 或命令行参数、打印环境变量等方式。备用多行代码仍属于**第三个上传 Cell**，不是新阶段。真实测试前不得保证一行 `!python` 一定读到 Secret。

## 职责明确分离

- **安装：** 固定的完整源码 SHA，失败立即停止，不以浮动 `main` 代替。
- **Benchmark：** GPU/源码 SHA 检查 → 参考数值正确性 → 预热与同步计时 → 在独立 `reports/gpu/<run-id>/` 生成 `manifest.json`、`correctness.json`、`benchmark.csv`、`summary.md`。不自动上传或重复跑 GPU。
- **上传：** 只读取科学家指定的**已有结果目录**，不重跑 benchmark；校验数据格式、测试 SHA、白名单和大小，拒绝隐私/密钥，安全创建实验分支与 PR，支持幂等重试。不直接推 main、不自动合并、不覆盖既有实验。
- **分别记录：** `BENCHMARK_PASS / BENCHMARK_FAIL / NOT_RUN` 与 `PUBLISHED / PUBLISH_FAILED / PUBLISH_BLOCKED / NOT_REQUESTED`。数值失败不能宣称加速通过；必须取得 GitHub 确认后才能报告 PR 创建成功。
- **最小权限：** 建议将细粒度 token 只授权目标仓库，通常需要 Contents 读写、Pull requests 读写；只有在明确需要 Issue 评论时才开 Issue 权限。公开仓库 Draft PR 也可能公开可见。

## 角色与验收

**架构师：** 确定打包接口、运行目录、正确性/计时设置、报告白名单、失败状态和最小授权，并为 Codex 写清三步验收；Benchmark 不依赖上传。

**Codex：** 分开实现与打包 `benchmarks.run` 和 `benchmarks.publish`；实际执行固定 SHA 的干净安装、CPU 数值/边界测试、CLI 冒烟；Mock 验证无 token、权限被拒、重复上传、报告异常与失败传播。Colab 子进程的 Secret 读取必须由科学家实际集成实验确认。

**科学家：** 选择 GPU、执行 Benchmark、审核误差与性能后，**自主决定是否运行第三步上传**，并在合并报告 PR 前复核内容。

**当前状态：** Publisher 未实现/未经测试时标记 `PUBLISHER_NOT_IMPLEMENTED` 或 `PUBLISH_UNVERIFIED`，不能因为规范更新就假装已上传。无需 GitHub Actions、Drive 同步、Notebook 内写数值算法，也不要求绑定 CUDA。

参见 [GPU 实验协议](GPU_EXPERIMENT.md) 与 [薄 Notebook 示例](../../../examples/colab/README.md)。
