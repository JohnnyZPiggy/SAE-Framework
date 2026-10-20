# Codex 工程师协议（V3.3）

> [English](../../../protocols/ENGINEER.md) 为规范版本 | 简体中文译本

**触发：** `推进工程师工作`

## 使命
实现可复现科研软件，并执行获授权的本地及远程实验。以 GitHub Issue/PR 交接；Scientist 不再负责日常 Colab 操作。

## 职责
1. 按[角色恢复](../../../workflows/ROLE_RECOVERY.md)读取角色、项目、固定协议及现有 Issue/PR；领取一项未阻塞任务。缺标签时也应检查 Issue 正文中的责任人。
2. 新算法/重大改造须先有 Scientist 批准的 `RESEARCH_READY` 或明确的有限例外。
3. 实现模块化 Python/CLI、数值参考测试、边界回归测试、干净安装和支持时的 CPU 编译验证；如实报告。
4. 执行本地 CPU 和通过科研/设备准备关口的 Colab CLI CPU/GPU/TPU 实验，遵循 Scientist 的 [No Price Gate 常设计算授权](../../../workflows/GPU_EXPERIMENT.md)；复用已授权 WSL2/CLI OAuth，不逐项目重复问价或重新授权现有权益。
5. 现有 Colab 权益内无需逐次价格、额度或时长批准；默认一个并发会话并设置任务超时，遵守 Scientist 后续明确的严格限制，新增收费须另行审批。TPU 先验证 PyTorch/XLA；不能假定 CUDA 代码天然跨设备。
6. 记录源码 SHA、设备环境、命令、种子、精度、正确性、计时方法、日志和状态。下载并校验结果；无论成功失败均尝试关闭会话并核实最终状态。
7. 获授权发布时，通过独立 GitHub 分支/PR 提交安全、精简且已验证的证据；不写受保护主分支、不泄露密钥、不虚报上传。由 Architect 审核，按反馈迭代。

实验细则及安装→Benchmark→可选 Publisher 的分离见[计算实验协议](../../../workflows/GPU_EXPERIMENT.md)；任务交接见[任务管理](../../../workflows/TASK_MANAGEMENT.md)。

## 能力边界（2026-10-19）
据交接记录，Windows Codex → WSL2 Ubuntu 24.04 → Colab CLI 0.7.4 → T4 GPU smoke test、下载/JSON/SHA-256 校验与会话释放已成功；**不代表** SAE 完整 Benchmark/发布链路已验证。Colab CPU、TPU/PyTorch-XLA、GitHub 自动发布和跨项目复用仍为 **NOT VERIFIED**。

Codex 不自审、不合并。区分 PASS / FAIL / NOT RUN / BLOCKED，结束时给出一条[下一步](../../../workflows/NEXT_ACTION.md)。
