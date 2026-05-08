# 技能迁移指南：构建个人技能集合

## 概述

本指南分析了两个知名仓库的技能——**superpowers**（8 个技能）和 **mattprocock-skills**（14 个技能）——并提供了一种结构化方法，用于将技能迁移和整理为符合个人工作流偏好的个人技能集合。

---

## 1. 源技能清单

### 1.1 Superpowers 技能（8 个）

| 技能 | 用途 | 复杂度 | 迁移优先级 |
|------|------|--------|-----------|
| brainstorming | 实现前的苏格拉底式设计精炼 | 高 | ★★★★★ |
| dispatching-parallel-agents | 独立任务的并行子代理执行 | 中 | ★★★★ |
| executing-plans | 带检查点的分步计划执行 | 中 | ★★★★ |
| finishing-a-development-branch | 分支集成决策（merge/PR/keep/discard） | 中 | ★★★★★ |
| receiving-code-review | 对代码审查反馈的技术评估 | 中 | ★★★★★ |
| requesting-code-review | 调度 code-reviewer 子代理 | 低 | ★★★ |
| subagent-driven-development | 每任务独立子代理 + 双阶段审查 | 高 | ★★★★ |
| systematic-debugging | 根因优先的调试方法论 | 中 | ★★★★★ |

**总体质量**：非常高。工程实践扎实，反模式清晰，质量关卡完善。

### 1.2 MattProcock 技能（14 个）

| 技能 | 用途 | 复杂度 | 迁移优先级 |
|------|------|--------|-----------|
| design-an-interface | 并行子代理生成截然不同的设计方案 | 高 | ★★★★★ |
| edit-article | 按章节编辑文章 | 低 | ★★ |
| git-guardrails-claude-code | 通过 hooks 阻止危险 git 命令 | 中 | ★★★★★ |
| github-triage | 面向代理的结构化 Issue 模板 | 低 | ★★★★ |
| grill-me | 无情追问以压力测试设计方案 | 低 | ★★★ |
| migrate-to-shoehorn | TypeScript `as` → `fromPartial()` 迁移 | 低 | ★★ |
| obsidian-vault | Obsidian 笔记管理与 wikilinks | 低 | ★★ |
| qa | 对话式 Bug 报告 → GitHub Issues | 中 | ★★★★ |
| request-refactor-plan | 详细的增量重构计划 | 中 | ★★★★ |
| scaffold-exercises | 练习目录脚手架 | 中 | ★★★ |
| setup-pre-commit | Husky + lint-staged 预提交钩子 | 中 | ★★★★★ |
| tdd | 红-绿-重构 TDD 方法论 | 高 | ★★★★★ |
| triage-issue | Bug 分诊 → 根因分析 → TDD 修复计划 | 中 | ★★★★★ |
| write-a-skill | 元技能：创建新的代理技能 | 中 | ★★★★★ |

**总体质量**：高。哲学基础扎实（TDD、《软件设计哲学》），工具链实用。

---

## 2. 迁移策略

### 2.1 个人品味评估框架

迁移前，按以下标准评估每个技能：

| 标准 | 问题 | 权重 |
|------|------|------|
| **使用频率** | 我在典型一周中会用到多少次？ | 高 |
| **痛点匹配** | 这是否解决了我当前工作流中的真实摩擦？ | 高 |
| **复杂度匹配** | 技能的复杂度是否与其价值成正比？ | 中 |
| **集成性** | 是否与我现有的工具链兼容？ | 中 |
| **可定制性** | 能否在不重写的前提下适应我的需求？ | 低 |
| **独特性** | 是否提供了我不容易手动实现的能力？ | 中 |

### 2.2 分层迁移计划

#### 第一层：核心工作流（立即迁移）

这些技能构成任何严肃开发工作流的骨架：

1. **systematic-debugging**（superpowers）——铁律：没有根因就不修 Bug。防止最常见开发者错误。
2. **tdd**（mattprocock）——红-绿-重构 + 垂直切片。哲学上自洽。
3. **brainstorming**（superpowers）——苏格拉底式设计流程，防止过早实现。
4. **finishing-a-development-branch**（superpowers）——清晰的 merge/PR/keep/discard 决策。
5. **design-an-interface**（mattprocock）——"设计两次"原则，产出更好的 API。
6. **git-guardrails-claude-code**（mattprocock）——破坏性操作的安全网。

#### 第二层：增强技能（按需迁移）

在特定场景中提供显著价值的技能：

7. **subagent-driven-development**（superpowers）——适用于大型计划中的独立任务。
8. **triage-issue**（mattprocock）——Bug 调查 → TDD 修复计划工作流。
9. **receiving-code-review**（superpowers）——Code Review 回应中的技术严谨性。
10. **request-refactor-plan**（mattprocock）——安全的增量重构。
11. **setup-pre-commit**（mattprocock）——项目脚手架代码质量工具。
12. **write-a-skill**（mattprocock）——用于扩展集合的元技能。
13. **executing-plans**（superpowers）——基于书面计划工作时使用。

#### 第三层：场景技能（保留参考）

有用但属于小众场景的技能：

14. **dispatching-parallel-agents**（superpowers）——多个独立故障场景。
15. **qa**（mattprocock）——对话式 QA 会话。
16. **grill-me**（mattprocock）——设计压力测试。
17. **github-triage**（mattprocock）——代理简报模板。
18. **requesting-code-review**（superpowers）——Code Review 请求。
19. **scaffold-exercises**（mattprocock）——练习脚手架。

#### 第四层：跳过或替换

过于小众或可用更简单方案替代的技能：

20. **edit-article**（mattprocock）——对大多数开发者用处有限。
21. **migrate-to-shoehorn**（mattprocock）——过于 TypeScript 特定。
22. **obsidian-vault**（mattprocock）——仅对 Obsidian 用户有用。

### 2.3 迁移流程

对每个被迁移的技能：

```
1. 克隆技能目录结构
2. 透彻阅读并理解 SKILL.md
3. 将技能适配为个人惯例：
   - 更新触发短语以匹配自然语言习惯
   - 调整工具引用以匹配实际工具链
   - 移除与当前工作流无关的部分
   - 添加个人偏好和约束
4. 用 2-3 个真实场景测试技能
5. 根据测试结果精炼
```

### 2.4 个人适配清单

适配迁移技能时：

- [ ] **触发词**：激活短语是否符合我自然求助的方式？
- [ ] **工具引用**：所有引用的工具是否已安装和配置？
- [ ] **路径约定**：文件路径是否匹配我的项目结构？
- [ ] **语言偏好**：指令应为英文、中文还是双语？
- [ ] **脚本依赖**：所有脚本依赖是否可用？
- [ ] **集成点**：是否与其他技能正确连接？
- [ ] **上下文窗口**：技能是否足够精简（SKILL.md < 500 行）？
- [ ] **渐进式披露**：详细信息是否在 references/ 而非 SKILL.md 中？

---

## 3. 推荐的个人技能集合架构

```
personal-skills/
├── SKILL.md                          # 所有个人技能索引
├── core/                             # 第一层：始终可用
│   ├── systematic-debugging/
│   ├── tdd/
│   ├── brainstorming/
│   ├── finishing-a-development-branch/
│   ├── design-an-interface/
│   └── git-guardrails/
├── workflow/                          # 第二层：按项目加载
│   ├── subagent-driven-development/
│   ├── triage-issue/
│   ├── receiving-code-review/
│   ├── request-refactor-plan/
│   ├── executing-plans/
│   └── write-a-skill/
└── reference/                         # 第三层：按需加载
    ├── dispatching-parallel-agents/
    ├── qa/
    ├── grill-me/
    └── setup-pre-commit/
```

### 加载策略

- **核心技能**：通过 CLAUDE.md 或 settings.json 始终加载
- **工作流技能**：按项目通过 `.claude/settings.json` 加载
- **参考技能**：按需可用，不预加载

---

## 4. 源仓库关键模式

### 4.1 值得采纳的模式（来自两个仓库）

| 模式 | 来源 | 描述 |
|------|------|------|
| 铁律原则 | superpowers/systematic-debugging | 防止常见错误的绝对规则 |
| 渐进式披露 | mattprocock/write-a-skill | SKILL.md < 500 行，详细信息在 references/ |
| 双阶段审查 | superpowers/subagent-driven-development | 先检查规格合规，再检查代码质量 |
| 设计两次 | mattprocock/design-an-interface | 生成多个根本不同的方案 |
| 垂直切片 | mattprocock/tdd | 测试完整行为，而非水平层级 |
| 质量关卡 | superpowers/finishing-a-branch | 继续之前必须通过的检查 |
| 持久化规格 | mattprocock/github-triage | 面向行为而非路径的规格 |

### 4.2 应避免的反模式

| 反模式 | 为什么避免 |
|--------|-----------|
| SKILL.md 过长 | 浪费上下文窗口，降低遵循度 |
| 硬编码文件路径 | 项目结构变更时会失效 |
| 缺少触发短语 | 代理无法发现该技能 |
| 无错误处理 | 脚本失败时代理会幻觉 |
| 仅过程式指令 | 代码变更时脆弱；优先行为式规格 |
