#!/usr/bin/env python3
"""Git Workflow Orchestrator — based on github-cli-skill.

Usage:
    python orchestrate.py init --title "Task Title" --description "Task desc" [--labels task]
    python orchestrate.py finish --message "Completion summary"
    python orchestrate.py status
    python orchestrate.py abort

Workflow:
    1. init  → Creates GitHub issue + first comment, saves state
    2. Agent executes task (with tests)
    3. finish → Appends completion message to first comment, closes issue
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
STATE_FILE = Path(".git-workflow.state.json")

sys.path.insert(0, str(SCRIPT_DIR))
from tracing import cmd_init as tracing_init, cmd_finish as tracing_finish


class _TracingArgs:
    """Minimal args namespace for tracing calls."""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def run_script(name: str, args_list: list) -> None:
    """Run a helper script in the same directory."""
    cmd = [sys.executable, str(SCRIPT_DIR / name)] + args_list
    subprocess.run(cmd, check=True)


def cmd_init(args):
    """Create issue from task description."""
    run_script("create_issue.py", [
        "--title", args.title,
        "--description", args.description,
        "--labels", args.labels,
    ] + (["--repo", args.repo] if args.repo else [])
      + (["--remote", args.remote] if args.remote else []))

    # Initialize local tracing
    try:
        state = json.loads(STATE_FILE.read_text())
        tracing_args = _TracingArgs(
            issue=state.get("issue"),
            title=state.get("title"),
            description=state.get("description"),
            parsed=args.instructions or ""
        )
        tracing_init(tracing_args)
    except Exception as e:
        print(f"Tracing init warning: {e}")

    print("\n=== NEXT STEP ===")
    print("Please implement the task and run tests.")
    print("After completion, run: python scripts/orchestrate.py finish --message '<summary>'")


def cmd_finish(args):
    """Close issue and append completion message to first comment."""
    if not STATE_FILE.exists() and not args.issue:
        print("Error: No active workflow found. Run 'init' first or provide --issue/--repo.", file=sys.stderr)
        sys.exit(1)

    # Read state BEFORE close_issue deletes it
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}

    cmd_args = ["--message", args.message]
    if args.issue:
        cmd_args += ["--issue", str(args.issue)]
    if args.repo:
        cmd_args += ["--repo", args.repo]

    run_script("close_issue.py", cmd_args)

    # Doc update check
    doc_message = ""
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "doc_checker.py"), "--markdown"],
            capture_output=True, text=True, check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            doc_message = "\n\n" + result.stdout.strip()
            print(doc_message.strip())
    except Exception:
        pass

    # Update local tracing
    try:
        tracing_args = _TracingArgs(
            issue=args.issue or state.get("issue"),
            title=state.get("title"),
            summary=args.message
        )
        tracing_finish(tracing_args)
    except Exception as e:
        print(f"Tracing finish warning: {e}")

    print("Workflow complete.")


def cmd_status(_args):
    """Show active workflow state."""
    if not STATE_FILE.exists():
        print("No active workflow found.")
        return

    state = json.loads(STATE_FILE.read_text())
    print("Active workflow:")
    print(f"  Issue:     #{state.get('issue')}")
    print(f"  Repo:      {state.get('repo')}")
    print(f"  Title:     {state.get('title')}")
    print(f"  Comment:   {state.get('first_comment_id')}")


def cmd_abort(_args):
    """Remove active workflow state without touching the issue."""
    if not STATE_FILE.exists():
        print("No active workflow to abort.")
        return

    state = json.loads(STATE_FILE.read_text())
    STATE_FILE.unlink()
    print(f"Aborted workflow for Issue #{state.get('issue')}. Issue was NOT closed.")


def main():
    parser = argparse.ArgumentParser(description="Git Workflow Orchestrator")
    sub = parser.add_subparsers(dest="cmd", help="Available commands")

    p_init = sub.add_parser("init", help="Create issue from task description")
    p_init.add_argument("--title", required=True, help="Issue title")
    p_init.add_argument("--description", required=True, help="Task description (becomes first comment)")
    p_init.add_argument("--labels", default="task", help="Comma-separated labels")
    p_init.add_argument("--repo", help="Repository (owner/repo). Auto-detected from git remote.")
    p_init.add_argument("--remote", default="origin", help="Git remote name for auto-detection")
    p_init.add_argument("instructions", nargs="?", default="", help="Additional implementation instructions")

    p_finish = sub.add_parser("finish", help="Append completion message to first comment and close issue")
    p_finish.add_argument("--message", required=True, help="Completion message to append")
    p_finish.add_argument("--issue", type=int, help="Issue number (overrides state file)")
    p_finish.add_argument("--repo", help="Repository (owner/repo, overrides state file)")

    sub.add_parser("status", help="Show active workflow state")
    sub.add_parser("abort", help="Remove workflow state without closing issue")

    args = parser.parse_args()

    handlers = {
        "init": cmd_init,
        "finish": cmd_finish,
        "status": cmd_status,
        "abort": cmd_abort,
    }

    handler = handlers.get(args.cmd)
    if not handler:
        parser.print_help()
        sys.exit(1)

    handler(args)


if __name__ == "__main__":
    main()
