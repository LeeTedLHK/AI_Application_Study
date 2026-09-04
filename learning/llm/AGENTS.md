# LLM Application Fundamentals — 专项规则

## 目标

Week 4 不依赖复杂 Agent Framework，先掌握 LLM 应用最基本的协议与控制流。

## 顺序

1. LLM API 请求 / 响应
2. system / user message
3. token / context window
4. temperature / top_p
5. streaming
6. Structured Output
7. Function / Tool Calling
8. Tool Result 回填
9. 最小 Tool Loop

## 必须理解

```text
Model 不会真正执行 Python 函数

Model
  ↓ 生成 tool call
Application
  ↓ 校验参数
Python Tool
  ↓ 执行
Tool Result
  ↓
Model
  ↓
Final Answer
```

## 练习优先使用数据业务 Tool

- `get_table_schema(table_name)`
- `get_metric_definition(metric_name)`
- `search_metadata(query)`
- `get_report(report_id)`
- `query_order(order_id)`

不要把天气 Tool 作为主要练习。

## Structured Output

必须覆盖：

- Pydantic schema
- 正常输出
- 缺字段
- 类型错误
- validation error
- repair / retry 的基本策略

## Tool Calling 验收

学习者应能：

- 写 Tool schema
- 解释 description
- 解析 tool call
- 校验参数
- 执行函数
- 回填 tool result
- 处理 tool error
- 限制循环次数

完成后再进入 Agent。
