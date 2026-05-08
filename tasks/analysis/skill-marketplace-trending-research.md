# Research: Getting Skills Trending in AI Marketplaces

**Date:** 2026-05-07

## Table of Contents

1. [Major Skill Marketplaces](#1-major-skill-marketplaces)
2. [skills.sh (by Vercel)](#2-skillssh-by-vercel)
3. [ClawHub (OpenClaw)](#3-clawhub-openclaw)
4. [Claude Code Plugin Marketplace (Official)](#4-claude-code-plugin-marketplace-official)
5. [Paid Marketplaces](#5-paid-marketplaces)
6. [Trending Strategy](#6-trending-strategy)
7. [What Top Skills Have in Common](#7-what-top-skills-have-in-common)
8. [Recommendations for fire-skills](#8-recommendations-for-fire-skills)
9. [Sources](#9-sources)

---

## 1. Major Skill Marketplaces

| Platform | Type | Scale | Cross-Platform |
|----------|------|-------|----------------|
| **skills.sh** (Vercel) | Open registry | 91,072+ skills | 19+ agents |
| **ClawHub** (OpenClaw) | Open registry | 52.7k tools, 180k users, 12M downloads | OpenClaw ecosystem |
| **Claude Code Marketplace** (Anthropic) | Official plugin system | Built into Claude Code | Claude Code only |
| **AgentPowers.ai** | Paid marketplace | Premium skills | Claude, Cursor, Codex |
| **MCP Market** | Directory + leaderboard | Community-driven | Multiple agents |
| **SkillsLLM.com** | Security-vetted directory | 1,600+ skills | Claude, Codex, ChatGPT |
| **claudeskills.info** | Free marketplace | 140+ skills | Claude Code |
| **claudemarketplaces.com** | Community directory | Curated + voting | Claude Code |

---

## 2. skills.sh (by Vercel)

### Overview
The largest cross-platform skill registry, launched by Vercel. Supports 19+ agent platforms: Claude Code, Cursor, Codex, GitHub Copilot, Cline, Gemini, Windsurf, AMP, Roo, Trae, Kilo, Goose, Droid, VSCode, OpenCode, and more.

### Stats
- **91,072 skills** indexed
- Install via `npx skills add`
- Leaderboard tabs: **All Time**, **Trending (24h)**, **Hot**
- Top skill: `find-skills` with 1.3M installs

### How to Publish
1. Create a **GitHub repo** with `SKILL.md` files (YAML frontmatter + instructions)
2. The directory crawls and indexes public repos containing SKILL.md files
3. Users install with `npx skills add`
4. Use `npx skills` CLI to manage skills

### SKILL.md Format
```yaml
---
name: my-skill
description: What it does
---

Skill instructions here...
```

### Trending Algorithm
- **Install count** is the primary ranking metric
- **Trending momentum** — skills gaining installs rapidly get boosted to the Trending tab
- **Hot** tab shows fastest-moving skills
- **Quality/security** — skills.sh/audits highlights security-vetted skills
- **Official publishers** (Anthropic, Vercel, Microsoft, etc.) get priority placement

### Key Resources
- [Community Session: How to create and publish skills](https://www.youtube.com/watch?v=jJUuuYuEykk)
- [GitHub: vercel-labs/skills](https://github.com/vercel-labs/skills)
- [trending-skills tracker](https://github.com/geekjourneyx/trending-skills) — automated daily leaderboard tracking
- [skills.sh Docs](https://skills.sh/docs)

---

## 3. ClawHub (OpenClaw)

### Overview
OpenClaw is a personal AI assistant platform. Its marketplace, **ClawHub** (clawhub.ai), is the central public registry for OpenClaw skills and plugins.

### Stats
- **52.7k tools**, **180k users**, **12M downloads**, **4.8 avg rating**
- Top skills: Self-Improving Agent (422.7k installs), Skill Vetter (230.8k), Github (171.2k)

### How to Publish
1. Create skill folder with `SKILL.md` (AgentSkills-compatible format)
2. Use `clawhub sync --all` to scan and publish
3. Security scan runs automatically (VirusTotal, ClawScan, static analysis)
4. Users install via `openclaw skills install <name>`

### SKILL.md Format (OpenClaw)
```yaml
---
name: my-skill
description: What it does
metadata: {"openclaw": {"requires": {"bins": ["uv"], "env": ["API_KEY"]}, "emoji": "..."}}
---
```

### Skill Precedence (highest first)
1. Workspace skills: `/skills`
2. Project agent skills: `/.agents/skills`
3. Personal agent skills: `~/.agents/skills`
4. Managed/local skills: `~/.openclaw/skills`
5. Bundled skills (shipped with install)
6. Extra skill folders (config)

### Security Note
[Security researchers have reported malware distribution through OpenClaw skills](https://socket.dev/blog/openclaw-skill-marketplace-emerges-as-active-malware-vector). If publishing here, ensure your skill passes security audits cleanly.

### Key Resources
- [OpenClaw Skills Documentation](https://docs.openclaw.ai/tools/skills)
- [ClawHub](https://clawhub.ai)
- [Awesome OpenClaw Skills](https://aiagentstore.ai/ai-agent/awesome-openclaw-skills)

---

## 4. Claude Code Plugin Marketplace (Official)

### Overview
Anthropic's official plugin distribution system built into Claude Code. Plugins bundle skills, hooks, subagents, MCP servers, and LSP servers.

### How to Create a Marketplace
1. Build plugin(s) with proper `plugin.json`
2. Create `.claude-plugin/marketplace.json` in your repo root:

```json
{
  "name": "my-marketplace",
  "owner": { "name": "Your Name", "email": "you@example.com" },
  "plugins": [
    {
      "name": "my-plugin",
      "source": "./plugins/my-plugin",
      "description": "What it does",
      "version": "1.0.0",
      "author": { "name": "Your Name" },
      "keywords": ["productivity", "automation"],
      "category": "development"
    }
  ]
}
```

3. Push to GitHub
4. Users install: `/plugin marketplace add owner/repo`
5. Individual plugins: `/plugin install my-plugin@my-marketplace`

### Plugin Sources Supported
| Source | Example |
|--------|---------|
| Relative path | `"./my-plugin"` |
| GitHub | `{"source": "github", "repo": "owner/repo"}` |
| Git URL | `{"source": "url", "url": "https://gitlab.com/..."}` |
| Git subdirectory | `{"source": "git-subdir", "url": "...", "path": "tools/plugin"}` |
| npm | `{"source": "npm", "package": "@org/plugin"}` |

### Key Features
- Version tracking, auto-updates, release channels (stable/latest)
- Team enforcement via `.claude/settings.json`
- Enterprise controls (`strictKnownMarketplaces`)
- Container pre-population via `CLAUDE_CODE_PLUGIN_SEED_DIR`

### Key Resources
- [Official Docs: Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
- [Create plugins](https://code.claude.com/docs/en/plugins)
- [Plugins reference (GitHub)](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)

---

## 5. Paid Marketplaces

### AgentPowers.ai
- **URL:** https://agentpowers.ai/
- **Model:** Premium/paid marketplace
- **What:** First paid marketplace for Claude Code skills. Creators publish, sell, and distribute SKILL.md packages.
- **Target:** Claude Code, Cursor, Codex users
- **Pricing:** One-time purchase, subscription (~$29/mo cited), or licensing

### Agensi.io
- **URL:** https://www.agensi.io/
- **Workflow:** Build skill → test across agents → submit to marketplace → set price
- **Guide:** [How to Sell AI Agent Skills](https://www.agensi.io/learn/sell-ai-agent-skills-creator-guide)

### Other Platforms
| Platform | URL | Model |
|----------|-----|-------|
| claudeskillsmarket.com | https://www.claudeskillsmarket.com/ | Free & paid, business-focused |
| claudeskills.info | https://claudeskills.info/skills/ | Free, 140+ skills |
| claudemarketplaces.com | https://claudemarketplaces.com/ | Community directory with voting |
| SkillsLLM.com | https://skillsllm.com/ | Free, 1,600+ security-vetted skills |
| MCP Market | https://mcpmarket.com/tools/skills/leaderboard | Leaderboard + publishing tools |

### Monetization Strategies
- **One-time purchase** — Sell SKILL.md packages directly
- **Subscription** — Recurring access (~$29/mo cited by creators)
- **Licensing** — Clients get SKILL.md files to run on their own servers
- **Hosted access** — Keep source code private, provide hosted execution (Agent37 model)

### Key Resources
- [Agent37: How to Monetize Claude Code Skills](https://www.agent37.com/blog/monetize-claude-code-skills)
- [Medium: How to Sell Claude Skills as a Subscription](https://medium.com/activated-thinker/how-to-sell-claude-skills-as-a-subscription-product-without-coding-the-non-developer-playbook-449a98018cac)
- [Panaversity: From Skills to Business](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/from-skills-to-business)

---

## 6. Trending Strategy

### Phase 1: Build a High-Quality Skill
1. **Solve a real, specific problem** — Top trending skills address high-demand needs (frontend design, React best practices, deployment)
2. **Follow the SKILL.md spec** — Proper YAML frontmatter with `name`, `description`, clear trigger conditions
3. **Make it cross-platform** — skills.sh supports 19+ agents; more compatibility = more installs
4. **Include proper metadata** — `keywords`, `category`, `tags` for discoverability
5. **Write excellent instructions** — [Analysis of top 100 skills](https://weber-stephen.medium.com/i-analyzed-the-top-100-claude-code-skills-d624d6e02541) identified 9 principles separating working skills from failures:
   - Be specific, not generic
   - Include examples and templates
   - Define clear trigger conditions
   - Provide error handling guidance
   - Keep instructions concise but complete

### Phase 2: Multi-Platform Distribution

Publish to **all** platforms simultaneously:

| Platform | Action |
|----------|--------|
| **GitHub** | Public repo with SKILL.md files — foundation for everything |
| **skills.sh** | Get indexed via GitHub (proper repo structure) |
| **ClawHub** | `clawhub sync --all` |
| **Claude Code Marketplace** | Create marketplace.json, `/plugin marketplace add` |
| **Awesome lists** | PRs to [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) (22k+ stars), [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) |
| **MCP Market** | List on [mcpmarket.com](https://mcpmarket.com/tools/skills/leaderboard) |
| **Paid channels** | List on AgentPowers.ai or Agensi.io |
| **SkillsLLM** | Submit for security vetting |

### Phase 3: Drive Initial Traction

The key metric for trending is **install count and velocity**:

1. **Blog/Content** — Write about your skill on Medium, Dev.to, or personal blog
2. **Reddit** — Post to r/ClaudeAI, r/ClaudeCode, r/PromptEngineering, r/aiagents, r/GithubCopilot
3. **Hacker News** — "Show HN" posts get traction (e.g., [Skills Registry showcase](https://news.ycombinator.com/item?id=46721900))
4. **X/Twitter** — The AI coding community is very active; tag relevant tools/companies
5. **YouTube** — Tutorial/walkthrough videos
6. **Cross-promote** — If your skill integrates with popular tools (Stripe, Supabase, Vercel), tag them
7. **Community sessions** — Participate in Vercel community sessions and similar events

### Phase 4: Maintain Momentum
- **Iterate quickly** based on user feedback
- **Version properly** — Use semver in `plugin.json` and marketplace entries
- **Respond to issues** on GitHub promptly
- **Keep security clean** — Skills with security flags get buried
- **Track your ranking** via:
  - [trending-skills tracker](https://github.com/geekjourneyx/trending-skills)
  - [Shareuhack Skills Ranking](https://www.shareuhack.com/en/tools/claude-skills-ranking)
  - [MCP Market Leaderboard](https://mcpmarket.com/tools/skills/leaderboard)

---

## 7. What Top Skills Have in Common

### skills.sh Leaderboard (as of 2026-05-07)

| Rank | Skill | Installs | Publisher | Why it trends |
|------|-------|----------|-----------|---------------|
| 1 | find-skills | 1.3M | Vercel | Meta-skill that discovers other skills |
| 2 | vercel-react-best-practices | 372K | Vercel | Official React guidance |
| 3 | frontend-design | 369K | Anthropic | Official Anthropic skill |
| 4-10 | azure-* | ~290K each | Microsoft | Official Azure integration |
| 30 | skill-creator | 184K | Anthropic | Official skill-building tool |
| 49 | ui-ux-pro-max | 147K | Community | High-quality UI/UX guidance |
| 51 | supabase-postgres-best-practices | 143K | Supabase | Official Supabase guidance |
| 53 | brainstorming | 137K | obra/superpowers | Community favorite workflow |
| 54 | shadcn | 125K | shadcn/ui | Massive existing user base |
| 58 | caveman | 109K | Community | Unique approach to coding |
| 70 | seo-audit | 98K | Community | Specific marketing pain point |
| 72 | pdf | 94K | Anthropic | Official document handling |

### ClawHub Top Skills

| Skill | Installs | Why it trends |
|-------|----------|---------------|
| Self-Improving Agent | 422.7K | Captures learnings for continuous improvement |
| Skill Vetter | 230.8K | Security-first skill vetting |
| Github | 171.2K | Essential developer tool |
| Gog (Google Workspace) | 168.3K | High-demand integration |
| Weather | 145.4K | Simple, universally useful |
| Multi Search Engine | 135.3K | 16 engines, broad appeal |

### Patterns for Success
- **Official skills from major companies** dominate the top (Anthropic, Vercel, Microsoft, Supabase, shadcn)
- **Community skills break through** by solving specific pain points extremely well (brainstorming, caveman, seo-audit, ui-ux-pro-max)
- **Meta-tools** (find-skills, skill-creator, skill-vetter) get massive installs because they're universally useful
- **Integration skills** for popular platforms (GitHub, Google, Supabase, Azure) consistently rank high

---

## 8. Recommendations for fire-skills

Given the existing skills in this repo (`innate-frontend`, `desktop-app`, `git-workflow`, `local-workflow`, etc.):

### Immediate Actions
1. **Publish to skills.sh first** — Largest cross-platform reach (91K+ skills, 19 agents)
2. **Create a Claude Code marketplace** using `marketplace.json` for team/enterprise distribution
3. **Submit to ClawHub** for the OpenClaw user base (180K users)
4. **Cross-list on MCP Market** and awesome lists

### Priority Skills to Publish
- **`innate-frontend`** — Most differentiated (57+ UI components, 7 Landing blocks, OKLCH themes, Next.js + React 19 + Tailwind CSS v4). This has the best chance to trend as it fills a specific, high-demand niche.
- **`desktop-app`** — Tauri v2 + Next.js desktop app template is unique in the ecosystem
- **`git-workflow`** — GitHub Issue-driven workflow is a specific pain point solver

### Promotion Strategy
- Write a blog post about the innate-frontend component library as a Claude Code skill
- Post to r/ClaudeAI, r/ClaudeCode, r/NextJS
- Create a YouTube walkthrough showing the skill in action
- Submit "Show HN" to Hacker News
- Tag relevant ecosystem tools (@vercel, @tailwindcss) on X/Twitter

### Monetization Path
1. Start with **free distribution** to build install count and trending momentum
2. Once established, consider **premium tiers** on AgentPowers.ai or Agensi.io
3. Offer **subscription access** for advanced skills (desktop-app, learning-mode)
4. **Licensing model** for enterprise use of the full skill suite

---

## 9. Sources

### Official Documentation
- [skills.sh — The Agent Skills Directory](https://skills.sh/)
- [skills.sh Docs](https://skills.sh/docs)
- [ClawHub — OpenClaw Skills Registry](https://clawhub.ai)
- [Create and distribute a plugin marketplace — Claude Code Docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [Create plugins — Claude Code Docs](https://code.claude.com/docs/en/plugins)
- [OpenClaw Skills Documentation](https://docs.openclaw.ai/tools/skills)
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [Agent Skills — Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

### Paid Marketplaces
- [AgentPowers.ai](https://agentpowers.ai/)
- [Agensi.io — How to Sell AI Agent Skills](https://www.agensi.io/learn/sell-ai-agent-skills-creator-guide)
- [Agent37 — How to Monetize Claude Code Skills](https://www.agent37.com/blog/monetize-claude-code-skills)
- [claudeskillsmarket.com](https://www.claudeskillsmarket.com/)

### Directories & Leaderboards
- [MCP Market Skills Leaderboard](https://mcpmarket.com/tools/skills/leaderboard)
- [Shareuhack Skills Ranking](https://www.shareuhack.com/en/tools/claude-skills-ranking)
- [awesome-claude-skills (22k+ stars)](https://github.com/travisvn/awesome-claude-skills)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [SkillsLLM.com](https://skillsllm.com/)
- [clawskills.sh](https://clawskills.sh/)

### Tracking & Analytics
- [trending-skills GitHub Tracker](https://github.com/geekjourneyx/trending-skills)
- [GitHub Ranking AI — Top 100 Claude Skills](https://github.com/yuxiaopeng/Github-Ranking-AI/blob/main/Top100/Claude.md)

### Tutorials & Guides
- [Community Session: How to create and publish skills](https://www.youtube.com/watch?v=jJUuuYuEykk)
- [I analyzed the top 100 Claude Code Skills — Medium](https://weber-stephen.medium.com/i-analyzed-the-top-100-claude-code-skills-d624d6e02541)
- [Best Claude Code Skills to Try in 2026 — Firecrawl](https://www.firecrawl.dev/blog/best-claude-code-skills)
- [DataCamp: How to Build Claude Code Plugins](https://www.datacamp.com/tutorial/how-to-build-claude-code-plugins)
- [just-be.dev: Why I Built a Claude Code Plugin Marketplace](https://just-be.dev/blog/why-i-built-a-claude-code-plugin-marketplace/)
- [GitHub: vercel-labs/skills](https://github.com/vercel-labs/skills)
- [GitHub: sanshao85/claude-skills-guide (publish.sh)](https://github.com/sanshao85/claude-skills-guide/blob/main/publish.sh)

### Community Discussions
- [Reddit: Claude Code Skills Actually Worth Installing](https://www.reddit.com/r/claude/comments/1s51b5u/the_claude_code_skills_actually_worth_installing/)
- [Reddit: Where to Find AI Agent Skills](https://www.reddit.com/r/aiagents/comments/1r66sab/guide_where_to_find_ai_agent_skills_openclaw/)
- [Reddit: I Built a Marketplace for Selling SKILL.md Packages](https://www.reddit.com/r/PromptEngineering/comments/1sm660j/i_built_a_marketplace_for_selling_claude_code/)
- [Reddit: Introducing Claude Code Plugins in Public Beta](https://www.reddit.com/r/ClaudeAI/comments/1o2bj9l/introducing_claude_code_plugins_in_public_beta/)
- [Hacker News: Show HN — A Registry for Curated Claude Skills](https://news.ycombinator.com/item?id=46721900)

### Security
- [OpenClaw Skill Marketplace Emerges as Active Malware Vector — Socket.dev](https://socket.dev/blog/openclaw-skill-marketplace-emerges-as-active-malware-vector)
