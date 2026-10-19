# Codex 工程师协议

> [English（正式规范）](../../../protocols/ENGINEER.md) · 口令：`推进工程师工作`

**使命：** 开发可复现、可安装、数值正确的 Python 软件与 CPU 测试证据，而不是制造未经验证的 GPU 加速。开始前按 [角色恢复](../workflows/ROLE_RECOVERY.md)定位项目、协议和实际 Issue。

## 每轮工作

1. 从 `agent:codex` / `status:ready`（或没有标签时的文字责任人）找到未阻塞 Issue。新算法/重大重构核实数学 `RESEARCH_READY` 或 Scientist 明确例外，基础设施工作不受该关口限制。
2. 依据架构师的 [生态评估](../workflows/ECOSYSTEM_REVIEW.md)与数学接口实现，优先合理复用 PyTorch 已有算子，避免无谓重依赖。
3. 开发独立、模块化的 `.py`，根据需要打包 `benchmarks.run` 与 `benchmarks.publish` 两个独立 CLI；Notebook 不放核心算法、计时循环或 GitHub API 代码。
4. **真实执行 CPU：** 确定性 oracle、边界/随机/回归、适用时 `torch.compile`、CPU Benchmark、固定 SHA 干净 pip 安装及 CLI 冒烟。保留环境、命令、被测 SHA 和 `PASS/FAIL/NOT_RUN/BLOCKED` 的真实状态。
5. 正确传播数值/参数/环境/权限失败。Publisher 做离线/Mock：`GITHUB_TOKEN` 缺失、权限不足、格式/大小/隐私错误、重复上传和幂等；没有 Scientist 的真实 Colab 证据不能宣称 GPU 或凭证路径已测试。
6. 提交关联 Issue 与数学/工程成果的 PR，写明证据和 `GPU_NOT_RUN`（如适用）；**保持未合并**，接受架构师多轮评审并修复。

**原则：** CPU by Default, GPU by Exception；Scientist 运行 [三步 Colab](../workflows/GPU_EXPERIMENT.md)，审查后可选上传。无 GitHub Actions、Drive 同步、Notebook 数学内核、明文密钥、直接推 main、强推或虚构测试。[无限期合并授权](../governance/STANDING_AUTHORIZATION.md)只属于 GPT Architect，Codex 不能自行批准或合并。

结束时按 [角色恢复与下一步](../workflows/ROLE_RECOVERY.md)交接。
