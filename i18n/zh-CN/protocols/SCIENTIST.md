# 人类 Scientist（项目科学负责人）

> [English（正式规范）](../../../protocols/SCIENTIST.md)

Scientist 决定科研方向、数学验收、真实 GPU 实验及重要治理/安全/许可证/公开数据问题。GPT/Codex 提供数学、工程和可核验证据。

1. **数学：** 新算法和重大张量化重构先与 Mentor 讨论矩阵向量结构和数学等价，审核 [数学研究](../workflows/MATHEMATICAL_RESEARCH.md)，作出 `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE` 或有限例外决定。
2. **CPU 工程：** Architect 做 Build-vs-Reuse 和派单，Codex 实际测试 CPU oracle、回归、打包及固定 SHA CLI。CPU 编译不能冒充 GPU 结果。
3. **Colab：** 通过架构师 `GPU_READY` 后，安装精确被测 SHA，运行独立 Benchmark，检查 `manifest.json`、`correctness.json`、`benchmark.csv`、`summary.md` 的误差和计时。
4. **可选上传：** 审查无敏感信息后，按 [三步协议](../workflows/GPU_EXPERIMENT.md)使用 Colab Secret `GITHUB_TOKEN` **单独**上传报告；Benchmark 不自动发布，公开数据由 Scientist 自己决定。
5. **权限：** Scientist 仍决定科研假设、数学结论、重要安全治理/许可和危险操作；不必在这些实质决定已满足后重复批准“点合并”。GPT Architect 依 [全部本人公开仓库无限期授权](../governance/STANDING_AUTHORIZATION.md)审核合格 PR 并最终决定是否合并，授权随时可撤销。

Scientist 无需亲自写笨重 Python、运行 GitHub Actions 或用 Drive 同步项目结果。保留 [三份科研成果](../workflows/THREE_ARTIFACT_HANDOFF.md)，按 [角色恢复与下一步](../workflows/ROLE_RECOVERY.md)继续。
