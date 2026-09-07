"""Day 11 验收测试：用生成器逐个产出启用的表名。

本课不要求学习 unittest；它只是验收脚手架。

运行：
    python -X utf8 -B learning/python/week01/test_day11_active_table_generator.py

行为契约：
1. 只产出 active=True 的 table_name，并保持输入顺序；
2. next() 取走一个值后，同一生成器从原位置继续；
3. 空输入不产出任何值。

不要修改测试预期来绕过失败。
"""

import unittest

from day11_active_table_generator import iter_active_table_names


class ActiveTableGeneratorTests(unittest.TestCase):
    def test_yields_only_active_table_names_in_order(self):
        configs = [
            {"table_name": "orders", "active": True},
            {"table_name": "users", "active": False},
            {"table_name": "events", "active": True},
        ]

        actual = list(iter_active_table_names(configs))

        self.assertEqual(actual, ["orders", "events"])

    def test_same_iterator_continues_after_next(self):
        configs = [
            {"table_name": "orders", "active": True},
            {"table_name": "users", "active": False},
            {"table_name": "events", "active": True},
        ]
        table_iterator = iter_active_table_names(configs)

        first = next(table_iterator)
        remaining = list(table_iterator)

        self.assertEqual(first, "orders")
        self.assertEqual(remaining, ["events"])

    def test_empty_input_yields_nothing(self):
        actual = list(iter_active_table_names([]))

        self.assertEqual(actual, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
