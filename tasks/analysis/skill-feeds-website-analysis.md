# Skill Feeds 网站构建分析

> 调研日期：2026-05-08
> 关联 Issue：#47
> 范围：构建 Skill Feeds 网站所需技术能力、Skill 清单与分类推荐

---

## 一、构建 Skill Feeds 网站所需的技术 Skill

### 1.1 整体架构

```
┌─────────────────────────────────────────────────────┐
│                    前端展示层                         │
│  Next.js 15 + React 19 + Tailwind CSS v4 + @innate/ui │
│  搜索/浏览/详情/对比/Feed 输出                        │
├─────────────────────────────────────────────────────┤
│                    API 服务层                         │
│  tRPC (内部) + REST API (公开) + Feed 端点            │
├─────────────────────────────────────────────────────┤
│                    数据层                             │
│  PostgreSQL + pgvector + Drizzle ORM                  │
│  全文搜索 + 向量搜索 + 时间序列指标                    │
├─────────────────────────────────────────────────────┤
│                    聚合管道                           │
│  skills.sh → ClawHub → GitHub → SkillsDirectory      │
│  爬取/去重/标准化/索引                                │
├─────────────────────────────────────────────────────┤
│                    基础设施                           │
│  Vercel + Supabase + Redis(Upstash) + GitHub Actions  │
└─────────────────────────────────────────────────────┘
```

### 1.2 前端 Skill

| Skill | 用途 | 推荐 |
|-------|------|------|
| **innate-frontend** | Web 前端开发框架，提供 57+ UI 组件、7 个 Landing 区块、OKLCH 主题系统 | 项目自有 |
| **Frontend Design (Anthropic)** | 推动独特视觉风格，避免 AI 风格同质化 | 每周 110k+ 安装 |
| **Vercel Web Design Guidelines** | 审查 UI 代码的 100+ 条无障碍/性能/UX 规则 | 每周 133k+ 安装 |
| **Vercel React Best Practices** | 57 条 React 性能优化规则 | Vercel 官方 |
| **Figma MCP Server** | 设计稿到代码的桥梁 | Figma 官方 |

### 1.3 后端 Skill

| Skill | 用途 | 推荐 |
|-------|------|------|
| **Postgres MCP Server** | 数据库 Schema 读取、查询编写、EXPLAIN ANALYZE | MCP 官方 |
| **GitHub MCP Server** | Issues/PRs/代码搜索，Skill 源数据获取 | MCP 官方 |
| **Composio MCP** | 250+ 平台统一集成 | Composio |
| **Context7 MCP** | 获取版本准确的库文档 | Upstash |

### 1.4 DevOps Skill

| Skill | 用途 | 推荐 |
|-------|------|------|
| **Vercel MCP Server** | 部署管理、构建日志、环境变量 | Vercel 官方 |
| **Playwright MCP** | 端到端浏览器测试 | Microsoft |
| **Docker MCP Catalog** | 100+ 容器化 MCP 服务器 | Docker 官方 |

### 1.5 安全 Skill

| Skill | 用途 | 推荐 |
|-------|------|------|
| **Trail of Bits Security** | CodeQL + Semgrep 静态分析 | 专业安全公司 |
| **Snyk MCP** | 依赖漏洞扫描、代码安全分析 | Snyk |
| **MCP Security Review** | 评估第三方 MCP 服务器安全性 | OWASP 框架 |

### 1.6 文档 Skill

| Skill | 用途 | 推荐 |
|-------|------|------|
| **Anthropic Document Skills** | PDF/DOCX/XLSX/PPTX 处理 | Anthropic 官方 |
| **Skill Creator** | 交互式 Skill 构建工具 | Anthropic 官方 |
| **Firecrawl** | Web 数据抓取和内容提取 | Firecrawl |

### 1.7 项目已有的参考资源

本项目 `references/` 目录已包含三个可索引的 Skill 集合：

| 集合 | Skill 数量 | 许可证 |
|------|-----------|--------|
| **Matt Pocock Skills** | 22 | MIT |
| **Composio SDK** | 22 | MIT |
| **Superpowers (Obra)** | 14 | MIT |

---

## 二、12 大类别 Top 5 Skill 推荐

### 1. 代码开发 (Code Development)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Superpowers** | 完整多 Agent 开发工作流：头脑风暴→实现计划→子 Agent 调度→TDD→代码审查 | 40.9k Stars，社区最大 Skill 库，支持多 Agent 并行和 RED-GREEN-REFACTOR | [obra/superpowers](https://github.com/obra/superpowers) |
| 2 | **GStack (Garry Tan)** | YC 总裁的 AI 工程团队工具包，覆盖设计、代码审查、QA、浏览器测试 | 来自高声望创作者，一个集合覆盖完整工程角色 | [garrytan/gstack](https://github.com/garrytan/gstack) |
| 3 | **Trail of Bits Security** | CodeQL + Semgrep 专业静态分析和漏洞检测 | 专业安全审计公司实际使用的工作流 | [trailofbits/skills](https://github.com/trailofbits/skills) |
| 4 | **E2B MCP Server** | 安全云端沙箱执行代码，支持 Python/JS/Shell | 弥合"写代码"和"验证代码"的关键差距 | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) |
| 5 | **Context7 MCP** | 获取版本准确的库文档，解决 LLM 训练数据过时问题 | 无需 API Key，确保 AI 基于最新 API 回答 | [upstash/context7-mcp](https://github.com/upstash/context7-mcp) |

### 2. 前端开发 (Frontend Development)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Frontend Design (Anthropic)** | 推动独特视觉风格，禁止过度使用的字体 | 每周 110k+ 安装，解决 AI 风格同质化 | [anthropics/skills](https://github.com/anthropics/skills) |
| 2 | **Vercel React Best Practices** | 57 条性能优化规则，覆盖请求瀑布流/Bundle/SSR 等 | 按实际影响排序优先级，编码 Vercel 团队性能经验 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| 3 | **Vercel Web Design Guidelines** | 100+ 条无障碍/性能/UX 规则审查 | 每周 133k+ 安装，输出精确 file:line 报告 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| 4 | **Vercel Composition Patterns** | 复合组件/Context Providers 替代布尔属性泛滥 | 解决设计系统最常见问题，React 19+ 模式 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| 5 | **Figma MCP Server** | Figma 设计稿完整结构信息暴露给 AI | 消除设计到代码鸿沟，AI 读取真实设计规范 | [MCP 官方](https://github.com/modelcontextprotocol) |

### 3. 后端开发 (Backend Development)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Postgres MCP Server** | 数据库 Schema 读取、查询编写、EXPLAIN ANALYZE | 改变游戏规则，AI 直接读取 Schema 并优化查询 | [MCP 官方](https://github.com/modelcontextprotocol/servers) |
| 2 | **Composio MCP** | 250+ 平台统一集成：GitHub/Slack/Gmail/Notion/Jira 等 | 一个配置连接数百个平台，最适合跨平台自动化 | [ComposioHQ/composio](https://github.com/ComposioHQ/composio) |
| 3 | **GitHub MCP Server** | Issues/PRs/代码搜索/仓库元数据完整访问 | 最广泛安装的 MCP 服务器，稳定性最佳 | [MCP 官方](https://github.com/modelcontextprotocol/servers) |
| 4 | **Stripe MCP Server** | 支付平台集成：客户管理/订阅/支付/退款 | SaaS 后端支付开发调试，消除切换控制台痛点 | [stripe/stripe-mcp](https://github.com/stripe/stripe-mcp) |
| 5 | **Sentry MCP Server** | 错误监控管道直连：堆栈跟踪/面包屑/事件搜索 | AI 获得完整错误上下文，修复建议更准确 | [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) |

### 4. DevOps/基础设施 (DevOps/Infrastructure)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Vercel MCP Server** | 部署/环境变量/构建日志/项目管理直接访问 | AI 拉取失败构建日志并建议修复，无需打开控制台 | [vercel/vercel-mcp](https://github.com/vercel/vercel-mcp) |
| 2 | **Playwright MCP** | 浏览器自动化：导航/点击/填表/UI 验证 | 弥合编写 UI 和验证其工作的差距 | [Microsoft](https://github.com/executeautomation/playwright-mcp-server) |
| 3 | **Docker MCP Catalog** | 100+ 容器化 MCP 服务器，内置隔离 | 企业级 DevOps 基础，环境一致性和隔离性 | [Docker 官方](https://www.docker.com/products/mcp-catalog) |
| 4 | **Cloudflare MCP** | 边缘网络/DNS/CDN 管理暴露给 AI | AI 直接参与边缘计算和 DNS 工作流 | [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) |
| 5 | **AWS MCP (Bedrock)** | S3/Lambda/IAM 等 AWS 服务集成 | 企业级云基础设施管理入口 | [AWS 官方](https://docs.aws.amazon.com/) |

### 5. 代码审查/质量 (Code Review/Quality)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Code Review Skill** | 11+ 语言/框架，9,500+ 检查项，结构化审查工作流 | 将审查标准化为可重复、可审计的专业流程 | [awesome-skills/code-review-skill](https://github.com/awesome-skills/code-review-skill) |
| 2 | **simplify (内置)** | 3 个并行 Agent 同时审查可读性/性能/正确性 | 利用子 Agent 并行加速审查，三维度同时分析 | Claude Code 内置 |
| 3 | **Trail of Bits Security** | CodeQL + Semgrep + 变体分析 | 专业安全审计师实际使用的结构化审查工作流 | [trailofbits/skills](https://github.com/trailofbits/skills) |
| 4 | **Vercel Guidelines (审查模式)** | 逐行审查 UI 代码，file:line 格式报告 | 自动化 UI 质量门禁，覆盖无障碍/语义化/键盘导航 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| 5 | **Snyk MCP** | 依赖漏洞扫描 + 代码安全分析 + 许可证合规 | 编码过程中实时发现和修复漏洞 | [snyk/saw-mcp](https://github.com/snyk/saw-mcp) |

### 6. 文档/内容 (Documentation/Content)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Anthropic Document Skills** | PDF/DOCX/XLSX/PPTX 处理套件 | 真正的文件操作，可串联使用实现文档自动化 | [anthropics/skills](https://github.com/anthropics/skills) |
| 2 | **Skill Creator** | 交互式 Skill 构建工具，问答式生成 SKILL.md | 消除构建自定义 Skill 的"白纸问题" | [anthropics/skills](https://github.com/anthropics/skills) |
| 3 | **Firecrawl** | Web 数据抓取/搜索/浏览器自动化，80%+ 召回率 | 从竞品文档、更新日志等网页提取内容 | [firecrawl/firecrawl-cli](https://github.com/firecrawl/firecrawl-cli) |
| 4 | **Context7 MCP** | 获取版本准确的库文档 | 确保文档引用基于最新 API，减少文档错误 | [upstash/context7-mcp](https://github.com/upstash/context7-mcp) |
| 5 | **doc-generator** | 从代码自动生成 README/API 文档/架构文档 | 文档自动化起点，保持文档与代码同步 | Agent Skills 标准参考 |

### 7. 产品设计 (Product Design)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **GStack Design** | 产品设计方向 Skill，提供建筑决策支持 | 将产品设计思维系统化，AI 扮演设计顾问 | [garrytan/gstack](https://github.com/garrytan/gstack) |
| 2 | **Corey Haines Marketing (32 Skills)** | 32 个营销 Skills：转化/文案/SEO/广告/留存/增长 | 覆盖完整营销漏斗，12.9k Stars | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) |
| 3 | **Frontend Design (Anthropic)** | 推动独特视觉风格，快速生成不同设计原型 | 产品设计验证阶段快速 A/B 对比 | [anthropics/skills](https://github.com/anthropics/skills) |
| 4 | **Figma MCP** | Figma 设计稿完整结构信息暴露给 AI | 设计交付关键桥梁，精确读取设计规范 | [MCP 官方](https://github.com/modelcontextprotocol) |
| 5 | **Remotion Best Practices** | 程序化视频生成：动画/音频/字幕/3D/图表 | 产品演示视频代码化生成，每周 117k 安装 | [remotion-dev/skills](https://github.com/remotion-dev/skills) |

### 8. 数据分析 (Data Analysis)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Data Exploration MCP** | 内置 Pandas/NumPy/Sklearn/SciPy 的数据科学工作台 | 百万级数据集验证，从探索到建模完整工作流 | [readingplusai](https://github.com/readingplusai/mcp-server-data-exploration) |
| 2 | **Hugging Face MCP** | 90 万+ 模型/20 万+ 数据集/30 万+ Spaces | ML 研究核心入口，自然语言发现资源 | [shreyaskarnik](https://github.com/shreyaskarnik/huggingface-mcp-server) |
| 3 | **MCP Pandas** | 容器化 Pandas MCP，FastAPI 服务 | Docker 容器化确保环境一致性 | [AlistairWalsh](https://github.com/AlistairWalsh/mcp-pandas) |
| 4 | **Claude Data Explorer** | CSV 数据分析，Python + JS 双实现 | 直接在对话中完成探索性数据分析 | [tofunori](https://github.com/tofunori/claude-mcp-data-explorer) |
| 5 | **Dataset Viewer MCP** | Hugging Face Dataset Viewer API 直连 | 无需下载即可浏览/过滤大型数据集 | [privetin](https://github.com/privetin/dataset-viewer-mcp) |

### 9. Git/版本控制 (Git/Version Control)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **GitHub MCP Server** | Issues/PRs/代码搜索/仓库元数据 | 最广泛安装、稳定性最佳的 MCP 服务器 | [MCP 官方](https://github.com/modelcontextprotocol/servers) |
| 2 | **Superpowers Git Worktrees** | 隔离分支创建，验证干净测试基线 | 自动化 Git 工作流管理 | [obra/superpowers](https://github.com/obra/superpowers) |
| 3 | **Linear MCP** | Linear Issue 跟踪完整生命周期管理 | 消除编辑器和 Issue 跟踪器之间的切换 | [linearapp/mcp-server](https://github.com/linearapp/mcp-server) |
| 4 | **Slack MCP** | 读取频道历史/发送消息/回复线程 | 长时间任务完成后自动通知 | [MCP 官方](https://github.com/modelcontextprotocol/servers) |
| 5 | **Composio MCP** | 250+ 平台统一集成 | 读 Ticket → 创建 Issue → 通知 Slack 一键搞定 | [ComposioHQ/composio](https://github.com/ComposioHQ/composio) |

### 10. 安全 (Security)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Trail of Bits Security** | CodeQL + Semgrep + 变体分析 + 结构化代码审计 | 顶级安全审计公司的专业工作流 | [trailofbits/skills](https://github.com/trailofbits/skills) |
| 2 | **Levo MCP** | 运行时安全智能：API 规格/漏洞/认证状态 | 唯一专为运行时安全设计的 MCP 服务器 | [levo.ai](https://www.levo.ai) |
| 3 | **Snyk MCP** | 依赖漏洞扫描 + DAST 动态测试 | 业界领先的依赖安全分析 | [snyk/saw-mcp](https://github.com/snyk/saw-mcp) |
| 4 | **MCP Security Review** | OWASP 框架评估 MCP 服务器安全态势 | 2026 年 2 月发现 341 个恶意 Skill 后至关重要 | [mcpmarket.com](https://mcpmarket.com/tools/skills/mcp-server-security-review) |
| 5 | **Shodan/Nmap MCP** | 互联网设备搜索 + 网络扫描封装 | 安全团队核心工具 MCP 标准化 | 社区维护 |

### 11. 项目管理 (Project Management)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Linear MCP** | Linear Issue 完整生命周期 + Sprint 状态 | 开发者在编辑器中即可管理 Issue | [linearapp/mcp-server](https://github.com/linearapp/mcp-server) |
| 2 | **Notion MCP** | Notion 页面/数据库/任务读写 | AI 直接参与知识管理和任务协调 | [MCP 官方](https://github.com/modelcontextprotocol/servers) |
| 3 | **GStack QA** | QA 工作流和代码审查标准化 | 每次代码变更都经过一致审查流程 | [garrytan/gstack](https://github.com/garrytan/gstack) |
| 4 | **Composio MCP (Jira+)** | 250+ 项目管理工具统一访问 | 多工具团队的统一入口 | [ComposioHQ/composio](https://github.com/ComposioHQ/composio) |
| 5 | **Superpowers /brainstorm + /write-plan** | 结构化问答精炼创意 → 2-5 分钟可执行任务 | 模糊产品想法系统化为可执行开发计划 | [obra/superpowers](https://github.com/obra/superpowers) |

### 12. AI/ML (Machine Learning)

| 排名 | Skill | 简介 | 推荐理由 | 来源 |
|------|-------|------|---------|------|
| 1 | **Hugging Face MCP** | 90 万+ 模型/20 万+ 数据集/30 万+ Spaces/每日论文 | ML 工作流起点，自然语言发现资源 | [shreyaskarnik](https://github.com/shreyaskarnik/huggingface-mcp-server) |
| 2 | **Data Exploration MCP** | 内置完整数据科学工具链的工作台 | 覆盖数据清洗→特征工程→建模完整流程 | [readingplusai](https://github.com/readingplusai/mcp-server-data-exploration) |
| 3 | **E2B MCP** | 安全云端沙箱执行 ML 训练/推理 | AI 不只写代码还能实际运行和迭代 | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) |
| 4 | **Composio ML 集成** | Hugging Face/W&B/Labelbox 等 ML 平台统一接口 | 实验跟踪/数据标注/模型部署单一接口 | [ComposioHQ/composio](https://github.com/ComposioHQ/composio) |
| 5 | **Dataset Viewer MCP** | Hugging Face Dataset Viewer API 直连 | ML 数据准备阶段加速器 | [privetin](https://github.com/privetin/dataset-viewer-mcp) |

---

## 三、Skill Feeds 网站的差异化定位

### 3.1 当前市场格局

| 平台 | 规模 | 特点 |
|------|------|------|
| **skills.sh** | 91,072+ Skills | 跨 19+ Agent 平台，排行榜 |
| **ClawHub** | 52.7K 工具/180K 用户 | 评分系统、安全扫描 |
| **claudemarketplaces.com** | 策划 + 投票 | 社区投票、评论 |
| **claudeskills.info** | 140+ Skills | Claude Code 专用 |
| **SkillsLLM.com** | 1,600+ Skills | 安全审计、多平台 |

### 3.2 建议的差异化方向

1. **跨平台聚合**：同时索引 skills.sh + ClawHub + GitHub 的统一入口
2. **Benchmark 驱动**：唯一提供自动化质量评分（PromptFoo）的站点
3. **中文友好**：当前所有市场均为英文，中文社区有空白
4. **Feed 优先**：RSS/Atom/JSON Feed 是核心功能，不是附加功能
5. **可视化对比**：Skill 对比雷达图、趋势图、跨平台指标合并

### 3.3 推荐实现路径

| 阶段 | 时间 | 交付 |
|------|------|------|
| Phase 1 | 1-2 周 | Schema + skills.sh 聚合 + 列表页 + 详情页 |
| Phase 2 | 2-3 周 | 全文搜索 + 分类浏览 + 标签过滤 |
| Phase 3 | 3-4 周 | PromptFoo 评测 + 雷达图展示 |
| Phase 4 | 4-5 周 | RSS/JSON Feed + 公开 API + 跨源聚合 |
| Phase 5 | 6-8 周 | 用户系统 + Skill 提交 + 评论评分 |

---

## 四、参考来源

- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [Anthropic 官方 Skill 文档](https://code.claude.com/docs/en/skills)
- [skills.sh](https://skills.sh)
- [MCP.Directory](https://mcp.directory/)
- [Firecrawl — Best Claude Code Skills 2026](https://www.firecrawl.dev/blog/best-claude-code-skills)
- [Firecrawl — 10 Best MCP Servers 2026](https://www.firecrawl.dev/blog/best-mcp-servers-for-developers)
- [Nimbalyst — Best Claude Code MCP Servers 2026](https://nimbalyst.com/blog/best-claude-code-mcp-servers/)
- [Snyk — 11 Data Science MCP Servers](https://snyk.io/articles/11-data-science-mcp-servers-for-sourcing-analyzing-and-visualizing-data/)
- [Levo.ai — Top 10 MCP Servers for Cybersecurity 2026](https://www.levo.ai/resources/blogs/top-mcp-servers-for-cybersecurity-2026)
- [Serenities AI — Agent Skills Guide 2026](https://serenitiesai.com/articles/agent-skills-guide-2026)
