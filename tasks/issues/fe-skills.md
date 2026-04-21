# Front End Skills

## Task 1: Analalysis FE Skills

1. 分析当前[text](../../fe-skills)中关于前端开发的web和desktop有哪些skill可以合并的
2. 请列出可以合并的清单

## Task 2: 合并FE Skill

1. 按照当前的建议开始合并skill
2. 先做frontend-web的skill
3. 然后做desktop-application的skill，当然desktop-application skill实际上包含了frontend-skill

请执行，同时理论上都需要代码作为references，但是由于shadcn-ui可能都会升级，所以需要考虑如何升级实际示范代码, 关于terminal skill的不需要合并，可能最后不需要这个skill

一下是参考的分析结果:

```
⏺ 分析完成

  对 fe-skills 目录下 11 个 skill/资源进行了详细分析，以下是可合并清单：

  合并组 1: Desktop App Skills（4 → 1）

  - tauri-desktop-app/SKILL.md
  - kimi-desktop-app/SKILL.md
  - glm-desktop-app/glm-desktop-app.json
  - advanced/create-tauri-desktop-app.json

  理由：技术栈完全一致（Tauri 2.x + Next.js 16 + React 19 + pnpm monorepo），kimi-desktop-app 是
  tauri-desktop-app 的具体实现，glm-desktop-app 是增加 AI 聊天功能，advanced JSON
  是初始化步骤。合并为统一 desktop-app Skill，内部用"场景选择"区分。

  合并组 2: Frontend + Validate（2 → 1）

  - innate-frontend/SKILL.md（保留为主体）
  - frontend-validate/SKILL.md（V1-V3 合并为验证子模块，V4 Tauri 部分移入 desktop-app）

  合并组 3: Terminal Setup（2 → 1）

  - beginner/terminal-setup-mac.json
  - beginner/terminal-setup-windows.json

  合并为一个 Skill，内部按 Mac/Windows 分支。

  不合并（保持独立）

  - prd-writer-skill、project-analysis-skill、kimi-user-cases/

  总计：11 → 6，减少 5 个
```
## ## 
## ## Task 3: 创建install fe-skill脚本

1. 检查当前脚本是否已经支持
2. 如果不支持请修改