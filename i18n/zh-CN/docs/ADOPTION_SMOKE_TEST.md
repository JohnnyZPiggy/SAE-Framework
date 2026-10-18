# SAE 子项目初始化冒烟验收（不使用 GitHub Actions）

> 语言：[English](../../../docs/ADOPTION_SMOKE_TEST.md) | **简体中文**

**目的：** 验证 SAE 规则复制到**新算法项目后**仍能工作，而不仅是母仓库的链接正常。这里只定义检查程序，**不代表已经运行测试**。

## 检查 1：操作前审查
1. 选择临时测试仓库或得到明确授权的目标项目，先记录原文件和默认分支。
2. 使用**真实不可变 commit SHA**（或固定 release）锁定 SAE Framework，不能只依赖漂移的 `main`。
3. 先提出待修改计划/分支，不经审查不得覆盖原 `AGENTS.md` 等文件。

## 检查 2：协议副本完整且路径正确

```text
<项目>/
  AGENTS.md                       # 适配目标项目根目录
  sae.yaml                        # 包含真实框架 SHA
  .sae/
    AGENTS.md
    README.md / README.zh-CN.md
    SAE_BOOTSTRAP.md / CHANGELOG.md
    docs/                         # 架构图与相关文档
    examples/                     # 模板关联引用
    protocols/
    workflows/                    # 含 MATHEMATICAL_RESEARCH.md
    templates/                    # 含 TENSORIZATION_STUDY.md
    i18n/zh-CN/                   # 双语导航与文档
```

`.sae/` 必须来自**同一固定版本**。在子项目目录中检查相对路径，防止它们指向缺失的母仓库目录。根 `AGENTS.md` 是**经过适配**的项目入口，需检查项目名称、SHA、角色路径和中文说明的链接。

## 检查 3：用实际指令演练
- **导师：** 新算法执行「推进导师工作」时，应优先研究矩阵向量/张量结构并形成数学研究报告。
- **架构师：** 「推进架构师工作」需要先检查科学家批准的研究关口，再派发算法实现 Issue；仓库基础设施可先准备。
- **工程师：** 「推进工程师工作」要真正找到开放任务。若 `agent:codex`、`status:ready` 标签不存在，须检查 Issue 标题/正文中的负责人及 ready 状态；真正评论领取后才报告已领取。
- **Colab：** GPU 由科学家运行；Publisher 尚未开发完成时只能手动发布，不可宣称自动完成。

## 检查 4：证据和权限
- CPU 测试必须按真实命令与结果记录 `PASS/FAIL/NOT RUN/BLOCKED`。
- 不添加 `.github/workflows/` Actions，不同步 Drive，不向 Git 提交密钥。
- 改动通过可审查 PR，不静默覆盖/合并，不 force-push。

## 输出
列出实际路径、固定 SHA、真实 Issue/PR 链接、完成与未完成项、风险和科学家需要批准的动作。

**说明：** 这是冒烟检查协议，不是已通过测试的证明。
