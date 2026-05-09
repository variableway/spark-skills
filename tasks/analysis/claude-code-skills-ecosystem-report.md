# Claude Code Skills & AI Agent Skills 生态系统全景报告

> 调研日期: 2026-05-08
> 数据来源: GitHub、Firecrawl Blog、Nimbalyst、Snyk、Levo.ai、Serenities AI、MCP Directory、Reddit 等社区资源
> 适用场景: Skill Feeds 网站推荐内容

---

## 生态系统概览

截至 2026 年 5 月，Agent Skills 已成为一个开放标准，获得 **16+ 主流 AI 工具**的支持，包括 Claude Code、Cursor、OpenAI Codex、Gemini CLI、VS Code、GitHub Copilot、JetBrains Junie 等。MCP（Model Context Protocol）服务器生态系统已增长到 **9,000+** 条目。GitHub 上多个 awesome-list 仓库持续维护更新。

关键资源入口:
- skills.sh — 官方 Skills 包管理器（类似 npm）
- mcp.directory — 2,002+ MCP 服务器目录
- claudemarketplaces.com — Claude Code 插件市场
- github.com/anthropics/skills — Anthropic 官方 Skills 仓库

---

## 一、代码开发 (Code Development)

### 1. Superpowers
- **简介**: 由 Obra 开发的最完整多 Agent 开发工作流框架，包含头脑风暴、实现计划、子 Agent 调度、TDD 和代码审查的完整生命周期。
- **推荐理由**: GitHub 40.9k Stars，3.1k Forks，是社区最大的 Skill 库。支持多 Agent 并行执行任务，自动执行 RED-GREEN-REFACTOR 测试纪律。
- **来源**: https://github.com/obra/superpowers

### 2. GStack (Garry Tan)
- **简介**: YC 总裁 Garry Tan 开发的 AI 工程团队工具包，将 Claude Code 变成完整工程团队，涵盖 Office Hours、设计、代码审查、QA 和浏览器测试。
- **推荐理由**: 来自带声望的创作者，覆盖从设计到 QA 的完整团队角色，一个 Skill 集合即可处理多种工程场景。
- **来源**: https://github.com/garrytan/gstack

### 3. CodeQL & Semgrep Security Skills (Trail of Bits)
- **简介**: 安全研究公司 Trail of Bits 提供的专业级静态分析和漏洞检测 Skills，封装了 CodeQL 和 Semgrep 工具链。
- **推荐理由**: 不是基础安全检查清单，而是专业安全审计公司实际使用的工作流编码。支持变体分析和结构化代码审计。
- **来源**: https://github.com/trailofbits/skills

### 4. E2B MCP Server
- **简介**: 提供 AI 一个安全的云端沙箱来实际运行代码（非仅编写），支持 Python/JavaScript 执行、Shell 命令、包安装，全部在隔离的 microVM 中。
- **推荐理由**: 弥合了"写代码"和"验证代码"之间的关键差距，特别适合数据分析、迁移脚本和需要验证逻辑的场景。
- **来源**: https://github.com/e2b-dev/E2B

### 5. Context7 MCP Server
- **简介**: 获取数千个库的当前版本特定文档，注入 AI 的上下文窗口，解决 LLM 训练数据过时的问题。
- **推荐理由**: 无需 API Key 即可使用，确保 AI 回答基于最新的库 API 而非过时的训练数据，对 React 19、Next.js 15 等快速迭代的库尤其有价值。
- **来源**: https://github.com/upstash/context7-mcp

---

## 二、前端开发 (Frontend Development)

### 1. Frontend Design (Anthropic 官方)
- **简介**: Anthropic 官方维护的前端设计 Skill，明确禁止过度使用的字体（Inter、Roboto 等），推动 Claude 做出深思熟虑的美学选择。
- **推荐理由**: 每周 110k+ 安装量，是目前安装量最大的 Skill 之一。有效解决"AI 风格同质化"问题，让前端产出具有独特视觉风格。
- **来源**: https://github.com/anthropics/skills (frontend-design)

### 2. Vercel React Best Practices
- **简介**: Vercel 工程团队出品的 57 条性能优化规则，覆盖请求瀑布流、Bundle 大小、SSR、数据获取、重渲染等 8 大类别。
- **推荐理由**: 按实际影响排序优先级，避免开发者（和 AI）跳过关键瓶颈而关注微观优化。编码了 Vercel 工程团队的性能优先级。
- **来源**: https://github.com/vercel-labs/agent-skills

### 3. Vercel Web Design Guidelines
- **简介**: 审查 UI 代码是否符合 100+ 条无障碍、性能和 UX 规则，输出精确的 `file:line` 格式发现报告。
- **推荐理由**: 每周 133k 安装量，覆盖 ARIA 属性、焦点状态、触控目标尺寸、语义化 HTML 等。始终获取最新版本的指南标准。
- **来源**: https://github.com/vercel-labs/agent-skills (web-design-guidelines)

### 4. Vercel Composition Patterns
- **简介**: 用复合组件（Compound Components）、Context Providers 和干净的组件 API 替代布尔属性泛滥，包含 React 19+ 模式。
- **推荐理由**: 解决设计系统中最常见的问题——布尔属性（isCompact, showHeader, hasBorder...）导致组件难以理解和扩展。对构建设计系统或共享组件库尤其有价值。
- **来源**: https://github.com/vercel-labs/agent-skills (composition-patterns)

### 5. Figma MCP Server
- **简介**: Figma 官方 Dev Mode MCP 服务器，将 Figma 中选中的设计稿的完整结构信息（层级、Auto Layout、变体、文本样式、间距 Token）直接暴露给 AI。
- **推荐理由**: 消除设计到代码的鸿沟，AI 可以读取真实的设计规范而非猜测截图，生成精确匹配设计系统的组件代码。
- **来源**: https://github.com/modelcontextprotocol (官方参考实现)

---

## 三、后端开发 (Backend Development)

### 1. Postgres MCP Server
- **简介**: 将 Postgres 数据库暴露给 AI，支持 Schema 读取、查询编写、数据检查和（可选的）数据变更操作。
- **推荐理由**: 对于数据库驱动的项目，这是改变游戏规则的工具。AI 可以直接读取 Schema、编写优化查询、执行 EXPLAIN ANALYZE。建议使用只读角色确保安全。
- **来源**: https://github.com/modelcontextprotocol/servers (server-postgres)

### 2. Composio MCP (250+ 集成)
- **简介**: 一个 MCP 服务器暴露 250+ 平台的工具，包括 GitHub、Slack、Gmail、Notion、Jira、Salesforce 等。OAuth 和 API Key 管理自动化。
- **推荐理由**: 无需为每个服务安装单独的 MCP 服务器，一个配置连接即可访问数百个平台。特别适合跨多平台的自动化工作流。
- **来源**: https://github.com/ComposioHQ/composio

### 3. GitHub MCP Server
- **简介**: 最广泛安装的 MCP 服务器，暴露 Claude Code 对 Issues、PRs、代码搜索和仓库元数据的完整访问能力。
- **推荐理由**: 将 Claude Code 从代码生成器转变为参与 Issue 和 PR 工作流的协作者。官方参考实现，稳定性最佳。
- **来源**: https://github.com/modelcontextprotocol/servers (server-github)

### 4. Stripe MCP Server
- **简介**: 将 Stripe 支付平台集成到 AI 工作流中，支持客户管理、订阅、支付、退款等操作。
- **推荐理由**: 对于涉及支付的 SaaS 后端开发，让 AI 直接操作 Stripe API 进行开发调试，消除反复切换控制台的痛点。
- **来源**: https://github.com/stripe/stripe-mcp

### 5. Sentry MCP Server
- **简介**: 将 AI 直连错误监控管道，获取完整的错误上下文、堆栈跟踪、面包屑和相关事件，支持按标签/环境/时间范围搜索。
- **推荐理由**: 消除"在 Sentry 看到错误 → 复制堆栈 → 粘贴到聊天 → 描述上下文"的低效循环。AI 获得和你一样的完整视图，修复建议更准确。
- **来源**: https://github.com/getsentry/sentry-mcp

---

## 四、DevOps/基础设施 (DevOps/Infrastructure)

### 1. Vercel MCP Server
- **简介**: 官方 Vercel MCP 服务器，提供对部署、环境变量、构建日志和项目管理的直接访问。
- **推荐理由**: 解决"本地能跑但 Vercel 不行"的经典问题。AI 可以拉取失败部署的构建日志、识别错误并建议修复，无需打开 Vercel 控制台。
- **来源**: https://github.com/vercel/vercel-mcp

### 2. Playwright MCP Server (Microsoft)
- **简介**: 微软出品的浏览器自动化 MCP，让 AI 控制真实浏览器进行导航、点击、填表和 UI 验证，基于无障碍树交互。
- **推荐理由**: 弥合编写 UI 代码和验证其工作之间的差距。AI 可以执行完整的端到端测试场景，消除"只在真实浏览器中出现的 Bug"。
- **来源**: https://github.com/executeautomation/playwright-mcp-server

### 3. Docker MCP Catalog
- **简介**: Docker 官方推出的 MCP 服务器目录，包含 100+ 已验证的容器化服务器，提供内置隔离。
- **推荐理由**: 将 MCP 服务器容器化部署，确保环境一致性和隔离性，是企业级 DevOps 工作流的基础。
- **来源**: https://www.docker.com/products/mcp-catalog

### 4. Cloudflare MCP Server
- **简介**: 将 Cloudflare 边缘网络、DNS、CDN 管理功能暴露给 AI，支持域名配置、缓存管理、安全策略设置。
- **推荐理由**: 对于使用 Cloudflare 基础设施的团队，让 AI 直接参与边缘计算和 DNS 工作流，减少运维操作的手动切换。
- **来源**: https://github.com/cloudflare/mcp-server-cloudflare

### 5. AWS MCP Integration (Bedrock Agents)
- **简介**: AWS 将 MCP 直接集成到 Bedrock Agents 中，支持 S3 操作、Lambda 管理、IAM 配置等 AWS 服务。
- **推荐理由**: 企业级云基础设施管理的入口，结合 AWS 的安全模型和 MCP 的标准化接口。
- **来源**: AWS 官方文档

---

## 五、代码审查/质量 (Code Review/Quality)

### 1. awesome-skills/code-review-skill
- **简介**: 专为 Claude Code 构建的生产级代码审查 Skill，覆盖 11+ 语言和框架，包含 9,500+ 检查项，将 AI 辅助审查转化为结构化专业工作流。
- **推荐理由**: 最全面的代码审查 Skill 之一，将审查过程标准化为可重复、可审计的专业流程。
- **来源**: https://github.com/awesome-skills/code-review-skill

### 2. /simplify (Claude Code 内置)
- **简介**: Claude Code 内置的并行代码审查 Skill，同时启动 3 个并行审查 Agent（可读性、性能、正确性），各自独立分析后合并为统一审查报告。
- **推荐理由**: 利用子 Agent 并行模式显著加速审查，三个维度同时分析比顺序审查更快更全面。
- **来源**: Claude Code 内置

### 3. Trail of Bits Security Review Skills
- **简介**: 专业安全审计公司 Trail of Bits 的代码审查方法论，封装了 CodeQL 静态分析、Semgrep 规则和变体分析。
- **推荐理由**: 非安全检查清单，而是编码了专业安全审计师实际使用的结构化审查工作流，安全深度远超普通 lint。
- **来源**: https://github.com/trailofbits/skills

### 4. Vercel Web Design Guidelines (审查模式)
- **简介**: 获取最新的 Web Interface Guidelines 并对代码进行逐行审查，输出 file:line 格式的发现报告。
- **推荐理由**: 自动化的 UI 质量门禁，覆盖无障碍、语义化、键盘导航等在赶工时容易被忽略的细节。
- **来源**: https://github.com/vercel-labs/agent-skills

### 5. Snyk MCP Server
- **简介**: Snyk 的 MCP 服务器，让 AI 直接访问依赖漏洞扫描、代码安全分析和许可证合规检查。
- **推荐理由**: 将 Snyk 的安全扫描能力直接集成到 AI 工作流中，在编码过程中实时发现和修复漏洞。
- **来源**: https://github.com/snyk/saw-mcp

---

## 六、文档/内容 (Documentation/Content)

### 1. Anthropic Document Skills (PDF/DOCX/XLSX/PPTX)
- **简介**: Anthropic 官方文档 Skills 套件，支持 PDF 提取/创建/合并/拆分、Word 文档编辑、Excel 分析、PowerPoint 演示文稿生成。
- **推荐理由**: 真正的文件操作而非文本描述。可以串联使用（从 PDF 提取数据 → 处理 → 输出到 Excel），实现文档自动化。
- **来源**: https://github.com/anthropics/skills (pdf, docx, xlsx, pptx)

### 2. Skill Creator (Anthropic 官方)
- **简介**: Anthropic 官方的交互式 Skill 构建工具，通过问答式流程生成完整的 SKILL.md 结构和支撑文件。
- **推荐理由**: 消除构建自定义 Skill 的"白纸问题"，交互式问答会发现你可能遗漏的边界情况。
- **来源**: https://github.com/anthropics/skills (skill-creator)

### 3. Firecrawl Skill + CLI
- **简介**: 提供 AI 可靠的 Web 数据访问能力，支持网页抓取、搜索、浏览器自动化，结果写入文件而非塞入上下文窗口。
- **推荐理由**: 80%+ 的内容召回率，JavaScript 渲染自动处理。特别适合从竞品文档、更新日志等网页提取内容用于文档编写。
- **来源**: https://github.com/firecrawl/firecrawl-cli

### 4. Context7 MCP Server
- **简介**: 获取版本准确的库文档，确保文档引用基于最新 API 而非过时训练数据。
- **推荐理由**: 编写技术文档时确保引用的 API 签名和用法与当前版本一致，减少文档错误。
- **来源**: https://github.com/upstash/context7-mcp

### 5. doc-generator Skill Recipe
- **简介**: 自动从代码生成项目文档的通用 Skill 模板，支持 README、API 文档（JSDoc/docstrings）、架构文档和更新日志。
- **推荐理由**: 实用的文档自动化起点，可以根据团队需求定制，保持文档与代码同步。
- **来源**: Agent Skills 开放标准参考实现

---

## 七、产品设计 (Product Design)

### 1. GStack — Office Hours + Design
- **简介**: Garry Tan 的 GStack 中包含的产品设计方向 Skill，提供建筑决策支持和设计方向指导。
- **推荐理由**: 将产品设计思维系统化，让 AI 扮演设计顾问角色进行结构化的产品决策讨论。
- **来源**: https://github.com/garrytan/gstack

### 2. Corey Haines Marketing Skills (32 个 Skills)
- **简介**: 生态系统中最大的营销专注 Skill 库（12.9k Stars），包含 32 个 Skills 覆盖转化优化、文案、SEO、付费广告、分析、留存、增长工程和销售运营。
- **推荐理由**: 覆盖完整营销漏斗（SEO → CRO → 留存 → 邮件序列），所有 Skill 共享 product-marketing-context 文件确保一致性。
- **来源**: https://github.com/coreyhaines31/marketingskills

### 3. Frontend Design Skill (Anthropic)
- **简介**: 推动前端设计从"AI 风格同质化"到独特、生产级 UI 的转变，在写代码前先确定视觉方向。
- **推荐理由**: 对产品设计验证阶段特别有用——快速生成不同设计风格的低保真原型进行 A/B 对比。
- **来源**: https://github.com/anthropics/skills (frontend-design)

### 4. Figma MCP Server
- **简介**: 将 Figma 设计稿的完整结构信息暴露给 AI，包括层级、Auto Layout、变体、Token 等。
- **推荐理由**: 设计师在 Figma 中完成设计后，AI 可以直接读取精确的设计规范生成代码，是设计交付的关键桥梁。
- **来源**: https://github.com/modelcontextprotocol (官方参考实现)

### 5. Remotion Best Practices
- **简介**: Remotion 团队官方维护的程序化视频 Skill，每周 117k 安装。覆盖动画、音频、字幕、3D、图表等。
- **推荐理由**: 产品演示视频、营销视频可以代码化生成，特别适合产品发布和内容营销场景。
- **来源**: https://github.com/remotion-dev/skills

---

## 八、数据分析 (Data Analysis)

### 1. Data Exploration MCP (ReadingPlus.ai)
- **简介**: 全面的数据分析 MCP 服务器（GitHub 343 Stars），将复杂数据集转化为清晰的洞察，作为个人数据科学家助手。内置 Pandas、NumPy、Scikit-learn、SciPy、Statsmodels。
- **推荐理由**: 已在真实数据集上验证（220 万条加州房地产数据、200 万条伦敦天气数据），提供从探索到建模的完整工作流。
- **来源**: https://github.com/readingplusai/mcp-server-data-exploration

### 2. Hugging Face MCP Server
- **简介**: 解锁 Hugging Face Hub 生态系统，提供 90 万+ 模型、20 万+ 数据集、30 万+ Spaces 的搜索和访问能力。
- **推荐理由**: AI/ML 研究的核心入口，通过自然语言发现相关模型、数据集和论文，消除手动搜索的繁琐。
- **来源**: https://github.com/shreyaskarnik/huggingface-mcp-server

### 3. MCP Pandas (Alistair Walsh)
- **简介**: 容器化架构的 Pandas MCP 服务器，通过 FastAPI 服务处理 pandas 操作，支持统计分析、数据可视化和探索性分析。
- **推荐理由**: Docker 容器化确保环境一致性，可以直接利用 Pandas 的全部能力进行数据操作和可视化。
- **来源**: https://github.com/AlistairWalsh/mcp-pandas

### 4. Claude MCP Data Explorer (tofunori)
- **简介**: 直接在 Claude 中分析 CSV 数据的 MCP 服务器，同时提供 Python（Pandas/NumPy/Sklearn）和 JavaScript（Plotly.js）两种实现。
- **推荐理由**: 消除在多应用间切换的需要，直接在对话中完成探索性数据分析。
- **来源**: https://github.com/tofunori/claude-mcp-data-explorer

### 5. Dataset Viewer MCP Server (privetin)
- **简介**: 直接访问 Hugging Face Dataset Viewer API，无需下载完整数据集即可浏览、搜索、过滤和提取数据子集。
- **推荐理由**: 对于大型数据集特别有价值，支持分页浏览、SQL 过滤和 Parquet 格式导出。
- **来源**: https://github.com/privetin/dataset-viewer-mcp

---

## 九、Git/版本控制 (Git/Version Control)

### 1. GitHub MCP Server
- **简介**: 生态中最成熟的 MCP 服务器，暴露对 Issues、PRs、代码搜索和仓库元数据的完整访问。
- **推荐理由**: 使用范围最广、稳定性最佳的 MCP 服务器。将 AI 变为 Git 工作流的真正参与者。
- **来源**: https://github.com/modelcontextprotocol/servers (server-github)

### 2. Superpowers — Git Worktrees Skill
- **简介**: Superpowers 中的 Git Worktrees 技能，创建隔离分支并在开始编码前验证干净的测试基线。
- **推荐理由**: 自动化的 Git 工作流管理，确保每个任务在独立分支上执行，完成后干净合并。
- **来源**: https://github.com/obra/superpowers

### 3. Linear MCP Server
- **简介**: 将 AI 连接到 Linear 项目管理系统，支持读取/创建/更新 Issues、管理标签/优先级/负责人、搜索项目和查看 Sprint 状态。
- **推荐理由**: 消除在编辑器和 Issue 跟踪器之间频繁切换的上下文切换损耗。
- **来源**: https://github.com/linearapp/mcp-server

### 4. Slack MCP Server
- **简介**: 让 AI 读取 Slack 频道历史、发送消息和回复线程，实现异步状态更新和团队协调。
- **推荐理由**: 长时间运行的任务完成后自动通知，无需离开编辑器即可协调团队工作。
- **来源**: https://github.com/modelcontextprotocol/servers (server-slack)

### 5. Composio MCP (统一集成)
- **简介**: 一个 MCP 连接 250+ 平台，包括 GitHub、Linear、Notion、Jira 等，统一管理认证和工作流。
- **推荐理由**: 需要同时操作多个开发工具时（如：读 Linear Ticket → 创建 GitHub Issue → 通知 Slack），一个连接搞定。
- **来源**: https://github.com/ComposioHQ/composio

---

## 十、安全 (Security)

### 1. Trail of Bits Security Skills
- **简介**: 专业安全研究公司的 Skills 集合，封装 CodeQL 和 Semgrep 静态分析、变体分析和结构化代码审计方法论。
- **推荐理由**: 将顶级安全审计公司的专业工作流带入日常开发，不是简单的检查清单而是深度安全分析。
- **来源**: https://github.com/trailofbits/skills

### 2. Levo MCP Server
- **简介**: 将运行时安全智能安全地暴露给 AI 和人类，提供 API 规格、运行时跟踪、漏洞、认证状态等实时安全数据。
- **推荐理由**: 唯一专为暴露运行时安全智能而设计的 MCP 服务器，支持代理自动验证修复、分诊问题和复现发现。
- **来源**: https://www.levo.ai

### 3. Snyk MCP Server
- **简介**: Snyk CLI 内置的 MCP 服务器，让 AI 运行安全扫描、配置认证目标和执行 DAST（动态应用安全测试）。
- **推荐理由**: 业界领先的依赖漏洞扫描和代码安全分析工具，通过 MCP 直接集成到 AI 工作流。
- **来源**: https://github.com/snyk/saw-mcp

### 4. MCP Server Security Review Skill
- **简介**: 基于 OWASP 框架的结构化 MCP 服务器安全评估 Skill，用于评估 MCP 服务器的安全态势。
- **推荐理由**: 随着 341 个恶意 Skill 被发现（2026 年 2 月），评估第三方 MCP 服务器的安全性变得至关重要。
- **来源**: https://mcpmarket.com/tools/skills/mcp-server-security-review

### 5. Shodan / Nmap MCP Servers
- **简介**: 将 Shodan 互联网设备搜索和 Nmap 网络扫描封装为受控 MCP 接口，用于自动化侦察和攻击面评估。
- **推荐理由**: 安全团队日常使用的核心工具通过 MCP 标准化，使 AI 辅助的安全评估可控、可审计。
- **来源**: 社区维护（awesome-mcp-servers/security）

---

## 十一、项目管理 (Project Management)

### 1. Linear MCP Server
- **简介**: 将 AI 连接到 Linear Issue 跟踪系统，支持完整的 Issue 生命周期管理、Sprint 状态查看和跨项目搜索。
- **推荐理由**: 使用 Linear 的团队的首选——开发者在编辑器中即可完成 Issue 的创建、更新和状态管理。
- **来源**: https://github.com/linearapp/mcp-server

### 2. Notion MCP Server
- **简介**: 将 Notion 工作空间暴露给 AI，支持读取/创建/更新页面、数据库和任务。
- **推荐理由**: 对于使用 Notion 作为项目信息中心的团队，让 AI 直接参与知识管理和任务协调。
- **来源**: https://github.com/modelcontextprotocol/servers

### 3. GStack — QA + Code Review
- **简介**: GStack 中的 QA 工作流和代码审查 Skills，提供质量保证和测试覆盖的工作流自动化。
- **推荐理由**: 将 QA 流程标准化为可重复的 Skill，确保每次代码变更都经过一致的审查流程。
- **来源**: https://github.com/garrytan/gstack

### 4. Composio MCP (Jira + 多平台)
- **简介**: 通过 Composio 统一访问 Jira、Asana、Monday.com 等 250+ 项目管理工具。
- **推荐理由**: 使用多个项目管理工具的团队的统一入口，一个 MCP 配置管理所有工具。
- **来源**: https://github.com/ComposioHQ/composio

### 5. Superpowers — /brainstorm + /write-plan
- **简介**: 通过结构化问答精炼创意、保存设计文档，然后将设计分解为 2-5 分钟的可执行任务，每个任务包含精确的文件路径和验证步骤。
- **推荐理由**: 将模糊的产品想法系统化为可执行的开发计划，再由子 Agent 按计划执行。
- **来源**: https://github.com/obra/superpowers

---

## 十二、AI/ML (Machine Learning)

### 1. Hugging Face MCP Server
- **简介**: 解锁 Hugging Face Hub 的完整 AI 资源生态——90 万+ 模型、20 万+ 数据集、30 万+ Spaces、每日论文列表。
- **推荐理由**: ML 工作流的起点。通过自然语言发现模型、数据集和论文，10 个工具覆盖模型/数据集/Spaces/论文/集合的搜索和详情。
- **来源**: https://github.com/shreyaskarnik/huggingface-mcp-server

### 2. Data Exploration MCP (ReadingPlus.ai)
- **简介**: 内置 Pandas、Scikit-learn、SciPy、Statsmodels 的完整数据科学工作台，支持数据加载、分析、建模和可视化。
- **推荐理由**: 在真实百万级数据集上验证过的数据科学助手，覆盖从数据清洗到特征工程到建模的完整 ML 准备流程。
- **来源**: https://github.com/readingplusai/mcp-server-data-exploration

### 3. E2B MCP Server (沙箱执行)
- **简介**: 安全的云端代码执行环境，支持 Python/JavaScript 在隔离的 microVM 中运行 ML 训练脚本、数据处理管道和模型推理。
- **推荐理由**: 让 AI 不只是写 ML 代码，还能实际运行、检查输出并迭代优化——这在 ML 开发中至关重要。
- **来源**: https://github.com/e2b-dev/E2B

### 4. Composio MCP (ML 平台集成)
- **简介**: 统一连接 250+ 平台，包括 ML 相关的 Hugging Face、Weights & Biases、Labelbox 等，统一管理实验跟踪和模型部署。
- **推荐理由**: 将 ML 实验跟踪、数据标注、模型部署等多个工具整合为单一接口，减少工具切换。
- **来源**: https://github.com/ComposioHQ/composio

### 5. Dataset Viewer MCP Server
- **简介**: 直接访问 Hugging Face Dataset Viewer API，无需下载即可浏览、过滤、搜索数据集，支持统计分析和 Parquet 导出。
- **推荐理由**: ML 开发中最耗时的数据准备阶段的加速器，快速评估数据集质量和适用性。
- **来源**: https://github.com/privetin/dataset-viewer-mcp

---

## 附录：关键 Skill/MCP 管理工具

| 工具 | 用途 | 地址 |
|------|------|------|
| skills.sh | Skills 包管理器（安装/搜索/发布） | https://skills.sh |
| mcp.directory | 2,002+ MCP 服务器目录 | https://mcp.directory |
| claudemarketplaces.com | Claude Code 插件市场 | https://claudemarketplaces.com |
| awesome-claude-skills | GitHub 精选列表 | https://github.com/ComposioHQ/awesome-claude-skills |
| awesome-mcp-servers | GitHub MCP 精选列表 | https://github.com/appcypher/awesome-mcp-servers |
| Docker MCP Catalog | 容器化 MCP 目录 | Docker Hub |
| agentskills.io | Agent Skills 开放标准官网 | https://agentskills.io |

---

## 数据来源

- [Firecrawl — Best Claude Code Skills to Try in 2026](https://www.firecrawl.dev/blog/best-claude-code-skills)
- [Firecrawl — 10 Best MCP Servers for Developers in 2026](https://www.firecrawl.dev/blog/best-mcp-servers-for-developers)
- [Nimbalyst — Best Claude Code MCP Servers in 2026](https://nimbalyst.com/blog/best-claude-code-mcp-servers/)
- [Snyk — 11 Data Science MCP Servers](https://snyk.io/articles/11-data-science-mcp-servers-for-sourcing-analyzing-and-visualizing-data/)
- [Levo.ai — Top 10 MCP Servers for Cybersecurity in 2026](https://www.levo.ai/resources/blogs/top-mcp-servers-for-cybersecurity-2026)
- [Serenities AI — Agent Skills Guide 2026](https://serenitiesai.com/articles/agent-skills-guide-2026)
- [MCP Directory — Awesome MCP Servers](https://mcp.directory/awesome-mcp-servers)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [Agensi.io — Best MCP Servers 2026](https://www.agensi.io/learn/best-mcp-servers-2026)
