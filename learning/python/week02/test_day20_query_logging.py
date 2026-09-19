"""第 20 天 pytest 练习：为已有查询函数写自动验收。

业务目标：将 Day 19 的人工运行结果变成可重复执行的测试；
只修改本测试文件，不修改 day19_query_logging.py 来迎合测试。

输入与预期：
1. run_query("orders", 100) 返回 table_name="orders"、limit=100、row_count=0。
2. run_query("orders", 0) 必须保留显式传入的 0，不能替换成默认值。
3. run_query("orders", 600) 会记录 WARNING，消息包含 orders 和 600；
   也要检查返回的 limit 仍是 600。
4. checked_query_limit(-1) 应向调用方抛出 ValueError；用 pytest.raises 验证。
   反向检查：若把 -1 换成合法的 0，这项异常测试应失败。

约束：每个测试函数只检查自己的场景；使用断言，不靠目测 print。
不修改业务函数或预期来获得绿色结果。

运行单项测试（在仓库根目录）：
    python -m pytest -q learning/python/week02/test_day20_query_logging.py::test_query_payload

全部完成后运行：
    python -m pytest -q learning/python/week02/test_day20_query_logging.py

验收：四个测试被 pytest 收集；普通、显式 0、高 limit 警告和负数拒绝
均通过；你能解释为何 0 会让第四个测试失败。
"""

import pytest

from learning.python.week01.day14_checked_query_limit import checked_query_limit
from day19_query_logging import run_query


def test_query_payload() -> None:
    """验证普通查询返回值。"""
    result = run_query("orders", 100)
    assert result == {"table_name": "orders", "limit": 100, "row_count": 0}


def test_explicit_zero_limit() -> None:
    """验证显式 limit=0 不会丢失。"""
    result = run_query("orders", 0)
    assert result == {"table_name": "orders", "limit": 0, "row_count": 0}


def test_high_limit_warning(caplog) -> None:
    """验证高 limit 的 WARNING 及其上下文。"""
    result = run_query("orders", 600)
    assert any(
        record.levelname == "WARNING"
        and "orders" in record.getMessage()
        and "600" in record.getMessage()
        for record in caplog.records
    )

    assert result["limit"] == 600


def test_negative_limit_raises_value_error() -> None:
    """验证负数 limit 被拒绝。"""
    with pytest.raises(ValueError):
        checked_query_limit(-1)
