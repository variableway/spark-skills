---
name: git-workflow
description: |
  基于 github-cli-skill 的 GitHub Issue 工作流 Skill。
  输入任务描述 → 创建 Issue → Agent 执行任务（含测试）→ 关闭 Issue 并将完成消息追加到首条评论。
type: skill
supported_agents:
  - claude-code
  - kimi
  - codex
  - opencode
---

# Git Workflow

基于 [github-cli-skill](../github-cli-skill/SKILL.md) 构建的 Issue 管理工作流。

## 工作流步骤

```mermaid
flowchart TD
    BEGIN([BEGIN]) --> INIT[运行 orchestrate.py init 创建 Issue]
    INIT --> COMMENT[首条评论写入任务描述]
    INIT --> IMPLEMENT[Agent 执行任务并测试]
    IMPLEMENT --> FINISH[运行 orchestrate.py finish]
    FINISH --> APPEND[将完成消息追加到首条评论末尾]
    APPEND --> CLOSE[关闭 Issue]
    CLOSE --> END([END])
```

### 步骤说明

1. **INIT** — 创建 Issue
   - 运行：`python git-workflow/scripts/orchestrate.py init --title "标题" --description "任务描述"`
   - 创建 GitHub Issue
   - 将任务描述作为**首条评论**写入
   - 保存工作流状态到 `.git-workflow.state.json`

2. **IMPLEMENT** — Agent 执行任务
   - 根据任务描述执行代码修改
   - 运行测试并修复问题

3. **FINISH** — 关闭 Issue
   - 运行：`python git-workflow/scripts/orchestrate.py finish --message "完成总结"`
   - **追加**完成消息到首条评论末尾（不覆盖原内容）
   - 关闭 Issue
   - 清理状态文件

## 前置要求

需要安装 GitHub CLI 并登录：

```bash
# macOS
brew install gh

# Linux
# 参见 https://github.com/cli/cli#installation

# 登录
gh auth login
```

## 脚本说明

### 创建 Issue

```bash
python git-workflow/scripts/create_issue.py \
  --title "实现登录功能" \
  --description "需要实现用户登录功能，包括..." \
  --labels "task,enhancement"
```

| 参数 | 说明 |
|------|------|
| `--title` | Issue 标题（必填） |
| `--description` | 任务描述，会写入首条评论（必填） |
| `--labels` | 逗号分隔的标签，默认 `task` |
| `--repo` | 手动指定仓库 `owner/repo`，不填则自动检测 |
| `--remote` | 指定 git remote，默认 `origin` |

### 关闭 Issue（追加评论）

```bash
python git-workflow/scripts/close_issue.py \
  --message "已完成登录功能实现。修改了 src/auth.py，添加了 JWT 验证。"
```

| 参数 | 说明 |
|------|------|
| `--message` | 追加到首条评论的完成消息（必填） |
| `--issue` | Issue 编号（覆盖状态文件） |
| `--repo` | 仓库（覆盖状态文件） |

**重要**：`--message` 会被追加到首条评论的末尾，**不会**覆盖原始任务描述。

### 编排器

```bash
# 初始化工作流
python git-workflow/scripts/orchestrate.py init \
  --title "任务标题" \
  --description "任务描述"

# 查看状态
python git-workflow/scripts/orchestrate.py status

# 完成工作流
python git-workflow/scripts/orchestrate.py finish \
  --message "任务已完成。测试通过。"

# 中止工作流（不关闭 Issue）
python git-workflow/scripts/orchestrate.py abort
```

## 快速参考

| 操作 | 命令 |
|------|------|
| 创建工作流 | `python scripts/orchestrate.py init --title "..." --description "..."` |
| 完成工作流 | `python scripts/orchestrate.py finish --message "..."` |
| 查看状态 | `python scripts/orchestrate.py status` |
| 中止工作流 | `python scripts/orchestrate.py abort` |

## 安装

### 项目级安装

```bash
# macOS / Linux
./scripts/install.sh --project

# Windows PowerShell
.\scripts\install.ps1 -Project
```

### 系统级安装

```bash
# macOS / Linux
./scripts/install.sh --system

# Windows PowerShell
.\scripts\install.ps1 -System
```

### 指定 Agent

```bash
# 仅安装到 Kimi
./scripts/install.sh --system --agent kimi

# Windows
.\scripts\install.ps1 -System -Agent kimi
```
