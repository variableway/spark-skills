# Guide: How to Try, Test, Modify & Integrate Other People's Skills

**Date:** 2026-05-08

A practical, step-by-step guide for rapidly discovering, evaluating, adapting, and integrating external skills into your project.

---

## Table of Contents

1. [Quick Start: 5-Minute Skill Trial](#1-quick-start-5-minute-skill-trial)
2. [Discovery: Where to Find Skills](#2-discovery-where-to-find-skills)
3. [Method A: Via Plugin Marketplace](#3-method-a-via-plugin-marketplace)
4. [Method B: Via skills.sh CLI](#4-method-b-via-skillssh-cli)
5. [Method C: Manual GitHub Clone](#5-method-c-manual-github-clone)
6. [Method D: Direct File Copy](#6-method-d-direct-file-copy)
7. [The Rapid Evaluation Checklist](#7-the-rapid-evaluation-checklist)
8. [How to Modify & Adapt a Skill](#8-how-to-modify--adapt-a-skill)
9. [How to Integrate Into Your Project](#9-how-to-integrate-into-your-project)
10. [Batch Testing: Try 10 Skills in an Hour](#10-batch-testing-try-10-skills-in-an-hour)
11. [Common Pitfalls](#11-common-pitfalls)
12. [Cheat Sheet](#12-cheat-sheet)

---

## 1. Quick Start: 5-Minute Skill Trial

The fastest way to try someone else's skill right now:

```bash
# Step 1: Find a skill on skills.sh (browser)
# Go to https://skills.sh/ and find something interesting

# Step 2: Install it (one command)
npx skills add                          # interactive picker — auto-detects your agent

# Step 3: Try it in Claude Code
claude
# Then type a prompt that matches the skill's description
# Example: if you installed "caveman", type "caveman mode"
```

That's it. The skill is now active in your session. If you don't like it, just delete the files.

---

## 2. Discovery: Where to Find Skills

### 2.1 Primary Sources

| Source | URL | What You'll Find |
|--------|-----|-----------------|
| **skills.sh** | [skills.sh](https://skills.sh/) | 91K+ skills, trending/popular rankings, cross-platform |
| **ClawHub** | [clawhub.ai](https://clawhub.ai/) | 52K+ tools, rated/reviewed, security scanned |
| **Official Anthropic** | [claude.com/plugins](https://claude.com/plugins) | Curated, tested, official skills |
| **MCP Market** | [mcpmarket.com](https://mcpmarket.com/tools/skills/leaderboard) | Skills ranked by GitHub stars |

### 2.2 Community Collections

| Collection | URL | Size |
|-----------|-----|------|
| awesome-claude-skills | [github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 22K+ stars |
| ComposioHQ/awesome-claude-skills | [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 78+ skills |
| alirezarezvani/claude-skills | [github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 235+ skills |
| anthropics/skills | [github.com/anthropics/skills](https://github.com/anthropics/skills) | Official Anthropic skills |

### 2.3 Search Tips

On **skills.sh**, use the leaderboard tabs:
- **All Time** — proven, widely-used skills
- **Trending (24h)** — what's hot right now
- **Hot** — fastest-growing

On **GitHub**, search:
```
"SKILL.md" topic:claude-code
"SKILL.md" topic:agent-skills
```

---

## 3. Method A: Via Plugin Marketplace

**Best for:** Skills packaged as Claude Code plugins with marketplace.json

```bash
# Step 1: Browse the official marketplace
# Inside Claude Code:
/plugin
# → Go to "Discover" tab → browse by category

# Step 2: Install a specific plugin
/plugin install github@claude-plugins-official

# Step 3: Try it immediately
# The skill is now active — use a prompt that matches its description

# Step 4: If you don't like it
/plugin disable github@claude-plugins-official
```

### Adding Community Marketplaces

```bash
# Add a third-party marketplace
/plugin marketplace add xiaolai/claude-plugin-marketplace

# Add Anthropic's demo marketplace
/plugin marketplace add anthropics/claude-code

# Add any GitHub repo with marketplace.json
/plugin marketplace add owner/repo-name

# Now browse and install from it
/plugin
# → "Discover" tab → you'll see plugins from all added marketplaces
```

### Scope Options

| Scope | What it does | File modified |
|-------|-------------|---------------|
| **User** (default) | Available in all your projects | `~/.claude/settings.json` |
| **Project** | Shared with all collaborators | `.claude/settings.json` (committed) |
| **Local** | Only you, only this project | `.claude/settings.local.json` |

```bash
# Install to project scope (team can use it)
claude plugin install my-skill@marketplace --scope project
```

---

## 4. Method B: Via skills.sh CLI

**Best for:** Cross-platform skills from the skills.sh registry

```bash
# Step 1: Install a skill (interactive)
npx skills add
# Shows a searchable list — type to filter, select to install

# Step 2: Install a specific skill by URL
npx skills add https://skills.sh/vercel-labs/skills/find-skills

# Step 3: The skill lands in your project's skill directory
# For Claude Code: .claude/skills/find-skills/SKILL.md

# Step 4: Start Claude Code and try it
claude
# Type a prompt that triggers the skill based on its description

# Step 5: Don't like it? Remove the directory
rm -rf .claude/skills/find-skills
```

### Using `find-skills` to Discover More

The #1 skill on skills.sh is `find-skills` — it searches skills.sh from within Claude Code:

```bash
npx skills add https://skills.sh/vercel-labs/skills/find-skills
```

Then in Claude Code:
```
find me skills for React component testing
```

It searches skills.sh and suggests matching skills you can install.

---

## 5. Method C: Manual GitHub Clone

**Best for:** Skill repos without marketplace.json, or when you want the full source

```bash
# Step 1: Clone the repo
git clone https://github.com/anthropics/skills.git /tmp/anthropics-skills

# Step 2: Browse what's inside
ls /tmp/anthropics-skills/
# frontend-design/  skill-creator/  pdf/  pptx/  ...

# Step 3: Copy the skill you want into your project
cp -r /tmp/anthropics-skills/frontend-design .claude/skills/

# Step 4: Clean up
rm -rf /tmp/anthropics-skills

# Step 5: Try it in Claude Code
claude
# Type: "design a landing page for my app"
```

### For Superpowers-style repos

```bash
# Clone obra/superpowers (137K installs, community favorite)
git clone https://github.com/obra/superpowers.git /tmp/superpowers

# Copy specific skills you want
cp -r /tmp/superpowers/skills/brainstorming .claude/skills/
cp -r /tmp/superpowers/skills/writing-skills .claude/skills/

# Clean up
rm -rf /tmp/superpowers
```

---

## 6. Method D: Direct File Copy

**Best for:** When you find a single SKILL.md and want to try it immediately

```bash
# Step 1: Create the skill directory
mkdir -p .claude/skills/my-new-skill

# Step 2: Download the SKILL.md directly
curl -o .claude/skills/my-new-skill/SKILL.md \
  https://raw.githubusercontent.com/owner/repo/main/skills/skill-name/SKILL.md

# Step 3: Try it
claude
```

### Using the mastra-ai/skills-api to fetch content

```bash
# If you self-host the API, you can fetch any skill's content:
curl http://localhost:3456/api/skills/anthropics/skills/frontend-design/content

# Returns the full parsed SKILL.md
```

---

## 7. The Rapid Evaluation Checklist

When you try a new skill, run through this checklist in **5 minutes**:

### 7.1 Quick Scan (1 minute)

```bash
# Read the SKILL.md
cat .claude/skills/skill-name/SKILL.md
```

Check:
- [ ] **Description is clear** — Do you understand what it does?
- [ ] **Trigger is specific** — Will it activate at the right times? Too broad = annoying, too narrow = never fires
- [ ] **Instructions are concise** — Under 200 lines is ideal; 500+ means the skill is probably too complex
- [ ] **No suspicious commands** — Watch for `curl | bash`, `rm -rf`, data exfiltration patterns
- [ ] **Dependencies are reasonable** — Does it need tools you don't have?

### 7.2 Functional Test (2 minutes)

In Claude Code, test with:

1. **Happy path** — Give a prompt that should trigger the skill. Does it work?
2. **False trigger test** — Give an unrelated prompt. Does the skill fire when it shouldn't?
3. **Quality check** — Is the output actually good? Better than without the skill?

### 7.3 Integration Check (2 minutes)

- [ ] Does it conflict with your existing skills? (same trigger words?)
- [ ] Does it match your project's conventions? (code style, file structure)
- [ ] Does it add real value over what you already have?

### Decision

| Result | Action |
|--------|--------|
| Passes all checks | Keep and integrate (Section 9) |
| Good idea but needs changes | Modify and adapt (Section 8) |
| Doesn't fit | Remove: `rm -rf .claude/skills/skill-name` |

---

## 8. How to Modify & Adapt a Skill

### 8.1 Understanding SKILL.md Anatomy

```yaml
---
name: original-skill-name                    # ← Change this
description: "What it does. Use when..."     # ← Critical: controls trigger behavior
---

# Skill Title

## Instructions

[The actual instructions Claude follows]

## Rules
[Constraints and guidelines]

## Examples
[Input/output examples]
```

### 8.2 What to Modify

| What | Why | How |
|------|-----|-----|
| **`name`** | Avoid conflicts with other skills | Rename to `my-project-skillname` |
| **`description`** | Control when it triggers | Make it more specific to your use case |
| **Instructions** | Adapt to your project conventions | Add your code style, file structure, naming conventions |
| **Examples** | Match your domain | Replace generic examples with project-specific ones |
| **Remove sections** | Reduce token overhead | Delete anything not relevant to your workflow |

### 8.3 Adaptation Patterns

#### Pattern 1: Narrow the Scope

Original skill is too broad? Narrow the description:

```yaml
# Before (triggers on ANY code review)
description: "Review code for quality issues"

# After (only triggers in your project)
description: "Review code changes in the fire-skills project for quality, following @innate/ui patterns and Tailwind CSS v4 conventions. Use when user asks to review code or changes in this project."
```

#### Pattern 2: Add Project Context

Inject your project's specifics:

```markdown
## Project Context

This skill operates in the fire-skills monorepo:
- Frontend: Next.js 16 + React 19 + Tailwind CSS v4
- Components: @innate/ui (57+ components)
- Task tracking: git-workflow (GitHub Issue-based)
- Testing: writing-skills (TDD methodology)
```

#### Pattern 3: Merge Multiple Skills

Combine the best parts of two skills:

```markdown
---
name: my-project-workflow
description: "Complete development workflow combining brainstorming with git-workflow for the fire-skills project."
---

# My Project Workflow

Combines elements from:
- brainstorming (from superpowers) — design before coding
- git-workflow (from dev/) — task tracking

## Step 1: Brainstorm
[Copy brainstorming instructions, adapted]

## Step 2: Track
[Copy git-workflow instructions]

## Step 3: Implement
[Your specific implementation patterns]
```

#### Pattern 4: Strip Down to Essentials

If a skill is bloated (500+ lines), keep only what you need:

```bash
# Read the original
wc -l .claude/skills/complex-skill/SKILL.md
# 847 lines — too much!

# Create a lean version
# Keep: frontmatter, core instructions, critical rules
# Remove: advanced features, edge cases, verbose examples

# Target: under 200 lines
```

### 8.4 Real Example: Adapting "brainstorming" from Superpowers

Original: 150+ lines with visual companion, checklist gates, spec directory conventions.

Adapted for your project:

```yaml
---
name: brainstorm
description: >
  Use before any new feature in the fire-skills project. Explores requirements
  before implementation. Triggers when user wants to build, create, or add something.
  Does NOT trigger for bug fixes, small edits, or refactors.
---

# Brainstorm

Quick design session before coding.

1. Read the current project context (check recent files, docs, commits)
2. Ask ONE clarifying question at a time (max 3)
3. Propose 2 approaches with trade-offs
4. Wait for approval before coding

## Rules
- Keep it under 5 minutes
- No implementation until approved
- Save brief spec to docs/specs/ if complex
```

Result: Same core behavior, 20 lines instead of 150+, tailored to your project.

---

## 9. How to Integrate Into Your Project

### 9.1 Integration Decision Tree

```
Is the skill useful as-is?
├── YES → Install to project scope
│         /plugin install skill-name@marketplace --scope project
│         OR: keep in .claude/skills/
│
├── NEEDS CHANGES → Fork and adapt
│         1. Copy to .claude/skills/my-skill/
│         2. Modify SKILL.md (Section 8)
│         3. Test thoroughly
│         4. Commit to repo
│
└── JUST IDEAS → Extract concepts, write your own
          1. Read their SKILL.md for inspiration
          2. Write a new skill from scratch
          3. Credit the original in comments if significant
```

### 9.2 Where to Put Skills in Your Project

```
.claude/skills/              ← Project-level skills (committed to git)
├── git-workflow/            ← Your custom workflows
├── local-workflow/
├── brainstorm/              ← Adapted from superpowers
└── code-review/             ← Adapted from community

superpowers/skills/          ← External skill collections (reference only)
├── brainstorming/           ← Original, unmodified
└── ...

mattprocock-skills/          ← Another external collection
├── caveman/                 ← Original, unmodified
└── ...
```

### 9.3 Managing Conflicts

If two skills have overlapping triggers:

```yaml
# Skill A
description: "Review code for quality. Use when user asks to review code."

# Skill B
description: "Review PRs on GitHub. Use when user asks to review a PR."
```

These will both fire on "review my code". Fix by making descriptions more specific:

```yaml
# Skill A — general code quality
description: "Review code quality in local files. Use when user asks to review code or files they're working on."

# Skill B — GitHub PR review
description: "Review a GitHub pull request. Use when user mentions 'PR', 'pull request', or asks to review changes on GitHub."
```

### 9.4 Version Control

Track your adapted skills in git:

```bash
# Commit your adaptations
git add .claude/skills/my-adapted-skill/
git commit -m "Add adapted code-review skill from anthropics/skills"
```

If you want to track the original source:

```bash
# Add as a git submodule (for reference)
git submodule add https://github.com/obra/superpowers.git superpowers

# Now you have the original for reference, your adaptations in .claude/skills/
```

---

## 10. Batch Testing: Try 10 Skills in an Hour

### 10.1 The Rapid Skill Sprint

Set up a test project:

```bash
# Create a throwaway project for testing skills
mkdir /tmp/skill-lab && cd /tmp/skill-lab
git init
claude init

# Now you have a clean environment to test skills without affecting your real project
```

### 10.2 Install Top 10 Skills from skills.sh

```bash
# In /tmp/skill-lab:

# 1. find-skills — the meta-skill that finds other skills
npx skills add https://skills.sh/vercel-labs/skills/find-skills

# 2. frontend-design — Anthropic's official design skill
npx skills add https://skills.sh/anthropics/skills/frontend-design

# 3. brainstorming — from superpowers
git clone --depth 1 https://github.com/obra/superpowers.git /tmp/sp
cp -r /tmp/sp/skills/brainstorming .claude/skills/
cp -r /tmp/sp/skills/writing-skills .claude/skills/
rm -rf /tmp/sp

# 4. caveman — token-saving mode
git clone --depth 1 https://github.com/juliusbrussee/caveman.git /tmp/caveman
cp -r /tmp/caveman/caveman .claude/skills/
rm -rf /tmp/caveman

# 5-10: Use find-skills to discover more
claude
# "find me skills for testing, code review, debugging, git workflows, and deployment"
```

### 10.3 Quick Test Each Skill

For each skill, run a 3-minute test:

```
Skill: frontend-design
Test prompt: "Design a pricing page for a SaaS app"
Check: Does it produce good layout guidance? Trigger correctly?
Verdict: KEEP / ADAPT / DROP

Skill: brainstorming
Test prompt: "I want to add user authentication"
Check: Does it ask good questions before jumping to code?
Verdict: KEEP / ADAPT / DROP

Skill: caveman
Test prompt: "caveman mode"
Test prompt 2: "explain React hooks" (should still be terse)
Test prompt 3: "normal mode" (should revert)
Verdict: KEEP / ADAPT / DROP
```

### 10.4 Score Sheet Template

| Skill | Trigger OK | Quality OK | Conflicts | Needs Adapt | Verdict |
|-------|-----------|-----------|-----------|------------|---------|
| find-skills | Y/N | Y/N | Y/N | Y/N | KEEP/ADAPT/DROP |
| frontend-design | Y/N | Y/N | Y/N | Y/N | KEEP/ADAPT/DROP |
| brainstorming | Y/N | Y/N | Y/N | Y/N | KEEP/ADAPT/DROP |
| caveman | Y/N | Y/N | Y/N | Y/N | KEEP/ADAPT/DROP |
| ... | ... | ... | ... | ... | ... |

### 10.5 Promote Winners to Real Project

```bash
# Copy skills that passed into your real project
cp -r /tmp/skill-lab/.claude/skills/good-skill /path/to/fire-skills/.claude/skills/

# Clean up the test lab
rm -rf /tmp/skill-lab
```

---

## 11. Common Pitfalls

### 11.1 Trigger Conflict

**Problem:** Two skills fire on the same prompt, producing confused output.

**Fix:** Make descriptions mutually exclusive with specific trigger conditions.

### 11.2 Token Bloat

**Problem:** Too many skills loaded = system prompt is huge = worse performance.

**Fix:**
- Keep only skills you actually use
- Strip verbose skills to essentials (target < 200 lines)
- Use `disable-model-invocation: true` for skills that should only trigger via slash command

### 11.3 Outdated Skills

**Problem:** Skill was written for an older model version and produces suboptimal results.

**Fix:** Test against the current model. If the model does fine without the skill, the skill is obsolete (Anthropic calls this "capability obsolescence detection").

### 11.4 Security Risks

**Problem:** Third-party skills can contain malicious instructions (341+ found on ClawHub).

**Fix:**
- Always read the full SKILL.md before using
- Watch for: `curl | bash`, `rm -rf`, API calls to unknown servers, data exfiltration patterns
- Prefer skills from verified publishers (Anthropic, Vercel, Microsoft, etc.)
- Use SkillProbe or security scanning for untrusted skills

### 11.5 "Works on My Machine"

**Problem:** Skill depends on tools/binaries that aren't in your environment.

**Fix:** Check the skill's `metadata.requires` section for dependencies:
```yaml
metadata: {"openclaw": {"requires": {"bins": ["uv"], "env": ["API_KEY"]}}}
```

---

## 12. Cheat Sheet

### Commands Quick Reference

```bash
# === DISCOVER ===
npx skills add                                    # Interactive skill picker
open https://skills.sh/                           # Browse skills.sh
open https://skills.sh/trending                   # Trending skills
open https://clawhub.ai                           # Browse ClawHub

# === INSTALL (Plugin Marketplace) ===
/plugin                                           # Browse all marketplaces
/plugin install name@marketplace                  # Install a plugin
/plugin install name@marketplace --scope project  # Install for team

# === INSTALL (skills.sh) ===
npx skills add                                    # Interactive
npx skills add https://skills.sh/owner/repo/name  # Direct URL

# === INSTALL (Manual) ===
git clone --depth 1 https://github.com/owner/repo.git /tmp/repo
cp -r /tmp/repo/skills/skill-name .claude/skills/
rm -rf /tmp/repo

# === MANAGE ===
/plugin disable name@marketplace                  # Disable without removing
/plugin uninstall name@marketplace                # Remove completely
/reload-plugins                                   # Apply changes without restart
rm -rf .claude/skills/skill-name                  # Remove manually installed skill

# === TEST ===
claude                                            # Start Claude Code
# Type a prompt that matches the skill's description
# Check: does it trigger? Is the output good? Any conflicts?

# === EVALUATE ===
npx skillmark run .claude/skills/skill-name       # Benchmark with Skillmark

# === BATCH TEST ===
mkdir /tmp/skill-lab && cd /tmp/skill-lab          # Clean test environment
git init && claude init
# Install and test skills here, promote winners to real project
```

### Workflow Summary

```
DISCOVER → INSTALL → TEST (5 min) → DECIDE
                                        ├── KEEP → integrate into project
                                        ├── ADAPT → modify SKILL.md → test again → integrate
                                        └── DROP → rm -rf .claude/skills/skill-name
```

### Sources

- [Discover and install prebuilt plugins — Claude Code Docs](https://code.claude.com/docs/en/discover-plugins)
- [Create and distribute a plugin marketplace — Claude Code Docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [skills.sh — The Agent Skills Directory](https://skills.sh/)
- [ClawHub — OpenClaw Skills Registry](https://clawhub.ai/)
- [Official Anthropic Skills — GitHub](https://github.com/anthropics/skills)
- [anthropics/claude-plugins-official — GitHub](https://github.com/anthropics/claude-plugins-official)
- [obra/superpowers — GitHub](https://github.com/obra/superpowers)
- [Agent Skills 101 — Practical Guide](https://blog.serghei.pl/posts/agent-skills-101/)
- [The Best Way to Do Agentic Development — DEV Community](https://dev.to/chand1012/the-best-way-to-do-agentic-development-in-2026-14mn)
