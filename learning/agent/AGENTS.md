# Agent / MCP — 专项规则

## 目标

Agent 是第二核心能力。

顺序：

```text
Tool Calling
→ 手写 Agent Loop
→ Error / Retry / Max Steps
→ State
→ OpenAI Agents SDK
→ Guardrail / HITL / Tracing
→ MCP
→ 可选 LangGraph
→ 最后考虑 Multi-Agent
```

## Week 8：手写 Agent Loop

先实现：

```text
messages
  ↓
LLM + tools
  ↓
tool call?
 ├─ yes → validate → execute → append result → loop
 └─ no  → final answer
```

逐步加入：

- max steps
- timeout
- retry
- tool exception
- stop condition
- state
- tracing / logging

必须解释：

> Agent 与一次 Tool Calling 的核心差异是什么？

## Week 9：主框架

默认主学：

**OpenAI Agents SDK**

学习：

- Agent
- Runner / execution model
- Tool
- Structured Output
- Agent as Tool
- Handoff
- Session / State
- Guardrail
- HITL
- Tracing

每个 SDK 抽象都要与手写版对照：

> Framework 替我做了什么？

## LangGraph

只作为状态图思想辅助：

- State
- Node
- Edge
- Conditional Edge
- Checkpoint

除非项目明确需要复杂状态流转，否则不与 OpenAI Agents SDK 双主修。

## Week 10：MCP

理解：

- Host
- Client
- Server
- Tool
- Resource
- Prompt

重点回答：

> MCP 和 Function Calling 分别解决哪一层问题？

推荐实现 Metadata / Database MCP：

- `get_table_schema`
- `search_metadata`
- `get_metric_definition`
- `execute_readonly_sql`

## Guardrail

智能取数场景至少考虑：

- SELECT only
- DDL / DML reject
- LIMIT
- timeout
- max rows
- schema allowlist
- 敏感字段
- SQL parse / EXPLAIN
- tool permission

## Harness / Loop Engineering

不单独作为大课程优先学习。

在实现：

- retry
- verification
- max steps
- state
- permissions
- sandbox
- logging
- eval

时指出：

> 这就是 Harness / Loop Engineering 的实际组成部分。

## Multi-Agent

只有能明确回答：

> 为什么一个 Agent + 多 Tools 不够？

才能进入。

没有上下文隔离、权限隔离、并行、职责边界等真实理由时，保持单 Agent / Workflow。
