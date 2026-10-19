# 人类科学家协议 — SAE V3.2

> [English](../../../protocols/SCIENTIST.md)（正式规范） | 简体中文

**Scientist 是研究负责人：** 选择课题、批准数学假设与权衡、亲自在 Colab 运行实验，并保留科学、重要安全/授权和许可证等**实质内容决定权**。GPT 的最终 PR 合并裁量权仅由 [常设授权](../governance/STANDING_AUTHORIZATION.md)规定。

## 一个科研周期

1. 决定课题，审查导师的[数学研究](../workflows/MATHEMATICAL_RESEARCH.md)，选择 `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE`，或明确批准有限参考实现。
2. 架构师和 Codex 先进行真实 CPU 工程；通过 [GPU Readiness](../templates/GPU_READINESS.md) 后才集中跑 Colab。
3. [Colab 三步](../workflows/COLAB_TWO_COMMAND.md)：**固定 SHA 安装 → 数值正确性与 GPU Benchmark → 审核后可选独立上传**。Secret 名为 `GITHUB_TOKEN`，不得打印或提交。
4. 检查被测源码 SHA、GPU、dtype/seed、误差、预热、同步计时和局限；从真实运行生成 `manifest.json`、`correctness.json`、`benchmark.csv` 与 `summary.md`，通过 [三文档交接](../workflows/THREE_ARTIFACT_HANDOFF.md)关联数学/工程证据。
5. Publisher 未真实验收则标 `PUBLISH_NOT_RUN`，必要时科学家明确授权安全的人工上传；不通过 Drive 同步。回传真实 PR/Issue 链接供 GPT 审核。

科学家不需要亲自维护大量 Python。Codex 不自我合并；GPT 经真实审核自主决定合格 PR 是否合并。合并授权不等于授权 GPT 擅自决定科研、安全等实质问题或后台运行实验。
