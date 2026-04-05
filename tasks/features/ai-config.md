# AI 配置 Skill

## 请创建一个 AI 配置 Skill

主要做的事情就是把不同的AI Agent Provider做成一个 Skill，用户可以通过这个 Skill来配置不同的AI Agent Provider，这些配置可以直接是模版文件直接复制到相应地址，做到用户只去修改API就可以，其他关于BASE_URL这种配置好了，不用修改。
比如：
- Claude Code
- Codex CLI
- aider
- 智谱 GLM
- opencode

claude code配置到GLM，只要运行skill `ai-config`  配置GLM，这个时候claude code就可以使用GLM provider了，再加上glm的API key 就可以使用了，其他codex 也是类似，一个自己比如openai 默认的，一个是GLM的，一个是openrouter的，如果添加其他可以后续再增加