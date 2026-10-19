# SAE V3.3 — 新项目 AGENTS 中文参考

> [English project template](../../../../examples/project/AGENTS.md) 为规范版本；本文件供中文阅读。目标项目根目录应复制英文模板并填写实际值。

**项目：** `<OWNER>/<PROJECT>`  
**科研目标：** `<ALGORITHM_OR_PAPER>`  
**SAE 固定快照：** `.sae/`，commit `<ACTUAL_40_CHARACTER_FRAMEWORK_SHA>`

## 工作前
读取项目根 `AGENTS.md`、`sae.yaml`、`.sae/AGENTS.md`、当前角色协议、相关流程与 GitHub Issue/PR。链接不等于已读取；不得悄悄升级固定快照。

## 分工
- **Scientist：** 决定研究方向、数学/科学结论及 GPU/TPU 硬件、会话/时长/额度授权。
- **GPT Architect/Mentor：** 数学指导、规格、Issue 派发、证据审核；按[固定治理协议](../../../../governance/STANDING_AUTHORIZATION.md)及当前所有者授权决定合格 PR 最终合并。
- **Codex：** 实现、本地 CPU 和获授权的 Colab CLI CPU/GPU/TPU 实验，校验报告、释放会话、经 GitHub 分支/PR 提交证据；不自合并或直接写受保护主分支。

## 流程
新算法/重大改造先完成 Scientist 审核的[数学研究](../../../../workflows/MATHEMATICAL_RESEARCH.md)，Architect 进行[生态复用评估](../../../../workflows/ECOSYSTEM_REVIEW.md)并派单，Codex 实现、测试和实验，Architect 审核 GitHub 证据。实验遵循[计算实验协议](../../../../workflows/GPU_EXPERIMENT.md)的固定 SHA 安装、无 GitHub 写入 Benchmark、可选发布三个独立阶段。设备兼容、Publisher 和加速效果都必须有实测证据。不默认使用 GitHub Actions、Drive 同步或未批准计算资源。

**口令：** `推进架构师工作` / `推进导师工作` / `推进工程师工作`。每轮开始执行[角色恢复](../../../../workflows/ROLE_RECOVERY.md)，结束给出[下一步](../../../../workflows/NEXT_ACTION.md)；如实标记 PASS / FAIL / NOT RUN / BLOCKED 和源码 SHA。
