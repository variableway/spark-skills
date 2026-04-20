#!/usr/bin/env python3
"""Create a GitHub issue from a task description.

Based on github-cli-skill. Uses gh CLI api command for all operations.
Saves workflow state to .git-workflow.state.json.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

STATE_FILE = Path(".git-workflow.state.json")


def run_gh(args: list, check: bool = True) -> subprocess.CompletedProcess:
    """Run a gh CLI command."""
    cmd = ["gh"] + args
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


def get_repo(remote_name: str = "origin") -> str:
    """Detect owner/repo from git remote."""
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


def create_issue(repo: str, title: str, body: str, labels: list = None) -> dict:
    """Create a GitHub issue using gh api."""
    fields = [f"title={title}", f"body={body}"]
    if labels:
        for label in labels:
            fields.append(f"labels[]={label}")

    args = ["api", "-X", "POST", f"repos/{repo}/issues"]
    for f in fields:
        args.extend(["-f", f])

    result = run_gh(args)
    if result.returncode != 0:
        raise RuntimeError(f"gh api create issue failed: {result.stderr}")

    return json.loads(result.stdout)


def add_comment(repo: str, issue_number: int, body: str) -> dict:
    """Add a comment to an issue using gh api."""
    args = [
        "api", "-X", "POST",
        f"repos/{repo}/issues/{issue_number}/comments",
        "-f", f"body={body}"
    ]
    result = run_gh(args)
    if result.returncode != 0:
        raise RuntimeError(f"gh api add comment failed: {result.stderr}")

    return json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser(
        description="Create a GitHub issue from a task description"
    )
    parser.add_argument("--title", required=True, help="Issue title")
    parser.add_argument("--description", required=True, help="Task description (becomes first comment)")
    parser.add_argument("--labels", default="task", help="Comma-separated labels")
    parser.add_argument("--repo", help="Repository (owner/repo). Auto-detected from git remote.")
    parser.add_argument("--remote", default="origin", help="Git remote name for auto-detection")
    args = parser.parse_args()

    repo = args.repo or get_repo(args.remote)
    if not repo:
        print("Error: Could not detect repository.", file=sys.stderr)
        print("Please provide --repo or run from a git repo with GitHub remote.", file=sys.stderr)
        sys.exit(1)

    labels = [l.strip() for l in args.labels.split(",")] if args.labels else None

    issue = create_issue(repo, args.title, args.description, labels)
    comment = add_comment(repo, issue["number"], args.description)

    state = {
        "issue": issue["number"],
        "repo": repo,
        "first_comment_id": comment["id"],
        "description": args.description,
        "title": args.title,
    }
    STATE_FILE.write_text(json.dumps(state, indent=2))

    print(f"Issue #{issue['number']} created: {issue.get('html_url', '')}")
    print(f"First comment ID: {comment['id']}")
    print(f"State saved to: {STATE_FILE}")


if __name__ == "__main__":
    main()
