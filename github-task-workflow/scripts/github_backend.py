#!/usr/bin/env python3
"""Unified GitHub backend - prefers `gh` CLI, falls back to API.

This module provides a unified interface for GitHub operations,
using `gh` command when available for better performance,
and falling back to REST API when `gh` is not installed.
"""

import json
import re
import shutil
import subprocess
import ssl
import certifi
from typing import Optional, List, Dict, Any

import urllib.request
import urllib.error


def _get_ssl_context():
    """Create SSL context with proper certificate handling."""
    return ssl.create_default_context(cafile=certifi.where())


class GitHubBackend:
    """Base class for GitHub operations."""
    
    def create_issue(
        self,
        repo: str,
        title: str,
        body: str,
        labels: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        raise NotImplementedError
    
    def update_issue(
        self,
        repo: str,
        issue_number: int,
        body: Optional[str] = None,
        state: Optional[str] = None
    ) -> Dict[str, Any]:
        raise NotImplementedError
    
    def get_issue(self, repo: str, issue_number: int) -> Dict[str, Any]:
        raise NotImplementedError
    
    def add_comment(
        self,
        repo: str,
        issue_number: int,
        body: str
    ) -> Dict[str, Any]:
        raise NotImplementedError


class GhCliBackend(GitHubBackend):
    """GitHub backend using `gh` CLI for better performance."""
    
    def __init__(self, token: Optional[str] = None):
        self.token = token
        self._env = self._prepare_env()
    
    def _prepare_env(self) -> Optional[dict]:
        """Prepare environment with token if provided."""
        import os
        if self.token:
            env = os.environ.copy()
            env["GITHUB_TOKEN"] = self.token
            return env
        return None
    
    def _run(self, args: List[str], check: bool = True) -> subprocess.CompletedProcess:
        """Run a gh command with optional token in environment."""
        cmd = ["gh"] + args
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=check,
            env=self._env
        )
        return result
    
    def create_issue(
        self,
        repo: str,
        title: str,
        body: str,
        labels: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Create a GitHub issue using gh CLI."""
        args = ["issue", "create", "--repo", repo, "--title", title, "--body", body]
        
        if labels:
            for label in labels:
                args.extend(["--label", label])
        
        args.extend(["--json", "number,title,url,html_url,state,body,labels"])
        
        result = self._run(args)
        data = json.loads(result.stdout)
        
        # Normalize output to match API format
        return {
            "number": data["number"],
            "title": data["title"],
            "url": data["url"],
            "html_url": data["html_url"],
            "state": data["state"],
            "body": data["body"],
            "labels": [{"name": lbl["name"]} for lbl in data.get("labels", [])]
        }
    
    def update_issue(
        self,
        repo: str,
        issue_number: int,
        body: Optional[str] = None,
        state: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update a GitHub issue using gh CLI."""
        # gh CLI doesn't have direct issue edit for body, use API fallback for body updates
        # But we can handle state changes
        if state:
            if state == "closed":
                self._run(["issue", "close", str(issue_number), "--repo", repo], check=False)
            elif state == "open":
                self._run(["issue", "reopen", str(issue_number), "--repo", repo], check=False)
        
        # For body updates, we still need to use API via gh api command
        if body:
            # Use gh api to update body
            json_data = json.dumps({"body": body})
            result = self._run([
                "api",
                "-X", "PATCH",
                f"repos/{repo}/issues/{issue_number}",
                "-f", f"body={body}"
            ])
        
        # Get updated issue
        return self.get_issue(repo, issue_number)
    
    def get_issue(self, repo: str, issue_number: int) -> Dict[str, Any]:
        """Get issue details using gh CLI."""
        result = self._run([
            "issue", "view", str(issue_number),
            "--repo", repo,
            "--json", "number,title,url,html_url,state,body,labels"
        ])
        data = json.loads(result.stdout)
        
        return {
            "number": data["number"],
            "title": data["title"],
            "url": data["url"],
            "html_url": data["html_url"],
            "state": data["state"],
            "body": data["body"],
            "labels": [{"name": lbl["name"]} for lbl in data.get("labels", [])]
        }
    
    def add_comment(
        self,
        repo: str,
        issue_number: int,
        body: str
    ) -> Dict[str, Any]:
        """Add a comment to an issue using gh CLI."""
        result = self._run([
            "issue", "comment", str(issue_number),
            "--repo", repo,
            "--body", body,
            "--json", "id,url,body"
        ])
        data = json.loads(result.stdout)
        
        return {
            "id": data.get("id"),
            "html_url": data.get("url"),
            "body": data.get("body")
        }


class ApiBackend(GitHubBackend):
    """GitHub backend using REST API (fallback)."""
    
    def __init__(self, token: Optional[str] = None):
        if not token:
            raise ValueError("GitHub token required for API backend")
        self.token = token
    
    def _make_request(
        self,
        method: str,
        url: str,
        data: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Make an authenticated HTTP request."""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        
        if data:
            headers["Content-Type"] = "application/json"
            body = json.dumps(data).encode("utf-8")
        else:
            body = None
        
        req = urllib.request.Request(
            url,
            data=body,
            headers=headers,
            method=method
        )
        
        try:
            context = _get_ssl_context()
            with urllib.request.urlopen(req, context=context) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            raise RuntimeError(f"GitHub API error: {e.code} - {error_body}")
    
    def create_issue(
        self,
        repo: str,
        title: str,
        body: str,
        labels: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Create a GitHub issue via API."""
        url = f"https://api.github.com/repos/{repo}/issues"
        data = {"title": title, "body": body}
        if labels:
            data["labels"] = labels
        return self._make_request("POST", url, data)
    
    def update_issue(
        self,
        repo: str,
        issue_number: int,
        body: Optional[str] = None,
        state: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update a GitHub issue via API."""
        url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
        data = {}
        if body:
            data["body"] = body
        if state:
            data["state"] = state
        if not data:
            raise ValueError("No updates specified")
        return self._make_request("PATCH", url, data)
    
    def get_issue(self, repo: str, issue_number: int) -> Dict[str, Any]:
        """Get issue details via API."""
        url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
        return self._make_request("GET", url)
    
    def add_comment(
        self,
        repo: str,
        issue_number: int,
        body: str
    ) -> Dict[str, Any]:
        """Add a comment to an issue via API."""
        url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
        return self._make_request("POST", url, {"body": body})


def is_gh_available() -> bool:
    """Check if `gh` CLI is installed and available."""
    return shutil.which("gh") is not None


def create_backend(token: Optional[str] = None) -> GitHubBackend:
    """Create the best available GitHub backend.
    
    Priority:
    1. GhCliBackend if `gh` is installed
    2. ApiBackend if token is provided
    
    Args:
        token: GitHub token (required for API backend)
        
    Returns:
        GitHubBackend instance
        
    Raises:
        RuntimeError: if no backend can be created
    """
    if is_gh_available():
        # gh CLI handles auth internally, but we can pass token via env
        return GhCliBackend(token)
    
    if token:
        return ApiBackend(token)
    
    raise RuntimeError(
        "No GitHub backend available. "
        "Please either:\n"
        "  1. Install GitHub CLI (gh): https://cli.github.com/\n"
        "  2. Provide a GitHub token for API access"
    )


def get_backend_info() -> Dict[str, Any]:
    """Get information about available backends."""
    return {
        "gh_available": is_gh_available(),
        "gh_path": shutil.which("gh"),
        "preferred": "gh" if is_gh_available() else "api"
    }
