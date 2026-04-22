# innate-next-mono Web Application 实现计划

> 评估 innate-next-mono 最初计划的 web application 项目是否可实现，并给出实现方案。
> 该项目目标：让用户在浏览器中浏览组件、选择组件、生成 AI Task。

---

## 一、原始计划评估

### 1.1 当前 frontend-tpl/ 目录现状

```
innate-next-mono/frontend-tpl/
├── ai-sdk-rag-chatbot-template/          # 空目录
├── awesome-shadcn-ui/                    # 空目录
├── Folo/                                 # 空目录
├── reui/                                 # 空目录
├── shadcn-cheatsheet/                    # 空目录
├── shadcn-dashboard-landing-template/    # 空目录
├── shadcn-ui/                            # 空目录
├── tweakcn/                              # 空目录
├── ui/                                   # 空目录
└── velocify/                             # 空目录
```

**结论**：`frontend-tpl/` 下全是空目录，说明之前有计划收集各种模板项目，但从未实际填充内容。这个目录结构可以重新利用或废弃。

### 1.2 原始 Web Application 构想

根据 Task 7 第 5-6 点的描述，用户最初想实现：

> "一个 web 页面，让用户直接在浏览器中打开，看到需要的组件、block，然后生成 AI 可以明白的内容，再进行 Task 的编写"

这本质上是一个 **"组件可视化选择器 + AI Task 生成器"**。

---

## 二、可行性评估

### 2.1 功能拆解

| 功能模块 | 技术难度 | 说明 |
|---------|---------|------|
| 组件展示（带预览） | 中 | iframe 嵌入或截图展示 |
| 组件选择（勾选） | 低 | 状态管理即可 |
| 生成安装命令 | 低 | 字符串拼接 |
| 生成 AI Task 描述 | 低 | 模板填充 |
| 暗色/亮色预览 | 低 | next-themes |
| 搜索/过滤组件 | 低 | 前端过滤 |
| 组件分类导航 | 低 | 静态分类 |

### 2.2 整体可行性

**结论：完全可行，且开发成本不高。**

原因：
1. 所有功能都是纯前端，无需后端
2. 可以静态导出部署到 GitHub Pages
3. 组件元数据可以用 JSON 文件静态维护
4. 预览可以用 iframe 嵌入 shadcn/ui 文档和 21st.dev

---

## 三、实现方案

### 3.1 项目名称和定位

```
apps/component-studio/   # 建议的目录名
```

**定位**：Innate 组件工作室 — 浏览、选择、生成的一站式工具。

### 3.2 页面结构

```
/component-studio/
├── /                     # 首页：组件总览 + 快速开始
├── /browse               # 组件浏览器：分类网格 + 搜索
│   └── ?category=buttons&source=shadcn
├── /preview/[id]         # 单个组件预览
├── /builder              # 选择器 + 已选面板
│   └── 生成命令 / 生成 Task
├── /templates            # 项目模板预设
│   └── /landing
│   └── /dashboard
│   └── /admin
└── /docs                 # 使用指南
```

### 3.3 核心页面实现

#### 首页 `/`

```tsx
// 快速入口：
// - "我想创建 Landing Page" → 跳转到 /builder?template=landing
// - "我想创建 Dashboard" → 跳转到 /builder?template=dashboard
// - "浏览所有组件" → 跳转到 /browse
// - "查看使用指南" → 跳转到 /docs
```

#### 组件浏览器 `/browse`

```tsx
// 左侧：分类导航
//   - shadcn/ui 官方
//   - 21st.dev 营销区块
//   - Aceternity UI 动画
//   - @innate/ui 业务区块
//
// 右侧：组件网格
//   - 每张卡片：预览图 + 名称 + 来源 + "添加"按钮
//   - 点击卡片：展开详情 + iframe 预览
```

#### 构建器 `/builder`

```tsx
// 三栏布局：
// 左侧：组件分类（可折叠）
// 中间：已选组件列表（可拖拽排序）
// 右侧：生成面板
//   - 安装命令（可复制）
//   - AI Task 描述（可复制）
//   - 导出为 JSON
```

### 3.4 数据层设计

```typescript
// lib/component-registry.ts

interface Component {
  id: string;
  name: string;
  description: string;
  source: "shadcn" | "21st" | "aceternity" | "innate";
  category: string;
  installCommand: string;
  previewUrl: string;      // iframe src
  thumbnailUrl?: string;   // 截图
  props?: PropDefinition[];
  tier: 1 | 2 | 3;
}

interface Template {
  id: string;
  name: string;
  description: string;
  components: string[];    // component ids
  layout: string;          // 布局描述
}

// 数据来源：
// - shadcn/ui：从官方 docs 抓取或手动维护
// - 21st.dev：从 API 或手动维护
// - @innate/ui：从 packages/ui/src/block/ 读取
```

### 3.5 关键交互流程

```
用户流程 A：从零开始构建页面
1. 打开 /component-studio/builder
2. 选择"Landing Page"模板
3. 模板自动添加推荐组件：
   - Hero Section（21st.dev）
   - Features Grid（21st.dev）
   - CTA（21st.dev）
   - Footer（21st.dev）
4. 用户添加额外组件：
   - 点击"添加组件" → 弹出 /browse 选择器
   - 选择"Testimonials Section"
5. 调整组件顺序（拖拽）
6. 点击"生成"
7. 右侧面板展示：
   - 安装命令（一键复制）
   - AI Task 描述（一键复制）
   - 预览链接

用户流程 B：浏览发现组件
1. 打开 /component-studio/browse
2. 搜索"table"
3. 看到 Table（shadcn/ui）+ Data Grid（21st.dev）
4. 点击 Table 卡片 → iframe 预览
5. 满意后点击"添加到项目"
6. 跳转到 /builder，Table 已在列表中
```

---

## 四、技术实现细节

### 4.1 项目初始化

```bash
cd apps/component-studio
npx shadcn@latest init --yes --template next --base-color zinc

# 安装额外依赖
npm install @dnd-kit/core @dnd-kit/sortable  # 拖拽排序
npm install lucide-react                      # 图标
npm install next-themes                       # 暗色模式
```

### 4.2 组件预览方案

| 方案 | 实现方式 | 优点 | 缺点 |
|------|---------|------|------|
| **iframe 嵌入** | `<iframe src="https://ui.shadcn.com/docs/components/button">` | 实时、真实 | 跨域限制、加载慢 |
| **截图展示** | 预生成 PNG/SVG 截图 | 快速、离线可用 | 需要定期更新截图 |
| **代码实时渲染** | 用 Sandpack/StackBlitz 渲染 | 可交互、精确 | 复杂、体积大 |

**推荐：截图 + iframe 回退**

```tsx
// 组件卡片
<ComponentCard>
  <div className="aspect-video bg-gray-100 rounded">
    {hasScreenshot ? (
      <img src={`/previews/${component.id}.png`} />
    ) : (
      <iframe src={component.previewUrl} loading="lazy" />
    )}
  </div>
  <h3>{component.name}</h3>
  <Button onClick={() => addToProject(component.id)}>
    添加
  </Button>
</ComponentCard>
```

### 4.3 暗色/亮色预览切换

```tsx
// 在 builder 页面提供主题切换
<ThemeToggle />

// 组件预览区域包裹在 ThemeProvider 中
<ThemeProvider attribute="class" defaultTheme={selectedTheme}>
  <PreviewArea>
    {/* 渲染已选组件的预览 */}
  </PreviewArea>
</ThemeProvider>
```

---

## 五、实现计划

| 阶段 | 任务 | 预估时间 |
|------|------|---------|
| **Day 1** | 项目初始化 + 首页 + 基础布局 | 4h |
| **Day 1** | 组件元数据 JSON 设计 + 数据填充 | 3h |
| **Day 2** | 组件浏览器 /browse 页面 | 4h |
| **Day 2** | 构建器 /builder 页面（选择 + 列表） | 4h |
| **Day 3** | 拖拽排序 + 生成面板 | 3h |
| **Day 3** | 模板预设 + 搜索过滤 | 3h |
| **Day 4** | 预览优化 + 截图生成 | 3h |
| **Day 4** | 暗色模式 + 响应式适配 | 2h |
| **Day 5** | 测试 + 部署到 GitHub Pages | 3h |

**总计：约 5 天（一个人全职）**

---

## 六、与 Skill 的集成

### 6.1 Skill 中如何引用 Component Studio

在 innate-frontend SKILL.md 中增加：

```markdown
## Component Studio（可视化工具）

如果你不确定需要哪些组件，或想可视化预览后再决定：

1. 打开 https://variableway.github.io/innate-next-mono/component-studio
2. 浏览组件并勾选需要的
3. 复制生成的安装命令或 AI Task 描述
4. 粘贴到终端或给 AI 执行
```

### 6.2 AI 如何使用 Component Studio

当用户说"我想创建一个 dashboard"时，AI 可以：

1. 先询问用户是否需要使用 Component Studio 选择组件
2. 或直接推荐默认的 Dashboard 模板组件组合
3. 生成代码时引用 Component Studio 中的组件 ID

---

## 七、总结

| 评估项 | 结论 |
|--------|------|
| 技术可行性 | ✅ 完全可行，纯前端项目 |
| 开发成本 | 🟡 中等，约 5 天全职开发 |
| 维护成本 | 🟡 中低，需要定期同步组件列表 |
| 用户价值 | ✅ 高，大幅降低非前端开发者使用门槛 |
| 与 Skill 协同 | ✅ 高，Skill 引用 Studio，Studio 生成 Skill Task |

**核心建议**：
1. **使用 `apps/component-studio/` 作为项目目录**（废弃空的 `frontend-tpl/`）
2. **先实现 MVP**：浏览 + 选择 + 生成命令（3 天）
3. **截图预览优先**，iframe 预览作为增强
4. **与 Skill 深度集成**：Skill 引导用户到 Studio，Studio 生成 Skill 任务
