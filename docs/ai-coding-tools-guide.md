# AI 编程工具配置指南

本文档介绍如何配置和使用各种 AI 编程助手工具，以及如何通过 `ai-config` Skill 快速配置 Provider。

## 目录

- [1. 快速配置（推荐）](#1-快速配置推荐)
- [2. Claude Code 配置指南](#2-claude-code-配置指南)
- [3. Codex CLI 配置指南](#3-codex-cli-配置指南)
- [4. OpenCode 配置指南](#4-opencode-配置指南)
- [5. 其他工具配置](#5-其他工具配置cline-openclaw)
- [6. 智谱 GLM Coding Plan](#6-智谱-glm-coding-plan)
- [7. 工具对比与选择建议](#7-工具对比与选择建议)

---

## 1. 快速配置（推荐）

### 使用 ai-config Skill

本项目提供了 `ai-config` Skill，支持两种配置方式：

**方式 A：自动安装（GLM 推荐）**

```bash
npx @z_ai/coding-helper
```

一条命令完成 GLM Coding Plan 的安装和配置。

**方式 B：模板复制**

```bash
# Claude Code + GLM
source ai-config/templates/claude-code/glm.sh

# Codex CLI + GLM
cp ai-config/templates/codex/glm.toml ~/.codex/config.toml

# Codex CLI + OpenRouter
cp ai-config/templates/codex/openrouter.toml ~/.codex/config.toml

# Codex CLI + OpenAI
cp ai-config/templates/codex/openai.toml ~/.codex/config.toml
```

详见 [ai-config/SKILL.md](../ai-config/SKILL.md)。

---

## 2. Claude Code 配置指南

### 2.1 安装

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### 2.2 使用智谱 GLM（推荐国内用户）

Claude Code 支持通过 Anthropic API 兼容协议接入智谱 GLM：

```bash
# 设置环境变量
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"
export ANTHROPIC_API_KEY="your-zhipu-api-key"

# 启动 Claude Code
claude
```

**模型映射关系**：

| Claude 模型层级 | 默认 GLM 模型 |
|----------------|-------------|
| Opus | GLM-4.7 |
| Sonnet | GLM-4.7 |
| Haiku | GLM-4.5-Air |

**切换到 GLM-5.1**：编辑 `~/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "GLM-4.5-Air",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "GLM-5.1",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "GLM-5.1"
  }
}
```

**使用 alias 不覆盖原有配置**：

```bash
# 在 ~/.zshrc 中添加
alias glm-cc='ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic ANTHROPIC_API_KEY="your-key" claude'
```

**验证**：启动后输入 `/status` 确认模型状态。

### 2.3 使用 Anthropic 原始 API

```bash
unset ANTHROPIC_BASE_URL
export ANTHROPIC_API_KEY="sk-ant-xxxxx"

# 国内用户需要代理
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port

claude
```

### 2.4 连接问题排查

**常见错误**：

```
Unable to connect to Anthropic services
Failed to connect to api.anthropic.com: ERR_BAD_REQUEST
```

**解决方案**：

| 方案 | 命令 |
|------|------|
| 配置代理 | `export HTTPS_PROXY=http://your-proxy:port` |
| 检查 API Key | `echo $ANTHROPIC_API_KEY` |
| 重新登录 | `claude logout && claude login` |
| 网络诊断 | `curl -v https://api.anthropic.com` |

---

## 3. Codex CLI 配置指南

### 3.1 安装

```bash
npm install -g @openai/codex
```

### 3.2 配置文件

配置文件位置：`~/.codex/config.toml`

### 3.3 使用智谱 GLM

```toml
model = "GLM-5.1"
model_provider = "glm"

[model_providers.glm]
name = "GLM"
base_url = "https://open.bigmodel.cn/api/coding/paas/v4"
env_key = "GLM_API_KEY"
wire_api = "chat"
```

```bash
export GLM_API_KEY="your-zhipu-api-key"
codex
```

### 3.4 使用 OpenRouter

```toml
model = "anthropic/claude-sonnet-4.6"
model_provider = "openrouter"

[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"
wire_api = "chat"
```

```bash
export OPENROUTER_API_KEY="your-openrouter-key"
codex
```

### 3.5 使用 OpenAI

```toml
model = "gpt-5.4"
model_provider = "openai"

[model_providers.openai]
name = "OpenAI"
base_url = "https://api.openai.com/v1"
env_key = "OPENAI_API_KEY"
wire_api = "chat"
```

```bash
export OPENAI_API_KEY="your-openai-key"
codex
```

### 3.6 使用 ModelScope（魔搭）

```toml
model = "ZhipuAI/GLM-4.5"
model_provider = "modelscope"

[model_providers.modelscope]
name = "modelscope"
wire_api = "chat"
base_url = "https://api-inference.modelscope.cn/v1"
env_key = "MODELSCOPE_API_KEY"
```

### 3.7 本地 Ollama

```toml
model = "mistral"
model_provider = "ollama"

[model_providers.ollama]
name = "ollama"
base_url = "http://localhost:11434/v1"
```

---

## 4. OpenCode 配置指南

### 4.1 安装

```bash
brew install opencode-ai/tap/opencode
# 或
curl -fsSL https://opencode.ai/install | bash
```

### 4.2 使用智谱 GLM（内置支持）

```bash
opencode auth login
# 选择 "Zhipu AI Coding Plan"，输入 API Key
opencode
# 使用 /models 命令选择 GLM 模型
```

### 4.3 使用 OpenAI

编辑 `~/.config/opencode/opencode.json` 或 `./.opencode.json`：

```json
{
  "providers": {
    "openai": {
      "apiKey": "",
      "disabled": false
    }
  },
  "agents": {
    "coder": {
      "model": "gpt-5.4",
      "maxTokens": 16384
    },
    "task": {
      "model": "gpt-5.4",
      "maxTokens": 16384
    },
    "title": {
      "model": "gpt-5.2-instant",
      "maxTokens": 80
    }
  },
  "mcpServers": {},
  "debug": false
}
```

---

## 5. 其他工具配置（Cline、OpenClaw）

### 5.1 Cline + GLM

在 Cline 扩展设置中：

| 配置项 | 值 |
|--------|-----|
| API Provider | `OpenAI Compatible` |
| Base URL | `https://open.bigmodel.cn/api/coding/paas/v4` |
| API Key | 你的智谱 API Key |
| 模型 | `GLM-5.1`（或 `GLM-5`、`GLM-4.7`） |

其他配置：
- 取消勾选 **Support Images**
- 调整 **Context Window Size** 为 `200000`

### 5.2 OpenClaw + GLM

编辑 `~/.openclaw/openclaw.json`，添加 GLM 模型：

```json
{
  "models": {
    "providers": {
      "zai": {
        "models": [
          {
            "id": "GLM-5.1",
            "name": "GLM-5.1",
            "reasoning": true,
            "input": ["text"],
            "cost": {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0},
            "contextWindow": 204800,
            "maxTokens": 131072
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "zai/GLM-5.1",
        "fallbacks": ["zai/GLM-5", "zai/GLM-4.7"]
      }
    }
  }
}
```

修改后运行：`openclaw gateway restart`

---

## 6. 智谱 GLM Coding Plan

### 6.1 什么是 Coding Plan

GLM Coding Plan 是智谱专为 AI 编码打造的订阅套餐，支持在 Claude Code、OpenCode、Cline、Codex CLI 等主流编码工具中使用。

### 6.2 可用模型

| 模型 | 说明 |
|------|------|
| GLM-5.1 | 最新旗舰版（推荐） |
| GLM-5 | 旗舰版 |
| GLM-4.7 | 高质量通用版 |
| GLM-4.6 | 均衡版 |
| GLM-4.5 | 高性能版 |
| GLM-4.5-Air | 轻量快速版 |

### 6.3 关键 API 端点

| 用途 | 端点 URL |
|------|---------|
| GLM Coding Plan (通用) | `https://open.bigmodel.cn/api/coding/paas/v4` |
| GLM Coding Plan (Claude Code) | `https://open.bigmodel.cn/api/anthropic` |
| GLM 通用 API | `https://open.bigmodel.cn/api/paas/v4` |

> **重要**：使用 Coding Plan 套餐时，必须使用 `coding/paas/v4` 端点，否则不会消耗套餐额度。

### 6.4 一键配置

```bash
npx @z_ai/coding-helper
```

### 6.5 获取 API Key

1. 访问 [智谱AI开放平台](https://open.bigmodel.cn)
2. 注册并登录
3. 在 [API Keys](https://open.bigmodel.cn/usercenter/apikeys) 页面创建/复制 API Key

---

## 7. 工具对比与选择建议

### 7.1 功能对比

| 特性 | Claude Code | Codex CLI | OpenCode | Cline | OpenClaw |
|------|-------------|-----------|----------|-------|----------|
| GLM Coding Plan | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenRouter | ❌ | ✅ | ❌ | ❌ | ❌ |
| OpenAI | ❌ | ✅ | ✅ | ✅ | ❌ |
| Anthropic | ✅ (默认) | ❌ | ❌ | ❌ | ❌ |
| 自定义 Provider | GLM only | 完全支持 | 内置 | OpenAI 兼容 | 内置 |
| IDE 集成 | VSCode/JetBrains | CLI | TUI | VSCode | TUI |
| 国产模型支持 | GLM 原生 | GLM 原生 | GLM 原生 | GLM 原生 | GLM 原生 |

### 7.2 选择建议

| 使用场景 | 推荐方案 |
|---------|---------|
| 国内用户，最强编码能力 | Claude Code + GLM-5.1 |
| 灵活切换模型 | Codex CLI + GLM/OpenRouter/OpenAI |
| 轻量终端工具 | OpenCode + GLM |
| IDE 内使用 | Cline + GLM |
| 多模型网关 | OpenClaw + GLM |
| 预算有限 | Codex CLI + GLM Coding Plan Lite |

### 7.3 快速切换别名配置

在 `~/.zshrc` 中添加：

```bash
# Claude Code + GLM
alias glm-cc='ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic ANTHROPIC_API_KEY="your-key" claude'

# Claude Code + Anthropic（需代理）
alias cc='claude'

# Codex + GLM
alias cx='codex'
```

然后执行：

```bash
source ~/.zshrc
```

---

## 附录：常见问题

### Q1: 如何查看智谱 API 余额？

访问 [智谱AI资源包管理](https://open.bigmodel.cn/creditmanage/resourcepack) 查看剩余额度。

### Q2: Codex CLI 配置文件在哪？

- macOS/Linux: `~/.codex/config.toml`
- Windows: `%USERPROFILE%\.codex\config.toml`

### Q3: 如何在项目中切换模型？

可以创建项目级配置文件：

```bash
# 在项目根目录创建
mkdir -p .codex
cp ai-config/templates/codex/glm.toml .codex/config.toml
```

### Q4: Claude Code 可以用 GLM 吗？

可以。Claude Code 通过 `ANTHROPIC_BASE_URL` 环境变量将请求重定向到智谱 API。设置后 Opus/Sonnet/Haiku 会自动映射到对应的 GLM 模型。

### Q5: Coding Plan 和普通 API 有什么区别？

Coding Plan 是专为编码工具设计的订阅套餐，有专属端点（`coding/paas/v4`），提供更高的额度配额和更快的响应速度（55+ tokens/秒）。

---

## 参考链接

- [智谱AI开放平台](https://open.bigmodel.cn)
- [GLM Coding Plan 文档](https://docs.bigmodel.cn/cn/coding-plan/overview)
- [OpenRouter](https://openrouter.ai)
- [Codex CLI GitHub](https://github.com/openai/codex)
- [OpenCode](https://opencode.ai)
