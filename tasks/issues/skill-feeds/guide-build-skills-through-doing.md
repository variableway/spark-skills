# Instruction Report: Building Your Own Skills Through Doing

**Date:** 2026-05-08

## The Core Idea

You don't design skills on paper. You **discover them by doing real work**, notice what patterns repeat, then capture those patterns into SKILL.md files. Skills are not invented — they are **mined from experience**.

```
TRADITIONAL (wrong approach):
  Think about what skill I need → Design it → Write SKILL.md → Try to use it

ACTUAL (right approach):
  Do real work with AI → Notice "I keep doing X the same way" → Capture X as a skill → Refine through more use
```

This report covers the complete process: from doing real things → observing patterns → extracting skills → refining → composing into workflows.

---

## Table of Contents

1. [The Skill-Building Lifecycle](#1-the-skill-building-lifecycle)
2. [Stage 1: Do Real Work (No Skills Yet)](#2-stage-1-do-real-work-no-skills-yet)
3. [Stage 2: Notice Repeating Patterns](#3-stage-2-notice-repeating-patterns)
4. [Stage 3: Extract a Rough Skill](#4-stage-3-extract-a-rough-skill)
5. [Stage 4: Use the Skill, Observe Failures](#5-stage-4-use-the-skill-observe-failures)
6. [Stage 5: Refine Until Stable](#6-stage-5-refine-until-stable)
7. [Stage 6: Compose Skills Into Workflows](#7-stage-6-compose-skills-into-workflows)
8. [Two Detailed Walkthroughs](#8-two-detailed-walkthroughs)
9. [The Skill Mining Toolkit](#9-the-skill-mining-toolkit)
10. [Anti-Patterns to Avoid](#10-anti-patterns-to-avoid)

---

## 1. The Skill-Building Lifecycle

```
    ┌──────────────────────────────────────────────────────────┐
    │                                                          │
    │   1. DO       ──→  Solve a real problem with AI          │
    │        │                                                 │
    │        ▼                                                 │
    │   2. NOTICE   ──→  "I keep doing this the same way"      │
    │        │                                                 │
    │        ▼                                                 │
    │   3. EXTRACT  ──→  Capture the pattern as a rough skill  │
    │        │                                                 │
    │        ▼                                                 │
    │   4. USE      ──→  Apply the skill on the next task      │
    │        │                                                 │
    │        ▼                                                 │
    │   5. REFINE   ──→  Fix what broke, add what was missing  │
    │        │                                                 │
    │        ▼                                                 │
    │   6. COMPOSE  ──→  Chain with other skills into workflow │
    │        │                                                 │
    │        └──────────→ back to 1 (new problem, new cycle)   │
    │                                                          │
    └──────────────────────────────────────────────────────────┘
```

**Critical principle:** Every skill in your library should have at least **3 real use cases** behind it. If you can't name 3 times you actually used the pattern, it's premature abstraction — don't write it yet.

---

## 2. Stage 1: Do Real Work (No Skills Yet)

### The Rule

**Never start by writing a skill.** Start by solving a real problem with raw AI interaction. The skill emerges from the doing.

### How It Works

You have a task. You use AI to help. You don't think about skills at all. You just work.

**Example: You need to review code before committing.**

```
You (to AI):
"Review the changes I made in the last commit. Check for:
 - Bugs and logic errors
 - Security issues
 - Missing error handling
 - Code style consistency
Then tell me if it's safe to push."

AI reviews... gives feedback... you fix... push.
```

You do this **manually every time**. No skill involved. Just raw prompting.

**Another example: You need to create a GitHub Issue for a task.**

```
You (to AI):
"Create a GitHub Issue titled 'Add user authentication' with this description:
Users need to log in with email/password. Should use JWT tokens..."

AI runs: gh issue create --title "..." --body "..."
```

You do this repeatedly. Each time you type a similar prompt.

### What's Happening

You're building **implicit knowledge** — you know what to ask the AI, what order to ask it in, what checks to run. But this knowledge lives only in your head and your prompt history.

### What NOT to Do

- Don't write a skill yet — you don't know what the skill should contain
- Don't try to generalize — focus on the specific task at hand
- Don't look at other people's skills for "inspiration" — that leads to designing skills you don't need

### When to Move to Stage 2

You're ready for Stage 2 when you catch yourself thinking: **"I've typed this same prompt 3+ times now."**

---

## 3. Stage 2: Notice Repeating Patterns

### The Signals

A pattern is ready to become a skill when you notice any of these:

| Signal | Example |
|--------|---------|
| **Same prompt, different inputs** | "Review my code" → "Review the API changes" → "Review the auth logic" |
| **Same sequence of steps** | Always: create issue → implement → test → close issue |
| **Same corrections to AI output** | "No, check for SQL injection too" — every single time |
| **Same checklist in your head** | Before shipping: security? tests? docs? migration? |
| **Same frustration** | "AI keeps forgetting to check X" or "AI always formats Y wrong" |

### How to Capture Patterns

Keep a simple log. After each work session, spend 2 minutes noting:

```markdown
## Pattern Log

### [Date]: Code Review
- What I asked: "Review my code"
- What AI missed: SQL injection check, missing test for edge case
- What I had to add manually: "Also check for security issues"
- Repetition count: 4th time this week
- Ready to skill-ify? YES

### [Date]: GitHub Issue Creation
- What I asked: "Create a GitHub Issue for..."
- Steps I always follow: describe task → add labels → assign
- What I keep re-typing: the gh issue create command with same flags
- Repetition count: 6th time
- Ready to skill-ify? YES
```

### The 3-Use Rule

Before extracting a skill, ask: **"Can I name 3 real instances where I did this?"**

```
Code review pattern:
  1. Reviewed auth middleware — caught missing token expiry
  2. Reviewed API endpoint — found SQL injection
  3. Reviewed React component — caught missing loading state
  → YES, 3 uses. Extract it.
```

---

## 4. Stage 3: Extract a Rough Skill

### The Extraction Process

Take your pattern log and turn it into a minimal SKILL.md.

**Step 1: Write the description (trigger)**

The description controls WHEN the skill activates. Be specific about:
- What action triggers it
- What context is required

```yaml
# BAD — too vague (triggers on everything)
description: "Review code for issues"

# BAD — too narrow (only works in one project)
description: "Review Go code in the fire-skills project"

# GOOD — specific enough to trigger correctly
description: >
  Review code changes for bugs, security issues, and quality.
  Use when user asks to review code, review changes, or check a PR.
  Checks: logic errors, security vulnerabilities, missing error handling,
  code style, test coverage.
```

**Step 2: Write the instructions (what AI should do)**

Start minimal. Just capture the core steps:

```markdown
# Code Review

## Steps

1. Read the changed files (use `git diff` or read the specified files)
2. Check for:
   - Logic errors and bugs
   - Security vulnerabilities (SQL injection, XSS, auth bypass)
   - Missing error handling
   - Code style consistency
   - Missing tests for new logic
3. For each issue found, explain:
   - What's wrong
   - Why it matters
   - How to fix it (with code example)
4. Give a verdict: SAFE TO PUSH / FIX BEFORE PUSHING
```

**Step 3: Add examples (from your real use cases)**

```markdown
## Examples

### Good review output
"Found 2 issues:

1. **SQL Injection** in `src/api/users.ts:42`
   The `id` parameter is interpolated directly into the query string.
   Fix: Use parameterized query.

2. **Missing error handling** in `src/api/users.ts:38`
   `db.query()` can throw but there's no try/catch.
   Fix: Wrap in try/catch, return 500 on failure.

Verdict: **FIX BEFORE PUSHING**"
```

**Step 4: Save as a rough skill**

```bash
mkdir -p .claude/skills/code-review
# Write the SKILL.md
```

### The "Rough" Part

At this stage, the skill is deliberately rough:
- It only covers what you've actually done (not hypothetical cases)
- It may be missing edge cases (you'll discover those in Stage 4)
- It may trigger incorrectly (you'll fix the description in Stage 5)

**This is fine.** A rough skill used 10 times beats a perfect skill never used.

---

## 5. Stage 4: Use the Skill, Observe Failures

### How to Use It

Just work normally. The skill will trigger (or not) based on its description. Pay attention to:

1. **False triggers** — Skill fires when it shouldn't
2. **Missed triggers** — Skill doesn't fire when it should
3. **Incomplete instructions** — AI follows the skill but misses something
4. **Wrong output format** — AI follows the steps but the format doesn't match what you need
5. **Edge cases** — AI gets confused by situations not covered in the skill

### The Failure Log

Every time the skill doesn't work perfectly, note it:

```markdown
## Failure Log: code-review skill

### Failure 1: False trigger
- What happened: User said "review the meeting notes" and the skill fired
- Why: Description says "review" without qualifying "code"
- Fix: Narrow the description to mention "code changes" explicitly

### Failure 2: Missed check
- What happened: AI didn't check for race conditions in async code
- Why: Instructions only mention "logic errors" generically
- Fix: Add "race conditions in async/await code" to the checklist

### Failure 3: Wrong format
- What happened: AI gave a paragraph instead of the structured format
- Why: Instructions say "explain" but don't enforce the format strictly enough
- Fix: Make the output format a HARD requirement with an explicit template
```

### The Key Metric

**How many tasks can you complete without manually correcting the AI?**

- 0/5 → Skill needs major rework
- 2/5 → Skill is getting there, refine the instructions
- 4/5 → Skill is stable, ready to compose
- 5/5 → Skill is mature, consider sharing it

---

## 6. Stage 5: Refine Until Stable

### What to Refine

Based on your failure log, fix three things:

#### 1. Refine the Description (Trigger Accuracy)

```yaml
# Before (causing false triggers)
description: "Review code for issues"

# After (specific trigger)
description: >
  Review CODE CHANGES for bugs, security issues, and quality.
  Use when user asks to review code, review changes, check a diff,
  or asks 'is this safe to push?'.
  Do NOT trigger for reviewing documents, plans, or text."
```

#### 2. Refine the Instructions (Completeness)

```markdown
# Before
2. Check for logic errors and bugs

# After
2. Check for:
   - Logic errors and bugs
   - Race conditions in async/await code
   - Off-by-one errors in loops
   - Null/undefined access without guards
   - Incorrect error propagation
```

#### 3. Refine the Output Format (Usability)

```markdown
# Before
3. For each issue found, explain what's wrong

# After
3. For each issue, output EXACTLY this format:
   **[SEVERITY: CRITICAL|WARNING|INFO] [CATEGORY] in `file:line`**
   What: one sentence
   Why: one sentence
   Fix: code block with the fix

4. End with EXACTLY:
   **Verdict: SAFE TO PUSH** or **Verdict: FIX BEFORE PUSHING**
```

### When to Stop Refining

Stop when:
- The skill triggers correctly 9 out of 10 times
- The output is useful without manual correction 8 out of 10 times
- You've used it on at least 5 different tasks

At this point, it's **stable** — good enough to rely on and compose with other skills.

---

## 7. Stage 6: Compose Skills Into Workflows

### What Changes

Once you have 3+ stable skills, you'll notice they naturally chain together:

```
Code review skill + GitHub Issue skill + Test skill = "Ship safe code" workflow
```

### How to Compose

Create a WORKFLOW.md that declares the chain:

```yaml
---
name: ship-safe-code
description: "Safe shipping workflow. Triggers when user says 'ship this', 'push this', or 'ready to deploy'"
---

# Ship Safe Code

## Steps

1. **Review** — Use `code-review` skill to check all changes
2. **Fix** — If issues found, fix them
3. **Test** — Use `writing-skills` (TDD) to verify fixes
4. **Security** — Use `scanning-for-secrets` to check for leaks
5. **Ship** — Use `gh-create-release` to create a release

## Rules
- NEVER skip step 1 (review)
- If review says "FIX BEFORE PUSHING", stop and fix
- Only proceed to step 5 when review says "SAFE TO PUSH"
```

### Workflow Evolution

Workflows evolve the same way skills do:

1. You compose a rough workflow
2. You use it on real tasks
3. You notice gaps (missing steps, wrong order, unnecessary steps)
4. You refine the workflow
5. Eventually it stabilizes

---

## 8. Two Detailed Walkthroughs

### Walkthrough 1: Build a "Skill Hub Development" Skill Through Doing

**The use case:** You want to build a Skill Hub (from the previous report) and naturally develop skills along the way.

#### Week 1: Do the work, notice patterns

```
Day 1: You fetch skills from skills.sh API
  → Typed the same curl command 5 times with different params
  → Pattern: "Fetch data from API endpoint"

Day 2: You set up PostgreSQL and import data
  → Wrote the same INSERT pattern 10 times
  → Pattern: "Import JSON data into PostgreSQL table"

Day 3: You build the search UI
  → Asked AI "create a search component" the same way 3 times
  → Pattern: "Build a search page with innate-frontend"

Day 4: You add skill scoring
  → Kept checking the same things (description length, security flags)
  → Pattern: "Auto-evaluate skill quality"

Day 5: You add trending data
  → Same query pattern for ranking data
  → Pattern: "Track and display trending skills"
```

#### Week 2: Extract skills from patterns

From Week 1's patterns, extract these skills:

**Skill 1: `api-data-fetcher`**
```yaml
---
name: api-data-fetcher
description: >
  Fetch paginated data from REST APIs. Use when user needs to
  collect data from an external API, import API data, or set up
  a data pipeline from an HTTP source.
---

# API Data Fetcher

## Steps
1. Identify the API endpoint and parameters
2. Test with curl: `curl "ENDPOINT?page=1&pageSize=10" | jq '.'`
3. Write a fetch script with:
   - Pagination handling (fetch all pages)
   - Error handling (retry on failure)
   - Rate limiting (delay between requests)
   - Progress logging (show count)
4. Save raw data as JSON for import
```
**Origin:** 5 real instances of fetching from skills.sh, GitHub, ClawHub APIs

**Skill 2: `json-to-postgres`**
```yaml
---
name: json-to-postgres
description: >
  Import JSON data into PostgreSQL tables. Use when user needs to
  load API data, CSV data, or JSON files into a database.
---

# JSON to PostgreSQL Importer

## Steps
1. Analyze JSON structure → design table schema
2. Create table with appropriate column types
3. Write import script:
   - Read JSON file
   - Transform to match table schema
   - Batch INSERT (100 rows per batch)
   - Handle duplicates with ON CONFLICT
4. Verify: `SELECT count(*) FROM table`
```
**Origin:** 10 real imports during the Skill Hub project

**Skill 3: `skill-quality-scorer`**
```yaml
---
name: skill-quality-scorer
description: >
  Score AI skills for quality. Use when evaluating skills from
  marketplaces or reviewing skill quality. Checks: description
  clarity, instruction quality, security, trigger specificity.
---

# Skill Quality Scorer

## Checks (each scored 0-20, total 0-100)

### 1. Description Clarity (20 pts)
- Specific about when to trigger? (10)
- Specific about what it does? (10)

### 2. Instruction Quality (20 pts)
- Clear step-by-step? (10)
- Under 200 lines? (5)
- Includes examples? (5)

### 3. Security (20 pts)
- No curl|bash patterns? (10)
- No data exfiltration? (10)

### 4. Trigger Specificity (20 pts)
- Won't false-trigger on unrelated prompts? (10)
- Won't miss relevant prompts? (10)

### 5. Dependencies (20 pts)
- Minimal external dependencies? (10)
- Dependencies are common/standard? (10)

## Output
Score: X/100
Grade: A (90+) / B (80+) / C (70+) / D (60+) / F (<60)
Issues: [list of problems found]
```
**Origin:** 3 real evaluation sessions where you kept checking the same criteria

#### Week 3: Compose into a workflow

```yaml
---
name: skill-hub-setup
description: >
  Set up a Skill Hub data pipeline. Use when setting up a new
  skill aggregation project or refreshing skill data.
---

# Skill Hub Setup

1. Use `api-data-fetcher` to pull skills from skills.sh
2. Use `json-to-postgres` to import into database
3. Use `skill-quality-scorer` to score each skill
4. Update trending rankings
```

**Result:** 4 skills + 1 workflow, all born from real work, none designed in advance.

---

### Walkthrough 2: Build a "Learn New Topics" Skill Through Doing

**The use case:** You want to learn music production, and along the way develop skills for learning any new topic.

#### Phase 1: Just learn (no skills)

```
Day 1: You explore music theory
  → Prompt: "Explain music theory basics for a programmer"
  → AI gives a good explanation but you don't retain it
  → You realize: reading about music ≠ understanding music

Day 2: You try to apply it
  → Prompt: "Help me write a chord progression"
  → AI gives you C-Am-F-G
  → You play it, it sounds basic
  → Prompt: "Make it more interesting"
  → AI suggests adding 7ths, inversions
  → You try it — sounds better
  → You realize: you learn by DOING, not reading

Day 3: You try to compose a full song
  → Prompt: "Help me write a simple song with these chords"
  → AI walks you through: melody → bass → drums → arrangement
  → Each step you try, fail, adjust, try again
  → You notice the SAME process works for any song:
     1. Pick key and tempo
     2. Write chord progression
     3. Add melody
     4. Add bass
     5. Add drums
     6. Arrange (intro, verse, chorus, bridge)
     7. Mix and adjust levels

Day 4: You try to mix
  → Prompt: "How do I mix this track?"
  → AI explains EQ, compression, reverb, panning
  → You apply each one, hear the difference
  → Process: solo each track → EQ → compress → add space → adjust volume

Day 5: You look back
  → You've made 3 rough songs
  → Each time you followed roughly the same steps
  → You've been typing similar prompts over and over
  → Pattern detected: "Learn a creative skill by building things"
```

#### Phase 2: Extract the patterns

**Pattern 1: "The Creative Learning Process"**

You did this for music. But you realize it's the same process you used for:
- Learning frontend development (build components → notice patterns → extract)
- Learning game design (build levels → notice what's fun → refine)
- Learning technical writing (write articles → notice structure → formalize)

Extract the meta-pattern:

```yaml
---
name: learn-by-building
description: >
  Learn a new creative or technical skill by building real projects
  instead of reading theory. Use when user says 'I want to learn X',
  'teach me X', or 'help me get started with X'. Covers any domain:
  coding, music, design, writing, research, etc.
---

# Learn by Building

## Philosophy
Reading about X ≠ knowing X. You learn by building real things.
Theory comes AFTER you've tried and failed, not before.

## Process

### Step 1: Quick Orientation (15 minutes)
Give a SHORT overview of the domain (not a lecture):
- 5 key concepts they need to know
- 3 tools they'll use
- 1 small project that teaches fundamentals

### Step 2: First Build (30 minutes)
Guide them through building the simplest possible version:
- Give clear, specific instructions
- Let them DO each step (don't do it for them)
- When they get stuck, explain the WHY, not just the fix
- Celebrate when it works (even if it's ugly)

### Step 3: Reflect (10 minutes)
Ask them:
- "What did you just build? Explain it in your own words."
- "What was confusing?"
- "What do you want to make next?"

### Step 4: Next Build (30 minutes)
Slightly harder project that builds on Step 2:
- Introduce ONE new concept at a time
- Connect it to what they already know
- Let them struggle a bit before helping

### Step 5: Pattern Recognition (10 minutes)
Point out the patterns:
- "You've now used [concept] 3 times. Here's the pattern: ..."
- "Notice how [step A] always leads to [step B] in this domain?"
- These patterns become the foundation for the next skill

### Step 6: Capture
Ask them to write down:
- 3 things they learned
- 1 thing that surprised them
- What they want to learn next
```

**Pattern 2: "Domain Onboarding" — the quick orientation template**

```yaml
---
name: domain-onboarding
description: >
  Quick orientation for a new domain. Use when starting to learn
  a new topic. Produces a domain map with concepts, tools, and
  a first project idea.
---

# Domain Onboarding

## Output Format (produce EXACTLY this)

### [DOMAIN] Quick Start

**5 Key Concepts:**
1. [Concept] — one sentence explanation
2. [Concept] — one sentence explanation
3. ...

**3 Tools You'll Use:**
1. [Tool] — what it does, why it matters
2. ...
3. ...

**First Project: [Name]**
- What: one sentence
- Why: teaches [fundamental concept]
- Steps: 5 numbered steps to complete it
- Success: how they know it worked

**Transfer Map:**
(What the user already knows that transfers to this domain)
| What you know | How it transfers |
|---|---|
| e.g., Programming logic | Music is pattern-based, like algorithms |
| e.g., CSS layouts | Design grids = rhythm structures |
```

**Pattern 3: "Build-Reflect-Next" cycle**

This is the core learning loop you discovered:

```yaml
---
name: build-reflect-next
description: >
  The core learning cycle. After completing any build exercise,
  run reflection and suggest the next step. Use when user completes
  a task or asks "what's next" in a learning context.
---

# Build → Reflect → Next

## Reflect (ask these questions)
1. "Explain what you just did in your own words"
2. "What was the hardest part?"
3. "What concept clicked for you?"
4. "What still feels confusing?"

## Next (suggest based on their answers)
- If they found it easy → increase difficulty by 30%
- If they found it hard → practice the same concept with different inputs
- If they're confused → explain the concept differently, with analogy
- If they're excited → build on their enthusiasm with a related challenge

## Rule
NEVER give more than ONE new concept at a time.
Mastery comes from repetition with slight variation, not flooding with new info.
```

#### Phase 3: Compose into a learning workflow

```yaml
---
name: learn-new-topic
description: >
  Complete learning workflow for any new domain. Triggers when
  user says "I want to learn X", "teach me X", or "help me get
  started with X".
---

# Learn New Topic Workflow

1. Use `domain-onboarding` — quick orientation (15 min)
2. Use `learn-by-building` — first 3 build cycles (2 hours)
3. Use `build-reflect-next` — after each build
4. When 3+ patterns detected → use `writing-skills` to create a domain-specific SKILL.md
5. Use `git-workflow` to track learning projects
```

**Result:** You started wanting to learn music production. You ended up with:
- 4 new transferable skills (learn-by-building, domain-onboarding, build-reflect-next, learn-new-topic)
- 1 domain-specific skill (music-composition, music-mixing)
- 1 workflow (learn-new-topic)
- All mined from real experience, not theoretical design

---

## 9. The Skill Mining Toolkit

### What to Keep Handy

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Pattern Log** | Note repeating patterns | After every work session (2 min) |
| **Failure Log** | Track where skills fail | Every time AI doesn't do what you want |
| **3-Use Rule** | Decide when to extract | Before writing any SKILL.md |
| **Rough-first** | Keep first drafts minimal | Always — never over-design |
| **git-workflow** | Track skill creation as tasks | When extracting or refining |

### The Minimal SKILL.md Template

Start with this. Nothing more:

```yaml
---
name: [verb]-[noun]
description: "[What it does]. Use when [trigger condition]."
---

# [Skill Name]

## Steps
1. [Step]
2. [Step]
3. [Step]

## Output
[What the result should look like]
```

If you can't fit it in this template, you're over-thinking it.

### Questions to Ask Before Writing a Skill

1. **Have I done this 3+ times?** If no → don't write it yet
2. **Can I name 3 specific instances?** If no → the pattern isn't clear enough
3. **Is this different from my existing skills?** If no → extend an existing skill instead
4. **Will I use this in the next month?** If no → don't bother
5. **Can I explain it in under 20 lines?** If no → it's probably multiple skills, not one

---

## 10. Anti-Patterns to Avoid

### Anti-Pattern 1: Designing Skills You Don't Need

```
❌ "I should have a skill for every possible task"
✅ "I have skills for tasks I actually do repeatedly"

❌ "Let me design a comprehensive skill framework"
✅ "Let me work for a week and see what patterns emerge"
```

### Anti-Pattern 2: Copying Others Without Understanding

```
❌ "This skill from skills.sh looks cool, let me install it and use it"
✅ "What problem does this skill solve? Do I have that problem? Have I
    encountered it 3+ times? If yes, let me write my own version based
    on MY experience with the problem"
```

Other people's skills are **inspiration**, not solutions. Your workflow is different from theirs.

### Anti-Pattern 3: Over-Abstracting

```
❌ One skill that handles code review, testing, deployment, and documentation
✅ Four small skills, each doing one thing well, composed into a workflow
```

### Anti-Pattern 4: Premature Sharing

```
❌ "I just wrote this skill, let me publish it to skills.sh"
✅ "I've used this skill on 10+ tasks, refined it 3 times, and it's stable.
    NOW I'll share it."
```

### Anti-Pattern 5: Skills That Replace Thinking

```
❌ Skill that says "always do X" for every situation
✅ Skill that says "consider X, Y, Z and pick the best approach for the context"
```

Skills should encode **decision-making wisdom**, not rigid rules. The best skills teach the AI *how to think* about a problem, not just *what to do*.

---

## Summary: The One-Page Process

```
1. Pick something you want to DO (not learn — DO)
2. Do it with AI assistance, raw prompting, no skills
3. When you notice "I keep typing the same thing":
   → Write it down in a Pattern Log
   → Wait until you have 3+ instances
4. Extract the pattern into a minimal SKILL.md
5. Use the skill on the next task
6. When it fails: note why, fix the skill
7. When it works 8/10 times: it's stable
8. When you have 3+ stable skills: compose into workflows
9. When the workflow is stable: consider sharing
10. Go back to step 1 — the cycle never ends
```

The skills you build through doing are always better than skills you design through thinking. Because they're grounded in YOUR real workflow, YOUR real mistakes, YOUR real patterns.
