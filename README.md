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

### Windows 安装 (install.ps1) - 推荐

PowerShell 脚本统一支持**系统级别**和**项目级别**安装：

```powershell
# 查看可用 skills
.\install.ps1 -List

# 查看可用 skill 文件夹
.\install.ps1 -ListFolders

# ========== 系统级别安装 ==========
# 安装所有 skills 到系统目录（所有 Agent）
.\install.ps1 -System -All

# 安装所有 skills 到特定 Agent（如 Kimi）
.\install.ps1 -System -Agent kimi -All

# 从特定文件夹安装（如 fe-skills）
.\install.ps1 -System -Folder fe-skills -All

# 安装指定 skills 到系统
.\install.ps1 -System -Skills "github-task-workflow","local-workflow"

# ========== 项目级别安装 ==========
# 安装所有 skills 到当前项目
.\install.ps1 -Project -All

# 从特定文件夹安装到当前项目
.\install.ps1 -Project -Folder fe-skills -All

# 安装指定 skills 到当前项目
.\install.ps1 -Project -Skills "github-task-workflow"
```

### Linux/macOS 安装 (install.sh)

统一支持**系统级别**和**项目级别**安装：

```bash
# 查看可用 skills
./install.sh --list

# ========== 系统级别安装 ==========
# 安装所有 skills 到系统目录（所有 Agent）
./install.sh --system --all

# 安装所有 skills 到特定 Agent（如 Kimi）
./install.sh --system --agent kimi --all

# 安装指定 skills 到系统
./install.sh --system github-task-workflow local-workflow

# ========== 项目级别安装 ==========
# 安装所有 skills 到当前项目
./install.sh --project --all

# 安装指定 skills 到当前项目
./install.sh --project github-task-workflow
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

### `innate-frontend`（fe-skills/）

统一的 Web 前端开发 Skill，基于 `@innate/ui` 组件库。

**核心能力**：
- **57+ 基础 UI 组件**：Button、Card、Dialog、Table 等（基于 Radix UI + Tailwind CSS v4）
- **7 个 Landing 区块**：Hero、Features、Pricing、FAQ、Stats、Testimonials、CTA
- **业务区块**：Auth、Mail、Chat
- **OKLCH 主题系统**：语义化色彩变量，支持亮/暗模式
- **项目验证规则**：CSS/Tailwind/React 配置自动检查
- **shadcn/ui 升级策略**

详见：[fe-skills/innate-frontend/SKILL.md](fe-skills/innate-frontend/SKILL.md)

### `desktop-app`（fe-skills/）

使用 Tauri 2 + Next.js 构建跨平台桌面/Web 应用，是 `innate-frontend` 的超集。

**可选模块**：PTY 终端、AI 聊天集成、教程/课程系统

详见：[fe-skills/desktop-app/SKILL.md](fe-skills/desktop-app/SKILL.md)

安装前端技能：`./install.sh --system --folder fe-skills --all`

## 仓库结构

```
spark-skills/
├── README.md                          # 本文件
├── SETUP.md                           # 仓库构建过程文档
├── install.sh                         # 统一安装脚本（支持 --folder/--system/--project）
├── install-skills.sh                  # 旧版安装脚本
├── docs/                              # 详细文档
│   ├── README.md                      # 文档索引
│   ├── Agents.md                      # 支持的 AI Agent 工具介绍
│   ├── ai-coding-tools-guide.md       # AI 编程工具配置指南
│   ├── spec/                          # 协议和规范定义
│   └── usage/                         # 使用指南
├── dev/                               # 开发工作流 Skills
│   ├── git-workflow/                  #   GitHub Issue 任务工作流
│   ├── local-workflow/                #   本地任务工作流
│   ├── github-cli-skill/              #   GitHub CLI 工具
│   ├── gh-create-release/             #   GitHub Release 创建
│   ├── ai-config/                     #   AI Provider 一键配置
│   ├── spark-task-init-skill/         #   任务目录初始化
│   └── scanning-for-secrets/          #   安全扫描
├── fe-skills/                         # 前端开发 Skills
│   ├── innate-frontend/               #   Web 前端开发（@innate/ui）
│   ├── desktop-app/                   #   桌面应用开发（Tauri + Next.js）
│   └── beginner/                      #   入门教程
├── product/                           # 产品设计 Skills
│   ├── prd-writer-skill/              #   PRD 撰写
│   └── project-analysis-skill/        #   项目分析设计
├── backend-skills/                    # 后端开发 Skills
│   └── golang-cli-app/                #   Go CLI 应用开发
├── mattprocock-skills/                # 第三方 Skills（社区贡献）
├── tasks/                             # 任务管理目录
│   ├── issues/                        #   任务定义文件
│   ├── features/                      #   功能特性任务
│   ├── tracing/                       #   执行追踪记录
│   └── done/                          #   已完成任务
└── .claude/skills/                    # Claude Code 项目级 Skills（符号链接）
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
