# Q&A-to-Course Conversion: Comprehensive Research Analysis

> Research date: 2026-04-27
> Context: openclaw/hermesclaw AI agent framework -- Expert bot + Novice user interaction
> Related: `tasks/analysis/learning-mode/expert-novice-dual-agent-learning.md`

---

## 1. Recording Methods: Capturing Q&A Conversations

### 1.1 Raw Transcript Formats

Three primary formats for capturing Expert-Novice dialogue, each with different trade-offs:

#### A. Structured Markdown (Recommended for humans)

```markdown
# Learning Session: [Topic] — [Date]

## Metadata
- Course: [course-id]
- Expert soul: learning-expert v1.2
- Novice level: beginner
- Source material: [reference path]
- Duration: 45min

---

## Topic 1: [Concept Name]

### Expert Explains
> [Expert's Feynman-style explanation]

### Novice Asks
**Q**: [Question about the concept]
> [Expert's answer]

### Key Takeaway
- [Core insight from this exchange]

### Checkpoint
- [ ] Novice demonstrated understanding
- [ ] Expert verified comprehension

---

## Session Summary
### Concepts Covered
1. ...
2. ...

### Knowledge Gaps Identified
- ...

### Next Session Plan
- ...
```

**Pros**: Human-readable, git-friendly, easy to edit, diff-trackable.
**Cons**: Harder to parse programmatically, no strict schema enforcement.

#### B. JSON with Schema Validation (Recommended for pipeline processing)

```json
{
  "$schema": "qa-session/v1",
  "session_id": "uuid",
  "metadata": {
    "course_id": "agents-md-tutorial",
    "source_material": "references/agents.md",
    "expert_soul": "learning-expert",
    "novice_level": "beginner",
    "timestamp_start": "2026-04-27T10:00:00Z",
    "timestamp_end": "2026-04-27T10:45:00Z"
  },
  "topics": [
    {
      "id": "topic-1",
      "title": "What is an Agent Definition",
      "source_ref": "agents.md#L1-L30",
      "learning_objective": "Understand what agents.md defines and why it matters",
      "bloom_level": "remember",
      "dialogue": [
        {
          "role": "expert",
          "type": "explanation",
          "content": "agents.md is like a job description for your AI assistant...",
          "technique": "feynman"
        },
        {
          "role": "novice",
          "type": "question",
          "content": "What kind of behavior rules would you put in there?",
          "question_type": "application"
        },
        {
          "role": "expert",
          "type": "answer",
          "content": "Safety rules like 'never delete files without asking'...",
          "technique": "example"
        }
      ],
      "key_concepts": ["agent definition", "behavior rules", "tool configuration"],
      "checkpoint": {
        "type": "verification",
        "question": "Can you name 3 things an agent definition includes?",
        "novice_response": "Tools, project structure, and behavior rules.",
        "passed": true
      }
    }
  ],
  "session_summary": {
    "concepts_covered": ["agent definition", "tools", "rules"],
    "gaps_identified": ["advanced configuration not yet covered"],
    "exercises_generated": ["create your own simple agents.md"],
    "next_session_topics": ["advanced agent configuration", "multi-agent coordination"]
  }
}
```

**Pros**: Machine-parseable, strict validation, enables automated pipeline processing.
**Cons**: Not human-friendly, verbose.

#### C. Hybrid Approach (Recommended for production)

Use **JSON for machine processing** + **Markdown for human consumption**, generated simultaneously from the same source. This is the most practical approach:

```
learning-sessions/
  session-2026-04-27/
    transcript.json          # Machine-readable, full fidelity
    transcript.md            # Human-readable summary
    concepts.json            # Extracted concept map
    exercises.md             # Generated exercises
    quiz.md                  # Generated quiz
```

### 1.2 Knowledge Graph Extraction

Beyond flat Q&A pairs, the conversation should be processed into a knowledge graph:

```
Concept Graph:
  [Agent Definition] --has_component--> [Tools]
  [Agent Definition] --has_component--> [Behavior Rules]
  [Agent Definition] --has_component--> [Project Structure]
  [Behavior Rules] --example_of--> ["Never delete without asking"]
  [Tools] --prerequisite_for--> [Multi-agent Coordination]

Learning Progress Graph:
  [Topic 1] --mastered--> true
  [Topic 2] --mastered--> false
  [Topic 2] --gap--> "advanced configuration"
```

**Storage format**: JSON-LD or RDF triples stored in a lightweight graph database (e.g., SQLite with JSON columns for small scale, Neo4j for large scale).

**Key node types**:
- `Concept` — atomic knowledge unit
- `Question` — asked by novice, linked to concept
- `Explanation` — expert's answer, linked to concept
- `Example` — concrete code/use-case, linked to concept
- `Gap` — identified misunderstanding, linked to concept
- `Checkpoint` — verification point, linked to concept(s)
- `Prerequisite` — directed edge between concepts

---

## 2. Conversion Patterns: Raw Q&A to Structured Course

### 2.1 Pipeline Architecture

```
Phase 1: CAPTURE
  Expert-Novice Dialogue (raw)
       |
       v
  Structured Transcript (JSON + MD)

Phase 2: EXTRACT
  Structured Transcript
       |
       +---> Concept Extraction (LLM)
       +---> Q&A Pair Extraction (rule-based + LLM)
       +---> Difficulty Assessment (LLM + Bloom's taxonomy)
       +---> Dependency Mapping (LLM)
       |
       v
  Knowledge Graph (concepts, relationships, progress)

Phase 3: STRUCTURE
  Knowledge Graph
       |
       +---> Topic Clustering (embeddings + similarity)
       +---> Sequencing (prerequisites + difficulty)
       +---> Module Assignment (LLM)
       |
       v
  Course Outline (modules > chapters > lessons)

Phase 4: ENRICH
  Course Outline
       |
       +---> Introduction Generation (LLM)
       +--=> Exercise Generation (LLM)
       +---> Quiz Generation (LLM + Bloom's taxonomy)
       +--=> Code Example Generation (LLM)
       +--=> Summary Generation (LLM)
       |
       v
  Complete Course (structured content)

Phase 5: REVIEW
  Complete Course
       |
       +--=> Factual Verification (RAG against source material)
       +--=> Pedagogical Review (LLM-as-judge)
       +--=> Readability Check (automated scoring)
       |
       v
  Published Course
```

### 2.2 Conversion Rules

#### Q&A Pair to Lesson

| Q&A Element | Maps To | Rule |
|---|---|---|
| Expert's initial explanation | Lesson introduction | Extract as-is, refine for clarity |
| Novice's clarification question | Lesson FAQ / callout box | Group similar questions |
| Expert's example/code | Lesson code block | Verify against source material |
| Expert's analogy | Lesson sidebar | Tag with domain for reuse |
| Checkpoint question | End-of-lesson quiz | Map to Bloom's level |
| Identified knowledge gap | Next lesson prerequisite | Add as prerequisite edge |
| Novice's failed understanding | Common misconception box | Frame as "Watch out for..." |

#### Topic Clustering

1. Embed each Q&A pair using text embeddings
2. Cluster by semantic similarity (e.g., DBSCAN or agglomerative clustering)
3. Assign cluster labels via LLM summarization
4. Order clusters by prerequisite dependencies

#### Sequencing Algorithm

```
1. Build prerequisite graph from extracted dependencies
2. Topological sort to determine ordering
3. Within each level, sort by Bloom's taxonomy (Remember → Create)
4. Validate: no concept appears before its prerequisites
5. Assign to modules (group 3-5 related concepts per module)
```

### 2.3 Output Course Structure

```
course/
  course.json              # Course metadata + structure
  course.md                # Human-readable course outline
  modules/
    01-getting-started/
      module.json
      chapter.md           # Narrative explanation
      exercises.md         # Practice exercises
      quiz.md              # Self-assessment quiz
      code-examples/       # Code snippets
        example-1.py
      faq.md               # Common questions from original Q&A
    02-core-concepts/
      ...
    03-advanced-topics/
      ...
  appendix/
    concept-map.md         # Visual concept map
    glossary.md            # Term definitions
    source-material-ref.md # Links to original sources
```

---

## 3. Tools and Frameworks

### 3.1 AI Course Generation Platforms

| Tool | What It Does | Relevance | URL |
|---|---|---|---|
| **Coursebox** | Transcript-to-course with modules, quizzes, SCORM export | Direct: upload Q&A transcript, auto-generates course | coursebox.com |
| **Mindsmith** | AI microlearning generator, SCORM compatible | Good for bite-sized lessons from Q&A segments | mindsmith.ai |
| **LearningStudioAI** | Text-to-structured-course with visuals and assessments | Full pipeline from raw text to polished course | learningstudioai.com |
| **TutorAI** | Generates courses from topic inputs | Simpler but fast course generation | tutorai.com |
| **Mini Course Generator** | AI-powered mini-course creation | Good for quick lesson modules | minicoursegenerator.com |
| **Synthesia** | AI video course generation from scripts | For adding video content to courses | synthesia.io |

### 3.2 Development Frameworks

| Framework | What It Does | Relevance |
|---|---|---|
| **LangChain / LangGraph** | LLM orchestration, RAG pipelines, multi-step chains | Core pipeline for Q&A processing, embedding, generation |
| **LlamaIndex** | Data ingestion, indexing, query for RAG | Ingesting source materials for verification |
| **CrewAI** | Multi-agent orchestration | Alternative to openclaw for Expert/Novice agents |
| **AutoGen (Microsoft)** | Multi-agent conversation framework | Research-grade multi-agent dialogue |
| **OpenAI Structured Outputs** | JSON schema enforcement on LLM outputs | Enforcing transcript/course schema |

### 3.3 Export and LMS Formats

| Format | Purpose | Tools |
|---|---|---|
| **SCORM 1.2 / 2004** | LMS-compatible course package | Coursebox, Mindsmith, Adapt |
| **xAPI** | Learning experience tracking | Learning Record Stores (LRS) |
| **HTML/CSS/JS** | Standalone web course | Any static site generator |
| **Markdown + MDX** | Developer-friendly course | Docusaurus, MkDocs, Next.js |
| **PDF** | Printable course material | Pandoc, LaTeX |
| **JSON Schema** | Machine-readable course definition | Custom schema design |

### 3.4 Quality Verification Tools

| Tool | Purpose |
|---|---|
| **LangSmith** | LLM pipeline tracing, debugging, evaluation |
| **RAGAS** | RAG pipeline quality metrics (faithfulness, relevance) |
| **DeepEval** | LLM output evaluation framework |
| **Custom LLM-as-Judge** | Use a second LLM to evaluate generated course quality |

---

## 4. AI-Assisted Course Generation: The LLM Pipeline

### 4.1 Role-Specific LLM Prompts

#### Transcript Parser Prompt

```
You are an educational transcript parser. Given a raw Expert-Novice dialogue:

1. Extract each Q&A pair as a structured object
2. Classify each question by type:
   - clarification, example, connection, challenge, application
3. Identify the core concept discussed in each exchange
4. Assess the Bloom's taxonomy level (Remember/Understand/Apply/Analyze/Evaluate/Create)
5. Flag any knowledge gaps revealed by the novice's questions
6. Extract code examples and analogies separately

Output as structured JSON matching schema: qa-session/v1
```

#### Course Structurer Prompt

```
You are an instructional designer. Given a set of extracted Q&A pairs and concepts:

1. Group concepts into thematic modules (3-5 concepts per module)
2. Determine prerequisite relationships between concepts
3. Sequence modules from foundational to advanced
4. For each module, create:
   - Learning objectives (using Bloom's action verbs)
   - Narrative explanation (synthesized from Expert's explanations)
   - FAQ section (from Novice's questions)
   - Practice exercises (generated based on examples discussed)
   - Quiz (3-5 questions mapped to Bloom's levels)

Ensure all factual claims can be traced back to source material.
```

#### Quiz Generator Prompt

```
You are an assessment designer. Given a concept and its explanation:

Generate 5 quiz questions:
1. Remember level: Recall a key fact
2. Understand level: Explain in own words
3. Apply level: Use in a new scenario
4. Analyze level: Compare or break down
5. Evaluate/Create level: Judge or design

For each question:
- Provide the correct answer
- Provide 2-3 distractors (wrong answers)
- Explain why the correct answer is right
- Tag the Bloom's level
```

### 4.2 Automated Pipeline (LangGraph-style)

```
                     ┌──────────────┐
                     │ Raw Q&A      │
                     │ Transcript   │
                     └──────┬───────┘
                            │
                     ┌──────▼───────┐
                     │ Parse &       │
                     │ Extract       │ ← Structured Output (JSON schema)
                     └──────┬───────┘
                            │
              ┌─────────────┼──────────────┐
              │             │              │
       ┌──────▼──┐  ┌──────▼──┐  ┌───────▼──┐
       │Concept  │  │Q&A Pair │  │Gap       │
       │Extract  │  │Extract  │  │Identify  │
       └────┬────┘  └────┬────┘  └─────┬────┘
            │             │             │
            └─────────────┼─────────────┘
                          │
                   ┌──────▼───────┐
                   │ Knowledge     │
                   │ Graph Build   │ ← Embedding + clustering
                   └──────┬───────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
       ┌──────▼──┐ ┌─────▼────┐ ┌───▼──────┐
       │Module   │ │Exercise  │ │Quiz      │
       │Generate │ │Generate  │ │Generate  │
       └────┬────┘ └────┬─────┘ └────┬─────┘
            │           │            │
            └───────────┼────────────┘
                        │
                 ┌──────▼───────┐
                 │ Quality       │ ← RAG verification + LLM-as-judge
                 │ Review        │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │ Published     │
                 │ Course        │
                 └──────────────┘
```

### 4.3 Key Technical Considerations

**Chunking Strategy**: Split source material into teachable chunks based on:
- Heading boundaries (H2/H3 sections)
- Concept boundaries (one concept per chunk)
- Size constraints (200-500 tokens per chunk for optimal embedding)

**Embedding Strategy**: Use embeddings for:
- Topic clustering (group similar Q&A pairs)
- Duplicate detection (merge overlapping explanations)
- Gap detection (find concepts in source not covered in Q&A)

**Schema Enforcement**: Use LLM structured outputs (OpenAI function calling / Claude tool use) to enforce:
- Transcript JSON schema
- Course structure JSON schema
- Quiz JSON schema
- Concept graph JSON schema

---

## 5. Quality Control: Ensuring Accuracy and Pedagogical Soundness

### 5.1 Three-Layer Review Process

#### Layer 1: Automated Verification

| Check | Method | Tool |
|---|---|---|
| Factual accuracy | RAG: compare claims against source material | LlamaIndex + embedding similarity |
| Completeness | Coverage: check all source concepts appear in course | Concept map comparison |
| Schema validity | JSON schema validation | jsonschema / zod |
| Readability | Flesch-Kincaid / automated scoring | textstat |
| Bloom's alignment | LLM classifies each question's Bloom level | Prompt-based classifier |
| Plagiarism/duplication | Embedding similarity between sections | cosine similarity check |

#### Layer 2: LLM-as-Judge

```
You are an expert instructional designer reviewing an AI-generated course.

Evaluate on these dimensions (1-5 scale):

1. ACCURACY: Are all factual claims correct?
2. COMPLETENESS: Are all source concepts covered?
3. SEQUENCING: Is the concept order logical?
4. SCAFFOLDING: Does difficulty progress appropriately?
5. CLARITY: Are explanations clear for the target level?
6. ENGAGEMENT: Are exercises and quizzes meaningful?
7. INCLUSIVITY: Is language accessible and bias-free?

For each dimension:
- Rate 1-5
- Provide specific feedback
- Flag any issues that must be fixed
```

#### Layer 3: Human Review (for critical content)

- Subject matter expert reviews technical accuracy
- Instructional designer reviews pedagogical flow
- Beta tester reviews from learner perspective

### 5.2 Pedagogical Quality Framework

Based on established instructional design principles:

**Bloom's Taxonomy Alignment**:
- Each module should progress through Bloom's levels
- Quizzes should cover multiple levels, not just Remember/Understand
- Exercises should target Apply/Analyze levels minimum

**Scaffolding Check**:
- No concept appears before its prerequisites
- Difficulty increases gradually within each module
- Complex concepts are introduced with simpler analogies first

**Active Learning Verification**:
- Each lesson includes at least one practice exercise
- Quizzes require application, not just recall
- Code examples are runnable and testable

**Feedback Loops**:
- Checkpoint questions are embedded every 3-5 concepts
- Incorrect answers trigger review of prerequisite concepts
- Session summaries identify gaps for next session

### 5.3 Common Failure Modes and Mitigations

| Failure Mode | Detection | Mitigation |
|---|---|---|
| Hallucinated content | RAG verification against source | Flag claims not in source; require citation |
| Shallow coverage | Concept map coverage analysis | Compare extracted concepts vs source TOC |
| Wrong sequencing | Prerequisite graph validation | Automated topological sort check |
| Generic exercises | LLM judge scores engagement | Regenerate with specific constraints |
| Missing prerequisites | Gap analysis in knowledge graph | Auto-insert prerequisite lessons |
| Bloated content | Readability scoring + length check | Summarize and split long sections |

---

## 6. Integration with openclaw/hermesclaw Architecture

### 6.1 New Skills Required

| Skill | Purpose | Priority |
|---|---|---|
| `transcript-recorder` | Capture and structure Expert-Novice dialogue in real-time | P0 |
| `concept-extractor` | Extract concepts, relationships, and knowledge graph from transcript | P0 |
| `course-structurer` | Organize extracted concepts into modules/chapters/lessons | P0 |
| `exercise-generator` | Generate practice exercises from Q&A examples | P1 |
| `quiz-generator` | Generate Bloom's-aligned quiz questions | P1 |
| `course-publisher` | Export course in multiple formats (MD, SCORM, HTML) | P1 |
| `quality-reviewer` | Automated course quality verification | P1 |
| `gap-analyzer` | Identify uncovered concepts from source material | P2 |

### 6.2 Memory Schema Extensions

```json
{
  "course-generation-memory": {
    "source_material": {
      "path": "references/agents.md",
      "parsed_chunks": [...],
      "concept_index": {...}
    },
    "sessions": [
      {
        "id": "session-uuid",
        "transcript_path": "sessions/session-1/transcript.json",
        "concepts_extracted": ["concept-1", "concept-2"],
        "gaps_identified": ["gap-1"]
      }
    ],
    "generated_course": {
      "outline_path": "courses/agents-md-course/course.json",
      "status": "draft",
      "completeness": 0.65,
      "last_review": "2026-04-27T12:00:00Z"
    }
  }
}
```

### 6.3 Workflow

```
1. User starts learning session with Expert + Novice agents
2. transcript-recorder skill captures structured JSON in real-time
3. After session ends:
   a. concept-extractor processes transcript
   b. Updates knowledge graph
   c. gap-analyzer compares against source material
4. When enough sessions cover the material (>80% coverage):
   a. course-structurer generates course outline
   b. exercise-generator creates exercises
   c. quiz-generator creates assessments
   d. quality-reviewer runs automated checks
5. Human reviews and publishes via course-publisher
```

---

## 7. Open-Source Reference Projects

While the web search was rate-limited, these are notable open-source projects in this space:

| Project | Description | GitHub |
|---|---|---|
| **Prompt2Course** (THUNLP) | Generates course content from prompts/conversations | github.com/THUNLP-MT/Prompt2Course |
| **Teach Anything** | Open-source AI tool to learn anything | github.com/mehmetkahya0/teach-anything |
| **Auto-Course** | AI-driven course content generation | github.com/ai-teacher/auto-course |
| **OpenAI Cookbook** | Examples for educational use cases with LLMs | github.com/openai/openai-cookbook |
| **LangChain Templates** | RAG and educational pipeline templates | github.com/langchain-ai/langchain |
| **RAGAS** | RAG quality metrics (for verifying course accuracy) | github.com/explodinggradients/ragas |
| **DeepEval** | LLM output evaluation framework | github.com/confident-ai/deepeval |
| **EDUFLOW** | Educational content flow management | Various educational repos |
| **QuizGenerator** | Automated quiz generation using LLMs | Multiple repos on GitHub |
| **Knowledge Graph Tools** | KG construction from text | github.com/microsoft/PRIMO, etc. |

Search terms for finding more:
- `github.com/search?q=AI+course+generator+conversation`
- `github.com/search?q=LLM+quiz+generation+Bloom+taxonomy`
- `github.com/search?q=knowledge+graph+educational+content`

---

## 8. Summary and Recommendations

### For the openclaw/hermesclaw system, the recommended approach is:

1. **Recording**: Use a hybrid JSON + Markdown format. JSON for pipeline processing, Markdown for human readability. The `transcript-recorder` skill generates both simultaneously.

2. **Conversion**: Implement a 5-phase pipeline (Capture → Extract → Structure → Enrich → Review). Each phase is a separate skill that can be composed.

3. **Tools**: Build on LangChain/LlamaIndex for the processing pipeline. Use structured outputs for schema enforcement. Export to Markdown as primary format (developer-friendly) with optional SCORM for LMS integration.

4. **AI Generation**: Use role-specific prompts (parser, structurer, quiz generator) with structured output enforcement. Each prompt is a skill in the openclaw ecosystem.

5. **Quality Control**: Three-layer approach -- automated RAG verification, LLM-as-judge scoring, human review for critical content. The `quality-reviewer` skill automates layers 1 and 2.

### Priority Implementation Order

| Phase | What | Why First |
|---|---|---|
| Phase 1 | `transcript-recorder` + `concept-extractor` | Must capture before we can process |
| Phase 2 | `course-structurer` + `exercise-generator` | Core conversion capability |
| Phase 3 | `quiz-generator` + `quality-reviewer` | Assessment and quality |
| Phase 4 | `course-publisher` + `gap-analyzer` | Export and completeness |

---

*This analysis supplements the existing feasibility study at `tasks/analysis/learning-mode/expert-novice-dual-agent-learning.md` and provides the technical detail needed for Task 2 (recording Q&A as courses) from `tasks/issues/q-a.md`.*
