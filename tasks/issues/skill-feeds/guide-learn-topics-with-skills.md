# Guide: Using AI Skills to Learn Any Topic — General Process & Two Detailed Examples

**Date:** 2026-05-08

---

## Table of Contents

1. [The General Process](#1-the-general-process)
2. [Stages & Which Skills to Use](#2-stages--which-skills-to-use)
3. [Example 1: Learn "How to Build a Skill Hub"](#3-example-1-learn-how-to-build-a-skill-hub)
4. [Example 2: Learn "How to Evaluate & Integrate Skills"](#4-example-2-learn-how-to-evaluate--integrate-skills)
5. [Cross-Domain Application](#5-cross-domain-application)

---

## 1. The General Process

Every learning journey with AI skills follows the same 6 stages:

```
Stage 1          Stage 2          Stage 3          Stage 4          Stage 5          Stage 6
EXPLORE    →    STRUCTURE    →   LEARN BY      →  PRACTICE    →   EVALUATE    →   INTEGRATE
"What is X?"    "Break X into    DOING           "Build a real   "Am I doing     "Make it part
                 learnable       (guided          project with     it right?"      of my workflow"
                 pieces"         experiments)     AI help)
```

### The Key Insight

You don't learn by reading. You learn by **building real things with AI guidance**. Each stage uses a different type of skill:

| Stage | Goal | Skill Type | Example Skills |
|-------|------|-----------|---------------|
| **1. EXPLORE** | Understand the landscape | Tutoring/Research | learning-mode, domain-explorer |
| **2. STRUCTURE** | Create a learning path | Planning | prd-writer, project-analysis |
| **3. LEARN BY DOING** | Guided hands-on practice | Teaching + Coding | writing-skills (TDD), code-generation |
| **4. PRACTICE** | Build something real | Development | innate-frontend, git-workflow |
| **5. EVALUATE** | Check quality | Benchmarking | promptfoo, skillmark |
| **6. INTEGRATE** | Make it yours | Workflow | skill-composer, workflow templates |

---

## 2. Stages & Which Skills to Use

### Stage 1: EXPLORE — "What is this domain about?"

**What happens:** You chat with AI to understand the landscape, key concepts, tools, and terminology.

**Skills to use:**
- **learning-mode** (dual-agent expert-novice) — Acts as both tutor and questioner
- **brainstorming** (from superpowers) — Explores what you want to learn before diving in
- **find-skills** — Discovers existing skills related to the topic

**How to do it:**
```
In Claude Code:
"I want to learn about [topic]. Act as an expert tutor.
 1. Give me a map of the domain — key concepts, tools, terminology
 2. Tell me what skills I already have that transfer to this domain
 3. Suggest a learning project that would teach me the fundamentals"
```

**Output:** A domain map + learning objectives + project idea

### Stage 2: STRUCTURE — "Break it into learnable pieces"

**What happens:** You organize the domain into a structured learning plan with clear milestones.

**Skills to use:**
- **prd-writer-skill** — Defines "what to build" as a project brief
- **project-analysis-skill** — Breaks the project into technical components
- **writing-plans** (from superpowers) — Creates structured execution plans

**How to do it:**
```
"Based on the domain map, create a learning project brief:
 - Project goal: [what you want to build]
 - Learning objectives: [what you want to learn]
 - Milestones: [break into 5 achievable steps]
 - Success criteria: [how you know you've learned it]"
```

**Output:** A project brief with milestones

### Stage 3: LEARN BY DOING — "Guided hands-on practice"

**What happens:** You work through small exercises that teach one concept at a time, with AI as your pair programmer.

**Skills to use:**
- **writing-skills** (TDD methodology: RED → GREEN → REFACTOR) — Learn by writing tests first
- **scaffold-exercises** (from mattprocock-skills) — Generate practice exercises
- **tdd** (from mattprocock-skills) — Test-driven learning

**How to do it:**
```
"For milestone 1 [specific concept], create a hands-on exercise:
 1. Give me a small, concrete task
 2. Let me try it first
 3. Review what I did and explain what I could improve
 4. Give me the next slightly harder exercise
 Repeat until I've mastered this milestone."
```

**Output:** Practical understanding of each concept

### Stage 4: PRACTICE — "Build something real"

**What happens:** You apply what you've learned to build the actual project from Stage 2.

**Skills to use:**
- **git-workflow** or **local-workflow** — Track tasks and progress
- Domain-specific skills (e.g., **innate-frontend** for web, **desktop-app** for desktop)
- **caveman** (from mattprocock-skills) — Save tokens during long build sessions

**How to do it:**
```
"Let's build [project from Stage 2].
 Use git-workflow to track each milestone as a task.
 Implement milestone 1 now."
```

**Output:** Working project code

### Stage 5: EVALUATE — "Am I doing it right?"

**What happens:** You review the quality of what you've built and identify gaps.

**Skills to use:**
- **promptfoo** — Benchmark the output quality
- **skillmark** — Score the skill you've developed
- **receiving-code-review** (from superpowers) — Get AI code review
- **verification-before-completion** (from superpowers) — Final quality check

**How to do it:**
```
"Review what I've built so far:
 1. Is the code quality good? What should I improve?
 2. Does it match the best practices of [domain]?
 3. What am I still missing or doing wrong?
 4. What should I learn next to get better?"
```

**Output:** Quality assessment + learning gaps identified

### Stage 6: INTEGRATE — "Make it part of my workflow"

**What happens:** You turn what you've learned into a reusable skill or workflow.

**Skills to use:**
- **writing-skills** (from superpowers) — Write a SKILL.md capturing your knowledge
- **skill-creator** (from Anthropic) — Generate a proper skill from your learning

**How to do it:**
```
"Based on everything I've learned about [topic],
 create a SKILL.md that captures:
 1. The key concepts and terminology
 2. Best practices and common patterns
 3. Step-by-step workflows
 4. Common pitfalls and how to avoid them
 Save it to .claude/skills/[topic]/SKILL.md"
```

**Output:** A reusable skill that encodes your learning

---

## 3. Example 1: Learn "How to Build a Skill Hub"

**Goal:** You want to build a web app that aggregates, searches, and evaluates AI skills from multiple marketplaces.

### Stage 1: EXPLORE (Day 1, 2 hours)

**Prompt to AI:**
```
I want to learn how to build a Skill Hub — a web application that:
1. Aggregates AI skills from skills.sh, ClawHub, and other marketplaces
2. Lets users search and discover skills
3. Evaluates skill quality with benchmarks

Act as an expert tutor. Give me:
a) A domain map of what I need to learn (data aggregation, search, evaluation, web frontend)
b) What existing skills I have that transfer (I already know Next.js, React, PostgreSQL)
c) A small project that would teach me the fundamentals
```

**AI's likely response:**
- Domain map: API integration, data pipelines, full-text search, vector embeddings, evaluation frameworks, web UI
- Transfer: Your innate-frontend skill covers the frontend. You need to learn: API aggregation, search implementation, PromptFoo evaluation
- Project: "Build a skill search engine that fetches the top 100 skills from skills.sh and lets you search them"

**Skills used:** brainstorming (to structure the conversation), learning-mode (tutor mode)

### Stage 2: STRUCTURE (Day 1, 1 hour)

**Prompt to AI:**
```
Create a learning project brief for building a Skill Hub:

Project: Skill Search Engine
Milestones:
1. Fetch skills from the skills.sh API (data aggregation)
2. Store in PostgreSQL with full-text search (database)
3. Build a search UI with Next.js (frontend)
4. Add skill quality scoring (evaluation)
5. Add trending dashboard (data visualization)

Success criteria: I can search 1000+ skills and see quality scores
```

**Skills used:** prd-writer-skill (define the project), project-analysis-skill (technical architecture)

### Stage 3: LEARN BY DOING (Day 2-3, 4 hours)

**Milestone 1 exercise: Fetch data from an API**

**Prompt to AI:**
```
I'm learning about API aggregation. Give me a hands-on exercise:

Task: Write a Node.js script that fetches the top 100 skills from
http://localhost:3456/api/skills and saves them as JSON.

Rules:
1. Show me the API endpoint documentation first
2. Let me write the code myself
3. Review my code and tell me what to improve
4. Then give me the next exercise: add pagination to fetch all 34K+ skills
```

**What you learn:** REST API consumption, pagination patterns, data transformation, error handling

**Skills used:** tdd (test-driven: write a test first, then implement), scaffold-exercises (generate practice tasks)

**Milestone 2 exercise: Full-text search**

**Prompt to AI:**
```
Now teach me PostgreSQL full-text search.

Exercise: Create a skills table with a TSVECTOR column for search.
Then write a query that searches for "React testing" and ranks by relevance.

Let me try first, then review my approach.
```

**What you learn:** PostgreSQL FTS, tsvector, tsquery, ranking, GIN indexes

**Milestone 3 exercise: Build the search UI**

**Prompt to AI:**
```
Using innate-frontend skill, build a search page with:
- Search input with debounced API calls
- Results grid showing skill cards
- Each card: name, description, installs, score
- Filter by source (skills.sh / ClawHub)

I'll build this component by component. Guide me through it.
```

**What you learn:** React search patterns, debouncing, API integration, component composition

**Skills used:** innate-frontend (UI components), writing-skills (TDD for each component)

### Stage 4: PRACTICE (Day 4-7)

**Prompt to AI:**
```
Let's build the full Skill Hub now.
Use git-workflow to track each milestone.

Implement:
1. Data pipeline: scheduled fetch from skills.sh API → PostgreSQL
2. Search API: tRPC router with FTS + vector search
3. Frontend: search page, trending dashboard, skill detail pages
4. Auto-scan: score each skill on import (security, clarity, trigger accuracy)
5. Quick-bench: one-click PromptFoo evaluation for any skill
```

**Skills used:** git-workflow (task tracking), innate-frontend (UI), local-workflow (backend), scanning-for-secrets (security)

### Stage 5: EVALUATE (Day 8)

**Prompt to AI:**
```
Review the Skill Hub I've built:
1. Code quality — are there anti-patterns?
2. Search quality — does it return relevant results?
3. Performance — are queries fast enough?
4. Security — any vulnerabilities in the API?
5. What should I learn next to make it better?
```

**Skills used:** receiving-code-review (from superpowers), verification-before-completion

### Stage 6: INTEGRATE (Day 9-10)

**Prompt to AI:**
```
Based on everything I learned building the Skill Hub,
create a SKILL.md for "skill-hub-development" that captures:
1. How to set up the data pipeline (mastra-ai/skills-api → PostgreSQL)
2. Search implementation (FTS + pgvector)
3. Evaluation integration (PromptFoo + Skillmark)
4. Frontend patterns (innate-frontend + search UI)
5. Deployment (Vercel + Supabase)
```

**Skills used:** skill-creator (from Anthropic), writing-skills (documentation)

**Final output:** A reusable `skill-hub-development` skill + a working Skill Hub + a tutorial you can share

---

## 4. Example 2: Learn "How to Evaluate & Integrate Skills"

**Goal:** You want to learn the process of discovering, testing, and integrating external skills into your workflow.

### Stage 1: EXPLORE (1 hour)

**Prompt to AI:**
```
I want to learn how to evaluate and integrate AI agent skills.
Give me a domain map covering:
a) Where to discover skills (skills.sh, ClawHub, GitHub)
b) How to install them (plugin marketplace, npx skills add, manual)
c) How to evaluate quality (trigger accuracy, output quality, security)
d) How to adapt them for my project (modify SKILL.md)
e) How to integrate into my workflow (WORKFLOW.md, git-workflow)
```

**Skills used:** brainstorming, learning-mode

### Stage 2: STRUCTURE (1 hour)

**Milestones:**
1. Install and try 5 skills from different sources
2. Evaluate each skill with a 5-minute test
3. Adapt one skill for the fire-skills project
4. Create a workflow that uses the adapted skill
5. Benchmark the adapted skill with PromptFoo

### Stage 3: LEARN BY DOING (3 hours)

**Exercise 1: Install a skill via plugin marketplace**

```bash
# In Claude Code:
/plugin
# → Discover tab → install "github" plugin
# → Try it: "show me my recent issues"

# Your first evaluation:
# Q: Did it trigger correctly?  A: Yes, it understood "issues"
# Q: Was the output useful?    A: Yes, showed real GitHub issues
# Q: Any conflicts?           A: None with my existing skills
```

**Exercise 2: Install via skills.sh CLI**

```bash
npx skills add
# Search for "brainstorming"
# Select it → installed to .claude/skills/brainstorming

# Test it:
claude
"I want to add a feature to my app"
# → Does it trigger brainstorming mode? Or jump straight to code?
```

**Exercise 3: Manual clone + adapt**

```bash
# Clone superpowers
git clone --depth 1 https://github.com/obra/superpowers.git /tmp/sp

# Read the brainstorming skill
cat /tmp/sp/skills/brainstorming/SKILL.md

# Identify what to adapt:
# - Too long (150+ lines) → trim to essentials
# - Uses docs/superpowers/specs/ → change to docs/specs/
# - Forces visual companion → make optional

# Create adapted version:
mkdir -p .claude/skills/brainstorm
# Write a lean 30-line version tailored to fire-skills
```

**Exercise 4: Evaluate with PromptFoo**

```bash
# Create a quick test config
cat > /tmp/bench-brainstorm.yaml << 'EOF'
providers:
  - anthropic:messages:claude-sonnet-4-5-20250929
tests:
  - description: "Should trigger brainstorming"
    vars:
      prompt: "I want to add user authentication"
    assert:
      - type: llm-rubric
        value: "Agent asks clarifying questions before coding"
  - description: "Should NOT trigger for bug fixes"
    vars:
      prompt: "Fix the typo in the README"
    assert:
      - type: llm-rubric
        value: "Agent does NOT start a brainstorming session for a simple fix"
EOF

npx promptfoo eval -c /tmp/bench-brainstorm.yaml
```

### Stage 4: PRACTICE (2 hours)

**The real test: Build a workflow that uses the adapted skill**

```
Prompt to AI:
"Create a WORKFLOW.md for the fire-skills project that uses:
1. brainstorm (adapted) — for feature design
2. prd-writer-skill — for PRD generation
3. project-analysis-skill — for technical design
4. git-workflow — for task execution

The workflow should be: brainstorm → PRD → technical design → implement (loop)"
```

### Stage 5: EVALUATE (1 hour)

```
"Review my adapted brainstorm skill:
1. Is the trigger description specific enough?
2. Are the instructions clear and concise?
3. Does it conflict with any other skills?
4. What would make it better?"
```

### Stage 6: INTEGRATE (1 hour)

```
"Create a SKILL.md called 'skill-evaluator' that captures my process:
1. How to discover skills (skills.sh, ClawHub, /plugin)
2. How to quick-test in 5 minutes
3. How to evaluate with auto-scan + PromptFoo
4. How to adapt for the fire-skills project
5. How to integrate into workflows

Save to .claude/skills/skill-evaluator/SKILL.md"
```

**Final output:** A `skill-evaluator` skill that codifies your evaluation process

---

## 5. Cross-Domain Application

The same 6-stage process works for ANY topic:

| Topic | Stage 1 (Explore) | Stage 4 (Practice) | Key Skills |
|-------|-------------------|-------------------|------------|
| **Music Production** | Learn theory, DAW concepts | Create a 4-track EP | learning-mode, domain-specific skill |
| **Game Development** | Learn game engine, patterns | Build a platformer | innate-frontend (for UI), desktop-app |
| **Data Science** | Learn pandas, visualization | Analyze a real dataset | research skill, analysis skill |
| **Technical Writing** | Learn documentation patterns | Write a tutorial series | writing-skills, tutorial-generator |
| **DevOps/Infra** | Learn Docker, CI/CD, IaC | Deploy a real app | scanning-for-secrets, gh-create-release |
| **Mobile Dev** | Learn React Native, Expo | Build a mobile app | innate-frontend (adapts), desktop-app |
| **AI/ML Engineering** | Learn training, fine-tuning | Fine-tune a model | research skill, evaluation skill |

### The Universal Template

```
1. "I want to learn [TOPIC]" → AI tutor explains domain
2. "Create a learning project" → Structured brief with milestones
3. "Give me exercise for [MILESTONE]" → Hands-on practice
4. "Let's build [PROJECT]" → Real project with git-workflow tracking
5. "Review what I built" → Quality assessment
6. "Create a SKILL.md for [TOPIC]" → Reusable knowledge capture
```

Each cycle through this loop makes you better at the domain AND builds your skill library. The skills you create become teaching tools for the next person.
