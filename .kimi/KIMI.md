# Kimi CLI - Project Instructions

This project uses GitHub Task Workflow for task execution.

## Auto-Workflow Trigger

When the user asks you to "execute", "run", "implement", or "work on" a task file (e.g., `tasks/*.md`), you **MUST** follow the **GitHub Task Workflow** defined in `github-task-workflow/SKILL.md`.

### Workflow Steps

1. **READ**: Read the task file and extract title/body
2. **CREATE ISSUE**: Run `python github-task-workflow/scripts/orchestrate.py init <task-file>`
3. **IMPLEMENT**: Execute the task, make code changes, run tests
4. **UPDATE ISSUE**: Run `python github-task-workflow/scripts/orchestrate.py finish`
5. **COMMIT**: Orchestrator handles git commit/push

### Available Skills

| Skill | Description | Use When |
|-------|-------------|----------|
| github-task-workflow | Full GitHub integration | Default for most tasks |
| local-workflow | Local-only tracing | User explicitly requests no GitHub |

### Rules

1. **Always use workflow** when user mentions task files
2. **Never skip steps** - always create Issue before implementing
3. **Use local-workflow** only when user explicitly says "use local workflow" or "no GitHub"
4. **Both workflows save local tracing** - local-workflow saves to `tasks/tracing/`, github-workflow saves to `tracing/`

## Task File Format

Task files are markdown files in `tasks/` directory:
- First line (without `# `) = Issue title
- Full content = Issue body
- Can contain multiple tasks (Task 1, Task 2, etc.)
