# 2026-09-23 学习记录

## Day 22 间隔复测

- 复测结果 2.5/3：能准确判断有限重试的请求次数、最终结果和最后异常。
- 补准：HTTPX 标量 `timeout=3` 会配置连接、读取、写入和连接池等待等阶段，不只代表读取；它仍不是整个函数的总时间预算。

## Day 23：async / await 与 Task

- Python 环境为 3.11.15；依据 Python 3.11 官方 asyncio 文档学习协程与 Task。
- 核心模型：`async def` 定义协程函数；调用后得到尚未执行的协程对象；`await` 让当前 Task 进入并等待协程；`asyncio.create_task()` 把协程包装成独立 Task 并安排到事件循环。
- 纠正“连续 await 自动并发”的误解：直接先 await 第一个查询再调用第二个查询是顺序执行；先创建两个 Task，再依次 await 才能让两个查询在 I/O 等待期间交错推进。
- 纠正“并行”术语：当前练习展示的是单线程事件循环中的协作式并发；同一时刻通常只有一个 Task 执行 Python 代码。

## 实现与验证

- TDD RED：先创建测试，首次因模块不存在无法收集；补充仅含 `NotImplementedError` 的接口脚手架后，两项测试均按预期失败。
- 学习者实现 `fetch_table` 与 `fetch_two_tables`：两个 Task 均在任何 await 之前创建，返回 orders / customers 元数据。
- 实际事件顺序为 `start:orders`、`start:customers`、`done:orders`、`done:customers`，证明不是直接连续 await 的顺序实现。
- Day 23 测试 2/2、仓库全量回归 38/38；无真实网络访问。
- Task 失败路径预测 3/3：能判断 Task 内 `ValueError` 会在 `await task` 处传播，后续语句不执行。

## 面试与巩固

- 面试评分 6/10：能说明 await 与 create_task 的执行关系；首次把调用 `async def` 的结果误答为协程函数，并未完整说明 CPU 密集代码为什么阻塞事件循环。
- 标准答案已记录到 `docs/interview_answer.md`。
- 每日巩固 3/3：协程对象、顺序/并发耗时及无 await 的 CPU 循环三题全部正确。

## 下一步

- Day 23 本地章节提交已创建：`learn(week02-day23): async tasks and cooperative concurrency`；未推送远程。
- 下一步进入 `asyncio.gather` 并发结果收集。
- 下次先用约 2 分钟复测协程函数、协程对象和 Task 的三层关系。
