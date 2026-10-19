# 算法项目 AGENTS 模板（复制到目标仓库根目录）

> [English 模板](../../../../examples/project/AGENTS.md)（正式规范） | 简体中文

这是**待复制的项目模板**；`.sae/` 路径只能在复制到目标算法仓库根目录后解析，不是 Framework 当前示例目录的相对链接。

**项目：** `<OWNER>/<PROJECT>`；**科研目标：** `<PAPER_OR_ALGORITHM>`；**包名：** `<PACKAGE_NAME>`。  
**SAE 固定版本：** `JohnnyZPiggy/SAE-Framework` V3.2，真实不可变 SHA `<ACTUAL_FRAMEWORK_SHA>`，快照 `.sae/`。

## 工作前读取

项目根 `AGENTS.md` 和 `sae.yaml` → 固定 `.sae/AGENTS.md` → 本角色 `.sae/protocols/` → 必需的 `.sae/workflows/`、当前 GitHub Issue/PR/真实 SHA。不可悄悄升级固定快照或仅凭仓库 URL 断言已读取；失败标 UNVERIFIED。

## 项目流程

- 新算法/重大张量改写先有 `docs/research/<algorithm>-tensorization.md` 与 Scientist `RESEARCH_READY`（或明确有限例外），才给 Codex 派单。
- Architect 简短调查 PyTorch 生态 REUSE/ADAPT/BUILD；Codex 真实执行 CPU oracle/边界/回归、支持时 `torch.compile`、干净安装与 CLI 测试；架构师审核 GPU_READY。
- Scientist Colab 三步：固定 SHA 安装 → Benchmark → **检查后可选独立上传**，Secret 名为 `GITHUB_TOKEN`。参考固定 `.sae/workflows/COLAB_TWO_COMMAND.md`（历史文件名）。不能把 CPU 通过冒充 GPU，Notebook 不写内核。
- 三份科研证据关联 GitHub Issue/PR；不启用 GitHub Actions 或 Drive 同步。

## 口令与权限

`推进导师工作` / `推进架构师工作` / `推进工程师工作` 每次只运行一个有边界周期，按固定 `ROLE_RECOVERY.md` / `NEXT_ACTION.md` 执行。

科学家对 `JohnnyZPiggy` **现在和未来本人拥有的全部公开仓库**授予 GPT 无限期、可撤销的最终合并裁量权，无需逐仓库登记或逐次请示；见 [Framework 当前授权](https://github.com/JohnnyZPiggy/SAE-Framework/blob/main/governance/STANDING_AUTHORIZATION.md)。仍须实时核实 owner/public、平台权限、真实 PR 证据及 Scientist 负责的实质决定。复制模板不产生 GitHub 权限；Codex 不自我合并，也不后台运行。

复制前填写占位符，并在**目标仓库真实目录**检查链接，不覆盖未经审核的现有文件。
