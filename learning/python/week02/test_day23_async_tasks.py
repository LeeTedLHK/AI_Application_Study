"""Day 23 async Task 测试：验证结果契约与真正的并发启动。

本测试不访问网络，也不使用耗时阈值。目标实现需要：
1. 异步获取 orders 与 customers 两张表的元数据；
2. 返回顺序固定为 orders、customers；
3. 先创建两个 Task，再等待结果，使两个 start 都发生在任意 done 之前。
"""

import asyncio

from day23_async_tasks import fetch_two_tables


def test_fetch_two_tables_returns_both_results() -> None:
    """捕获空结果、错误表名或返回顺序颠倒。"""
    events: list[str] = []

    result = asyncio.run(fetch_two_tables(events))

    assert result == [
        {"table_name": "orders"},
        {"table_name": "customers"},
    ]


def test_fetch_two_tables_starts_both_before_any_finishes() -> None:
    """捕获直接连续 await 导致的顺序执行。"""
    events: list[str] = []

    asyncio.run(fetch_two_tables(events))

    assert set(events[:2]) == {"start:orders", "start:customers"}
    assert set(events[2:]) == {"done:orders", "done:customers"}
