# FE Skills Frontend 优化调研报告

> 调研目标：当前 fe-skills 强依赖私有仓库（innate-next-mono 等），分析风险并给出优化方案。
> 核心问题：是否需要创建 template 项目？如何聚合开源组件？Skill 应如何调整？

---

## 一、现状问题分析

### 1.1 当前依赖结构

```
fe-skills/
├── innate-frontend/SKILL.md ──→ 引用 innate-next-mono（私有仓库）
└── desktop-app/SKILL.md ──────→ 引用 innate-executable（私有仓库）
```

### 1.2 风险清单

| 风险 | 严重程度 | 说明 |
|------|---------|------|
| **仓库不再维护** | 🔴 高 | innate-next-mono、innate-websites、innate-executable 均为个人/组织私有仓库，维护优先级不确定 |
| **版本锁定过时** | 🔴 高 | shadcn/ui、Tauri、Next.js 升级频繁，私有仓库若不及时跟进，skill 引用的代码模式会过时 |
| **Agent 无法读取** | 🟡 中 | 私有仓库需要权限，AI Agent 在生成项目时无法直接复制其中的代码 |
| **生态封闭** | 🟡 中 | @innate/ui 是内部组件库，与社区生态（shadcn/ui、21st.dev 等）割裂，新组件需要手写而非复用 |
| **维护成本高** | 🟡 中 | 维护 57+ 组件 + 7 个 Landing 区块 + 主题系统 + Monorepo 结构，需要持续投入 |

### 1.3 根本矛盾

当前模式：**"自建组件库"** → 成本高、易过时、生态封闭

业界趋势：**"聚合社区组件 + 自定义配置"** → 成本低、自动更新、生态开放

---

## 二、前端组件生态调研（2025）

### 2.1 shadcn/ui 生态现状

shadcn/ui 已经从"一组组件"演化为**组件分发平台**：

- **核心理念**：Open Code — 组件源码直接复制到项目中，而非通过 npm 依赖
- **CLI 升级**：`npx shadcn@latest add <component>` 支持安装官方和社区组件
- **Registry 系统**：`npx shadcn add @<registry>/<component>` 支持第三方注册表
- **官方模板**：内置 monorepo、Next.js、Vite 等 starter 模板

### 2.2 主流社区 Registry

| Registry | 定位 | 特色 | 适用场景 |
|----------|------|------|---------|
| **shadcn/ui 官方** | 基础组件 | 30+ 基础组件，Radix UI + Tailwind | 所有项目基础 |
| **21st.dev** | 社区聚合 | 700+ 组件，Hero/Features/CTA 等营销区块丰富 | Landing Page、营销站 |
| **Aceternity UI** | 动画效果 | Framer Motion 驱动的视觉冲击组件 | 创意展示、作品集 |
| **Magic UI** | 动画组件 | 150+ 动画效果，confetti、neon gradients | Landing Page、SaaS |
| **Origin UI** | 高级组件 | 200+ 区块，timeline、rich dialogs | 复杂业务应用 |
| **Motion Primitives** | 轻量动画 | 简洁动画组件，与 shadcn/ui 风格一致 | 现有项目增量添加 |
| **Tremor** | Dashboard | 数据可视化图表，被 Vercel 收购 | 后台、数据面板 |

### 2.3 模板项目（Starter Kit）生态

| 项目 | 技术栈 | 特点 |
|------|--------|------|
| **shadcn/ui monorepo template** | Next.js + pnpm workspace | 官方维护，最权威 |
| **super-saas-template** | Next.js + Turborepo + Supabase | 生产级 SaaS 起步 |
| **next-js-boilerplate** | Next.js + NextAuth + Prisma + shadcn/ui | 功能齐全 |
| **turborepo-shadcn-ui-tailwindcss** | Turborepo + shadcn/ui | 轻量 monorepo |

### 2.4 关键趋势

1. **不再自建组件库** — 维护成本高，社区已有成熟方案
2. **聚合而非创造** — 挑选社区最佳组件，组合成自己的 starter kit
3. **配置即代码** — 主题、字体、动画通过配置文件定义，不修改组件源码
4. **CLI 驱动安装** — `npx shadcn add` 成为标准 workflow

---

## 三、方案对比

### 方案 A：继续维护私有仓库（现状）

| 维度 | 评估 |
|------|------|
| 成本 | 高 — 需持续跟进 shadcn/ui、Radix UI、Tailwind 升级 |
| 质量 | 中 — 依赖个人维护质量 |
| 生态 | 差 — 与社区割裂，新组件需手写 |
| 可持续性 | 差 — 一旦维护者停止更新，skill 立即过时 |
| Agent 可用性 | 差 — 私有仓库代码 Agent 无法直接读取 |

**结论：不推荐。**

### 方案 B：完全依赖外链引用（21st.dev、shadcn/ui）

| 维度 | 评估 |
|------|------|
| 成本 | 低 — 无需维护任何代码 |
| 质量 | 高 — 直接使用社区最佳实践 |
| 生态 | 优 — 随时获取最新组件 |
| 可持续性 | 优 — 社区持续维护 |
| Agent 可用性 | 中 — 需要网络访问，离线时 skill 缺乏代码参考 |

**结论：可用，但 Skill 本身会变得"空洞" — 只有指引没有代码。Agent 离线时无法工作。**

### 方案 C：创建聚合型 Template 项目（推荐）

创建一个公开维护的 template 项目（如 `variableway/innate-ui-kit` 或 `variableway/fe-starter`），角色定位是 **"聚合器 + 配置层"** 而非 "组件库"。

| 维度 | 评估 |
|------|------|
| 成本 | 中 — 初始搭建后，主要工作是跟进社区更新 |
| 质量 | 高 — 聚合社区最佳组件 + 自定义主题/配置 |
| 生态 | 优 — 与社区同步，同时保留自定义能力 |
| 可持续性 | 优 — 社区组件持续更新，只需维护自己的配置层 |
| Agent 可用性 | 优 — 公开仓库，Agent 可直接读取代码 |

**结论：推荐。** 平衡了维护成本和生态开放。

---

## 四、推荐方案：聚合型 Template 项目

### 4.1 项目定位

**不是组件库，而是 Starter Kit + 配置层。**

```
innate-fe-starter/（建议的新仓库名）
├── apps/
│   └── web/                    # Next.js 16 Web 应用模板
│       ├── app/
│       │   ├── layout.tsx      # 根布局（字体、主题 Provider）
│       │   ├── page.tsx        # Landing Page 示例
│       │   └── dashboard/      # Dashboard 布局示例
│       ├── components/
│       │   └── ui/             # shadcn/ui 官方组件（通过 CLI 安装）
│       ├── lib/
│       │   └── utils.ts        # cn() 工具
│       ├── globals.css         # 主题变量（OKLCH / CSS 变量）
│       └── next.config.ts
├── packages/
│   └── ui/                     # 可选：内部共享包（仅放自定义配置，不放组件源码）
│       └── src/
│           └── globals.css     # 统一 Design Tokens
├── components.json             # shadcn/ui 配置
├── tailwind.config.ts          # Tailwind 配置
└── README.md                   # 组件来源清单 + 安装指南
```

### 4.2 核心原则

1. **组件来自社区** — 基础组件用 `npx shadcn@latest add`，营销区块用 `npx shadcn@latest add "https://21st.dev/r/..."`
2. **自定义仅限配置层** — 主题变量、字体、动画参数通过 `globals.css` 和 `tailwind.config.ts` 定义，不修改组件源码
3. **文档即代码** — README 中记录每个组件的来源（哪个 registry、安装命令、版本）
4. **定期同步脚本** — 用脚本检查组件更新：`npx shadcn@latest diff`

### 4.3 与 Skill 的关系

```
innate-frontend SKILL.md
    ├── 项目初始化 ──→ 引用 innate-fe-starter 作为模板
    ├── 组件使用 ──→ 引用 shadcn/ui + 21st.dev + Aceternity
    ├── 主题配置 ──→ 引用 innate-fe-starter/packages/ui/globals.css
    └── 代码模式 ──→ 引用 innate-fe-starter/apps/web/ 下的示例文件
```

### 4.4 迁移路径

| 步骤 | 动作 | 优先级 |
|------|------|--------|
| 1 | 创建新的公开仓库 `innate-fe-starter` | 🔴 高 |
| 2 | 用 `npx shadcn@latest init` 初始化 Next.js 16 项目 | 🔴 高 |
| 3 | 安装常用 shadcn/ui 组件 + 21st.dev 营销区块 | 🔴 高 |
| 4 | 配置 OKLCH 主题变量和字体 | 🟡 中 |
| 5 | 创建 Landing Page 和 Dashboard 示例页面 | 🟡 中 |
| 6 | 更新 SKILL.md，引用新仓库替代 innate-next-mono | 🟡 中 |
| 7 | 逐步减少对 innate-next-mono 的引用 | 🟢 低 |
| 8 | 归档 innate-next-mono（可选） | 🟢 低 |

---

## 五、Skill 调整建议

### 5.1 innate-frontend SKILL.md 应调整的内容

| 当前内容 | 建议调整 |
|---------|---------|
| `@innate/ui` workspace 包 | 改为直接引用 shadcn/ui 官方组件 + 21st.dev 区块 |
| 57+ 组件清单 | 改为「推荐组件来源清单」（shadcn/ui 官方 + 21st.dev + Aceternity） |
| innate-next-mono 链接 | 改为 innate-fe-starter（新建）链接 |
| 组件编写规范 | 保留，但注明"优先从社区安装，自定义时遵循此规范" |
| OKLCH 主题系统 | 保留，这是自定义配置层的核心价值 |

### 5.2 desktop-app SKILL.md 应调整的内容

| 当前内容 | 建议调整 |
|---------|---------|
| innate-executable 链接 | 改为新的 desktop starter 模板（可基于 innate-fe-starter + Tauri） |
| UI 层引用 | 直接引用 innate-fe-starter 的 UI 配置，不重复定义 |

---

## 六、聚合开源组件的具体做法

### 6.1 推荐聚合策略

```bash
# 1. 初始化项目
npx shadcn@latest init --yes --template next --base-color zinc

# 2. 安装 shadcn/ui 官方基础组件
npx shadcn@latest add button card dialog sidebar tabs table

# 3. 安装 21st.dev 营销区块
npx shadcn@latest add "https://21st.dev/r/serafim/hero"
npx shadcn@latest add "https://21st.dev/r/serafim/features"
npx shadcn@latest add "https://21st.dev/r/serafim/pricing"

# 4. 安装 Aceternity UI 动画组件（可选）
npx shadcn@latest add "https://ui.aceternity.com/components/3d-card"
```

### 6.2 记录组件来源

在 `README.md` 或 `COMPONENTS.md` 中记录：

```markdown
## 组件来源清单

| 组件 | 来源 | 安装命令 | 版本 |
|------|------|---------|------|
| Button | shadcn/ui 官方 | `npx shadcn@latest add button` | 2.1.0 |
| Hero | 21st.dev/serafim | `npx shadcn@latest add "https://21st.dev/r/serafim/hero"` | latest |
| Features Grid | 21st.dev/serafim | `npx shadcn@latest add "https://21st.dev/r/serafim/features"` | latest |
```

### 6.3 更新检查流程

```bash
# 每周/每月运行一次
npx shadcn@latest diff          # 查看官方组件更新
# 21st.dev 组件需手动检查更新（目前无 diff 工具）
```

---

## 七、总结与建议

### 7.1 核心结论

1. **维护私有组件库（@innate/ui）是反模式** — 成本高、易过时、与社区割裂
2. **应该创建聚合型 Template 项目** — 不是组件库，而是 Starter Kit + 配置层 + 最佳实践
3. **Skill 应该转向"引用社区 + 自定义配置"** — 减少对私有仓库的依赖

### 7.2 推荐行动

| 优先级 | 行动 | 负责人 |
|--------|------|--------|
| P0 | 创建新的公开仓库 `innate-fe-starter`（或类似名称） | 用户 |
| P0 | 初始化 Next.js 16 + shadcn/ui + 21st.dev 组件 | 用户 |
| P1 | 配置 OKLCH 主题和字体系统 | 用户 |
| P1 | 更新 innate-frontend/desktop-app SKILL.md | Agent（已完成部分） |
| P2 | 创建桌面应用 starter（基于 web starter + Tauri） | 用户 |
| P2 | 归档 innate-next-mono（标记为 deprecated） | 用户 |

### 7.3 Skill 长期演进方向

```
当前：Skill → 引用私有仓库 → 维护成本高
      ↓
未来：Skill → 引用公开 Template → 聚合社区组件 → 可持续
```

Skill 的核心价值应从"定义组件"转向"定义如何选择和组合组件"。
