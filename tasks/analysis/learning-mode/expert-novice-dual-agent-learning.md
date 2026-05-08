# Expert/Novice Dual-Agent Learning Mode — Feasibility Analysis

## 1. Concept Overview

### 1.1 Core Idea

Create a group chat with two AI agents that collaborate to teach a human learner:

| Role | Responsibility | Behavior |
|------|---------------|----------|
| **Expert** | Explains concepts, guides learning path | Uses Feynman technique / Socratic method |
| **Novice** | Learns from Expert, asks questions | Demonstrates understanding, identifies gaps |

The human learner observes or participates in the Expert-Novice dialogue, learning through:
1. Expert's structured explanations
2. Novice's questions (which the learner might also have)
3. Expert's answers to Novice's questions
4. Novice's attempts to apply knowledge

### 1.2 Learning Model

```
┌─────────────────────────────────────────────────┐
│                  Group Chat                       │
│                                                   │
│   Expert ──explains──▶ Novice                     │
│     │                     │                       │
│     │   answers           │  asks questions       │
│     │   ◀─────────────────│                       │
│     │                     │                       │
│     └──────┬──────────────┘                       │
│            │                                      │
│            ▼                                      │
│     Human Learner (observes / participates)        │
└─────────────────────────────────────────────────┘
```

---

## 2. Feasibility Analysis

### 2.1 Technical Feasibility: ✅ Feasible

| Aspect | Assessment | Details |
|--------|-----------|---------|
| Multi-agent chat | ✅ Mature | OpenClaw supports skills + souls; LangChain/AutoGen/CrewAI all support multi-agent |
| Role-based prompting | ✅ Proven | System prompts can define Expert/Novice personas reliably |
| Context sharing | ✅ Available | Shared chat history provides common context |
| Memory persistence | ⚠️ Needs design | Need to track learning progress across sessions |
| Skill composition | ✅ Available | Skills can be stacked (e.g., Feynman + Socratic) |

### 2.2 Learning Effectiveness: ✅ Promising

Research-backed advantages:
- **Feynman Technique**: Explaining concepts simply reveals gaps (Expert does this for Novice)
- **Socratic Method**: Guided questioning activates critical thinking (Expert asks Novice)
- **Protégé Effect**: Teaching others reinforces learning (Novice "teaches back")
- **Social Learning**: Observing dialogue is more engaging than reading docs

### 2.3 Key Risks

| Risk | Mitigation |
|------|-----------|
| Expert hallucinates incorrect explanations | Add verification skill; cross-reference docs |
| Novice asks trivial questions | Configurable depth level; context-aware questioning |
| Conversation loops without progress | Progress tracking; learning objectives |
| Context window overflow | Summarization skill; chunked learning |

---

## 3. Input / Output Design

### 3.1 Course Type A: agents.md Tutorial (e.g., "How to use this repository")

#### Input

```
agents.md  (tutorial document)
├── Prerequisites
├── Installation steps
├── Usage examples
├── Configuration options
└── Troubleshooting
```

**Expert Input:**
- Full agents.md content as knowledge base
- Course learning objectives (auto-generated from document structure)
- Learner's assumed level (beginner / intermediate)

**Novice Input:**
- Learner's background (e.g., "I know git basics but never used agents")
- Learning goals (e.g., "I want to understand how to create my own agent")
- Current understanding state (tracked via memory)

#### Output

```
Learning Session Output:
├── Structured dialogue transcript
├── Key concepts identified
├── Q&A pairs (Novice's questions + Expert's answers)
├── Practice exercises generated
├── Knowledge checkpoints (quiz-like verification)
└── Progress summary
```

#### Example Dialogue Flow

```
Expert: Today we'll learn how to use agents.md. First, agents.md defines
        how an AI agent behaves in your project. Think of it as a "job
        description" for your AI assistant. What do you think an agent
        needs to know to do its job well?

Novice: Hmm, maybe it needs to know what tools are available? And what
        the project structure looks like?

Expert: Exactly right! In agents.md, we define:
        1. Available tools (scripts, commands)
        2. Project structure awareness
        3. Behavior rules (what to do / what not to do)
        Can you give me an example of a "behavior rule" you'd want an
        agent to follow?

Novice: Maybe... "never delete files without asking first"?

Expert: Perfect example! That's exactly the kind of safety rule you'd
        put in agents.md. Now let me show you the actual format...
```

### 3.2 Course Type B: General Course (e.g., references folder materials)

#### Input

```
Course materials
├── Lecture notes / textbook chapters
├── Code examples
├── Diagrams / architecture descriptions
├── Practice problems
└── Assessment criteria
```

**Expert Input:**
- Course content as knowledge base
- Curriculum structure (chapters, prerequisites, dependencies)
- Teaching strategy (Feynman-first, Socratic-first, or hybrid)

**Novice Input:**
- Learner's prior knowledge assessment
- Learning pace preference
- Preferred learning style (code examples vs. analogies vs. visual)

#### Output

```
Learning Session Output:
├── Concept explanations (simplified by Expert)
├── Analogy bank (Expert-generated analogies)
├── Q&A log (Novice's questions + Expert's answers)
├── Code examples with annotations
├── Practice exercises with solutions
├── Self-assessment quiz
├── Learning progress report
└── Next session recommendation
```

---

## 4. Implementation Design

### 4.1 Required Skills

| Skill | Role | Purpose | Source |
|-------|------|---------|--------|
| **Feynman Explainer** | Expert | Break down complex concepts into simple explanations | Custom skill |
| **Socratic Questioner** | Expert | Ask guided questions to check understanding | Custom skill |
| **Active Learner** | Novice | Ask clarifying questions, request examples/code | Custom skill |
| **Knowledge Validator** | Expert | Verify Novice's understanding before moving on | Custom skill |
| **Progress Tracker** | System | Track learning progress, generate reports | Custom skill |
| **Content Parser** | System | Parse course materials into teachable chunks | Custom skill |

### 4.2 Required Souls

```yaml
# Expert Soul
name: learning-expert
description: |
  An experienced teacher who excels at breaking down complex topics
  using the Feynman technique. Patient, encouraging, and skilled at
  Socratic questioning. Adapts explanation depth to learner's level.
traits:
  - patient
  - methodical
  - encouraging
  - precise
rules:
  - Always verify understanding before advancing
  - Use analogies from the learner's domain
  - Never skip foundational concepts
  - Provide code examples when teaching technical topics
  - Celebrate correct answers, gently correct mistakes

---
# Novice Soul
name: learning-novice
description: |
  A curious learner who asks thoughtful questions to build understanding.
  Not afraid to say "I don't understand" and always requests concrete
  examples. Represents a learner at the specified knowledge level.
traits:
  - curious
  - honest about gaps
  - persistent
  - practical
rules:
  - Always ask for examples when concepts are abstract
  - Request code demonstrations for technical topics
  - Identify when explanations are too shallow
  - Try to apply concepts before asking for more help
  - Summarize understanding in own words
```

### 4.3 Required Memory

```
Memory Architecture:
├── Course Memory (shared)
│   ├── Course content (parsed and chunked)
│   ├── Learning objectives
│   └── Progress state (completed topics, current topic)
├── Expert Memory
│   ├── Teaching strategy adjustments
│   ├── Topics that needed more explanation
│   └── Effective analogies used
└── Novice Memory
    ├── Understanding checkpoints (passed/failed)
    ├── Questions asked and answers received
    └── Knowledge gaps identified
```

### 4.4 Implementation Steps

```
Phase 1: Foundation (Week 1-2)
├── Design Expert soul with Feynman technique prompt
├── Design Novice soul with active learning prompt
├── Create Content Parser skill (markdown → teachable chunks)
└── Test basic Expert→Novice dialogue

Phase 2: Core Skills (Week 2-3)
├── Implement Socratic Questioner skill for Expert
├── Implement Active Learner skill for Novice
├── Add Knowledge Validator skill
└── Test with agents.md tutorial content

Phase 3: Progress System (Week 3-4)
├── Implement Progress Tracker skill
├── Design memory schema for learning state
├── Add session resume capability
└── Test multi-session learning continuity

Phase 4: Polish (Week 4-5)
├── Add code example generation
├── Add practice exercise generation
├── Add self-assessment quiz generation
└── End-to-end testing with real course content
```

---

## 5. Skill Design Details

### 5.1 Feynman Explainer Skill

```yaml
---
name: feynman-explainer
description: |
  Break down complex technical concepts using the Feynman technique.
  Simplify to essential ideas, use analogies, identify gaps.
type: teaching
---

## Instructions

When explaining a concept:

1. **State the concept simply** — One sentence, no jargon
2. **Explain to a beginner** — As if teaching a 12-year-old
3. **Identify gaps** — What did you struggle to simplify? That's where the gaps are
4. **Use analogies** — Connect to everyday experiences
5. **Review and refine** — Can you make it even simpler?

### For technical content:
- Always provide a code example
- Show input → output explicitly
- Explain the "why" before the "how"

### Anti-patterns:
- ❌ Using jargon without defining it first
- ❌ Skipping "obvious" steps
- ❌ Assuming prior knowledge not in the course
- ❌ Explaining the "what" without the "why"
```

### 5.2 Active Learner Skill

```yaml
---
name: active-learner
description: |
  Actively learn from explanations by asking clarifying questions,
  requesting examples, and demonstrating understanding.
type: learning
---

## Instructions

After receiving an explanation:

1. **Paraphrase** — Restate in your own words to verify understanding
2. **Question** — Ask about anything unclear:
   - "Can you give me a real example of this?"
   - "What happens if [edge case]?"
   - "How does this relate to [previous concept]?"
3. **Apply** — Try to use the concept in a new scenario
4. **Identify gaps** — State what you still don't understand

### Question types:
- **Clarification**: "What does X mean in this context?"
- **Example**: "Can you show me a code example?"
- **Connection**: "How does this relate to what we learned earlier?"
- **Challenge**: "What if we did Y instead of X?"
- **Application**: "So if I wanted to do Z, I would...?"
```

---

## 6. OpenClaw-Specific Implementation

### 6.1 Architecture with OpenClaw

```
OpenClaw Learning System:
├── Skills (installed via clawhub)
│   ├── feynman-explainer/
│   │   └── SKILL.md
│   ├── active-learner/
│   │   └── SKILL.md
│   ├── content-parser/
│   │   ├── SKILL.md
│   │   └── scripts/parse-course.py
│   └── progress-tracker/
│       ├── SKILL.md
│       └── scripts/track-progress.py
├── Souls (registered via onlycrabs.ai)
│   ├── learning-expert/SOUL.md
│   └── learning-novice/SOUL.md
└── Memory (local persistence)
    ├── course-state.json
    ├── expert-memory.json
    └── novice-memory.json
```

### 6.2 Agent Configuration

```yaml
# Expert Agent
agent:
  name: Learning Expert
  soul: learning-expert
  skills:
    - feynman-explainer
    - socratic-questioner
    - knowledge-validator
  memory: persistent
  temperature: 0.3  # More factual, less creative

# Novice Agent
agent:
  name: Learning Novice
  soul: learning-novice
  skills:
    - active-learner
  memory: persistent
  temperature: 0.7  # More varied questions
```

### 6.3 Session Flow

```
1. User provides course material (URL / file path / text)
2. Content Parser skill chunks the material
3. Learning objectives are auto-generated
4. Session starts:
   a. Expert introduces first concept (Feynman style)
   b. Novice paraphrases and asks questions
   c. Expert answers and verifies understanding
   d. Progress Tracker updates state
   e. Repeat for next concept
5. Session ends with:
   a. Summary of learned concepts
   b. Practice exercises
   c. Self-assessment quiz
   d. Next session recommendation
```

---

## 7. Evaluation Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| Concept coverage | > 90% of course material | Topic checklist |
| Understanding verification | > 80% correct on checks | Knowledge checkpoints |
| Question quality | > 70% non-trivial questions | Manual / LLM evaluation |
| Session engagement | > 5 exchanges per concept | Dialogue length |
| Learning retention | > 70% after 24 hours | Follow-up quiz |

---

## 8. Conclusion

### Feasibility: ✅ Technically feasible, pedagogically promising

**Why it works:**
- Expert-Novice dialogue naturally implements active learning
- Feynman technique + Socratic method is a proven pedagogical combination
- Multi-agent AI frameworks (OpenClaw, CrewAI, AutoGen) provide the infrastructure
- Memory systems enable continuity across learning sessions

**Key to success:**
1. Well-crafted souls (personas) for Expert and Novice
2. Structured skill design (Feynman + Socratic + Active Learning)
3. Persistent memory for learning progress
4. Content parser that chunks materials appropriately

**Recommended next steps:**
1. Prototype with a single agents.md tutorial
2. Test Expert soul with Feynman technique prompt
3. Test Novice soul with active learning prompt
4. Evaluate dialogue quality with real learners
5. Iterate on skills based on feedback
