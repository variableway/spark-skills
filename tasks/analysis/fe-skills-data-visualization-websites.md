# 数据可视化图表参考网站调研

> 目标：为数据分析场景推荐 5-10 个高质量的图表展示网站，帮助用户选择图表类型并生成精确的 AI Task。

---

## 一、为什么需要图表参考网站

### 1.1 问题场景

后端开发者在构建数据面板时常常遇到：
- "我有这些数据，但不知道用什么图表展示最好"
- "我想参考行业最佳实践的 dashboard 布局"
- "AI 生成的图表太基础，想要更专业的可视化方案"

### 1.2 图表参考网站的价值

| 价值 | 说明 |
|------|------|
| **设计灵感** | 看到数据可以如何被可视化 |
| **布局参考** | 学习 Dashboard 的空间组织和信息层级 |
| **图表选型** | 了解不同数据类型适合什么图表 |
| **AI Task 精确化** | "参考 [网站] 的 [dashboard] 实现"比"做一个好看的图表"精确 100 倍 |

---

## 二、推荐的 10 个数据可视化参考网站

### 1. Tableau Public Gallery ⭐⭐⭐⭐⭐

**网址**: https://public.tableau.com/app/discover

**特点**:
- 全球最大的社区可视化作品库
- 数百万个交互式 dashboard，涵盖几乎所有行业
- 可下载原始 workbook 进行反向工程
- "Viz of the Day" 每日精选最佳作品

**适合场景**: 寻找行业-specific 的 dashboard 设计（金融、医疗、电商、物流等）

**AI Task 示例**:
```
请参考 Tableau Public 上 "SaaS Metrics Dashboard" 的风格，
使用 recharts 实现：
- 顶部：MRR、ARR、Churn Rate 3 个 KPI 卡片
- 中间：月度收入趋势折线图（面积图）
- 底部：客户分层饼图 + 功能使用热力图
```

---

### 2. Looker Studio (Google) Report Gallery ⭐⭐⭐⭐⭐

**网址**: https://lookerstudio.google.com/gallery

**特点**:
- Google 官方的模板库，与 GA4、Ads、BigQuery 深度集成
- 一键"Use template"复制到自己的数据源
- 营销和分析场景最丰富
- 免费使用

**适合场景**: 营销数据分析、网站流量分析、广告效果追踪

**AI Task 示例**:
```
参考 Looker Studio Gallery 中的 "Google Analytics 4 Traffic Report"，
使用 Next.js + recharts 实现一个网站流量分析面板：
- 会话数、用户数、跳出率 KPI
- 流量来源饼图
- 页面浏览量柱状图
```

---

### 3. Grafana Dashboard Gallery ⭐⭐⭐⭐

**网址**: https://grafana.com/grafana/dashboards/

**特点**:
- 工程/运维监控 dashboard 的标杆
- 实时数据、告警、时间序列可视化
- 大量开源社区贡献的 dashboard 模板
- 技术栈监控（K8s、数据库、API）最专业

**适合场景**: 系统监控、DevOps 面板、实时数据流

**AI Task 示例**:
```
参考 Grafana 的 "Node Exporter Full" dashboard 布局，
使用 recharts + WebSocket 实现系统监控面板：
- CPU/内存/磁盘使用率实时折线图
- 网络流量面积图
- 告警事件列表
```

---

### 4. Plotly Dash Gallery ⭐⭐⭐⭐

**网址**: https://dash.gallery/

**特点**:
- Python/R 开发者的首选可视化框架
- 强调交互性和代码级控制
- 每个示例都有完整的源代码
- 金融、科学计算、ML 场景丰富

**适合场景**: 需要复杂交互的分析师应用、数据科学项目

**AI Task 示例**:
```
参考 Plotly Dash Gallery 中的 "Drug Discovery" 示例，
使用 React + recharts 实现一个交互式数据探索面板：
- 散点图矩阵（多维度筛选）
- 直方图分布
- 相关性热力图
- 联动筛选器
```

---

### 5. Observable Plot Gallery ⭐⭐⭐⭐

**网址**: https://observablehq.com/plot/gallery

**特点**:
- Mike Bostock (D3.js 作者) 创建
- 数据可视化理论和实践结合最好
- 每个图表都有数据转换逻辑说明
- 强调"Grammar of Graphics"理念

**适合场景**: 学习可视化原理、选择正确的图表类型

**AI Task 示例**:
```
参考 Observable Plot Gallery 的 "Monthly Temperature" 示例，
使用 recharts 实现一个热力图：
- X 轴：月份
- Y 轴：城市
- 颜色：温度值（红-蓝渐变）
- 悬停显示精确温度
```

---

### 6. D3.js Gallery ⭐⭐⭐⭐

**网址**: https://observablehq.com/@d3/gallery

**特点**:
- 最底层、最灵活的可视化方案
- 包含大量创新的可视化形式
- 力导向图、桑基图、和弦图等高级图表
- 代码完全开源

**适合场景**: 需要高度自定义的可视化、创新图表形式

**AI Task 示例**:
```
参考 D3.js Gallery 的 "Radial Tidy Tree"，
使用 React + D3.js 实现一个组织架构的径向树图：
- 中心为 CEO
- 每层向外辐射
- 可折叠/展开节点
- 点击显示详细信息
```

---

### 7. Superset (Apache) Dashboard Examples ⭐⭐⭐

**网址**: https://superset.apache.org/gallery

**特点**:
- Apache 开源 BI 工具
- 企业级 dashboard 设计
- SQL 驱动的数据可视化
- 丰富的过滤器和下钻功能

**适合场景**: 企业 BI 报告、SQL 分析师

**AI Task 示例**:
```
参考 Apache Superset Gallery 的 "Sales Dashboard"，
使用 Next.js + recharts 实现销售分析面板：
- 销售额 KPI（同比/环比）
- 区域销售地图
- 产品销售排行柱状图
- 时间范围筛选器
```

---

### 8. Recharts Examples ⭐⭐⭐⭐

**网址**: https://recharts.org/en-US/examples

**特点**:
- 本项目技术栈（React + recharts）的官方示例
- 可直接复制粘贴的代码
- 涵盖所有常见图表类型
- 组合图表、自定义 tooltip 等高级用法

**适合场景**: 本项目直接参考，技术匹配度最高

**AI Task 示例**:
```
参考 Recharts 官方示例 "ComposedChart"，
实现一个组合图表：
- 柱状图：月度收入
- 折线图：目标完成率（次 Y 轴）
- 面积图：累积收入
- 自定义 tooltip 显示详细数据
```

---

### 9. Nivo (Raphaël Benitte) ⭐⭐⭐⭐

**网址**: https://nivo.rocks/

**特点**:
- 基于 D3.js 的 React 图表库
- 高度可定制、动画效果出色
- 提供 Storybook 式交互文档
- 雷达图、树图、日历图等特色图表

**适合场景**: 需要精美动画和特殊图表类型的项目

**AI Task 示例**:
```
参考 Nivo 的 "Radar Chart" 示例，
使用 recharts 或 nivo 实现能力评估雷达图：
- 6 个维度：技术、沟通、领导力、创新、执行、协作
- 多个人员对比
- 悬停显示具体分数
```

---

### 10. MUI X Charts (Material UI) ⭐⭐⭐

**网址**: https://mui.com/x/react-charts/

**特点**:
- Material Design 风格的图表
- 与 MUI 组件库风格统一
- 企业级性能和可访问性
- 丰富的图表类型

**适合场景**: 使用 MUI 作为 UI 库的项目（本项目不使用，但可作设计参考）

---

## 三、按场景推荐的网站组合

| 场景 | 主要参考 | 辅助参考 |
|------|---------|---------|
| **营销分析** | Looker Studio Gallery | Tableau Public |
| **SaaS 指标** | Tableau Public | Recharts Examples |
| **系统监控** | Grafana Gallery | Nivo |
| **数据科学** | Observable Plot | Plotly Dash |
| **财务分析** | Tableau Public | Superset Gallery |
| **组织架构** | D3.js Gallery | Nivo |
| **地理数据** | Tableau Public | Observable Plot |

---

## 四、在 Skill 中如何引用

### 4.1 建议增加的 Skill 内容

在 innate-frontend SKILL.md 中增加：

```markdown
## 数据可视化参考

构建数据面板时，参考以下网站选择图表和布局：

| 网站 | 适用场景 | 链接 |
|------|---------|------|
| Tableau Public | 全行业 dashboard 灵感 | https://public.tableau.com |
| Looker Studio Gallery | 营销/流量分析 | https://lookerstudio.google.com/gallery |
| Grafana Gallery | 系统监控/DevOps | https://grafana.com/grafana/dashboards |
| Recharts Examples | 本项目技术栈直接参考 | https://recharts.org/en-US/examples |
| Observable Plot | 可视化理论/图表选型 | https://observablehq.com/plot/gallery |

### 使用方式

1. 在参考网站找到相似的 dashboard
2. 截图或记录 URL
3. 对 AI 说："请参考 [网站] 上的 [dashboard 名称] 风格，使用 recharts 实现..."
```

### 4.2 精确化 AI Task 的模板

```markdown
请实现一个数据可视化面板，参考如下设计：

**设计参考**:
- 整体布局参考：[网站 URL] 的 [Dashboard 名称]
- 图表风格参考：[网站 URL] 的 [Chart 名称]

**数据**:
- [描述你的数据]

**要求**:
- 使用 recharts + shadcn/ui Card 组件
- 暗色模式适配
- 响应式布局
- 悬停显示详细数据
```

---

## 五、总结

| 网站 | 核心优势 | 推荐度 |
|------|---------|--------|
| **Tableau Public** | 海量社区作品，全行业覆盖 | ⭐⭐⭐⭐⭐ |
| **Looker Studio Gallery** | 营销场景最专业，一键复制 | ⭐⭐⭐⭐⭐ |
| **Grafana Gallery** | 工程监控标杆 | ⭐⭐⭐⭐ |
| **Plotly Dash Gallery** | 交互式分析应用 | ⭐⭐⭐⭐ |
| **Observable Plot** | 可视化理论最佳 | ⭐⭐⭐⭐ |
| **Recharts Examples** | 本项目技术栈直接参考 | ⭐⭐⭐⭐ |
| **D3.js Gallery** | 创新图表形式 | ⭐⭐⭐⭐ |
| **Superset Gallery** | 企业 BI 报告 | ⭐⭐⭐ |
| **Nivo** | 精美动画+特殊图表 | ⭐⭐⭐⭐ |
| **MUI X Charts** | Material Design 风格 | ⭐⭐⭐ |

**核心建议**：
1. **Tableau Public + Looker Studio Gallery** 作为首要参考来源
2. **Recharts Examples** 作为技术实现直接参考
3. 在 Skill 中明确给出"参考 [网站] 的 [作品]"的用法模板
