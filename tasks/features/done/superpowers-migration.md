# Superpowers Skills 吸收迁移计划

## 背景

当前仓库 `fire-skills` 中包含一个嵌套的 `superpowers/` 目录（obra/superpowers 的 fork，186 个文件 / 3.4MB）。目标是将其中有价值的 Skill 提炼出来，吸收到自研体系中，使仓库更精简、更聚焦。

## 目标

1. 从 superpowers 14 个 Skill 中筛选出适合自研体系的 Skill
2. 按分类组织到 `dev/` 子目录
3. 改造 install.sh 支持递归扫描子目录
4. 移除 `superpowers/` 目录

## 迁移后目录结构

```
fire-skills/
├── dev/                                  # 开发流程 Skills（从 superpowers 吸收）
│   │
│   │  ── 第一档：直接搬迁（纯方法论，无平台依赖）──
│   ├── tdd/                              # ← test-driven-development
│   ├── systematic-debugging/             # ← 同名
│   ├── verification-before-completion/   # ← 同名
│   ├── receiving-code-review/            # ← 同名
│   │
│   │  ── 第二档：改造后吸收 ──
│   ├── brainstorming/                    # ← 去掉 server 强依赖
│   ├── writing-plans/                    # ← 去掉 superpowers: 引用
│   ├── requesting-code-review/           # ← 去掉 subagent 调度
│   ├── finishing-branch/                 # ← finishing-a-development-branch 精简版
│
├── github-task-workflow/                 # 任务管理（保持根目录）
├── local-workflow/
├── spark-task-init-skill/
├── ai-config/                            # AI 配置
├── scanning-for-secrets/                 # 安全
├── github-cli-skill/                     # GitHub 工具
├── innate-frontend/                      # 前端
├── tauri-desktop-app/                    # 桌面应用
│
├── install.sh                            # 改为递归扫描
└── README.md                             # 更新 Skill 列表
```

## 不吸收的 Skill（3 个）

| Skill | 不吸收理由 |
|-------|-----------|
| subagent-driven-development | 核心调度器，强依赖 Task tool + 3 个 subagent prompt 文件 |
| using-superpowers | Superpowers 引导入口，全内容关于如何使用 superpowers 体系 |
| writing-skills | 元技能，教如何给 superpowers 写 skill |

## 执行阶段

### Phase 1: 修改 install.sh 支持递归扫描

**改动点**：`get_available_skills()` 函数从单层扫描改为递归查找 `SKILL.md`

**改动前**：
```bash
get_available_skills() {
    local skills=()
    for dir in "$SCRIPT_DIR"/*/; do
        if [ -d "$dir" ] && [ -f "$dir/SKILL.md" ]; then
            skills+=("$(basename "$dir")")
        fi
    done
    echo "${skills[@]}"
}
```

**改动后**：
```bash
get_available_skills() {
    find "$SCRIPT_DIR" -name "SKILL.md" -not -path "*/node_modules/*" -not -path "*/.git/*" | \
        while read f; do
            local dir=$(dirname "$f")
            echo "${dir#$SCRIPT_DIR/}"
        done
}
```

同时需要调整 `install_skill_to_dir` 等函数，使 symlink 目标名仍为 Skill 名称（去掉路径前缀）。

**验证**：`./install.sh --list` 列出所有 Skill（含 dev/ 下的）

### Phase 2: 直接搬迁第一档 Skill（4 个）

以下 Skill 为纯方法论文档，只需：
- 复制到 `dev/` 对应目录
- 在 frontmatter 添加 `supported_agents` 和 `category: dev`
- 全局替换 `superpowers:xxx` 引用为纯文本描述
- 清理不需要的附件文件

| 源 | 目标 | 改动 |
|----|------|------|
| `superpowers/skills/test-driven-development/` | `dev/tdd/` | 添加 frontmatter；移除 `superpowers:` 引用 |
| `superpowers/skills/systematic-debugging/` | `dev/systematic-debugging/` | 添加 frontmatter；移除 `superpowers:` 引用 |
| `superpowers/skills/verification-before-completion/` | `dev/verification-before-completion/` | 添加 frontmatter（无外部引用） |
| `superpowers/skills/receiving-code-review/` | `dev/receiving-code-review/` | 添加 frontmatter（无外部引用） |

**验证**：每个 Skill 的 SKILL.md frontmatter 包含 name/description/category/supported_agents

### Phase 3: 改造吸收第二档 Skill（5 个）

需要手工调整内容，移除平台依赖：

| 源 | 目标 | 改造要点 |
|----|------|---------|
| `superpowers/skills/brainstorming/` | `dev/brainstorming/` | 保留核心流程；server 脚本标记为可选；移除 `superpowers:writing-plans` 强制调用 |
| `superpowers/skills/writing-plans/` | `dev/writing-plans/` | 移除 `REQUIRED SUB-SKILL: superpowers:subagent-driven-development`，改为建议 |
| `superpowers/skills/requesting-code-review/` | `dev/requesting-code-review/` | 移除 `Dispatch superpowers:code-reviewer subagent`，改为审查清单步骤 |
| `superpowers/skills/finishing-a-development-branch/` | `dev/finishing-branch/` | 精简；去掉 worktree 强依赖 |
| `superpowers/skills/executing-plans/` | `dev/executing-plans/` | 移除 `superpowers:finishing-a-development-branch` 强制调用 |

**每个 Skill 的统一改造清单**：
1. frontmatter 添加 `category: dev` 和 `supported_agents`
2. 全局替换 `superpowers:xxx` → 纯文本引用（如 "参见 tdd Skill"）
3. 移除 `SUBAGENT-STOP`、`EXTREMELY-IMPORTANT` 等 superpowers 体系特有的标记
4. 移除对 Task tool / Skill tool 的平台特定引用
5. 保留核心方法论内容和流程图

### Phase 4: 更新文档 + 清理

1. 更新 `README.md`：
   - Skill 列表增加 dev 分类
   - 移除 superpowers 相关说明
   - 更新目录结构图
2. 移除 `superpowers/` 目录

### Phase 5: 全量验证

| 验证项 | 预期结果 |
|--------|---------|
| `./install.sh --list` | 列出所有 Skill（含 dev/ 下 9 个） |
| `./install.sh --list` | 不再列出 superpowers 相关内容 |
| 所有 SKILL.md frontmatter | 包含 name/description/category/supported_agents |
| 所有 Python 脚本 py_compile | 通过 |
| dev/ 下无 `superpowers:` 残留引用 | grep 验证 |

## 风险与回退

| 风险 | 缓解措施 |
|------|---------|
| install.sh 递归扫描可能发现意外文件 | 限定只查找 `*/SKILL.md`，排除 node_modules/.git |
| 改造后的 Skill 丢失原版完整性 | superpowers 原始仓库仍可独立获取 |
| symlink 安装路径变化 | 安装目标仍为扁平目录，源路径不影响 |

## 时间线

- Phase 1: install.sh 改造
- Phase 2: 第一档直接搬迁
- Phase 3: 第二档改造吸收
- Phase 4: 文档更新 + 清理
- Phase 5: 全量验证
