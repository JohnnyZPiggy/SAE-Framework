# GPU 实验准备验收 — <algorithm>

> [English](../../../templates/GPU_READINESS.md) | 简体中文

**算法项目 / Issue：** <URL>  
**真实被测源码 SHA：** <FULL_SHA>  
**审核：** GPT Architect  
**结论：** CPU_BLOCKED / GPU_READY  
**GPU 实验：** NOT_RUN（真实 Colab 执行前）

| 关口 | PASS / FAIL / NOT_RUN / WAIVED | 真实证据（命令、输出、链接） |
| --- | --- | --- |
| 科学家已审核数学报告 | | |
| CPU 参考算法、随机和边界正确性 | | |
| CPU eager 与 `torch.compile` 执行 | | |
| 需要时的 fullgraph / graph-break 检查 | | |
| CPU Benchmark 与误差容差 | | |
| 干净环境、固定 SHA 的 pip 安装和打包 CLI | | |
| GPU 默认 workload、设备失败和报告设计 | | |
| 两条 Colab 命令及被测源码 SHA | | |

**豁免（理由 + 架构师批准）：** <无或详情>  
**尚未解决：** <无或 Issue 链接>  
**GPU 待测队列 Issue：** <链接或 NOT_QUEUED>  
**审核依据：** <简短结论>

必选项 FAIL 或 NOT_RUN 且无明确批准豁免，不得标记 GPU_READY。**GPU_READY 不代表 GPU 正确性、GPU 编译或 GPU 加速已通过。** GPU 真实运行和实验报告另行记录。
