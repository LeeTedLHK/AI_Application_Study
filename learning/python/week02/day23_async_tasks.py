"""Day 23 编码练习：用 Task 并发启动两个元数据查询。

请亲手实现下面两个协程：

``fetch_table(table_name, events)``
1. 向 events 追加 ``start:<table_name>``；
2. 使用 ``await asyncio.sleep(0)`` 模拟可让出控制权的异步 I/O；
3. 向 events 追加 ``done:<table_name>``；
4. 返回 ``{"table_name": table_name}``。

``fetch_two_tables(events)``
1. 分别为 orders 和 customers 创建 Task；
2. 必须先创建两个 Task，再开始 await；
3. 等待两个结果，按 orders、customers 的顺序返回列表。

约束：
- 本章只使用 ``async def``、``await``、``asyncio.create_task``；
- 不使用 ``gather``、``TaskGroup``、``time.sleep``、真实网络或 print；
- 不修改测试预期来制造通过。

运行：
    python -m pytest -q learning/python/week02/test_day23_async_tasks.py

验收：
- 返回两张表的元数据且顺序正确；
- 两个 start 都出现在任意 done 之前，证明不是直接连续 await。
"""

import asyncio


async def fetch_table(
    table_name: str,
    events: list[str],
) -> dict[str, str]:
    """模拟一次异步元数据查询。"""
    events.append(f"start:{table_name}")
    await asyncio.sleep(0)
    events.append(f"done:{table_name}")
    return {"table_name": table_name}


async def fetch_two_tables(events: list[str]) -> list[dict[str, str]]:
    """并发获取 orders 与 customers 的元数据。"""
    orders_task = asyncio.create_task(fetch_table("orders", events))
    customers_task = asyncio.create_task(fetch_table("customers", events))
    orders = await orders_task
    customers = await customers_task
    return [orders, customers]