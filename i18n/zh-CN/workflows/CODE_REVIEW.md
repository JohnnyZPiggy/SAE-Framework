# PR 技术审核：证据关口

> [English](../../../workflows/CODE_REVIEW.md)（正式规范） | 简体中文

架构师必须阅读**最新真实 PR Diff、修改文件、head SHA 和 Issue 验收条件**，不能只看作者自述。

## 核验清单

- **数学：** 科学家确认过的目标、假设、参考 oracle；
- **API/数值：** 形状、dtype/设备、稳定性、容差、边界/回归、内存复杂度；
- **CPU：** Codex 真实运行结果、适用时 `torch.compile`、干净 pip 安装和 CLI；`NOT_RUN` 不是 `PASS`；
- **GPU：** 声称或要求 GPU 时须科学家提供与被测 SHA 匹配的 Colab 正确性和预热/同步测速，不能拿 CPU 冒充；
- **安全/平台：** 无密钥隐私泄漏，许可证与依赖风险、GitHub 冲突/权限/保护与审查意见；未配置 Actions 不等于 CI Passed。

审核结果：`REQUEST_CHANGES`、`CONDITIONALLY_READY`、`MERGE_APPROVED` 或 `DO_NOT_MERGE`；**只有 GitHub 真实返回合并 SHA 才是 `MERGED`**。

最终合并权、T1/T2/T3 和审计只以 [常设授权](../governance/STANDING_AUTHORIZATION.md)为准。GPT 负责符合条件 PR 的最终技术决定，Scientist 保留重大科研/安全内容决定；Codex 不自行合并。不强推或直接推主分支。Benchmark 比较须保持问题与精度等价，并披露编译/预热/同步/波动。
