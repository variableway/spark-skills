# AI Dialogue-Based Learning Effectiveness: Experiment Design Guide

## Executive Summary

This document provides a concrete, step-by-step protocol for designing the simplest possible experiment to test whether AI dialogue-based learning (Socratic tutoring, expert-novice conversation) actually produces measurable learning gains. It synthesizes methodologies from published studies (Bastani 2024, Graesser's AutoTutor, Khan Academy's Khanmigo), established education research methods, and available tools/frameworks.

---

## Part 1: Concrete Step-by-Step Experiment Protocol

### The Minimal Viable Experiment (MVE)

The simplest valid experiment design is a **pre-test / post-test randomized controlled trial** with two conditions:

```
Group A (Treatment):   Pre-test --> AI Dialogue Tutoring Session(s) --> Post-test --> Delayed Post-test (optional)
Group B (Control):     Pre-test --> Self-study / Traditional Material --> Post-test --> Delayed Post-test (optional)
```

### Phase 0: Preparation (1-2 weeks)

1. **Choose a narrow, well-defined topic**
   - Must be specific enough to teach in 1-3 sessions
   - Must be testable with objective questions
   - Examples: "Newton's Third Law", "JavaScript closures", "Supply and demand equilibrium", "Photosynthesis"
   - Criteria: Can be assessed with 10-20 questions, has clear right/wrong answers

2. **Develop the assessment instrument (pre/post test)**
   - Create 15-20 questions covering the topic at multiple Bloom's taxonomy levels:
     - 5-6 questions: Remember/Understand (factual recall, definitions)
     - 5-6 questions: Apply/Analyze (use concepts in new situations, compare)
     - 3-4 questions: Evaluate/Create (justify reasoning, design solutions)
   - Create TWO equivalent versions (Form A, Form B) for counterbalancing
   - Pilot the test with 3-5 people not in the study to verify clarity and difficulty

3. **Prepare learning materials for both conditions**
   - Treatment: AI dialogue system with Socratic tutoring prompts (your AI tutor)
   - Control: Equivalent content presented as text/article or video (same factual content, no dialogue)
   - Ensure both cover the SAME knowledge points (content parity is critical)

4. **IRB / Ethics approval** (if required by your institution)
   - Informed consent form
   - Data handling plan
   - Right to withdraw

### Phase 1: Recruitment & Randomization

1. **Recruit participants**
   - Target: students or learners who are novices in the chosen topic
   - Screen for prior knowledge (exclude experts)
   - Minimum N depends on expected effect size (see Part 4 below)

2. **Random assignment**
   - Use a random number generator to assign each participant to Group A or Group B
   - Stratify if needed (e.g., ensure equal distribution of gender, prior GPA)

### Phase 2: Pre-test (Day 1)

1. Administer the pre-test (15-20 questions, 15-20 minutes)
2. Collect basic demographics: age, education level, prior experience with topic
3. **Do NOT reveal correct answers** after the pre-test

### Phase 3: Intervention (Day 1-2)

**Group A (AI Dialogue Treatment):**
- Participant engages with AI tutor for 30-45 minutes
- AI uses Socratic questioning, never gives direct answers
- Session is logged for later analysis
- Participant works through 3-5 target problems/concepts

**Group B (Control - Self-Study):**
- Participant reads equivalent study material for 30-45 minutes
- Same factual content, no interactive dialogue
- Can take notes

### Phase 4: Immediate Post-test (same session or next day)

1. Administer post-test (same or parallel form)
2. Optional: administer a **transfer test** (novel problems requiring same concepts)
3. Collect subjective feedback: "How confident do you feel about this topic?" (Likert 1-5)

### Phase 5: Delayed Post-test (7-14 days later, optional but recommended)

1. Re-administer test without prior notice
2. Measures retention and deeper learning
3. This is where AI dialogue learning often shows its strongest advantage

### Phase 6: Analysis

See Part 5 below for detailed analysis plan.

---

## Part 2: What to Measure and How

### Primary Outcome Measures

| Measure | What It Captures | How to Calculate |
|---------|-----------------|-----------------|
| **Raw Learning Gain** | Absolute improvement | Post-test score - Pre-test score |
| **Normalized Learning Gain (Hake gain)** | Proportion of possible improvement achieved | (Post - Pre) / (Max - Pre) |
| **Effect Size (Cohen's d)** | Standardized magnitude of difference | (Mean_treatment - Mean_control) / Pooled_SD |
| **Retention Rate** | How much learning persists | Delayed-post / Immediate-post ratio |

### Secondary Outcome Measures

| Measure | What It Captures | How to Measure |
|---------|-----------------|---------------|
| **Time on task** | Efficiency | Log timestamps |
| **Confidence calibration** | Metacognition | Pre/post confidence ratings vs. actual scores |
| **Transfer score** | Deep understanding | Novel problem post-test |
| **Engagement** | Subjective experience | Likert scale survey |
| **Dialogue quality** (treatment only) | Socratic interaction depth | Code dialogues for question types, explanation depth |

### Bloom's Taxonomy Assessment Matrix

Design your test to measure at each level:

```
Level 1 - Remember:   "What is the definition of X?"
Level 2 - Understand: "Explain X in your own words."
Level 3 - Apply:      "Solve this new problem using X."
Level 4 - Analyze:    "Compare X and Y. How are they different?"
Level 5 - Evaluate:   "Which approach is better and why?"
Level 6 - Create:     "Design a solution for this novel scenario."
```

Track gains at each level separately. AI dialogue tutoring often shows the largest gains at levels 3-6 (deeper learning), while rote study may show similar gains at levels 1-2.

### Measurement Formulas

**Normalized Gain (Hake, 1998):**
```
g = (Post% - Pre%) / (100% - Pre%)

Interpretation:
  g >= 0.7  = High gain (interactive engagement)
  0.3-0.7  = Medium gain
  g < 0.3  = Low gain (traditional instruction)
```

**Cohen's d:**
```
d = (M1 - M2) / SD_pooled

Interpretation:
  d = 0.2  = Small effect
  d = 0.5  = Medium effect
  d = 0.8  = Large effect
```

---

## Part 3: Minimum Sample Size

### Power Analysis Reference Table

For a two-group between-subjects design (alpha = 0.05, power = 0.80):

| Expected Effect Size | Cohen's d | Minimum N per group | Total N |
|---------------------|-----------|--------------------|---------|
| Very Small | 0.2 | 394 | 788 |
| Small | 0.3 | 176 | 352 |
| Medium | 0.5 | 64 | 128 |
| Large | 0.8 | 26 | 52 |

### What Effect Size to Expect for AI Tutoring

Based on the literature:
- **One-on-one human tutoring**: d = 0.6-2.0 (Bloom's 2-sigma problem)
- **Intelligent tutoring systems (ITS)**: d = 0.3-1.0
- **AI chatbot/LLM tutoring**: d = 0.2-0.8 (highly variable, depends on design)
- **Bastani 2024 finding**: AI tutor IMPROVED practice scores (+48%) but HARMED exam scores (-17%) -- negative effect, d approximately -0.3 to -0.5

### Recommended Starting Point

**For a pilot/proof-of-concept study:**
- Target **N = 30-50 total** (15-25 per group) -- enough for a medium-to-large effect
- Use this to estimate the actual effect size for your specific intervention
- Then run a properly powered follow-up study

**For a publishable study:**
- Use G*Power (free) to calculate exact sample size based on pilot effect size
- Target **N = 100-200 total** for medium effects
- Add 15-20% buffer for attrition

### Within-Subject vs. Between-Subject

| Design | Min N | Pros | Cons |
|--------|-------|------|------|
| **Between-subjects** | Larger (~64/group for d=0.5) | No carryover; cleaner causal inference | Needs more participants |
| **Within-subject (crossover)** | Smaller (~34 total for d=0.5) | Fewer participants; controls individual differences | Learning carryover between conditions |
| **Mixed (recommended)** | ~50-100 total | Pre/post within + treatment between | Best of both worlds |

**Recommendation:** Use the **mixed design** (all participants take pre+post test, randomized to treatment or control). This is the standard in education research and gives you ANCOVA statistical power advantages.

---

## Part 4: How to Analyze Results

### Statistical Analysis Plan

#### Step 1: Descriptive Statistics
```
For each group, report:
- Mean pre-test score (SD)
- Mean post-test score (SD)
- Mean gain score (SD)
- Normalized gain
- Effect size (Cohen's d)
```

#### Step 2: Check Assumptions
- Normality: Shapiro-Wilk test on gain scores
- Homogeneity of variance: Levene's test
- If violated, use non-parametric alternatives (Mann-Whitney U)

#### Step 3: Primary Analysis

**Option A: ANCOVA (Recommended)**
```python
# Using statsmodels or similar
# DV: post-test score
# IV: group (treatment vs control)
# Covariate: pre-test score
from statsmodels.formula.api import ols
model = ols('post_test ~ group + pre_test', data=df).fit()
```
ANCOVA is preferred because:
- Controls for pre-existing differences
- Increases statistical power
- Standard in education research

**Option B: Independent t-test on gain scores**
```python
from scipy import stats
treatment_gains = df[df.group=='treatment']['gain']
control_gains = df[df.group=='control']['gain']
t_stat, p_value = stats.ttest_ind(treatment_gains, control_gains)
```

**Option C: Mixed ANOVA (if you have delayed post-test)**
```python
# Within: time (pre, post, delayed)
# Between: group (treatment, control)
```

#### Step 4: Effect Size
```python
import numpy as np
def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_sd = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_sd
```

#### Step 5: Bloom's Level Breakdown
Analyze gains separately at each taxonomy level to determine WHERE the AI dialogue tutoring helps most.

### What Results to Report

```
1. Descriptive table (means, SDs for each group x time)
2. ANCOVA results (F-statistic, p-value, partial eta-squared)
3. Effect size (Cohen's d with 95% CI)
4. Normalized learning gain per group
5. Bloom's level analysis (gains by cognitive level)
6. (If applicable) Retention analysis from delayed post-test
7. (If applicable) Dialogue analysis: correlation between Socratic moves and learning gains
```

---

## Part 5: Tools, Templates, and Frameworks

### Power Analysis Tools

| Tool | URL | Cost | Notes |
|------|-----|------|-------|
| **G*Power** | https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower | Free | Gold standard; desktop app (Windows/Mac) |
| **PowerUp!** | https://www.powerup.ph | Free | Designed for multilevel education studies |
| **WebPower** | https://webpower.psychstat.org | Free (web) | Online power analysis |

### Experiment Frameworks (A/B Testing for Education)

| Framework | URL / Source | Notes |
|-----------|-------------|-------|
| **UpGrade** | GitHub (CMU) | Open-source A/B testing for ed-tech; from Carnegie Mellon's LearnLab |
| **ASSISTments E-TRIALS** | https://assistments.org | Built-in experiment framework; run RCTs in real math classrooms |
| **PlanOut** | GitHub (facebookarchive/PlanOut) | General-purpose field experiment framework (Python); by Facebook Research |
| **GrowthBook** | https://github.com/growthbook/growthbook | Open-source feature flagging + A/B testing |

### Statistical Analysis Tools

| Tool | Notes |
|------|-------|
| **R + lme4 package** | Free; best for mixed-effects models in education data |
| **Python (scipy, statsmodels)** | Free; good for t-tests, ANOVA, ANCOVA, regression |
| **JASP** | Free; user-friendly GUI for Bayesian and frequentist analysis |
| **jamovi** | Free; spreadsheet-based statistical analysis |

### Templates

A minimal experiment needs these documents:

1. **Pre/Post Test** -- 15-20 questions, Bloom's-leveled
2. **Consent Form** -- Standard IRB template
3. **Demographics Survey** -- Age, education, prior knowledge
4. **Session Log Template** -- Timestamps, condition, duration
5. **Confidence Survey** -- Pre/post self-assessment
6. **Data Analysis Script** -- Python/R template for ANCOVA

---

## Part 6: Key Lessons from Published Studies

### Bastani et al. (2024) -- "Generative AI Can Harm Learning"

**Study Design:**
- RCT in a Turkish high school, mathematics
- ~1,000 students across multiple classrooms
- 3 conditions: (1) AI tutor (GPT-4 based, guided), (2) standard GPT-4 chatbot, (3) control (no AI)
- Pre-test, practice sessions, exam (post-test)

**Key Finding -- The Paradox:**
- AI tutor group: practice scores +48% BUT exam scores -17% vs. control
- Students outsourced thinking to AI, creating an "illusion of learning"
- The AI did the cognitive work instead of scaffolding the student to do it

**Critical Lesson for Your Experiment:**
- DO NOT measure only practice performance -- always measure independent performance (exam/test without AI)
- Design your AI tutor to use Socratic questioning (not giving answers)
- Include a delayed post-test to measure actual retention
- Track HOW students use the AI (do they ask for answers or engage in reasoning?)

### Graesser's AutoTutor Studies (1999-2015)

**Study Design:**
- Pre-test / post-test, 3 conditions: AutoTutor, human tutor, read-only control
- Topics: computer literacy, physics, biology
- 30-45 minute sessions per topic
- Both shallow and deep knowledge questions

**Key Findings:**
- AutoTutor produced d = 0.5-1.5 sigma gains over baseline
- Comparable to novice/average human tutors
- Largest gains on deep reasoning questions (Bloom's levels 3-6)
- The 5-step dialogue frame was key: (1) main question, (2) student answer, (3) feedback, (4) Socratic scaffolding, (5) summary

**Critical Lesson for Your Experiment:**
- Use a structured dialogue protocol (not free-form chat)
- Measure shallow AND deep knowledge separately
- 30-45 minutes is a viable session length

### Chi et al. (2001) -- Self-Explanation and Tutoring

**Key Insight:**
- The act of EXPLAINING (not just receiving information) drives learning
- "Tutee" benefit: students who teach/explain learn more than those who listen
- This is the theoretical basis for Socratic AI tutoring

---

## Part 7: Quick-Start Checklist

For the absolute simplest experiment (can be run in 1-2 weeks):

- [ ] Pick ONE narrow topic (e.g., "How JavaScript closures work")
- [ ] Write a 15-question pre/post test (5 recall, 5 application, 5 analysis)
- [ ] Prepare AI dialogue prompt/system instructions (Socratic mode)
- [ ] Prepare control material (same content, text format)
- [ ] Recruit 30-50 participants (classmates, colleagues, online volunteers)
- [ ] Randomize into 2 groups
- [ ] Run pre-test (15 min)
- [ ] Run intervention (30-45 min per person)
- [ ] Run post-test immediately after (15 min)
- [ ] Run delayed post-test 1 week later (optional but recommended)
- [ ] Analyze with ANCOVA or independent t-test on gain scores
- [ ] Calculate normalized gain and Cohen's d
- [ ] Report results with effect sizes and confidence intervals

---

## Key References

1. **Hake, R.R. (1998).** "Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses." *American Journal of Physics*, 66(1), 64-74. -- **Normalized gain methodology**

2. **Bastani, H., Bastani, O., Sungu, A., et al. (2024).** "Generative AI Can Harm Learning." *SSRN*. -- **RCT showing AI can harm learning if designed poorly**

3. **Graesser, A.C., et al. (1999).** "AutoTutor: A simulation of a human tutor." *Cognitive Science Society Proceedings*. -- **Socratic dialogue tutoring protocol**

4. **Chi, M.T.H., et al. (2001).** "Why self-explanations improve learning." -- **Theoretical basis for dialogue-based learning**

5. **Cohen, J. (1988).** *Statistical Power Analysis for the Behavioral Sciences.* -- **Effect sizes and power analysis**

6. **Bloom, B.S. (1984).** "The 2 Sigma Problem: The Search for Methods of Group Instruction as Effective as One-to-One Tutoring." *Educational Researcher*. -- **Benchmark for tutoring effectiveness**

7. **Creswell, J.W.** *Educational Research: Planning, Conducting, and Evaluating Quantitative and Qualitative Research.* -- **General education research methodology**

8. **Campbell, D.T. & Stanley, J.C.** *Experimental and Quasi-Experimental Designs for Research.* -- **Experiment design foundations**
