# SAE Framework V3.2 工程路线图

> [English](../../../docs/ROADMAP.md) | 简体中文

**现状：** 已有架构、角色规范和模板，**不等于已实现 CLI**。以真实 GitHub Issue 与测试证据判断完成状态。

## P0 — Bootstrap CLI（Codex，[Issue #2](https://github.com/JohnnyZPiggy/SAE-Framework/issues/2)）

先检查目标仓库，支持 dry-run、保留已有文件；从**同一不可变 Framework SHA**安装完整、自包含的中英文 `.sae/` 规范和目标根 `AGENTS.md`、`sae.yaml`。验收快照链接、配置校验、权限不足和重复初始化。不启用 GitHub Actions，不偷偷升级现有算法项目。

## P0 — 独立 Benchmark 与 Publisher CLI（Codex，[Issue #3](https://github.com/JohnnyZPiggy/SAE-Framework/issues/3)）

打包彼此独立的 `PACKAGE_NAME.benchmarks.run` 和 `PACKAGE_NAME.benchmarks.publish`；Benchmark 不自动上传。Publisher 校验白名单、实际被测 SHA、大小/秘密、幂等性和真实 GitHub PR；使用 Colab Secret `GITHUB_TOKEN` 或实测安全子进程传递方案。Codex 跑 CPU/Mock/干净安装测试；科学家跑真实 GPU、凭证和 PR 集成。未经测试状态为 **NOT IMPLEMENTED / NOT RUN**。

## P1 — Colab 三步体验

**指定 SHA 安装 → GPU Benchmark → 科学家看过结果后可选独立上传**。唯一规范见 [Colab 三步契约](../workflows/COLAB_TWO_COMMAND.md)（历史文件名暂时保留），不再把 `--publish` 放在 Benchmark 里。

## P1/P2 — 可选质量改进

Codex 本地做配置/Markdown 链接校验，不强制 GitHub Actions；可增加简洁 Issue/PR 状态摘要、经过审核的版本迁移指南，不增加 Agent 或数据库。

所有工作要有 Issue、实际证据和架构师审核，不虚报完成。
