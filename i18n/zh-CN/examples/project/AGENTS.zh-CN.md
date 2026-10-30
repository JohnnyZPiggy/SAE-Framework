# SAE V3.4 — 新项目 AGENTS 中文参考

> [English project template](../../../../examples/project/AGENTS.md) 为规范版本；本文件供中文阅读。目标项目根目录应复制英文模板并填写实际值。

**项目：** `<OWNER>/<PROJECT>`  
**科研目标：** `<ALGORITHM_OR_PAPER>`  
**SAE 固定快照：** `.sae/`，commit `<ACTUAL_40_CHARACTER_FRAMEWORK_SHA>`

## 工作前
读取项目根 `AGENTS.md`、`sae.yaml`、`.sae/AGENTS.md`、当前角色协议、相关流程与 GitHub Issue/PR。链接不等于已读取；不得悄悄升级固定快照。

## 分工
- **Scientist：** 设定/调整科研目标，随时可停止；不进行常规科研/工程/算力签核。
- **Architect/Mentor（默认 Claude）：** 自主决定数学研究、`RESEARCH_READY`、规格、验收、迭代及合格 PR 合并；按[固定治理协议](../../../../governance/STANDING_AUTHORIZATION.md)及当前所有者授权决定合格 PR 最终合并。
- **Engineer（如 Codex）：** 实现、本地 CPU 和现有账户 Colab CLI CPU/GPU/TPU 实验，校验报告、释放会话、经 GitHub 分支/PR 提交证据；不自合并或直接写受保护主分支。


## 简洁优先
遵循固定版本的[简洁契约](../../governance/SIMPLICITY_CONTRACT.md)：满足 Issue 完成标准的最小改动；只在信任边界校验；只测真正可能出错的地方；以 Git 作为完整性层。每个 Issue 写明规模预算和"不需要做"清单；审查可给出 `REQUEST_SIMPLIFY`。

## 流程
新项目固定协议包含[Lean Lab](../../../../workflows/LEAN_RESEARCH_LAB.md)时，`EXPLORE` 使用一个有界 Codex 批次和简短观察记录，`VALIDATE` 才需 GPT 审核数学、精确 SHA 与实测数值/性能证据。新算法/重大改造由 GPT 自行决定简明[数学研究](../../../../workflows/MATHEMATICAL_RESEARCH.md)，与[生态复用评估](../../../../workflows/ECOSYSTEM_REVIEW.md)、参考实现和 `PROBE_ONLY` 设备探针并行推进；Codex 实现、测试与实验，GPT 审查证据和合格 PR，**无须 Scientist 逐环节签核**。实验遵循[计算实验协议](../../../../workflows/GPU_EXPERIMENT.md)的固定 SHA 安装、无 GitHub 写入 Benchmark、可选发布三个独立阶段。若固定协议包含[实验默认执行](../../../../workflows/GPU_EXPERIMENT.md)，范围内科研/工程决定由 GPT 自行完成；Codex 在既有账户内无需人工算力许可。新增收费、非公开敏感披露或外部高影响操作须另获用户同意。设备兼容、Publisher 和加速效果须有实测证据；不默认 GitHub Actions 或 Drive 同步，也不自动升级旧项目固定协议。

**口令：** `推进架构师工作` / `推进导师工作` / `推进工程师工作`。每轮开始执行[角色恢复](../../../../workflows/ROLE_RECOVERY.md)，结束给出[下一步](../../../../workflows/NEXT_ACTION.md)；如实标记 PASS / FAIL / NOT RUN / BLOCKED 和源码 SHA。
