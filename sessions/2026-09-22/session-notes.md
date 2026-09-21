# 2026-09-22 学习记录

## Day 22：HTTP retry

- 已完成 Day 21 的间隔复测 3/3，进入 retry。
- HTTPX 官方行为核对：`HTTPTransport(retries=n)` 的内置重试针对 `ConnectError` / `ConnectTimeout`；`ReadTimeout`、`503` 等需要应用层决定，不应凭“发生异常”统一重试。
- 已完成 Day 22 实现、面试追问、闭卷巩固和边界复测。

## 关键模型

- retry 是对可能暂时失败的请求进行有限次数重试；必须考虑请求幂等性、异常类型、状态码、退避等待和总时间预算。
- 404、认证失败和参数错误通常不应重试；连接失败、连接超时可能重试；ReadTimeout / 429 / 5xx 需结合明确策略。

## 实现与测试

- 先写四项测试并运行 RED，确认占位实现不能靠修改测试制造绿色结果。
- 学习者实现 `fetch_status_with_retry(url, timeout=3.0, max_attempts=3)`：只捕获 `httpx.ConnectError` / `httpx.ConnectTimeout`；成功响应先执行 `raise_for_status()` 再返回状态码；404 和 `ReadTimeout` 直接传播。
- 首次验收发现 `max_attempts=0` 会因循环未进入而隐式返回 `None`；学习者补上 `max_attempts < 1` 的 `ValueError` 校验，并新增测试覆盖该分支。
- Day 22 测试 5/5，仓库全量回归 36/36；测试均使用 `monkeypatch` 替换 `httpx.get`，未访问真实外部服务。

## 面试与巩固

- 面试题：为什么当前策略只重试连接异常，不重试 404 与 ReadTimeout？`max_attempts=3`、`timeout=3` 是否等于函数最多运行 9 秒？
- 面试评分 8/10：准确说明连接失败可能通过重连恢复、404 重试通常无效、timeout 不是函数总时限；补准 ReadTimeout 并非永远不能重试，而是本章策略有意排除，是否重试需结合幂等性、重复负载、退避和总时间预算。
- 闭卷巩固首次 3 题中前两题正确；第 3 题先回答为旧版 `None`，经复测当前代码后纠正为“不发请求并抛出 `ValueError("max_attempts must be at least 1")`”，最终 3/3。

## 下一步

- Day 22 章节提交已创建：`de8766d`（`learn(week02-day22): bounded HTTP retry`）；仅纳入本章代码、测试与记录，不推送远程。
- 下一步进入 async / await 基础。
