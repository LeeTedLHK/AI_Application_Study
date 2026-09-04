# 使用说明

## 1. 推荐启动方式

始终从仓库根目录启动 Codex 或 Hermes。

例如：

```powershell
cd E:\AI_Application_Study
codex
```

或者在同一根目录启动 Hermes。

不需要：

```text
学 Python → 退出 Agent → cd learning/python → 重开
学 RAG → 退出 Agent → cd learning/rag → 重开
```

根 `AGENTS.md` 已要求 Agent 根据任务主动读取对应专项规则。

## 2. 日常使用示例

### 学习

```text
今天继续 Week 1，帮我按当前 tracker 安排 1 小时学习。
```

### Debug

```text
我这个 FastAPI 返回 422，按 Debug Mode 带我排查，不要直接告诉我答案。
```

### RAG

```text
继续 RAG Week 6，今天我想理解 Hybrid Search，并把它加到 Project A。
```

### 项目

```text
继续 Intelligent Query Agent 的下一个里程碑，先读取 tracker 和项目 README。
```

### 面试

```text
开始本周周测。
```

## 3. 最重要的三个入口

- `AGENTS.md`：总控
- `progress/ai-learning-tracker.md`：当前真实进度
- `projects/`：求职成果

## 4. 不建议的使用方式

不要每次开新会话都从零描述：

- 自己是谁
- 当前学到哪
- 目标是什么

Agent 应优先读取根规则和 tracker。

## 5. 一小时学习默认节奏

```text
5 min    回顾 / 诊断
10-15    核心概念
30-35    动手实现 / Debug
5-10     总结 + 面试追问
```

## 6. 周末

3～4 小时优先用于：

- 完整 Lab
- 项目里程碑
- Eval
- Code Review
- Mock Interview

不建议把整个周末都用于连续看课程。
