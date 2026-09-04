# Backend — FastAPI / 工程化专项规则

## 目标

Week 3 形成“能够独立写一个 AI Backend Service”的基础能力。

## 主线

```text
HTTP
→ FastAPI
→ Pydantic
→ Route / Service
→ Exception
→ Dependency
→ Async I/O
→ SSE
→ Tests
→ Logging
→ Docker
```

## 必须构建

一个真实 AI Chat API：

```text
Client
  ↓ POST /chat
FastAPI Route
  ↓
Request Validation
  ↓
Service
  ↓
LLM Client
  ↓
Response
```

逐步增加：

- `/health`
- Request / Response Schema
- Exception Handler
- 配置管理
- logging
- async endpoint
- timeout
- retry
- SSE streaming
- pytest
- Docker

## 推荐结构

```text
app/
├── main.py
├── api/
├── schemas/
├── services/
├── core/
└── tests/
```

不要过早引入 DDD / CQRS 等复杂架构。

## 必须能解释

- GET / POST
- path / query / body
- HTTP status
- 为什么 FastAPI 返回 422
- Pydantic 的职责
- sync vs async endpoint
- I/O bound
- timeout vs retry
- SSE vs 普通 response
- middleware vs dependency
- 为什么 route 不应该包含全部业务逻辑

## 验收

至少做到：

- 独立添加 endpoint
- 独立定义 Pydantic schema
- 能排查 4xx / 5xx
- 实现 service
- 写至少 3 个测试
- Docker 运行
- 解释 request → response 全链路
