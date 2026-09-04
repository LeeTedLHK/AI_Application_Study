# Intelligent Query Agent

> 主简历项目：智能取数 / NL2SQL Agent

## 业务链

```text
User Question
→ Intent / Requirement Parse
→ Metadata RAG
→ Metric Definition
→ SQL Plan
→ SQL Generation
→ SQL Guardrail
→ Validation / EXPLAIN
→ Read-only Execute
→ Result Analysis
→ Report / Answer
```

## 第一原则

禁止直接设计成：

```text
用户问题 → LLM → 直接执行 SQL
```

至少分离：

- 需求理解
- Metadata / Metric Retrieval
- SQL Planning
- SQL Generation
- Validation
- Execution

## SQL Plan

生成 SQL 前优先输出结构化计划，例如：

```json
{
  "tables": [],
  "joins": [],
  "dimensions": [],
  "metrics": [],
  "filters": [],
  "time_range": null
}
```

最终 schema 应通过项目实践共同设计。

## Guardrail

至少覆盖：

- SELECT only
- DDL / DML reject
- LIMIT
- timeout
- max rows
- schema allowlist
- EXPLAIN / parser
- tool permission

## Self-Correction

```text
DB / Validation Error
→ classify
→ provide error context
→ revise SQL
→ retry
```

必须限制 max retry 并记录每次修订原因。

## Evaluation

至少区分：

- metadata retrieval correctness
- metric / intent correctness
- SQL execution correctness
- SQL semantic correctness
- answer correctness
- unsafe query rejection rate
- latency
- token / model cost

SQL 能运行 != SQL 语义正确。

## 里程碑

### M1
Mock metadata + 单表只读 SQL Tool

### M2
Metadata RAG + Structured SQL Plan

### M3
多表 SQL + Validation

### M4
Agent Loop + Self-Correction

### M5
MCP Tools + Tracing

### M6
Evaluation + Docker + README

### M7
面试版 Architecture / Trade-offs
