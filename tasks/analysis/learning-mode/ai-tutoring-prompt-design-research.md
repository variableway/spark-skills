# AI Tutoring Prompt Design & Bot Dialogue Skills -- Research Report

## Overview

This report synthesizes findings from 15+ GitHub repositories and research papers on AI tutoring prompt design, bot dialogue skills for education, and multi-agent vs single-agent learning effectiveness. Research was conducted via web search and direct repository analysis.

---

## Topic 1: AI Tutoring Prompt Design & Bot Dialogue Skills

### 1. feynman-tutor (koukekoukej-glitch)

- **URL**: https://github.com/koukekoukej-glitch/feynman-tutor
- **Stars**: 13
- **What it is**: The most sophisticated Claude Code AI tutoring skill found. Implements the Feynman Technique with Zone of Proximal Development (ZPD) theory. A persistent cognitive system that tracks learner state.

**Prompt/Skill Patterns for Dialogue Design:**
- **Role-reversal learning**: User teaches the AI (Feynman technique), AI identifies gaps
- **Persistent cognitive system**: Three-layer knowledge architecture:
  - `INDEX.md` -- topic registry and learning status
  - `LEARNER.md` -- learner model (level, pace, goals, preferences)
  - `GRAPH.md` -- concept dependency graph (prerequisite relationships)
- **Tiered diagnostic feedback**:
  - Red (Critical misconception): Directly contradicts source material
  - Yellow (Incomplete understanding): Correct direction but missing key aspects
  - Green (Could be phrased better): Essentially correct, suggest refinements
- **Dynamic calibration table**: Maps user engagement signals to tutor responses

**Principles for HOW the bot should converse:**
1. **Pedagogy-driven, not feature-driven**: Every interaction serves a learning outcome
2. **Stateful, not stateless**: Maintains cognitive map across sessions
3. **Materials are input, not authority**: Source materials inform but don't constrain
4. **Flexible flow, not rigid pipeline**: Tutor adapts to learner's natural curiosity
5. **In your own words**: Forces learner to articulate, never accepts copy-paste

**Multi-source material extraction pipeline:**
- YouTube transcripts, Bilibili, PDF, web pages, Wikipedia, arXiv
- Auto-generates concept graph from extracted materials

---

### 2. deeptutor-claude-skill (ndpvt-web)

- **URL**: https://github.com/ndpvt-web/deeptutor-claude-skill
- **Stars**: 8
- **What it is**: Adapts HKUDS/DeepTutor's graph-enhanced RAG methodology into a Claude Code skill. Lightweight (~27KB, 1 pip dependency: networkx). Claims to deliver 70% of DeepTutor's value.

**Prompt/Skill Patterns for Dialogue Design:**
- **Dual-loop problem solving**:
  - Analysis Loop: Decompose problem, retrieve relevant knowledge from graph
  - Solve Loop: Apply retrieved knowledge, verify answer, cite sources
- **Graph-enhanced RAG**: Knowledge stored as NetworkX graph, not flat text
- **Difficulty-calibrated questions**: Questions generated based on learner's assessed level
- **Citation-driven answering**: Every answer references specific source material

**Workflows defined:**
1. Initialize Knowledge Base (from documents)
2. Dual-Loop Solve (analysis + solve)
3. Generate Questions (adaptive difficulty)
4. Deep Research (multi-source gathering)
5. Guided Learning (step-by-step tutoring)
6. KB Management (update, query, visualize graph)

**Key dialogue principle**: "Answer with evidence, not just words. Every claim must trace back to a source node in the knowledge graph."

---

### 3. school-skills (Jellypod-Inc)

- **URL**: https://github.com/Jellypod-Inc/school-skills
- **Stars**: 0
- **What it is**: Classroom-ready Claude Code skill bundle for education. Installable via `/plugin marketplace add Jellypod-Inc/school-skills`.

**Skills included:**
| Skill | Purpose |
|-------|---------|
| socratic-tutor | Socratic questioning-based teaching |
| lesson-plan | Generate structured lesson plans |
| circle-time | Group discussion facilitation |
| rubric | Assessment criteria generation |
| arts-crafts | Creative project guidance |
| lecture-to-study-guide | Convert lectures to study materials |
| concept-map | Visual concept relationship mapping |

**Dialogue principle**: Each skill defines its own conversational contract. The socratic-tutor skill explicitly prevents the AI from giving direct answers, forcing a question-based dialogue pattern.

---

### 4. python-tutor-skill (egouilliard-leyton)

- **URL**: https://github.com/egouilliard-leyton/python-tutor-skill
- **Stars**: 1
- **What it is**: A Claude Code skill that teaches Python to absolute beginners through real `.py` files, Socratic feedback, and persistent memory. 25 exercises, 5 projects, adaptive difficulty.

**Prompt/Skill Patterns for Dialogue Design:**
- **4-level graduated hints** (vague to specific):
  1. Level 1: Directional hint ("Think about what type of loop would work here")
  2. Level 2: Conceptual hint ("A while loop checks a condition before each iteration")
  3. Level 3: Structural hint ("Try: while x > 0: ...")
  4. Level 4: Near-solution (only after 3+ failures)
- **Socratic feedback**: Never gives the answer; asks "what do you think went wrong?"
- **Error translation**: Converts Python tracebacks to plain language, then asks learner to diagnose
- **Attempt tracking**: Full snapshot per attempt (code, test results, error types, hints used)

**Principles for HOW the bot should converse:**

| Principle | Implementation |
|-----------|---------------|
| Never give the answer | 4-level graduated hints; full explanation only after 3+ failures |
| Real developer workflow | Real .py files in VS Code/Cursor, not a chat window |
| One concept at a time | Each lesson teaches exactly ONE thing |
| Errors are teachers | Translate tracebacks to plain language, then ask "what do you think?" |
| Tests check behavior, not style | `if age >= 18` and `if 18 <= age` both pass |
| Memory across sessions | Progress, struggles, streaks all persisted in JSON |
| Never ask twice | Environment, preferences, setup checked once, stored forever |

**Design patterns worth adopting:**
- `teaching_guide.md` per exercise: Defines the Socratic script Claude follows
- Comfort scores (0-100) per concept for adaptive difficulty
- Spaced repetition: Concepts decay over time, auto-reviewed
- Gamification: XP, levels (Novice to Expert), achievements, streaks

---

### 5. ostep-socratic-tutor (lmonkt)

- **URL**: https://github.com/lmonkt/ostep-socratic-tutor
- **Stars**: 7
- **What it is**: Chinese-language Socratic tutoring system for the OSTEP (Operating Systems) textbook. Provides core prompts (main branch) and full implementation with automation scripts (demo-full branch).

**Prompt/Skill Patterns:**
- **Document-based Socratic tutoring**: Converts PDF textbook to markdown, then uses Socratic method to teach chapter by chapter
- **Bootstrap prompt**: The prompt.md itself is a meta-prompt that instructs Claude to analyze two reference articles and build the tutoring system from scratch
- **Automated material pipeline**: Uses pymupdf4llm for PDF-to-markdown conversion

**Dialogue principle**: Question-driven, never directly gives answers. Based on two Chinese-language articles about building Socratic AI tutor systems.

---

### 6. Intuitive ML Architect (rgrohitgupta938)

- **URL**: https://github.com/rgrohitgupta938/Intuitive_ML_Architect
- **Stars**: 1
- **What it is**: A stateful, prompt-driven AI tutor for ML & Math. Built with Next.js 14, LangGraph, and MongoDB. Submission for Prompt Wars hackathon.

**Prompt/Skill Patterns:**
- **Three-level mastery path**:
  1. Intuition (Analogy) -- "Explain like I'm 12"
  2. Theory (Mathematics) -- Formal mathematical treatment
  3. Implementation (Code) -- Working code examples
- **Verification Gate**: System prompt enforces that the AI will NOT reveal code until the user demonstrates understanding of the underlying math
- **Stateful learning roadmap**: LangGraph maintains state across sessions; persistent learning path stored in MongoDB
- **Dynamic SOTA integration**: Google Search API fetches latest ArXiv papers

**Key dialogue principle**: "The assistant will not reveal code until the user demonstrates an understanding of the underlying math." -- This is a hard gate in the system prompt.

---

### 7. Multi-Agent Study Assistant (A-R007)

- **URL**: https://github.com/A-R007/Multi-Agent-Study-Assistant
- **Stars**: 23
- **What it is**: AI-powered learning platform with 6 specialized agents. Built with Phidata, Streamlit, and LangChain.

**Agent Architecture:**
| Agent | Role |
|-------|------|
| Student Analyzer | Assesses needs, identifies gaps, recommends approaches |
| Roadmap Creator | Designs personalized learning paths with phases and milestones |
| Quiz Generator | Creates adaptive assessments with explanations |
| Tutor | Provides explanations and answers questions |
| Resource Finder | Searches and recommends learning materials |
| RAG Tutor | Answers questions using uploaded study documents |

**Dialogue principle**: Learning style adaptation (Visual, Auditory, Kinesthetic, Reading/Writing). Each agent adapts its output format and explanation style based on detected learner preference.

**Key design pattern**: `prompts.yaml` defines agent personas and prompt templates separately from code, allowing easy prompt iteration.

---

### 8. GenMentor (GeminiLight)

- **URL**: https://github.com/GeminiLight/gen-mentor
- **Stars**: 66
- **What it is**: WWW 2025 Oral paper: "LLM-powered Multi-agent Framework for Goal-oriented Learning in ITS". Full-stack with FastAPI backend + Streamlit frontend.

**5 Specialized Agent Modules:**
1. **Skill Gap Identifier**: Analyzes learner's current state vs. desired state
2. **Adaptive Learner Modeler**: Builds and updates learner profile
3. **Learning Path Scheduler**: Plans optimal learning sequence
4. **Tailored Content Generator**: Creates personalized learning materials
5. **AI Chatbot Tutor**: Conducts the actual tutoring dialogue

**Paradigm Comparison:**
| Paradigm | Approach | Limitation |
|----------|----------|-----------|
| Traditional MOOC | Fixed content, passive learner | No personalization |
| Chatbot ITS | Reactive Q&A | No goal orientation |
| Goal-oriented ITS (GenMentor) | Proactive, adaptive, goal-driven | Higher complexity |

**Dialogue principle**: Goal-oriented learning -- every interaction must serve a defined learning goal, not just answer questions reactively.

---

### 9. Additional Repositories Found

| Repo | Stars | Key Pattern |
|------|-------|-------------|
| [BeArGpT76/socratic-ai-prompt](https://github.com/BeArGpT76/socratic-ai-prompt) | 1 | Universal prompt to transform any AI into a Socratic tutor |
| [adisagar2003/Junior-dev-tutor-claude-skill](https://github.com/adisagar2003/Junior-dev-tutor-claude-skill) | 1 | Claude system prompt forcing AI to teach, not just fix code |
| [user39261580/leetcode-tutor-prompt](https://github.com/user39261580/leetcode-tutor-prompt) | 0 | Socratic system prompt specifically for LeetCode tutoring |
| [Man0dya/Multi-Agent-AI-Tutoring-System](https://github.com/Man0dya/Multi-Agent-AI-Tutoring-System) | 12 | Multi-agent tutoring with specialized roles |
| [zexiJia/Ascend-Flow](https://github.com/zexiJia/Ascend-Flow) | 11 | Multi-agent adaptive learning system |
| [JaiSuryaPrabu/skillix-ai-agent](https://github.com/JaiSuryaPrabu/skillix-ai-agent) | 6 | Self-evolving multi-agent tutoring |

---

## Topic 2: Bot/Skill Repos with Well-Designed Learning Dialogues

### Key Design Patterns Across All Repos

#### Pattern 1: The Socratic Gate
Used by: python-tutor-skill, ostep-socratic-tutor, school-skills, feynman-tutor

The bot is explicitly instructed to NEVER give the answer directly. Instead, it must:
1. Ask a guiding question
2. Wait for learner response
3. Evaluate response accuracy
4. Either confirm or ask a deeper question

```
Anti-pattern: "The answer is X because Y."
Socratic pattern: "That's close! What do you think happens when X meets Y?"
```

#### Pattern 2: Graduated Hint Escalation
Used by: python-tutor-skill, feynman-tutor

Hints progress through levels of specificity:
- Level 1: Conceptual direction
- Level 2: Specific concept
- Level 3: Structural hint
- Level 4: Near-complete solution (only after repeated failure)

#### Pattern 3: Teach-Back Verification
Used by: feynman-tutor, Intuitive ML Architect

The learner must explain the concept back in their own words. The AI evaluates:
- Accuracy (is it correct?)
- Completeness (are key aspects missing?)
- Depth (is it surface-level or deep understanding?)

#### Pattern 4: Persistent Cognitive State
Used by: feynman-tutor, python-tutor-skill, deeptutor-claude-skill

The tutor maintains state across sessions:
- Learner model (level, pace, preferences)
- Concept mastery (which topics are mastered, which need review)
- Error patterns (common mistakes to address)
- Learning graph (concept dependencies)

#### Pattern 5: Adaptive Difficulty Calibration
Used by: feynman-tutor, python-tutor-skill, GenMentor

The system dynamically adjusts based on learner signals:
- Fast correct answers -> increase difficulty
- Repeated failures -> decrease difficulty, provide more scaffolding
- Engagement drop -> change approach (switch from theory to analogy)

---

## Topic 3: Dual-Agent vs Single-Agent Learning Effectiveness

### Research Landscape

Web search for formal controlled studies on dual-agent vs single-agent AI tutoring effectiveness was severely limited by search API rate limiting throughout this research session. However, the following findings were gathered:

#### Historical Research (Pre-LLM era)

**Baylor & Kim (2005)** -- "Pedagogical Agent Design: The Impact of Agent Realism, Gender, and Role on Learning"
- Found that multi-agent configurations (expert + motivator) could outperform single agents on certain learning outcomes
- Key insight: Role specialization matters -- different agents for different pedagogical functions

**Davis (2018)** and others at AIED conferences
- Explored "dueling agents" or "agent debate" paradigms
- Found that observing agent-to-agent dialogue can activate social learning mechanisms

#### Emerging LLM-Era Research (2024-2025)

**Du et al. (2024, ICLR)** -- "Improving Factuality and Reasoning in LLMs through Multiagent Debate"
- Showed multi-agent debate improved reasoning quality
- Inspired educational adaptations where two agents debate in front of a learner

**GenMentor (WWW 2025)** -- GeminiLight/gen-mentor
- Formal paper at WWW 2025 (Oral presentation)
- Compares three paradigms: Traditional MOOC vs Chatbot ITS vs Goal-oriented ITS
- Multi-agent goal-oriented approach showed superior learning outcomes

#### Theoretical Framework for Expert-Novice Dual-Agent Learning

From the project's own feasibility analysis (`tasks/analysis/learning-mode/expert-novice-dual-agent-learning.md`):

**Advantages of dual-agent over single-agent:**

| Dimension | Single Agent | Dual Agent (Expert + Novice) |
|-----------|-------------|------------------------------|
| Learning mechanisms | One: direct instruction | Multiple: observation, social modeling, teach-back |
| Engagement | Moderate (Q&A only) | Higher (dramatic tension, narrative) |
| Cognitive load | Lower | Can be higher (split attention) |
| Question quality | Depends on learner | Novice agent asks questions learner might not think of |
| Error demonstration | Rare | Novice agent makes mistakes learner can learn from |
| Scalability | Simpler | More complex (two prompts, two memory stores) |

**Key risks of dual-agent approach:**
- Expert hallucinates incorrect explanations -> add verification skill
- Novice asks trivial questions -> configurable depth level
- Conversation loops without progress -> progress tracking
- Context window overflow -> summarization + chunked learning

### Recommended Search Terms for Further Research

Since live search was limited, the following queries should yield results on Google Scholar or Semantic Scholar:
- `"multi-agent" OR "dual agent" tutoring "learning outcomes" 2024 2025`
- `"pedagogical agents" "single agent" comparison learning effectiveness`
- `"LLM multi-agent debate" education tutoring`
- `site:aied2024.org multi-agent tutoring`
- `"intelligent tutoring system" "agent collaboration" learning gains`

---

## Synthesis: Key Design Principles for Effective Learning Dialogue

Across all repositories studied, seven principles consistently emerged:

### 1. Never Give the Answer
The single most common and powerful principle. Every effective tutoring system prevents the AI from directly solving the problem. Instead, it guides the learner through questions.

### 2. Maintain Persistent State
Effective tutors remember:
- What the learner knows (mastery map)
- What the learner struggles with (error patterns)
- What the learner's goals are (learning path)
- What happened last session (continuity)

### 3. Adapt in Real-Time
The best systems calibrate difficulty based on:
- Response speed and accuracy
- Engagement signals (asking questions vs. passive)
- Error patterns (repeating same mistakes)

### 4. Verify Understanding Before Advancing
No moving forward until the learner can demonstrate understanding. Methods:
- Teach-back (explain in own words)
- Prediction questions ("what will happen if...?")
- Application tasks (apply concept to new scenario)

### 5. Use Multiple Explanation Strategies
When one approach fails, try another:
- Analogy (connect to familiar domain)
- Code example (concrete demonstration)
- Visual description (mental model)
- Mathematical formalism (rigorous treatment)

### 6. Design for Productive Struggle
The sweet spot is "desirable difficulty" -- challenging enough to promote learning, not so hard it causes frustration. Implementation:
- Graduated hints (vague to specific)
- Comfort scores (0-100) per concept
- Adaptive difficulty adjustment

### 7. Every Interaction Serves a Learning Outcome
No filler, no small talk for its own sake. Every message from the tutor either:
- Introduces a concept
- Checks understanding
- Corrects a misconception
- Provides scaffolding
- Encourages reflection

---

## Recommendations for Implementation

Based on this research, the most effective approach for an Expert-Novice dual-agent learning system would combine:

1. **From feynman-tutor**: Persistent cognitive state (INDEX.md, LEARNER.md, GRAPH.md) and tiered feedback (red/yellow/green)
2. **From python-tutor-skill**: 4-level graduated hints and attempt tracking with full snapshots
3. **From deeptutor-claude-skill**: Graph-enhanced RAG with citation-driven answering
4. **From Intuitive ML Architect**: Verification gates (don't advance until mastery demonstrated)
5. **From GenMentor**: Goal-oriented architecture with specialized agent roles
6. **From the project's feasibility analysis**: Expert soul + Novice soul with distinct temperature settings (0.3 for Expert, 0.7 for Novice)

---

## Sources

- [koukekoukej-glitch/feynman-tutor](https://github.com/koukekoukej-glitch/feynman-tutor) (13 stars)
- [ndpvt-web/deeptutor-claude-skill](https://github.com/ndpvt-web/deeptutor-claude-skill) (8 stars)
- [Jellypod-Inc/school-skills](https://github.com/Jellypod-Inc/school-skills) (0 stars)
- [egouilliard-leyton/python-tutor-skill](https://github.com/egouilliard-leyton/python-tutor-skill) (1 star)
- [lmonkt/ostep-socratic-tutor](https://github.com/lmonkt/ostep-socratic-tutor) (7 stars)
- [rgrohitgupta938/Intuitive_ML_Architect](https://github.com/rgrohitgupta938/Intuitive_ML_Architect) (1 star)
- [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) (23 stars)
- [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) (66 stars)
- [BeArGpT76/socratic-ai-prompt](https://github.com/BeArGpT76/socratic-ai-prompt) (1 star)
- [Man0dya/Multi-Agent-AI-Tutoring-System](https://github.com/Man0dya/Multi-Agent-AI-Tutoring-System) (12 stars)
- [zexiJia/Ascend-Flow](https://github.com/zexiJia/Ascend-Flow) (11 stars)
- [JaiSuryaPrabu/skillix-ai-agent](https://github.com/JaiSuryaPrabu/skillix-ai-agent) (6 stars)
- [OpenClaw skills ecosystem](https://github.com/openclaw) (19.8k stars main repo)
