# Desktop App 示范项目索引

> 本文件索引与 `desktop-app` Skill 相关的参考项目。
> 实现具体功能时，按下方「任务-项目映射表」定位到对应仓库的代码文件。

---

## 任务-项目映射表

| 你要做的 | 参考项目 | 关键文件路径 |
|---------|---------|-------------|
| **初始化 Tauri + Next.js 项目** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src-tauri/tauri.conf.json` |
| **配置 Rust 后端（Commands + Plugin）** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src-tauri/src/lib.rs` |
| **配置 Tauri 权限（Capabilities）** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src-tauri/capabilities/default.json` |
| **实现 Zustand + Tauri Store 持久化** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src/lib/tauri-storage.ts` |
| **实现 PTY 终端** | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src-tauri/src/lib.rs`（PTY 部分）+ `src/components/terminal/` |
| **搭建桌面应用布局**（Sidebar + StatusBar） | [innate-executable](https://github.com/variableway/innate-executable) | `apps/desktop/src/components/layout/app-shell.tsx` |
| **查看 UI 组件实现** | [innate-next-mono](https://github.com/variableway/innate-next-mono) | `packages/ui/src/components/ui/*.tsx` |
| **学习 Diff UI 设计** | [1code](https://github.com/21st-dev/1code) | 源码中 diff preview 相关组件 |
| **学习 Terminal 面板设计** | [1code](https://github.com/21st-dev/1code) | 源码中 terminal panel 相关组件 |
| **学习多 Agent 切换架构** | [1code](https://github.com/21st-dev/1code) | 状态管理和工作区隔离相关代码 |

---

## 项目简介

### innate-executable
基础桌面应用模板。包含 Tauri v2 + Next.js + PTY 终端 + 教程系统的完整实现。这是 desktop-app Skill 的最直接参考。

### innate-next-mono
@innate/ui 组件库源项目。desktop-app 的 UI 层完全基于此。

### 1code
开源 Coding Agent Client。高级功能参考（Diff UI、Terminal 面板、Git 工作流）。采用 Apache 2.0 许可证，建议阅读源码理解思路后重新实现，不直接复制代码。

---

## 引用原则

1. **innate-executable 可直接参考** — 同一组织仓库，可直接复制配置和基础代码模式
2. **1code 仅作思路参考** — 第三方项目，阅读源码理解设计后用自己的技术栈实现
3. **版本标注** — Tauri 和 Next.js 升级频繁，引用时标注使用的版本号
4. **Skill 中保留核心模式** — Tauri 配置、tauri-storage.ts 等通用代码直接写在 SKILL.md 中，无需每次查仓库
