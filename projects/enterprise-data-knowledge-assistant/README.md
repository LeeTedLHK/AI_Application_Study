# Enterprise Data Knowledge Assistant

## 目标

构建面向数据开发场景的企业知识 RAG。

```text
Documents
→ Parse / Clean
→ Chunk
→ Embed
→ Milvus
→ Query Rewrite
→ Vector + BM25
→ Hybrid
→ Rerank
→ Context
→ LLM
→ Citation
```

## 数据建议

- 数据字典
- 指标口径
- 报表说明
- ETL 文档
- SQL 开发规范

## 必须包含

- FastAPI
- 文档解析
- 可配置 Embedding
- Milvus
- Metadata
- Hybrid Search
- Rerank
- Citation
- Evaluation Dataset
- Eval Report
- Logging
- Tests
- Docker
- Architecture README

## 里程碑

### M1
Baseline Vector RAG

### M2
Metadata + Filter

### M3
BM25 + Hybrid

### M4
Rerank

### M5
Evaluation

### M6
FastAPI + Docker + Tests

### M7
面试版 Architecture / Trade-offs
