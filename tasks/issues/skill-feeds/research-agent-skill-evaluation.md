# Deep Research: Agent Skill Evaluation & Top 20 OSS Eval Tools

**Date:** 2026-05-08
**Task:** Task 2 from skill-feeds.md

## Table of Contents

1. [Evaluation Methodologies](#1-evaluation-methodologies)
2. [Evaluation Dimensions & Metrics](#2-evaluation-dimensions--metrics)
3. [How Anthropic Evaluates Agent Skills](#3-how-anthropic-evaluates-agent-skills)
4. [The SKILL.md Evaluation Challenge](#4-the-skillmd-evaluation-challenge)
5. [Major Agent Benchmarks](#5-major-agent-benchmarks)
6. [Top 23 OSS Eval Projects](#6-top-23-oss-eval-projects)
7. [Skill-Specific Benchmarking Tools](#7-skill-specific-benchmarking-tools)
8. [Comparison: Eval Frameworks vs Benchmarks](#8-comparison-eval-frameworks-vs-benchmarks)
9. [Open Problems](#9-open-problems)
10. [Sources](#10-sources)

---

## 1. Evaluation Methodologies

### 1.1 Core Concepts

An evaluation ("eval") is a test for an AI system: provide an input, apply grading logic to the output, and measure success. For agents, evals extend beyond single-turn responses to cover multi-turn interactions involving tool calls, environment state changes, and adaptive reasoning.

**Key structural elements (Anthropic definition):**

| Concept | Definition |
|---------|-----------|
| **Task** (test case) | A single test with defined inputs and success criteria |
| **Trial** | Each attempt at a task (multiple trials needed because outputs vary) |
| **Grader** | Logic that scores some aspect of performance |
| **Transcript** (trace/trajectory) | Complete record — outputs, tool calls, reasoning, intermediate results |
| **Outcome** | Final environment state at end of trial |
| **Evaluation harness** | Infrastructure that runs evals end-to-end |
| **Evaluation suite** | Collection of tasks measuring specific capabilities |

### 1.2 Trajectory Evaluation

Assesses whether the agent took the right steps in the right order:

- **Ordered trajectory matching** — Tools called in specific sequence
- **Unordered trajectory matching** — Correct set of tools invoked regardless of sequence (more flexible)
- **Step-by-step logical progression** — Each step follows from the previous
- **Tool call verification** — Which tools, with what parameters, outputs correctly interpreted

**Anthropic guidance:** Grade what the agent produced, not the path it took. Rigid step-by-step checks tend to be brittle because frontier models frequently find valid approaches that eval designers did not anticipate.

### 1.3 Goal/Outcome Evaluation

Focuses on the final state — did the agent achieve the objective?

- **State-based verification** — Check the environment's actual state (e.g., does a database record exist?)
- **Test suite execution** — For coding agents, do the unit tests pass?
- **Binary pass/fail** — Did the agent accomplish the task or not?
- **Partial credit** — Grade each component independently for multi-component tasks

### 1.4 Efficiency Evaluation

Measures the cost of achieving the goal:

- **Token usage** — Input/output tokens consumed
- **Number of turns/steps** — Interaction rounds needed
- **Number of tool calls** — Total invocations (detecting overuse or underuse)
- **Latency** — Time to first token, total time to completion
- **Cost per task** — Token usage × pricing
- **Cost vs. quality tradeoff** — Is additional cost justified by quality improvements?

### 1.5 Robustness Evaluation

Measures how the agent handles edge cases and adversarial inputs:

- **Multi-trial consistency** — Run same task multiple times, measure variance
- **pass@k** — Probability of at least one success in k attempts
- **pass^k** — Probability that all k trials succeed (essential for customer-facing agents)
- **Edge case coverage** — Test boundary conditions explicitly
- **Adversarial inputs** — Red teaming to find failure modes

### 1.6 Safety Evaluation

Checks whether the agent avoids harmful actions:

- **Attack Success Rate (ASR)** — Percentage of adversarial prompts eliciting harmful behavior
- **Red teaming benchmarks** — MCP-SafetyBench, HarmBench, DREAM
- **Security benchmarks** — CVE-Bench, SEC-bench, Agent Security Bench (ASB)
- **Skill security auditing** — SkillProbe for auditing skill marketplaces

---

## 2. Evaluation Dimensions & Metrics

### 2.1 Quality Metrics

| Metric | Description | Common Tools |
|--------|-------------|--------------|
| Accuracy/Correctness | Factual accuracy of outputs | Exact match, LLM-as-judge |
| Faithfulness | Output grounded in retrieved context | RAGAS Faithfulness, TruLens |
| Hallucination Rate | Frequency of fabricated content | HaluEval, custom LLM judges |
| Refusal Rate | Percentage of prompts declined | Promptfoo, custom monitoring |
| Context Adherence | Responses stay within provided context | RAGAS, Arize Phoenix |
| Instruction Following | Model follows formatting/style/task instructions | IFEval, AlpacaEval, MT-Bench |
| Answer Relevancy | Response relevance to user query | RAGAS Answer Relevance |

### 2.2 Tool Use Metrics

| Metric | Description |
|--------|-------------|
| Tool Selection Accuracy | Did the agent pick the right tool? |
| Tool Call Success Rate | How often do invocations succeed? |
| Parameter Correctness | Were arguments passed correctly? |
| Tool Usage Frequency | Detecting overuse or underuse |
| Output Interpretation | Did agent correctly interpret tool outputs? |

### 2.3 Task Performance Metrics

| Metric | Description |
|--------|-------------|
| Task Completion Rate | Percentage of tasks successfully completed |
| Success Rate (pass@k, pass^k) | Probabilistic success across multiple trials |
| Partial Completion | Multi-component scoring for complex tasks |
| Time to Completion | End-to-end latency |
| First-Try Success Rate (pass@1) | Success on first attempt |

### 2.4 Efficiency Metrics

| Metric | Description |
|--------|-------------|
| Total Token Usage | Input + output tokens consumed |
| Number of Turns | Interaction rounds |
| Number of Tool Calls | Total invocations |
| Cost per Task | Economic cost |
| Time to First Token | Latency before first response |
| Output Tokens per Second | Generation speed |

---

## 3. How Anthropic Evaluates Agent Skills

### 3.1 Evaluation Philosophy: "Start with Evaluation"

1. Identify specific gaps in agent capabilities by running representative tasks
2. Observe where the agent struggles or requires additional context
3. Build skills incrementally to address shortcomings
4. Iterate based on observations of how the agent uses the skill in real scenarios

### 3.2 Skill-Creator 2.0 Evaluation Tooling (March 2026)

Anthropic's skill-creator now includes dedicated evaluation capabilities:

| Feature | Description |
|---------|-------------|
| **Eval writing** | Define test prompts, describe what "good" looks like, run tests |
| **Benchmark mode** | Standardized assessment tracking eval pass rate, elapsed time, token usage |
| **Multi-agent parallel evals** | Independent agents run evals in parallel with clean contexts |
| **Comparator agents (A/B testing)** | Two skill versions or skill vs. no skill, judged blind |
| **Description optimization** | Analyzes descriptions against sample prompts to reduce false positives/negatives |
| **Regression detection** | Run evals against new models to catch quality shifts |
| **Capability obsolescence detection** | Detects when base model passes evals without the skill loaded |

### 3.3 Grader Types

| Type | Examples | Characteristics |
|------|----------|-----------------|
| **Code-based** | String match, regex, binary tests, static analysis, outcome verification | Fast, cheap, objective, reproducible |
| **Model-based** | Rubric scoring, NL assertions, pairwise comparison, reference-based evaluation | Flexible, scalable, captures nuance |
| **Human** | SME review, crowdsourced judgment, spot-check sampling | Gold standard but expensive and slow |

### 3.4 Two Types of Skills

- **Capability uplift** — Help the model do something it cannot do consistently. May become unnecessary as models improve.
- **Encoded preference** — Document workflows the model can already do, but sequenced per team process. More durable.

### 3.5 Anthropic's Practical Evaluation Workflow

1. **Start with evaluation** — Identify where the agent fails before building the skill
2. **Build incrementally** — Add instructions, scripts, resources piece by piece
3. **Monitor real usage** — Watch how Claude uses the skill in real scenarios
4. **Iterate based on observations** — Pay attention to unexpected trajectories
5. **Tune the description** — Name and description control trigger accuracy (most critical evaluation point)
6. **Use A/B comparison** — Compare skill vs. no-skill, old vs. new version
7. **Check for obsolescence** — Run evals with and without the skill
8. **Run regression tests** — After model updates, verify skills still work

---

## 4. The SKILL.md Evaluation Challenge

### 4.1 Three-Dimensional Skill Evaluation Model

**Dimension 1: Trigger Accuracy** — Does the agent activate the skill at the right time?
- **False positives** — Skill triggers when it should not
- **False negatives** — Skill does not trigger when it should
- **Description precision** — The YAML frontmatter `name` and `description` control trigger decisions
- Anthropic's skill-creator now analyzes descriptions against sample prompts to reduce both false positives and negatives

**Dimension 2: Workflow Correctness (Instruction Adherence)** — Does the agent follow the skill's instructions?
- Does it load the full SKILL.md when triggered?
- Does it follow procedural instructions in the correct order?
- Does it use referenced files (progressive disclosure) appropriately?
- Does it execute bundled scripts when indicated?
- Does it respect guardrails and constraints?

**Dimension 3: Output Quality (Skill Utility)** — Does the skill improve agent performance vs. no skill?
- **A/B comparison** — Same task with and without skill loaded
- **Comparator agents** — Blind evaluation
- **Benchmark mode** — Standardized assessment
- **Skill vs. base model** — Does the base model already pass without the skill?

### 4.2 SkillTester: Academic Framework

SkillTester (arXiv: 2603.28815) evaluates two dimensions:

**Utility Evaluation:**
- Paired baseline comparisons (skill vs. no-skill)
- Systematically assesses how well skills perform on practical tasks
- Measures improvement across diverse task types

**Security Evaluation:**
- Assesses whether skills introduce safety/security risks
- Tests for malicious behavior in third-party skills
- Part of ecosystem including SkillsBench (86 tasks, 11 domains), SkillProbe (security auditing), CVE-Bench

### 4.3 Skill Coverage and Generalization

- Test across the full range of intended use cases
- Include edge cases and boundary conditions
- Test with different phrasings of the same request
- Verify the skill does not activate for unrelated tasks
- Regular regression testing against model updates

### 4.4 Agent Skill Audit

[agentskillreport.com](https://agentskillreport.com/) conducted a systematic audit of 673 agent skills across 41 repositories, evaluating validation results, content quality scores, contamination risk, and behavioral analysis.

---

## 5. Major Agent Benchmarks

| Benchmark | Domain | Key Metric | Notable Details |
|-----------|--------|-----------|-----------------|
| **SWE-bench Verified** | Software Engineering | % GitHub issues resolved | Gold standard for coding agents |
| **Terminal-Bench** | End-to-end technical tasks | % tasks completed | Real tasks (building kernels, training ML) |
| **WebArena** | Web Navigation | % success rate | Browser-based tasks |
| **GAIA** | General AI Assistant | % correct answers | Multi-modal, multi-step reasoning |
| **AgentBench** | Multi-domain | Composite score | Multi-environment benchmark |
| **OSWorld** | Desktop OS | % task completion | Full OS-level GUI interaction |
| **tau-bench** | Conversational agents | Multi-dimensional scoring | Multi-turn with simulated user |
| **BrowseComp** | Research/Web search | % correct answers | Finding needles in haystacks |
| **CORE-Bench** | Research replication | % tasks correct | Academic research completion |

**Critical caveat:** UC Berkeley RDI audited eight major benchmarks and found an automated agent could achieve near-perfect scores without solving a single task — exposing data contamination and gaming vulnerabilities.

---

## 6. Top 23 OSS Eval Projects

### Category 1: Agent Evaluation Frameworks

| # | Project | Stars | Language | Evaluates |
|---|---------|-------|----------|-----------|
| 1 | [promptfoo](https://github.com/promptfoo/promptfoo) | ~21K | TypeScript | Prompts, agents, RAG; red teaming. Declariptive config, CI/CD, custom assertions, browser viewer. Used by OpenAI and Anthropic. |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | ~15.2K | Python | 14+ built-in metrics (hallucination, faithfulness, etc.). Pytest-based interface. LLM-as-Judge. |
| 3 | [Langfuse](https://github.com/langfuse/langfuse) | ~26.8K | TypeScript | LLM observability, tracing, prompt management, dataset-driven evals. Self-hostable. |
| 4 | [Arize Phoenix](https://github.com/Arize-ai/phoenix) | ~9.6K | Python | AI observability, LLM tracing, experiment evaluation. OpenTelemetry-based. |
| 5 | [MLflow](https://github.com/mlflow/mlflow) | ~25.8K | Python | End-to-end ML/AI lifecycle with native LLM eval. Prompt engineering UI, experiment tracking. |
| 6 | [agentevals](https://github.com/agentevals-dev/agentevals) | ~123 | Python | Framework-agnostic agent eval from OTel traces — no re-runs needed. Scores reasoning, tool use, latency. |
| 7 | [AWS agent-evaluation](https://github.com/awslabs/agent-evaluation) | ~360 | Python | LLM agent as evaluator to systematically test virtual agent behavior. |
| 8 | [LangChain agentevals](https://github.com/langchain-ai/agentevals) | ~575 | Python | Agent trajectory evaluation — tool call superset/subset checks, trajectory similarity scoring. |

### Category 2: LLM/Prompt Evaluation

| # | Project | Stars | Language | Evaluates |
|---|---------|-------|----------|-----------|
| 9 | [OpenAI Evals](https://github.com/openai/evals) | ~18.4K | Python | LLM output quality, safety, capabilities. Custom benchmarks with scoring. |
| 10 | [OpenAI Simple-Evals](https://github.com/openai/simple-evals) | ~4.5K | Python | Lightweight model accuracy benchmarking (MMLU, HumanEval, MATH). |
| 11 | [RAGAS](https://github.com/explodinggradients/ragas) | ~13.8K | Python | RAG pipeline eval — faithfulness, context precision/recall, answer relevance. |
| 12 | [Anthropic Evals](https://github.com/anthropics/evals) | ~380 | Mixed | Official Anthropic eval templates for model behavior and safety. |

### Category 3: Skill & Task Benchmarks

| # | Project | Stars | Language | Evaluates |
|---|---------|-------|----------|-----------|
| 13 | [SWE-bench](https://github.com/swe-bench/SWE-bench) | ~4.9K | Python | AI agents solving real GitHub issues. Gold standard coding benchmark. |
| 14 | [AgentBench](https://github.com/THUDM/AgentBench) | ~3.4K | Python | Multi-environment agent eval (OS, web, DB, games). ICLR 2024. |
| 15 | [WebArena](https://github.com/web-arena-x/webarena) | ~1.5K | Python | Autonomous web agents — navigation, forms, information retrieval. |
| 16 | [ToolBench](https://github.com/OpenBMB/ToolBench) | ~5.6K | Python | LLM tool use with 16,000+ real APIs. ICLR 2024 spotlight. |
| 17 | [OpenHands](https://github.com/OpenHands/OpenHands) | ~72.9K | Python | AI-driven software development + SWE-bench evaluation. CodeAct Agent. |

### Category 4: Agent Trajectory & Specialized Evaluation

| # | Project | Stars | Language | Evaluates |
|---|---------|-------|----------|-----------|
| 18 | [AgentBoard](https://github.com/hkust-nlp/AgentBoard) | ~413 | Python | Multi-turn agent trajectory analysis. Progress rate beyond final success. NeurIPS 2024 oral. |
| 19 | [T-Eval](https://github.com/open-compass/T-Eval) | ~306 | Python | Step-by-step tool use decomposition: instruction following, planning, tool selection, parameter extraction. ACL 2024. |
| 20 | [tau-bench](https://github.com/sierra-research/tau-bench) | ~1.2K | Python | Multi-turn tool use dialog eval. Simulated user interacts with agent. |
| 21 | [MLE-bench](https://github.com/openai/mle-bench) | ~1.5K | Python | 75 Kaggle competitions as eval tasks for ML engineering agents. |
| 22 | [MLAgentBench](https://github.com/snap-stanford/MLAgentBench) | ~338 | Python | 13 ML experiment tasks. Benchmarks GPT-4, Claude, Gemini. ICML 2024. |
| 23 | [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) | ~697 | Python | Agents in simulated software company — Git, code review, travel booking. |

---

## 7. Skill-Specific Benchmarking Tools

### Skillmark
- **What:** CLI-based agent skill benchmarking platform with public leaderboard
- **Repo:** [github.com/claudekit/skillmark](https://github.com/claudekit/skillmark)
- **Website:** [skillmark.sh](https://skillmark.sh/)
- **Install:** `npm install -g skillmark` or `npx skillmark run <skill-path>`
- **How it works:**
  - Accepts local paths, Git repos, or skills.sh references
  - Claude-based engine runs tests defined as Markdown + YAML frontmatter
  - Two test types: **knowledge** (Q&A concept coverage) and **task** (execution tests)
  - Metrics: accuracy, tokens_total, duration_ms, tool_count, cost_usd
  - Results upload to Cloudflare Workers + D1 leaderboard
- **Sample leaderboard scores:** context-engineering (16.3% composite), skill-creator (9.2%), code-review (7.6%) — indicating rigorous benchmarks
- **License:** MIT

### SkillsBench
- **What:** First academic benchmark for evaluating how AI agents leverage modular Skills
- **Repo:** [github.com/benchflow-ai/skillsbench](https://github.com/benchflow-ai/skillsbench)
- **Website:** [skillsbench.ai](https://skillsbench.ai/)
- **Paper:** [arxiv.org/abs/2602.12670](https://arxiv.org/abs/2602.12670)
- **How it works:**
  - Gym-style benchmarking on the Harbor framework (containerized eval environment)
  - **86 tasks across 11 domains** (healthcare, SWE, research, etc.)
  - Each task tested under 3 conditions: no skill, with curated skill, with self-generated skill
  - Tests skill composition (2+ skills working together)
  - Deterministic verifiers + LLM-based evaluation
- **Key findings:** Curated skills improve performance by +16.2 percentage points on average; healthcare +51.9pp
- **Quick start:**
  ```bash
  uv tool install harbor
  git clone https://github.com/benchflow-ai/skillsbench.git
  harbor tasks init "<task-name>"
  harbor run -p tasks/<task-id> -a oracle
  ```
- **License:** Apache 2.0

### PinchBench
- **What:** Benchmarking system for evaluating LLMs as the "brain" of OpenClaw coding agents
- **Repo:** [github.com/pinchbench/skill](https://github.com/pinchbench/skill)
- **Website:** [pinchbench.com](https://pinchbench.com/)
- **Developed by:** Kilo.ai team (Rust-based)
- **What it tests:** 53 real-world tasks across 8 categories:
  | Category | Tasks |
  |----------|-------|
  | Productivity | Calendar, daily summaries |
  | Research | Stock prices, conferences, markets |
  | Writing | Blog posts, emails |
  | Coding | Weather scripts, file structures |
  | Analysis | Spreadsheets, PDFs, documents |
  | Email | Triage, search |
  | Memory | Context retrieval, knowledge management |
  | Skills | ClawHub, skill discovery |
- **Key distinction:** Benchmarks models as agent brains, not individual skill files
- **Tested:** 100+ LLMs, 50 models, 403+ run records
- **License:** MIT

### LangChain Skill Benchmarks
- **What:** Treatment-based framework testing how skill documentation design impacts agent adherence
- **Repo:** [github.com/langchain-ai/skills-benchmarks](https://github.com/langchain-ai/skills-benchmarks)
- **Metrics:** Pass rate, turns, duration, artifact quality

### SkillProbe
- **What:** Security auditing tool for agent skill marketplaces
- **Paper:** [arxiv.org/html/2603.21019v1](https://arxiv.org/html/2603.21019v1)
- **Focus:** Detects malicious behavior in third-party skills

### SkillMarket.ai
- **What:** Community-driven platform for AI skill rankings and reviews
- **Website:** [skillmarket.ai](https://skillmarket.ai/)
- **Features:** Independent benchmarks, user reviews, side-by-side comparisons

### Comparison Table

| Tool | Focus | Best For |
|------|-------|----------|
| **Skillmark** | Individual SKILL.md benchmarking | Quick local validation with leaderboard |
| **SkillsBench** | Skill augmentation efficacy (academic) | Measuring how skills improve agent performance |
| **PinchBench** | Model-as-agent-brain evaluation | Comparing LLMs on real-world coding tasks |
| **LangChain Skill Benchmarks** | Documentation quality impact | Testing how skill docs affect agent adherence |
| **SkillProbe** | Security auditing | Detecting malicious skills |
| **SkillMarket.ai** | Community rankings | User reviews and comparisons |

---

## 8. Comparison: Eval Frameworks vs Benchmarks

### Frameworks (tools to run your own evals)

| Framework | Language | Key Strength |
|-----------|----------|-------------|
| promptfoo | TypeScript | Most versatile; red teaming + custom assertions + CI/CD |
| DeepEval | Python | 14+ metrics out of the box; Pytest integration |
| Langfuse | TypeScript | Full observability platform; self-hostable |
| MLflow | Python | End-to-end ML lifecycle; enterprise-grade |
| Arize Phoenix | Python | Real-time observability; notebook-based UI |
| agentevals | Python | OTel-native; no re-runs needed |

### Benchmarks (fixed test suites to score against)

| Benchmark | Domain | Key Strength |
|-----------|--------|-------------|
| SWE-bench | Coding | Gold standard for software engineering agents |
| SkillsBench | Skills | Only benchmark specifically for skill utility |
| ToolBench | Tool use | Largest tool/API evaluation (16K+ APIs) |
| WebArena | Web | Realistic web navigation tasks |
| tau-bench | Conversational | Multi-turn tool use with simulated users |
| AgentBench | Multi-domain | Broadest environment coverage |

### For SKILL.md Evaluation Specifically

| Priority | Tool | Why |
|----------|------|-----|
| **1st** | Skillmark | Purpose-built for SKILL.md benchmarking with leaderboard |
| **2nd** | SkillsBench | Academic rigor, 86 tasks, skill vs. no-skill comparison |
| **3rd** | Promptfoo | Most flexible framework; custom assertions for trigger accuracy, workflow correctness, output quality |
| **4th** | DeepEval | 14+ metrics, hallucination/faithfulness detection for skill output |
| **5th** | LangChain Skill Benchmarks | Tests documentation quality impact on agent adherence |

---

## 9. Open Problems

1. **Benchmark contamination** — Many popular benchmarks are vulnerable to gaming and data contamination (Berkeley RDI audit)
2. **Non-determinism** — Agent behavior varies between runs, requiring statistical approaches (pass@k, pass^k)
3. **Creative solutions vs. eval rigidity** — Frontier models can find solutions that surpass static evals but get penalized
4. **Evaluation cost** — Comprehensive agent evals are expensive in compute, tokens, and time
5. **Subjective quality** — For research and conversational agents, "correctness" is inherently subjective
6. **Multi-agent evaluation** — Evaluating agents that coordinate with other agents adds combinatorial complexity
7. **Skill obsolescence** — As models improve, capability uplift skills may become unnecessary

---

## 10. Sources

### Official Documentation
- [Demystifying evals for AI agents — Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Equipping agents for the real world with Agent Skills — Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Improving skill-creator — Claude Blog](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)
- [Evaluate Agent Workflows — OpenAI](https://developers.openai.com/api/docs/guides/agent-evals)
- [Testing Agent Skills Systematically — OpenAI](https://developers.openai.com/blog/eval-skills)
- [Microsoft Foundry Agent Evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators)
- [Google Cloud: Agent Evaluation](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation)

### OSS Projects
- [promptfoo](https://github.com/promptfoo/promptfoo)
- [DeepEval](https://github.com/confident-ai/deepeval)
- [Langfuse](https://github.com/langfuse/langfuse)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix)
- [MLflow](https://github.com/mlflow/mlflow)
- [OpenAI Evals](https://github.com/openai/evals)
- [RAGAS](https://github.com/explodinggradients/ragas)
- [SWE-bench](https://github.com/swe-bench/SWE-bench)
- [AgentBench](https://github.com/THUDM/AgentBench)
- [WebArena](https://github.com/web-arena-x/webarena)
- [ToolBench](https://github.com/OpenBMB/ToolBench)
- [OpenHands](https://github.com/OpenHands/OpenHands)
- [tau-bench](https://github.com/sierra-research/tau-bench)
- [MLE-bench](https://github.com/openai/mle-bench)
- [agentevals](https://github.com/agentevals-dev/agentevals)
- [LangChain agentevals](https://github.com/langchain-ai/agentevals)
- [AgentBoard](https://github.com/hkust-nlp/AgentBoard)
- [T-Eval](https://github.com/open-compass/T-Eval)
- [MLAgentBench](https://github.com/snap-stanford/MLAgentBench)
- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany)
- [Anthropic Evals](https://github.com/anthropics/evals)

### Skill-Specific Tools
- [Skillmark](https://github.com/claudekit/skillmark) — [skillmark.sh](https://skillmark.sh/)
- [SkillsBench](https://github.com/benchflow-ai/skillsbench) — [skillsbench.ai](https://skillsbench.ai/)
- [PinchBench](https://github.com/pinchbench/skill) — [pinchbench.com](https://pinchbench.com/)
- [LangChain Skill Benchmarks](https://github.com/langchain-ai/skills-benchmarks)
- [SkillMarket.ai](https://skillmarket.ai/)
- [Agent Skill Audit](https://agentskillreport.com/)

### Academic Papers
- [SkillTester: Benchmarking Utility and Security of Agent Skills](https://arxiv.org/html/2603.28815v1)
- [SkillsBench](https://arxiv.org/abs/2602.12670)
- [SkillProbe](https://arxiv.org/html/2603.21019v1)
- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/html/2507.21504v1)
- [MCP-SafetyBench](https://arxiv.org/html/2512.15163v2)
- [CUBE: A Standard for Unifying Agent Benchmarks](https://arxiv.org/pdf/2603.15798)

### Industry Articles
- [AI Agent Evaluation — IBM](https://www.ibm.com/think/topics/ai-agent-evaluation)
- [AI Agent Evaluation — Databricks](https://www.databricks.com/blog/what-is-agent-evaluation)
- [AWS: Evaluating AI Agents](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [Galileo: CLEAR Framework](https://galileo.ai/blog/ai-agent-evaluation)
- [Braintrust: Agent Evaluation Framework](https://www.braintrust.dev/articles/ai-agent-evaluation-framework)
- [Berkeley RDI Benchmark Audit](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)
- [LangSmith Trajectory Evals](https://docs.langchain.com/langsmith/trajectory-evals)
- [Arize Agent Trajectory Evaluations](https://arize.com/docs/ax/evaluate/evaluators/trace-and-session-evals/trace-level-evaluations/agent-trajectory-evaluations)
