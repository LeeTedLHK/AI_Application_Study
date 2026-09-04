# Harness Design Notes

## 为什么采用根总控 + 专项 AGENTS

目标是同时解决：

- 总路线不能偏航
- 专项教学需要更具体
- 不希望根 AGENTS 过大
- 不希望学习者频繁切终端
- Codex / Hermes 都需要能理解项目级上下文

因此：

```text
Root AGENTS
   ↓
Domain Router
   ↓
Specialized AGENTS
   ↓
Tracker
   ↓
Project / Interview
```

## 为什么 learning 与 projects 分离

`learning/` 回答：

> 我正在学习什么？

`projects/` 回答：

> 我能拿什么证明自己会？

这样避免 Lab 和求职项目混在一起。

## 为什么 progress 独立

进度不是 Python、RAG 或 Agent 任一领域私有。

它属于整个 12 周计划，因此放根级 `progress/`。

## 为什么 interview 独立

面试训练贯穿所有阶段，不属于某个知识领域。

## 为什么 docs 独立

这里存放：

- 使用说明
- Roadmap
- Migration
- 架构决策

这些不应该污染 Agent 的日常执行上下文。
