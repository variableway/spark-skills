---
name: innate-frontend
description: "使用 Next.js + React 19 + TypeScript + Tailwind CSS v4 + @innate/ui 组件库快速搭建 Web 前端应用。提供 57 个 UI 组件、7 个 Landing 区块、Auth/Mail/Chat 业务区块、OKLCH 主题系统。配合 tauri-desktop-app Skill 可构建桌面应用。"
type: skill
supported_agents:
  - claude-code
  - kimi
  - codex
  - opencode
---

# Innate Frontend Skill

统一的 Web 前端开发 Skill，基于 [innate-next-mono](https://github.com/variableway/innate-next-mono) 项目提炼。

提供完整的 `@innate/ui` 组件库（57 个基础组件 + 7 个 Landing 区块 + Auth/Mail/Chat 业务区块），配合 Next.js 16 + Tailwind CSS v4 + OKLCH 主题系统。

> **桌面应用**：如需构建 Tauri 桌面应用，请使用 `tauri-desktop-app` Skill。本 Skill 聚焦 Web 前端。

## 技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| Next.js | 16+ | React 框架（App Router） |
| React | 19 | UI 库 |
| TypeScript | 6 | 类型安全 |
| Tailwind CSS | 4 | 样式系统（OKLCH 色彩空间） |
| @innate/ui | 0.1.0 | UI 组件库（基于 Radix UI） |
| pnpm | workspace | 包管理 + monorepo |
| Lucide React | latest | 图标库 |
| React Hook Form + Zod | latest | 表单验证 |
| Recharts | 3.x | 图表 |

## 触发条件

当用户说"创建 Web 应用"、"新建前端项目"、"创建页面"、"innate-frontend"、"使用 innate-ui 组件"等时触发。

当需要构建任何 Web 前端页面或组件时，应遵循本 Skill 的规范。

## 组件库总览

### 基础组件（57 个）

**表单控件**：Button, ButtonGroup, Input, InputGroup, InputOTP, Textarea, Select, Checkbox, RadioGroup, Switch, Slider, Field, Label, Form

**布局组件**：Card, Separator, ScrollArea, Resizable, AspectRatio, Collapsible, Sidebar, Container

**导航组件**：Tabs, Accordion, Breadcrumb, NavigationMenu, Menubar, Pagination

**数据展示**：Table, Badge, Avatar, Progress, Skeleton, Chart, Spinner, Kbd, Item

**反馈组件**：Alert, AlertDialog, Toast, Sonner, Tooltip, HoverCard

**覆盖层**：Dialog, Sheet, Drawer, Popover, DropdownMenu, ContextMenu, Command

**其他**：Calendar, Carousel, Toggle, ToggleGroup, Empty, useMobile, useToast

### 业务区块组件

**Landing 区块**（7 个）：
- `HeroSection` — 英雄区域，支持 badge、高亮标题、双 CTA
- `FeaturesSection` — 特性展示网格
- `PricingSection` — 价格方案
- `TestimonialsSection` — 用户评价
- `FaqSection` — 常见问题（手风琴式）
- `StatsSection` — 数据统计
- `CTASection` — 行动召唤

**Auth 区块**：LoginForm

**Mail 区块**：Inbox, MailList, MailDisplay

**Chat 区块**：ChatInterface, MessageList

## 使用指南

### Step 1: 导入组件

```tsx
// 基础组件 — 从 @innate/ui 直接导入
import { Button, Card, CardHeader, CardContent, Dialog, DialogTrigger, DialogContent } from "@innate/ui"

// 业务区块 — 同样从 @innate/ui 导入
import { HeroSection, FeaturesSection, PricingSection } from "@innate/ui"

// 工具函数
import { cn } from "@innate/ui"

// 样式（在 layout.tsx 中引入）
import "@innate/ui/globals.css"
```

### Step 2: 使用组件

```tsx
// 基础组件使用
<Card>
  <CardHeader>标题</CardHeader>
  <CardContent>内容</CardContent>
</Card>

// Button 变体
<Button variant="default">主要按钮</Button>
<Button variant="outline">轮廓按钮</Button>
<Button variant="ghost">幽灵按钮</Button>
<Button variant="destructive" size="sm">危险按钮</Button>
```

### Step 3: 使用 Landing 区块

```tsx
import { HeroSection, FeaturesSection, CTASection } from "@innate/ui"

export default function LandingPage() {
  return (
    <main>
      <HeroSection
        badge={{ text: "新版本发布" }}
        title="构建更好的产品"
        titleHighlight="更好"
        subtitle="使用我们的工具快速搭建现代化应用"
        primaryCta={{ text: "开始使用", href: "/start" }}
        secondaryCta={{ text: "了解更多", href: "/docs" }}
      />
      <FeaturesSection
        title="核心特性"
        features={[
          { title: "快速", description: "闪电般的性能", icon: <ZapIcon /> },
          { title: "安全", description: "企业级安全", icon: <ShieldIcon /> },
        ]}
      />
      <CTASection
        title="准备好了吗？"
        description="立即开始你的旅程"
        cta={{ text: "免费注册", href: "/signup" }}
      />
    </main>
  )
}
```

### Step 4: 暗色模式

```tsx
// 在 layout.tsx 中使用 next-themes
import { ThemeProvider } from "next-themes"

export default function RootLayout({ children }) {
  return (
    <ThemeProvider attribute="class" defaultTheme="system">
      {children}
    </ThemeProvider>
  )
}
```

## 组件编写规范

当需要创建新组件时，遵循以下模式：

### 基础组件模式

```tsx
"use client"

import * as React from "react"
import { cn } from "../../lib/utils"

interface MyComponentProps {
  className?: string
  children?: React.ReactNode
}

function MyComponent({ className, children }: MyComponentProps) {
  return (
    <div
      data-slot="my-component"
      className={cn("base-styles-here", className)}
    >
      {children}
    </div>
  )
}

export { MyComponent, type MyComponentProps }
```

### CVA 变体模式

```tsx
import { cva, type VariantProps } from "class-variance-authority"

const myVariants = cva("base-styles", {
  variants: {
    variant: {
      default: "bg-primary text-primary-foreground",
      outline: "border border-input bg-background",
      ghost: "hover:bg-accent",
    },
    size: {
      sm: "h-8 px-3 text-xs",
      default: "h-10 px-4 text-sm",
      lg: "h-12 px-6 text-base",
    },
  },
  defaultVariants: {
    variant: "default",
    size: "default",
  },
})
```

## 主题系统

使用 OKLCH 色彩空间，通过 CSS 变量定义：

| 变量 | 用途 |
|------|------|
| `--background` / `--foreground` | 页面背景和文字 |
| `--card` / `--card-foreground` | 卡片背景和文字 |
| `--primary` / `--primary-foreground` | 主色调 |
| `--secondary` / `--secondary-foreground` | 次色调 |
| `--muted` / `--muted-foreground` | 弱化色调 |
| `--accent` / `--accent-foreground` | 强调色调 |
| `--destructive` / `--destructive-foreground` | 危险/错误色 |
| `--border` / `--input` / `--ring` | 边框、输入框、焦点环 |
| `--chart-1` ~ `--chart-5` | 图表配色 |
| `--radius` | 基础圆角（sm/md/lg/xl 自动派生） |
| `--sidebar-*` | 侧边栏专用色 |

所有颜色在 `:root`（亮色）和 `.dark`（暗色）下都有定义。

## Monorepo 项目结构

```
project/
├── apps/
│   └── web/                        # Next.js Web 应用
│       ├── src/
│       │   ├── app/                # App Router 页面
│       │   │   ├── layout.tsx
│       │   │   ├── page.tsx
│       │   │   └── ...
│       │   └── components/         # 业务组件
│       ├── package.json
│       └── next.config.js
├── packages/
│   ├── ui/                         # @innate/ui 组件库
│   │   └── src/
│   │       ├── components/ui/      # 57 个基础组件
│   │       ├── block/              # 业务区块
│   │       │   ├── landing/        # Landing 页区块
│   │       │   ├── auth/           # 认证区块
│   │       │   ├── mail/           # 邮件区块
│   │       │   └── chat/           # 聊天区块
│   │       ├── lib/utils.ts        # cn() 工具
│   │       ├── globals.css         # Design tokens
│   │       └── index.ts            # 统一导出
│   ├── utils/                      # 工具函数
│   └── tsconfig/                   # TS 配置
├── pnpm-workspace.yaml
└── package.json
```

## 页面开发模式

### Landing Page 模式

```tsx
// app/page.tsx
import { HeroSection, FeaturesSection, PricingSection, FaqSection, CTASection } from "@innate/ui"

export default function LandingPage() {
  return (
    <main className="flex flex-col">
      <HeroSection {...} />
      <FeaturesSection {...} />
      <PricingSection {...} />
      <FaqSection {...} />
      <CTASection {...} />
    </main>
  )
}
```

### Dashboard 模式

```tsx
import { Sidebar, SidebarProvider, SidebarInset } from "@innate/ui"

export default function DashboardLayout({ children }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <SidebarInset>
        <main className="p-6">{children}</main>
      </SidebarInset>
    </SidebarProvider>
  )
}
```

### 表单模式

```tsx
import { Form, Field, Input, Button } from "@innate/ui"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
})

function LoginForm() {
  const form = useForm({ resolver: zodResolver(schema) })
  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <Field name="email" render={({ field }) => <Input {...field} />} />
        <Field name="password" render={({ field }) => <Input type="password" {...field} />} />
        <Button type="submit">登录</Button>
      </form>
    </Form>
  )
}
```

## 注意事项

1. **统一使用 @innate/ui**：所有前端项目使用统一的组件库，不要重复造轮子
2. **OKLCH 色彩空间**：自定义颜色时使用 `oklch()` 格式，与主题系统一致
3. **data-slot 属性**：组件根元素添加 `data-slot="component-name"` 用于样式定位
4. **cn() 合并类名**：始终使用 `cn()` 而非模板字符串合并 className
5. **"use client"**：所有交互组件必须添加客户端指令
6. **类型导出**：组件 Props 类型使用 `export type { XxxProps }` 导出

## 参考项目

- [innate-next-mono](https://github.com/variableway/innate-next-mono) — 组件库源项目
- [innate-executable](https://github.com/variableway/innate-executable) — Tauri + @innate/ui 使用示例
- [innate-websites](https://github.com/variableway/innate-websites) — 网站项目示例
- [tauri-desktop-app Skill](../tauri-desktop-app/SKILL.md) — 桌面应用开发 Skill
