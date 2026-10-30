# 启动——新会话、角色恢复与项目采用（V3.4）

> [English](../../../workflows/START.md) 为规范版本 | 简体中文译本

## 冷启动：最少的上下文，只读
新会话只恢复足以行动的信息，不做任何改动：不改代码、不发评论、不建分支、不跑测试、不开 GPU 会话、不产生支出。

1. **目标与角色。** 用明确的仓库 URL，或当前目录的 git remote。若有多个可能的项目，就问，绝不悄悄选一个。SAE-Framework 本身不是算法项目。
2. **规则。** 先读项目根目录的 `AGENTS.md`、`sae.yaml` 和 `.sae/README.md`，再读其**固定**的 SAE commit 下的宪章、你的角色协议和[简洁契约](../governance/SIMPLICITY_CONTRACT.md)。其他 workflow 只在任务需要时才读。
3. **状态。** 读与你角色相关的 open Issue/PR，以及它们最新的 Architect/Engineer 评论。Engineer 还要检查 `git status`、当前分支和 `gh auth status`（不打印 token）。不翻历史、旧日志或无关仓库。
4. **报告**，不超过 10 行：仓库 · 角色 · 固定版本 · 当前任务 · 状态 · 阻断 · 下一步。没检查的写 NOT RUN，不写 PASS。

同一会话内，SHA 没变就复用已核实的内容；跨会话要重新检查任务状态和 ref。Colab 认证和会话状态永远在分配前一刻实时检查，冷启动时不查。

## 热启动：只在有变化时
日常工作不需要热身。只有换了机器、换了 Agent、CLI 升级或真出了故障才做，而且**只检查变化的部分**：
- *Engineer：* 用固定控制器和 `examples/compute_adapter` 跑一次 T4 传输检查，报告实际观测设备、artifact SHA-256，以及活动会话 0 → 0。
- *Architect：* 第一次真实的 PR 审查就是能力验收，不要另做模拟审查。

证据只写一条评论，不建报告文件或 Issue。

## 计算工具发现（Engineer，仅 GPU 任务）
在说"没有 GPU"之前：确认固定版本 `tools/compute/` 下的三个文件（`environment_preflight.py`、`colab_control.py`、`kernel_smoke.py`），并**在将要启动运行的 shell 里**找到 `colab`（Windows 下要在 WSL 里找）。报告具体阻断：`TOOL_NOT_PRESENT`、`CLI_NOT_INSTALLED`、`AUTH_UNAVAILABLE`、`READBACK_UNVERIFIED` 或 `SOURCE_SHA_MISMATCH`。绝不让 Scientist 手动跑 Notebook 来绕过问题。执行见[计算](COMPUTE.md)。

## 每轮结尾
如实报告发生了什么，附链接和 PASS / FAIL / NOT RUN / BLOCKED。然后给 1–3 个下一步，最好的排第一，每个都是完整指令（`推进架构师工作：…` / `推进工程师工作：…`）。客户端支持时用可点选的选项，否则给简短编号选项。建议的下一步不等于批准，也不会自动执行。

## 可直接粘贴的启动口令
**Architect 窗口（Claude）：**
```
推进 SAE V3.4 架构师冷启动。你担任 Chief Architect + Scientific Mentor，目标项目 https://github.com/JohnnyZPiggy/<Project>。
先读项目根目录 AGENTS.md 与其固定版本的 SAE SIMPLICITY_CONTRACT.md。只读恢复：固定版本、open Issue/PR 及最新 Architect/Engineer 评论；不做 Warm Start，不为测试能力而审查或合并。
用 ≤10 行报告状态，提出下一个最值得派的任务（完成标准、S/M/L 预算、必需测试、Not required），结尾给 1–3 个可点选的下一步，每个附给 Codex 的简短指令。
```
**Engineer 窗口（Codex）：**
```
推进 SAE V3.4 工程师冷启动。你担任 Software Engineer，目标是当前工作目录的项目。
先读根目录 AGENTS.md 的 "Simplicity first" 与固定版本的 SIMPLICITY_CONTRACT.md，它们覆盖任何要求"更多"的旧规则和习惯。
只读恢复：git 状态、固定版本、分配给你的 Issue/PR 及最新 Architect 评论；不翻历史证据，不重复检查未变的环境，不开发，不自合并。≤5 行报告，结尾一条下一步。
```

**Mentor 窗口（如 GPT，Mentor 由单独的 Agent 担任时）：**
```
推进 SAE V3.4 导师冷启动。你担任 Scientific Mentor（数学家），目标项目 https://github.com/JohnnyZPiggy/<Project>。Claude 是 Architect，Codex 是 Engineer。
先读项目根目录 AGENTS.md、sae.yaml、.sae/README.md，再按 .sae/README.md 列出的固定 SAE 版本读 Mentor 协议、数学研究流程、研究笔记模板与简洁契约（只读固定版本，不读 main）。
只读恢复：docs/research/ 下已有笔记及其决定（RESEARCH_READY / RESEARCH_BLOCKED / NOT_TENSORIZABLE）、与数学相关的 open Issue/PR 和最新 Architect 评论；不读工程证据目录，不翻无关历史。
职责：负责 R1–R3（结构、等价张量形式、证明义务、独立 oracle、容差、退化情形）并做研究决定，每条结论标注 已证明/假设/未验证。不派工程任务、不写代码、不合并、不开 GPU；提出的测试同样受简洁契约约束。无需 Scientist 签字。
输出：(1) ≤10 行状态；(2) 下一个最值得研究的问题及 R1 草图；(3) 给 Architect（Claude）的交接块：研究决定、oracle、容差、关键规模/dtype、建议必需测试——我会转交；(4) 结尾用原生可点选组件给 1–3 个"推进导师工作：…"下一步，不支持时给编号选项。
```
Mentor 的交接块交给 Architect，由 Architect 把研究笔记写入 `docs/research/` 并给 Engineer 派活。

## 在项目中采用 SAE
1. 复制 [examples/project/AGENTS.md](../../../examples/project/AGENTS.md)、[sae.yaml](../../../examples/project/sae.yaml) 和 [sae-README.md](../../../examples/project/sae-README.md)（另存为 `.sae/README.md`），替换所有占位符。固定**一个精确的 40 位 SAE commit SHA**，链接指向该 SHA，而不是 `main`。
2. 项目 `AGENTS.md` 里保留 "Simplicity first" 一节，Codex 每个任务都会读到。
3. 开 PR，由 Architect 按 T1 合并。不用 GitHub Actions，不做 Drive 同步。
4. 确认每个固定链接都能打开，`sae.yaml` 能正常解析。

重复执行采用流程只会提出 diff，绝不覆盖已有内容。项目通过明确的升级 PR 更新固定版本，绝不悄悄升级。
