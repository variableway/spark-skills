#!/usr/bin/env python3
"""Create a GitHub issue from a task description.

Uses GitHub CLI (gh) when available for better performance,
falls back to REST API otherwise.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from config_loader import get_github_token, get_config_info
from github_backend import create_backend, is_gh_available, get_backend_info


def get_git_remote(repo_url: str = None, remote_name: str = "origin") -> str:
    """Get owner/repo from git remote or provided URL.
    
    Args:
        repo_url: Optional repo URL or owner/repo string
        remote_name: Git remote name to check (default: origin)
        
    Returns:
        owner/repo string
    """
    if repo_url:
        # Check if already in owner/repo format
        if re.match(r"^[\w.-]+/[\w.-]+$", repo_url):
            return repo_url
        # Extract from GitHub URL
        match = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", repo_url)
        if match:
            return match.group(1)
    
    # Try to get from git config
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", remote_name],
            capture_output=True,
            text=True,
            check=True
        )
        remote_url = result.stdout.strip()
        match = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", remote_url)
        if match:
            return match.group(1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Create a GitHub issue from a task",
        epilog="If --repo is not provided, will try to detect from git remote."
    )
    parser.add_argument("--repo", help="Repository (owner/repo or URL). Auto-detected from git if not provided.")
    parser.add_argument("--remote", default="origin", help="Git remote name to use for auto-detection (default: origin)")
    parser.add_argument("--title", required=True, help="Issue title")
    parser.add_argument("--body", required=True, help="Issue body (markdown)")
    parser.add_argument("--labels", help="Comma-separated list of labels")
    parser.add_argument("--token", help="GitHub token (or set GITHUB_TOKEN env var)")
    parser.add_argument("--output-json", action="store_true", help="Output full JSON response")
    
    args = parser.parse_args()
    
    # Detect repo
    repo = get_git_remote(args.repo, args.remote)
    if not repo:
        print("Error: Could not detect repository.", file=sys.stderr)
        print("Please provide --repo or run from within a git repository with GitHub remote.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Using repository: {repo}")
    
    # Show backend info
    backend_info = get_backend_info()
    if backend_info["gh_available"]:
        print(f"Using GitHub CLI: {backend_info['gh_path']}")
    else:
        print("GitHub CLI not found, using REST API fallback")
    
    labels = None
    if args.labels:
        labels = [l.strip() for l in args.labels.split(",")]
    
    # Get token using priority chain
    token = get_github_token(args.token)
    
    # Show token source if using API fallback
    if not backend_info["gh_available"]:
        if not token:
            print("Error: GitHub token not found (required for API fallback).", file=sys.stderr)
            print("\nTo configure:", file=sys.stderr)
            print("  1. Set GITHUB_TOKEN environment variable", file=sys.stderr)
            print("  2. Create project config: .github-task-workflow.yaml", file=sys.stderr)
            print("  3. Create global config: ~/.config/github-task-workflow/config.yaml", file=sys.stderr)
            print("\nOr install GitHub CLI: https://cli.github.com/", file=sys.stderr)
            sys.exit(1)
        
        config_info = get_config_info()
        if config_info["token_source"]:
            print(f"Using token from: {config_info['token_source']}")
    
    try:
        # Create backend (prefers gh, falls back to API)
        backend = create_backend(token)
        issue = backend.create_issue(repo, args.title, args.body, labels)
        
        # Write active issue marker for hook integration
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
