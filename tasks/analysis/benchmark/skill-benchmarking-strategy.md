# Skill Benchmarking Strategy

## Overview

This document provides a comprehensive strategy for benchmarking AI agent skills, based on analysis of major benchmarking tools and best practices from the ecosystem.

---

## 1. Benchmarking Tools Landscape

### 1.1 Tool Comparison Matrix

| Tool | Type | Focus | Metrics | Maturity |
|------|------|-------|---------|----------|
| **SkillsBench** | Gym-style benchmark | Skill composition (2+ skills working together) | Task completion rate, agent behavior | Early, active development |
| **PinchBench** | Benchmark system | Real-world LLM coding agent tasks (scheduling, coding, research) | Task accuracy, real-world fidelity | Moderate |
| **Skillmark** | CLI platform | Individual skill testing with public leaderboard | Accuracy, tokens, duration, cost | Moderate, has leaderboard |
| **Claude Code Skill Benchmarks** | Treatment-based experiment | Skill documentation design impact on adherence | Pass rate, turns, duration, artifact quality | Mature, LangChain-backed |
| **SRE-skills-bench** | Domain benchmark | Site Reliability Engineering tasks | Real-world SRE problem solving | Early |
| **Performance Benchmark Skill** | Plug-in skill | Core Web Vitals, API latency, build speed | LCP, FID, CLS, response times | Practical |

### 1.2 Recommended Tool Selection

| Goal | Recommended Tool | Why |
|------|-----------------|-----|
| Quick local skill validation | **Skillmark** | CLI-based, runs locally or from Git repos, has leaderboard |
| Documentation quality testing | **Claude Code Skill Benchmarks** | Treatment-based methodology directly tests documentation impact |
| Multi-skill composition | **SkillsBench** | Specifically designed for skill interaction testing |
| Performance regression | **Performance Benchmark Skill** | Pre/Post PR comparison reports |

---

## 2. Benchmarking Methodology

### 2.1 Four-Dimension Evaluation Framework

Based on synthesis of all benchmarking tools, skills should be evaluated across four dimensions:

```
┌─────────────────────────────────────────────┐
│           Skill Quality Model               │
├─────────────┬─────────────┬─────────────────┤
│ Correctness │ Efficiency  │ Discoverability │
│             │             │                 │
│ Does the    │ How many    │ Can the agent   │
│ skill work  │ tokens/time │ find and        │
│ as intended?│ does it use?│ trigger it?     │
├─────────────┴─────────────┴─────────────────┤
│              Robustness                      │
│ Does it handle edge cases and failures?      │
└─────────────────────────────────────────────┘
```

#### Dimension 1: Correctness (Primary)

- **Knowledge tests**: Can the agent recall and apply skill concepts?
- **Task tests**: Can the agent execute the skill's workflow end-to-end?
- **Pattern adherence**: Does the agent follow the skill's recommended patterns?

**Measurement**: Pass rate on predefined test cases (0-100%)

#### Dimension 2: Efficiency (Secondary)

- **Token consumption**: Total tokens used during skill execution
- **Duration**: Wall-clock time to complete skill tasks
- **Tool calls**: Number of tool invocations needed
- **Cost**: Estimated API cost per execution

**Measurement**: Benchmark against baseline (no skill) and alternatives

#### Dimension 3: Discoverability (Tertiary)

- **Trigger accuracy**: Does the agent select the right skill for a given prompt?
- **False positive rate**: Does the agent trigger the skill inappropriately?
- **Description clarity**: Can the agent understand the skill from description alone?

**Measurement**: Test with varied prompt phrasings, measure selection accuracy

#### Dimension 4: Robustness (Essential)

- **Edge case handling**: Does the skill work with unusual inputs?
- **Error recovery**: Can the agent recover from script failures?
- **Cross-project portability**: Does the skill work across different project types?

**Measurement**: Edge case test suite, failure injection tests

### 2.2 Testing Process

```
Phase 1: Static Analysis
├── SKILL.md line count (< 500?)
├── Directory structure compliance
├── Frontmatter completeness (name, description)
└── Progressive disclosure check

Phase 2: Knowledge Testing
├── Concept coverage quiz
├── Decision tree comprehension
└── Anti-pattern recognition

Phase 3: Task Execution
├── Happy path execution
├── Alternative path execution
└── Error path execution

Phase 4: Comparative Analysis
├── vs. No skill (baseline)
├── vs. Alternative skill versions
└── vs. Previous skill version (regression)
```

---

## 3. Practical Benchmarking Setup

### 3.1 Using Skillmark (Recommended Starting Point)

```bash
# Install
npm install -g skillmark

# Create test structure for a skill
mkdir -p my-skill/tests

# Define a knowledge test
cat > my-skill/tests/concepts.yaml << 'EOF'
---
name: core-concepts
type: knowledge
concepts:
  - root-cause-analysis
  - hypothesis-testing
  - systematic-approach
timeout: 120
---
# Test Prompt
You encounter a failing test. Describe the debugging approach you would take.
EOF

# Define a task test
cat > my-skill/tests/execution.yaml << 'EOF'
---
name: end-to-end-execution
type: task
tools:
  - Read
  - Grep
  - Bash
timeout: 300
---
# Test Prompt
There is a bug in src/calculator.ts where division by zero returns Infinity
instead of throwing an error. Debug and fix this issue.
EOF

# Run benchmark
skillmark run ./my-skill --model opus --runs 3

# View results
cat skillmark-results/report.md

# Publish to leaderboard (optional)
skillmark publish skillmark-results/result.json --api-key <key>
```

### 3.2 Using Claude Code Skill Benchmarks Methodology

For rigorous documentation quality testing, adopt the treatment-based approach:

```
1. Define treatments:
   - CONTROL: No skill (baseline)
   - CURRENT: Current skill version
   - IMPROVED: Modified skill version

2. Create task suite:
   - 5-10 realistic tasks covering the skill's scope
   - Each task has validation criteria in task.toml

3. Run each treatment × task combination:
   - Execute in isolated Docker environments
   - Record pass/fail, turns, duration

4. Compare treatments:
   - Pass rate improvement over CONTROL
   - Efficiency metrics (turns, duration)
   - Identify documentation changes that improve adherence
```

### 3.3 Custom Local Benchmark Script

For a lightweight approach without external dependencies:

```bash
#!/bin/bash
# benchmark-skill.sh - Quick local skill benchmarking

SKILL_PATH=$1
RESULTS_DIR="benchmark-results/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$RESULTS_DIR"

# Test cases array
declare -A TESTS=(
  ["trigger-detection"]="Does the skill activate for relevant prompts?"
  ["concept-coverage"]="Does the agent demonstrate key concepts?"
  ["happy-path"]="Can the agent complete a standard workflow?"
  ["edge-case"]="Does the agent handle unusual inputs?"
  ["error-recovery"]="Does the agent recover from failures?"
)

for test_name in "${!TESTS[@]}"; do
  echo "Running test: $test_name"
  echo "${TESTS[$test_name]}"
  # Manual evaluation or automated checking
  echo "Result: [PASS/FAIL/PARTIAL]" >> "$RESULTS_DIR/results.txt"
done

echo "Benchmark complete. Results in $RESULTS_DIR/"
```

---

## 4. Best Practices for Skill Quality

### 4.1 Writing Benchmarked Skills (from mgechev/skills-best-practices)

| Practice | Implementation |
|----------|---------------|
| Keep SKILL.md < 500 lines | Move details to references/ |
| Use progressive disclosure | Load supporting files only when needed |
| Write in third-person imperative | "Extract the text..." not "I will extract..." |
| Use consistent terminology | Same term for same concept everywhere |
| Bundle complex operations in scripts/ | Don't make LLM generate repetitive code |
| Provide concrete templates in assets/ | Agents pattern-match well with examples |
| Add error handling to scripts | Scripts should return descriptive error messages |

### 4.2 Four-Stage Validation Process

Based on mgechev/skills-best-practices:

**Stage 1: Discovery Validation**
- Test description in isolation
- Generate prompts that should/shouldn't trigger the skill
- Optimize for discoverability

**Stage 2: Logic Validation**
- Simulate execution step-by-step for realistic use case
- Identify where agent must guess or hallucinate
- Fill gaps in instructions

**Stage 3: Edge Case Testing**
- Script failures (legacy dependencies, missing tools)
- Unsupported configurations
- Missing fallbacks
- Implicit assumptions

**Stage 4: Architecture Refinement**
- Enforce progressive disclosure
- Keep SKILL.md as high-level steps
- Move dense rules to references/
- Add dedicated error handling section

---

## 5. Scoring Framework

### 5.1 Composite Score Calculation

```
Score = (Correctness × 0.40) + (Efficiency × 0.25) + (Discoverability × 0.15) + (Robustness × 0.20)

Where each dimension is scored 0-100:
- Correctness: Pass rate on test suite
- Efficiency: Normalized against baseline (100 = same as baseline, >100 = better)
- Discoverability: Trigger accuracy across prompt variations
- Robustness: Edge case pass rate
```

### 5.2 Score Interpretation

| Score Range | Rating | Action |
|------------|--------|--------|
| 90-100 | Excellent | Production ready |
| 75-89 | Good | Minor improvements needed |
| 60-74 | Adequate | Significant improvements needed |
| 40-59 | Needs Work | Major rewrite recommended |
| 0-39 | Poor | Consider replacing |

---

## 6. Recommended Benchmarking Workflow

```
For each skill in your personal collection:

1. Write test cases (knowledge + task)
2. Run Skillmark locally
3. Record baseline scores
4. Improve skill based on results
5. Re-run and compare
6. Repeat until score > 75

Periodically (monthly):
- Re-benchmark all skills against latest models
- Compare scores with leaderboard
- Retire skills that consistently score < 60
```

---

## 7. Key References

| Resource | URL | Purpose |
|----------|-----|---------|
| SkillsBench | github.com/benchflow-ai/skillsbench | Multi-skill composition benchmarking |
| PinchBench | github.com/pinchbench/skill | Real-world agent task evaluation |
| Skillmark | github.com/claudekit/skillmark | CLI benchmarking with leaderboard |
| LangChain Skill Benchmarks | github.com/langchain-ai/skills-benchmarks | Documentation design impact testing |
| Skills Best Practices | github.com/mgechev/skills-best-practices | Skill writing guidelines |
| SRE-skills-bench | github.com/Rootly-AI-Labs/SRE-skills-bench | Domain-specific SRE benchmarking |
| Performance Benchmark | github.com/openclaw/skills/.../performance-benchmark | Web performance benchmarking skill |
