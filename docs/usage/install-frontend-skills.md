# Frontend Skills 安装指南

本指南介绍如何安装和使用 Spark Skills 中的前端开发技能：`innate-frontend`（Web 应用）和 `tauri-desktop-app`（桌面应用）。

## 技能概览

| 技能 | 用途 | 技术栈 |
|------|------|--------|
| **innate-frontend** | Web 应用开发 | Next.js 16, React 19, TypeScript, Tailwind CSS v4, @innate/ui |
| **tauri-desktop-app** | 桌面应用开发 | Tauri 2.x, Next.js 16, React 19, TypeScript, shadcn/ui |

## 安装

### 系统级安装（推荐）

为所有支持的 Agent 同时安装两个技能：

```bash
cd ~/innate/spark-skills
./install.sh --system innate-frontend tauri-desktop-app
```

为特定 Agent 安装：

```bash
# 仅安装到 Claude Code
./install.sh --system --agent claude-code innate-frontend tauri-desktop-app

# 仅安装到 Kimi
./install.sh --system --agent kimi innate-frontend tauri-desktop-app

# 仅安装到 Codex
./install.sh --system --agent codex innate-frontend tauri-desktop-app

# 仅安装到 OpenCode
./install.sh --system --agent opencode innate-frontend tauri-desktop-app
```

### 项目级安装

将技能安装到当前项目中：

```bash
./install.sh --project innate-frontend tauri-desktop-app
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

检查技能是否正确链接：

```bash
# 检查 Claude Code
ls -la ~/.claude/skills/ | grep -E "innate-frontend|tauri-desktop-app"

# 检查 Kimi
ls -la ~/.kimi/skills/ | grep -E "innate-frontend|tauri-desktop-app"

# 检查 Codex
ls -la ~/.codex/skills/ | grep -E "innate-frontend|tauri-desktop-app"

# 检查 OpenCode
ls -la ~/.opencode/skills/ | grep -E "innate-frontend|tauri-desktop-app"
```

每个命令应显示两个符号链接指向 `spark-skills` 仓库中的对应目录。

## 使用

### 创建 Web 应用

在 Agent 对话中触发 `innate-frontend` 技能：

> "使用 innate-frontend 创建一个新的 Web 应用项目"
> "创建一个包含登录页和仪表板的 Web 应用"

技能提供：
- 57+ `@innate/ui` 组件（Button, Card, Dialog, Table 等）
- 7 个 Landing 区块（Hero, Features, Pricing, FAQ, Stats, Testimonials, CTA）
- 业务区块：Auth, Mail, Chat
- OKLCH 颜色主题系统

### 创建桌面应用

在 Agent 对话中触发 `tauri-desktop-app` 技能：

> "使用 tauri-desktop-app 创建一个桌面应用"
> "创建一个带侧边栏的 Tauri 桌面应用"

技能提供：
- 56+ shadcn/ui 组件
- 桌面布局模板（AppShell, AppSidebar, StatusBar）
- Tauri IPC 通信模式
- 平台检测逻辑
- 完整的项目脚手架模板

## 技能选择指南

```
需要 Web 应用？ → innate-frontend
需要桌面应用？ → tauri-desktop-app
两者都需要？   → 同时安装两个技能
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
# 移除 Claude Code 中的前端技能
rm ~/.claude/skills/innate-frontend ~/.claude/skills/tauri-desktop-app

# 移除 Kimi 中的前端技能
rm ~/.kimi/skills/innate-frontend ~/.kimi/skills/tauri-desktop-app

# 移除 Codex 中的前端技能
rm ~/.codex/skills/innate-frontend ~/.codex/skills/tauri-desktop-app

# 移除 OpenCode 中的前端技能
rm ~/.opencode/skills/innate-frontend ~/.opencode/skills/tauri-desktop-app
```
