在 GitHub 上，“benchmark skill”主要涉及 AI 智能体（Agents）的能力评估以及开发者个人技能展示两个方面。目前最热门的应用场景是针对 Claude Code、Codex 或 OpenClaw 等智能体框架的自动化评估。
## 1. AI 智能体技能评估 (Agent Skill Benchmarking) [1] 
许多 GitHub 项目致力于量化评估 AI 智能体执行特定任务的能力（通常称为 "Skill"）。

* [SkillsBench](https://github.com/benchflow-ai/skillsbench): 衡量智能体利用模块化指令、脚本和资源执行专业工作流的效率。
* [PinchBench](https://github.com/pinchbench/skill): 专门用于评估 LLM 模型作为 coding agent（如 OpenClaw）在真实任务（如调度会议、编写代码、研究主题）中的表现。
* [SRE-skills-bench](https://github.com/Rootly-AI-Labs/SRE-skills-bench): 被称为 SRE 领域的 "SWE-bench"，测试大模型解决真实世界站点可靠性工程（SRE）任务的能力。
* [Claude Code Skill Benchmarks](https://github.com/langchain-ai/skills-benchmarks): 测量技能文档设计如何影响 Claude Code 对推荐模式的遵循程度。
* [Skillmark](https://github.com/claudekit/skillmark): 一个智能体技能基准测试平台，提供 CLI 和公共排行榜，用于运行本地或 Git 仓库中的技能测试并发布结果。 [2, 3, 4, 5, 6, 7, 8] 

## 2. 性能基准测试技能 (Performance Benchmarking Skills)
部分项目将“基准测试”本身作为一个可插拔的技能（Skill）提供给 AI 助手，使其能自动完成性能分析。 [4] 

* [Performance Benchmark Skill](https://github.com/openclaw/skills/blob/main/skills/djc00p/performance-benchmark/SKILL.md): 允许智能体测量页面性能（Core Web Vitals）、API 延迟和构建速度，并生成 PR 前后的对比报告。
* everything-claude-code Benchmark: 为 Claude Code 设计的技能，用于检测性能回归和对比不同技术栈的优劣。 [9, 10] 

## 3. 开发者技能展示与认证
对于开发者个人，GitHub 也是衡量和展示“硬技能”的基准。 [11] 

* [GitHub Foundations Certification](https://education.github.com/experiences/foundations_certificate): 验证开发者对 GitHub 基础技能掌握情况的认证项目。
* [Skill-Extraction-benchmark](https://github.com/jensjorisdecorte/Skill-Extraction-benchmark): 用于评估从简历或职位描述中提取技能（基于 ESCO 分类法）的系统数据集。
* GitHub Copilot Competency: 针对 AI 辅助编程工具使用能力的技能基准测试。 [12, 13, 14] 

## 4. 最佳实践
如果你正在开发自己的 Agent Skill 并希望其通过基准测试，可以参考 [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices)，该指南介绍了如何编写专业级的智能体技能、维护精简的上下文窗口以及使用 LLM 进行验证。 [15] 
您是想评估某个 AI 智能体的技能，还是想在 GitHub 上建立个人的技能基准以供求职参考？

[1] [https://x.com](https://x.com/ivanburazin/status/2042256226910671074#:~:text=The%20folks%20at%20@benchflow_ai%20recently%20published%20SkillsBench%2C,performance%20vs.%20agents%20generating%20their%20own%20knowledge.)
[2] [https://github.com](https://github.com/benchflow-ai/skillsbench#:~:text=SkillsBench%20measures%20how%20effectively%20agents%20leverage%20skills%E2%80%94modular,instructions%2C%20scripts%2C%20and%20resources%E2%80%94to%20perform%20specialized%20workflows.)
[3] [https://github.com](https://github.com/pinchbench/skill#:~:text=PinchBench%20is%20a%20benchmarking%20system%20for%20evaluating%20LLM%20models%20as%20OpenClaw%20coding%20agents.)
[4] [https://github.com](https://github.com/pinchbench)
[5] [https://github.com](https://github.com/Rootly-AI-Labs/SRE-skills-bench)
[6] [https://github.com](https://github.com/langchain-ai/skills-benchmarks#:~:text=Claude%20Code%20Skill%20Benchmarks.%20Measures%20how%20skill,affects%20Claude%20Code%27s%20adherence%20to%20recommended%20patterns.)
[7] [https://github.com](https://github.com/langchain-ai/skills-benchmarks/releases)
[8] [https://github.com](https://github.com/claudekit/skillmark)
[9] [https://github.com](https://github.com/affaan-m/everything-claude-code/blob/main/skills/benchmark/SKILL.md)
[10] [https://github.com](https://github.com/openclaw/skills/blob/main/skills/djc00p/performance-benchmark/SKILL.md)
[11] [https://github.com](https://github.com/hylarucoder/benchmark-skill-ui-ux-pro-max#:~:text=%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E4%BD%BF%E7%94%A8Claude%20Code%20SDK%20%E8%B0%83%E7%94%A8GLM%204.7%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%EF%BC%8C%E7%BB%93%E5%90%88ui%2Dux%2Dpro%2Dmax%20Skill%20%E8%87%AA%E5%8A%A8%E6%89%B9%E9%87%8F%E7%94%9F%E6%88%90%E9%AB%98%E8%B4%A8%E9%87%8F%E7%BD%91%E7%AB%99%E8%90%BD%E5%9C%B0%E9%A1%B5%E7%9A%84%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95%E9%A1%B9%E7%9B%AE%E3%80%82)
[12] [https://github.com](https://github.com/jensjorisdecorte/Skill-Extraction-benchmark)
[13] [https://education.github.com](https://education.github.com/experiences/foundations_certificate)
[14] [https://www.skillsoft.com](https://www.skillsoft.com/skill-benchmark/github-copilot-competency-intermediate-level-91968b39-b5eb-4678-b16b-8d9e307ae83c#:~:text=The%20GitHub%20Copilot%20Competency%20benchmark%20measures%20your,best%20practices%20and%20testing%20and%20security%20features.)
[15] [https://github.com](https://github.com/mgechev/skills-best-practices)

