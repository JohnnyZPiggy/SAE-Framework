---
name: SAE 工程任务（中文）
about: 适用于数学算法或 PyTorch 工程任务
title: "[SAE] "
labels: []
assignees: []
---

<!-- 如有标签权限，可选择 agent:codex、status:ready、kind:engineering、priority:p1 -->

**研究目的：**

**前置张量化研究报告链接与状态（RESEARCH_READY / 明确例外 / 基础设施不适用）：**

**数学 / 数值契约：**

**输入、输出与精度要求：**

**交付成果：**

**验收测试（必须提供真实证据）：**

**Colab 三步验收（算法任务）：** 指定 GitHub SHA 安装 → 独立 `benchmarks.run --device cuda --out reports/gpu/RUN_ID` → 科学家审核后**可选** `benchmarks.publish --report-dir reports/gpu/RUN_ID` 上传。Benchmark 不自动发布，Publisher 从名为 `GITHUB_TOKEN` 的 Colab Secret 安全获得凭证；Codex 真实执行 CPU 数值、打包与 CLI 测试；Scientist GPU/上传未执行应写 NOT_RUN。

**Colab GPU 验证方案（如需要）：**

**依赖与阻塞：**
