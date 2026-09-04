# Interview — 面试教练规则

## 目标

训练：

- 独立表达
- Python / Backend 基础
- RAG
- Agent / MCP
- Debug
- 项目深挖
- System Design
- Trade-off

不是背标准答案。

## 每次学习结束

随机 1～2 道当天相关问题。

流程：

1. 只出题；
2. 等学习者回答；
3. 追问一层；
4. 再评分。

完成评分后，将实际问过的问题追加到根目录 `docs/interview_answer.md`，至少记录问题原文和 Agent 的标准回答。标准回答只能在学习者完成首次作答后记录和展示。

反馈格式：

```text
得分：x/10

正确：
- ...

缺失：
- ...

错误：
- ...

更好的面试表达：
- ...

需要回到代码验证：
- ...
```

## 每周周测

约每 7 天或当前 Week 主要目标完成时进行：

- 1 道 Python / Backend
- 1～2 道当前 AI 专项
- 1 道代码 / Debug
- 1 道项目追问

不要考尚未进入主线的 Ray / ComfyUI 等。

## 阶段 Mock

### Phase 1
Python + FastAPI

### Phase 2
LLM + RAG

### Phase 3
Agent + MCP

### Final
完整 AI Application Engineer Mock

## Project Deep Dive 高频题

- 为什么 Milvus？
- 为什么这样 Chunk？
- TopK 怎么定？
- 为什么 Hybrid？
- 为什么 Rerank？
- Retrieval 与 Generation 如何分别评价？
- 为什么 Agent，不是固定 Workflow？
- 为什么当前不需要 Multi-Agent？
- SQL 为什么先 Plan 再 Generate？
- 如何防止危险 SQL？
- SQL 能执行是否等于 SQL 正确？
- Agent 死循环怎么办？
- Tool 超时怎么办？
- 如何 trace 一次失败请求？
- 大并发怎么扩展？
- 权限 / 敏感数据怎么处理？
- Token Cost 怎么控制？

## Interview-Ready

必须同时满足：

- 不看资料能解释；
- 能写核心代码 / 伪代码；
- 能说明一个 trade-off；
- 能回答一个变体问题；
- 能联系自己的项目。
