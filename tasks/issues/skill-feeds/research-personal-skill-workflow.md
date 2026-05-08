# Research & Plan: Personal SKILL Execution Workflow

**Date:** 2026-05-08
**Task:** Task 3 — 完全个人workflow的SKILL执行路径

## Table of Contents

1. [Current State: Your Skill Ecosystem](#1-current-state-your-skill-ecosystem)
2. [The Evolving AI Usage Path](#2-the-evolving-ai-usage-path)
3. [Skill Composition Framework](#3-skill-composition-framework)
4. [Learning-to-Practice SKILL Workflow](#4-learning-to-practice-skill-workflow)
5. [Cross-Domain Skill Transfer](#5-cross-domain-skill-transfer)
6. [Reproducible Tutorial Generation](#6-reproducible-tutorial-generation)
7. [Action Plan](#7-action-plan)

---

## 1. Current State: Your Skill Ecosystem

### What You Have

| Category | Skills | Key Tools |
|----------|--------|-----------|
| **Dev Workflow** | git-workflow, local-workflow, github-cli-skill, gh-create-release, spark-task-init | GitHub Issue-driven execution |
| **Frontend** | innate-frontend (57+ components, Next.js 16), desktop-app (Tauri v2) | React 19, Tailwind v4, @innate/ui |
| **Backend** | Go CLI skill | Go language |
| **Product** | prd-writer-skill, project-analysis-skill | PRD → Technical Design |
| **Writing/Testing** | writing-skills (RED-GREEN-REFACTOR), superpowers (14 skills) | TDD methodology |
| **Security** | scanning-for-secrets | Secret detection |
| **AI Config** | ai-config (multi-provider) | GLM, OpenAI, Anthropic, OpenRouter |
| **Learning** | learning-mode experiments (dual-agent, QA-to-course, AI tutoring) | Expert-novice pairs |

### What You Need
- A **unified framework** to compose these skills into personal workflows
- A **learning pipeline** that turns "I want to learn X" into a working skill
- **Cross-domain templates** so the coding workflow transfers to writing, music, research, etc.
- **Tutorial generation** so workflows become reproducible guides

---

## 2. The Evolving AI Usage Path

### 2.1 The Maturity Model

A coder with broad interests evolves through distinct stages. Each stage builds on the previous one:

```
Stage 1: Single-Tool User          Stage 2: Skill User           Stage 3: Workflow Builder
"I use Claude to write code"  →   "I have skills for specific   →  "I chain skills into
                                    tasks and domains"               automated workflows"
                                                                      ↓
Stage 4: Skill Composer           Stage 5: Ecosystem Builder    Stage 6: Teacher/Creator
"I compose skills across         "My skill ecosystem evolves     "I generate tutorials,
 domains for new projects"        automatically from my work"     courses, and share workflows"
```

### 2.2 Stage Details

**Stage 1: Single-Tool User**
- Using AI for code completion, Q&A, debugging
- No structured skills, ad-hoc prompting
- *You are past this stage*

**Stage 2: Skill User**
- Have structured SKILL.md files for specific tasks
- Skills trigger automatically based on context
- Each skill solves one class of problems
- *You are here — ~35 skills across 7 categories*

**Stage 3: Workflow Builder**
- Skills are composed into multi-step workflows
- `git-workflow` is your first workflow (init → implement → finish)
- Need to build more workflows for other domains
- *Transitioning here*

**Stage 4: Skill Composer**
- Create new skills by composing existing ones
- "Build me a music production workflow" = desktop-app + writing-skills + custom music skill
- Cross-domain skill transfer becomes natural
- *This is the target for the next 3 months*

**Stage 5: Ecosystem Builder**
- Skills self-improve through usage (learning-mode experiments → skill evolution)
- New skills are generated from observed patterns (like OpenClaw's Skill Workshop)
- The skill set grows organically with your interests

**Stage 6: Teacher/Creator**
- Workflows are packaged as reproducible tutorials
- Others can follow your path
- Community contribution and skill marketplace presence

### 2.3 Your Current Position & Next Steps

You're at **Stage 2 → 3** (Skill User → Workflow Builder). The next evolution is:

1. **Build 3-5 cross-domain workflows** (not just coding)
2. **Create a skill composition system** that lets you declare "I want to do X" and auto-assembles the right skills
3. **Add a learning pipeline** so new domains get a structured onboarding

---

## 3. Skill Composition Framework

### 3.1 The Composition Problem

You already know how to develop things. The challenge isn't "can I build it?" but rather "which skills do I combine, in what order, to be most productive?"

Example: Building a web app requires:
- `innate-frontend` (UI components)
- `prd-writer-skill` (define what to build)
- `project-analysis-skill` (architecture)
- `git-workflow` (task tracking)
- `scanning-for-secrets` (security check)

But today you have to remember and manually invoke each one.

### 3.2 Proposed: Workflow Manifest (WORKFLOW.md)

A workflow manifest declares the skills needed for a project type:

```yaml
# workflows/web-app.yml
name: web-app
description: Full-stack web application development workflow
trigger: "build a web app", "create a website", "develop a web application"

stages:
  - name: define
    description: Define what to build
    skills: [prd-writer-skill]
    output: PRD document

  - name: plan
    description: Technical design
    skills: [project-analysis-skill]
    input_from: define
    output: Technical spec

  - name: scaffold
    description: Project setup
    skills: [innate-frontend, desktop-app]
    input_from: plan
    output: Project structure

  - name: implement
    description: Task-by-task development
    skills: [git-workflow, innate-frontend]
    input_from: scaffold
    loop: true  # repeat for each feature

  - name: secure
    description: Security review
    skills: [scanning-for-secrets]
    input_from: implement

  - name: release
    description: Ship it
    skills: [gh-create-release]
    input_from: secure
```

### 3.3 Workflow Templates

Based on your existing skills, here are the first workflow templates:

#### Workflow A: Full-Stack Web App
```
prd-writer → project-analysis → innate-frontend → git-workflow (loop) → security → release
```

#### Workflow B: Desktop Application
```
prd-writer → project-analysis → desktop-app → git-workflow (loop) → release
```

#### Workflow C: Learning a New Domain
```
learning-mode (dual-agent) → write-practice-skill → evaluate-skill → iterate
```

#### Workflow D: Content Creation (Writing/Blogging)
```
research-skill → outline-skill → writing-skills → review-skill → publish-skill
```

#### Workflow E: Open Source Contribution
```
explore-repo-skill → understand-architecture → find-good-first-issue → implement → pr-skill
```

### 3.4 The Meta-Workflow: "Build Me a Workflow"

The most powerful composition is a meta-workflow that creates other workflows:

```
1. User says: "I want to build a mobile app"
2. System asks clarifying questions about the project
3. System selects relevant skills from the pool
4. System generates a WORKFLOW.md tailored to the project
5. User reviews and adjusts
6. System executes the workflow
```

This is essentially a **skill-composer skill** — a skill that creates workflows from skills.

---

## 4. Learning-to-Practice SKILL Workflow

### 4.1 The Learning Pipeline

For a coder with broad interests, the challenge is: "I want to learn X, but I don't want to just read about it — I want to build something real with AI assistance."

Here's the proposed pipeline:

```
Phase 1: EXPLORE (1-2 days)
├── Use learning-mode (dual-agent) to understand the domain
├── Identify key concepts and skills needed
└── Output: Domain map + learning objectives

Phase 2: SKETCH (1 day)
├── Define a small, real project in the domain
├── Use prd-writer-skill adapted for the new domain
└── Output: Project brief

Phase 3: SCAFFOLD (1 day)
├── Create a new skill for the domain (write-a-skill)
├── Set up project structure
└── Output: SKILL.md + project skeleton

Phase 4: BUILD (ongoing)
├── Execute tasks using git-workflow
├── Skill grows with each task
├── Document what you learn as skill instructions
└── Output: Working project + evolving skill

Phase 5: EVALUATE (weekly)
├── Use skill-creator eval or PromptFoo
├── Identify gaps in the skill
├── Update SKILL.md based on findings
└── Output: Improved skill + benchmark scores

Phase 6: SHARE (when ready)
├── Generate tutorial from the workflow
├── Package as reproducible guide
└── Output: Tutorial document + publishable skill
```

### 4.2 Example: "I Want to Learn Music Production"

| Phase | Action | Skills Used | Output |
|-------|--------|-------------|--------|
| Explore | AI tutor explains music theory, DAW concepts | learning-mode (dual-agent) | Domain map: theory, mixing, mastering, MIDI, synthesis |
| Sketch | Define project: "Create a 4-track EP using AI-assisted composition" | prd-writer-skill (adapted) | Project brief with tracks, style, timeline |
| Scaffold | Create `music-production` skill with DAW setup, composition patterns | write-a-skill | SKILL.md with instructions for music workflow |
| Build | Compose, mix, and master each track with AI assistance | music-production + git-workflow | 4 tracks + evolving skill |
| Evaluate | Review tracks, identify skill gaps | evaluation skill | Improved composition patterns |
| Share | "How I Made an EP with AI: A Step-by-Step Guide" | tutorial generation | Blog post + publishable skill |

### 4.3 The Learning-to-Practice Template

A generalized template that works for any domain:

```yaml
# workflows/learn-and-practice.yml
name: learn-and-practice
description: Learn a new domain by building a real project with AI assistance

variables:
  domain: ""          # e.g., "music production", "game dev", "data science"
  project_goal: ""    # e.g., "Create a 4-track EP", "Build a platformer game"

stages:
  - name: explore
    prompt_template: |
      I want to learn about {{domain}}.
      Act as an expert tutor. Help me understand:
      1. Key concepts and terminology
      2. Core skills needed
      3. Recommended learning path
      4. A small project that would teach me the fundamentals
    skill: learning-mode
    output: domain_map.md

  - name: sketch
    prompt_template: |
      Based on the domain map, create a project brief for: {{project_goal}}
      Include: objectives, deliverables, timeline, success criteria
    skill: prd-writer-skill
    input_from: explore
    output: project_brief.md

  - name: scaffold
    prompt_template: |
      Create a SKILL.md for {{domain}} that captures:
      1. Domain-specific best practices
      2. Tool setup instructions
      3. Common patterns and workflows
      4. Quality criteria
    skill: write-a-skill
    input_from: sketch
    output: SKILL.md + project structure

  - name: build
    prompt_template: |
      Execute the next task in the {{domain}} project.
      Follow the SKILL.md instructions.
    skill: git-workflow
    input_from: scaffold
    loop: true

  - name: evaluate
    prompt_template: |
      Review the work done so far on {{project_goal}}.
      What went well? What could improve?
      Update the SKILL.md with new learnings.
    skill: writing-skills (review)
    input_from: build
    output: updated SKILL.md

  - name: share
    prompt_template: |
      Generate a tutorial from this learning journey:
      {{domain}} → {{project_goal}}
      Include all steps, code, and lessons learned.
    skill: tutorial-generator
    input_from: evaluate
    output: tutorial.md
```

---

## 5. Cross-Domain Skill Transfer

### 5.1 Universal Patterns

Many domains share the same fundamental workflow patterns:

| Pattern | Coding | Writing | Music | Research | Design |
|---------|--------|---------|-------|----------|--------|
| **Define** | PRD | Outline | Brief | Research question | Design brief |
| **Plan** | Architecture | Structure | Arrangement | Methodology | Wireframe |
| **Build** | Code | Draft | Compose | Experiment | Prototype |
| **Review** | Code review | Edit | Mix/master | Peer review | Critique |
| **Ship** | Deploy | Publish | Release | Paper | Handoff |

### 5.2 Transfer Strategy

When entering a new domain, you don't start from zero. You:

1. **Map the domain to universal patterns** — Every domain has define → plan → build → review → ship
2. **Adapt existing skills** — Your `prd-writer-skill` becomes an `outline-writer-skill` or `brief-writer-skill`
3. **Create domain-specific extensions** — Add domain knowledge as a thin layer on top of universal patterns
4. **Reuse workflows** — The `git-workflow` pattern (init → implement → finish) maps to any iterative process

### 5.3 Domain Skill Templates

#### Template: Research & Analysis
```
research-question-skill → methodology-skill → experiment-skill → analysis-skill → paper-skill
```
*Adapts:* project-analysis → data-analysis, writing-skills → academic-writing

#### Template: Creative Production (Video/Podcast/Art)
```
creative-brief-skill → storyboard-skill → production-skill → post-production-skill → distribution-skill
```
*Adapts:* prd-writer → creative-brief, git-workflow → production-pipeline

#### Template: Teaching & Education
```
course-design-skill → lesson-planning-skill → content-creation-skill → assessment-skill → feedback-skill
```
*Adapts:* learning-mode → course-design, writing-skills → content-creation

### 5.4 The Skill Transfer Matrix

Your existing skills and what they transfer to:

| Existing Skill | Transfers To | How |
|---------------|-------------|-----|
| `git-workflow` | Any iterative project | init → implement → finish pattern |
| `prd-writer-skill` | Creative briefs, research proposals, course designs | Structured definition of "what to build" |
| `project-analysis-skill` | Architecture for any domain | Breaking down complex things into components |
| `innate-frontend` | Any UI/visual project | Component system, design tokens, theming |
| `writing-skills` | Any content that needs quality | TDD → Test-Driven Documentation |
| `learning-mode` | Any new domain onboarding | Expert-novice dual-agent learning |
| `ai-config` | Any AI tool setup | Multi-provider configuration pattern |

---

## 6. Reproducible Tutorial Generation

### 6.1 Tutorial Generation Pipeline

Every workflow execution can produce a tutorial:

```
Workflow Execution (git-workflow tracing)
├── tasks/tracing/issue-*.md    ← execution logs
├── SKILL.md files              ← skill instructions
├── Project code                ← actual output
└── Evaluation results          ← quality metrics
         ↓
Tutorial Generator Skill
├── Reads execution trace
├── Extracts key decisions and reasoning
├── Structures as step-by-step guide
├── Adds code examples and explanations
└── Generates tutorial document
         ↓
Output: tutorial.md
```

### 6.2 Tutorial Template

```markdown
# How to [Achieve X]: A Step-by-Step AI-Assisted Guide

## What You'll Build
[Brief description + screenshot/demo]

## Prerequisites
- [Tools and setup needed]
- [Skills to install: npx skills add ...]

## Step 1: Define Your Project
**Skill used:** prd-writer-skill
**Prompt:** "I want to build..."
**What happened:** [Description of the step]
**Key decisions:** [Why we chose X over Y]

## Step 2: Plan the Architecture
...

## Step 3: Build Feature by Feature
...

## Step 4: Review & Refine
...

## Step 5: Ship It
...

## What I Learned
[Reflections and lessons]

## Try It Yourself
[Exact commands and prompts to reproduce]
```

### 6.3 Auto-Generation from Workflow Traces

The `tasks/tracing/` directory already captures workflow execution. A tutorial-generator skill can:

1. Read all trace files for a project
2. Extract the sequence of prompts, tool calls, and decisions
3. Group by workflow stages
4. Add explanatory context
5. Output a formatted tutorial

---

## 7. Action Plan

### Phase 1: Foundation (Week 1-2)

**Goal:** Create the workflow composition system

- [ ] Create `workflows/` directory in the project root
- [ ] Design WORKFLOW.md specification (YAML frontmatter + stages)
- [ ] Build `workflow-web-app.yml` — your most common workflow
- [ ] Build `workflow-learn-and-practice.yml` — the learning pipeline
- [ ] Create a `skill-composer` skill that generates workflows from natural language

**Deliverable:** 2 working workflows + composer skill

### Phase 2: Learning Pipeline (Week 3-4)

**Goal:** Make the "learn X" path repeatable

- [ ] Refine `learning-mode` into a proper skill (not just experiments)
- [ ] Build `domain-explorer` skill — generates a domain map from "I want to learn X"
- [ ] Build `tutorial-generator` skill — creates reproducible guides from workflow traces
- [ ] Test with 2 new domains you're interested in

**Deliverable:** Complete learn-and-practice pipeline tested on 2 domains

### Phase 3: Cross-Domain Templates (Week 5-6)

**Goal:** Build templates for non-coding domains

- [ ] Create `workflow-research.yml` — research & analysis pipeline
- [ ] Create `workflow-content.yml` — writing/blogging/podcast pipeline
- [ ] Create `workflow-teaching.yml` — course creation pipeline
- [ ] Document the skill transfer matrix with real examples

**Deliverable:** 4+ cross-domain workflow templates

### Phase 4: Ecosystem Evolution (Week 7-8)

**Goal:** Make the ecosystem self-improving

- [ ] Build a `skill-evolution` skill that updates SKILL.md files based on usage patterns
- [ ] Integrate evaluation (from Task 2 research) into the workflow cycle
- [ ] Create a personal skill dashboard (could use the Skill Feeds Site from Task 1)
- [ ] Publish top skills to skills.sh / ClawHub

**Deliverable:** Self-improving skill ecosystem + published skills

### Phase 5: Share & Teach (Ongoing)

**Goal:** Generate and share tutorials

- [ ] Generate tutorials from completed workflows
- [ ] Publish on blog / Medium / GitHub
- [ ] Create a "Personal AI Workflow" course
- [ ] Contribute workflows back to the community

**Deliverable:** Published tutorials + community contributions

---

## Quick Reference: File Structure

```
fire-skills/
├── workflows/                        # NEW: Workflow manifests
│   ├── workflow-web-app.yml
│   ├── workflow-learn-and-practice.yml
│   ├── workflow-research.yml
│   ├── workflow-content.yml
│   └── workflow-teaching.yml
├── skills/                           # Skills organized by domain
│   ├── dev/                          # Existing dev skills
│   ├── fe-skills/                    # Existing frontend skills
│   ├── learning/                     # NEW: Learning pipeline skills
│   │   ├── domain-explorer/SKILL.md
│   │   ├── tutorial-generator/SKILL.md
│   │   └── skill-composer/SKILL.md
│   └── cross-domain/                 # NEW: Domain-specific skills
│       ├── writing/SKILL.md
│       ├── research/SKILL.md
│       └── teaching/SKILL.md
├── tutorials/                        # NEW: Generated tutorials
│   └── (auto-generated from workflows)
└── tasks/
    └── tracing/                      # Existing: workflow execution logs
```

---

## Summary

| Question | Answer |
|----------|--------|
| How to build an evolving AI usage path? | **Maturity model:** Tool User → Skill User → Workflow Builder → Skill Composer → Ecosystem Builder → Teacher. You're at Stage 2→3. |
| How to compose skills into workflows? | **WORKFLOW.md manifests** with stages, each referencing skills. A `skill-composer` skill auto-generates workflows from natural language. |
| How to generate reproducible tutorials? | **Tutorial generator skill** reads workflow traces from `tasks/tracing/`, extracts key decisions, and outputs step-by-step guides. |
| How to handle other domains? | **Universal pattern:** Every domain has define → plan → build → review → ship. Map existing skills to these patterns, add thin domain-specific layers. |
| How to learn new domains with AI? | **Learn-and-practice pipeline:** Explore (dual-agent) → Sketch (PRD) → Scaffold (new skill) → Build (iterate) → Evaluate (benchmark) → Share (tutorial). |
