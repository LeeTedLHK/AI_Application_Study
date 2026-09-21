# 2026-09-21 学习记录

## Day 21 跨日继续

- Day 21 HTTP / timeout 面试题及分段响应追问已回答，首次评分 7/10；题目与标准答案已归档到 `docs/interview_answer.md`。
- 正确区分 404 和超时、知道 `timeout=3.0` 不是整个函数的严格总时限；需要补准 `ReadTimeout` 是客户端等待下一段数据超时，完整响应结束后不会因总耗时自动抛异常。
- 2026-09-20 开始的章节跨日继续；不得把 9 月 20 日未做的收尾巩固追记为已完成。

## 下一步

- 闭卷交错巩固首次 3/3：正确判断每 2 秒一段、持续 10 秒不会因总耗时触发 3 秒 ReadTimeout；两段间隔 4 秒会超时；404 抛出 HTTPStatusError，不满足 `pytest.raises(httpx.ReadTimeout)`。
- 最终回归 31/31、编译、导入静默和 `git diff --check` 通过；本章测试使用替身请求，未验证真实外部服务。
- Day 21 跨日章节掌握等级 `Modified-It`。下次先约 2 分钟间隔复测 ReadTimeout 的每段等待语义，再进入 HTTP retry。
- 章节提交为 `learn(week02-day21): HTTP status and timeout`；仅纳入本章文件与记录，不纳入 `test.py` 或 `query_service.py`，不推送远程。
- 2026-09-22 间隔复测 3/3：准确判断总响应 10 秒但每段 2 秒不会触发 3 秒 ReadTimeout；段间 4 秒会触发；404 的 HTTPStatusError 不满足 ReadTimeout 预期。
