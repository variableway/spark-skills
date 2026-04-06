#!/usr/bin/env python3
"""跨 Agent 的 GitHub Task Workflow 编排器。

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
from config_loader import get_github_token
from github_backend import create_backend, get_backend_info


STATE_FILE = Path(".github-task-workflow.state.json")

# Import tracing module (legacy tracing in github-task-workflow/tracing.py)
from tracing import cmd_init as tracing_init, cmd_finish as tracing_finish

# Import local-workflow tracing for dual tracing support
LOCAL_WORKFLOW_TRACING = Path(__file__).parent.parent.parent / "local-workflow" / "scripts" / "tracing.py"
if LOCAL_WORKFLOW_TRACING.exists():
    import importlib.util
    spec = importlib.util.spec_from_file_location("local_tracing", LOCAL_WORKFLOW_TRACING)
    local_tracing = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(local_tracing)
    local_tracing_init = local_tracing.cmd_init
    local_tracing_finish = local_tracing.cmd_finish
else:
    local_tracing_init = None
    local_tracing_finish = None


class _TracingArgs:
    """Minimal args namespace for tracing calls."""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def _get_git_remote(repo_url: str = None, remote_name: str = "origin") -> str:
    """Get owner/repo from git remote or provided URL."""
    import re
    
    if repo_url:
        if re.match(r"^[\w.-]+/[\w.-]+$", repo_url):
            return repo_url
        match = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", repo_url)
        if match:
            return match.group(1)
    
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", remote_name],
            capture_output=True, text=True, check=True
        )
        remote_url = result.stdout.strip()
        match = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", remote_url)
        if match:
            return match.group(1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    return None


def _ensure_repo_and_token():
    repo = _get_git_remote()
    token = get_github_token()
    
    if not repo:
        print("Error: Could not detect GitHub repository from git remote.", file=sys.stderr)
        sys.exit(1)
    
    # Check backend availability
    backend_info = get_backend_info()
    if not backend_info["gh_available"] and not token:
        print("Error: GitHub token not found (required for API fallback).", file=sys.stderr)
        print("Configure via GITHUB_TOKEN env var or .github-task-workflow.yaml", file=sys.stderr)
        print("Or install GitHub CLI: https://cli.github.com/", file=sys.stderr)
        sys.exit(1)
    
    return repo, token


def cmd_init(args):
    task_path = Path(args.task_file)
    if not task_path.exists():
        print(f"Error: Task file not found: {task_path}", file=sys.stderr)
        sys.exit(1)

    repo, token = _ensure_repo_and_token()

    try:
        content = task_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading task file: {e}", file=sys.stderr)
        sys.exit(1)

    lines = content.split("\n")
    title = lines[0].lstrip("# ").strip() if lines else task_path.stem
    body = content

    if STATE_FILE.exists():
        old = json.loads(STATE_FILE.read_text())
        print(f"Warning: Existing workflow found for Issue #{old.get('issue')}. Abort it first if stale.", file=sys.stderr)

    try:
        backend = create_backend(token)
        issue = backend.create_issue(repo, title, body, labels=["task"])
    except Exception as e:
        print(f"Error creating issue: {e}", file=sys.stderr)
        sys.exit(1)

    state = {
        "issue": issue["number"],
        "repo": repo,
        "task_file": str(task_path),
        "instructions": args.instructions or "",
        "html_url": issue.get("html_url", ""),
        "status": "created"
    }
    STATE_FILE.write_text(json.dumps(state, indent=2))

    # Initialize legacy local tracing (tracing/)
    try:
        tracing_args = _TracingArgs(
            task=str(task_path),
            issue=issue["number"],
            parsed=args.instructions or ""
        )
        tracing_init(tracing_args)
    except Exception as e:
        print(f"Tracing init warning: {e}")
    
    # Initialize local-workflow tracing (tasks/tracing/) - dual tracing
    if local_tracing_init:
        try:
            local_tracing_args = _TracingArgs(
                task=str(task_path),
                parsed=args.instructions or ""
            )
            local_task_id = local_tracing_init(local_tracing_args)
            print(f"Local-workflow tracing initialized: {local_task_id}")
        except Exception as e:
            print(f"Local-workflow tracing init warning: {e}")

    print(f"Created Issue #{issue['number']}: {issue.get('html_url', '')}")
    print(f"State saved to: {STATE_FILE}")
    print("\n=== NEXT STEP ===")
    print("Please implement the task now.")
    print("After implementation, run: python scripts/orchestrate.py finish")


def cmd_status(_args):
    if not STATE_FILE.exists():
        print("No active workflow found.")
        return

    state = json.loads(STATE_FILE.read_text())
    print(f"Active workflow:")
    print(f"  Issue:     #{state['issue']}")
    print(f"  URL:       {state.get('html_url', '')}")
    print(f"  Repo:      {state['repo']}")
    print(f"  Task file: {state['task_file']}")
    print(f"  Status:    {state['status']}")
    if state.get("instructions"):
        print(f"  Instructions: {state['instructions']}")


def cmd_finish(_args):
    if not STATE_FILE.exists():
        print("Error: No active workflow found. Run 'init' first.", file=sys.stderr)
        sys.exit(1)

    state = json.loads(STATE_FILE.read_text())
    repo = state["repo"]
    issue_number = state["issue"]
    token = get_github_token()

    # Check backend availability
    backend_info = get_backend_info()
    if not backend_info["gh_available"] and not token:
        print("Error: GitHub token not found.", file=sys.stderr)
        sys.exit(1)

    # Gather git summary for the comment
    try:
        changed = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True, text=True, check=False
        ).stdout.strip()
    except Exception:
        changed = ""

    comment_lines = ["### Implementation Completed", ""]
    if state.get("instructions"):
        comment_lines.append(f"**Instructions**: {state['instructions']}")
        comment_lines.append("")
    if changed:
        comment_lines.append("**Files changed**:")
        for f in changed.split("\n"):
            if f.strip():
                comment_lines.append(f"- `{f}`")
    else:
        comment_lines.append("Task implementation is done.")

    comment = "\n".join(comment_lines)

    try:
        backend = create_backend(token)
        backend.add_comment(repo, issue_number, comment)
        backend.update_issue(repo, issue_number, state="closed")
        print(f"Updated and closed Issue #{issue_number}")

        # Update legacy local tracing (tracing/)
        try:
            tracing_args = _TracingArgs(
                task=state.get("task_file", ""),
                issue=issue_number,
                comment=comment
            )
            tracing_finish(tracing_args)
        except Exception as e:
            print(f"Tracing finish warning: {e}")
        
        # Update local-workflow tracing (tasks/tracing/) - dual tracing
        if local_tracing_finish:
            try:
                local_tracing_args = _TracingArgs(
                    task=state.get("task_file", ""),
                    summary=comment
                )
                local_tracing_finish(local_tracing_args)
                print("Local-workflow tracing updated")
            except Exception as e:
                print(f"Local-workflow tracing finish warning: {e}")
    except Exception as e:
        print(f"Error updating issue: {e}", file=sys.stderr)
        sys.exit(1)

    # Git commit and push
    try:
        subprocess.run(["git", "add", "-A"], check=False)
        subprocess.run(
            ["git", "commit", "-m", f"Complete task (Refs: #{issue_number})"],
            capture_output=True, text=True, check=False
        )
        push_result = subprocess.run(["git", "push"], capture_output=True, text=True, check=False)
        if push_result.returncode == 0:
            print("Code committed and pushed.")
        else:
            print("Commit created, but push may need attention.")
    except Exception as e:
        print(f"Git operation warning: {e}")

    STATE_FILE.unlink()
    print("Workflow complete.")


def cmd_abort(_args):
    if not STATE_FILE.exists():
        print("No active workflow to abort.")
        return

    state = json.loads(STATE_FILE.read_text())
    STATE_FILE.unlink()
    print(f"Aborted workflow for Issue #{state.get('issue')}")


def main():
    parser = argparse.ArgumentParser(description="GitHub Task Workflow Orchestrator")
    sub = parser.add_subparsers(dest="cmd", help="Available commands")

    p_init = sub.add_parser("init", help="Create issue from task file and save state")
    p_init.add_argument("task_file", help="Path to the task markdown file")
    p_init.add_argument("instructions", nargs="?", default="", help="Additional implementation instructions")

    sub.add_parser("status", help="Show active workflow state")
    sub.add_parser("finish", help="Update issue with summary, close it, and push code")
    sub.add_parser("abort", help="Remove active workflow state without updating issue")

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
