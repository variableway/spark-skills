# Template 项目组件安装策略与可视化选择器方案

> 目标：解决"template 项目如何干净安装组件"和"如何让用户直观选择组件"的问题。

---

## 一、问题分析

### 1.1 当前 Template 项目的组件安装问题

innate-next-mono 目前的 `scripts/init-starter.sh` 会一次性安装所有组件：

```bash
npx shadcn@latest add button card dialog sidebar tabs table badge avatar ...
```

**问题**：
- 安装了大量可能用不到的组件（"臃肿"）
- 没有选择性安装的机制
- 用户不知道有哪些组件可用

### 1.2 两种安装策略对比

| 策略 | 描述 | 优点 | 缺点 |
|------|------|------|------|
| **全量安装** | 一次性安装所有常用组件 | 简单、开箱即用 | 项目臃肿、依赖过多、启动慢 |
| **按需安装** | 使用时才安装需要的组件 | 项目干净、依赖精简 | 需要知道组件名称、多次执行命令 |

**推荐：混合策略** — 基础组件全量安装，高级/营销组件按需安装。

---

## 二、推荐的组件安装策略

### 2.1 三层组件分类

```
Tier 1: 基础组件（必装）
├── button, card, input, label, separator
├── dialog, sheet, dropdown-menu
├── avatar, badge, skeleton
└── toast, sonner

Tier 2: 布局组件（按项目类型安装）
├── sidebar, navigation-menu, tabs, accordion
├── table, pagination, scroll-area
├── breadcrumb, menubar
└── resizable, collapsible

Tier 3: 营销/高级组件（按需安装）
├── 21st.dev: hero, features, pricing, cta, testimonials
├── Aceternity UI: animated components, effects
├── Magic UI: particles, backgrounds, animations
└── chart (recharts): data visualization
```

### 2.2 分层安装脚本

```bash
#!/usr/bin/env bash
# scripts/init-starter.sh — 分层安装

set -euo pipefail

cd apps/web

echo "📦 Tier 1: 安装基础组件（必装）"
npx shadcn@latest add -y -o \
  button card input label separator \
  dialog sheet dropdown-menu \
  avatar badge skeleton \
  toast sonner

echo ""
echo "🧩 Tier 2: 安装布局组件"
read -p "是否需要 Dashboard 布局组件？(y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  npx shadcn@latest add -y -o \
    sidebar navigation-menu tabs accordion \
    table pagination scroll-area
fi

echo ""
echo "🎨 Tier 3: 安装营销区块"
read -p "是否需要 Landing Page 营销区块？(y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  npx shadcn@latest add "https://21st.dev/r/serafim/hero"
  npx shadcn@latest add "https://21st.dev/r/serafim/features"
  npx shadcn@latest add "https://21st.dev/r/serafim/pricing"
  npx shadcn@latest add "https://21st.dev/r/serafim/cta"
fi

echo ""
echo "✅ 安装完成！"
```

### 2.3 基于项目类型的预设安装

```bash
# scripts/init-by-type.sh

case "$1" in
  "landing")
    echo "初始化 Landing Page 项目..."
    npx shadcn@latest add button card input separator
    npx shadcn@latest add "https://21st.dev/r/serafim/hero"
    npx shadcn@latest add "https://21st.dev/r/serafim/features"
    npx shadcn@latest add "https://21st.dev/r/serafim/pricing"
    npx shadcn@latest add "https://21st.dev/r/serafim/cta"
    ;;
  "dashboard")
    echo "初始化 Dashboard 项目..."
    npx shadcn@latest add button card input table sidebar
    npx shadcn@latest add tabs accordion pagination
    npx shadcn@latest add chart  # recharts
    ;;
  "admin")
    echo "初始化 Admin 后台项目..."
    npx shadcn@latest add button input table form select
    npx shadcn@latest add dialog dropdown-menu navigation-menu
    ;;
  *)
    echo "用法: ./init-by-type.sh [landing|dashboard|admin]"
    exit 1
    ;;
esac
```

---

## 三、可视化组件选择器方案

### 3.1 方案概述

**目标**：创建一个 Web 页面，让用户在浏览器中：
1. 浏览所有可用组件（带预览）
2. 勾选需要的组件
3. 一键生成安装命令
4. 生成 AI 可以理解的 Task 描述

### 3.2 技术实现

```
apps/component-picker/  # 新增：组件选择器应用
├── app/
│   ├── page.tsx          # 主页面：组件网格 + 选择器
│   ├── preview/
│   │   └── [id]/page.tsx # 单个组件预览页面
│   └── api/
│       └── generate/route.ts  # 生成安装命令 API
├── components/
│   ├── component-card.tsx     # 组件卡片（缩略图 + 名称 + 勾选框）
│   ├── component-grid.tsx     # 组件网格布局
│   ├── selected-panel.tsx     # 已选组件面板
│   └── install-command.tsx    # 安装命令展示
├── data/
│   └── components.json        # 组件元数据（来源 registry）
└── package.json
```

### 3.3 组件元数据结构

```json
// data/components.json
{
  "categories": [
    {
      "name": "基础组件",
      "components": [
        {
          "id": "button",
          "name": "Button",
          "description": "按钮组件，支持多种变体",
          "source": "shadcn/ui",
          "install": "npx shadcn@latest add button",
          "preview": "https://ui.shadcn.com/docs/components/button",
          "tier": 1
        },
        {
          "id": "card",
          "name": "Card",
          "description": "卡片容器",
          "source": "shadcn/ui",
          "install": "npx shadcn@latest add card",
          "preview": "https://ui.shadcn.com/docs/components/card",
          "tier": 1
        }
      ]
    },
    {
      "name": "营销区块",
      "components": [
        {
          "id": "21st-hero",
          "name": "Hero Section",
          "description": "英雄区域，带标题和 CTA",
          "source": "21st.dev",
          "install": "npx shadcn@latest add 'https://21st.dev/r/serafim/hero'",
          "preview": "https://21st.dev/r/serafim/hero",
          "tier": 3
        }
      ]
    }
  ]
}
```

### 3.4 页面交互流程

```
用户打开 /component-picker
    ↓
看到分类网格：基础组件 | 布局组件 | 营销区块 | 动画效果
    ↓
点击组件卡片 → 展开预览（iframe 或 截图）
    ↓
勾选需要的组件 → 右侧已选面板实时更新
    ↓
点击"生成命令" → 展示：
   - shadcn/ui 安装命令
   - 21st.dev 安装命令
   - AI Task 描述（"我需要实现一个包含 Button、Card、Hero Section 的页面..."）
    ↓
复制命令到终端执行，或复制 Task 描述给 AI
```

### 3.5 与 AI 的集成

**生成 AI Task 描述的模板**：

```markdown
我需要创建一个前端页面，使用以下组件：

**基础组件**（shadcn/ui）：
- Button、Card、Input、Dialog

**布局组件**（shadcn/ui）：
- Sidebar、Table、Tabs

**营销区块**（21st.dev）：
- Hero Section（标题："欢迎使用"，副标题："快速搭建应用"）
- Features Section（3 个特性卡片）

**主题**：使用 @innate/ui 的 OKLCH 主题系统（zinc 色系）
**字体**：Manrope（body）+ Sora（display）
**技术栈**：Next.js 16 + Tailwind CSS v4

请使用 innate-frontend Skill 实现这个页面。
```

---

## 四、可行性与实现计划

### 4.1 可行性评估

| 维度 | 评估 |
|------|------|
| 技术可行性 | ✅ 高 — Next.js + iframe 预览即可实现 |
| 数据维护 | ⚠️ 中 — 需要定期同步 shadcn/ui 和 21st.dev 的组件列表 |
| 用户体验 | ✅ 高 — 可视化选择比命令行直观得多 |
| 开发成本 | 🟡 中 — 约 1-2 天开发时间 |

### 4.2 实现计划

| 阶段 | 任务 | 时间 |
|------|------|------|
| Phase 1 | 创建 `apps/component-picker/` 项目骨架 | 2h |
| Phase 2 | 实现组件网格 + 选择器 UI | 4h |
| Phase 3 | 集成组件预览（iframe/截图） | 3h |
| Phase 4 | 实现"生成命令"和"生成 Task"功能 | 3h |
| Phase 5 | 导入 shadcn/ui + 21st.dev 组件元数据 | 2h |
| Phase 6 | 测试 + 部署到 GitHub Pages | 2h |

**总计：约 2 天**

### 4.3 部署方案

```bash
# 部署到 GitHub Pages
cd apps/component-picker
next build --output export
# 推送到 gh-pages 分支
```

访问地址：`https://variableway.github.io/innate-next-mono/component-picker`

---

## 五、总结

| 问题 | 解决方案 |
|------|---------|
| 组件安装臃肿 | 三层分类 + 分层安装脚本 |
| 用户不知道有哪些组件 | 可视化组件选择器 Web 页面 |
| 手动写安装命令易错 | 勾选后自动生成安装命令 |
| AI 不理解组件需求 | 勾选后自动生成 AI Task 描述 |

**核心建议**：
1. **立即实施**：分层安装脚本（`scripts/init-by-type.sh`）— 成本低、收益高
2. **短期实施**：可视化组件选择器 — 大幅提升非前端开发者体验
3. **长期维护**：组件元数据 JSON 需要定期同步社区更新
