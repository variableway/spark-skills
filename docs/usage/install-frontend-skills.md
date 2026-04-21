# Frontend Skills 安装指南

本指南介绍如何安装和使用 Spark Skills 中的前端开发技能：`innate-frontend`（Web 应用）和 `desktop-app`（桌面应用）。

## 技能概览

| 技能 | 用途 | 技术栈 |
|------|------|--------|
| **innate-frontend** | Web 应用开发 | Next.js 16, React 19, TypeScript, Tailwind CSS v4, @innate/ui |
| **desktop-app** | 桌面/Web 应用开发 | Tauri 2.x, Next.js 16, React 19, TypeScript, @innate/ui + Rust |

> `desktop-app` 是 `innate-frontend` 的超集 — 它包含前端技能的所有 UI 规范，并增加了 Tauri 桌面层和 Rust 后端。可选模块包括 PTY 终端、AI 聊天集成和教程系统。

## 安装

### 系统级安装（推荐）

为所有支持的 Agent 安装前端技能：

```bash
cd ~/innate/spark-skills

# 安装所有 fe-skills
./install.sh --system --folder fe-skills --all

# 或安装特定技能
./install.sh --system --folder fe-skills innate-frontend desktop-app
```

为特定 Agent 安装：

```bash
# 仅安装到 Claude Code
./install.sh --system --agent claude-code --folder fe-skills --all

# 仅安装到 Kimi
./install.sh --system --agent kimi --folder fe-skills --all

# 仅安装到 Codex
./install.sh --system --agent codex --folder fe-skills --all

# 仅安装到 OpenCode
./install.sh --system --agent opencode --folder fe-skills --all
```

### 项目级安装

将技能安装到当前项目中：

```bash
./install.sh --project --folder fe-skills --all
```

### 查看可用技能

```bash
# 列出所有文件夹
./install.sh --list-folders

# 列出 fe-skills 文件夹中的技能
./install.sh --folder fe-skills --list
```

## 安装路径

系统级安装会在以下目录创建符号链接：

| Agent | 路径 |
|-------|------|
| 通用 | `~/.config/agents/skills/` |
| Claude Code | `~/.claude/skills/` |
| Kimi CLI | `~/.kimi/skills/` |
| Codex CLI | `~/.codex/skills/` |
| OpenCode | `~/.opencode/skills/` |

## 验证安装

```bash
ls -la ~/.claude/skills/ | grep -E "innate-frontend|desktop-app"
```

应显示两个符号链接指向 `spark-skills` 仓库中的对应目录。

## 使用

### 创建 Web 应用

在 Agent 对话中触发 `innate-frontend` 技能：

> "使用 innate-frontend 创建一个新的 Web 应用项目"

技能提供：
- 57+ `@innate/ui` 组件
- 7 个 Landing 区块 + Auth/Mail/Chat 业务区块
- OKLCH 颜色主题系统
- 项目验证规则
- shadcn/ui 升级策略

### 创建桌面应用

在 Agent 对话中触发 `desktop-app` 技能：

> "使用 desktop-app 创建一个桌面应用"
> "创建一个带侧边栏和终端的 Tauri 桌面应用"

技能提供：
- Tauri v2 IPC 通信模式
- PTY 终端集成（可选）
- AI 聊天集成（可选）
- 教程/课程系统（可选）
- 状态持久化（Zustand + Tauri Store）
- 完整的项目脚手架

## 技能选择指南

```
只需要 Web 应用？        → innate-frontend
需要桌面应用？           → desktop-app（已包含前端规范）
Web + 桌面都需要？       → 同时安装两个（desktop-app 引用 innate-frontend 的 UI 规范）
```

## 更新技能

由于使用符号链接安装，更新只需拉取最新代码：

```bash
cd ~/innate/spark-skills
git pull
```

所有 Agent 的技能会自动更新。

## 卸载

移除符号链接即可：

```bash
rm ~/.claude/skills/innate-frontend ~/.claude/skills/desktop-app
rm ~/.kimi/skills/innate-frontend ~/.kimi/skills/desktop-app
rm ~/.codex/skills/innate-frontend ~/.kimi/skills/desktop-app
rm ~/.opencode/skills/innate-frontend ~/.kimi/skills/desktop-app
```
