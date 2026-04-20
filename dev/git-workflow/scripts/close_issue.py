#!/usr/bin/env python3
"""Close a GitHub issue and append completion message to the first comment.

The first comment (which originally contained the task description) is updated
by appending the completion message to the end — the original content is preserved.

Uses gh CLI api command for all operations.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

STATE_FILE = Path(".git-workflow.state.json")


def run_gh(args: list, check: bool = True) -> subprocess.CompletedProcess:
    """Run a gh CLI command."""
    cmd = ["gh"] + args
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


def get_comment(repo: str, comment_id: str) -> dict:
    """Get a comment by ID using gh api."""
    result = run_gh(["api", f"repos/{repo}/issues/comments/{comment_id}"])
    if result.returncode != 0:
        raise RuntimeError(f"gh api get comment failed: {result.stderr}")
    return json.loads(result.stdout)


def update_comment(repo: str, comment_id: str, body: str) -> dict:
    """Update a comment by ID using gh api."""
    result = run_gh([
        "api", "-X", "PATCH",
        f"repos/{repo}/issues/comments/{comment_id}",
        "-f", f"body={body}"
    ])
    if result.returncode != 0:
        raise RuntimeError(f"gh api update comment failed: {result.stderr}")
    return json.loads(result.stdout)


def close_issue(repo: str, issue_number: int) -> None:
    """Close an issue using gh issue close."""
    result = run_gh(["issue", "close", str(issue_number)], check=False)
    if result.returncode != 0:
        raise RuntimeError(f"gh issue close failed: {result.stderr}")


def main():
    parser = argparse.ArgumentParser(
        description="Close an issue and append completion message to its first comment"
    )
    parser.add_argument("--message", required=True, help="Completion message to append")
    parser.add_argument("--issue", type=int, help="Issue number (overrides state file)")
    parser.add_argument("--repo", help="Repository (owner/repo, overrides state file)")
    args = parser.parse_args()

    if STATE_FILE.exists():
        state = json.loads(STATE_FILE.read_text())
    else:
        state = {}

    issue_number = args.issue or state.get("issue")
    repo = args.repo or state.get("repo")
    comment_id = state.get("first_comment_id")
    original_description = state.get("description", "")

    if not issue_number or not repo:
        print("Error: Issue number and repo required. Provide --issue/--repo or run init first.", file=sys.stderr)
        sys.exit(1)

    if not comment_id:
        print("Error: First comment ID not found in state. Run init first.", file=sys.stderr)
        sys.exit(1)

    # Get current comment body
    comment = get_comment(repo, comment_id)
    current_body = comment.get("body", original_description)

    # Append completion message
    separator = "\n\n---\n\n"
    if separator.strip() in current_body:
        new_body = current_body + "\n\n" + args.message
    else:
        new_body = current_body + separator + "### Task Completion Update\n\n" + args.message

    update_comment(repo, comment_id, new_body)
    close_issue(repo, issue_number)

    # Clean up state file
    if STATE_FILE.exists():
        STATE_FILE.unlink()

    print(f"Issue #{issue_number} closed.")
    print("First comment updated with appended completion message.")


if __name__ == "__main__":
    main()
