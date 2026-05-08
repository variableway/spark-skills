# 技能基准测试策略

## 概述

本文档提供了一套综合的 AI 代理技能基准测试策略，基于对主要基准测试工具和生态系统最佳实践的分析。

---

## 1. 基准测试工具全景

### 1.1 工具对比矩阵

| 工具 | 类型 | 侧重点 | 指标 | 成熟度 |
|------|------|--------|------|--------|
| **SkillsBench** | 健身房式基准 | 技能组合（2+ 技能协同工作） | 任务完成率、代理行为 | 早期，活跃开发中 |
| **PinchBench** | 基准系统 | 真实世界 LLM 编码代理任务（调度、编码、研究） | 任务准确率、真实保真度 | 中等 |
| **Skillmark** | CLI 平台 | 单个技能测试 + 公共排行榜 | 准确率、Token、耗时、成本 | 中等，有排行榜 |
| **Claude Code Skill Benchmarks** | 处置式实验 | 技能文档设计对遵循度的影响 | 通过率、轮次、耗时、产物质量 | 成熟，LangChain 出品 |
| **SRE-skills-bench** | 领域基准 | 站点可靠性工程任务 | 真实 SRE 问题解决 | 早期 |
| **Performance Benchmark Skill** | 插件式技能 | Core Web Vitals、API 延迟、构建速度 | LCP、FID、CLS、响应时间 | 实用型 |

### 1.2 推荐工具选择

| 目标 | 推荐工具 | 原因 |
|------|---------|------|
| 快速本地技能验证 | **Skillmark** | 基于 CLI，支持本地或 Git 仓库运行，有排行榜 |
| 文档质量测试 | **Claude Code Skill Benchmarks** | 处置式方法论，直接测试文档影响 |
| 多技能组合测试 | **SkillsBench** | 专为技能交互测试设计 |
| 性能回归检测 | **Performance Benchmark Skill** | PR 前后对比报告 |

---

## 2. 基准测试方法论

### 2.1 四维评估框架

综合所有基准测试工具的分析，技能应在四个维度上进行评估：

```
┌─────────────────────────────────────────────┐
│            技能质量模型                       │
├─────────────┬─────────────┬─────────────────┤
│  正确性      │   效率       │  可发现性        │
│             │             │                 │
│ 技能是否按  │ 使用了多少   │ 代理能否找到    │
│ 预期工作？  │ Token/时间？ │ 并触发它？       │
├─────────────┴─────────────┴─────────────────┤
│              鲁棒性                          │
│ 能否处理边缘情况和错误恢复？                   │
└─────────────────────────────────────────────┘
```

#### 维度一：正确性（主要）

- **知识测试**：代理能否回忆和应用技能概念？
- **任务测试**：代理能否端到端执行技能工作流？
- **模式遵循**：代理是否遵循技能推荐的模式？

**度量方式**：预定义测试用例的通过率（0-100%）

#### 维度二：效率（次要）

- **Token 消耗**：技能执行期间使用的总 Token 数
- **耗时**：完成技能任务的挂钟时间
- **工具调用**：所需的工具调用次数
- **成本**：每次执行的估算 API 成本

**度量方式**：与基线（无技能）和替代方案对比

#### 维度三：可发现性（辅助）

- **触发准确率**：代理是否为给定提示选择正确的技能？
- **误触发率**：代理是否在不恰当的场景触发技能？
- **描述清晰度**：代理能否仅凭描述理解技能？

**度量方式**：用多样化的提示措辞测试，测量选择准确率

#### 维度四：鲁棒性（必要）

- **边缘情况处理**：技能是否适用于异常输入？
- **错误恢复**：代理能否从脚本失败中恢复？
- **跨项目可移植性**：技能是否在不同项目类型中有效？

**度量方式**：边缘情况测试套件、故障注入测试

### 2.2 测试流程

```
阶段 1：静态分析
├── SKILL.md 行数（< 500 行？）
├── 目录结构合规性
├── 前言完整性（名称、描述）
└── 渐进式披露检查

阶段 2：知识测试
├── 概念覆盖测验
├── 决策树理解
└── 反模式识别

阶段 3：任务执行
├── 正常路径执行
├── 替代路径执行
└── 错误路径执行

阶段 4：对比分析
├── vs. 无技能（基线）
├── vs. 替代技能版本
└── vs. 上一版技能（回归检测）
```

---

## 3. 实用基准测试配置

### 3.1 使用 Skillmark（推荐入门方案）

```bash
# 安装
npm install -g skillmark

# 创建技能测试结构
mkdir -p my-skill/tests

# 定义知识测试
cat > my-skill/tests/concepts.yaml << 'EOF'
---
name: core-concepts
type: knowledge
concepts:
  - root-cause-analysis
  - hypothesis-testing
  - systematic-approach
timeout: 120
---
# 测试提示
你遇到了一个失败的测试。描述你会采取的调试方法。
EOF

# 定义任务测试
cat > my-skill/tests/execution.yaml << 'EOF'
---
name: end-to-end-execution
type: task
tools:
  - Read
  - Grep
  - Bash
timeout: 300
---
# 测试提示
src/calculator.ts 中存在一个 Bug，除以零时返回 Infinity
而不是抛出错误。调试并修复这个问题。
EOF

# 运行基准测试
skillmark run ./my-skill --model opus --runs 3

# 查看结果
cat skillmark-results/report.md

# 发布到排行榜（可选）
skillmark publish skillmark-results/result.json --api-key <key>
```

### 3.2 使用 Claude Code Skill Benchmarks 方法论

对于严格的文档质量测试，采用处置式方法：

```
1. 定义处置组：
   - CONTROL：无技能（基线）
   - CURRENT：当前技能版本
   - IMPROVED：修改后的技能版本

2. 创建任务套件：
   - 5-10 个覆盖技能范围的仿真任务
   - 每个任务在 task.toml 中定义验证标准

3. 运行每个处置 × 任务组合：
   - 在隔离的 Docker 环境中执行
   - 记录通过/失败、轮次、耗时

4. 对比处置组：
   - 相对 CONTROL 的通过率提升
   - 效率指标（轮次、耗时）
   - 识别提升遵循度的文档变更
```

### 3.3 自定义本地基准测试脚本

无需外部依赖的轻量级方案：

```bash
#!/bin/bash
# benchmark-skill.sh - 快速本地技能基准测试

SKILL_PATH=$1
RESULTS_DIR="benchmark-results/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$RESULTS_DIR"

# 测试用例数组
declare -A TESTS=(
  ["trigger-detection"]="技能是否对相关提示激活？"
  ["concept-coverage"]="代理是否展示了关键概念？"
  ["happy-path"]="代理能否完成标准工作流？"
  ["edge-case"]="代理是否处理了异常输入？"
  ["error-recovery"]="代理是否从失败中恢复？"
)

for test_name in "${!TESTS[@]}"; do
  echo "运行测试: $test_name"
  echo "${TESTS[$test_name]}"
  # 手动评估或自动化检查
  echo "结果: [通过/失败/部分通过]" >> "$RESULTS_DIR/results.txt"
done

echo "基准测试完成。结果保存在 $RESULTS_DIR/"
```

---

## 4. 技能质量最佳实践

### 4.1 编写可基准测试的技能（源自 mgechev/skills-best-practices）

| 实践 | 实现方式 |
|------|---------|
| 保持 SKILL.md < 500 行 | 将详细信息移至 references/ |
| 使用渐进式披露 | 仅在需要时加载支撑文件 |
| 使用第三人称祈使语气 | "提取文本……" 而非 "我将提取……" |
| 使用一致的术语 | 同一概念始终使用相同术语 |
| 将复杂操作打包到 scripts/ | 不要让 LLM 反复生成重复代码 |
| 在 assets/ 中提供具体模板 | 代理对具体示例的模式匹配能力极强 |
| 为脚本添加错误处理 | 脚本应返回描述性错误信息 |

### 4.2 四阶段验证流程

基于 mgechev/skills-best-practices：

**阶段 1：发现验证**
- 独立测试描述文本
- 生成应该/不应该触发技能的提示
- 优化可发现性

**阶段 2：逻辑验证**
- 为真实用例逐步模拟执行
- 识别代理必须猜测或产生幻觉的环节
- 填补指令空白

**阶段 3：边缘情况测试**
- 脚本失败（旧依赖、缺失工具）
- 不支持的配置
- 缺少回退方案
- 隐含假设

**阶段 4：架构精炼**
- 强制执行渐进式披露
- 保持 SKILL.md 为高层步骤
- 将密集规则移至 references/
- 添加专门的错误处理章节

---

## 5. 评分框架

### 5.1 综合得分计算

```
得分 = (正确性 × 0.40) + (效率 × 0.25) + (可发现性 × 0.15) + (鲁棒性 × 0.20)

各维度评分范围 0-100：
- 正确性：测试套件通过率
- 效率：相对基线标准化（100 = 与基线相同，>100 = 更优）
- 可发现性：跨提示变体的触发准确率
- 鲁棒性：边缘情况通过率
```

### 5.2 得分解读

| 得分范围 | 等级 | 行动 |
|---------|------|------|
| 90-100 | 优秀 | 可用于生产环境 |
| 75-89 | 良好 | 需要小幅改进 |
| 60-74 | 合格 | 需要显著改进 |
| 40-59 | 待改进 | 建议大幅重写 |
| 0-39 | 较差 | 考虑替换 |

---

## 6. 推荐的基准测试工作流

```
对个人集合中的每个技能：

1. 编写测试用例（知识 + 任务）
2. 本地运行 Skillmark
3. 记录基线分数
4. 根据结果改进技能
5. 重新运行并对比
6. 重复直到得分 > 75

定期执行（每月）：
- 用最新模型重新基准测试所有技能
- 与排行榜对比分数
- 淘汰持续得分 < 60 的技能
```

---

## 7. 核心参考资源

| 资源 | 地址 | 用途 |
|------|------|------|
| SkillsBench | github.com/benchflow-ai/skillsbench | 多技能组合基准测试 |
| PinchBench | github.com/pinchbench/skill | 真实世界代理任务评估 |
| Skillmark | github.com/claudekit/skillmark | CLI 基准测试 + 排行榜 |
| LangChain Skill Benchmarks | github.com/langchain-ai/skills-benchmarks | 文档设计影响测试 |
| Skills Best Practices | github.com/mgechev/skills-best-practices | 技能编写指南 |
| SRE-skills-bench | github.com/Rootly-AI-Labs/SRE-skills-bench | 领域特定 SRE 基准测试 |
| Performance Benchmark | github.com/openclaw/skills/.../performance-benchmark | Web 性能基准测试技能 |
