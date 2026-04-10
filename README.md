# Spark Skills

个人习惯的 AI Agent Skill 仓库，统一收集、管理和分发适配多种 AI 编程助手的 Skills。

## 支持的 AI Agent

本仓库中的 Skill 力求兼容以下 Agent 工具：

| Agent | 配置文件位置 | 说明 |
|-------|-------------|------|
| **Claude Code** | `~/.claude/skills/` | 通过 `SKILL.md` 自动识别 |
| **Kimi CLI** | `~/.kimi/skills/` 或 Kimi 内置 skills | 通过 `SKILL.md` 自动识别 |
| **Codex** | `~/.codex/skills/` (或项目目录) | 通过 `SKILL.md` 自动识别 |
| **OpenCode** | `~/.opencode/skills/` (或项目目录) | 通过 `SKILL.md` 自动识别 |

> 所有 Skill 均以标准 `SKILL.md` 作为入口，并辅以 Python 脚本和参考文档。

## 快速安装

### 新安装脚本 (install-v2.sh) - 推荐

统一支持**系统级别**和**项目级别**安装：

```bash
# 查看可用 skills
./install-v2.sh --list

# ========== 系统级别安装 ==========
# 安装所有 skills 到系统目录（所有 Agent）
./install-v2.sh --system --all

# 安装所有 skills 到特定 Agent（如 Kimi）
./install-v2.sh --system --agent kimi --all

# 安装指定 skills 到系统
./install-v2.sh --system github-task-workflow local-workflow

# ========== 项目级别安装 ==========
# 安装所有 skills 到当前项目
./install-v2.sh --project --all

# 安装指定 skills 到当前项目
./install-v2.sh --project github-task-workflow
```

**系统级别安装位置**：
- `~/.config/agents/skills/` (通用)
- `~/.claude/skills/` (Claude Code)
- `~/.kimi/skills/` (Kimi CLI)
- `~/.codex/skills/` (Codex)
- `~/.opencode/skills/` (OpenCode)

**项目级别安装位置**：
- `./.agents/skills/` (通用)
- `./.kimi/skills/` (Kimi CLI)
- `./.claude/skills/` (Claude Code)
- 自动创建 `.kimi/KIMI.md` 项目配置
- 自动创建 `tasks/` 目录

### 旧安装脚本 (install.sh) - 仅系统级别

```bash
# 安装所有 skills 到 Claude Code
./install.sh claude-code

# 安装所有 skills 到 Kimi
./install.sh kimi
```

### 手动链接

```bash
# 以 Claude Code 为例
ln -s $(pwd)/github-task-workflow ~/.claude/skills/github-task-workflow
```

## 已包含 Skills

### `github-task-workflow`

通过 GitHub Issues 管理任务全生命周期：从任务创建、实现跟踪到提交完成总结。

> **注意**：这是一个 AI Agent Skill，支持三种使用方式：
> 1. **普通对话模式（推荐）**：直接说"请执行 tasks/xxx.md"
> 2. **普通对话模式**：直接说"执行 `tasks/xxx.md`"
> 3. **编排器模式（跨 Agent）**：`python scripts/orchestrate.py init tasks/xxx.md`，然后 AI 实现，再 `python scripts/orchestrate.py finish`

**核心能力**：
- **创建 Issue**：`python scripts/create_issue.py --title "..." --body "..."`
- **更新 Issue**：`python scripts/update_issue.py --issue 123 --comment "..."`
- **跨 Agent 编排器**：`python scripts/orchestrate.py init/finish/status/abort`
- **自动仓库检测**：支持从 git remote 自动推断 `owner/repo`
- **多级配置**：支持命令行参数、环境变量、项目级配置、全局配置

**自定义 Agent（强制工作流）**：
```bash
kimi --agent-file github-task-workflow/agent/kimi-agent.yaml
```

详见：[github-task-workflow/SKILL.md](github-task-workflow/SKILL.md)

### `spark-task-init`

为 spark-cli 初始化任务目录结构的 Skill。

**功能**：
- 创建任务目录结构（tasks/features/, tasks/config/ 等）
- 创建示例特性模板文件
- 可在任意目录执行

**使用方式**：
```bash
# 方式一：使用 spark 命令
spark task init

# 方式二：使用 skill 直接执行
kimi --agent-file spark-task-init-skill/SKILL.md
```

详见：[spark-task-init-skill/SKILL.md](spark-task-init-skill/SKILL.md)

### `ai-config`

一键配置 AI Agent Provider 到各种 AI 编程工具。

**两种配置方式**：
- **方式 A（推荐）**：`npx @z_ai/coding-helper` 一键配置 GLM
- **方式 B**：复制预置模板文件，只需修改 API Key

**支持的工具**：Claude Code、Codex CLI、OpenCode、Cline、OpenClaw

**支持的 Provider**：GLM Coding Plan、OpenRouter、OpenAI、Anthropic

**使用方式**：
```bash
# GLM 一键配置
npx @z_ai/coding-helper

# 或手动复制模板
cp ai-config/templates/codex/glm.toml ~/.codex/config.toml
```

详见：[ai-config/SKILL.md](ai-config/SKILL.md)

### `innate-frontend`

统一的 Web 前端开发 Skill，基于 `@innate/ui` 组件库。

**核心能力**：
- **57 个基础 UI 组件**：Button、Card、Dialog、Table 等（基于 Radix UI + Tailwind CSS v4）
- **7 个 Landing 区块**：Hero、Features、Pricing、FAQ、Stats、Testimonials、CTA
- **业务区块**：Auth（LoginForm）、Mail（Inbox/List/Display）、Chat（Interface/MessageList）
- **OKLCH 主题系统**：语义化色彩变量，支持亮/暗模式
- **Monorepo 架构**：pnpm workspace + 共享包

**触发词**：创建 Web 应用、新建前端项目、使用 innate-ui 组件

**配合使用**：与 `tauri-desktop-app` Skill 配合可构建桌面应用

详见：[innate-frontend/SKILL.md](innate-frontend/SKILL.md)

### `tauri-desktop-app`

使用 Tauri 2 + Next.js 快速搭建跨平台桌面应用。

详见：[tauri-desktop-app/SKILL.md](tauri-desktop-app/SKILL.md)

## 仓库结构

```
spark-skills/
├── README.md                          # 本文件
├── SETUP.md                           # 仓库构建过程文档
├── docs/                              # 详细文档
│   ├── index.md                       # 文档中心首页
│   ├── README.md                      # 文档索引
│   ├── Agents.md                      # 支持的 AI Agent 工具介绍
│   └── ai-coding-tools-guide.md       # AI 编程工具配置指南
├── install.sh                         # 多 Agent 安装脚本
├── github-task-workflow/              # Skill: GitHub 任务工作流
│   ├── SKILL.md                       # Skill 入口（标准格式）
│   ├── scripts/                       # 可执行脚本
│   │   ├── config_loader.py
│   │   ├── create_issue.py
│   │   ├── orchestrate.py
│   │   ├── task_watcher.py
│   │   └── update_issue.py
│   └── references/                    # 详细参考文档
│       ├── workflow.md
│       ├── automation-hooks.md
│       └── full-auto-roadmap.md
├── spark-task-init-skill/             # Skill: spark task 初始化
│   └── SKILL.md                       # Skill 入口
├── ai-config/                         # Skill: AI Provider 配置
│   ├── SKILL.md                       # Skill 入口
│   └── templates/                     # 各工具配置模板
│       ├── claude-code/               # Claude Code 模板
│       ├── codex/                     # Codex CLI 模板
│       ├── opencode/                  # OpenCode 模板
│       ├── cline/                     # Cline 配置说明
│       └── openclaw/                  # OpenClaw 配置片段
├── innate-frontend/                   # Skill: Web 前端开发（@innate/ui）
│   ├── SKILL.md                       # Skill 入口
│   └── references/                    # 参考文档
│       ├── component-catalog.md       # 组件清单
│       └── theme-system.md            # 主题系统说明
├── tauri-desktop-app/                 # Skill: Tauri 桌面应用开发
│   ├── SKILL.md                       # Skill 入口
│   └── templates/                     # 项目模板
└── ...                                # 未来添加更多 skills
```

## 添加新 Skill

1. 在仓库根目录创建新文件夹，命名即为 skill 名称
2. 编写 `SKILL.md`，包含标准的 YAML frontmatter：

```yaml
---
name: your-skill-name
description: 一句话描述该 skill 的用途和触发场景
supported_agents:
  - claude-code
  - kimi
  - codex
  - opencode
---
```

3. 在 `SKILL.md` 同级目录下按需创建 `scripts/`、`references/` 等子目录
4. 更新本 README 的 Skill 列表
5. 运行 `./install.sh <agent>` 将新 skill 同步到对应 Agent

## 设计原则

- **单一入口**：每个 skill 只有一个 `SKILL.md`，降低维护成本
- **无外部强依赖**：优先使用标准库或系统自带工具
- **脚本自解释**：所有 Python 脚本均内置 `--help`
- **配置分层**：支持 CLI > 环境变量 > 项目配置 > 全局配置的优先级链
