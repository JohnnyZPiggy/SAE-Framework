# SAE Agent Warm Start — 角色能力热身（V3.3）

> [English](../../../workflows/AGENT_WARM_START.md) 为权威协议 | 简体中文

Warm Start 是**冷启动完成后用户按需调用的有界实际能力测试**，不是新的审批、独立 Agent、周期考试或日常任务准入。复用已核实的身份、项目、SHA 和工具信息，不重复全文读取。

## 模式
- **Standard（默认）**：每角色做一次实际代表性任务，不默认分配 GPU。
- **Full（明确指定）**：增加跨角色证据交接；Engineer 在本环境支持、已有认证和权益的条件下，做**一次真实有界 GPU 冒烟**。无需 Scientist 逐次算力审批，但须遵守服务端实际限制和会话清理。

## Chief Architect
选一项实际 Issue/PR，核对精确 head/base SHA、diff、架构和已有测试证据，做出可执行的接受/修改意见，产出 Engineer 最小任务。Full 按常设授权模拟合并决策，**不为了证明能力而真的合并**；权限按具体操作核实。

## Scientific Mentor
选一个真实算法问题，独立推导重要恒等式/张量结构，说明维度、假设、数值稳定与失败情形；用可信来源或独立小算例交叉核对，提出具有容差的最小 Oracle。区分已证明、已观察、假设；Full 补充 Engineer 可执行 CPU/GPU 测试规格。不强制增加科研文档。

## Software Engineer
优先使用 Scientist 指定工作区，**明确允许 D 盘 Dropbox 同步目录**存储 scratch、缓存、结果与测试；核实实际运行环境、Git/gh、现有 Python/PyTorch 依赖。使用隔离任务目录完成小型 CPU 正确性测试，核实真实写入位置、清理自己产生的可丢弃文件并避免 Git 意外追踪。不默认重装、不全盘扫描、不悄悄把大量临时文件写入 C 盘。

**Full GPU：** 复用固定 SAE Controller/Colab CLI，在真实分配前检查已认证状态、额度、现有会话、固定 SHA 与有界超时；默认至多一个会话。运行小规模 PyTorch 计算、CPU/参考正确性对照并记录真实 GPU 型号；下载结果验证字节数、身份和 SHA-256，停止并核实会话释放。证据放用户指定工作区，安全清理任务自产生的临时文件。标记 PROBE_ONLY，不当作正式算法加速结论。不新增付费、凭证或系统账号设置。无可用 GPU 时记录明确阻断，但**不得阻断独立 CPU/数学研究**。

## 交接与完成
每个能力只测一次；Architect/Mentor 复用 Engineer 的实测证据。只在环境、源码或任务权限实质变化时补充相关检查，远端分配前仍刷新动态状态。默认在对话里返回一份精简能力矩阵；需要跨 Agent 接力时可写当前 Issue/PR，不为热身单独创建额外文件。记录角色、环境、源码 SHA、PASS/FAIL/NOT RUN/BLOCKED、证据、临时目录残留、GPU 会话清理和下一项任务。

## 一句话热身口令
- **Architect + Mentor：** “推进 SAE Full Warm Start，担任 Chief Architect + Scientific Mentor，目标 <repo>；复用冷启动状态，审查真实变更、推导实际数学问题并产出 Engineer 验证任务，热身本身不合并 PR。”
- **Engineer：** “推进 SAE Full Warm Start，担任 Software Engineer，目标当前 Git 仓库；优先 D 盘 Dropbox 工作区完成 CPU 测试，已有权益及技术条件允许时通过固定 Colab CLI 做一次 GPU 冒烟、哈希校验与会话释放核查，报告真实证据。”

项目固定协议、[计算实验](../../../workflows/GPU_EXPERIMENT.md)、[工程师计算工具](../../../workflows/ENGINEER_COMPUTE_DISCOVERY.md)、[常设授权](../../../governance/STANDING_AUTHORIZATION.md)和用户最新指令继续适用。
