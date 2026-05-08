# Research: Skill Feeds Site — APIs, Aggregation & Benchmarking

**Date:** 2026-05-07

## Table of Contents

1. [Skills.sh API & Data](#1-skillssh-api--data)
2. [ClawHub (OpenClaw) API & Data](#2-clawhub-openclaw-api--data)
3. [Other Aggregation Sources](#3-other-aggregation-sources)
4. [SKILL.md Format & Programmatic Collection](#4-skillmd-format--programmatic-collection)
5. [PromptFoo for Skill Benchmarking](#5-promptfoo-for-skill-benchmarking)
6. [Existing Benchmark Frameworks](#6-existing-benchmark-frameworks)
7. [Sources](#7-sources)

---

## 1. Skills.sh API & Data

### Overview
Skills.sh is powered by **mastra-ai/skills-api**, a fully open-source API server. This is the primary data source for skill aggregation.

- **Repository:** [github.com/mastra-ai/skills-api](https://github.com/mastra-ai/skills-api)
- **Scale:** 34,000+ skills from 2,800+ repositories
- **Also usable as:** `@mastra/skills-api` npm package for direct data access
- **CLI source:** [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)

### Available API Endpoints (port 3456)

| Endpoint | Description |
|----------|-------------|
| `GET /api/skills` | List and search skills (paginated). Params: `query`, `owner`, `repo`, `sortBy` (name/installs), `sortOrder`, `page`, `pageSize` (max 100) |
| `GET /api/skills/top` | Top skills by installs |
| `GET /api/skills/:skillId` | Skill by ID |
| `GET /api/skills/:owner/:repo/:skillId` | Skill by source and ID |
| `GET /api/skills/:owner/:repo/:skillId/files` | Skill file contents from GitHub |
| `GET /api/skills/:owner/:repo/:skillId/content` | Parsed SKILL.md from GitHub |
| `GET /api/skills/by-source/:owner/:repo` | All skills from a repo |
| `GET /api/skills/sources` | All source repositories with counts |
| `GET /api/skills/sources/top` | Top sources by installs |
| `GET /api/skills/owners` | All owners with counts |
| `GET /api/skills/agents` | Supported AI agents |
| `GET /api/skills/stats` | Registry statistics |

### npm Package Usage
```js
import { skills, metadata, getTopSkills, supportedAgents, fetchSkillFromGitHub } from '@mastra/skills-api';
```

### Data Refresh Options
- Manual: `pnpm scrape`
- Scheduled: `AUTO_REFRESH=true` (configurable interval, minimum 5 minutes)
- Admin API: `POST /api/admin/refresh`

### Ranking System
Skills are ranked by anonymous telemetry from the `skills` CLI — aggregated install counts only. Three views: All Time, Trending (24h), Hot.

### Storage
Supports S3-compatible storage (AWS, MinIO, Cloudflare R2) for production deployments.

---

## 2. ClawHub (OpenClaw) API & Data

### Overview
ClawHub is open source at [github.com/openclaw/clawhub](https://github.com/openclaw/clawhub). Uses Convex for backend (DB + file storage + HTTP actions) with GitHub OAuth.

- **Scale:** 52.7k tools, 180k users, 12M downloads, 4.8 avg rating
- **Search:** OpenAI embeddings (`text-embedding-3-small`) + Convex vector search (semantic, not just keyword)
- **Features:** Browse, publish, version, search, star, comment, moderation/approval, install telemetry

### CLI Tool (`clawhub`)

```bash
clawhub search <query>      # Discover skills
clawhub explore             # Browse skills
clawhub install <slug>      # Install a skill
clawhub uninstall <slug>    # Uninstall
clawhub skill publish <path> # Publish a skill
clawhub sync                # Sync/publish updates
clawhub skill rename        # Canonicalize
clawhub skill merge         # Merge duplicates
clawhub package publish <source> # Publish plugins
```

### API Schema
Defined in `packages/schema` (`clawhub-schema`). Exposes Convex HTTP actions for all operations.

### Security
Includes security analysis checking skill metadata declarations against actual behavior. 341+ malicious skills identified as of Feb 2026 ([PurpleBox Security report](https://www.prplbx.com/blog/agent-skills-supply-chain)).

---

## 3. Other Aggregation Sources

| Source | Type | Notes |
|--------|------|-------|
| [SkillsDirectory.com](https://www.skillsdirectory.com/api-docs) | Third-party API | Free tier: 100 req/day. Security-tested skills. |
| [MCP Market](https://mcpmarket.com/tools/skills) | Directory | Agent skills leaderboard for Claude, ChatGPT, Codex |
| [Awesome Skills](https://www.awesomeskills.dev/en) | Curated atlas | Reusable agent skills across platforms |
| [OneSkill](https://oneskill.dev/) | Directory | Verified skills directory |
| [LobeHub Skills](https://lobehub.com/skills) | Browse directory | Claude Code, Codex CLI, ChatGPT compatible |
| [Atmos](https://atmos.tools/ai/agent-skills) | Cross-platform | Portable skills for Claude Code, Gemini, Codex, Cursor, Windsurf |
| [SkillsLLM.com](https://skillsllm.com/) | Security-vetted | 1,600+ skills, Claude/Codex/ChatGPT |
| [claudeskills.info](https://claudeskills.info/skills/) | Free marketplace | 140+ skills |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | GitHub repo | 232+ skills |

---

## 4. SKILL.md Format & Programmatic Collection

### SKILL.md Structure

```markdown
---
name: my-skill
description: What this skill does and when to use it
metadata: {"openclaw": {"requires": {"env": ["API_KEY"], "bins": ["curl"]}}}
---

# My Skill

Instructions for the agent...
```

### Required Frontmatter
- `name` — unique identifier (lowercase, hyphens)
- `description` — what the skill does (agents use this for activation decisions)

### Optional Frontmatter (Claude Code extensions)
- `when_to_use`, `argument-hint`, `arguments`
- `disable-model-invocation`, `user-invocable`
- `allowed-tools`, `model`, `effort`
- `context: fork`, `agent`
- `hooks`, `paths`, `shell`

### Collection Approaches

1. **mastra-ai/skills-api scraper** — Self-host, run `scrapeAndSave()`. Crawls GitHub repos for SKILL.md files.
2. **Skills.sh CLI** — `npx skills find <query>` for interactive/keyword search.
3. **GitHub API scanning** — Skills live in standard locations (`skills/`, `.claude/skills/`). The `vercel-labs/skills` CLI discovers them.
4. **ClawHub CLI** — `clawhub search` for semantic search.
5. **Direct GitHub fetch** — `fetchSkillFromGitHub(owner, repo, skillId)` returns parsed SKILL.md content.

### Unified Schema for Aggregation

```
{
  name: string,
  description: string,
  owner: string,
  repo: string,
  installs: number,
  source: "skills.sh" | "clawhub" | "skillsdirectory" | ...,
  content: string,          // full SKILL.md text
  metadata: object,         // parsed frontmatter metadata
  rating?: number,          // ClawHub only
  downloads?: number,       // ClawHub only
  security_scan?: object,   // security analysis results
  fetched_at: timestamp
}
```

---

## 5. PromptFoo for Skill Benchmarking

### What is PromptFoo
Open-source CLI/library for evaluating and red-teaming LLM applications. Recently acquired by OpenAI. Runs locally, supports 50+ providers including Anthropic Claude. Evaluates prompts through a **matrix**: every prompt × every provider × every test case.

### Core Architecture

```
Configuration (YAML)
├── providers:    # LLM backends (anthropic, openai, custom)
├── prompts:      # Templates with {{variable}} placeholders (Nunjucks)
├── tests:        # Test cases with vars + assertions
└── scenarios:    # Grouped test suites that matrix vars × tests
```

### Assertion Types for Skill Benchmarking

**Deterministic (no LLM needed):**
- `equals`, `contains`, `regex` — exact output matching
- `is-json`, `contains-json` — structure validation
- `javascript`, `python` — custom code validation
- `latency`, `cost` — performance thresholds
- `levenshtein`, `rouge-n`, `bleu` — text similarity

**Model-assisted (LLM grades output):**
- `llm-rubric` — LLM grades against a rubric description
- `similar` — cosine similarity via embeddings
- `g-eval` — chain-of-thought evaluation
- `factuality` — factual accuracy checking
- `classifier` — classification-based scoring

**Agent-specific:**
- `trajectory:tool-used` — checks specific tools were called
- `trajectory:tool-sequence` — validates tool call ordering
- `trajectory:step-count` — agent step efficiency
- `trajectory:goal-success` — goal completion check

### Mapping Skills to PromptFoo

| Skill Concept | PromptFoo Equivalent |
|---|---|
| Skill description | The `prompt` under test |
| Skill workflows | Test cases with workflow-specific inputs |
| Expected behavior | Assertions validating output quality |
| Edge cases | Additional test cases with adversarial inputs |
| Skill scripts | Custom providers or assertion functions |

### Example Config for Skill Benchmarking

```yaml
providers:
  - anthropic:messages:claude-sonnet-4-5-20250929

prompts:
  - file://prompts/skill-execute.txt

tests:
  - description: "Happy path - basic execution"
    vars:
      skill_name: "qa"
      task: "User reports login button doesn't work"
    assert:
      - type: llm-rubric
        value: "Response follows the QA skill workflow"
        metric: correctness
      - type: javascript
        value: "output.includes('gh issue create')"
        metric: tool_usage
      - type: latency
        threshold: 60000
        metric: efficiency

  - description: "Edge case - vague report"
    vars:
      skill_name: "qa"
      task: "It's broken"
    assert:
      - type: llm-rubric
        value: "Agent asks clarifying questions"
```

### Scaling Test Generation
- Dynamic test generation via Python/JS functions
- Dataset generation feature for expanding coverage
- `maxConcurrency` for parallelism (default: 4)
- Disk-based caching to avoid redundant API calls
- `repeat` option for statistical significance
- CI/CD integration for automated regression

### Custom Provider for Claude Code Agent
Write a custom JavaScript/Python provider that:
1. Takes skill name + task as input
2. Invokes Claude Code agent with the skill loaded
3. Captures full agent output (tool calls, reasoning, final response)
4. Returns structured output for assertion evaluation

---

## 6. Existing Benchmark Frameworks

### Four-Dimension Evaluation Framework
(From existing `tasks/analysis/benchmark/skill-benchmarking-strategy.md`)

| Dimension | What it measures | PromptFoo mapping |
|-----------|-----------------|-------------------|
| **Correctness** | Does the skill produce correct results? | `llm-rubric`, `factuality`, `equals` |
| **Efficiency** | Speed, cost, token usage | `latency`, `cost`, `trajectory:step-count` |
| **Discoverability** | Does the agent activate the right skill? | Test cases checking trigger accuracy |
| **Robustness** | Handles edge cases, adversarial inputs | Custom assertions, `javascript`/`python` |

### Named Benchmark Projects
- **Skillmark** — Skill benchmarking framework
- **SkillsBench** — Multi-skill evaluation
- **PinchBench** — Pinch-point testing for skills

---

## 7. Sources

### APIs & Data
- [mastra-ai/skills-api (GitHub)](https://github.com/mastra-ai/skills-api) — Open-source API for skills.sh
- [vercel-labs/skills (GitHub)](https://github.com/vercel-labs/skills) — Skills CLI
- [openclaw/clawhub (GitHub)](https://github.com/openclaw/clawhub) — Open-source ClawHub
- [SkillsDirectory.com API Docs](https://www.skillsdirectory.com/api-docs)
- [skills.sh](https://skills.sh/)
- [clawhub.ai](https://clawhub.ai/)

### Benchmarking
- [PromptFoo Docs — Intro](https://www.promptfoo.dev/docs/intro/)
- [PromptFoo — Configuration Guide](https://www.promptfoo.dev/docs/configuration/guide/)
- [PromptFoo — Assertions & Metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)
- [PromptFoo — Configuration Reference](https://www.promptfoo.dev/docs/configuration/reference/)
- [PromptFoo — Custom Providers](https://www.promptfoo.dev/docs/providers/custom-api/)
- [PromptFoo — CI/CD Integration](https://www.promptfoo.dev/docs/integrations/ci-cd/)
- [PromptFoo GitHub](https://github.com/promptfoo/promptfoo)
- [Rate Your Claude Code Skills (mager.co)](https://mager.co/blog/2026-02-23-skills-validate-eval/)

### Security
- [PurpleBox Security — Agent Skills Supply Chain](https://www.prplbx.com/blog/agent-skills-supply-chain)
- [Socket.dev — OpenClaw Malware Vector](https://socket.dev/blog/openclaw-skill-marketplace-emerges-as-active-malware-vector)
