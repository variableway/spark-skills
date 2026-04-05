# Spark Skills 文档中心

> 个人习惯的 AI Agent Skill 仓库，统一收集、管理和分发适配多种 AI 编程助手的 Skills。

## 快速链接

### 📚 文档

- [支持的 Agent 工具](./Agents.md) - Claude Code、Codex CLI、Kimi CLI、OpenCode 等
- [AI 编程工具配置指南](./ai-coding-tools-guide.md) - 详细配置教程

### 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/your-username/spark-skills.git
cd spark-skills

# 安装 skills 到你的 Agent
./install.sh claude-code  # 或 kimi / codex / opencode
```

### 🛠 推荐配置

#### 国内用户（无需代理）

**方案一：Claude Code + GLM-5.1（推荐）**

```bash
# 一键配置
npx @z_ai/coding-helper

# 或手动配置
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"
export ANTHROPIC_API_KEY="your-zhipu-api-key"
claude
```

**方案二：Codex CLI + GLM-5.1**

```bash
npm install -g @openai/codex
cp ai-config/templates/codex/glm.toml ~/.codex/config.toml
export GLM_API_KEY="your-zhipu-api-key"
codex
```

**方案三：OpenCode + GLM**

```bash
opencode auth login
# 选择 "Zhipu AI Coding Plan"
opencode
```

#### 海外用户

**Claude Code**

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude login
```

---

## 文档目录

```
docs/
├── index.md                    # 本文件（文档首页）
├── README.md                   # 文档索引
├── Agents.md                   # Agent 工具介绍
└── ai-coding-tools-guide.md    # 配置指南
```

---

更多信息请访问 [项目主页](../README.md)。
