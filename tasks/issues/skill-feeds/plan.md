# Plan: Skill Feeds Site

**Date:** 2026-05-07
**Based on:** [research.md](./research.md) | [marketplace research](../../analysis/skill-marketplace-trending-research.md)

## Table of Contents

1. [Vision & Goals](#1-vision--goals)
2. [Architecture Overview](#2-architecture-overview)
3. [Tech Stack](#3-tech-stack)
4. [Data Layer — Aggregation Pipeline](#4-data-layer--aggregation-pipeline)
5. [Skill Benchmarking with PromptFoo](#5-skill-benchmarking-with-promptfoo)
6. [Site Features](#6-site-features)
7. [Scalability Design](#7-scalability-design)
8. [Implementation Phases](#8-implementation-phases)
9. [File Structure](#9-file-structure)
10. [Open Questions](#10-open-questions)

---

## 1. Vision & Goals

### What
A Skill Feeds Site that aggregates AI agent skills from multiple marketplaces (skills.sh, ClawHub, etc.), displays trending data, and benchmarks skill quality using PromptFoo.

### Goals
1. **Aggregate** — Collect skills from skills.sh, ClawHub, and other registries into a unified index
2. **Rank** — Show trending, popular, and new skills with cross-marketplace install/rating data
3. **Benchmark** — Run PromptFoo evaluations against skills to produce quality scores
4. **Compare** — Let users compare skills side-by-side with benchmark results
5. **Self-promote** — Feature fire-skills alongside community skills with benchmark-backed quality signals

### Target Users
- AI agent users looking for the best skills
- Skill developers tracking their ranking and quality
- The fire-skills project itself (distribution and credibility)

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                   Skill Feeds Site                    │
│              (Next.js + React 19 + Tailwind)          │
├─────────────┬───────────────┬────────────────────────┤
│  Feed UI    │  Benchmark UI │  Skill Detail Pages    │
│  (trending, │  (scores,     │  (content, source,     │
│   popular)  │   comparisons)│   install, benchmark)  │
├─────────────┴───────────────┴────────────────────────┤
│                   API Layer (tRPC)                    │
├─────────────────────────┬────────────────────────────┤
│    Aggregation Service  │   Benchmark Service        │
│  (scheduled collection  │  (PromptFoo runner,        │
│   from marketplaces)    │   result storage)          │
├─────────────────────────┴────────────────────────────┤
│              Database (PostgreSQL + pgvector)          │
├───────────────────────────────────────────────────────┤
│              Data Sources                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │
│  │skills.sh │ │ ClawHub  │ │ SkillsDir│ │ GitHub  │ │
│  │ (mastra  │ │ (Convex  │ │  (API)   │ │ (SKILL  │ │
│  │  API)    │ │  API)    │ │          │ │  repos) │ │
│  └──────────┘ └──────────┘ └──────────┘ └─────────┘ │
└───────────────────────────────────────────────────────┘
```

---

## 3. Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| **Framework** | Next.js 15 (App Router) | SSR for SEO, API routes, React Server Components |
| **UI** | React 19 + Tailwind CSS v4 | Matches fire-skills stack, fast rendering |
| **Components** | @innate/ui | Use the project's own component library (dogfooding) |
| **API** | tRPC | Type-safe API layer, end-to-end TypeScript |
| **Database** | PostgreSQL + pgvector | Relational data + vector search for skill similarity |
| **ORM** | Drizzle ORM | Lightweight, type-safe, good migration support |
| **Cache** | Redis (Upstash) | Rate limiting, API caching, session management |
| **Aggregation** | Custom scraper service | Scheduled data collection from marketplaces |
| **Benchmarking** | PromptFoo | Skill quality evaluation engine |
| **Deployment** | Vercel + Supabase | Serverless, scales to zero, managed Postgres |
| **Auth** | NextAuth.js (optional) | GitHub OAuth for skill submissions |

---

## 4. Data Layer — Aggregation Pipeline

### 4.1 Data Sources & Collection

| Source | Method | Frequency | Data |
|--------|--------|-----------|------|
| **skills.sh** | Self-host `mastra-ai/skills-api` or call their API | Every 6h | Skills, installs, trending, owners, repos |
| **ClawHub** | `clawhub search` CLI or Convex HTTP API | Every 6h | Skills, ratings, downloads, security scans |
| **SkillsDirectory** | REST API (free: 100 req/day) | Daily | Security-tested skills |
| **GitHub** | GitHub API for SKILL.md repos | Weekly | New repos, updated content |

### 4.2 Unified Skill Schema

```typescript
interface Skill {
  id: string;                    // composite: source + owner + repo + name
  name: string;
  description: string;
  content: string;               // full SKILL.md text
  owner: string;
  repo: string;
  source: "skills.sh" | "clawhub" | "skillsdirectory" | "github" | "fire-skills";
  sourceUrl: string;             // link to original listing

  // Metrics (from marketplaces)
  installs: number;
  downloads: number;             // ClawHub
  rating: number;                // ClawHub
  trending24h: number;           // skills.sh trending rank
  allTimeRank: number;           // skills.sh all-time rank

  // Metadata
  agents: string[];              // supported AI agents
  categories: string[];
  tags: string[];
  securityScan?: SecurityScanResult;

  // Benchmark (our data)
  benchmark?: BenchmarkResult;

  // Timestamps
  fetchedAt: Date;
  updatedAt: Date;
  publishedAt: Date;
}
```

### 4.3 Aggregation Service Architecture

```
Aggregation Scheduler (cron)
├── skills.sh collector
│   ├── Fetch /api/skills (paginated)
│   ├── Fetch /api/skills/top (rankings)
│   └── Fetch trending/hot data
├── ClawHub collector
│   ├── clawhub search (broad queries)
│   └── Fetch ratings + download counts
├── Normalizer
│   ├── Map to unified schema
│   ├── Deduplicate (same skill on multiple platforms)
│   └── Merge metrics across sources
└── Storage
    ├── Upsert into PostgreSQL
    └── Update vector embeddings (pgvector)
```

### 4.4 Deduplication Strategy
Same skill often appears on multiple platforms. Merge strategy:
1. Match by `owner/repo/name` (GitHub-based identity)
2. If match found, merge metrics (sum installs, keep highest rating)
3. If no match, create new entry with source tag
4. Maintain `sources[]` array to track cross-platform presence

---

## 5. Skill Benchmarking with PromptFoo

### 5.1 Benchmark Dimensions

| Dimension | What it measures | PromptFoo assertion types |
|-----------|-----------------|--------------------------|
| **Correctness** | Produces correct, useful output | `llm-rubric`, `factuality`, `equals` |
| **Efficiency** | Speed, cost, minimal steps | `latency`, `cost`, `trajectory:step-count` |
| **Discoverability** | Agent activates skill at the right time | Trigger accuracy test cases |
| **Robustness** | Handles edge cases gracefully | Custom JS/Python assertions |

### 5.2 Benchmark Score Model

```
Overall Score = weighted average of dimensions
  Correctness:   40% weight
  Efficiency:    20% weight
  Discoverability: 20% weight
  Robustness:    20% weight

Each dimension: 0-100 scale
Overall: 0-100 scale

Grade: A (90+), B (80+), C (70+), D (60+), F (<60)
```

### 5.3 Benchmark Pipeline

```
Benchmark Runner (PromptFoo)
├── Test Case Generator
│   ├── Read SKILL.md content
│   ├── Parse description, triggers, workflows
│   └── Generate test cases (happy path + edge cases)
├── Provider Layer
│   ├── Anthropic Claude (primary)
│   ├── OpenAI GPT (secondary comparison)
│   └── Custom provider (wraps agent execution)
├── Assertion Suite
│   ├── Correctness assertions (llm-rubric)
│   ├── Efficiency assertions (latency, step-count)
│   ├── Trigger assertions (does the skill activate?)
│   └── Robustness assertions (edge cases)
├── Result Aggregator
│   ├── Collect scores per dimension
│   ├── Calculate weighted overall score
│   └── Store results with timestamps
└── Report Generator
    ├── Per-skill benchmark report
    ├── Cross-skill comparison table
    └── Trend over time (improving/regressing)
```

### 5.4 Test Case Generation

Automatic test generation from SKILL.md content:

```yaml
# Generated from SKILL.md frontmatter
scenarios:
  - config:
      - vars: { skill: "frontend-design", source: "anthropics/skills" }
      - vars: { skill: "shadcn", source: "shadcn/ui" }
    tests:
      # Correctness
      - description: "Happy path execution"
        vars: { task: "Build a responsive navbar" }
        assert:
          - type: llm-rubric
            value: "Output follows skill's documented workflow"
            metric: correctness

      # Discoverability
      - description: "Trigger accuracy - should activate"
        vars: { task: "Design a login form" }
        assert:
          - type: llm-rubric
            value: "Agent correctly activates this skill"
            metric: discoverability

      # Robustness
      - description: "Edge case - vague request"
        vars: { task: "Make it look better" }
        assert:
          - type: llm-rubric
            value: "Agent handles vague input gracefully"
            metric: robustness
```

### 5.5 Benchmark Schedule
- **Full benchmark:** Weekly (all skills, all dimensions)
- **Quick benchmark:** Daily (top 100 trending skills, correctness only)
- **On-demand:** When a new skill is submitted or updated
- **CI integration:** On PR for fire-skills internal skills

### 5.6 Custom Provider for Agent Execution

```typescript
// Custom PromptFoo provider that wraps Claude Code agent execution
const claudeCodeProvider = {
  id: () => 'claude-code-agent',
  callApi: async (prompt, context, options) => {
    const skillName = context.vars.skill;
    const task = context.vars.task;
    // Execute Claude Code with the skill loaded
    // Capture tool calls, reasoning, final response
    return { output: agentOutput, tokenUsage, cost };
  }
};
```

---

## 6. Site Features

### 6.1 Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Trending skills, benchmark highlights, search |
| Trending | `/trending` | Skills gaining installs fastest (24h/7d/30d) |
| Popular | `/popular` | All-time most installed skills |
| Newest | `/newest` | Recently added skills |
| Benchmarked | `/benchmarked` | Skills with benchmark scores |
| Skill Detail | `/skill/:id` | Full skill info: content, installs, benchmark, source |
| Compare | `/compare` | Side-by-side skill comparison (up to 4) |
| Categories | `/categories` | Skills organized by category |
| Search | `/search?q=` | Full-text + vector search |
| About | `/about` | Methodology, scoring, sources |

### 6.2 Skill Detail Page
Each skill page shows:
- SKILL.md content (rendered markdown)
- Source marketplace links
- Install/download counts from all sources
- Benchmark scores with dimension breakdown (radar chart)
- Benchmark history (trend over time)
- Related/similar skills
- Security scan status

### 6.3 Comparison View
Select 2-4 skills to compare:
- Side-by-side benchmark scores
- Install counts across platforms
- Feature overlap matrix
- Pricing (if paid)

### 6.4 Feed/API
- JSON feed of trending skills (for integration)
- RSS feed for new skills
- REST API for programmatic access

---

## 7. Scalability Design

### 7.1 Database

```
PostgreSQL + pgvector
├── skills (main table, ~100K rows)
│   ├── indexes: name, owner, source, installs, rating, trending24h
│   └── vector column: embedding (for similarity search)
├── skill_metrics (time series)
│   ├── daily snapshots: installs, trending_rank, downloads
│   └── index: skill_id, date
├── benchmark_results
│   ├── per-skill, per-dimension scores
│   └── index: skill_id, run_date
├── skill_sources (cross-platform mapping)
│   └── maps skill to multiple marketplace listings
└── benchmark_runs
    └── metadata about each benchmark execution
```

### 7.2 Caching Strategy

| Data | Cache TTL | Storage |
|------|-----------|---------|
| Skill listings (popular) | 1 hour | Redis + Next.js ISR |
| Skill detail | 15 min | Redis + Next.js ISR |
| Trending data | 5 min | Redis |
| Benchmark scores | 24 hours | Redis + DB |
| Search results | 10 min | Redis |

### 7.3 Aggregation Scaling
- **Phase 1 (0-10K skills):** Single server, cron-based collection
- **Phase 2 (10K-100K):** Queue-based collection (BullMQ + Redis), parallel collectors
- **Phase 3 (100K+):** Event-driven collection, webhook integrations with marketplaces

### 7.4 Benchmark Scaling
- **Phase 1:** Sequential PromptFoo runs, ~50 skills/day
- **Phase 2:** Parallel runners with `maxConcurrency`, ~500 skills/day
- **Phase 3:** Distributed runners across multiple machines, full coverage

### 7.5 Performance Budget
- Homepage: < 2s LCP
- Skill detail: < 1.5s LCP
- Search: < 500ms response
- API: < 200ms p95

---

## 8. Implementation Phases

### Phase 1 — Foundation (Week 1-2)
- [ ] Set up Next.js project with App Router
- [ ] Configure PostgreSQL + Drizzle ORM
- [ ] Build database schema and migrations
- [ ] Implement skills.sh aggregation (mastra-ai/skills-api)
- [ ] Basic skill listing page (trending + popular)
- [ ] Skill detail page

### Phase 2 — Benchmark Integration (Week 3-4)
- [ ] Set up PromptFoo in the project
- [ ] Build test case generator from SKILL.md
- [ ] Implement benchmark runner service
- [ ] Build benchmark score display (radar chart)
- [ ] Store and display benchmark history

### Phase 3 — Multi-Source & Search (Week 5-6)
- [ ] Add ClawHub aggregation
- [ ] Add SkillsDirectory aggregation
- [ ] Implement deduplication across sources
- [ ] Build full-text + vector search
- [ ] Skill comparison page

### Phase 4 — Feeds & Polish (Week 7-8)
- [ ] JSON/RSS feed endpoints
- [ ] REST API documentation
- [ ] SEO optimization (meta tags, structured data)
- [ ] Performance optimization (ISR, caching)
- [ ] Deploy to Vercel + Supabase

### Phase 5 — Community (Future)
- [ ] User accounts (GitHub OAuth)
- [ ] Skill submissions
- [ ] Reviews and ratings
- [ ] Benchmark requests (on-demand evaluation)
- [ ] Badge/widget for skill authors to embed

---

## 9. File Structure

```
skill-feeds/
├── apps/
│   └── web/                          # Next.js app
│       ├── app/
│       │   ├── page.tsx              # Home (trending)
│       │   ├── trending/page.tsx
│       │   ├── popular/page.tsx
│       │   ├── newest/page.tsx
│       │   ├── benchmarked/page.tsx
│       │   ├── skill/[id]/page.tsx   # Skill detail
│       │   ├── compare/page.tsx
│       │   ├── categories/page.tsx
│       │   ├── search/page.tsx
│       │   └── api/
│       │       ├── feed/json/route.ts
│       │       ├── feed/rss/route.ts
│       │       └── trpc/[trpc]/route.ts
│       ├── components/
│       │   ├── skill-card.tsx
│       │   ├── benchmark-radar.tsx
│       │   ├── skill-compare.tsx
│       │   └── search-bar.tsx
│       └── lib/
│           └── trpc.ts
├── packages/
│   ├── db/                           # Drizzle ORM
│   │   ├── schema/
│   │   │   ├── skills.ts
│   │   │   ├── metrics.ts
│   │   │   ├── benchmarks.ts
│   │   │   └── sources.ts
│   │   └── migrations/
│   ├── aggregator/                   # Data collection
│   │   ├── sources/
│   │   │   ├── skills-sh.ts
│   │   │   ├── clawhub.ts
│   │   │   └── skills-directory.ts
│   │   ├── normalizer.ts
│   │   ├── deduplicator.ts
│   │   └── scheduler.ts
│   ├── benchmark/                    # PromptFoo integration
│   │   ├── runner.ts
│   │   ├── test-generator.ts
│   │   ├── providers/
│   │   │   └── claude-code.ts
│   │   ├── assertions/
│   │   │   ├── correctness.ts
│   │   │   ├── efficiency.ts
│   │   │   ├── discoverability.ts
│   │   │   └── robustness.ts
│   │   └── scorer.ts
│   └── api/                          # tRPC routers
│       ├── routers/
│       │   ├── skills.ts
│       │   ├── benchmarks.ts
│       │   ├── search.ts
│       │   └── feeds.ts
│       └── trpc.ts
├── benchmarks/                       # PromptFoo test configs
│   ├── configs/
│   │   ├── correctness.yaml
│   │   ├── efficiency.yaml
│   │   ├── discoverability.yaml
│   │   └── robustness.yaml
│   └── results/                      # Stored benchmark outputs
├── package.json
├── turbo.json                        # Turborepo config
└── README.md
```

---

## 10. Open Questions

| # | Question | Options | Recommendation |
|---|----------|---------|---------------|
| 1 | Monorepo or separate repo? | a) Inside fire-skills monorepo b) New repo | **(a)** — keeps skills and feeds together, easier to benchmark internal skills |
| 2 | Self-host mastra-ai/skills-api or call skills.sh directly? | a) Self-host b) Call production API | **(a)** — full control, no rate limits, can customize scraper |
| 3 | Database hosting? | a) Supabase b) Neon c) Self-hosted Postgres | **(a)** — managed, free tier, pgvector support |
| 4 | Benchmark runner: local or cloud? | a) Local dev machine b) GitHub Actions c) Dedicated server | **(b)** — CI integration, scheduled runs, reproducible |
| 5 | PromptFoo: CLI or library? | a) CLI (`npx promptfoo eval`) b) Node.js library | **(b)** — programmatic control, result processing, no shell overhead |
| 6 | First data source priority? | a) skills.sh only b) skills.sh + ClawHub c) All sources | **(a)** first, then expand — 91K+ skills is enough for MVP |
| 7 | How to handle paid skills for benchmarking? | a) Skip b) Benchmark free version c) Purchase and benchmark | **(a)** initially — focus on open skills |
| 8 | Authentication needed? | a) No auth b) GitHub OAuth c) Full auth | **(a)** for MVP — add auth when community features are built |
