# SAE Colab 实验报告 — <run-id>

> 语言：[English](../../../templates/EXPERIMENT_REPORT.md) | **简体中文**

**Issue：** #<编号>  
**代码 PR：** #<编号>  
**被测试的源码 commit：** `<40 位 SHA>`  
**报告 PR：** <链接>  
**实验操作者：** 人类科学家  
**UTC 时间：** <时间>  
**状态：** PASS / FAIL / NOT RUN / BLOCKED

## 三文档溯源关联
**数学研究报告：** `docs/research/<algorithm>-tensorization.md` / 链接  
**工程实现报告：** `docs/engineering/<algorithm>-engineering.md` / 链接  
**实验运行路径：** `reports/gpu/<run-id>/summary.md`  
**实际被测源码 SHA：** `<sha>`  
**实验报告发布 commit（如存在）：** `<另一个 SHA 或 NOT YET PUBLISHED>`

这是 [三文档交接协议](../workflows/THREE_ARTIFACT_HANDOFF.md) 中的**实验验证文档**，必须基于Codex 经 Scientist 计算资源授权实际执行 Colab 的输出生成，不能预先声称成功。

## 环境
CPU/GPU 型号、驱动/CUDA/PyTorch 版本、Colab runtime、dtype、种子、具体安装源。

## 正确性
参考基线、容差、比较指标、最大绝对/相对误差、失败数量、特殊边界案例。

## Benchmark
规模、方法、CUDA 同步、预热、`torch.compile` 编译开销、重复次数、统计汇总、单位与同精度比较。

## 实验结果
链接 `manifest.json`、`correctness.json`、`benchmark.csv` 和小图片。

## 解读
科学含义、局限、潜在性能瓶颈与测量偏差。

## 下一步
验收 / Codex 修复 / 重跑 / GPT 导师讲解。