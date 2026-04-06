# AI Agent Communication Protocols

## Overview

This document compares different communication mechanisms between AI Agents and host systems (Claude Code, Kimi CLI, etc.), and explains why capturing structured output is challenging.

## Communication Patterns

### Pattern 1: Stdio-based Text Streaming (Most Common)

**Used by**: Claude Code, Kimi CLI, Codex CLI, aider

```
┌─────────────┐      stdin       ┌─────────┐
│   Human     │ ───────────────> │  Host   │
│   User      │                  │  CLI    │
└─────────────┘                  └────┬────┘
                                      │
                                      │ stdio
                                      ▼
                               ┌─────────────┐
                               │   AI Agent  │
                               │  (Remote    │
                               │   Server)   │
                               └──────┬──────┘
                                      │
                                      │ SSE/WebSocket
                                      │ (streaming)
                                      ▼
                               ┌─────────────┐
                               │   LLM       │
                               │  (Kimi/     │
                               │  Claude/etc)│
                               └─────────────┘
```

**Data Flow**:
1. User types message → Host CLI
2. Host CLI sends to AI Agent (via HTTP API with streaming)
3. AI Agent streams tokens back
4. Host CLI renders tokens to terminal

**Challenge**: The Host CLI only sees text tokens, not structured data.

### Pattern 2: Function Calling / Tool Use

**Used by**: Claude Code (Tools API), Kimi CLI (Function Calling)

```
┌─────────────┐                    ┌─────────────┐
│   Host      │ <── Function Call ─│   AI Agent  │
│   CLI       │                    │             │
│             │ ── Tool Result ──> │             │
└──────┬──────┘                    └─────────────┘
       │
       │ Can write files, execute commands
       ▼
┌─────────────┐
│  Local FS   │
│  Tracing    │
└─────────────┘
```

**How it works**:
1. AI Agent decides to call a function (e.g., `write_file`)
2. Host CLI executes the function locally
3. Result returned to AI Agent
4. AI Agent continues

**Advantage**: Structured data can be captured via function parameters.

### Pattern 3: ACP (Agent Communication Protocol)

**Used by**: Kimi CLI (optional), some enterprise tools

```json
{
  "protocol": "acp",
  "version": "1.0",
  "message_type": "task_complete",
  "payload": {
    "task_id": "local-20260406-abc123",
    "status": "completed",
    "summary": "...",
    "files_changed": [...]
  }
}
```

**Status**: Not widely adopted, mostly proprietary.

## Standard Interfaces Comparison

| Protocol | Standardized | Structured | Stream Support | Used By |
|----------|--------------|------------|----------------|---------|
| Stdio Text | ❌ De facto | ❌ Text only | ✅ Yes | Most CLIs |
| Function Calling | ⚠️ Vendor-specific | ✅ Yes | ❌ Request/Response | Claude, Kimi |
| MCP | ⚠️ Emerging | ✅ Yes | ✅ Yes | Claude Desktop |
| ACP | ⚠️ Proprietary | ✅ Yes | ✅ Yes | Kimi Enterprise |
| LSP | ✅ Open standard | ✅ Yes | ✅ Yes | Code editors |

## Why There's No Universal Standard

### 1. Different Use Cases

- **Claude Code**: Focused on software engineering, rich tool ecosystem
- **Kimi CLI**: Focused on coding tasks, integrates with Moonshot API
- **Codex CLI**: Focused on quick edits, minimal overhead
- **OpenCode**: Focused on IDE integration

### 2. Vendor Lock-in

Each vendor has incentives to create their own ecosystem:
- Anthropic → Claude Code + Claude Desktop
- Moonshot → Kimi CLI + Kimi IDE
- OpenAI → Codex CLI + ChatGPT plugins

### 3. Technical Constraints

- **Streaming**: Hard to mix structured data with text streaming
- **Context Window**: Protocol overhead consumes tokens
- **Latency**: Additional protocol layers add latency

## How Host CLIs Currently Capture Output

### Method 1: Regex Parsing (Fragile)

```python
# Host CLI captures terminal output and parses
output = capture_terminal_output()

# Look for patterns
if "## Task Execution Summary" in output:
    summary = extract_between(output, "## Task Execution Summary", "##")
```

**Pros**: No AI Agent changes needed
**Cons**: Fragile, depends on formatting

### Method 2: Special Markers

```markdown
<!-- TASK_OUTPUT_START -->
{"status": "completed", "files": [...]}
<!-- TASK_OUTPUT_END -->
```

**Pros**: Machine-readable
**Cons**: Visual clutter, token overhead

### Method 3: Side-channel File (Our Approach)

```bash
# Set env var
export TASK_OUTPUT_FILE=".task-output.md"

# AI Agent writes to file
# Host reads file after execution
```

**Pros**: Clean, no protocol changes
**Cons**: AI Agent must be aware of the file

### Method 4: Function Calling (Recommended)

```python
# Define a tool
class RecordTaskOutput:
    def execute(self, summary, files_changed):
        append_to_tracing(summary, files_changed)
        return {"status": "recorded"}

# AI Agent calls the tool
result = record_task_output(
    summary="Implemented feature X",
    files_changed=["src/x.py"]
)
```

**Pros**: Reliable, structured, integrated
**Cons**: Requires tool support from Host CLI

## Recommendations

### For Our Local-Workflow

**Current approach** (side-channel file) is reasonable but requires:
1. System prompt to tell AI Agent about the file
2. AI Agent cooperation to write the file

**Better approach**: Function calling if the Host CLI supports it.

### For AI Agent Developers

Support multiple output methods:

```python
def record_output(content):
    # Method 1: Environment variable file
    if file := os.getenv("TASK_OUTPUT_FILE"):
        write_file(file, content)
    
    # Method 2: Function calling
    if function_calling_available():
        call_function("record_task_output", content)
    
    # Method 3: Stdout with markers
    print(f"<!-- TASK_OUTPUT_START -->\n{content}\n<!-- TASK_OUTPUT_END -->")
```

### For Protocol Standardization

The industry is moving toward:
- **MCP (Model Context Protocol)**: Anthropic-led, gaining traction
- **LSP-inspired protocols**: For IDE integrations
- **OpenAI's function calling**: De facto standard for tools

## References

- [MCP Specification](https://modelcontextprotocol.io/)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tools API](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
