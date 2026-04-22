---
name: desktop-app
description: "使用 Tauri v2 + Next.js + React 19 + TypeScript + Tailwind CSS v4 构建跨平台桌面/Web 应用。包含 monorepo 项目模板、Tauri IPC 通信、PTY 终端、教程系统、AI 聊天集成、状态持久化。UI 层使用 @innate/ui 组件库（innate-frontend Skill）。"
type: skill
supported_agents:
  - claude-code
  - kimi
  - codex
  - opencode
---

# Desktop App Skill

使用 Tauri v2 + Next.js 构建跨平台桌面/Web 应用的统一 Skill。

基于 [innate-executable](https://github.com/variableway/innate-executable) 和 [Innate Playground](https://github.com/variableway/innate-next-mono) 项目提炼。包含完整的 monorepo 结构、Tauri IPC 通信模式、PTY 终端、AI 聊天集成等功能模块。

> **UI 组件库**：使用 [innate-frontend](../innate-frontend/SKILL.md) Skill 定义的 `@innate/ui` 组件库和前端规范。本 Skill 聚焦 Tauri 桌面层和 Rust 后端。

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Tauri | 2.x | 跨平台桌面框架 |
| Next.js | 16+ | React 框架（App Router, 静态导出） |
| React | 19 | UI 库 |
| TypeScript | 5+ | 类型安全 |
| Tailwind CSS | 4 | 样式系统 |
| @innate/ui | workspace | UI 组件库（Radix UI + shadcn/ui） |
| pnpm | workspace | 包管理 + monorepo |
| Lucide React | latest | 图标库 |
| Rust | 1.77+ | Tauri 后端 |
| portable-pty | 0.8 | PTY 终端后端（可选） |

## 触发条件

当用户说"创建桌面应用"、"新建 Tauri 项目"、"desktop-app"、"tauri-desktop-app"、"kimi-desktop-app"、"glm-desktop-app" 等时触发。

## 项目结构

```
project/
├── apps/
│   └── desktop/                    # Tauri + Next.js 主应用
│       ├── src-tauri/             # Rust 后端
│       │   ├── src/
│       │   │   ├── main.rs
│       │   │   └── lib.rs         # Tauri Commands + PTY
│       │   ├── tauri.conf.json
│       │   ├── capabilities/
│       │   │   └── default.json   # 权限配置
│       │   ├── Cargo.toml
│       │   └── icons/
│       ├── src/
│       │   ├── app/               # Next.js App Router 页面
│       │   │   ├── layout.tsx     # 根布局
│       │   │   ├── page.tsx       # 首页
│       │   │   ├── chat/          # AI 聊天页（可选）
│       │   │   ├── tutorials/     # 教程列表页（可选）
│       │   │   ├── admin/         # 管理后台（可选）
│       │   │   └── settings/      # 设置页
│       │   ├── components/
│       │   │   ├── layout/        # 布局组件
│       │   │   │   ├── app-shell.tsx
│       │   │   │   ├── app-sidebar.tsx
│       │   │   │   └── status-bar.tsx
│       │   │   ├── chat/          # 聊天组件（可选）
│       │   │   ├── terminal/      # 终端组件（可选）
│       │   │   └── tutorial/      # 教程组件（可选）
│       │   ├── lib/
│       │   │   ├── tauri-storage.ts   # Zustand 持久化适配器
│       │   │   ├── tutorial-scanner.ts # MDX 教程扫描（可选）
│       │   │   └── glm-client.ts      # AI API 客户端（可选）
│       │   ├── store/
│       │   │   └── useAppStore.ts      # Zustand 全局状态
│       │   └── types/
│       │       └── index.ts
│       ├── public/tutorials/      # 内置教程 MDX（可选）
│       ├── next.config.ts         # output: "export"
│       ├── package.json
│       └── tsconfig.json
├── packages/
│   ├── ui/                        # @innate/ui 组件库（innate-frontend Skill）
│   ├── utils/                     # 工具函数
│   └── tsconfig/                  # 共享 TS 配置
├── pnpm-workspace.yaml
└── package.json
```

---

## 核心模式

### 1. Tauri / Web 双端兼容

所有调用 Tauri API 的地方必须检查环境：

```typescript
const isTauri = (): boolean =>
  typeof window !== 'undefined' && '__TAURI_INTERNALS__' in window;

// 安全调用
async function callTauri<T>(command: string, args?: Record<string, unknown>): Promise<T | null> {
  if (isTauri()) {
    const { invoke } = await import("@tauri-apps/api/core");
    return invoke<T>(command, args);
  }
  return null;
}
```

### 2. Next.js 静态导出配置

Tauri 的 `frontendDist` 指向静态文件，因此 Next.js 必须静态导出：

```typescript
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",           // 静态导出（Tauri 要求）
  distDir: "out",             // 输出目录
  images: {
    unoptimized: true,        // 静态导出必须禁用图片优化
  },
  transpilePackages: ["@innate/ui", "@innate/utils"],
};

export default nextConfig;
```

### 3. 页面组件的 "use client" 使用规范

Tauri API 只在客户端 window 对象上存在。但**不要无脑给所有页面加 `"use client"`**，应遵循以下分层原则：

**页面级组件**（必须 `"use client"`）：
```tsx
"use client";

import { useState, useEffect } from "react";

export default function Page() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return <LoadingSpinner />;
  }

  return <div>...</div>;
}
```

**原因**：Next.js SSR 阶段无法访问 `window.__TAURI_INTERNALS__`，不等待 mounted 会导致 hydration mismatch。

**布局级组件**（优先 Server Component）：
```tsx
// app/layout.tsx — 不加 "use client"
export default function RootLayout({ children }) {
  return (
    <html lang="zh-CN" suppressHydrationWarning>
      <body>{children}</body>
    </html>
  );
}
```

**提取客户端逻辑到子组件**：
```tsx
// app/page.tsx — Server Component（不加 "use client"）
import { TauriClient } from "@/components/tauri-client";

export default function Page() {
  return (
    <main>
      <h1>Dashboard</h1>
      {/* 只有需要 Tauri API 的部分用客户端组件包裹 */}
      <TauriClient />
    </main>
  );
}

// components/tauri-client.tsx — Client Component
"use client";

export function TauriClient() {
  // Tauri API 调用逻辑
}
```

> **原则**：能作为 Server Component 的就保持 Server Component，只在真正需要浏览器 API 的最小组件上加 `"use client"`。

### 4. Next.js 16 桌面应用模式

桌面应用同样受益于 Next.js 16 的新特性：

**Turbopack**：
```bash
# next.config.ts
const nextConfig = {
  // Turbopack 是默认构建工具，无需额外配置
  output: "export",
  distDir: "out",
};
```

**React Compiler**（推荐启用）：
```ts
// next.config.ts
const nextConfig = {
  output: "export",
  reactCompiler: true,
};
```

**Async APIs**：
```tsx
// app/settings/page.tsx — 即使是 "use client" 页面，动态 API 仍是异步的
"use client";

import { useSearchParams } from "next/navigation";

export default function SettingsPage() {
  // Next.js 16 中 useSearchParams 仍保持同步 hook 行为
  // 但 cookies(), headers(), draftMode() 在 Server Actions 中变为 async
  return <div>...</div>;
}
```

**Cache Components**（适用于 Web 模式）：
```tsx
'use cache'

export async function StaticContent() {
  const data = await fetchSomeData()
  return <div>{data}</div>
}
```

> 注意：桌面应用通常以 `output: "export"` 静态导出，因此大部分页面已经是静态的。Cache Components 主要对混合 Web/桌面部署有用。

### 5. Tauri IPC 通信

**Rust 端（lib.rs）**：
```rust
#[tauri::command]
fn get_platform() -> String {
    let os = std::env::consts::OS.to_string();
    let arch = std::env::consts::ARCH.to_string();
    format!("{}-{}", os, arch)
}
```

**注册命令**：
```rust
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_store::Builder::default().build())
        .invoke_handler(tauri::generate_handler![
            get_platform,
            // 其他命令...
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

### 6. 侧边栏布局

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

特性：Cmd/Ctrl+B 折叠/展开、移动端自动切换为 Sheet、图标模式 / 展开模式。

---

## Rust 后端开发

### Cargo.toml 依赖

```toml
[dependencies]
serde_json = "1.0"
serde = { version = "1.0", features = ["derive"] }
log = "0.4"
tauri = { version = "2", features = [] }
tauri-plugin-log = "2"
tauri-plugin-shell = "2"
tauri-plugin-dialog = "2"
tauri-plugin-fs = "2"
tauri-plugin-store = "2"
# 可选：PTY 终端
portable-pty = "0.8"
tokio = { version = "1", features = ["io-util"] }
```

### 权限配置

`capabilities/default.json`：

```json
{
  "permissions": [
    "core:default",
    "dialog:default",
    "dialog:allow-open",
    "fs:default",
    {
      "identifier": "fs:allow-read-dir",
      "allow": [{ "path": "$HOME/**" }]
    },
    "store:default",
    "shell:allow-execute",
    "shell:allow-spawn",
    "shell:allow-kill",
    "shell:allow-stdin-write"
  ]
}
```

### 添加自定义 Rust 命令

1. 在 `src-tauri/src/lib.rs` 中编写 `#[tauri::command]` 函数
2. 在 `.invoke_handler(tauri::generate_handler![...])` 中注册
3. 若涉及新权限，更新 `capabilities/default.json`
4. 前端通过 `invoke("command_name", args)` 调用

---

## 状态持久化（Zustand + Tauri Store）

### tauriStorage 双端适配

- **Tauri 环境**：使用 `@tauri-apps/plugin-store`
- **Web 环境**：回退到 `localStorage`
- **写队列**：单例 + 队列化写入，避免并发文件冲突

```typescript
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { tauriStorage } from '../lib/tauri-storage';

export const useAppStore = create<AppState>()(
  persist(
    (set, get) => ({
      // state and actions
    }),
    {
      name: 'app-storage',
      storage: tauriStorage,
      partialize: (state) => ({
        workspaces: state.workspaces,
        progress: state.progress,
        // 只持久化需要的数据
      }),
    }
  )
);
```

---

## 可选功能模块

> 以下模块根据项目需要选择集成，不是所有桌面应用都必须包含。

### 模块 A: PTY 终端集成

> 适用场景：IDE 类应用、教程平台、开发工具

参考：[references/playground-mode.md](references/playground-mode.md)

核心能力：
- **Rust 端**：使用 `portable-pty` 创建持久化 PTY 会话
- **前端**：`xterm.js` 渲染终端，通过 Tauri event 系统收发数据
- **命令执行**：Store 中统一 `executeCommandInTerminal()` 入口

```
用户点击运行 → executeCommandInTerminal() → writeToPty() → PTY 后端
→ pty-output event → TerminalPanel (xterm.js)
```

Rust PTY 初始化：
```rust
let pty_system = native_pty_system();
let pair = pty_system.openpty(PtySize { rows: 24, cols: 80, ... })?;
let cmd = if cfg!(windows) { CommandBuilder::new("cmd") }
          else { CommandBuilder::new("sh") };
let _child = pair.slave.spawn_command(cmd)?;
// 后台线程读取输出 → app_handle.emit("pty-output", data)
```

### 模块 B: AI 聊天集成

> 适用场景：AI 助手应用、对话式工具、智能编辑器

参考：[references/ai-chat-mode.md](references/ai-chat-mode.md)

核心能力：
- **API 客户端**：封装 AI API 调用（GLM/OpenAI/其他），支持流式输出
- **聊天界面**：消息列表 + Markdown 渲染 + 代码高亮 + 打字机效果
- **多会话管理**：对话历史持久化，自动生成标题

API 流式调用模式：
```typescript
// src/lib/glm-client.ts
async function streamChat(messages, onChunk) {
  const response = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${API_KEY}` },
    body: JSON.stringify({ model, messages, stream: true }),
  });
  const reader = response.body.getReader();
  // 读取 SSE: data: {"choices":[{"delta":{"content":"..."}}]}
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    // 解析 delta.content → onChunk(text)
  }
}
```

### 模块 C: 教程/课程系统

> 适用场景：技能学习平台、交互式教程、培训工具

参考：[references/playground-mode.md](references/playground-mode.md)

核心能力：
- **教程扫描器**：扫描 `public/tutorials/` 下的 MDX 文件
- **课程管理**：`_course.json` 定义课程元数据，编号前缀控制顺序
- **可执行教程**：教程中的代码块可通过 PTY 终端运行

MDX Frontmatter 格式：
```yaml
---
title: 安装 Node.js
description: 使用 fnm 安装 Node.js
difficulty: beginner
duration: 10
category: dev-tools
tags: [nodejs, fnm]
source: local
---
```

---

## Tauri 项目验证规则

> 来源：frontend-validate Skill 的 Tauri/Monorepo 特定检查。

### Tauri 配置检查

- [ ] `src-tauri/tauri.conf.json` 中 `frontendDist` 与 Next.js `distDir` 一致
- [ ] `devUrl` 指向正确的开发服务器端口
- [ ] `beforeDevCommand` 配置了 Next.js 开发启动命令
- [ ] `capabilities/default.json` 包含所有使用的插件权限
- [ ] `productName` 和 `identifier` 已自定义（非默认值）

### Monorepo 配置检查

- [ ] `pnpm-workspace.yaml` 包含 `apps/*` 和 `packages/*`
- [ ] 子包使用 `workspace:*` 协议引用 workspace 包
- [ ] TypeScript 配置正确继承（如需要）

### 常见问题排查

| 问题 | 排查方向 |
|------|----------|
| `window.__TAURI_INTERNALS__ is not defined` | 页面是否 `"use client"`；是否在 SSR 阶段访问 |
| Tauri dev 白屏/找不到页面 | 检查 `output: "export"` 配置；检查 `devUrl` 和端口 |
| Next.js 构建失败 | 检查动态路由是否有 `generateStaticParams` |
| 样式丢失 | Tailwind v4 检查 `globals.css` 是否有 `@import "tailwindcss"` |
| Zustand 状态不持久 | 检查 `tauriStorage` 是否被正确使用；检查 `partialize` |
| 终端无输出 | 检查 `pty_write` / `pty_resize` 是否注册；检查 shell 权限 |
| pnpm workspace 包找不到 | 检查 `pnpm-workspace.yaml` 和 `workspace:*` 引用 |

---

## 使用指南

### 初始化新项目

```bash
# 1. 创建项目目录
mkdir my-desktop-app && cd my-desktop-app

# 2. 创建 monorepo 结构
mkdir -p apps/desktop packages/ui packages/utils packages/tsconfig

# 3. 配置 pnpm workspace
# pnpm-workspace.yaml: packages: ['apps/*', 'packages/*']

# 4. 初始化 desktop 应用
cd apps/desktop
pnpm init
pnpm add next react react-dom
pnpm add -D @tauri-apps/cli typescript @types/react @types/react-dom

# 5. 初始化 Tauri
pnpm tauri init

# 6. 安装依赖并启动
cd ../..
pnpm install
cd apps/desktop
pnpm tauri dev
```

### 添加 UI 组件

```bash
# 在 packages/ui 目录下添加组件
cd packages/ui
npx shadcn@latest add button card sidebar dialog tabs
```

> 详见 [innate-frontend Skill](../innate-frontend/SKILL.md) 的组件库规范。

### 构建发布

```bash
cd apps/desktop

# 构建 Next.js 静态导出
next build

# 构建 Tauri 桌面安装包
npx tauri build
# → .dmg (macOS) / .msi (Windows) / .AppImage (Linux)
```

---

## 最佳实践

### Do

- 所有页面组件顶部加 `"use client"`
- 页面渲染前检查 `mounted` 状态，避免 hydration mismatch
- Tauri API 调用前检查 `"__TAURI_INTERNALS__" in window`
- 使用 `@innate/ui` 组件和 `cn()` 保持 UI 一致
- 新增 Rust 命令后同步更新 `capabilities/default.json`
- 使用 pnpm workspace 协议引用本地包：`"workspace:*"`

### Don't

- 在页面组件中忘记 `"use client"` 导致 Tauri API 报错
- 在服务端渲染阶段直接访问 `window` 对象
- 修改 Tauri 配置后忘记同步 `frontendDist` 和 Next.js `distDir`
- 在 Zustand 中直接修改原状态对象（始终用 `set`）
- 生产环境 `tauri.conf.json` 中 `"csp": null`（需配置安全策略）

---

## 示范项目

以下开源项目展示了本 Skill 规范的实际应用。实现具体功能时，按「任务 → 项目 → 文件路径」定位参考代码。

| 你要做的 | 参考项目 | 关键文件路径 |
|---------|---------|-------------|
| **初始化桌面应用（前端层）** | [innate-next-mono](https://github.com/variableway/innate-next-mono) | `apps/web/` — Web Starter 模板，作为桌面应用前端基础 |
| **配置 Tauri + Rust 后端** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src-tauri/tauri.conf.json` |
| **配置 Rust Commands** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src-tauri/src/lib.rs` |
| **配置 Tauri 权限** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src-tauri/capabilities/default.json` |
| **实现 Zustand + Tauri Store 持久化** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src/lib/tauri-storage.ts` |
| **实现 PTY 终端** | [innate-executable](https://github.com/variableway/innate-executable) | `src-tauri/src/lib.rs`（PTY 部分） |
| **搭建桌面应用布局** | [innate-executable](https://github.com/variableway/innate-executable) | `src/components/layout/app-shell.tsx` |
| **查看 UI 组件实现** | [innate-next-mono](https://github.com/variableway/innate-next-mono) | `packages/ui/src/block/` — 业务区块 |
| **学习 Diff UI / Terminal 设计** | [1code](https://github.com/21st-dev/1code) | 源码中对应功能模块（思路参考，不直接复制） |

> 完整映射表和引用原则见 [references/demo-projects.md](references/demo-projects.md)

## 参考资源

- [innate-executable](https://github.com/variableway/innate-executable) — 基础桌面应用模板
- [innate-next-mono](https://github.com/variableway/innate-next-mono) — Playground 完整实现
- [Tauri v2 官方文档](https://v2.tauri.app/)
- [innate-frontend Skill](../innate-frontend/SKILL.md) — Web 前端组件库规范
- [示范项目索引](references/demo-projects.md) — 参考项目关键代码模式提取
- [Playground 模式参考](references/playground-mode.md) — PTY 终端 + 教程系统
- [AI Chat 模式参考](references/ai-chat-mode.md) — GLM API 聊天集成
