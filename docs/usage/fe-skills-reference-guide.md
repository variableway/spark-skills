# FE Skills 示范代码引用策略指南

> 本文档分析现有参考项目与 fe-skills 的对应关系，并给出如何在 Skill 中引用这些项目作为示范代码的具体建议。

---

## 一、现状分析

### 1.1 当前 Skill 的代码示例问题

| 问题 | 说明 |
|------|------|
| 只有片段代码 | SKILL.md 中包含大量代码片段（如 Button 用法、Tauri IPC 模式），但缺乏**完整的页面/模块级示范** |
| 外链依赖 | 引用了 GitHub 项目链接，但 AI Agent 在离线环境或无法访问外部网络时无法读取 |
| 无项目级示范 | 没有展示"一个完整的页面/功能是如何组织的"，只有零散的模式 |
| 缺乏演进对比 | 没有展示从简单到复杂的渐进式实现路径 |

### 1.2 参考项目与 Skill 的映射关系

| 项目 | 对应 Skill | 角色定位 | 可提取的示范价值 |
|------|-----------|---------|-----------------|
| [innate-next-mono](https://github.com/variableway/innate-next-mono) | `innate-frontend` | **核心源项目** | 组件库实现、Monorepo 结构、主题系统 |
| [innate-websites](https://github.com/variableway/innate-websites) | `innate-frontend` | **应用实例** | Landing Page 完整实现、Dashboard 布局、数据流 |
| [innate-executable](https://github.com/variableway/innate-executable) | `desktop-app` | **桌面应用模板** | Tauri + Next.js 整合、教程系统、PTY 终端 |
| [21st-dev/1code](https://github.com/21st-dev/1code) | `desktop-app` | **高级参考** | 多 Agent 架构、Diff UI、Git 集成、Terminal 面板 |
| [serafimcloud/21st](https://github.com/serafimcloud/21st) | `innate-frontend` | **设计参考** | 组件发布规范、Demo 模式、主题系统设计 |

---

## 二、示范代码引用策略

### 策略 1: 在 Skill 中增加「示范项目」章节

在每个 SKILL.md 中增加独立章节，引用具体项目并说明可学习的代码模式。

```markdown
## 示范项目

### 项目 A: innate-next-mono（组件库实现）
- **用途**: 学习 @innate/ui 组件库的内部实现
- **关键路径**:
  - `packages/ui/src/components/ui/button.tsx` — CVA 变体模式
  - `packages/ui/src/block/landing/hero-section.tsx` — Landing 区块组织
  - `packages/ui/src/globals.css` — OKLCH 主题变量定义

### 项目 B: innate-websites（应用实现）
- **用途**: 学习如何组合组件构建完整页面
- **关键路径**:
  - `apps/web/app/page.tsx` — Landing Page 完整实现
  - `apps/web/app/making/issues/page.tsx` — 数据列表页
  - `apps/web/components/layout/` — 自定义布局组件
```

### 策略 2: 在 references/ 下创建「示范代码索引」

为每个引用项目创建索引文档，列出可复制的关键代码文件路径和模式说明。

目录结构建议：

```
fe-skills/
├── innate-frontend/
│   ├── SKILL.md
│   └── references/
│       ├── component-catalog.md          # 已有：组件清单
│       ├── theme-system.md               # 已有：主题系统
│       └── demo-projects.md              # 新增：示范项目索引
├── desktop-app/
│   ├── SKILL.md
│   └── references/
│       ├── playground-mode.md            # 已有：PTY + 教程
│       ├── ai-chat-mode.md               # 已有：AI 聊天
│       └── demo-projects.md              # 新增：示范项目索引
```

### 策略 3: 将关键代码模式内联到 Skill 中

对于最常用、最复杂的模式，不应只给外链，而应把**精简后的完整代码**直接放在 SKILL.md 或 references/ 中。

需要内联的代码（按优先级）：

| 优先级 | 代码模式 | 来源项目 | 放入位置 |
|-------|---------|---------|---------|
| P0 | 完整 Landing Page 实现 | innate-websites | `references/demo-projects.md` |
| P0 | Tauri + Next.js 项目初始化结构 | innate-executable | `references/demo-projects.md` |
| P1 | Dashboard 布局（Sidebar + 主内容） | innate-websites | SKILL.md 或 references |
| P1 | Zustand + tauriStorage 完整实现 | innate-executable | `references/demo-projects.md` |
| P1 | PTY 终端前后端完整代码 | innate-executable | `references/playground-mode.md` |
| P2 | AI 聊天流式调用实现 | 1code / innate-executable | `references/ai-chat-mode.md` |
| P2 | 组件发布规范（code.tsx + demo.tsx） | 21st.dev | `references/component-patterns.md` |

### 策略 4: 使用 Git Submodule 或脚本同步（可选）

如果希望 Skill 中始终包含最新代码，可考虑：

```bash
# 方案 A: Git Submodule（不推荐，增加复杂度）
git submodule add https://github.com/variableway/innate-next-mono fe-skills/_demo/innate-next-mono

# 方案 B: 脚本定期拉取关键文件（推荐）
# 在 fe-skills/ 下创建 scripts/sync-demo-code.sh
# 定期从 GitHub 拉取关键文件到 references/demo-code/ 目录
```

**推荐做法**: 不直接复制整个仓库，而是**手动提取并精简**关键代码模式放入 references/ 中。原因：
1. 源项目可能包含大量与 Skill 无关的代码
2. 需要适配 Skill 的上下文（如 `@innate/ui` 包名）
3. 避免版权和仓库体积问题

---

## 三、具体建议：为每个项目做什么

### 3.1 innate-next-mono → 组件实现示范

**应提取的内容**：

```markdown
## @innate/ui 组件实现示范

来源: https://github.com/variableway/innate-next-mono

### Button 组件完整实现

`packages/ui/src/components/ui/button.tsx`

```tsx
// 完整源码展示 CVA + Radix UI + Tailwind 的结合方式
// ...（实际提取并精简后的代码）
```

### HeroSection Landing 区块

`packages/ui/src/block/landing/hero-section.tsx`

```tsx
// 展示如何构建一个可配置的业务区块组件
// ...
```

### globals.css 主题变量

`packages/ui/src/globals.css`

```css
/* OKLCH 主题变量完整定义 */
/* ... */
```
```

**操作建议**: 
- 创建 `fe-skills/innate-frontend/references/demo-projects.md`
- 提取 5-8 个最关键文件的精简代码
- 每个代码块前标注来源路径

### 3.2 innate-websites → 页面组装示范

**应提取的内容**：

- `apps/web/app/page.tsx` — 展示 Landing Page 如何组合多个 Section 组件
- `apps/web/app/making/layout.tsx` — Dashboard 布局模式
- `apps/web/app/making/issues/page.tsx` — 数据获取 + 列表渲染
- `apps/web/components/layout/app-shell.tsx` — 自定义布局壳

**操作建议**:
- 创建 `fe-skills/innate-frontend/references/demo-projects.md`（与上面同一文件）
- 重点展示"组装"而非"实现"——说明如何用 @innate/ui 的组件拼出完整页面

### 3.3 innate-executable → 桌面应用模板示范

**应提取的内容**：

- `apps/desktop/src-tauri/tauri.conf.json` — Tauri v2 配置模板
- `apps/desktop/src-tauri/src/lib.rs` — Rust 后端结构（含 PTY）
- `apps/desktop/src/app/layout.tsx` — 带 Tauri 检测的根布局
- `apps/desktop/src/lib/tauri-storage.ts` — Zustand 持久化适配器完整实现
- `apps/desktop/src/store/useAppStore.ts` — 全局状态管理

**操作建议**:
- 创建 `fe-skills/desktop-app/references/demo-projects.md`
- 这是 desktop-app skill 最核心的补充——目前 skill 只有模式片段，缺少完整项目骨架

### 3.4 21st-dev/1code → 高级功能参考

**应提取的内容**（选择性参考，不直接复制）：

- **Diff UI 模式**: 如何展示代码变更（可借鉴其 UI 设计思路）
- **Terminal 面板**: 底部/侧边栏终端的集成方式
- **Git 工作流 UI**: 可视化 git 操作界面
- **多 Agent 切换**: 前端状态管理架构

**操作建议**:
- 在 `fe-skills/desktop-app/references/advanced-examples.md` 中**描述性引用**
- 不复制代码，而是说明"1code 实现了 XX 功能，其核心思路是..."
- 提供对应功能的实现建议，而非直接代码

### 3.5 serafimcloud/21st → 组件设计规范参考

**应提取的内容**：

- **组件文件结构**: `code.tsx` + `demos/default/code.demo.tsx` 的分离模式
- **主题规范**: CSS 变量的使用方式
- **Demo 规范**: 如何用 props 驱动 demo 内容（而非 hardcode）

**操作建议**:
- 创建 `fe-skills/innate-frontend/references/component-patterns.md`
- 重点借鉴其**设计规范**，用于指导未来 @innate/ui 组件的演进

---

## 四、推荐执行步骤

### Step 1: 创建示范代码索引（高优先级）

```bash
# 创建文件
touch fe-skills/innate-frontend/references/demo-projects.md
touch fe-skills/desktop-app/references/demo-projects.md
```

内容：列出每个参考项目的关键文件路径、用途说明、可学习的模式。

### Step 2: 提取关键代码到 Skill（中优先级）

从 `innate-executable` 和 `innate-next-mono` 中提取最关键的实现代码：

1. **Tauri 项目完整骨架** → 放入 `desktop-app/references/demo-projects.md`
2. **Zustand + tauriStorage 完整实现** → 补充到 `desktop-app/SKILL.md`
3. **Landing Page 完整组装示例** → 补充到 `innate-frontend/SKILL.md`
4. **Button / Card 等核心组件源码** → 放入 `innate-frontend/references/demo-projects.md`

### Step 3: 在 SKILL.md 中增加「示范项目」章节（中优先级）

在两个 SKILL.md 的「参考资源」部分前增加：

```markdown
## 示范项目

以下开源项目展示了本 Skill 规范的实际应用。关键代码模式已提取到 [references/demo-projects.md](references/demo-projects.md)。

| 项目 | 说明 | 关键学习点 |
|------|------|-----------|
| [innate-next-mono](...) | 组件库源项目 | 组件内部实现、主题系统 |
| [innate-websites](...) | 网站应用实例 | 页面组装、Dashboard 布局 |
```

### Step 4: 建立同步机制（低优先级，可选）

如果源项目频繁更新，可创建同步脚本：

```bash
# fe-skills/scripts/sync-demo-code.sh
# 从 GitHub API 拉取特定文件的最新内容
# 更新到 references/demo-code/ 目录
```

---

## 五、注意事项

1. **版权与许可**: 引用自己仓库（variableway/*）无版权问题；引用第三方项目（21st-dev/*）时应遵循其许可证（Apache 2.0），建议描述性引用而非直接复制大量代码。

2. **代码精简**: 不要复制整个文件，只提取与 Skill 模式相关的核心部分，去除业务逻辑噪音。

3. **版本锁定**: 在引用的代码块前标注版本/日期，因为 shadcn/ui、Tauri 等依赖会升级。

4. **保持 Skill 体积可控**: 示范代码应放入 `references/` 下的独立文件，而非全部内联到 SKILL.md，避免主文件过长影响 Agent 读取效率。

5. **URL 稳定性**: GitHub 文件链接使用 permalink（包含 commit hash），避免链接失效。
