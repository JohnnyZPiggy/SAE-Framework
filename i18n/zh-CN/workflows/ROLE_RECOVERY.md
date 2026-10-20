# 角色恢复与完整性协议（V3.3）

> [English](../../../workflows/ROLE_RECOVERY.md) 为规范版本 | 简体中文译本

## 目的
GitHub 保存持续项目状态。新对话或中断后须恢复明确角色、目标、固定协议、任务证据和实际权限；这只是读取检查，不是后台 Agent 或额外数据库。

## 恢复检查
1. 确认用户指定的目标仓库；不明确就询问，不能把 SAE Framework 母仓库默认为算法项目。
2. 遵守明确角色口令：`推进导师工作` → GPT Mentor；`推进架构师工作` → GPT Architect；`推进工程师工作` → Codex Engineer；不得擅自换角色。
3. 读取项目 `AGENTS.md`、`sae.yaml`、固定 `.sae/` 协议和相关流程；不得悄悄把 V3.2 项目升级到 V3.3。
4. 检查实时 Issue/PR、候选源码 SHA、数学/工程/实验报告及 Scientist 决定。区分数学批准、CPU 验证、加速器准备状态与**特定设备真实验证**；不能由 CPU 或 CLI 选项推断 GPU/TPU 已可用。
5. GPU/TPU 前核实真实 GitHub/CLI/运行环境权限和 Scientist 当前的 [No Price Gate Colab 常设授权](../../../workflows/GPU_EXPERIMENT.md)（及后续更严格限制或撤销）；既有权益内不重新索要价格预测或逐次时长/额度审批。无权限、超出既有权益或授权撤销才 BLOCKED；缺少逐次预算数字本身不构成阻塞。
6. 只执行一个有边界的角色周期：Mentor 研究教学；Architect 设计、审核、决定合并；Codex 实现并执行获授权的本地/Colab CPU/GPU/TPU 实验，下载校验结果、释放会话、提交 PR；Scientist 保留实质科研和预算决定。
7. 如实报告 PASS/FAIL/NOT RUN/BLOCKED、源码/报告链接、阻塞与一条[下一步](../../../workflows/NEXT_ACTION.md)。

执行/发布遵循[计算实验协议](../../../workflows/GPU_EXPERIMENT.md)；合并裁量遵循[常设授权](../../../governance/STANDING_AUTHORIZATION.md)。禁止虚报、擅自换角色、无限重试、GitHub Actions 或 Codex 自合并。
