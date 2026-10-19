# 【SAE 工程任务】<简短标题>

> 语言：[English](../../../templates/ISSUE_TEMPLATE.md) | **简体中文**

**负责人：** Codex / Architect / Scientist  
**优先级：** P0 / P1 / P2  
**状态：** ready / in-progress / review / experiment / blocked / accepted  
**类型：** math / engineering / experiment / learning  
**依赖：** #<Issue 编号>（无则填写 none）

## 科学目的
这个任务解决什么数学或工程问题？为什么值得做？

## 数学结构研究前置审核
**研究报告：** `docs/research/<algorithm>-tensorization.md` / 链接  
**科学家决策：** RESEARCH_READY / 明确批准的有限例外  
**矩阵向量 / 张量化结构与限制：** <概述>  
*仅做仓库初始化的任务可以标记不适用。*

## 数学与数值契约
定义、假设、参考基线、不变量、输入输出形状、dtype/设备要求、数值容差。

## 交付内容
- [ ] 独立的 Python 模块 / CLI / 设计说明
- [ ] 数值测试与 Benchmark 代码
- [ ] 文档和可复现运行命令

## Colab 三步交付关口（算法任务）
- [ ] 从指定精确源码 SHA 安装包，独立 Benchmark CLI 正常运行
- [ ] 可选独立 Publisher 只读取已有报告目录，不重跑 GPU
- [ ] Codex 真实运行 CPU 数值、打包/CLI 与 Publisher Mock 测试
- [ ] 科学家 GPU 与可选上传：未真实执行必须写 **NOT_RUN**
- [ ] 核对被测 SHA、异常处理及 Secret `GITHUB_TOKEN` 安全访问

## 验收条件
- [ ] 数学契约与参考基线一致
- [ ] 指定边界和正确性测试
- [ ] 真实 CPU 验证已记录
- [ ] GPU 相关任务使用候选源码 SHA 在 Colab 测试
- [ ] 无 GitHub Actions、无密钥泄露

## 任务交接
目标分支、PR/实验报告、遗留问题与阻塞。