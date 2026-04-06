#!/usr/bin/env python3
"""Local Task Tracing - 将任务执行过程记录到本地 tracing 目录。

功能：
1. Task 创建时：记录原始内容和 Agent 解析后的内容
2. Task 完成时：追加 Issue 更新内容到同一文件
3. 文件按 task 文件名命名，支持追加

用法：
    python tracing.py init --task tasks/features/tracing.md --issue 7 [--parsed "..."]
    python tracing.py finish --task tasks/features/tracing.md --issue 7 [--comment "..."]
    python tracing.py status
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


TRACING_DIR = Path("tracing")


def _task_stem(task_path: str) -> str:
    """从 task 文件路径提取不含扩展名的文件名作为 tracing 文件名。"""
    return Path(task_path).stem


def _tracing_file(task_path: str) -> Path:
    """获取对应的 tracing 文件路径。"""
    return TRACING_DIR / f"{_task_stem(task_path)}.md"


def _ensure_dir():
    """确保 tracing 目录存在。"""
    TRACING_DIR.mkdir(parents=True, exist_ok=True)


def _read_task_content(task_path: str) -> str:
    """读取 task 文件原始内容。"""
    p = Path(task_path)
    if not p.exists():
        return f"(task file not found: {task_path})"
    return p.read_text(encoding="utf-8")


def cmd_init(args):
    """初始化 tracing 记录：写入原始内容和解析后内容。"""
    _ensure_dir()

    task_path = args.task
    issue_number = args.issue
    parsed = args.parsed or ""

    original = _read_task_content(task_path)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tracing_file = _tracing_file(task_path)

    # 如果文件已存在，追加新的 task 记录
    if tracing_file.exists():
        existing = tracing_file.read_text(encoding="utf-8")
        separator = f"\n\n---\n\n## Task Entry ({now})\n\n"
        content = existing + separator
    else:
        content = f"# Tracing: {_task_stem(task_path)}\n\n"
        content += f"## Task Entry ({now})\n\n"

    content += f"- **Task File**: `{task_path}`\n"
    content += f"- **GitHub Issue**: #{issue_number}\n"
    content += f"- **Started At**: {now}\n"
    content += f"- **Status**: in_progress\n\n"

    content += "### Original Task Content\n\n"
    content += original.strip() + "\n\n"

    if parsed:
        content += "### Agent Parsed Content\n\n"
        content += parsed.strip() + "\n\n"

    tracing_file.write_text(content, encoding="utf-8")
    print(f"Tracing initialized: {tracing_file}")


def cmd_finish(args):
    """完成 tracing 记录：追加 Issue 更新内容，标记完成。"""
    task_path = args.task
    issue_number = args.issue
    comment = args.comment or ""

    tracing_file = _tracing_file(task_path)

    if not tracing_file.exists():
        print(f"Warning: No tracing file found for {task_path}. Creating new entry.", file=sys.stderr)
        _ensure_dir()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"# Tracing: {_task_stem(task_path)}\n\n"
        content += f"## Task Entry ({now})\n\n"
        content += f"- **Task File**: `{task_path}`\n"
        content += f"- **GitHub Issue**: #{issue_number}\n"
        content += f"- **Status**: completed\n\n"
        tracing_file.write_text(content, encoding="utf-8")
    else:
        content = tracing_file.read_text(encoding="utf-8")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update status from in_progress to completed
        content = content.replace("- **Status**: in_progress", "- **Status**: completed")
        content += f"- **Completed At**: {now}\n"

        if comment:
            content += f"\n### Issue Update Content\n\n"
            content += comment.strip() + "\n\n"

        tracing_file.write_text(content, encoding="utf-8")

    print(f"Tracing updated: {tracing_file}")


def cmd_status(_args):
    """显示 tracing 目录中的所有记录。"""
    if not TRACING_DIR.exists():
        print("No tracing directory found.")
        return

    files = sorted(TRACING_DIR.glob("*.md"))
    if not files:
        print("No tracing records found.")
        return

    print(f"Tracing records ({len(files)}):\n")
    for f in files:
        text = f.read_text(encoding="utf-8")
        # Extract status
        status = "unknown"
        for line in text.split("\n"):
            if "**Status**:" in line:
                status = line.split("**Status**:")[1].strip()
                break
        print(f"  - {f.name}  [{status}]")


def main():
    parser = argparse.ArgumentParser(description="Local Task Tracing")
    sub = parser.add_subparsers(dest="cmd", help="Available commands")

    # init
    p_init = sub.add_parser("init", help="Initialize tracing record for a task")
    p_init.add_argument("--task", required=True, help="Task file path (e.g. tasks/features/tracing.md)")
    p_init.add_argument("--issue", required=True, type=int, help="GitHub Issue number")
    p_init.add_argument("--parsed", help="Agent-parsed task content")

    # finish
    p_finish = sub.add_parser("finish", help="Mark tracing record as completed with Issue update")
    p_finish.add_argument("--task", required=True, help="Task file path")
    p_finish.add_argument("--issue", required=True, type=int, help="GitHub Issue number")
    p_finish.add_argument("--comment", help="Issue update content to append")

    # status
    sub.add_parser("status", help="Show all tracing records")

    args = parser.parse_args()

    handlers = {
        "init": cmd_init,
        "finish": cmd_finish,
        "status": cmd_status,
    }

    handler = handlers.get(args.cmd)
    if not handler:
        parser.print_help()
        sys.exit(1)

    handler(args)


if __name__ == "__main__":
    main()
