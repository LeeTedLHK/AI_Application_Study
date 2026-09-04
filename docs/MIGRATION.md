# 从旧学习目录迁移到新结构

> 这是一次性迁移说明，不是日常 Agent 规则。

## 新根目录

目录名可自定义，例如：

```text
AI_Application_Study/
```

新结构：

```text
根目录/
├── AGENTS.md
├── learning/
├── projects/
├── interview/
├── progress/
├── sessions/
└── docs/
```

## 旧资料处理原则

如果原来已有：

- Python labs
- session notes
- python-learning-tracker
- RAG 实验
- Agent Demo

不要删除。

建议：

1. 将旧 Python Labs 迁入 `learning/python/` 下适合的位置；
2. 将旧 RAG 实验迁入 `learning/rag/`；
3. 将有求职价值的完整项目迁入 `projects/`；
4. 读取旧 tracker；
5. 将有效掌握状态合并到 `progress/ai-learning-tracker.md`；
6. 旧 tracker 作为历史参考保留。

## 迁移后

日常只把：

`progress/ai-learning-tracker.md`

作为全局学习状态来源。
