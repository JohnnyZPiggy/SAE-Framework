# SAE 工程设计与实现报告 — <算法名称>

> 语言：[English](../../../templates/ENGINEERING_REPORT.md) | **简体中文**

**目标项目：** `<owner/repo>`  
**算法 / 里程碑：** <名称>  
**关联 Issue / 代码 PR：** <链接>  
**数学研究文档：** `docs/research/<algorithm>-tensorization.md` — 已批准 `RESEARCH_READY` / 明确有限例外 / 仓库初始化任务不适用  
**总架构师：** GPT · **工程师：** Codex · **科学负责人：** 人类 Scientist  
**被测源码 commit：** `<真实 40 位 SHA 或 NOT YET AVAILABLE>`  
**进度：** SPECIFIED / IMPLEMENTING / REVIEW / CPU_VERIFIED / BLOCKED（写清真实证据）

## 1. 数学与工程契约（GPT 架构师）
链接已审核的数学报告，明确参考版和张量版、张量维度、dtype、支持的设备、数值参考判据、误差容差、边界和数学假设。**引用数学方程，不复制整篇研究报告。**

## 2. 工程设计（架构师 → Codex）
记录模块位置、Python 接口、CLI 参数、输入输出结构、按需使用的 batching/`torch.compile`、硬件可移植性与资源限制。提出工程任务、依赖及验收关口。

## 3. 实际实现记录（Codex）
| 模块与修改路径 | 对应数学结构 / 功能 | 实现取舍与限制 |
| --- | --- | --- |
| `src/...` | | |
| `tests/...` | | |
| `benchmarks/...` | | |

如偏离数学规格，必须请架构师/科学家确认，不能自行改变数学问题。

## 4. 真实验证证据（Codex）
| 测试或基线比较 | PASS / FAIL / NOT RUN / BLOCKED | 实际命令、环境、种子和证据 |
| --- | --- | --- |
| 原始算法/参考结果对照 | NOT RUN | |
| CPU 单元与回归测试 | NOT RUN | |
| 随机与特殊边界情况 | NOT RUN | |
| CPU Benchmark（如适用） | NOT RUN | |
| GPU / TPU 实验（由科学家操作） | NOT RUN | 链接实验报告，不能编造结果 |

仅在实际测量后才报告最大/相对误差，描述容差和失败；GPU 加速结论引用 `reports/gpu/<run-id>/summary.md`，不重复抄性能数值。

## 5. 复现与交接（Codex）
- **测试源码 commit SHA：** <真实 SHA / NOT RUN>
- **Python/PyTorch、dtype、设备：** <真实环境 / NOT RUN>
- **命令、输入、种子：** <实际命令>
- **Issue / PR / 附件：** <链接>
- **交付科学家的 Colab 实验说明：** <候选 SHA、CLI、规模、容差>
- **已知问题与限制：** <说明>

## 6. 审核与后续（架构师 + 科学家）
- **架构师审查：** REQUEST_CHANGES / CONDITIONALLY_READY / ACCEPTED（附理由和链接）。
- **科学家的决定：** <已批准决策链接或 pending>。
- **下一步：** 修复 / 重跑 CPU / Colab 实验 / 返回数学研究。
- **学习收获：** 可选的一条数学或数值洞见，不强制长文记录。

工程文档**不取代 GitHub PR 正式审查**，不能把没有执行的 GPU 测试写成通过，也不能覆盖其他证据。
