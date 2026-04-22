# Tasks 目录

任务管理和追踪目录，用于 git-workflow 和 local-workflow 工作流。

## 子目录

| 目录 | 说明 |
|------|------|
| `issues/` | 任务定义文件（Markdown），描述具体的待执行任务 |
| `features/` | 功能特性任务文件 |
| `tracing/` | 任务执行追踪记录（自动生成，Issue 编号对应） |
| `done/` | 已完成的任务归档 |
| `mindstorm/` | 头脑风暴和概念验证文档 |
| `prd/` | 产品需求文档 |
| `planning/` | 规划文档 |
| `analysis/` | 分析文档 |
| `config/` | 任务配置 |

## 工作流

```
issues/feature.md  →  git-workflow init  →  tracing/issue-N.md  →  执行  →  done/
issues/feature.md  →  local-workflow init  →  tracing/xxx.md    →  执行  →  done/
```

## 使用方式

```bash
# 通过 git-workflow 执行任务
请执行 @tasks/issues/xxx.md Task 1

# 通过 local-workflow 执行任务（无需 GitHub）
请使用 local-workflow 执行 @tasks/issues/xxx.md Task 1
```
