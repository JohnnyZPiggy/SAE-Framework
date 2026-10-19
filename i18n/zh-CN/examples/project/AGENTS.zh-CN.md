## 算法项目统一执行要求

读取固定版本 `.sae/`。按数学研究 → CPU 工程与 `torch.compile` → 架构师 GPU_READY → 科学家 Colab GPU 的顺序工作；链接数学、工程、实验三份报告。Notebook 最终只有固定 SHA 的 pip 安装和打包 Benchmark CLI 两条命令。CPU 可复现的问题必须先由 Codex 修复，不要反复打断科学家。Publisher 未真实实现和验证不得宣称上传成功。

# SAE 新项目 AGENTS 入口模板（中文说明）

> 语言：[English](../../../../examples/project/AGENTS.md) | **简体中文**

**注意：** 这份文件仅用于中文阅读。实际初始化时应把英文 [AGENTS.md 模板](../../../../examples/project/AGENTS.md) 复制到**目标项目根目录**，填写真实值。不要原样复制母仓库独有的相对语言切换链接；目标项目的中文说明应指向 `.sae/i18n/zh-CN/examples/project/AGENTS.zh-CN.md`。

项目：`<OWNER>/<PROJECT>`  
SAE Framework：`JohnnyZPiggy/SAE-Framework`，架构版本 V3.2  
框架快照：`.sae/`，固定在真实 commit `<REPLACE_WITH_ACTUAL_FRAMEWORK_SHA>`

## 工作前读取
1. 当前项目 `AGENTS.md` 和 `sae.yaml`。
2. `.sae/AGENTS.md` 共同规则。
3. 当前角色 `.sae/protocols/ARCHITECT.md`、`ENGINEER.md` 或 `MENTOR.md`。
4. 相关工作流程、Issue/PR 规格。

**链接不等于自动加载。** 必须确认固定版本本地快照存在；缺失时先执行 Bootstrap，不要猜测规则。

## 数学研究前置关口
在新算法实现和正式 Benchmark 前，读取 `.sae/workflows/MATHEMATICAL_RESEARCH.md`，由 GPT 导师与科学家完成 `docs/research/<algorithm>-tensorization.md` 数学结构与张量化研究，经过 `RESEARCH_READY` 审核或科学家明确例外授权后，总架构师才派发 Codex 工程。张量化研究不保证实际加速。

## 本项目的额外说明
- 科学目标：`<PAPER_OR_ALGORITHM>`
- Python 包名：`<PACKAGE_NAME>`
- 人类科学家运行 Colab GPU；Codex 运行 CPU；GPT 做审查和导师指导。
- GitHub Issues/PR 是共享任务与证据中心。不配置 GitHub Actions，不使用 Drive 同步。
- 计算和报告发布使用经测试的 Python 模块，Notebook 只负责调度。
- 不擅自覆盖文件、发布秘密或自行合并。

## 三条指令
`推进架构师工作` / `推进工程师工作` / `推进导师工作`。
## 每轮必须提示下一步

完成实质性工作后，按固定快照中的 [下一步口令协议](.sae/workflows/NEXT_ACTION.md) 推荐一个最优口令、最多两个备选，注明 GitHub 证据与科学家审批要求；不得虚报本地执行或 GPU 就绪。

## 先恢复角色与项目状态

每次实质性工作前读取固定的 [角色恢复协议](.sae/workflows/ROLE_RECOVERY.md)，核对用户口令、项目 Issue/PR、阶段关口和实际工具权限；不得悄悄换角色、假装已连接笔记本或升级固定快照。结束后使用 [下一步口令](.sae/workflows/NEXT_ACTION.md)。

## 架构设计前的生态调查

架构师向 Codex 派单前，按固定版本 [生态评估协议](.sae/workflows/ECOSYSTEM_REVIEW.md) 检查 PyTorch 原生功能、第三方包与论文参考实现，在工程报告中说明 Build-vs-Reuse 方案；坚持 CPU-first、跨硬件和少依赖，不自动升级固定 SAE 快照。
