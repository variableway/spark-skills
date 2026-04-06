# AI Agent Protocol for Task Workflow

## Overview

This document defines the protocol between AI Agents (Claude Code, Kimi, Codex, etc.) and the Task Workflow system. The protocol ensures consistent task execution, output capture, and tracing across all AI Agents.

## Core Concepts

### 1. Task Execution Lifecycle

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  READ   │ -> │  PARSE  │ -> │ EXECUTE │ -> │ CAPTURE │ -> │ RECORD  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
    │              │              │              │              │
    ▼              ▼              ▼              ▼              ▼
 Read task     Extract        AI Agent       Capture        Write to
 file          requirements   implements     output         tracing
               & intent                      & results
```

### 2. Agent Output Format

AI Agents SHOULD produce output in a structured format that can be captured and recorded:

```markdown
## Task Execution Summary

### Task Information
- **Task File**: `tasks/features/example.md`
- **Task ID**: local-20260406-abc123
- **Started At**: 2026-04-06 10:00:00
- **Completed At**: 2026-04-06 11:30:00

### Agent Understanding
[AI Agent's interpretation of the task requirements]

### Actions Taken
1. [Action 1 description]
2. [Action 2 description]
...

### Files Modified
- `path/to/file1` - [description of changes]
- `path/to/file2` - [description of changes]

### Execution Results
- **Status**: ✅ Success / ❌ Failed / ⚠️ Partial
- **Tests**: [test results if applicable]
- **Notes**: [any important notes]

### AI Agent Reflection
[What worked well, what could be improved]
```

## Protocol Specification

### 1. Task Parsing Protocol

When an AI Agent reads a task file, it MUST:

1. **Extract Metadata**
   ```yaml
   title: "First line without # prefix"
   body: "Full markdown content"
   requirements: "List of requirements/acceptance criteria"
   ```

2. **Parse Intent**
   - Identify the primary goal
   - Extract constraints and requirements
   - Note any specific technologies or approaches mentioned

3. **Generate Agent-Parsed Content**
   ```markdown
   ### Agent Parsed Content
   
   **Primary Goal**: [main objective]
   
   **Requirements**:
   - [requirement 1]
   - [requirement 2]
   
   **Approach**: [planned implementation approach]
   
   **Estimated Complexity**: [low/medium/high]
   ```

### 2. Output Capture Protocol

#### 2.1 Environment Variable Interface

The workflow system sets environment variables to guide AI Agents:

```bash
# Set by the workflow system before invoking AI Agent
export TASK_WORKFLOW_MODE="github"  # or "local"
export TASK_FILE="tasks/features/example.md"
export TASK_TRACING_DIR="tasks/tracing"
export TASK_CAPTURE_OUTPUT="true"
```

#### 2.2 Output Capture Methods

**Method A: File-based Capture (Recommended)**

AI Agent writes structured output to a designated file:

```python
# AI Agent writes to this file
OUTPUT_FILE = ".task-output.md"

with open(OUTPUT_FILE, "w") as f:
    f.write(generate_summary())
```

**Method B: Stdout with Markers**

AI Agent wraps output in special markers:

```markdown
<!-- TASK_OUTPUT_START -->
## Task Execution Summary
...
<!-- TASK_OUTPUT_END -->
```

**Method C: Function Call (for programmatic agents)**

```python
# AI Agent calls workflow API
workflow.record_output(
    task_file="tasks/example.md",
    summary="...",
    files_changed=[...],
    status="success"
)
```

### 3. Tracing Integration Protocol

#### 3.1 Automatic Tracing

When `TASK_CAPTURE_OUTPUT=true`, the workflow system:

1. Intercepts AI Agent output
2. Parses structured content
3. Appends to tracing file

#### 3.2 Tracing File Format

```markdown
# Tracing: example-task

## Task Entry (2026-04-06 10:00:00)

- **Task File**: `tasks/features/example.md`
- **Task ID**: local-20260406-abc123
- **Status**: completed
- **Started At**: 2026-04-06 10:00:00
- **Completed At**: 2026-04-06 11:30:00

### Original Task Content

[Original task content preserved]

### Agent Parsed Content

[AI Agent's interpretation]

### AI Agent Output

[Captured output from AI Agent execution]

### Execution Metadata

- **Agent Type**: kimi / claude-code / codex
- **Execution Time**: 90 minutes
- **Files Changed**: 5
- **Lines Changed**: +200/-50
```

## Implementation Guide

### For AI Agent Developers

1. **Support Environment Variables**
   ```python
   import os
   
   if os.getenv("TASK_CAPTURE_OUTPUT") == "true":
       output_file = os.getenv("TASK_OUTPUT_FILE", ".task-output.md")
       write_structured_output(output_file)
   ```

2. **Generate Structured Summary**
   ```python
   def generate_summary():
       return f"""## Task Execution Summary

### Actions Taken
{format_actions(actions)}

### Files Modified
{format_files(files)}

### Results
{format_results(results)}
"""
   ```

3. **Respect Workflow Mode**
   - In `github` mode: Expect GitHub Issue integration
   - In `local` mode: Only use local tracing

### For Workflow System Developers

1. **Set Environment Variables**
   ```bash
   export TASK_WORKFLOW_MODE="local"
   export TASK_FILE="$TASK_FILE"
   export TASK_CAPTURE_OUTPUT="true"
   export TASK_OUTPUT_FILE=".task-output.md"
   ```

2. **Capture and Record Output**
   ```python
   def capture_agent_output():
       if os.path.exists(".task-output.md"):
           content = read(".task-output.md")
           append_to_tracing(content)
           os.remove(".task-output.md")  # Clean up
   ```

## Example: Complete Workflow

### Step 1: Initialize Task

```bash
# User runs:
python local-workflow/scripts/orchestrate.py init tasks/feature.md

# System:
# 1. Creates tracing file
# 2. Sets environment variables
# 3. Prompts AI Agent
```

### Step 2: AI Agent Execution

```bash
# AI Agent receives prompt:
"Execute tasks/feature.md"

# AI Agent:
# 1. Reads task file
# 2. Parses requirements
# 3. Executes implementation
# 4. Writes .task-output.md
```

### Step 3: Capture and Record

```bash
# User runs:
python local-workflow/scripts/orchestrate.py finish

# System:
# 1. Reads .task-output.md
# 2. Appends to tracing file
# 3. Commits changes
# 4. Cleans up
```

## Future Extensions

### 1. Real-time Streaming

Capture AI Agent output in real-time:

```python
for chunk in agent.stream_output():
    tracing.append(chunk)
```

### 2. Multi-Agent Collaboration

```markdown
### Agent Collaboration

- **Primary Agent**: kimi (implementation)
- **Secondary Agents**: 
  - codex (code review)
  - claude-code (documentation)
```

### 3. Metrics and Analytics

```yaml
execution_metrics:
  time_total: 5400  # seconds
  time_thinking: 1200
  time_coding: 3000
  time_testing: 1200
  tokens_input: 15000
  tokens_output: 8000
  api_calls: 45
```

## References

- [local-workflow/SKILL.md](../../local-workflow/SKILL.md)
- [github-task-workflow/SKILL.md](../../github-task-workflow/SKILL.md)
