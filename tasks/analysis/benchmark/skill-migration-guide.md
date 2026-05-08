# Skill Migration Guide: Building a Personal Skill Collection

## Overview

This guide analyzes skills from two prominent repositories — **superpowers** (8 skills) and **mattprocock-skills** (14 skills) — and provides a structured approach to migrating and curating skills into a personal collection that matches individual workflow preferences.

---

## 1. Source Skill Inventory

### 1.1 Superpowers Skills (8 skills)

| Skill | Purpose | Complexity | Migration Priority |
|-------|---------|------------|-------------------|
| brainstorming | Socratic design refinement before implementation | High | ★★★★★ |
| dispatching-parallel-agents | Parallel sub-agent execution for independent tasks | Medium | ★★★★ |
| executing-plans | Step-by-step plan execution with checkpoints | Medium | ★★★★ |
| finishing-a-development-branch | Branch integration decisions (merge/PR/keep/discard) | Medium | ★★★★★ |
| receiving-code-review | Technical evaluation of code review feedback | Medium | ★★★★★ |
| requesting-code-review | Dispatch code-reviewer subagent | Low | ★★★ |
| subagent-driven-development | Fresh subagent per task with two-stage review | High | ★★★★ |
| systematic-debugging | Root-cause-first debugging methodology | Medium | ★★★★★ |

**Overall Quality**: Very High. Strong engineering practices, clear anti-patterns, excellent quality gates.

### 1.2 MattProcock Skills (14 skills)

| Skill | Purpose | Complexity | Migration Priority |
|-------|---------|------------|-------------------|
| design-an-interface | Parallel sub-agents for radically different designs | High | ★★★★★ |
| edit-article | Section-based article editing | Low | ★★ |
| git-guardrails-claude-code | Block dangerous git commands via hooks | Medium | ★★★★★ |
| github-triage | Agent brief templates for durable issues | Low | ★★★★ |
| grill-me | Relentless questioning for design stress-testing | Low | ★★★ |
| migrate-to-shoehorn | TypeScript `as` → `fromPartial()` migration | Low | ★★ |
| obsidian-vault | Obsidian note management with wikilinks | Low | ★★ |
| qa | Conversational bug reporting → GitHub issues | Medium | ★★★★ |
| request-refactor-plan | Detailed refactor plans with tiny commits | Medium | ★★★★ |
| scaffold-exercises | Exercise directory scaffolding | Medium | ★★★ |
| setup-pre-commit | Husky + lint-staged pre-commit hooks | Medium | ★★★★★ |
| tdd | Red-green-refactor TDD methodology | High | ★★★★★ |
| triage-issue | Bug triage → root cause → TDD fix plan | Medium | ★★★★★ |
| write-a-skill | Meta-skill: create new agent skills | Medium | ★★★★★ |

**Overall Quality**: High. Strong philosophical foundations (TDD, A Philosophy of Software Design), practical tooling.

---

## 2. Migration Strategy

### 2.1 Personal Taste Assessment Framework

Before migrating, evaluate each skill against these personal criteria:

| Criterion | Question | Weight |
|-----------|----------|--------|
| **Frequency** | How often will I use this in a typical week? | High |
| **Pain Point** | Does this solve a real friction in my current workflow? | High |
| **Complexity Fit** | Is the skill's complexity proportional to its value? | Medium |
| **Integration** | Does it work with my existing tools and stack? | Medium |
| **Customization** | Can I adapt it without rewriting? | Low |
| **Uniqueness** | Does it provide something I can't easily do manually? | Medium |

### 2.2 Tier-Based Migration Plan

#### Tier 1: Core Workflow (Migrate Immediately)

These skills form the backbone of any serious development workflow:

1. **systematic-debugging** (superpowers) — Iron Law: no fixes without root cause. Prevents the most common developer mistake.
2. **tdd** (mattprocock) — Red-green-refactor with vertical slicing. Philosophically sound.
3. **brainstorming** (superpowers) — Socratic design process prevents premature implementation.
4. **finishing-a-development-branch** (superpowers) — Clear merge/PR/keep/discard decisions.
5. **design-an-interface** (mattprocock) — "Design it twice" principle produces better APIs.
6. **git-guardrails-claude-code** (mattprocock) — Safety net for destructive operations.

#### Tier 2: Enhancement (Migrate When Needed)

Skills that add significant value in specific scenarios:

7. **subagent-driven-development** (superpowers) — For large plans with independent tasks.
8. **triage-issue** (mattprocock) — Bug investigation → TDD fix plan workflow.
9. **receiving-code-review** (superpowers) — Technical rigor in review responses.
10. **request-refactor-plan** (mattprocock) — Safe incremental refactoring.
11. **setup-pre-commit** (mattprocock) — Project scaffolding for code quality.
12. **write-a-skill** (mattprocock) — Meta-skill for extending the collection.
13. **executing-plans** (superpowers) — When working from written plans.

#### Tier 3: Situational (Keep for Reference)

Skills that are useful but niche:

14. **dispatching-parallel-agents** (superpowers) — Multiple independent failures.
15. **qa** (mattprocock) — Conversational QA sessions.
16. **grill-me** (mattprocock) — Design stress-testing.
17. **github-triage** (mattprocock) — Agent brief templates.
18. **requesting-code-review** (superpowers) — Code review requests.
19. **scaffold-exercises** (mattprocock) — Exercise scaffolding.

#### Tier 4: Skip or Replace

Skills that are either too niche or can be replaced by simpler approaches:

20. **edit-article** (mattprocock) — Limited use for most developers.
21. **migrate-to-shoehorn** (mattprocock) — Too TypeScript-specific.
22. **obsidian-vault** (mattprocock) — Only useful for Obsidian users.

### 2.3 Migration Process

For each skill being migrated:

```
1. Clone the skill directory structure
2. Read and understand the SKILL.md thoroughly
3. Adapt the skill to personal conventions:
   - Update trigger phrases to match your natural language
   - Adjust tool references to your actual toolchain
   - Remove sections irrelevant to your workflow
   - Add personal preferences and constraints
4. Test the skill with 2-3 realistic scenarios
5. Refine based on test results
```

### 2.4 Personal Adaptation Checklist

When adapting a migrated skill:

- [ ] **Trigger words**: Do the activation phrases match how I naturally ask for help?
- [ ] **Tool references**: Are all referenced tools installed and configured?
- [ ] **Path conventions**: Do file paths match my project structure?
- [ ] **Language preference**: Should instructions be in English, Chinese, or bilingual?
- [ ] **Script dependencies**: Are all script dependencies available?
- [ ] **Integration points**: Does it connect properly with my other skills?
- [ ] **Context window**: Is the skill lean enough (< 500 lines for SKILL.md)?
- [ ] **Progressive disclosure**: Are heavy details in references/ not SKILL.md?

---

## 3. Recommended Personal Skill Collection Architecture

```
personal-skills/
├── SKILL.md                          # Index of all personal skills
├── core/                             # Tier 1: Always available
│   ├── systematic-debugging/
│   ├── tdd/
│   ├── brainstorming/
│   ├── finishing-a-development-branch/
│   ├── design-an-interface/
│   └── git-guardrails/
├── workflow/                          # Tier 2: Project-specific
│   ├── subagent-driven-development/
│   ├── triage-issue/
│   ├── receiving-code-review/
│   ├── request-refactor-plan/
│   ├── executing-plans/
│   └── write-a-skill/
└── reference/                         # Tier 3: Load on demand
    ├── dispatching-parallel-agents/
    ├── qa/
    ├── grill-me/
    └── setup-pre-commit/
```

### Loading Strategy

- **Core skills**: Always loaded via CLAUDE.md or settings.json
- **Workflow skills**: Loaded per-project based on `.claude/settings.json`
- **Reference skills**: Available on-demand, not pre-loaded

---

## 4. Key Patterns from Source Repos

### 4.1 Patterns Worth Adopting (from both repos)

| Pattern | Source | Description |
|---------|--------|-------------|
| Iron Law principle | superpowers/systematic-debugging | Absolute rules that prevent common mistakes |
| Progressive disclosure | mattprocock/write-a-skill | SKILL.md < 500 lines, details in references/ |
| Two-stage review | superpowers/subagent-driven-development | Spec compliance first, then code quality |
| Design it twice | mattprocock/design-an-interface | Generate multiple radical alternatives |
| Vertical slicing | mattprocock/tdd | Test complete behaviors, not horizontal layers |
| Quality gates | superpowers/finishing-a-branch | Mandatory checks before proceeding |
| Durable specifications | mattprocock/github-triage | Behavior-focused, not path-dependent specs |

### 4.2 Anti-Patterns to Avoid

| Anti-Pattern | Why Avoid |
|-------------|-----------|
| Overly long SKILL.md | Wastes context window, reduces adherence |
| Hardcoded file paths | Breaks when project structure changes |
| Missing trigger phrases | Agent can't discover the skill |
| No error handling | Agent hallucinates when scripts fail |
| Procedural instructions only | Fragile to code changes; prefer behavioral specs |
