# Backend Developer 使用 Frontend Skill 完整流程

> 目标：让后端开发者用最少的步骤、最低的认知负担，获得美观可用的前端界面。
> 前提：后端开发者不需要理解 React、Tailwind、npm 的底层原理。

---

## 一、核心理念

### 1.1 后端开发者的需求

```
后端开发者想要什么：
"告诉我做什么，我照做，最后给我一个能看的界面。"

后端开发者不想知道：
❌ Server Component 和 Client Component 的区别
❌ Tailwind 的类名系统
❌ pnpm workspace 的工作原理
❌ shadcn/ui CLI 的内部机制
```

### 1.2 本流程的设计原则

| 原则 | 说明 |
|------|------|
| **复制粘贴优先** | 所有命令都可以直接复制粘贴执行 |
| **选择少即是多** | 不给太多选项，默认就是最佳实践 |
| **可视化确认** | 每步都有预览确认，不盲写代码 |
| **出错有救** | 常见错误给出复制粘贴即可修复的方案 |
| **不解释为什么** | 只告诉"做什么"，不解释"为什么" |

---

## 二、准备工作（一次性）

### Step 1: 安装 Node.js

```bash
# 检查是否已安装
node --version

# 如果显示版本号（如 v20+），跳过此步骤
# 如果显示 "command not found"，访问 https://nodejs.org 下载安装 LTS 版本
```

### Step 2: 安装 pnpm

```bash
# 复制粘贴执行：
npm install -g pnpm

# 验证：
pnpm --version
```

### Step 3: 克隆 Template 项目

```bash
# 复制粘贴执行：
git clone https://github.com/variableway/innate-next-mono.git my-frontend
cd my-frontend
```

---

## 三、使用流程

### 场景 A：我想要一个 Landing Page（营销页面）

#### Step 1: 初始化项目

```bash
# 复制粘贴执行：
pnpm install
```

#### Step 2: 生成 Mockup（核心步骤）

**打开 Claude**，发送以下内容：

```
请生成一个 Landing Page 的 HTML mockup，要求：
- 顶部：导航栏（Logo + 3 个菜单项 + 登录按钮）
- 英雄区域：大标题 + 副标题 + 两个 CTA 按钮
- 特性区域：3 列卡片，每列有图标+标题+描述
- 价格区域：3 个价格方案卡片
- 底部：Footer（链接 + 版权信息）

使用 Tailwind CSS，请用 Artifacts 预览效果。
```

> **注意**：你只需要描述业务需求（"顶部有什么、中间有什么"），不需要知道组件名称。

#### Step 3: 确认并截图

- 在 Claude 的预览中查看效果
- 不满意就说"把标题改大一点"、"颜色换成蓝色"等
- **满意后截图保存**

#### Step 4: 让 AI 根据 Mockup 生成代码

**新建对话**，上传截图，发送：

```
请根据这张 mockup 截图，使用 innate-frontend Skill 规范实现代码。

要求：
1. 使用 shadcn/ui 组件实现
2. 使用 @innate/ui 的主题系统
3. 使用 Next.js App Router
4. 生成完整的 page.tsx 文件
5. 告诉我需要安装哪些组件
```

#### Step 5: 安装组件（复制粘贴）

AI 会告诉你类似这样的命令：

```bash
# 复制粘贴执行（在 apps/web 目录下）：
cd apps/web
npx shadcn@latest add button card navigation-menu badge
npx shadcn@latest add "https://21st.dev/r/serafim/hero"
npx shadcn@latest add "https://21st.dev/r/serafim/features"
npx shadcn@latest add "https://21st.dev/r/serafim/pricing"
```

> **如果安装失败**：见文末"常见错误修复"

#### Step 6: 复制代码到项目

AI 会生成 `apps/web/app/page.tsx` 的代码，复制粘贴到对应文件。

#### Step 7: 启动查看

```bash
# 复制粘贴执行：
cd apps/web
pnpm dev

# 打开浏览器访问 http://localhost:3000
```

---

### 场景 B：我想要一个 Dashboard（数据面板）

#### Step 1: 初始化（同场景 A）

#### Step 2: 生成 Mockup

```
请生成一个 Dashboard 的 HTML mockup，要求：
- 左侧：固定侧边栏（Logo + 5 个导航图标）
- 顶部：搜索框 + 用户头像
- 主内容区：
  - 第一行：4 个 KPI 数字卡片（用户数、收入、增长率、活跃度）
  - 第二行：左侧折线图（月度趋势），右侧饼图（用户分布）
  - 第三行：数据表格（最近 10 条记录）

使用 Tailwind CSS，请用 Artifacts 预览效果。
```

#### Step 3-4: 确认截图 + 让 AI 生成代码（同场景 A）

#### Step 5: 安装组件

```bash
cd apps/web
npx shadcn@latest add button card input sidebar avatar badge table tabs
npx shadcn@latest add chart  # 用于图表
```

#### Step 6-7: 复制代码 + 启动（同场景 A）

---

### 场景 C：我想要一个数据可视化页面

#### Step 1: 找参考

打开 https://public.tableau.com ，搜索与你业务相关的 dashboard：
- 销售数据 → 搜索 "sales dashboard"
- 用户分析 → 搜索 "user analytics"
- 系统监控 → 搜索 "system monitoring"

找到喜欢的截图保存。

#### Step 2: 让 AI 实现

上传截图，发送：

```
请参考这张 dashboard 截图，使用 recharts + shadcn/ui 实现类似效果。

我的数据是：
- 月度销售额：[12000, 19000, 15000, 22000, 28000, 35000]
- 用户来源：直接访问 40%，搜索 30%，社交媒体 20%，邮件 10%
- 产品类别：A 产品 35%，B 产品 25%，C 产品 40%

要求：
1. 使用 @innate/ui 的主题系统
2. 暗色模式适配
3. 响应式布局
```

#### Step 3-7: 安装组件 + 复制代码 + 启动（同场景 A）

---

## 四、AI Prompt 模板库

### 4.1 通用模板

```
请根据以下描述实现前端页面：

【页面类型】：Landing Page / Dashboard / 表单页 / 数据展示
【布局描述】：（用文字描述每个区域有什么）
【配色偏好】：暗色 / 亮色 / 跟随系统
【技术栈】：Next.js 16 + shadcn/ui + @innate/ui 主题

请生成：
1. 需要安装的组件列表
2. 完整的 page.tsx 代码
3. 任何需要额外配置的说明
```

### 4.2 带 Mockup 的模板（推荐）

```
请参考附件的 mockup 截图，实现前端代码。

要求：
1. 尽可能还原截图中的布局和样式
2. 使用 shadcn/ui 组件实现
3. 使用 @innate/ui/globals.css 的主题变量
4. 生成完整的 page.tsx 文件
5. 列出需要安装的组件命令

我的业务场景是：（一句话描述）
```

### 4.3 修改现有页面的模板

```
请修改当前页面，要求：
- 【修改1】：把侧边栏从左侧移到顶部
- 【修改2】：在 Dashboard 增加一个"最近活动"区域
- 【修改3】：把按钮颜色从蓝色改成绿色

请只输出修改后的完整代码，不需要解释为什么。
```

---

## 五、常见错误修复（复制粘贴即可）

### 错误 1：`npx shadcn@latest add` 卡住或失败

```bash
# 解决方案 1：使用 pnpm 替代 npx
pnpm dlx shadcn@latest add button

# 解决方案 2：清除缓存重试
rm -rf ~/.npm/_npx
npx shadcn@latest add button

# 解决方案 3：检查网络（如果使用代理）
npm config set proxy http://your-proxy:port
```

### 错误 2：`@innate/ui` 找不到

```bash
# 解决方案：确认在 apps/web 目录下执行
pwd
# 应该显示 .../my-frontend/apps/web

# 如果不是，执行：
cd apps/web

# 然后重新安装依赖
cd ../..
pnpm install
```

### 错误 3：`pnpm dev` 报错 "port 3000 already in use"

```bash
# 解决方案：使用其他端口
pnpm dev --port 3001
```

### 错误 4：样式不生效（页面是白屏或没有 CSS）

```bash
# 解决方案 1：检查 globals.css 导入
# 确认 apps/web/app/layout.tsx 中有：
# import "@innate/ui/globals.css"

# 解决方案 2：重启 dev server
Ctrl+C
pnpm dev
```

### 错误 5：暗色模式不工作

```bash
# 解决方案：确认 layout.tsx 中有 ThemeProvider
# 检查 apps/web/app/layout.tsx 是否包含：
# <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
```

### 错误 6：组件 props 报错（TypeScript 错误）

```bash
# 解决方案：通常是因为组件版本不兼容
# 尝试重新安装该组件：
npx shadcn@latest add button --overwrite
```

---

## 六、快速参考卡片

### 6.1 常用命令

| 你想做什么 | 命令 |
|-----------|------|
| 启动项目 | `cd apps/web && pnpm dev` |
| 安装组件 | `npx shadcn@latest add [组件名]` |
| 查看可用组件 | 访问 https://ui.shadcn.com/docs/components |
| 查看营销区块 | 访问 https://21st.dev |
| 查看图表示例 | 访问 https://recharts.org/en-US/examples |
| 构建生产版本 | `cd apps/web && pnpm build` |

### 6.2 常用文件位置

| 文件 | 路径 | 什么时候修改 |
|------|------|-------------|
| 页面代码 | `apps/web/app/page.tsx` | 修改页面内容 |
| 布局代码 | `apps/web/app/layout.tsx` | 修改整体布局（导航、主题） |
| 全局样式 | `apps/web/app/globals.css` | 很少需要修改 |
| 主题变量 | `packages/ui/src/globals.css` | 修改颜色、字体 |
| 组件目录 | `apps/web/components/ui/` | AI 自动安装，不需要手动修改 |

### 6.3 常用 AI 对话模板

| 场景 | 发送给 AI |
|------|----------|
| 从零创建页面 | "请生成 [页面类型] 的 mockup" → 确认后 → "请根据截图实现代码" |
| 修改现有页面 | "请修改当前页面：[具体修改要求]。输出完整代码。" |
| 添加图表 | "请参考 [截图/URL]，使用 recharts 实现 [图表类型]" |
| 调整样式 | "请把 [元素] 的 [属性] 改成 [值]。输出完整代码。" |
| 修复错误 | "我遇到了这个错误：[错误信息]。请给出修复方案。" |

---

## 七、进阶：如果你愿意多了解一点

### 7.1 什么时候需要了解 React

| 场景 | 需要了解的程度 |
|------|--------------|
| 只是复制 AI 生成的代码 | 不需要 |
| 修改简单的文字/颜色 | 不需要 |
| 调整布局结构 | 一点点（知道哪个标签对应哪个区域） |
| 添加交互逻辑（点击、表单提交） | 需要了解基础概念 |
| 连接后端 API | 需要了解 `useEffect` 和 `fetch` |

### 7.2 推荐学习路径（如果需要）

```
第 1 周：不用学，直接按本流程使用
第 2-3 周：如果需要修改交互，了解 React 基础（组件、props、state）
第 4 周：如果需要连接 API，了解 `useEffect` 和 async/await
```

---

## 八、总结

### 8.1 后端开发者的最小可行路径

```
1. 克隆项目 + pnpm install（一次性）
2. 对 AI 说"生成 mockup" → 确认效果 → 截图
3. 对 AI 说"根据截图实现代码" → 复制粘贴
4. pnpm dev → 看效果
5. 不满意 → 回到步骤 2
```

### 8.2 关键成功因素

| 因素 | 说明 |
|------|------|
| **Mockup 优先** | 永远不要跳过 mockup 直接写代码 |
| **截图驱动** | 用图片沟通比用文字精确 100 倍 |
| **复制粘贴** | 所有命令都直接复制，不要手打 |
| **小步迭代** | 一次只改一个东西，确认后再改下一个 |
| **不追根究底** | 不理解为什么没关系，只要知道怎么做 |

### 8.3 如果还是搞不定

如果按本流程操作仍然遇到困难，建议：
1. **使用 Lovable**（https://lovable.dev）— 完全无代码，文字描述直接生成可部署应用
2. **使用 v0.dev**（https://v0.dev）— Vercel 出品，生成 React 组件质量最高
3. **找一个前端同事** — 10 分钟帮你解决可能需要你折腾 2 小时的问题
