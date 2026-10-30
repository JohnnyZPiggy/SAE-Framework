# Colab 计算工具

> [English](README.md) | 简体中文

三个独立的 Python 文件：本地预检和有界的 Colab GPU 控制器。它们不是包、守护进程或发布器，科研计算由项目的驱动脚本负责。来源与许可：[NOTICE](NOTICE.md)。

| 文件 | 作用 |
|---|---|
| `environment_preflight.py` | 检查精确 commit、未提交改动和可写临时路径；导出已提交的源码树（标准库 + Git） |
| `colab_control.py` | 每种设备一个 GPU 会话：确认零会话 → 分配 → 探测设备 → 运行驱动 → 下载 → 关闭 → 确认归零 |
| `kernel_smoke.py` | 远端探针：输出 `KERNEL_REACHABLE` 和一行 `DEVICE_OBSERVED` JSON（来自 `nvidia-smi`，能导入 torch 时也记录 torch 信息） |

**需要**已认证的 Colab CLI **0.7.4**，并且要在启动运行的那个 shell 里（Windows 下在 WSL 里）。支持请求 `T4`、`L4`、`G4`、`H100`、`A100`；G4 按实际观测到的 `RTX PRO 6000` 匹配。真机验证过：T4、L4、A100、G4。H100 被 provider 拒绝。

## 用法
先做本地检查，这一步不会分配会话：
```sh
python tools/compute/colab_control.py --preflight-only --cli colab \
  --repo-path path/to/project --source-sha <40 位 SHA> --run-id check-1 --out out/check-1
```
用项目已提交的驱动和清单做真机运行：
```sh
python tools/compute/colab_control.py --cli colab --repo-path path/to/project \
  --source-sha <40 位 SHA> --driver scripts/driver.py --artifacts experiments/artifacts.json \
  --devices T4,L4,A100,G4 --run-id m2b-1 --out out/m2b-1
```
研究规模的运行要显式设置预算，例如 `--task-seconds 14400 --allocation-seconds 10800 --work-timeout 3600 --cleanup-seconds 120`。预算按每种设备分别计算。

## 适配器约定
- `--driver` 和 `--artifacts` 必须是 `--repo-path` 里已提交的文件，从精确的 `--source-sha` 读取（忽略未提交的副本）。
- 清单格式为 `{"artifacts": [{"name": "result.json"}]}`。名称以 `.json` 结尾，不含路径分隔符。每个文件从 `/content/<name>` 下载，内容必须包含精确的 `source_sha` 和 `"status": "PASS"`。
- 驱动会收到环境变量 `SAE_CANDIDATE_SHA`、`SAE_DEVICE_REQUESTED` 和 `SAE_DEVICE_OBSERVED`（JSON）。
- 设备不匹配时为 `BLOCKED`，除非传入 `--allow-device-mismatch`。

示例：[examples/compute_adapter](../../examples/compute_adapter/)，只生成一个传输测试文件。

## 安全行为
- 分配前，认证的 `usage` 读回必须显示**活动会话为 0、余额为正**，否则不分配。
- 只要尝试过分配，无论成功、失败还是 Ctrl-C，都会执行 `stop`，再重新读回确认活动会话为 0。释放未确认记为 `CLEANUP_FAILED`，并中止多设备序列。
- 一次只开一个会话；超时有限；不自动重试；不调用任何购买或计费命令。
- 报告（`colab-control.json`、`colab-devices.json`）记录：状态、SHA、请求/实际设备、前后的活动会话数与余额、artifact SHA-256、命令退出码。原始 CLI 输出一律不写入，因为它可能含 token 或会话 URL。
- 这里的 `PASS` 只表示传输和来源校验通过，**不是**科研验收；数值证据由项目自己保存。

## 测试
```sh
python -m unittest discover -s tools/compute/tests
```
