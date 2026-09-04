# Projects — 项目 Tech Lead 规则

## 原则

项目是求职证据，不是 Agent 代写作品。

学习者必须拥有：

- 架构解释权
- 核心代码理解
- Debug 经验
- Evaluation 数据
- Trade-off
- 面试表达

Agent 可以搭脚手架，但关键路径必须让学习者参与实现或修改。

## 项目要求

每个里程碑结束必须：

1. Demo
2. Test
3. Failure Case
4. Code Review
5. Architecture Decision
6. 2～3 个项目追问

关键技术决策记录：

```text
Problem
Options
Decision
Why
Trade-offs
Evidence
```

## 两个长期项目

### A
`enterprise-data-knowledge-assistant/`

用于承载 RAG / Retrieval / Evaluation / Backend。

### B
`intelligent-query-agent/`

简历主项目，用于承载 Metadata RAG / SQL Agent / Guardrail / MCP / Agent Engineering。
