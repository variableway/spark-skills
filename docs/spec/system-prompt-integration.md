# System Prompt Integration Guide

## Problem

The AI Agent Protocol sets environment variables (`TASK_OUTPUT_FILE`, etc.), but AI Agents (Claude Code, Kimi CLI) **do not automatically recognize them**.

## Solution

Inject instructions into the AI Agent's system prompt to make it aware of the protocol.

## How System Prompts Work

### Claude Code

Claude Code reads `.claude/CLAUDE.md` or `.claude/settings.json`:

```json
{
  "system_prompt": "When executing tasks..."
}
```

### Kimi CLI

Kimi CLI can use `--agent-file` or project-level `.kimi/KIMI.md`.

### Universal Pattern

```markdown
# AI Agent Workflow Instructions

When you complete a task execution, follow this protocol:

## Environment Variables

Check these environment variables:
- `TASK_CAPTURE_OUTPUT` - If "true", write structured output
- `TASK_OUTPUT_FILE` - Path to write output (e.g., ".task-output.md")
- `TASK_WORKFLOW_MODE` - "local" or "github"

## Output Format

If `TASK_CAPTURE_OUTPUT=true`, write to `TASK_OUTPUT_FILE`:

```markdown
## Task Execution Summary

### Understanding
[Your understanding of the task]

### Actions Taken
1. [Action 1]
2. [Action 2]

### Files Modified
- `file/path` - [description]

### Results
- **Status**: ✅ Completed
- **Notes**: [any important notes]
```

## Example

```bash
# User asks
"Execute tasks/login.md"

# Your actions:
1. Read tasks/login.md
2. Implement the task
3. Write summary to .task-output.md (if TASK_CAPTURE_OUTPUT=true)
4. Report completion to user
```

## Implementation

### For Claude Code

Create `.claude/CLAUDE.md`:

```markdown
# Task Workflow Protocol

When executing task files (tasks/*.md), you MUST follow this protocol:

1. Read the task file
2. Execute the implementation
3. Check environment variables:
   - If `TASK_CAPTURE_OUTPUT=true`, write structured output to `TASK_OUTPUT_FILE`
4. Report completion

### Output Format

Write to `$TASK_OUTPUT_FILE`:

```markdown
## Task Execution Summary

### Understanding
...

### Actions Taken
...

### Files Modified
...

### Results
- **Status**: ✅ Completed
```
```

### For Kimi CLI

Create `.kimi/KIMI.md`:

```markdown
# Kimi Task Workflow

When executing tasks/*.md files:

## Protocol

1. Check environment variables
2. Execute task
3. If TASK_CAPTURE_OUTPUT=true, write to TASK_OUTPUT_FILE
4. Finish

## Environment Variables Reference

| Variable | Meaning |
|----------|---------|
| TASK_CAPTURE_OUTPUT | Whether to capture output |
| TASK_OUTPUT_FILE | Where to write output |
| TASK_WORKFLOW_MODE | "local" or "github" |
```

## Automated Injection

### Option 1: Wrapper Script

Create a wrapper that sets env vars and prepends instructions:

```bash
#!/bin/bash
# workflow-run.sh

export TASK_CAPTURE_OUTPUT=true
export TASK_OUTPUT_FILE=".task-output.md"
export TASK_FILE="$1"

# Prepend protocol instructions to system prompt
SYSTEM_PROMPT="$PWD/.kimi/KIMI.md"

kimi --system-prompt "$SYSTEM_PROMPT" "Execute $TASK_FILE"

# After execution, capture output
python local-workflow/scripts/orchestrate.py finish
```

### Option 2: Modified Orchestrator

Modify orchestrate.py to automatically inject instructions:

```python
def cmd_init(args):
    # ... existing code ...
    
    # Inject system prompt
    inject_system_prompt()
    
    # Then invoke AI Agent
    invoke_ai_agent_with_prompt(
        task_file=args.task_file,
        system_prompt=PROTOCOL_INSTRUCTIONS
    )

def inject_system_prompt():
    """Inject protocol instructions into project."""
    kimi_prompt = Path(".kimi/KIMI.md")
    claude_prompt = Path(".claude/CLAUDE.md")
    
    protocol = """
# AI Agent Protocol

When executing tasks, check TASK_CAPTURE_OUTPUT and write to TASK_OUTPUT_FILE.
"""
    
    if not kimi_prompt.exists():
        kimi_prompt.parent.mkdir(parents=True, exist_ok=True)
        kimi_prompt.write_text(protocol)
    
    if not claude_prompt.exists():
        claude_prompt.parent.mkdir(parents=True, exist_ok=True)
        claude_prompt.write_text(protocol)
```

## Testing the Integration

### Test 1: Environment Variables

```bash
python local-workflow/scripts/orchestrate.py init tasks/test.md
echo "TASK_CAPTURE_OUTPUT=$TASK_CAPTURE_OUTPUT"
echo "TASK_OUTPUT_FILE=$TASK_OUTPUT_FILE"
```

### Test 2: System Prompt Injection

```bash
# Check if .kimi/KIMI.md was created
cat .kimi/KIMI.md
```

### Test 3: Full Workflow

```bash
# Initialize
python local-workflow/scripts/orchestrate.py init tasks/test.md

# AI Agent should now:
# 1. See the system prompt
# 2. Check environment variables
# 3. Write output to .task-output.md

# Check if file was created
ls -la .task-output.md

# Finish
python local-workflow/scripts/orchestrate.py finish
```

## Limitations

1. **Not Universal**: Each AI Agent has different system prompt mechanisms
2. **Requires Cooperation**: AI Agent must be programmed to check env vars
3. **Token Overhead**: System prompt consumes context window tokens

## Future Improvements

1. **Native Protocol Support**: Convince vendors to support standard protocol
2. **MCP Integration**: Use Model Context Protocol for structured communication
3. **Wrapper Libraries**: Create SDK that handles protocol automatically
