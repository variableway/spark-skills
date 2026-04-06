#!/usr/bin/env python3
"""Create a GitHub issue from a task description - Fixed for SSL issues."""

# Patch SSL before any other imports
import sys
import os

# Add the scripts directory to path to import ssl_context
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ssl_context import patch_urllib
patch_urllib()

# Now import the rest
import argparse
import json
import subprocess
import urllib.request
import urllib.error

from config_loader import get_github_token, get_config_info


def get_git_remote(repo_url: str = None, remote_name: str = "origin") -> str:
    """Get owner/repo from git remote or provided URL."""
    if repo_url:
        import re
        if re.match(r"^[\w.-]+/[\w.-]+$", repo_url):
            return repo_url
        match = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", repo_url)
        if match:
            return match.group(1)
    
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", remote_name],
            capture_output=True,
            text=True,
            check=True
        )
        remote_url = result.stdout.strip()
        import re
        match = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", remote_url)
        if match:
            return match.group(1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    return None


def create_issue(repo: str, title: str, body: str, labels: list = None, token: str = None) -> dict:
    """Create a GitHub issue via API."""
    if not token:
        raise ValueError(
            "GitHub token required. Provide via:\n"
            "  1. --token argument\n"
            "  2. GITHUB_TOKEN environment variable\n"
            "  3. Project config: .github-task-workflow.yaml\n"
            "  4. Global config: ~/.config/github-task-workflow/config.yaml"
        )
    
    url = f"https://api.github.com/repos/{repo}/issues"
    
    data = {
        "title": title,
        "body": body
    }
    
    if labels:
        data["labels"] = labels
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise RuntimeError(f"GitHub API error: {e.code} - {error_body}")


def main():
    parser = argparse.ArgumentParser(
        description="Create a GitHub issue from a task",
        epilog="If --repo is not provided, will try to detect from git remote."
    )
    parser.add_argument("--repo", help="Repository (owner/repo or URL)")
    parser.add_argument("--remote", default="origin", help="Git remote name")
    parser.add_argument("--title", required=True, help="Issue title")
    parser.add_argument("--body", required=True, help="Issue body")
    parser.add_argument("--labels", help="Comma-separated list of labels")
    parser.add_argument("--token", help="GitHub token")
    parser.add_argument("--output-json", action="store_true", help="Output JSON")
    
    args = parser.parse_args()
    
    repo = get_git_remote(args.repo, args.remote)
    if not repo:
        print("Error: Could not detect repository.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Using repository: {repo}")
    
    labels = None
    if args.labels:
        labels = [l.strip() for l in args.labels.split(",")]
    
    token = get_github_token(args.token)
    if not token:
        print("Error: GitHub token not found.", file=sys.stderr)
        sys.exit(1)
    
    config_info = get_config_info()
    if config_info["token_source"]:
        print(f"Using token from: {config_info['token_source']}")
    
    try:
        issue = create_issue(repo, args.title, args.body, labels, token)
        
        # Write active issue marker
        from pathlib import Path
        try:
            cwd = Path.cwd()
            (cwd / ".github-task-workflow.active-issue").write_text(str(issue['number']))
        except Exception:
            pass
        
        if args.output_json:
            print(json.dumps(issue, indent=2))
        else:
            print(f"Issue created: {issue['number']}")
            print(f"URL: {issue['html_url']}")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
