# Report: How to Build a Skill Hub — From Idea to Working Product

**Date:** 2026-05-08

You want to build a **Skill Hub** — a place to discover, evaluate, and integrate AI skills into your workflow. This report breaks down exactly what to do, step by step, using your existing project as the foundation.

---

## Table of Contents

1. [What You're Building](#1-what-youre-building)
2. [The Problem You're Solving](#2-the-problem-youre-solving)
3. [How to Get the Latest Skill Information](#3-how-to-get-the-latest-skill-information)
4. [How to Make Skills Searchable & Discoverable](#4-how-to-make-skills-searchable--discoverable)
5. [How to Evaluate Skills Quickly](#5-how-to-evaluate-skills-quickly)
6. [How to Integrate Into Your Workflow](#6-how-to-integrate-into-your-workflow)
7. [Concrete Step-by-Step Execution Plan](#7-concrete-step-by-step-execution-plan)
8. [Architecture Diagram](#8-architecture-diagram)
9. [Tech Choices & Why](#9-tech-choices--why)
10. [What to Do This Week](#10-what-to-do-this-week)

---

## 1. What You're Building

A **Skill Hub** that does 4 things:

```
DISCOVER ──→ SEARCH ──→ EVALUATE ──→ INTEGRATE
   │            │           │            │
   ▼            ▼           ▼            ▼
 Aggregate     Find the    Test quality  Add to your
 latest skills right skill  quickly      workflow
 from all                  with real
 marketplaces              benchmarks
```

This is NOT just a directory. It's an **active workflow tool** that helps you go from "I need a skill for X" to "I have a tested, integrated skill in my project" in minutes.

---

## 2. The Problem You're Solving

Right now, if you want to find and use a skill, you have to:

1. Go to skills.sh → browse → find something interesting
2. Go to ClawHub → browse → maybe find something else
3. Read the SKILL.md → decide if it's good
4. Install it → test it manually → decide if it works
5. Adapt it → integrate into your project

This takes **30-60 minutes per skill** and there are 91,000+ skills on skills.sh alone. You need a faster way.

**Your Skill Hub reduces this to 5 minutes per skill** by automating discovery, search, and evaluation.

---

## 3. How to Get the Latest Skill Information

### 3.1 Primary Data Source: mastra-ai/skills-api

The skills.sh directory is powered by an **open-source API** you can run yourself.

```bash
# Clone and run the skills.sh API locally
git clone https://github.com/mastra-ai/skills-api.git
cd skills-api
pnpm install
pnpm start
# API runs on http://localhost:3456
```

**This gives you 12 endpoints** to fetch skill data programmatically:

| What you need | API endpoint |
|---------------|-------------|
| All skills (paginated) | `GET /api/skills?page=1&pageSize=100` |
| Trending skills | `GET /api/skills?sortBy=installs&sortOrder=desc` |
| Top skills | `GET /api/skills/top` |
| Search by keyword | `GET /api/skills?query=react` |
| Skills by owner | `GET /api/skills/by-source/anthropics/skills` |
| Full SKILL.md content | `GET /api/skills/anthropics/skills/frontend-design/content` |
| All sources/repos | `GET /api/skills/sources` |
| Statistics | `GET /api/skills/stats` |

### 3.2 Secondary Data Source: ClawHub

```bash
# Install the ClawHub CLI
npm install -g clawhub

# Search skills
clawhub search "code review"

# Browse
clawhub explore
```

### 3.3 Automatic Data Refresh

Set up scheduled data collection so your hub always has the latest:

```bash
# In skills-api, enable auto-refresh
AUTO_REFRESH=true pnpm start
# Refreshes every 6 hours by default
```

Or use cron:
```bash
# Refresh every 6 hours
0 */6 * * * curl -X POST http://localhost:3456/api/admin/refresh
```

### 3.4 What Data You Get

For each skill, you get:
- **name** — skill identifier
- **description** — what it does (controls trigger behavior)
- **owner/repo** — where it lives on GitHub
- **installs** — how many people use it
- **trending rank** — is it gaining momentum?
- **full content** — the complete SKILL.md file
- **supported agents** — which AI tools it works with

---

## 4. How to Make Skills Searchable & Discoverable

### 4.1 Full-Text Search

Skills already have structured metadata (name, description, owner). Build a search index:

```sql
-- PostgreSQL with full-text search
CREATE TABLE skills (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  content TEXT,          -- full SKILL.md
  owner TEXT,
  repo TEXT,
  installs INTEGER DEFAULT 0,
  trending_24h INTEGER,
  source TEXT,           -- 'skills.sh', 'clawhub', etc.
  fetched_at TIMESTAMP,
  -- Full-text search index
  search_vector TSVECTOR GENERATED ALWAYS AS (
    setweight(to_tsvector('english', coalesce(name, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(description, '')), 'B') ||
    setweight(to_tsvector('english', coalesce(content, '')), 'C')
  ) STORED
);

CREATE INDEX idx_skills_search ON skills USING GIN (search_vector);
```

Search query:
```sql
-- Find skills for React component testing
SELECT name, description, installs,
       ts_rank(search_vector, query) AS relevance
FROM skills, plainto_tsquery('english', 'React component testing') query
WHERE search_vector @@ query
ORDER BY relevance DESC, installs DESC
LIMIT 20;
```

### 4.2 Vector Similarity Search (Semantic)

For "find me skills similar to what I need" — use embeddings:

```sql
-- Add pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

ALTER TABLE skills ADD COLUMN embedding vector(1536);

-- Generate embeddings from description + content
-- (using OpenAI text-embedding-3-small or similar)
```

Search by similarity:
```sql
-- Find skills similar to a description
SELECT name, description, installs,
       1 - (embedding <=> $1) AS similarity
FROM skills
ORDER BY embedding <=> $1
LIMIT 20;
```

### 4.3 Category & Tag System

Auto-categorize skills based on their content:

```typescript
function categorizeSkill(skill: Skill): string[] {
  const categories = [];
  const text = `${skill.name} ${skill.description}`.toLowerCase();

  if (text.match(/react|next\.?js|tailwind|css|html|frontend|ui/)) categories.push('frontend');
  if (text.match(/api|backend|server|database|sql|postgres/)) categories.push('backend');
  if (text.match(/test|qa|benchmark|eval|assert/)) categories.push('testing');
  if (text.match(/security|vulnerability|secret|scan/)) categories.push('security');
  if (text.match(/git|github|deploy|ci|cd|release/)) categories.push('devops');
  if (text.match(/design|figma|ux|layout|theme/)) categories.push('design');
  if (text.match(/debug|fix|error|trace|log/)) categories.push('debugging');
  if (text.match(/learn|teach|tutorial|course|study/)) categories.push('learning');
  if (text.match(/writ|blog|content|article|doc/)) categories.push('writing');
  if (text.match(/research|search|analysis|data/)) categories.push('research');

  return categories.length > 0 ? categories : ['general'];
}
```

---

## 5. How to Evaluate Skills Quickly

### 5.1 The Three-Layer Evaluation System

You need to evaluate skills at three levels of depth:

```
Layer 1: AUTO-SCAN (instant, no API cost)
├── Read SKILL.md
├── Check description clarity
├── Check instruction length
├── Check for security red flags
├── Score: 0-100
└── Filter: only pass skills scoring 60+

Layer 2: QUICK-BENCH (1 minute, low API cost)
├── Test trigger accuracy (5 prompts)
├── Test basic output quality (1 prompt)
├── Measure response latency
├── Score: 0-100 per dimension
└── Filter: only pass skills scoring 70+

Layer 3: DEEP-BENCH (10 minutes, full evaluation)
├── Full PromptFoo benchmark suite
├── All 4 dimensions: correctness, efficiency, discoverability, robustness
├── Multiple test cases per skill
├── Score: detailed breakdown
└── Decision: keep, adapt, or drop
```

### 5.2 Layer 1: Auto-Scan (No API Calls Needed)

```typescript
interface AutoScanResult {
  score: number;         // 0-100
  passed: boolean;       // score >= 60
  issues: string[];
  metrics: {
    descriptionClarity: number;    // Is the description specific?
    instructionConciseness: number; // Under 200 lines?
    securityFlags: number;          // Suspicious patterns?
    triggerSpecificity: number;     // Will it trigger correctly?
    dependencyCount: number;        // How many external deps?
  };
}

function autoScan(skill: Skill): AutoScanResult {
  const issues: string[] = [];
  let score = 100;

  // 1. Description clarity (20 points)
  if (!skill.description || skill.description.length < 20) {
    issues.push('Description too short or missing');
    score -= 20;
  } else if (skill.description.length > 500) {
    issues.push('Description too long — may cause trigger issues');
    score -= 5;
  }

  // 2. Instruction length (20 points)
  const lineCount = skill.content.split('\n').length;
  if (lineCount > 500) {
    issues.push(`Too verbose: ${lineCount} lines (target < 200)`);
    score -= 20;
  } else if (lineCount > 300) {
    issues.push(`Somewhat verbose: ${lineCount} lines`);
    score -= 10;
  }

  // 3. Security flags (30 points)
  const content = skill.content.toLowerCase();
  const redFlags = ['curl | bash', 'rm -rf', 'wget | sh', '/etc/passwd', 'exfil', 'upload'];
  for (const flag of redFlags) {
    if (content.includes(flag)) {
      issues.push(`Security red flag: "${flag}"`);
      score -= 30;
      break;
    }
  }

  // 4. Trigger specificity (15 points)
  if (!skill.description.match(/use when|trigger|invoke|activ/i)) {
    issues.push('No clear trigger condition in description');
    score -= 15;
  }

  // 5. Dependencies (15 points)
  if (content.match(/requires.*bins.*\[/)) {
    const bins = content.match(/bins:\s*\[(.*?)\]/)?.[1]?.split(',').length || 0;
    if (bins > 5) {
      issues.push(`Too many dependencies: ${bins} binaries required`);
      score -= 15;
    }
  }

  return { score: Math.max(0, score), passed: score >= 60, issues, metrics: {
    descriptionClarity: 0, instructionConciseness: 0, securityFlags: 0,
    triggerSpecificity: 0, dependencyCount: 0
  }};
}
```

### 5.3 Layer 2: Quick-Bench with PromptFoo

Set up a PromptFoo config template for rapid skill testing:

```yaml
# benchmarks/quick-bench.yaml
providers:
  - anthropic:messages:claude-sonnet-4-5-20250929

prompts:
  - file://benchmarks/prompts/skill-test.txt

tests:
  # Trigger accuracy tests (does it fire when it should?)
  - description: "Should trigger - positive case"
    vars:
      skill_description: "{{skill_description}}"
      user_prompt: "{{trigger_positive_prompt}}"
    assert:
      - type: llm-rubric
        value: "The agent correctly identified this as a task for the {{skill_name}} skill and followed its instructions"
        threshold: 0.7

  # Trigger accuracy (should NOT fire)
  - description: "Should NOT trigger - negative case"
    vars:
      skill_description: "{{skill_description}}"
      user_prompt: "{{trigger_negative_prompt}}"
    assert:
      - type: llm-rubric
        value: "The agent correctly did NOT invoke the {{skill_name}} skill for this unrelated request"
        threshold: 0.7

  # Output quality
  - description: "Output quality"
    vars:
      skill_description: "{{skill_description}}"
      user_prompt: "{{happy_path_prompt}}"
    assert:
      - type: llm-rubric
        value: "Output follows the skill's documented workflow and produces a useful, accurate result"
        threshold: 0.7
      - type: latency
        threshold: 30000  # under 30 seconds
```

Run it:
```bash
# Quick-bench a single skill
npx promptfoo eval -c benchmarks/quick-bench.yaml \
  --var skill_name="frontend-design" \
  --var skill_description="Design beautiful, responsive web interfaces..." \
  --var trigger_positive_prompt="Design a pricing page" \
  --var trigger_negative_prompt="Fix a Python bug" \
  --var happy_path_prompt="Create a hero section for a SaaS landing page"
```

### 5.4 Layer 3: Deep Bench with Skillmark

For skills that pass Layer 2, run a full Skillmark benchmark:

```bash
# Install Skillmark
npm install -g skillmark

# Run benchmark on a skill
npx skillmark run .claude/skills/frontend-design

# Output: result.json + report.md with scores
# accuracy, tokens_total, duration_ms, tool_count, cost_usd
```

---

## 6. How to Integrate Into Your Workflow

### 6.1 The Integration Pipeline

```
Discovery (auto) → Auto-Scan (instant) → Quick-Bench (1 min) → Try It (5 min) → Integrate
     │                    │                     │                    │              │
     ▼                    ▼                     ▼                    ▼              ▼
  Collect 91K+       Score 0-100          Pass trigger +        Manual test     Adapt SKILL.md
  skills from        Filter <60           quality tests?         in Claude      → commit to
  skills.sh,         Flag security                                Code           project
  ClawHub,           issues
  GitHub
```

### 6.2 Integration Decision Matrix

| Auto-Scan | Quick-Bench | Try It | Action |
|-----------|-------------|--------|--------|
| < 60 | - | - | Skip (not worth testing) |
| 60-80 | < 70 | - | Interesting but needs work — bookmark for later |
| 60-80 | 70+ | Passes | **Adapt and integrate** — modify for your project |
| 80+ | 70+ | Passes | **Direct integrate** — use as-is |
| Any | Any | Fails | Check if the concept is good — build your own version |

---

## 7. Concrete Step-by-Step Execution Plan

### Week 1: Data Foundation

**Day 1-2: Set up the data pipeline**

```bash
# 1. Clone and run the skills.sh API
git clone https://github.com/mastra-ai/skills-api.git skill-hub/api
cd skill-hub/api
pnpm install
pnpm start
# → API running at localhost:3456

# 2. Verify it works
curl http://localhost:3456/api/skills/stats
# → {"total": 34000+, "sources": 2800+, ...}

# 3. Fetch top 1000 skills
curl "http://localhost:3456/api/skills?pageSize=100&sortBy=installs&sortOrder=desc" | jq '.' > data/top-skills.json

# 4. Fetch all categories
curl http://localhost:3456/api/skills/sources | jq '.' > data/sources.json
```

**Day 3-4: Set up search**

```bash
# 5. Set up PostgreSQL with pgvector (use Supabase free tier)
# Or local: docker run -d -p 5432:5432 pgvector/pgvector:pg16

# 6. Create the skills table (see Section 4.1)

# 7. Import skills from the API
# Write a simple script:
node scripts/import-skills.js
# → Fetches all skills from localhost:3456 → inserts into PostgreSQL
```

**Day 5: Set up auto-scan**

```bash
# 8. Implement the Auto-Scan function (see Section 5.2)
# 9. Run it on all imported skills
node scripts/auto-scan-all.js
# → Each skill gets a score 0-100
# → Skills scoring < 60 get flagged
```

### Week 2: Search & Evaluation

**Day 1-2: Build the search interface**

```bash
# 10. Create a Next.js app
npx create-next-app@latest skill-hub/web --typescript --tailwind --app

# 11. Add search page
# Simple: text search → SQL full-text query → display results
# Advanced: vector similarity search → semantic matching

# 12. Add skill cards showing:
# - Name, description, installs, auto-scan score
# - Source (skills.sh / ClawHub)
# - Quick actions: "Try It", "Quick-Bench", "View Content"
```

**Day 3-4: Add Quick-Bench**

```bash
# 13. Install PromptFoo
npm install promptfoo

# 14. Set up the quick-bench template (see Section 5.3)

# 15. Add a "Quick Bench" button to each skill card
# → Runs PromptFoo with skill's description + test prompts
# → Shows results in 60 seconds
```

**Day 5: Add the "Try It" workflow**

```bash
# 16. One-click install: "Try this skill"
# → Downloads SKILL.md to a temp project
# → Opens Claude Code with the skill loaded
# → User tests manually

# 17. "Integrate" button
# → Copies skill to real project's .claude/skills/
# → Offers to modify the SKILL.md for project context
```

### Week 3: Polish & Workflow Integration

- Add trending data (refresh daily)
- Add skill comparison (side-by-side 2-4 skills)
- Add evaluation history (track how skills score over time)
- Add "My Skills" page (skills you've integrated)
- Add export (generate WORKFLOW.md from selected skills)

---

## 8. Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      Skill Hub (Next.js)                        │
│                                                                 │
│  ┌─────────┐  ┌──────────┐  ┌───────────┐  ┌───────────────┐  │
│  │ Search  │  │ Trending │  │ Skill     │  │ Evaluation    │  │
│  │ Page    │  │ Dashboard│  │ Detail    │  │ Dashboard     │  │
│  └────┬────┘  └────┬─────┘  └─────┬─────┘  └───────┬───────┘  │
│       │            │              │                 │           │
│       └────────────┴──────────────┴─────────────────┘           │
│                              │                                  │
│                    ┌─────────┴─────────┐                        │
│                    │   tRPC API Layer  │                        │
│                    └─────────┬─────────┘                        │
├──────────────────────────────┼──────────────────────────────────┤
│                    ┌─────────┴─────────┐                        │
│                    │  PostgreSQL +     │                        │
│                    │  pgvector         │                        │
│                    │  (skills, scores, │                        │
│                    │   embeddings)     │                        │
│                    └─────────┬─────────┘                        │
├──────────────────────────────┼──────────────────────────────────┤
│          Background Services │                                   │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Aggregator   │  │ Auto-Scanner │  │ Quick-Bench Runner   │  │
│  │ (every 6h)   │  │ (on import)  │  │ (on demand)          │  │
│  │              │  │              │  │                      │  │
│  │ Fetch from:  │  │ Score 0-100  │  │ PromptFoo +          │  │
│  │ - skills.sh  │  │ Check:       │  │ Skillmark            │  │
│  │ - ClawHub    │  │ - Security   │  │                      │  │
│  │ - GitHub     │  │ - Clarity    │  │ Dimensions:          │  │
│  │              │  │ - Length     │  │ - Trigger accuracy   │  │
│  │              │  │ - Triggers   │  │ - Output quality     │  │
│  └──────────────┘  └──────────────┘  │ - Latency            │  │
│                                       └──────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│          Data Sources (external)                                │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ mastra-ai/   │  │ ClawHub API  │  │ GitHub API           │  │
│  │ skills-api   │  │ (Convex)     │  │ (SKILL.md repos)     │  │
│  │ (34K+ skills)│  │ (52K+ tools) │  │                      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Tech Choices & Why

| Component | Choice | Why |
|-----------|--------|-----|
| **Data API** | Self-host `mastra-ai/skills-api` | Open-source, 12 endpoints, no rate limits, fresh data |
| **Database** | PostgreSQL + pgvector | Full-text search + vector similarity + relational data |
| **Hosted DB** | Supabase (free tier) | Managed Postgres with pgvector, generous free tier |
| **Frontend** | Next.js 15 + @innate/ui | Your existing stack, dogfooding your own components |
| **Search** | PostgreSQL FTS + pgvector | Keyword + semantic search in one database |
| **Auto-Scan** | Custom Node.js script | Simple scoring logic, no external deps needed |
| **Quick-Bench** | PromptFoo | Mature evaluation engine, supports all assertion types |
| **Deep-Bench** | Skillmark | Purpose-built for SKILL.md benchmarking |
| **Deployment** | Vercel + Supabase | Serverless, scales to zero, free to start |

---

## 10. What to Do This Week

### Today (2 hours)

```bash
# 1. Clone and run the skills.sh API
git clone https://github.com/mastra-ai/skills-api.git /tmp/skills-api
cd /tmp/skills-api && pnpm install && pnpm start

# 2. Explore the data
curl http://localhost:3456/api/skills/stats
curl "http://localhost:3456/api/skills?pageSize=5&sortBy=installs&sortOrder=desc" | jq '.skills[0]'
curl http://localhost:3456/api/skills/anthropics/skills/frontend-design/content

# 3. Try searching
curl "http://localhost:3456/api/skills?query=react+testing&pageSize=10" | jq '.skills[].name'
```

### Tomorrow (4 hours)

```bash
# 4. Set up PostgreSQL (local Docker or Supabase)
# 5. Create the skills table
# 6. Write import script to fetch all skills from the API
# 7. Implement auto-scan scoring
```

### Day 3-5 (rest of week)

```bash
# 8. Create Next.js app with search page
# 9. Connect to PostgreSQL, display skills with scores
# 10. Add "Try It" button (downloads SKILL.md to temp project)
# 11. Add trending dashboard
```

### End of Week Deliverable

A working Skill Hub where you can:
- Search 34K+ skills by keyword or semantic similarity
- See auto-scan scores for every skill
- Click "Try It" to test any skill in 2 minutes
- See trending data updated daily

---

## Quick Reference: Key Repos

| Repo | What | Why You Need It |
|------|------|----------------|
| [mastra-ai/skills-api](https://github.com/mastra-ai/skills-api) | Skills.sh API server | Primary data source with 12 REST endpoints |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | Skills CLI | `npx skills add` for installing skills |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Evaluation engine | Quick-bench and deep-bench testing |
| [claudekit/skillmark](https://github.com/claudekit/skillmark) | Skill benchmarking | SKILL.md-specific benchmarking with leaderboard |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ClawHub marketplace | Secondary data source for skill ratings |
| [anthropics/skills](https://github.com/anthropics/skills) | Official Anthropic skills | Reference implementations to learn from |
| [obra/superpowers](https://github.com/obra/superpowers) | Community skills | 137K installs, proven patterns |
