---
name: github-cli
description: 简化版 GitHub CLI 工具，支持仓库创建和 Issue 管理
type: skill
supported_agents:
  - claude-code
  - kimi
  - codex
  - opencode
---

# GitHub CLI Skill

使用 `gh` 命令行工具管理 GitHub 仓库和 Issue。

## 前置要求

需要安装 GitHub CLI 并登录：

```bash
# macOS
brew install gh

# 登录
gh auth login
```

## 常用命令

### 仓库管理

```bash
# 创建新仓库（当前目录）
gh repo create --public --source=. --push

# 创建新仓库（指定名称）
gh repo create my-repo --public --clone

# 查看当前仓库
gh repo view --web
```

### Issue 管理

```bash
# 创建 Issue
gh issue create --title "标题" --body "内容" --label "bug"

# 从文件创建 Issue（文件内容为 body）
gh issue create --title "标题" --body-file ./issue-body.md --label "bug"

# 列出 Issues
gh issue list

# 查看 Issue
gh issue view 123

# 在浏览器打开 Issue
gh issue view 123 --web

# 添加评论
gh issue comment 123 --body "评论内容"

# 关闭 Issue
gh issue close 123

# 重新打开 Issue
gh issue reopen 123
```

## Python 脚本集成

```python
import subprocess

def create_issue(title: str, body: str, labels: list = None):
    """创建 GitHub Issue"""
    cmd = ["gh", "issue", "create", "--title", title, "--body", body]
    if labels:
        for label in labels:
            cmd.extend(["--label", label])
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout.strip()

def create_issue_from_file(title: str, body_file: str, labels: list = None):
    """从文件创建 GitHub Issue（文件内容为 body）"""
    cmd = ["gh", "issue", "create", "--title", title, "--body-file", body_file]
    if labels:
        for label in labels:
            cmd.extend(["--label", label])
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout.strip()

def close_issue(issue_number: int):
    """关闭 Issue"""
    subprocess.run(
        ["gh", "issue", "close", str(issue_number)],
        check=True
    )

def comment_issue(issue_number: int, body: str):
    """添加评论"""
    subprocess.run(
        ["gh", "issue", "comment", str(issue_number), "--body", body],
        check=True
    )
```

## 快速参考

| 操作 | 命令 |
|------|------|
| 创建 Issue | `gh issue create --title "xxx" --body "yyy"` |
| 从文件创建 Issue | `gh issue create --title "xxx" --body-file ./file.md` |
| 关闭 Issue | `gh issue close <number>` |
| 添加评论 | `gh issue comment <number> --body "xxx"` |
| 创建仓库 | `gh repo create --public --source=. --push` |

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
# 仅安装到 Claude Code
./scripts/install.sh --system --agent claude-code

# Windows
.\scripts\install.ps1 -System -Agent claude-code
```
