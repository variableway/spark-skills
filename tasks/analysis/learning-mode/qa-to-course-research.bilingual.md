# Q&A-to-Course: Recording & Top GitHub Repos Analysis
# 问答转课程：记录方法与 Top GitHub 仓库分析

> Research date: 2026-04-27
> Issue: [#42](https://github.com/variableway/fire-skills/issues/42)
> Source: `tasks/issues/q-a.md` Task 2
> Related: `tasks/analysis/learning-mode/expert-novice-dual-agent-learning.md`

---

## Part 1: How to Record Q&A into a Course / 如何将问答记录成课程

### EN: Recording Methods

Three recommended formats for capturing Expert-Novice dialogue:

| Format | Best For | Pros | Cons |
|---|---|---|---|
| **Structured Markdown** | Human readability, git-friendly | Easy to edit, diff-trackable | Hard to parse programmatically |
| **JSON with Schema** | Pipeline processing, automation | Strict validation, machine-parseable | Not human-friendly, verbose |
| **Hybrid (JSON + MD)** | Production use | Best of both worlds | Double storage |

### CN: 记录方法

三种推荐的对话记录格式：

| 格式 | 适用场景 | 优点 | 缺点 |
|---|---|---|---|
| **结构化 Markdown** | 人工阅读、git 友好 | 易编辑、可追踪变更 | 难以程序化解析 |
| **JSON + Schema 校验** | 流水线处理、自动化 | 严格校验、机器可解析 | 不够友好、冗长 |
| **混合模式（JSON + MD）** | 生产环境 | 兼具两者优势 | 双倍存储空间 |

### EN: Conversion Pipeline (5 Phases)

```
Phase 1: CAPTURE → Structured Transcript (JSON + MD)
Phase 2: EXTRACT → Concept extraction, Q&A classification, difficulty mapping
Phase 3: STRUCTURE → Topic clustering, prerequisite sequencing, module assignment
Phase 4: ENRICH → Introductions, exercises, quizzes, code examples, summaries
Phase 5: REVIEW → RAG verification + LLM-as-judge + optional human review
```

### CN: 转换流水线（5 个阶段）

```
阶段 1: 捕获 → 结构化对话记录（JSON + MD）
阶段 2: 提取 → 概念提取、问答分类、难度映射
阶段 3: 结构化 → 主题聚类、前置知识排序、模块分配
阶段 4: 丰富 → 生成导言、练习、测验、代码示例、总结
阶段 5: 审核 → RAG 验证 + LLM 评判 + 可选人工审核
```

### EN: Quality Control (3 Layers)

| Layer | Method | Automation |
|---|---|---|
| Layer 1: Automated | RAG verification, concept coverage, schema validation | Full |
| Layer 2: LLM-as-Judge | 7-dimension evaluation (accuracy, completeness, sequencing...) | Full |
| Layer 3: Human | SME review, instructional designer review, beta testing | Manual |

### CN: 质量控制（3 层）

| 层次 | 方法 | 自动化程度 |
|---|---|---|
| 第 1 层：自动化 | RAG 验证、概念覆盖率、Schema 校验 | 全自动 |
| 第 2 层：LLM 评判 | 7 维度评估（准确性、完整性、排序...） | 全自动 |
| 第 3 层：人工 | 领域专家审核、教学设计审核、Beta 测试 | 手动 |

### EN: Skills Needed for openclaw/hermesclaw

| Skill | Purpose | Priority |
|---|---|---|
| `transcript-recorder` | Capture structured Expert-Novice dialogue in real-time | P0 |
| `concept-extractor` | Extract concepts and relationships from transcript | P0 |
| `course-structurer` | Organize concepts into modules/chapters/lessons | P0 |
| `exercise-generator` | Generate practice exercises from Q&A examples | P1 |
| `quiz-generator` | Generate Bloom's-aligned quiz questions | P1 |
| `course-publisher` | Export course in multiple formats | P1 |
| `quality-reviewer` | Automated course quality verification | P1 |
| `gap-analyzer` | Identify uncovered concepts from source | P2 |

### CN: openclaw/hermesclaw 需要的 Skill

| Skill | 用途 | 优先级 |
|---|---|---|
| `transcript-recorder` | 实时捕获结构化 Expert-Novice 对话 | P0 |
| `concept-extractor` | 从对话中提取概念和关系 | P0 |
| `course-structurer` | 将概念组织为模块/章节/课时 | P0 |
| `exercise-generator` | 从问答示例生成练习题 | P1 |
| `quiz-generator` | 生成布鲁姆分类对齐的测验题 | P1 |
| `course-publisher` | 多格式导出课程 | P1 |
| `quality-reviewer` | 自动化课程质量验证 | P1 |
| `gap-analyzer` | 识别源材料中未覆盖的概念 | P2 |

> **Full technical details**: See `qa-to-course-research.md` for complete schemas, pipeline architecture, prompt templates, and integration design.
>
> **完整技术细节**：完整的 Schema、流水线架构、Prompt 模板和集成设计请参见 `qa-to-course-research.md`。

---

## Part 2: Top 20 GitHub Repos for AI-Assisted Learning & Course Generation
## 第二部分：AI 辅助学习与课程生成 Top 20 GitHub 仓库

### Tier 1: High Relevance + High Stars / 高相关 + 高星标

| # | Repo | Stars | Description (EN) | 描述（中文） | Relevance / 相关性 |
|---|------|-------|-------------------|-------------|-------------------|
| 1 | [JushBJJ/Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | ~29.6k | GPT-4 AI Tutor with customizable learning styles, Socratic dialogue, curriculum generation | GPT-4 AI 导师，支持自定义学习风格、苏格拉底对话、课程生成 | Most starred AI tutor. Models expert-novice paradigm with adaptive depth |
| 2 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | ~110k | 21 lessons for building with Generative AI | 21 节生成式 AI 入门课程 | Reference architecture for structured AI educational content |
| 3 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | ~47k | 12-week, 24-lesson AI curriculum with quizzes and assignments | 12 周 24 节 AI 课程，含测验和作业 | Demonstrates structured curriculum design at scale |
| 4 | [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en) | ~28.7k | Interactive deep learning book with code, math, and discussions | 交互式深度学习书，含代码、数学和讨论 | Jupyter-based model for knowledge-to-interactive-content conversion |
| 5 | [fastai/fastbook](https://github.com/fastai/fastbook) | ~24.9k | The fast.ai deep learning book (open source) | fast.ai 深度学习开源教材 | Expert-to-novice knowledge transfer via structured interactive content |
| 6 | [microsoft/ai-edu](https://github.com/microsoft/ai-edu) | ~14.1k | AI education materials for students, teachers, IT professionals | 面向学生、教师、IT 从业者的 AI 教育资源 | Demonstrates multi-level learning path organization |
| 7 | [microsoft/AI-System](https://github.com/microsoft/AI-System) | ~4.3k | AI System education resource | AI 系统设计教育资源 | Shows complex knowledge decomposition into structured modules |

### Tier 2: Directly Relevant to AI Tutoring / Course Generation / 直接相关

| # | Repo | Stars | Description (EN) | 描述（中文） | Relevance / 相关性 |
|---|------|-------|-------------------|-------------|-------------------|
| 8 | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | ~997 | Visual and Interactive AI Tutor | 可视化交互式 AI 导师 | Conversational AI tutor with knowledge graph visualization |
| 9 | [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | ~900 | AI tutor powered by Theory-of-Mind reasoning | 基于"心智理论"推理的 AI 导师 | ToM-based student modeling for adaptive learning |
| 10 | [thiswillbeyourgithub/AnkiAIUtils](https://github.com/thiwillbeyourgithub/AnkiAIUtils) | ~847 | AI-powered Anki flashcard tools with explanations and mnemonics | AI 驱动的 Anki 记忆卡片工具 | Pipeline: extract knowledge → generate educational artifacts |
| 11 | [luban-agi/Awesome-AIGC-Tutorials](https://github.com/luban-agi/Awesome-AIGC-Tutorials) | ~4.5k | Curated AIGC tutorials and resources | 精选 AIGC 教程和资源 | Demonstrates educational content curation at scale |
| 12 | [riiid/ednet](https://github.com/riiid/ednet) | ~366 | 131M+ AI tutoring interactions dataset | 1.31 亿次 AI 辅导交互数据集 | Largest open dataset for modeling conversational learning |
| 13 | [towardsai/ai-tutor-rag-system](https://github.com/towardsai/ai-tutor-rag-system) | ~232 | RAG-based tutoring system for LLM courses | 基于 RAG 的 LLM 课程辅导系统 | RAG + course content = interactive Q&A tutoring |
| 14 | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | ~194 | Open Source Intelligent Tutoring System with BKT | 开源智能辅导系统（贝叶斯知识追踪） | Most complete open-source ITS with adaptive problem selection |
| 15 | [THU-KEG/MOOCCubeX](https://github.com/THU-KEG/MOOCCubeX) | ~171 | Large-scale knowledge repository for MOOCs | 大规模 MOOC 知识库 | Knowledge graph framework for structuring course content |

### Tier 3: Emerging / Specialized / 新兴 / 专门项目

| # | Repo | Stars | Description (EN) | 描述（中文） | Relevance / 相关性 |
|---|------|-------|-------------------|-------------|-------------------|
| 16 | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | ~66 | Multi-agent framework for goal-oriented learning (WWW 2025) | 面向目标学习的多智能体框架（WWW 2025） | Published research: multi-agent orchestration for learning |
| 17 | [TochusC/ai-assistant-teaching-website](https://github.com/TochusC/ai-assistant-teaching-website) | ~79 | LLM-powered teaching website with AI assistant | LLM 驱动的智能教学网站 | Complete teaching platform with AI assistant integration |
| 18 | [Haozhe-Xing/agent_learning](https://github.com/Haozhe-Xing/agent_learning) | ~118 | Learn AI Agent Development with daily arXiv tracking | AI Agent 开发教程，含每日 arXiv 追踪 | Automated knowledge curation and learning path generation |
| 19 | [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion) | ~86 | Trinity K12 AI Education Companion System | K12 AI 教育陪伴系统 | Expert-novice learning paradigm for K12 |
| 20 | [studyield/studyield](https://github.com/studyield/studyield) | ~19 | Open-source AI learning platform with teach-back evaluation | 开源 AI 学习平台，含"反向教学"评估 | Most directly relevant: teach-back + multi-agent + knowledge graphs |

### Honorable Mentions / 荣誉提名

| Repo | Stars | Key Relevance / 关键相关性 |
|------|-------|--------------------------|
| [tobyilee/course-builder](https://github.com/tobyilee/course-builder) | 10 | Multi-agent → complete courses (slides + notes + quiz + TTS). 多智能体生成完整课程 |
| [bhataasim1/ai-course-generator](https://github.com/bhataasim1/ai-course-generator) | 47 | Gemini-powered course structure generation. Gemini 驱动课程结构生成 |
| [kongfoo-ai/internTA](https://github.com/kongfoo-ai/internTA) | 27 | Multi-agent AI TA that learns from limited data. 从少量数据学习的多智能体 AI 助教 |
| [run-llama/study-llama](https://github.com/run-llama/study-llama) | 23 | AI studying companion powered by LlamaCloud. LlamaCloud 驱动的 AI 学习伴侣 |
| [miuuyy/Clew](https://github.com/miuuyy/Clew) | 19 | AI agent: goals → dependency graphs (generative roadmap). 目标转依赖图的 AI 代理 |
| [arun3676/ai-learning-path-generator](https://github.com/arun3676/ai-learning-path-generator) | 20 | RAG + adaptive path generation. RAG + 自适应学习路径生成 |
| [StudyDrift/lextures](https://github.com/StudyDrift/lextures) | 56 | "First truly adaptive learning environment". "首个真正自适应学习环境" |
| [jaluoma/pruju-ai](https://github.com/jaluoma/pruju-ai) | 55 | AI TA: students interact with teacher's materials. AI 助教：学生与教师材料交互 |

---

## Key Takeaways / 关键发现

### EN

1. **No single repo does "conversation-to-course" end-to-end.** This is a gap in the market. The closest are `tobyilee/course-builder` (topic-to-course) and `studyield/studyield` (teach-back evaluation).

2. **The most mature pattern** is AI tutoring (Mr. Ranedeer, ChatTutor, tutor-gpt), where LLMs act as adaptive Socratic tutors. These capture Q&A interaction but do not convert it into structured courses.

3. **The "learning from interaction" pattern** is emerging in research: `gen-mentor` (WWW 2025), `internTA`, and `riiid/ednet` dataset.

4. **Course generation tools** generate from topics/prompts, but none yet generate courses from recorded Q&A conversations with an expert.

5. **Knowledge graph approaches** (MOOCCubeX, studyield, Clew) provide the structured representation layer needed to organize extracted knowledge into course structures.

### CN

1. **目前没有单一仓库实现端到端的"对话转课程"。** 这是一个市场空白。最接近的是 `tobyilee/course-builder`（主题转课程）和 `studyield/studyield`（反向教学评估）。

2. **最成熟的模式**是 AI 辅导（Mr. Ranedeer、ChatTutor、tutor-gpt），LLM 作为自适应苏格拉底式导师。这些系统捕获了问答交互，但尚未将其转化为结构化课程。

3. **"从交互中学习"模式**正在研究中兴起：`gen-mentor`（WWW 2025）、`internTA` 和 `riiid/ednet` 数据集。

4. **课程生成工具**从主题/Prompt 生成课程，但尚无工具能从与专家的问答对话中生成课程。

5. **知识图谱方法**（MOOCCubeX、studyield、Clew）提供了将提取的知识组织成课程结构所需的结构化表示层。

---

## Recommended Next Steps / 建议的后续步骤

### EN

1. **Build `transcript-recorder` skill first** — without capture, nothing else works
2. **Prototype with `studyield` and `course-builder`** — they are the closest existing implementations
3. **Use `Mr.-Ranedeer-AI-Tutor` prompt patterns** — proven Socratic tutoring methodology
4. **Reference `d2l-en` and `fastbook`** for output format — they demonstrate gold-standard educational content structure
5. **Consider contributing to existing repos** rather than building from scratch

### CN

1. **首先构建 `transcript-recorder` skill** — 没有捕获，其他都无法进行
2. **用 `studyield` 和 `course-builder` 做原型** — 它们是最接近的现有实现
3. **参考 `Mr.-Ranedeer-AI-Tutor` 的 Prompt 模式** — 经过验证的苏格拉底教学法
4. **参考 `d2l-en` 和 `fastbook` 的输出格式** — 它们展示了黄金标准的教育内容结构
5. **考虑为现有仓库贡献代码**，而不是从零开始构建

---

*Full technical report: `tasks/analysis/learning-mode/qa-to-course-research.md`*
