# 非前端开发者使用 Frontend Skill 指南

> 目标：解决"后端开发者想要美观前端界面，但缺乏前端经验"的问题。
> 核心思路：AI 生成 Mockup → Skill 精确调用组件 → 快速迭代

---

## 一、问题分析

### 1.1 后端开发者使用 Frontend Skill 的痛点

| 痛点 | 具体表现 |
|------|---------|
| **不会描述布局** | "我想要一个好看的 dashboard" — 太模糊，AI 无法精确生成 |
| **不了解组件** | 不知道有哪些组件可用，不知道组件的 props 有哪些 |
| **布局想象困难** | 脑中只有模糊的画面，无法转化为精确的组件组合指令 |
| **调试成本高** | 生成的界面不满意，反复修改消耗大量 token/credits |

### 1.2 为什么直接用文字描述布局容易出错

以 Dashboard 为例：

```
❌ 模糊描述：
"创建一个 dashboard，有侧边栏、顶部导航、数据卡片"
→ AI 可能生成：
   - 侧边栏在左边还是右边？
   - 数据卡片是 2 列还是 3 列？
   - 顶部导航包含什么菜单？
   - 暗色还是亮色主题？

✅ 精确描述：
"创建 dashboard：左侧固定 240px 侧边栏（Logo + 5 个导航项），
  顶部 64px 导航栏（搜索框 + 用户头像下拉菜单），
  主内容区 3 列等宽卡片网格（每卡片含标题+数字+趋势图标），
  底部 48px 状态栏"
```

**关键洞察**：布局问题本质上是"空间关系"问题，文字描述天然不擅长表达空间关系。

---

## 二、解决方案：Mockup-Driven Development

### 2.1 核心流程

```
后端开发者想法
    ↓
[Step 1] AI 生成 Mockup（视觉草稿）
    ↓
[Step 2] 开发者确认/调整 Mockup
    ↓
[Step 3] Skill 根据 Mockup 精确调用组件
    ↓
[Step 4] 生成代码 + 运行验证
    ↓
[Step 5] 微调（循环 Step 1-4）
```

### 2.2 Step 1: AI 生成 Mockup 的工具选择

| 工具 | 用法 | 成本 | 输出 |
|------|------|------|------|
| **v0.dev** | 截图/文字 → React 组件 | 免费 $5/月 | 可交互原型 + React 代码 |
| **Claude Artifacts** | 文字描述 → 实时预览 | 免费（Claude 内）| HTML/CSS 原型 |
| **shadcn/ui Builder** | `npx shadcn create` → 可视化配置 | 免费 | 完整项目脚手架 |
| **Lovable** | 文字 → 全栈应用 | 免费 5 msg/天 | 完整可部署应用 |
| **Figma + AI 插件** | 文字 → Figma 设计稿 | Figma 免费版 | 设计稿（需人工转代码）|

**推荐方案（后端开发者）**：

**方案 A：Claude Artifacts（零成本，最简）**
```
对 Claude 说：
"请生成一个 Dashboard 的 HTML mockup，包含：
- 左侧深色侧边栏
- 顶部搜索栏
- 中间 4 个 KPI 卡片
- 底部数据表格
请用 Tailwind CSS 类名，让我可以直接预览效果"
```
→ Claude 生成可实时预览的 HTML，开发者确认后让 Claude 用 Skill 规范重写为 React 组件。

**方案 B：v0.dev（质量最高）**
```
在 v0.dev 输入：
"Dashboard with sidebar navigation, search bar, 4 KPI cards in a grid,
 and a data table at the bottom. Dark mode, zinc color scheme."
```
→ v0 生成 React + Tailwind 组件，导出代码后交给 Skill 整合到项目中。

**方案 C：shadcn/ui Builder（最符合 Skill 规范）**
```bash
npx shadcn@latest create
# 在浏览器中可视化选择：
# - Framework: Next.js
# - Base color: Zinc
# - Style: New York
# - Components: 勾选需要的组件
# - 生成命令后运行
```

### 2.3 Step 2-3: 从 Mockup 到 Skill 精确调用

**关键技巧：让 AI "读取" Mockup 后再生成代码**

```
用户操作：
1. 截图保存 Mockup（或复制 v0 生成的代码）
2. 对 AI 说："请根据这张 mockup，使用 innate-frontend Skill 规范实现"

AI 处理流程：
1. 分析 Mockup 结构（识别组件类型和布局关系）
2. 映射到 Skill 中的组件清单
3. 生成精确的组件调用代码
```

**示例映射表**：

| Mockup 中的视觉元素 | 对应 Skill 组件 | 安装命令 |
|-------------------|---------------|---------|
| 顶部导航栏 + Logo | Navbar / NavigationMenu | `npx shadcn@latest add navigation-menu` |
| 左侧图标导航 | Sidebar | `npx shadcn@latest add sidebar` |
| 数字展示卡片 | Card + 自定义样式 | `npx shadcn@latest add card` |
| 数据表格 | Table | `npx shadcn@latest add table` |
| 趋势图表 | Chart (recharts) | `npx shadcn@latest add chart` |
| 搜索输入框 | Input + Command | `npx shadcn@latest add input command` |
| 用户头像下拉 | Avatar + DropdownMenu | `npx shadcn@latest add avatar dropdown-menu` |

---

## 三、实践建议

### 3.1 给后端开发者的 Skill 使用流程

```markdown
## 我想要一个前端界面

### Step 1: 生成 Mockup
对 Claude 说："请用 HTML + Tailwind 生成一个 [功能] 的 mockup，
要求：[具体布局描述]。请用 Artifacts 预览。"

### Step 2: 确认并截图
- 调整 mockup 直到满意
- 截图保存

### Step 3: 交给 Skill 实现
对 Claude 说："请根据这张 mockup，使用 innate-frontend Skill：
1. 识别 mockup 中的所有组件
2. 使用 `npx shadcn@latest add` 安装需要的组件
3. 按照 mockup 的精确布局实现代码
4. 使用 @innate/ui 的主题系统"
```

### 3.2 在 Skill 中增加"Mockup 优先"提示

建议在 innate-frontend SKILL.md 的「触发条件」后增加：

```markdown
## 非前端开发者快速开始

如果你不熟悉前端开发，请按以下顺序：

1. **先生成 Mockup**：对 AI 说"请生成 [功能] 的 HTML mockup"
2. **确认布局**：通过预览调整直到满意
3. **截图给 Skill**："请根据这张 mockup 实现"

这样比直接用文字描述布局精确 10 倍。
```

### 3.3 推荐的 Mockup 粒度

| 粒度 | 适合场景 | 示例 |
|------|---------|------|
| **页面级** | 完整页面 | "生成 Dashboard 页面 mockup" |
| **区块级** | 页面局部 | "生成 Hero Section mockup" |
| **组件级** | 单一组件 | "生成带搜索和过滤的数据表格 mockup" |

**建议**：后端开发者从**页面级**开始，先看到整体效果，再逐块细化。

---

## 四、与现有工具的对比

| 方式 | 精确度 | 速度 | 成本 | 适合谁 |
|------|--------|------|------|--------|
| 纯文字描述 | 低 | 快 | 低 | 前端专家 |
| Mockup → Skill | 高 | 中 | 低 | **后端开发者（推荐）** |
| v0.dev 直接生成 | 高 | 快 | 中 | 全栈开发者 |
| Lovable 全栈生成 | 高 | 快 | 高 | 非开发者 |
| Figma 设计稿 | 最高 | 慢 | 高 | 设计师 |

---

## 五、总结

**核心结论**：

1. **后端开发者不应直接用文字描述布局** — 空间关系用文字表达天然不精确
2. **Mockup 是桥梁** — 先用 AI 生成视觉草稿，确认后再转代码，精确度提升 10 倍
3. **Claude Artifacts 是最简单的 Mockup 工具** — 零成本、实时预览、可直接修改
4. **Skill 应内置"Mockup 优先"工作流** — 降低非前端开发者的使用门槛

**给 Skill 的改进建议**：

在 innate-frontend SKILL.md 中增加「非前端开发者指南」章节，明确：
- 先用 AI 生成 Mockup
- 确认后截图给 Skill
- Skill 自动映射 Mockup → 组件 → 代码
