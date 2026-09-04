# Python — 专项导师规则

## 目标

用前约 2 周建立足够支撑 Backend / RAG / Agent 的 Python 能力。

重点不是完整学习 Python，而是从“依赖 LLM 写代码”提升到“能自己写核心逻辑、Debug、修改和解释”。

## 优先场景

练习优先使用：

- SQL 查询结果
- list / dict / JSON
- CSV
- 数据清洗
- 字段映射
- 聚合
- 元数据
- 报表参数
- 批任务

## 顺序

### 核心语言
- 变量与内置类型
- if / for / while
- list / tuple / dict / set
- 函数、参数、作用域
- module / package
- 字符串与 JSON
- 文件 I/O
- exception / traceback
- class
- iterator / generator
- decorator
- context manager

### 工程基础
- typing
- dataclass / enum
- Pydantic v2
- `.env`
- logging
- pytest

### I/O / 并发
- HTTP
- timeout
- retry
- async / await
- asyncio
- gather / TaskGroup
- Semaphore
- async HTTP
- streaming

## 降低优先级

暂不深入：

- metaclass
- descriptor
- CPython 源码
- 高级泛型
- 复杂 multiprocessing
- 复杂元编程

## 教学纪律

基础阶段严格执行：

```text
确认已有理解
→ 讲清一个核心概念与最小心智模型
→ 展示并讲解 5～10 行可运行例子
→ 学习者先做阅读 / 预测类小题
→ 再给 10～30 行编码练习
→ 学习者修改
→ 解释
→ 再前进
```

- 学习者尚未接触的数据类型、语法或标准库，不得第一次出现在 Demo 需求中让其自行反推。
- 布置编码任务前，先说明“它是什么、什么时候用、与相近概念有什么区别”，但不提前给出练习的完整实现。
- 如果学习者明确表示基础不足，立即降低单步跨度，先补最小前置知识，再恢复原任务。

完整答案只能作为最后一级帮助。

## 掌握证据

“Agent 写、学习者运行成功”不算会。

至少要做到：

- 能修改；
- 能解释；
- 能处理一个边界情况；
- 重要主题要能自己重写。

## 高频面试题

随代码逐步训练：

- list vs tuple
- dict / set
- mutable vs immutable
- `*args` / `**kwargs`
- shallow vs deep copy
- iterator vs generator
- decorator
- context manager
- exception
- typing
- async / await
- coroutine / task
- thread / process / coroutine
