---
name: tauri-desktop-app
description: "使用 Tauri + Next.js + TypeScript + Tailwind CSS + shadcn-ui 快速搭建跨平台桌面应用。提供完整的项目模板、UI 组件库、侧边栏布局、平台检测和 Tauri IPC 通信模式。"
type: skill
supported_agents:
  - claude-code
  - kimi
  - codex
  - opencode
---

# Tauri Desktop App Skill

使用 Tauri + Next.js 快速搭建跨平台桌面应用的 Skill。

从 [innate-executable](https://github.com/variableway/innate-executable) 项目提炼，包含完整的 monorepo 结构、56+ shadcn/ui 组件、侧边栏布局和 Tauri IPC 通信模式。

## 技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| Tauri | 2.x | 跨平台桌面框架 |
| Next.js | 16+ | React 框架（App Router） |
| React | 19 | UI 库 |
| TypeScript | 5+ | 类型安全 |
| Tailwind CSS | 4 | 样式系统 |
| shadcn/ui | latest | UI 组件库（基于 Radix UI） |
| pnpm | workspace | 包管理 + monorepo |
| Lucide React | latest | 图标库 |

## 项目结构

```
project/
├── apps/
│   └── desktop/                    # Tauri + Next.js 主应用
│       ├── src-tauri/             # Rust 后端
│       │   ├── src/
│       │   │   ├── main.rs
│       │   │   └── lib.rs         # Tauri Commands
│       │   ├── tauri.conf.json
│       │   ├── capabilities/
│       │   └── icons/
│       ├── src/
│       │   ├── app/               # Next.js App Router
│       │   │   ├── layout.tsx     # 根布局
│       │   │   ├── page.tsx       # 首页
│       │   │   └── settings/      # 设置页
│       │   └── components/
│       │       └── layout/        # 布局组件
│       │           ├── app-shell.tsx
│       │           ├── app-sidebar.tsx
│       │           └── status-bar.tsx
│       ├── package.json
│       └── tailwind.config.js
├── packages/
│   ├── ui/                        # 共享 UI 组件库
│   │   └── src/
│   │       ├── components/ui/     # shadcn/ui 组件
│   │       ├── lib/utils.ts       # cn() 工具
│   │       └── globals.css        # Design tokens
│   ├── utils/                     # 工具函数
│   │   └── src/index.ts
│   └── tsconfig/                  # 共享 TS 配置
│       ├── base.json
│       ├── nextjs.json
│       └── react-library.json
├── pnpm-workspace.yaml
└── package.json
```

## 使用指南

当用户说"创建桌面应用"、"新建 Tauri 项目"、"tauri-desktop-app"等时：

### Step 1: 初始化项目

```bash
# 创建项目目录
mkdir my-desktop-app && cd my-desktop-app

# 从模板复制结构
cp -r tauri-desktop-app/templates/* .

# 安装依赖
pnpm install

# 初始化 shadcn/ui（在 packages/ui 目录）
cd packages/ui && npx shadcn@latest init
```

### Step 2: 添加 UI 组件

```bash
# 在 packages/ui 目录下添加组件
cd packages/ui
npx shadcn@latest add button card sidebar dialog tabs
```

可用的 56+ 组件：
- **基础**：Button, Input, Label, Card, Badge, Separator
- **表单**：Form, Field, Checkbox, Radio Group, Select, Switch
- **导航**：Sidebar, Menubar, Navigation Menu, Breadcrumb
- **反馈**：Alert, Dialog, Toast, Tooltip, Hover Card
- **数据展示**：Table, Tabs, Pagination, Progress, Skeleton
- **覆盖层**：Sheet, Drawer, Popover, Context Menu
- **复杂组件**：Accordion, Carousel, Calendar, Chart, Command

### Step 3: 启动开发

```bash
# 开发模式
pnpm dev

# 构建 Tauri 应用
pnpm tauri build
```

### Step 4: 自定义

1. 修改 `src-tauri/tauri.conf.json` 中的 `productName` 和 `identifier`
2. 修改 `src/components/layout/app-sidebar.tsx` 中的导航菜单
3. 在 `src-tauri/src/lib.rs` 中添加 Rust Commands
4. 在 `packages/ui/` 中扩展组件库

## 核心模式

### Tauri IPC 通信

**Rust 端（lib.rs）：**
```rust
#[command]
fn get_platform() -> String {
    let os = std::env::consts::OS.to_string();
    let arch = std::env::consts::ARCH.to_string();
    format!("{}-{}", os, arch)
}

#[command]
fn custom_command(name: &str) -> String {
    format!("Hello, {}!", name)
}
```

**前端调用：**
```tsx
// 安全的 Tauri 调用（兼容 Web 模式）
async function callTauri<T>(command: string, args?: Record<string, unknown>): Promise<T | null> {
  if ("__TAURI_INTERNALS__" in window) {
    const { invoke } = await import("@tauri-apps/api/core");
    return invoke<T>(command, args);
  }
  return null;
}

// 使用
const platform = await callTauri<string>("get_platform");
```

### 平台检测

```tsx
// Status Bar 中的平台图标
const platformIcon =
  platform.includes("macos") ? "🍎" :
  platform.includes("windows") ? "🪟" :
  platform.includes("linux") ? "🐧" : "🌐";
```

### 侧边栏布局

```tsx
// App Shell 结构
<AppShell>
  <AppSidebar />           {/* 可折叠侧边栏 */}
  <SidebarInset>
    <main>{children}</main> {/* 主内容区 */}
    <StatusBar />           {/* 底部状态栏 */}
  </SidebarInset>
</AppShell>
```

特性：
- Cmd/Ctrl+B 折叠/展开
- 移动端自动切换为 Sheet
- 图标模式 / 展开模式
- 分组导航

## 模板文件说明

| 文件 | 说明 |
|------|------|
| `templates/pnpm-workspace.yaml` | pnpm workspace 配置 |
| `templates/package.json` | 根 package.json（monorepo scripts） |
| `templates/apps/desktop/src-tauri/tauri.conf.json` | Tauri 配置 |
| `templates/apps/desktop/src-tauri/src/lib.rs` | Rust 命令模板 |
| `templates/apps/desktop/src/components/layout/app-shell.tsx` | 布局 Shell |
| `templates/apps/desktop/src/components/layout/app-sidebar.tsx` | 侧边栏 |
| `templates/apps/desktop/src/components/layout/status-bar.tsx` | 状态栏 |
| `templates/packages/ui/src/lib/utils.ts` | cn() 工具函数 |
| `templates/packages/ui/src/globals.css` | Design tokens |
| `templates/packages/tsconfig/base.json` | TS 基础配置 |

## 注意事项

1. **Tauri 2.x**：使用 `@tauri-apps/api` v2 和 `@tauri-apps/cli` v2
2. **Next.js 静态导出**：Tauri 需要 `output: 'export'` 在 next.config.js 中
3. **CSP 安全**：开发时 `tauri.conf.json` 中 `"csp": null`，生产环境需配置
4. **跨平台测试**：平台检测逻辑需在 Web 模式下优雅降级
5. **图标**：使用 `pnpm tauri icon` 生成多平台图标

## 参考项目

- [innate-executable](https://github.com/variableway/innate-executable) — 本 Skill 的来源项目
- [Tauri 官方文档](https://v2.tauri.app/)
- [shadcn/ui](https://ui.shadcn.com/)
