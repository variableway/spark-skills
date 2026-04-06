#!/usr/bin/env python3
"""Local Task Workflow 编排器 - 纯本地工作流，无需 GitHub。

用法：
    python orchestrate.py init tasks/login.md "使用 JWT 实现"
    python orchestrate.py status
    python orchestrate.py finish
    python orchestrate.py abort
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tracing import cmd_init as tracing_init, cmd_finish as tracing_finish


STATE_FILE = Path(".local-workflow.state.json")


class _TracingArgs:
    """Minimal args namespace for tracing calls."""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def cmd_init(args):
    task_path = Path(args.task_file)
    if not task_path.exists():
        print(f"Error: Task file not found: {task_path}", file=sys.stderr)
        sys.exit(1)

    if STATE_FILE.exists():
        old = json.loads(STATE_FILE.read_text())
        print(f"Warning: Existing workflow found for task '{old.get('title')}'. Abort it first if stale.", file=sys.stderr)

    # Initialize local tracing
    try:
        tracing_args = _TracingArgs(
            task=str(task_path),
            parsed=args.instructions or ""
        )
        task_id = tracing_init(tracing_args)
    except Exception as e:
        print(f"Tracing init error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"\nTask ID: {task_id}")
    print(f"State saved to: {STATE_FILE}")
    print("\n=== NEXT STEP ===")
    print("Please implement the task now.")
    print("After implementation, run: python local-workflow/scripts/orchestrate.py finish")


def cmd_status(_args):
    if not STATE_FILE.exists():
        print("No active local workflow found.")
        return

    state = json.loads(STATE_FILE.read_text())
    print(f"Active local workflow:")
    print(f"  Task ID:   {state.get('task_id', 'N/A')}")
    print(f"  Title:     {state.get('title', 'N/A')}")
    print(f"  Task file: {state.get('task_file', 'N/A')}")
    print(f"  Status:    {state.get('status', 'N/A')}")
    print(f"  Started:   {state.get('started_at', 'N/A')}")
    if state.get("completed_at"):
        print(f"  Completed: {state.get('completed_at')}")
    if state.get("instructions"):
        print(f"  Instructions: {state['instructions']}")
    if state.get("tracing_file"):
        print(f"  Tracing:   {state['tracing_file']}")


def cmd_finish(_args):
    if not STATE_FILE.exists():
        print("Error: No active workflow found. Run 'init' first.", file=sys.stderr)
        sys.exit(1)

    state = json.loads(STATE_FILE.read_text())
    task_file = state.get("task_file", "")

    # Gather git summary for the summary
    try:
        changed = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True, text=True, check=False
        ).stdout.strip()
    except Exception:
        changed = ""

    summary_lines = ["### Implementation Completed", ""]
    if state.get("instructions"):
        summary_lines.append(f"**Instructions**: {state['instructions']}")
        summary_lines.append("")
    if changed:
        summary_lines.append("**Files changed**:")
        for f in changed.split("\n"):
            if f.strip():
                summary_lines.append(f"- `{f}`")
    else:
        summary_lines.append("Task implementation is done.")

    summary = "\n".join(summary_lines)

    # Update local tracing
    try:
        tracing_args = _TracingArgs(
            task=task_file,
            summary=summary
        )
        tracing_finish(tracing_args)
        print(f"Tracing updated for task: {state.get('title', task_file)}")
    except Exception as e:
        print(f"Tracing finish warning: {e}")

    # Git commit and push
    task_title = state.get("title", "task")
    commit_message = f"Complete: {task_title}"
    
    try:
        subprocess.run(["git", "add", "-A"], check=False)
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            capture_output=True, text=True, check=False
        )
        push_result = subprocess.run(["git", "push"], capture_output=True, text=True, check=False)
        if push_result.returncode == 0:
            print("Code committed and pushed.")
        else:
            print("Commit created, but push may need attention.")
    except Exception as e:
        print(f"Git operation warning: {e}")

    # Clean up state file
    STATE_FILE.unlink()
    print("Local workflow complete.")


def cmd_abort(_args):
    if not STATE_FILE.exists():
        print("No active workflow to abort.")
        return

    state = json.loads(STATE_FILE.read_text())
    task_file = state.get("task_file", "")
    
    STATE_FILE.unlink()
    print(f"Aborted workflow for task: {state.get('title', task_file)}")


def main():
    parser = argparse.ArgumentParser(description="Local Task Workflow Orchestrator (No GitHub Required)")
    sub = parser.add_subparsers(dest="cmd", help="Available commands")

    p_init = sub.add_parser("init", help="Create local tracing from task file and save state")
    p_init.add_argument("task_file", help="Path to the task markdown file")
    p_init.add_argument("instructions", nargs="?", default="", help="Additional implementation instructions")

    sub.add_parser("status", help="Show active workflow state")
    sub.add_parser("finish", help="Update tracing with summary and push code")
    sub.add_parser("abort", help="Remove active workflow state without updating tracing")

    args = parser.parse_args()

    handlers = {
        "init": cmd_init,
        "status": cmd_status,
        "finish": cmd_finish,
        "abort": cmd_abort,
    }

    handler = handlers.get(args.cmd)
    if not handler:
        parser.print_help()
        sys.exit(1)

    handler(args)


if __name__ == "__main__":
    main()
