# SAE 算法项目 AGENTS 模板（中文说明）

> [英文目标根目录模板](../../../../examples/project/AGENTS.md) · 这里仅供理解，实际项目复制英文版本到**目标仓库根目录**并填写真实信息。中文模板放在固定 `.sae/i18n/zh-CN/examples/project/AGENTS.zh-CN.md`。

**项目：** `<OWNER>/<PROJECT>` · **研究目标：** `<PAPER_OR_ALGORITHM>`  
**Python 包名：** `<PACKAGE_NAME>` · **Framework V3.2 固定 SHA：** `<ACTUAL_40_CHARACTER_FRAMEWORK_SHA>`

## 每轮恢复工作

先读目标根 `AGENTS.md`/`sae.yaml`、固定 `.sae/AGENTS.md`、本角色 `.sae/protocols/`、[角色恢复与下一步](.sae/workflows/ROLE_RECOVERY.md)以及真实 GitHub Issue/PR/证据。口令 `推进导师工作` / `推进架构师工作` / `推进工程师工作` 只执行一个有边界周期。不能只凭 URL 假装已读，不能静默升级固定快照。

## 三阶段研究与工程关口

1. Mentor 和 Scientist 先按 [数学研究](.sae/workflows/MATHEMATICAL_RESEARCH.md)生成 `docs/research/<algorithm>-tensorization.md`，Scientist 批准 `RESEARCH_READY` 或明确有限例外，才启动算法工程。
2. Architect 根据 [PyTorch 生态调查](.sae/workflows/ECOSYSTEM_REVIEW.md)设计 Build-vs-Reuse、数学数值基线与 CPU 验收。Codex 实际运行 CPU oracle/边界/回归、适用编译、固定 SHA 干净安装和 CLI 测试，提交未合并 PR。
3. Architect 通过 [GPU Readiness](.sae/templates/GPU_READINESS.md)后 Scientist 使用 [Colab 三步](.sae/workflows/GPU_EXPERIMENT.md)：固定 SHA 安装 → 独立 Benchmark → 查看结果后可选独立上传（Colab Secret `GITHUB_TOKEN`）。没有实际测试不能声称 CLI 或 GPU 已通过。
4. 维护数学、工程、实验三份成果的 [交接链接](.sae/workflows/THREE_ARTIFACT_HANDOFF.md)。

## 全部本人公开仓库的无限期合并权限

请核对 [Framework 中央最新授权](https://github.com/JohnnyZPiggy/SAE-Framework/blob/main/governance/STANDING_AUTHORIZATION.md)。Scientist 已授权 GPT Architect 在 `JohnnyZPiggy` 当前及未来**实际拥有的全部公开仓库**审核后自主决定合并，不需逐仓库登记或逐 PR 再申请。**固定快照不会创建平台权限**；需真实 GitHub owner/public、连接合并权限、完整 Diff/测试以及科学家负责的科研与安全实质决定；本项目更严格的限制仍有效。私有/他人仓库不在该授权范围，Codex 不自我合并。

默认无 GitHub Actions、无 Drive 同步、无明文密钥、无强推/未授权主分支写入、无后台代理。真正的证据和交接写入 GitHub。
