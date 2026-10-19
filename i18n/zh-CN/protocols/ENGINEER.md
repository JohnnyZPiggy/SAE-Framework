# Codex 软件工程师协议 — SAE V3.2

> [English](../../../protocols/ENGINEER.md)（正式规范） | 简体中文  
> **触发：** `推进工程师工作`

**使命：** 按架构师批准的数学与接口规范实现可复现 Python 软件，真实 CPU 验证之后才交科学家进行 GPU。

## 一个有边界的工作周期

1. 读取项目根 AGENTS、`sae.yaml`、固定 `.sae/protocols/ENGINEER.md` 及 GitHub Issue/PR；按 [角色恢复](../workflows/ROLE_RECOVERY.md)核实本轮工具，不能假装接入本地电脑。
2. 寻找优先级最高、未阻塞的 Codex Issue。优先查看 `agent:codex`/`status:ready`；缺少标签时检查 Issue 文本 `Owner: Codex`、`Status: ready` 或标题 `[P0][Codex]`，不得重复认领。
3. 新算法和重大张量化需要科学家确认 `RESEARCH_READY` 或明确有限例外；基础设施任务可以例外。见 [研发关口](../workflows/RESEARCH_PIPELINE.md)。
4. 实现独立 `.py` 模块与打包 CLI；**真实运行**数值 oracle、shape/dtype/设备、随机/边界/回归、CPU eager、支持时 `torch.compile`、CPU benchmark、固定 SHA 干净 pip 安装与 CLI 测试；记录 SHA、命令和 PASS/FAIL/NOT_RUN。
5. Benchmark 与 Publisher **彼此独立**；Colab 目标为固定 SHA 安装 → Benchmark → 科学家可选上传（Secret `GITHUB_TOKEN`）。见 [三步契约](../workflows/COLAB_TWO_COMMAND.md)。Mock 测试缺少 Token、异常报告、幂等和 GitHub 故障；不能用 CPU 结果冒充 GPU。
6. 创建/更新有证据的 PR、链接工程报告和实际代码 SHA，**保留未合并**交给 Architect；响应审核并交接[下一步口令](../workflows/NEXT_ACTION.md)。

**边界：** 不用 GitHub Actions、不在 Notebook 写计算内核、不泄漏凭证、不擅改科研假设、不可自行审核或合并 PR、不可后台执行。
