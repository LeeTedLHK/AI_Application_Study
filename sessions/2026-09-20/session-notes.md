# 2026-09-20 学习记录

## 当前章节

- Day 21：HTTP GET、响应状态与 timeout；章节于 2026-09-21 跨日完成，9 月 20 日未做的巩固不追记。
- Day 20 间隔复测 2/2：准确判断日志同记录条件不能跨记录拼接，以及负数 `ValueError` 与合法 0 对 `pytest.raises` 的影响。

## 已完成的阅读预测

- 对 `httpx.get` 后调用 `raise_for_status()`：200 返回状态码，404 抛出状态异常，超时在取得响应前抛出异常。
- 删除 `raise_for_status()` 后：404 状态码会正常返回；请求超时仍会抛出异常。
- 当前环境已确认 HTTPX 0.28.1，练习以官方 QuickStart / Timeouts 文档为依据。

## 编码练习状态

- 已提供 `learning/python/week02/day21_http_status.py` 任务说明和待实现函数，核心实现留给学习者。
- 三项不访问外网的测试覆盖 200 与显式 timeout、404、ReadTimeout；首次运行 3/3 因 `NotImplementedError` 按预期失败。
- 学习者已亲手实现 `fetch_status`：将 timeout 传给 `httpx.get`，调用 `raise_for_status()`，成功时返回状态码；本章三项测试 3/3、仓库回归 31/31 通过。
- 学习者解释 404 在 `raise_for_status()` 抛出、ReadTimeout 在 `httpx.get()` 抛出，且各自后续语句不执行；原理验收通过。
- 面试追问在 2026-09-21 跨日完成，首次 7/10；需补准读取超时按等待每段数据计算。巩固在 9 月 21 日完成 3/3，章节提交按当日记录执行。
- `test.py` 和 `query_service.py` 是其他用户改动，不纳入本章。
