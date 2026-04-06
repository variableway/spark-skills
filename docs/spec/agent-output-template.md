# AI Agent Output Template

This template helps AI Agents produce structured output that can be automatically captured by the workflow system.

## Quick Start

When executing a task, write your output to `.task-output.md` in this format:

```markdown
## Task Execution Summary

### Understanding
[Your interpretation of what the task requires]

### Actions Taken
1. [First action you took]
2. [Second action you took]
3. ...

### Files Modified
| File | Changes |
|------|---------|
| `path/to/file1` | [brief description] |
| `path/to/file2` | [brief description] |

### Results
- **Status**: ✅ Completed / ❌ Failed / ⚠️ Partial
- **Tests**: [test results if applicable]
- **Issues Encountered**: [any problems and how you solved them]

### Reflection
[What worked well, what could be improved next time]
```

## Environment Variables

The workflow system sets these environment variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `TASK_WORKFLOW_MODE` | `local` or `github` | Current workflow mode |
| `TASK_FILE` | `tasks/xxx.md` | Path to task file |
| `TASK_ID` | `local-20260406-xxx` | Unique task ID |
| `TASK_CAPTURE_OUTPUT` | `true` | Whether to capture output |
| `TASK_OUTPUT_FILE` | `.task-output.md` | Where to write output |

## Example Output

### Example 1: Feature Implementation

```markdown
## Task Execution Summary

### Understanding
Implement a user authentication system using JWT tokens. The task requires:
- Login endpoint with email/password
- Token generation and validation
- Protected route middleware

### Actions Taken
1. Read existing codebase to understand project structure
2. Created `src/auth/jwt.py` for token generation/validation
3. Created `src/auth/middleware.py` for route protection
4. Updated `src/routes/login.py` with JWT integration
5. Added tests in `tests/test_auth.py`

### Files Modified
| File | Changes |
|------|---------|
| `src/auth/jwt.py` | New file - JWT token handling |
| `src/auth/middleware.py` | New file - auth middleware |
| `src/routes/login.py` | Modified - added JWT login |
| `tests/test_auth.py` | New file - unit tests |

### Results
- **Status**: ✅ Completed
- **Tests**: 5/5 passed
- **Coverage**: 92% of new code

### Reflection
The implementation went smoothly. Using PyJWT library simplified token handling. 
Next time could add refresh token mechanism.
```

### Example 2: Bug Fix

```markdown
## Task Execution Summary

### Understanding
Fix the memory leak in the data processing pipeline. The issue was reported 
in production where memory usage grows indefinitely during batch processing.

### Actions Taken
1. Analyzed memory usage patterns with memory_profiler
2. Identified unclosed file handles in `src/processing/batch.py`
3. Added context managers (`with` statements) for file operations
4. Added explicit cleanup for large data structures
5. Verified fix with stress test (10k batches)

### Files Modified
| File | Changes |
|------|---------|
| `src/processing/batch.py` | Fixed file handle leaks, added cleanup |
| `tests/test_batch_memory.py` | New file - memory leak regression test |

### Results
- **Status**: ✅ Completed
- **Memory Before**: ~2GB after 10k batches
- **Memory After**: ~150MB after 10k batches
- **Tests**: New regression test passes

### Issues Encountered
- Initial fix didn't cover all code paths
- Had to refactor two additional functions to use generators

### Reflection
Memory leaks are tricky. Should add memory profiling to CI pipeline to catch 
similar issues early.
```

## For Workflow Developers

### Python Helper Function

```python
def write_task_output(understanding, actions, files, results, reflection=""):
    """Write structured output for workflow capture."""
    import os
    from datetime import datetime
    
    output_file = os.getenv("TASK_OUTPUT_FILE", ".task-output.md")
    
    content = f"""## Task Execution Summary

### Understanding
{understanding}

### Actions Taken
{format_actions(actions)}

### Files Modified
{format_files(files)}

### Results
{format_results(results)}
"""
    if reflection:
        content += f"\n### Reflection\n{reflection}\n"
    
    with open(output_file, "w") as f:
        f.write(content)
    
    print(f"Task output written to: {output_file}")


def format_actions(actions):
    return "\n".join(f"{i+1}. {action}" for i, action in enumerate(actions))


def format_files(files):
    lines = ["| File | Changes |", "|------|---------|"]
    for f in files:
        lines.append(f"| `{f['path']}` | {f['desc']} |")
    return "\n".join(lines)


def format_results(results):
    lines = [f"- **Status**: {results.get('status', 'Unknown')}"]
    if 'tests' in results:
        lines.append(f"- **Tests**: {results['tests']}")
    if 'issues' in results:
        lines.append(f"- **Issues**: {results['issues']}")
    return "\n".join(lines)
```

### Usage Example

```python
write_task_output(
    understanding="Implement JWT authentication",
    actions=[
        "Created jwt.py for token handling",
        "Created middleware.py for auth protection",
        "Updated login routes"
    ],
    files=[
        {"path": "src/auth/jwt.py", "desc": "New file"},
        {"path": "src/auth/middleware.py", "desc": "New file"}
    ],
    results={
        "status": "✅ Completed",
        "tests": "5/5 passed"
    },
    reflection="Implementation went smoothly"
)
```

## Integration with Workflow

When you run:

```bash
python local-workflow/scripts/orchestrate.py finish
```

The workflow system will:

1. Read `.task-output.md`
2. Append it to the tracing file
3. Include it in the git commit
4. Clean up the temporary file

This creates a complete audit trail of what the AI Agent did and why.
