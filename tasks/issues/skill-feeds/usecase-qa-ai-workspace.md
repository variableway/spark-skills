# Use Case: Building a Software QA AI Workspace — From Daily Pain to Product

**Date:** 2026-05-08

---

## Table of Contents

1. [The Idea & The Pain](#1-the-idea--the-pain)
2. [What the Product Does](#2-what-the-product-does)
3. [System Skills That Power This Project](#3-system-skills-that-power-this-project)
4. [Project Skills You Build Along the Way](#4-project-skills-you-build-along-the-way)
5. [Phase 1: Scratch — Do QA Work Manually](#5-phase-1-scratch--do-qa-work-manually)
6. [Phase 2: Notice Patterns & Extract Skills](#6-phase-2-notice-patterns--extract-skills)
7. [Phase 3: Build the Product](#7-phase-3-build-the-product)
8. [Phase 4: Ship & Evolve](#8-phase-4-ship--evolve)
9. [Final Skill Architecture](#9-final-skill-architecture)
10. [Day-by-Day Execution Calendar](#10-day-by-day-execution-calendar)

---

## 1. The Idea & The Pain

### The Daily QA Reality

You're a developer who also handles QA (common in small teams). Every day you:

1. Check GitHub Issues for new bug reports — triage them
2. Write test cases for new features — manually, from the PRD
3. Run regression tests — manual or semi-automated
4. File bugs with repro steps — time-consuming
5. Verify fixes — re-test, close issues
6. Generate QA reports — summarize what was tested, what passed/failed

**The pain:**
- Triage takes 30 min/day, every day, same process
- Writing test cases from PRDs is repetitive — same structure, different features
- Filing bugs follows the same template every time
- QA reports are always the same format with different data
- You keep writing the same prompts to AI: "triage this bug", "write test cases for this feature", "generate a QA report"

### The Idea

**A QA AI Workspace** — a web app where:
- Bugs flow in from GitHub → AI auto-triages them
- You paste a PRD or feature spec → AI generates test cases
- Test runs are tracked → AI identifies flaky tests and regressions
- Bug reports are filed with one click → AI writes repro steps
- QA reports are generated automatically → AI summarizes the week

---

## 2. What the Product Does

### Core Features

```
┌─────────────────────────────────────────────────────────────────┐
│                    QA AI Workspace                               │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Bug Triage   │  │ Test Case    │  │ QA Dashboard         │  │
│  │              │  │ Generator    │  │                      │  │
│  │ GitHub Issues│  │              │  │ Pass/Fail rates      │  │
│  │ → auto-label │  │ PRD → test   │  │ Flaky test alerts   │  │
│  │ → auto-prior │  │ cases with   │  │ Bug trend graph     │  │
│  │ → repro hint│  │ steps &      │  │ Coverage heatmap     │  │
│  │              │  │ assertions   │  │ Weekly report gen   │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐                              │
│  │ Test Runner  │  │ Bug Reporter │                              │
│  │              │  │              │                              │
│  │ Run tests    │  │ One-click    │                              │
│  │ Track results│  │ bug filing   │                              │
│  │ Detect flaky │  │ with AI      │                              │
│  │              │  │ repro steps  │                              │
│  └──────────────┘  └──────────────┘                              │
│                                                                  │
│  Tech Stack: Next.js 16 + React 19 + Tailwind v4 + @innate/ui  │
│  AI: Claude API for triage, test generation, report writing     │
│  Backend: PostgreSQL + tRPC                                      │
└─────────────────────────────────────────────────────────────────┘
```

### User Flow

```
Morning routine:
1. Open QA Workspace → see dashboard: 3 new bugs overnight
2. Click "Triage" → AI labels each bug, suggests priority, writes repro hints
3. Review AI suggestions → approve or adjust
4. Click "Generate Test Cases" for a new feature → AI reads the PRD, writes 15 test cases
5. Review test cases → edit as needed → export to test framework
6. Click "Run Regression" → tests execute → results flow back to dashboard
7. End of week → click "Generate QA Report" → AI writes full summary
```

---

## 3. System Skills That Power This Project

These are skills you already have (or should have) at system level. They handle the **how to develop** part:

| System Skill | What It Does in This Project |
|-------------|------------------------------|
| `git-workflow` | Track every feature as a GitHub Issue → implement → close |
| `innate-frontend` | Build all UI: dashboard, triage view, test case editor, reports |
| `brainstorming` | Design each feature before coding (forced by the skill's HARD-GATE) |
| `writing-plans` | Plan multi-step implementations before touching code |
| `tdd` | Write test cases for the QA workspace itself (meta: using TDD to build a testing tool) |
| `systematic-debugging` | When the test runner or triage logic breaks |
| `verification` | Before shipping each feature: run all checks |
| `caveman` | Save tokens during long build sessions |
| `writing-skills` | When you create new project-level skills (see below) |

### How System Skills Compose During Development

```
You: "Build the bug triage feature"

AI automatically chains:
  1. brainstorming     → "What should triage look like? Let me ask you 3 questions..."
  2. writing-plans     → "Here's the plan: backend triage logic + frontend triage UI + GitHub webhook"
  3. git-workflow init → Creates Issue #12 "Implement bug triage"
  4. tdd               → "First, let me write a test for the triage scoring function..."
  5. innate-frontend   → "Using @innate/ui Card, Badge, and Button components for the triage view"
  6. verification      → "Running all tests... 12 passed, 0 failed"
  7. git-workflow finish → Closes Issue #12 with completion summary
```

**You didn't coordinate anything.** The AI naturally composed 7 system skills because each one's description triggers at the right time.

---

## 4. Project Skills You Build Along the Way

These are **QA-domain-specific skills** that only make sense for this project. You build them through the "do → notice → extract" cycle.

### Skill 1: `bug-triage`

**How you discover it:** You manually triage bugs for a week. Every time, you:
1. Read the bug title + description
2. Check: is it a real bug or a feature request?
3. Assign priority: P0 (production down), P1 (broken feature), P2 (annoyance), P3 (nice to fix)
4. Assign labels: bug type (UI, API, data, auth, performance)
5. Write a quick repro hint: "Try clicking X with Y condition"
6. Assign to the right person or milestone

After doing this 15 times, you extract the pattern:

```yaml
# qa-workspace/.claude/skills/bug-triage/SKILL.md
---
name: bug-triage
description: >
  Triage a bug report for the QA Workspace. Use when a new bug arrives
  via GitHub webhook, user report, or when user says "triage this bug",
  "analyze this issue", or "what priority is this?". Auto-classifies
  bug type, assigns priority, suggests repro steps, and labels.
---

# Bug Triage

## Classification

### Bug Type
- **UI**: Visual issue, layout broken, wrong colors, missing elements
- **API**: Endpoint returns wrong data, status codes, auth errors
- **Data**: Database inconsistency, missing records, duplicate data
- **Performance**: Slow response, timeout, memory leak
- **Security**: Auth bypass, data leak, injection, XSS

### Priority
- **P0**: Production is down or data is lost. Drop everything.
- **P1**: Core feature broken for users. Fix within 24 hours.
- **P2**: Feature partially broken or ugly workaround exists. Fix this week.
- **P3**: Minor annoyance or edge case. Fix when convenient.
- **Question**: Not a bug — needs more information from reporter.

## Process
1. Read the bug title and full description
2. Check if it's a real bug or a feature request (if feature, relabel and skip triage)
3. Classify the bug type (UI/API/Data/Performance/Security)
4. Assign priority based on impact + urgency
5. Write a repro hint (1-2 sentences on how to trigger it)
6. Suggest assignee based on component ownership
7. Output as structured JSON for the triage API

## Output Format
```json
{
  "classification": "API",
  "priority": "P1",
  "repro_hint": "Call GET /api/users with an expired JWT token. Returns 200 instead of 401.",
  "suggested_labels": ["bug", "api", "auth"],
  "suggested_assignee": "backend-team",
  "confidence": 0.85,
  "reasoning": "Auth middleware not checking token expiry. Affects all authenticated endpoints."
}
```
```

**Origin:** 15 real bug triages during Week 1 of the project.

### Skill 2: `test-case-generator`

**How you discover it:** You write test cases for 5 features. Every time:
1. Read the PRD or feature spec
2. Identify test scenarios: happy path, edge cases, error cases
3. Write each test case with: description, preconditions, steps, expected result
4. Cover: functional, boundary, negative, integration

After writing 50+ test cases manually, you extract the pattern:

```yaml
# qa-workspace/.claude/skills/test-case-generator/SKILL.md
---
name: test-case-generator
description: >
  Generate structured test cases from a feature spec or PRD. Use when
  user says "write test cases", "generate tests for this feature",
  "how to test this", or provides a PRD/feature description and asks
  for test coverage. Produces test cases with steps, expected results,
  and priority.
---

# Test Case Generator

## Process
1. Read the feature spec/PRD
2. Identify all user-facing behaviors
3. For each behavior, generate test cases in these categories:

### Categories (generate ALL that apply)
- **Happy path**: Normal user does the right thing → expected success
- **Edge case**: Boundary values, empty inputs, max length, special chars
- **Error case**: Invalid input, missing required fields, wrong format
- **Authorization**: Unauthenticated, wrong role, expired session
- **Concurrency**: Race conditions, duplicate submissions, stale data
- **Performance**: Large dataset, many concurrent users, slow network

## Output Format (per test case)
```
TC-[feature]-[number]: [short title]
Priority: Critical | High | Medium | Low
Type: Functional | Boundary | Negative | Auth | Performance
Preconditions: [what must be true before testing]
Steps:
  1. [action]
  2. [action]
  3. [action]
Expected: [what should happen]
Actual: [leave blank — filled during testing]
Status: Not Run | Pass | Fail | Blocked
```

## Rules
- Minimum 5 test cases per feature
- Every API endpoint gets at least: happy path, auth failure, validation failure
- Every UI form gets at least: valid input, invalid input, empty input
- Mark the 3 most important test cases as "Critical"
```

**Origin:** 50+ manually written test cases across 5 features during Weeks 1-2.

### Skill 3: `qa-report-generator`

**How you discover it:** You write weekly QA reports for 3 weeks. Every time:
1. Query test results from the past week
2. Calculate pass/fail rates, new bugs found, bugs fixed
3. Identify flaky tests
4. Summarize risk areas
5. Write it all in the same format

```yaml
# qa-workspace/.claude/skills/qa-report-generator/SKILL.md
---
name: qa-report-generator
description: >
  Generate QA summary reports. Use when user asks for a "QA report",
  "testing summary", "weekly QA update", or "how did testing go".
  Pulls data from test results and bug tracker, produces formatted report.
---

# QA Report Generator

## Data Sources
1. Test run results (pass/fail/skip counts per suite)
2. Bug tracker (new bugs, resolved bugs, open bugs by priority)
3. Flaky test detector (tests with inconsistent results)

## Report Sections

### 1. Executive Summary
- Period: [date range]
- Tests run: [total], passed: [N], failed: [N], skipped: [N]
- Pass rate: [%] (vs last week: [%])
- New bugs: [N], resolved: [N], net change: [+/-N]

### 2. Test Coverage
- [Feature]: [pass rate] — [status emoji]
- [Feature]: [pass rate] — [status emoji]

### 3. Bug Analysis
- New bugs by priority: P0: [N], P1: [N], P2: [N], P3: [N]
- Bug trend: [improving/stable/worsening]
- Longest open bugs: [list top 3]

### 4. Flaky Tests
- Tests with >20% result variance: [list]
- Recommendation: [fix/remove/quarantine]

### 5. Risk Assessment
- High risk areas: [features with low pass rate or many open bugs]
- Recommendations: [what to focus on next week]

### 6. Next Week Priorities
- [ ] [Priority item 1]
- [ ] [Priority item 2]
- [ ] [Priority item 3]
```

**Origin:** 3 weekly QA reports during Weeks 2-4.

### Skill 4: `flaky-test-detector`

**How you discover it:** You notice some tests pass sometimes and fail other times. You investigate each one manually: look at test history, check timing, check dependencies. After 5 investigations, you extract the pattern.

```yaml
# qa-workspace/.claude/skills/flaky-test-detector/SKILL.md
---
name: flaky-test-detector
description: >
  Detect and diagnose flaky tests. Use when user reports "test sometimes
  fails", "flaky test", or when test results show inconsistent pass/fail
  patterns. Analyzes test history and identifies root causes.
---

# Flaky Test Detector

## Detection Criteria
A test is flaky if over the last 10 runs:
- Pass rate is between 30% and 70%
- OR: pass rate changed significantly after a specific commit

## Diagnosis Checklist
1. **Timing dependency**: Does it use sleep/wait? Race condition?
2. **Order dependency**: Does it depend on other tests running first?
3. **External dependency**: API call, database state, file system?
4. **Data dependency**: Does it assume specific test data exists?
5. **Randomness**: Does it use random values or shuffled data?
6. **Resource contention**: Memory, ports, file handles?

## Output
```
Flaky Test: [test name]
Pass rate (last 10): 60% (6 pass, 4 fail)
Likely cause: [timing/order/data/external/random/resource]
Evidence: [specific observations]
Fix suggestion: [concrete recommendation]
```
```

**Origin:** 5 flaky test investigations during Weeks 2-3.

---

## 5. Phase 1: Scratch — Do QA Work Manually (Week 1)

### Goal
Don't build anything. Just do QA work with AI assistance. Observe what repeats.

### Daily Log

**Monday: Bug Triage Day**

```
You: "I have 8 new GitHub Issues. Help me triage them."

AI: "Let me read each one..."
[Reads Issue #101]
"This looks like a P1 API bug. The /api/users endpoint returns 500 when
 email is null. Labels: bug, api, backend. Repro: create a user with
 null email, call GET /api/users."

You: "Good. Next one."
[Issue #102]
"This is a feature request, not a bug. User wants dark mode.
 Labels: feature-request, UI. Priority: P3."

You: "Correct. Next..."

[After all 8]
You note: "I typed 'help me triage' and the AI did the same analysis
  every time: classify, prioritize, label, repro hint.
  Pattern detected: triage has a fixed structure."
```

**Pattern Log Entry:**
```
Bug triage — 8 instances today
Same process every time: classify → prioritize → label → repro → assign
Ready to skill-ify after 3 more instances
```

**Tuesday: Test Case Writing Day**

```
You: "I need test cases for the user registration feature.
 The PRD says: users sign up with email + password,
 get confirmation email, must verify within 24 hours."

AI: "Here are test cases:
 TC-reg-01: Successful registration with valid email/password
 TC-reg-02: Registration with existing email — should show error
 TC-reg-03: Registration with weak password — should reject
 TC-reg-04: Registration with invalid email format — should reject
 TC-reg-05: Confirmation email not verified within 24h — account disabled
 TC-reg-06: Resend confirmation email
 ..."

You note: "Same structure every time: happy path → duplicate →
 validation → timeout → edge cases. I keep asking the same thing
 for different features."
```

**Pattern Log Entry:**
```
Test case generation — 3 features this week
Same categories: happy path, edge, error, auth, performance
Same output format: TC-number, priority, type, steps, expected
Ready to skill-ify after 2 more features
```

**Wednesday-Sunday: Continue doing QA, logging patterns**

By end of Week 1, your Pattern Log has:
- Bug triage: 15 instances → ready to extract
- Test case generation: 5 features → ready to extract
- QA report writing: 2 instances → need 1 more
- Flaky test investigation: 5 instances → ready to extract

---

## 6. Phase 2: Notice Patterns & Extract Skills (Week 2)

### Extract Skills from Pattern Log

Using the `writing-skills` (system) skill:

```
You: "I've been doing QA triage for 2 weeks. Here's my pattern log:

Bug triage (15 instances):
- Read title + description
- Classify: UI/API/Data/Performance/Security
- Prioritize: P0/P1/P2/P3/Question
- Write repro hint
- Suggest labels and assignee

Create a SKILL.md that captures this pattern."

AI uses writing-skills (system) → produces bug-triage/SKILL.md
→ You save to qa-workspace/.claude/skills/bug-triage/
```

Repeat for:
- `test-case-generator` → from 5 features of test case writing
- `qa-report-generator` → from 3 weekly reports (need 1 more, but good enough)
- `flaky-test-detector` → from 5 investigations

### Test Each Extracted Skill

```
You: "Triage this bug: 'Login page shows 500 error when password contains
 special characters &'"

AI triggers bug-triage skill:
{
  "classification": "API",
  "priority": "P1",
  "repro_hint": "Go to /login, enter any email, enter password 'test&123', click Login",
  "suggested_labels": ["bug", "api", "auth"],
  "confidence": 0.9
}

You: "Correct. The repro hint is accurate. Skill works."
```

If the skill fails or misses something → update the instructions.

---

## 7. Phase 3: Build the Product (Weeks 3-6)

### Week 3: Project Setup + Bug Triage Feature

**System skills in play:** `git-workflow`, `innate-frontend`, `brainstorming`, `writing-plans`, `tdd`

```
You: "Let's build the QA Workspace. Start with the bug triage feature."

AI chains:
  1. brainstorming (system):
     "Before coding, let me clarify: How do bugs arrive? GitHub webhook?
      Manual entry? Both? What triage info do you show in the UI?"

  2. writing-plans (system):
     "Plan:
     - Backend: GitHub webhook receiver + triage API endpoint
     - Frontend: Triage inbox view + triage detail panel
     - AI integration: Claude API for auto-triage using bug-triage skill"

  3. git-workflow init (system):
     Creates Issue #1 "Bug triage: webhook + API + UI"

  4. tdd (system):
     "First, write a test for the triage scoring function:
     test('classifies auth errors as API type and P1 priority')"

  5. innate-frontend (system):
     "Using @innate/ui:
     - Card for each bug in the inbox
     - Badge for priority (P0=red, P1=orange, P2=yellow, P3=gray)
     - Button for 'Accept Triage' / 'Edit Triage'"

  6. Project skill bug-triage activates:
     When the AI writes the triage logic, it follows the skill's
     classification system and output format

  7. verification (system):
     "Running tests... 18 passed, 0 failed"

  8. git-workflow finish (system):
     Closes Issue #1
```

### Week 4: Test Case Generator Feature

**Same system skills, different feature:**

```
You: "Build the test case generator. Users paste a PRD, AI generates test cases."

AI chains: brainstorming → writing-plans → git-workflow init → tdd → innate-frontend

Project skill test-case-generator activates:
  - AI follows the skill's category system (happy, edge, error, auth, perf)
  - Uses the skill's output format (TC-number, priority, type, steps, expected)

Result: PRD input → AI analysis → structured test case list → export to CSV/JSON
```

### Week 5: Dashboard + QA Reports

```
You: "Build the QA dashboard with weekly report generation."

System skills: brainstorming, writing-plans, git-workflow, innate-frontend, tdd

Project skill qa-report-generator activates:
  - AI builds the report template matching the skill's sections
  - Dashboard shows data in the same structure as the report
```

### Week 6: Flaky Test Detection + Polish

```
You: "Add flaky test detection. Analyze test run history for inconsistency."

Project skill flaky-test-detector activates:
  - AI implements the detection algorithm from the skill
  - UI shows flaky tests with diagnosis and fix suggestions
```

---

## 8. Phase 4: Ship & Evolve (Week 7+)

### Ship

```
System skill: gh-create-release → "Create release v1.0.0"
```

### Evolve

As you use the product daily, you discover new patterns:

**Week 8:** You notice you keep writing "verification checklist" comments on PRs
→ Extract: `pr-verification-checklist` skill

**Week 9:** You notice the AI suggests wrong test priorities sometimes
→ Refine `test-case-generator` skill: add domain-specific priority rules

**Week 10:** You notice you keep cross-referencing bugs with related test cases
→ Extract: `bug-test-traceability` skill — links bugs to test cases that cover them

**Week 12:** You have 7 project skills → compose into workflows:

```yaml
# qa-workspace/.claude/skills/daily-qa-routine/SKILL.md
---
name: daily-qa-routine
description: >
  Morning QA routine. Triggers when user says "morning QA", "daily QA",
  or "start QA day". Runs through the daily QA workflow.
---

1. Use `bug-triage` — triage any new bugs overnight
2. Use `flaky-test-detector` — check for new flaky tests from last night's run
3. Use `test-case-generator` — generate test cases for today's features
4. Use `qa-report-generator` — update the daily dashboard

# Weekly (Fridays):
5. Use `qa-report-generator` — generate full weekly report
```

---

## 9. Final Skill Architecture

### What You End Up With

```
SYSTEM LEVEL (~/.claude/skills/) — 15 skills
├── git-workflow/          # Task tracking (pre-existing)
├── local-workflow/        # Local tracking (pre-existing)
├── github-cli-skill/      # GitHub ops (pre-existing)
├── gh-create-release/     # Releases (pre-existing)
├── innate-frontend/       # UI components (pre-existing)
├── desktop-app/           # Desktop framework (pre-existing)
├── caveman/               # Token saver (pre-existing)
├── brainstorming/         # Design first (pre-existing)
├── writing-plans/         # Planning (pre-existing)
├── tdd/                   # Test-driven dev (pre-existing)
├── systematic-debugging/  # Debug methodology (pre-existing)
├── verification/          # Quality gate (pre-existing)
├── writing-skills/        # Skill authoring (pre-existing)
├── requesting-code-review/# Code review (pre-existing)
└── ship-feature/          # Feature workflow (pre-existing)

PROJECT LEVEL (qa-workspace/.claude/skills/) — 7 skills
├── bug-triage/              # Bug classification & prioritization
├── test-case-generator/     # PRD → structured test cases
├── qa-report-generator/     # Data → formatted QA report
├── flaky-test-detector/     # Test consistency analysis
├── pr-verification/         # PR checklists (extracted Week 8)
├── bug-test-traceability/   # Bug ↔ test case linking (extracted Week 10)
└── daily-qa-routine/        # Workflow: chains all above (Week 12)
```

### How They Compose

```
Daily use:
  "morning QA"
  → daily-qa-routine (project workflow)
    → bug-triage (project) — triages new bugs
    → flaky-test-detector (project) — checks test health
    → test-case-generator (project) — for today's features
    → innate-frontend (system) — renders the dashboard
    → git-workflow (system) — tracks everything

Building new features:
  "add regression test suite tracking"
  → brainstorming (system) — designs the feature
  → writing-plans (system) — creates implementation plan
  → git-workflow (system) — tracks the task
  → tdd (system) — writes tests first
  → innate-frontend (system) — builds the UI
  → test-case-generator (project) — informs the feature design
  → verification (system) — checks quality
```

---

## 10. Day-by-Day Execution Calendar

### Week 1: Do QA Manually, Log Patterns

| Day | What You Do | Patterns Found |
|-----|------------|---------------|
| Mon | Triage 8 bugs manually with AI | Bug triage pattern (8 instances) |
| Tue | Write test cases for user registration | Test case generation pattern (1 feature) |
| Wed | Write test cases for payment flow | Test case generation pattern (2 features) |
| Thu | Investigate 2 flaky tests | Flaky test pattern (2 instances) |
| Fri | Write weekly QA report | QA report pattern (1 instance) |

### Week 2: Extract Skills, Test Them

| Day | What You Do | Skill Created |
|-----|------------|---------------|
| Mon | Extract `bug-triage` from 15 triages | `bug-triage/SKILL.md` |
| Tue | Extract `test-case-generator` from 5 features | `test-case-generator/SKILL.md` |
| Wed | Extract `flaky-test-detector` from 5 investigations | `flaky-test-detector/SKILL.md` |
| Thu | Extract `qa-report-generator` from 3 reports | `qa-report-generator/SKILL.md` |
| Fri | Test all 4 skills, fix failures | Refined versions |

### Week 3-6: Build the Product

| Week | Feature | System Skills Used | Project Skills Used |
|------|---------|-------------------|-------------------|
| 3 | Bug triage (webhook + API + UI) | brainstorm, plans, tdd, frontend, git-workflow, verify | bug-triage |
| 4 | Test case generator (PRD → tests) | brainstorm, plans, tdd, frontend, git-workflow, verify | test-case-generator |
| 5 | Dashboard + QA reports | brainstorm, plans, tdd, frontend, git-workflow, verify | qa-report-generator |
| 6 | Flaky test detection + polish | brainstorm, plans, tdd, frontend, git-workflow, verify | flaky-test-detector |

### Week 7: Ship

| Day | What You Do |
|-----|------------|
| Mon | Final testing, bug fixes |
| Tue | Security review (scanning-for-secrets) |
| Wed | Write documentation |
| Thu | Create release v1.0.0 (gh-create-release) |
| Fri | Deploy + announce |

### Week 8+: Use & Evolve

| Week | New Pattern Detected | New Skill Extracted |
|------|---------------------|-------------------|
| 8 | PR verification checklists | `pr-verification` |
| 10 | Bug ↔ test case linking | `bug-test-traceability` |
| 12 | Morning routine composition | `daily-qa-routine` workflow |

---

## Key Takeaway

You didn't start by designing 7 QA skills. You started by **doing QA work for 2 weeks**, noticed what repeated, extracted only the patterns with 3+ real instances, refined them through failure, and composed them into a workflow.

The product was built by the same skills that the product manages. The system skills (TDD, brainstorming, git-workflow) built the product. The project skills (bug-triage, test-case-generator) ARE the product's core logic, extracted into SKILL.md format so the AI can execute them consistently.

**This is the pattern: Do → Notice → Extract → Refine → Compose. Build skills through doing, not through design.**
