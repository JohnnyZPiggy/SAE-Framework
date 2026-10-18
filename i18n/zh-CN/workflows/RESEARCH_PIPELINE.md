# 研究先行、CPU 验证、GPU 收尾：三阶段研发协议

> [English](../../../workflows/RESEARCH_PIPELINE.md) | 简体中文

## 默认原则

**CPU by Default. GPU by Exception.** 算法项目默认先研究数学，再完成 CPU 工程与编译测试，最后集中使用 Colab GPU 验证与优化。GitHub 是长期交接记录，不依赖 GitHub Actions、Drive 同步或后台自主 Agent。

### 第一阶段：数学研究（GPT Mentor + Scientist）

分析数学等价变换、矩阵向量/批处理/张量结构、复杂度、数值稳定性、参考算法与顺序依赖。输出既有 `docs/research/<algorithm>-tensorization.md`。科学家批准 `RESEARCH_READY` 后才进入工程；`RESEARCH_BLOCKED` 继续研究，`NOT_TENSORIZABLE` 可以停止或明确批准其他方案。

### 第二阶段：CPU 工程研究（GPT Architect + Codex）

GPT 规定算法接口、数值容差、实验预设、可安装包和未来 Colab 双命令接口；Codex 在笔记本 CPU 环境实现独立 Python 模块，并**真实执行**参考精度、随机/边界测试、dtype/shape、CPU eager、CPU `torch.compile`（支持时）、可选 `fullgraph=True`、graph break 检查、CPU benchmark、干净 pip 安装与 CLI 冒烟测试。记录实际结果、环境、源码 SHA 到 `docs/engineering/<algorithm>-engineering.md`。**CPU compile 通过不代表 GPU compile 通过，更不代表 GPU 加速。**

Codex 填写 [GPU Readiness](../../../templates/GPU_READINESS.md)，GPT Architect 核验后才标记 `GPU_READY`。不能运行的测试必须记为 `NOT_RUN`，不得写 PASS。日常 CPU 循环无需科学家反复开 Colab。

### GPU Readiness 阶段关口

需要数学研究已审核、CPU 数值测试真实通过、CPU `torch.compile` 证据或明确豁免、可安装的 Benchmark CLI、固定默认 workload、真实被测 SHA、GPU 错误处理和报告格式、两行 Colab 目标命令。任何豁免必须有理由和架构师批准。不满足则 `CPU_BLOCKED` 并创建/更新 Codex Issue。`GPU_READY` **只是待 GPU 验收，不是 GPU 已成功运行**。

### 第三阶段：GPU 实验与性能工程（Scientist + GPT + Codex）

通过关口的算法进入 GitHub Issue 形式的待测队列；科学家有空时集中运行 Colab。最终目标是指定源码 SHA 的 pip 安装 + 一条打包的 Benchmark CLI（可选 `--publish`）。Publisher 尚未实现和验证前，必须如实保留人工上传方式。先验证 GPU 精度，再测编译、同步、预热、耗时、不同设备配置，保存 run ID、真实 SHA 与实验报告。

GPU 编译/精度出错，返回第二阶段并让 Codex 先在 CPU 复现可修复问题；数学前提失效则回到第一阶段。没有解决已知问题前，不反复要求科学家跑 GPU。`GPU_VERIFIED` 只代表真实验证，不等于加速成功。

## 一句话恢复工作

在**已指定的算法仓库、且工具权限可用**的会话中，`推进导师工作`、`推进架构师工作`、`推进工程师工作` 表示：读取固定 SAE 版本、AGENTS/sae.yaml、开放 Issues/PR、已有报告；选择最高优先级且未阻塞的本角色任务；执行一轮有边界的工作；回写证据与下一步。不得假装已连接本地笔记本、已在后台执行或已完成无法实际运行的任务。若 Codex 本地环境不可用，先写好 GitHub 工单。科学家保留研究和 GPU 验收权。

## 状态和证据

`RESEARCH_READY`、`RESEARCH_BLOCKED`、`CPU_IN_PROGRESS`、`CPU_BLOCKED`、`CPU_VALIDATED`、`GPU_READY`、`GPU_IN_PROGRESS`、`GPU_VERIFIED`、`GPU_BLOCKED`。状态以 GitHub Issue/PR 为准，链接既有数学、工程、实验三份报告。GPU 队列只需 Issue/标签，不增加软件系统。

已有三文档保持正式科研记录；GPU Readiness 只是一张轻量关口表。新项目应固定包含本协议的 SAE commit，老项目不会自动升级。实验 PR 由科学家审核，不自动合并。
