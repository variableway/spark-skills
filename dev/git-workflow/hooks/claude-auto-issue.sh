#!/bin/bash
# Claude Code Hook: Auto-suggest git-workflow when task execution is detected.
# Install: add to .claude/settings.json under hooks.UserPromptSubmit
#
# Input (stdin JSON): { "prompt": "...", ... }
# Output: additional context JSON appended to conversation, or silent exit.

read -r JSON 2>/dev/null || exit 0

# Extract the prompt text
PROMPT=$(echo "$JSON" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('prompt', ''))
except:
    print('')
" 2>/dev/null)

if [ -z "$PROMPT" ]; then
    exit 0
fi

# Detect task execution patterns in multiple languages
# Patterns: "execute task", "执行任务", "执行 Task", "run task", "implement task",
#           "Task N:", "Task N ", "complete task", "完成任务"
MATCH=$(echo "$PROMPT" | python3 -c "
import sys, re
prompt = sys.stdin.read().lower()
patterns = [
    r'执行\s*(task|任务)',
    r'execute\s*(task|任务)',
    r'run\s*task',
    r'implement\s*task',
    r'complete\s*task',
    r'完成任务',
    r'task\s*\d+[\s:]',
    r'@tasks[/\\\\]',
    r'please\s+(execute|run|do|complete)\s+task',
]
for p in patterns:
    if re.search(p, prompt):
        print('match')
        break
" 2>/dev/null)

if [ "$MATCH" != "match" ]; then
    exit 0
fi

# Output additional context telling Claude to use git-workflow
cat <<'CTX'
{"additionalContext": "IMPORTANT: The user is asking to execute a task. You MUST use the git-workflow skill for this. Follow these steps:\n1. Run INIT: python scripts/orchestrate.py init --title \"<task title>\" --description \"<task description>\"\n2. IMPLEMENT: Execute the actual task work\n3. Run FINISH: python scripts/orchestrate.py finish --message \"<completion summary>\"\nThis creates a GitHub Issue, tracks the work, and closes the issue automatically."}
CTX
