# RAG — Retrieval / Evaluation 专项规则

## 目标

Week 5～7 是核心阶段之一。

不能停留在：

```text
上传文档 → Embedding → Vector DB → LLM
```

必须掌握：

```text
Document
→ Parse
→ Clean
→ Chunk
→ Embed
→ Index
→ Query
→ Rewrite
→ Retrieve
→ Hybrid
→ Rerank
→ Context
→ Generate
→ Citation
→ Evaluate
```

## 数据源

优先：

- 数据字典
- 表说明
- 指标口径
- SQL 开发规范
- ETL 文档
- 报表说明
- FAQ

## Week 5：Baseline

只做最小闭环：

- Loader
- Chunk
- Embedding
- Milvus
- Vector Search
- TopK
- Context
- Answer
- Citation

## Week 6：Retrieval Engineering

从失败案例引入：

- Chunk Size
- Overlap
- Metadata
- Filter
- Query Rewrite
- BM25
- Hybrid Search
- RRF / Merge 思想
- Rerank
- Parent / Child（需要时）

每增加一个组件都回答：

> 它解决了什么具体失败？

## Week 7：Evaluation

建立 Golden Dataset：

```text
question
expected_document / chunk
expected_answer
metadata
```

至少观察：

- Recall@K
- MRR
- Answer Correctness
- Faithfulness
- Latency
- Token Cost

有合适工具时可扩展 Context Precision / Recall。

## 实验记录

每次调优记录：

```text
Hypothesis
Change
Dataset
Metric
Result
Failure Cases
Decision
```

禁止“感觉更好了”作为工程结论。

## 高频追问

- 文档里有答案为什么召回不到？
- Chunk 太大 / 太小分别怎样？
- 为什么需要 overlap？
- BM25 vs Vector Search？
- 为什么 Hybrid？
- Rerank 为什么不直接替代 Retriever？
- TopK 怎么选？
- Metadata Filter 什么时候需要？
- 换 Embedding 模型为什么通常要重建向量？
- RAG vs Fine-tuning？
- 如何区分 retrieval error 和 generation error？

## 验收

进入 Agent 核心阶段前应能：

- 从零画 RAG 架构
- 分析 retrieval failure
- 修改 chunk / topK 并重新评估
- 解释 Hybrid + Rerank
- 展示一份真实 Eval 结果
