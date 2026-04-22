# 自动文档更新方案

> 任务完成后自动更新项目文档的设计方案。

## 问题

每次完成任务后，相关文档（README.md、目录索引、使用指南）经常忘记更新，导致文档与实际代码/结构脱节。

## 方案概览

**推荐方案：在 git-workflow 的 finish 阶段集成文档检查，不创建独立的 docs skill。**

理由：
1. 文档更新与任务完成是强关联的，应在同一工作流中处理
2. 避免引入额外 skill 增加维护成本
3. Claude Code hooks 机制天然支持"任务完成时触发"

---

## 方案一：集成到 git-workflow finish（推荐）

### 设计

在 `orchestrate.py finish` 阶段，自动生成一份"文档更新建议"，附加到 Issue 评论中。

```
┌─────────────┐    ┌──────────────┐    ┌─────────────────────┐    ┌───────────┐
│  init        │───►│  implement   │───►│  finish             │───►│  close    │
│  创建 Issue  │    │  执行任务    │    │  1. 完成摘要        │    │  Issue    │
│              │    │              │    │  2. 文档更新检查 →  │    │           │
└─────────────┘    └──────────────┘    │     生成建议列表    │    └───────────┘
                                       └─────────────────────┘
```

### 实现步骤

#### Step 1: 创建文档检查脚本

`dev/git-workflow/scripts/doc_checker.py`

```python
"""检查任务完成后哪些文档需要更新。"""

import subprocess
import json
import os
import re
from pathlib import Path

# 需要检查的文档规则
DOC_RULES = [
    {
        "name": "README.md Skill 列表",
        "file": "README.md",
        "trigger": "新增/删除/重命名 SKILL.md 文件",
        "check": lambda changes: any('SKILL.md' in c for c in changes),
    },
    {
        "name": "目录 README.md",
        "file": "<changed-dir>/README.md",
        "trigger": "目录结构变化（新增/删除文件）",
        "check": lambda changes: any('SKILL.md' in c or 'README.md' in c for c in changes),
    },
    {
        "name": "安装指南",
        "file": "docs/usage/install-frontend-skills.md",
        "trigger": "skill 名称或目录变化",
        "check": lambda changes: any('fe-skills/' in c for c in changes),
    },
]


def get_changed_files():
    """获取本次任务修改的所有文件（相比 init 时的 commit）。"""
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True, text=True
    )
    return result.stdout.strip().split('\n')


def check_docs():
    """检查哪些文档可能需要更新，返回建议列表。"""
    changed = get_changed_files()
    suggestions = []

    for rule in DOC_RULES:
        if rule["check"](changed):
            suggestions.append({
                "doc": rule["name"],
                "file": rule["file"],
                "reason": rule["trigger"],
            })

    # 自动检测：受影响的目录是否缺少 README.md
    dirs_with_changes = set()
    for f in changed:
        dir_path = os.path.dirname(f)
        if dir_path and not dir_path.startswith('.'):
            dirs_with_changes.add(dir_path)

    for d in dirs_with_changes:
        readme = os.path.join(d, "README.md")
        if not os.path.exists(readme):
            suggestions.append({
                "doc": f"{d}/README.md",
                "file": readme,
                "reason": "目录缺少 README.md",
            })

    return suggestions


if __name__ == "__main__":
    suggestions = check_docs()
    if suggestions:
        print("📋 文档更新建议：")
        for s in suggestions:
            print(f"  - {s['doc']}: {s['reason']}")
    else:
        print("✅ 无需文档更新")
```

#### Step 2: 在 orchestrate.py finish 中集成

```python
# orchestrate.py finish 阶段末尾添加
from doc_checker import check_docs

def finish(message):
    # ... 现有完成逻辑 ...

    # 文档更新检查
    suggestions = check_docs()
    if suggestions:
        doc_msg = "\n\n## 文档更新建议\n\n"
        for s in suggestions:
            doc_msg += f"- **{s['doc']}**: {s['reason']}\n"

        # 追加到 Issue 评论
        update_issue(issue_number, doc_msg)
```

#### Step 3: 在 CLAUDE.md 中添加提醒

```markdown
## 文档更新提醒

任务完成后，检查以下文档是否需要更新：
1. 受影响目录的 `README.md`
2. 项目根目录 `README.md` 的 Skill 列表
3. `docs/usage/` 下的安装指南（如果 skill 目录结构变化）
```

### 优点

- 无需新 skill，集成在现有工作流中
- 自动检测，不依赖人工记忆
- 只生成建议，不强制修改（由 AI 或用户决定是否更新）

### 缺点

- 需要修改 `orchestrate.py`，增加耦合
- 检测规则需要持续维护

---

## 方案二：独立 docs-update Skill（可选进阶）

如果方案一不够，可以创建独立的 docs-update skill。

### 触发方式

```
手动触发：/docs-update
自动触发：通过 Claude Code hooks 在任务完成后调用
```

### SKILL.md 结构

```
docs-update/
├── SKILL.md              # Skill 定义
├── scripts/
│   └── doc_checker.py    # 文档检查脚本
└── references/
    └── doc-rules.md      # 文档更新规则
```

### 工作流

```
任务完成 → hook 触发 → docs-update skill
                          │
                          ├─ 1. git diff 检测变更
                          ├─ 2. 匹配文档更新规则
                          ├─ 3. 生成更新建议列表
                          └─ 4. 输出到对话 / Issue 评论
```

### Hook 配置

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/skills/docs-update/hooks/check-docs.sh",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### 优点

- 独立可复用，不耦合 git-workflow
- 支持手动触发（/docs-update）
- 可跨 Agent 使用

### 缺点

- 多一个 skill 需要维护
- hook 配置增加复杂度

---

## 推荐实施路径

```
Phase 1（立即可做）:
  1. 在 CLAUDE.md 中添加"文档更新提醒"段落
  2. 在 git-workflow finish 后，AI 自动检查受影响目录的 README.md

Phase 2（需要开发）:
  1. 创建 doc_checker.py 脚本
  2. 集成到 orchestrate.py finish 阶段
  3. 自动在 Issue 评论中追加文档更新建议

Phase 3（按需）:
  1. 如果规则复杂度增加，拆分为独立的 docs-update skill
  2. 配置 Claude Code Stop hook 自动触发
```

## 文档更新规则清单

| 变更类型 | 需要更新的文档 | 优先级 |
|----------|---------------|--------|
| 新增/删除 SKILL.md | `README.md` Skill 列表 + 目录 README | P0 |
| 修改 SKILL.md | 目录 README.md（如果有描述性内容） | P1 |
| 目录结构变化 | 受影响目录的 README.md | P1 |
| 新增安装命令 | `docs/usage/` 相关指南 | P1 |
| 新增脚本/工具 | 对应 Skill 的 SKILL.md | P2 |
| 配置文件变化 | `docs/` 下的配置指南 | P2 |
