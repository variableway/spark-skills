# Instruction Report: System vs Project Skills — Architecture, Coordination & Real Examples

**Date:** 2026-05-08

---

## Table of Contents

1. [The Three Levels of Skills](#1-the-three-levels-of-skills)
2. [Your Current Skill Map (Real)](#2-your-current-skill-map-real)
3. [The Decision Framework](#3-the-decision-framework)
4. [System-Level Skills: What & Why](#4-system-level-skills-what--why)
5. [Project-Level Skills: What & Why](#5-project-level-skills-what--why)
6. [The Multi-Domain Problem](#6-the-multi-domain-problem)
7. [Coordination: When Skills Need Each Other](#7-coordination-when-skills-need-each-other)
8. [Real Architecture: Multi-Domain Products](#8-real-architecture-multi-domain-products)
9. [Concrete File Structure](#9-concrete-file-structure)
10. [Migration Plan: What to Move Where](#10-migration-plan-what-to-move-where)

---

## 1. The Three Levels of Skills

Skills live at three levels, each with a different purpose and scope:

```
┌─────────────────────────────────────────────────────────────┐
│ LEVEL 1: SYSTEM (~/.claude/skills/ or ~/.openclaw/skills/) │
│ "Available in EVERY project, EVERY session"                 │
│ Purpose: Universal dev workflow & shared tech stack         │
│ Owner: You personally                                        │
├─────────────────────────────────────────────────────────────┤
│ LEVEL 2: PROJECT (.claude/skills/ or /skills/)              │
│ "Available in THIS project, shared with team"               │
│ Purpose: Domain-specific workflow & business logic           │
│ Owner: Project team                                          │
├─────────────────────────────────────────────────────────────┤
│ LEVEL 3: WORKSPACE (/skills/ in a sub-project)              │
│ "Available only in this sub-project/module"                 │
│ Purpose: Module-specific patterns                            │
│ Owner: Module developer                                      │
└─────────────────────────────────────────────────────────────┘
```

### The Key Question

**"If I switch to a completely different project tomorrow, do I still need this skill?"**

- **YES** → System level
- **NO, but my team on THIS project needs it** → Project level
- **NO, only this specific module needs it** → Workspace level

---

## 2. Your Current Skill Map (Real)

Here's what you actually have right now:

### System Level (`~/.claude/skills/`) — 6 skills

| Skill | Purpose | Correct Level? |
|-------|---------|---------------|
| `git-workflow` | GitHub Issue task tracking | **System** — you use this everywhere |
| `local-workflow` | Local task tracking | **System** — you use this everywhere |
| `github-cli-skill` | GitHub CLI wrapper | **System** — git is universal |
| `gh-create-release` | GitHub releases | **System** — releases are universal |
| `innate-frontend` | Next.js + @innate/ui components | **System** — shared tech stack |
| `desktop-app` | Tauri v2 + Next.js desktop | **System** — shared tech stack |

### Project Level (in repo, but not in `.claude/skills/`)

| Collection | Skills | Currently At | Should Be |
|-----------|--------|-------------|-----------|
| `superpowers/skills/` | 14 skills (brainstorming, TDD, debugging, etc.) | Project root, not loaded | Some system, some project |
| `mattprocock-skills/` | 21 skills (caveman, QA, triage, etc.) | Project root, not loaded | Some system, some project |

### The Problem Right Now

1. **superpowers** and **mattprocock-skills** sit in the repo but aren't in `.claude/skills/`, so they're **not actually loaded** when you use Claude Code
2. Some skills that belong at system level (like `caveman`, `tdd`, `systematic-debugging`) are trapped at project level
3. Some skills that belong at project level (like `obsidian-vault`, `migrate-to-shoehorn`) might be mixed in with universal ones

---

## 3. The Decision Framework

### Rule 1: Frequency + Universality = System Level

A skill belongs at **system level** if:
- You use it in **multiple projects** (not just fire-skills)
- It's about **how you work**, not **what you're building**
- It applies regardless of the domain

### Rule 2: Domain + Context = Project Level

A skill belongs at **project level** if:
- It references **specific files, paths, or conventions** of the project
- It encodes **domain knowledge** specific to the product
- Other projects would need a **different version** of it

### Rule 3: Module + Narrow Scope = Workspace Level

A skill belongs at **workspace level** if:
- It only applies to one **sub-module** of a larger project
- It references **internal APIs or patterns** specific to that module
- Even other modules in the same project don't need it

---

## 4. System-Level Skills: What & Why

### What Goes Here

**Dev workflow skills** — how you work, regardless of what you're building:

| Skill | Why It's System-Level | Your Version |
|-------|----------------------|-------------|
| `git-workflow` | Every project uses git + GitHub | **Already system** ✅ |
| `local-workflow` | Local task tracking works everywhere | **Already system** ✅ |
| `github-cli-skill` | GitHub operations are universal | **Already system** ✅ |
| `gh-create-release` | Releases are universal | **Already system** ✅ |

**Shared tech stack skills** — tools you use across all projects:

| Skill | Why It's System-Level | Your Version |
|-------|----------------------|-------------|
| `innate-frontend` | Your shared component library | **Already system** ✅ |
| `desktop-app` | Your desktop app framework | **Already system** ✅ |

**Universal dev practices** — skills that improve any coding task:

| Skill | Why It Should Be System-Level | Currently At |
|-------|------------------------------|-------------|
| `caveman` (mattprocock) | Token-saving mode — useful everywhere | Project ❌ → Move to system |
| `systematic-debugging` (superpowers) | Every project has bugs | Project ❌ → Move to system |
| `writing-skills` (superpowers) | You write skills in every project | Project ❌ → Move to system |
| `verification-before-completion` (superpowers) | Quality gate — universal | Project ❌ → Move to system |
| `test-driven-development` (superpowers) | TDD applies everywhere | Project ❌ → Move to system |
| `brainstorming` (superpowers) | Design before code — universal | Project ❌ → Move to system |
| `writing-plans` (superpowers) | Planning — universal | Project ❌ → Move to system |
| `requesting-code-review` (superpowers) | Code review — universal | Project ❌ → Move to system |

### What Does NOT Belong at System Level

These skills reference specific domains, tools, or project structures:

| Skill | Why It's Project-Level | Belongs In |
|-------|----------------------|-----------|
| `obsidian-vault` (mattprocock) | References specific Obsidian vault | Projects that use Obsidian |
| `migrate-to-shoehorn` (mattprocock) | Specific migration task | The project that needs it |
| `domain-model` (mattprocock) | References CONTEXT.md, ADR docs | Projects using DDD |
| `scaffold-exercises` (mattprocock) | For course/tutorial projects | Learning projects only |
| `ubiquitous-language` (mattprocock) | DDD glossary — project-specific | Projects using DDD |

---

## 5. Project-Level Skills: What & Why

### What Goes Here

**Domain-specific workflows** — how you build THIS product:

| Example Skill | What It Does | Why Project-Level |
|--------------|-------------|-------------------|
| `skill-hub-development` | How to build the Skill Hub | Specific to the Skill Hub product |
| `music-production` | How to compose/mix/master | Specific to music projects |
| `game-physics` | Physics engine patterns | Specific to game projects |
| `data-pipeline` | ETL workflow for analytics | Specific to data projects |

**Project conventions** — how THIS team works:

| Example Skill | What It Does | Why Project-Level |
|--------------|-------------|-------------------|
| `fire-skills-conventions` | Code style, file structure, naming | Specific to this repo |
| `innate-ui-patterns` | How to use @innate/ui in this project | Project-specific usage patterns |
| `deploy-to-staging` | This project's deployment flow | Infra is project-specific |

**Business logic helpers** — domain knowledge for THIS product:

| Example Skill | What It Does | Why Project-Level |
|--------------|-------------|-------------------|
| `skill-evaluator` | How to evaluate skills for the hub | Business logic of the Skill Hub |
| `user-auth-flow` | Authentication patterns for this app | Product-specific auth |
| `payment-integration` | Stripe integration for this app | Product-specific payments |

---

## 6. The Multi-Domain Problem

### The Scenario

You develop multiple products across different domains, all using the same tech stack:

```
variableway/
├── fire-skills/          ← Skill development tools (domain: developer tools)
├── skill-hub/            ← Skill aggregation platform (domain: developer tools)
├── music-app/            ← Music production tool (domain: music)
├── learning-platform/    ← Online course platform (domain: education)
└── personal-site/        ← Your website (domain: content)
```

**Shared tech stack:** Next.js + React 19 + Tailwind v4 + @innate/ui + TypeScript

### What's Shared (System-Level)

Every project uses these, so they live at system level:

```
~/.claude/skills/
├── git-workflow/           # Task tracking — same in every project
├── local-workflow/         # Local tracking — same in every project
├── github-cli-skill/       # GitHub operations — same everywhere
├── gh-create-release/      # Releases — same everywhere
├── innate-frontend/        # Shared UI components — same stack
├── desktop-app/            # Desktop framework — same stack
├── caveman/                # Token saver — useful everywhere
├── systematic-debugging/   # Debug — universal
├── brainstorming/          # Design before code — universal
├── writing-plans/          # Planning — universal
├── tdd/                    # Test-driven — universal
├── verification/           # Quality gate — universal
└── writing-skills/         # Skill authoring — universal
```

### What's Different (Project-Level)

Each project has domain-specific skills:

```
fire-skills/
└── .claude/skills/
    ├── skill-evaluator/        # How to evaluate skills (domain: dev tools)
    └── skill-publisher/        # How to publish to marketplaces (domain: dev tools)

skill-hub/
└── .claude/skills/
    ├── data-aggregation/       # Fetch from APIs (domain: data platform)
    ├── skill-search/           # Search implementation (domain: search)
    └── skill-benchmarking/     # Evaluation engine (domain: evaluation)

music-app/
└── .claude/skills/
    ├── music-composition/      # Chord progressions, melody (domain: music)
    ├── music-mixing/           # EQ, compression, reverb (domain: music)
    └── music-production/       # DAW workflow (domain: music)

learning-platform/
└── .claude/skills/
    ├── course-design/          # Curriculum structure (domain: education)
    ├── exercise-generator/     # Practice problems (domain: education)
    └── progress-tracking/      # Learning analytics (domain: education)
```

### How System + Project Skills Work Together

When you're working on the **music-app**:

```
System skills loaded:    git-workflow, innate-frontend, caveman, tdd, ...
Project skills loaded:   music-composition, music-mixing, music-production

You: "Create a chord progression for a verse, then build a UI component
      that visualizes it"

AI uses:
  music-composition  → generates the chord progression (project skill)
  innate-frontend    → builds the UI component (system skill)
  git-workflow       → tracks the task (system skill)
```

When you switch to the **learning-platform**:

```
System skills loaded:    git-workflow, innate-frontend, caveman, tdd, ...
Project skills loaded:   course-design, exercise-generator, progress-tracking

You: "Create an exercise about React hooks, then build the exercise UI"

AI uses:
  exercise-generator → generates the exercise (project skill)
  innate-frontend    → builds the UI (system skill)
  git-workflow       → tracks the task (system skill)
```

**Same system skills, different project skills.** The system skills provide the "how to develop" layer. The project skills provide the "what to build" layer. They compose naturally without coordination.

---

## 7. Coordination: When Skills Need Each Other

### The Truth: Most Skills Don't Need Coordination

Skills are designed to be **independent**. Each one handles a specific concern. In 90% of cases, they don't need to talk to each other.

```
You: "Debug this failing test"
AI picks: systematic-debugging (system) → does the job

You: "Design the payment flow"
AI picks: brainstorming (system) → does the job

You: "Compose a bass line"
AI picks: music-composition (project) → does the job
```

No coordination needed. The skill triggers based on the prompt and does its thing.

### When Coordination IS Needed

Coordination matters when **multiple skills must run in sequence** to complete a task:

**Example: "Ship a new feature"**

```
Needs 5 skills in order:
  1. brainstorming     → design the feature
  2. writing-plans     → plan the implementation
  3. tdd               → write tests, then implement
  4. verification      → check everything works
  5. gh-create-release → ship it
```

**This is what workflows are for.** A workflow doesn't coordinate skills — it **declares the sequence**:

```yaml
# ~/.claude/skills/ship-feature/SKILL.md
---
name: ship-feature
description: >
  Complete feature shipping workflow. Use when user says "ship this",
  "implement and ship", or "build this feature end to end".
---

# Ship Feature

1. Use `brainstorming` — design before coding
2. Use `writing-plans` — create implementation plan
3. Use `tdd` — red-green-refactor cycle
4. Use `verification` — run all checks
5. Use `gh-create-release` — create release
```

The workflow skill acts as a **coordinator** — it's a skill that calls other skills in order.

### The Coordination Patterns

| Pattern | How It Works | Example |
|---------|-------------|---------|
| **Sequential** | Skill A then Skill B then Skill C | brainstorm → plan → tdd → verify → release |
| **Conditional** | If X, use Skill A; if Y, use Skill B | If "web app" → innate-frontend; if "desktop" → desktop-app |
| **Parallel** | Skills A and B run independently | frontend component + backend API at the same time |
| **Loop** | Repeat Skill A until done | git-workflow loops for each task in a feature |

### The Key Insight

**You don't need a coordination framework.** You need a **workflow skill** that declares the order. The AI reads the workflow and calls each skill naturally. It's prompt-level composition, not API-level orchestration.

---

## 8. Real Architecture: Multi-Domain Products

### Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                     SYSTEM LEVEL (~/.claude/skills/)                 │
│                                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌───────────┐  │
│  │ git-workflow │  │ innate-      │  │ desktop-   │  │ caveman   │  │
│  │ local-workflow│  │ frontend     │  │ app        │  │ tdd       │  │
│  │ github-cli   │  │ (57+ UI      │  │ (Tauri v2) │  │ debug     │  │
│  │ gh-release   │  │  components) │  │            │  │ brainstorm│  │
│  └─────────────┘  └──────────────┘  └────────────┘  │ verify    │  │
│       ↑                  ↑               ↑           │ plans     │  │
│       │     SHARED TECH STACK + DEV WORKFLOW          │ reviews   │  │
│       │                                                │ writing   │  │
│  ┌────┴────────────────────────────────────────────────┴──────────┐  │
│  │                     AVAILABLE IN ALL PROJECTS                   │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘

┌─────────────────────┐  ┌────────────────────┐  ┌────────────────────┐
│ fire-skills/        │  │ skill-hub/          │  │ music-app/         │
│ .claude/skills/     │  │ .claude/skills/     │  │ .claude/skills/    │
│                     │  │                     │  │                    │
│ • skill-evaluator   │  │ • data-aggregation  │  │ • composition      │
│ • skill-publisher   │  │ • skill-search      │  │ • mixing           │
│ • skill-benchmark   │  │ • skill-benchmark   │  │ • production       │
│                     │  │ • trending-engine   │  │ • arrangement      │
│ DOMAIN: dev tools   │  │ DOMAIN: platform    │  │ DOMAIN: music      │
└─────────────────────┘  └─────────────────────┘  └────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐
│ learning-platform/  │  │ personal-site/      │
│ .claude/skills/     │  │ .claude/skills/     │
│                     │  │                     │
│ • course-design     │  │ • blog-writing      │
│ • exercise-gen      │  │ • seo-optimization  │
│ • progress-track    │  │ • deployment         │
│ • assessment        │  │                     │
│                     │  │ DOMAIN: content     │
│ DOMAIN: education   │  │                     │
└─────────────────────┘  └─────────────────────┘
```

### Real Example: Building the Skill Hub

**System skills that kick in automatically:**
- `innate-frontend` → when building any UI component
- `git-workflow` → when tracking tasks
- `tdd` → when writing tests
- `brainstorming` → when designing features
- `systematic-debugging` → when things break

**Project skills that are Skill Hub-specific:**

```yaml
# skill-hub/.claude/skills/data-aggregation/SKILL.md
---
name: data-aggregation
description: >
  Fetch and normalize skill data from external marketplaces.
  Use when user needs to collect skills from skills.sh, ClawHub,
  or other sources. Handles pagination, deduplication, and
  normalization into the unified skill schema.
---

# Steps
1. Fetch from mastra-ai/skills-api: GET /api/skills (paginated)
2. Fetch from ClawHub: clawhub search (broad queries)
3. Normalize both sources to unified schema
4. Deduplicate by owner/repo/name
5. Upsert into PostgreSQL with updated metrics
6. Log: [source] fetched [N] skills, [M] new, [K] updated
```

```yaml
# skill-hub/.claude/skills/skill-search/SKILL.md
---
name: skill-search
description: >
  Search skills in the local database using full-text and vector
  search. Use when user wants to find, search, or discover skills.
  Supports keyword search, semantic similarity, and filtering.
---

# Steps
1. Parse the search query (keywords + intent)
2. Run PostgreSQL full-text search (tsvector)
3. Run pgvector similarity search (if semantic)
4. Merge and rank results
5. Apply filters (source, category, min_score)
6. Return ranked list with relevance scores
```

**How they compose:**

```
You: "Find me the best React testing skills"

AI calls:
  1. skill-search (project) → searches database
  2. skill-evaluator (project) → scores top results
  3. innate-frontend (system) → displays results in UI

No coordination needed — each skill handles its own concern.
```

### Real Example: Building the Music App

**System skills that kick in:**

```
You: "Build a piano roll editor component"

AI uses:
  brainstorming (system) → "What should the piano roll look like?"
  innate-frontend (system) → Uses @innate/ui components for the grid
  tdd (system) → Write tests for note placement first
  git-workflow (system) → Track as a task
```

**Project skill kicks in for domain knowledge:**

```
You: "When the user clicks a note, play the corresponding sound"

AI uses:
  music-composition (project) → "C4 = 261.63 Hz, use Web Audio API"
```

**The boundary is clean:** System handles "how to build," project handles "what to build."

---

## 9. Concrete File Structure

### Recommended Structure

```
~/.claude/                              ← SYSTEM LEVEL
├── settings.json                        ← Global settings (env, marketplaces)
└── skills/                              ← Universal skills
    ├── git-workflow/SKILL.md
    ├── local-workflow/SKILL.md
    ├── github-cli-skill/SKILL.md
    ├── gh-create-release/SKILL.md
    ├── innate-frontend/SKILL.md
    ├── desktop-app/SKILL.md
    ├── caveman/SKILL.md                 ← NEW (move from mattprocock)
    ├── systematic-debugging/SKILL.md    ← NEW (move from superpowers)
    ├── writing-skills/SKILL.md          ← NEW (move from superpowers)
    ├── verification/SKILL.md            ← NEW (move from superpowers)
    ├── tdd/SKILL.md                     ← NEW (move from superpowers)
    ├── brainstorming/SKILL.md           ← NEW (move from superpowers)
    ├── writing-plans/SKILL.md           ← NEW (move from superpowers)
    ├── requesting-code-review/SKILL.md  ← NEW (move from superpowers)
    ├── ship-feature/SKILL.md            ← NEW (workflow: compose above)
    └── learn-by-building/SKILL.md       ← NEW (from learning research)

~/workspace/variableway/innate/fire-skills/  ← fire-skills PROJECT
├── .claude/
│   ├── settings.json                    ← Project settings (hooks)
│   └── skills/                          ← Project-specific skills
│       ├── skill-evaluator/SKILL.md     ← How to evaluate skills
│       └── skill-publisher/SKILL.md     ← How to publish skills
├── superpowers/                         ← REFERENCE ONLY (not loaded)
│   └── skills/...
└── mattprocock-skills/                  ← REFERENCE ONLY (not loaded)
    └── ...

~/workspace/variableway/innate/skill-hub/    ← skill-hub PROJECT
├── .claude/
│   └── skills/
│       ├── data-aggregation/SKILL.md
│       ├── skill-search/SKILL.md
│       └── skill-benchmarking/SKILL.md
└── ...

~/workspace/variableway/innate/music-app/    ← music-app PROJECT
├── .claude/
│   └── skills/
│       ├── music-composition/SKILL.md
│       ├── music-mixing/SKILL.md
│       └── music-production/SKILL.md
└── ...
```

### How Claude Code Resolves Skills

When you start Claude Code in `~/workspace/variableway/innate/music-app/`:

```
Loaded skills (merged, highest precedence wins):
  1. ~/.claude/skills/*                  (system — 15 universal skills)
  2. music-app/.claude/skills/*          (project — 3 music skills)

Total: 18 skills available

Trigger resolution:
  "debug this"           → systematic-debugging (system)
  "compose a melody"     → music-composition (project)
  "build a UI component" → innate-frontend (system)
  "ship this feature"    → ship-feature workflow (system) → chains into project skills
```

When you switch to `~/workspace/variableway/innate/skill-hub/`:

```
Loaded skills (merged):
  1. ~/.claude/skills/*                  (system — 15 universal skills)
  2. skill-hub/.claude/skills/*          (project — 3 platform skills)

Total: 18 skills available

Trigger resolution:
  "debug this"           → systematic-debugging (system)
  "search for React skills" → skill-search (project)
  "build a UI component" → innate-frontend (system)
  "ship this feature"    → ship-feature workflow (system)
```

**Same system skills. Different project skills. Zero coordination overhead.**

---

## 10. Migration Plan: What to Move Where

### Move to System Level (do this now)

```bash
# From mattprocock-skills → system
cp -r mattprocock-skills/caveman ~/.claude/skills/

# From superpowers → system
cp -r superpowers/skills/brainstorming ~/.claude/skills/
cp -r superpowers/skills/systematic-debugging ~/.claude/skills/
cp -r superpowers/skills/writing-skills ~/.claude/skills/
cp -r superpowers/skills/writing-plans ~/.claude/skills/
cp -r superpowers/skills/test-driven-development ~/.claude/skills/tdd
cp -r superpowers/skills/verification-before-completion ~/.claude/skills/verification
cp -r superpowers/skills/requesting-code-review ~/.claude/skills/
cp -r superpowers/skills/executing-plans ~/.claude/skills/
cp -r superpowers/skills/finishing-a-development-branch ~/.claude/skills/
```

### Keep at Project Level (in fire-skills)

```bash
# Domain-specific skills that only matter for this project
# Leave them where they are, or move into .claude/skills/ if you want them loaded

# mattprocock skills that stay project-level:
# obsidian-vault, domain-model, scaffold-exercises, ubiquitous-language
# migrate-to-shoehorn, grill-me, design-an-interface
```

### Create New Workflow Skills

```bash
# Ship feature workflow (system level)
mkdir -p ~/.claude/skills/ship-feature
# Write SKILL.md that chains: brainstorm → plan → tdd → verify → release

# Learn by building workflow (system level)
mkdir -p ~/.claude/skills/learn-by-building
# Write SKILL.md with the 6-stage learning process
```

### Result

After migration:
- **~15 system skills** — universal dev workflow + shared tech stack
- **3-5 project skills per project** — domain-specific
- **2 workflow skills** — compose system + project skills into sequences
- **Zero coordination framework needed** — skills compose through prompt-level triggers

The architecture is: **thin project layer on top of thick system layer.** You take your system skills to every project. Each project adds only what's unique about its domain.
