# Playground 模式参考

> 从 kimi-desktop-app Skill 和 advanced/create-tauri-desktop-app.json 提炼。
> 适用场景：IDE 类应用、技能学习平台、交互式教程。

## 应用入口

`playground/apps/desktop/`

## 技术栈细节

| 技术 | 版本 | 用途 |
|------|------|------|
| Tauri | v2.10.3 | 桌面应用框架 |
| Next.js | 16.2.2 | React 框架（App Router） |
| React | 19.2.4 | UI 库 |
| Zustand | v5 | 状态管理 |
| xterm.js | v5.5.0 | 终端渲染 |
| portable-pty | 0.8 | Rust PTY 后端 |
| Radix UI | — | 组件基础（@innate/ui） |
| lucide-react | 0.511.0 | 图标库 |

## PTY 终端实现

### 前端：terminal-panel.tsx

- 使用 `@xterm/xterm` + `@xterm/addon-fit`
- Tauri 模式：通过事件 `pty-output` / `pty-exit` 与 Rust 通信
- Web 模式：模拟常见 shell 命令（`ls`, `cd`, `node -v` 等）
- 支持右侧/底部分栏、拖拽调整大小

### 后端：lib.rs PTY 实现

```rust
// 在 setup 中初始化持久 PTY
let pty_system = native_pty_system();
let pair = pty_system.openpty(PtySize { rows: 24, cols: 80, ... })
    .expect("Failed to open PTY");

let cmd = if cfg!(windows) {
    CommandBuilder::new("cmd")
} else {
    CommandBuilder::new("sh")
};

let _child = pair.slave.spawn_command(cmd)
    .expect("Failed to spawn shell");

// 管理 writer / master
app.manage(AppPtyState(Mutex::new(AppState {
    master: Some(master),
    writer: Some(writer),
})));

// 后台线程读取 PTY 输出并推送到前端
std::thread::spawn(move || {
    // read -> app_handle.emit("pty-output", data)
});
```

### 执行命令流程

Store 中的 `executeCommandInTerminal`：

1. 显示终端面板
2. 若设置了工作区，先 `cd` 到工作区路径
3. 延迟 300ms 后发送实际命令到 PTY
4. PTY 执行并将输出通过事件流推送到 xterm.js

```typescript
executeCommandInTerminal: (command: string) => {
  const state = get();
  state.showTerminal();
  const wsPath = state.currentWorkspace?.path || ...;
  if (wsPath) {
    writeToPty(`cd "${wsPath}"\r`);
    setTimeout(() => writeToPty(command + "\r"), 300);
  } else {
    writeToPty(command + "\r");
  }
}
```

## 教程/课程系统

### 教程扫描器

`playground/apps/desktop/src/lib/tutorial-scanner.ts`

核心能力：
- **`scanBuiltin()`**: 扫描 `public/tutorials/` 下的内置 MDX 教程
- **`scanWorkspace(path)`**: 通过 Tauri FS API 扫描用户本地工作区的教程
- **`loadSkillContent(slug, workspacePath, courseId)`**: 加载单篇技能内容
- **`saveSkillToWorkspace(...)`**: 保存 MDX 到工作区
- **`generateSkillMDX(meta)`**: 根据元数据生成带 frontmatter 的 MDX

### 内置课程目录结构

```
public/tutorials/
├── _course.json                   # 课程元数据
├── tutorial-001.mdx               # 独立技能
├── openclaw-quickstart/
│   ├── _course.json
│   ├── 01-install.mdx
│   ├── 02-manual-install.mdx
│   └── ...
└── terminal-basics/
    ├── _course.json
    ├── 01-ls.mdx
    └── 02-cd-pwd.mdx
```

## 页面路由结构

| 路由 | 说明 |
|------|------|
| `/` | 首页（Dashboard） |
| `/courses` | 课程列表 |
| `/courses/detail` | 课程详情 |
| `/tutorials` | 技能列表 |
| `/tutorial/[id]` | 技能详情（MDX 渲染） |
| `/tutorial/edit` | 技能编辑 |
| `/admin/workspace` | 工作区管理 |
| `/admin/courses` | 课程管理 |
| `/settings` | 设置页 |

**动态路由页面结构**：

```tsx
// tutorial/[id]/page.tsx
export { default } from "./client";

// tutorial/[id]/client.tsx
"use client";
export default function TutorialDetailClient({ id }) {
  // 实际渲染逻辑
}
```

## 开发启动

```bash
# 方式 1: 项目根目录启动脚本
./start-playground.sh

# 方式 2: 手动启动
cd playground
pnpm install
cd apps/desktop
npx tauri dev
```

**开发服务器地址**: `http://localhost:3001`
