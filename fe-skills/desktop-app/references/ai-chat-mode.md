# AI Chat 模式参考

> 从 glm-desktop-app Skill 提炼。
> 适用场景：AI 助手应用、对话式工具、智能编辑器。

## 概述

在桌面/Web 应用中集成 AI 聊天功能，支持流式输出、多会话管理和对话历史持久化。

## 支持的 AI 服务

| 服务 | API 端点 | 模型 |
|------|----------|------|
| 智谱 GLM | `https://open.bigmodel.cn/api/paas/v4/chat/completions` | GLM-4.5-air, GLM-5.1 |
| OpenAI 兼容 | 可替换为任意 OpenAI 兼容 API | 按服务而定 |

## 实现步骤

### Step 1: API 客户端

`src/lib/glm-client.ts`：

```typescript
const BASE_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
const API_KEY = process.env.ANTHROPIC_AUTH_TOKEN

// 流式调用
async function streamChat(
  messages: Array<{role: string, content: string}>,
  model: string,
  onChunk: (text: string) => void
): Promise<void> {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({ model, messages, stream: true }),
  });

  const reader = response.body!.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n').filter(line => line.startsWith('data: '));

    for (const line of lines) {
      const data = JSON.parse(line.slice(6));
      const content = data.choices?.[0]?.delta?.content;
      if (content) onChunk(content);
    }
  }
}
```

### Step 2: 聊天界面组件

`src/components/chat/` 目录：

**chat-panel.tsx** — 聊天主面板：
- 使用 Zustand store 管理消息状态
- 消息列表自动滚动到底部
- 输入框支持 Enter 发送 / Shift+Enter 换行

**chat-message.tsx** — 单条消息：
- 用户消息：右对齐，蓝色背景
- AI 消息：左对齐，灰色背景，使用 react-markdown 渲染
- 代码块：语法高亮 + 一键复制按钮

**chat-input.tsx** — 输入区域：
- Textarea 自适应高度
- 发送按钮 + 模型选择下拉框
- 发送中显示 loading 状态

依赖：`react-markdown`, `remark-gfm`, `rehype-highlight`, `zustand`

### Step 3: 流式对话 Hook

`src/hooks/use-chat-stream.ts`：

```typescript
function useChatStream(model: string) {
  const { messages, addMessage, updateMessage } = useAppStore();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const abortRef = useRef<AbortController | null>(null);

  async function sendMessage(content: string) {
    addMessage({ role: 'user', content });
    addMessage({ role: 'assistant', content: '' });
    setIsLoading(true);

    try {
      await streamChat(
        messages.concat({ role: 'user', content }),
        model,
        (chunk) => updateMessage(lastIndex, chunk)
      );
    } catch (e) {
      setError(e.message);
    } finally {
      setIsLoading(false);
    }
  }

  function cancel() {
    abortRef.current?.abort();
  }

  return { sendMessage, isLoading, error, cancel };
}
```

### Step 4: 会话持久化

在 Zustand store 中扩展：

```typescript
interface AppState {
  conversations: Array<{
    id: string;
    title: string;        // 自动从第一条消息生成（前 20 字）
    messages: Message[];
    model: string;
    createdAt: number;
    updatedAt: number;
  }>;
  currentConversationId: string | null;
  // ... 其他状态
}
```

持久化配置（复用 tauriStorage）：
- Tauri 环境：tauri-plugin-store
- Web 环境：localStorage

### Step 5: 集成到布局

```
导航路由:
  / → 首页
  /chat → AI 聊天
  /workspace → 工作区管理
  /settings → 设置
```

## API Key 配置

### Web 模式

在 `.env.local` 中：
```
ANTHROPIC_AUTH_TOKEN=your_api_key
```

### 桌面模式（GLM 示例）

配置脚本自动写入：
1. `~/.zshrc` 或 `~/.bashrc` 的环境变量
2. `~/.claude/settings.json` 中的 API 配置：
   - `ANTHROPIC_BASE_URL`: API 端点
   - `ANTHROPIC_DEFAULT_HAIKU_MODEL`: 轻量模型
   - `ANTHROPIC_DEFAULT_SONNET_MODEL`: 旗舰模型

## 错误处理

| 错误类型 | 处理方式 |
|----------|----------|
| API Key 无效 | 提示重新配置 |
| 网络超时 | 自动重试 1 次 |
| 速率限制 | 提示稍后再试 |
| 流式中断 | 保留已接收内容 + 重试按钮 |
