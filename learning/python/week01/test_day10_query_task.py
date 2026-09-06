"""Day 10 验收测试：用 class 表达一个查询任务。

本课不要求学习 unittest 的写法；它只是验收脚手架。

运行：
    python -X utf8 -B learning/python/week01/test_day10_query_task.py

三个初始行为契约：
1. 实例能把自己的 table_name 和 limit 转成 Python 字典；
2. 两个实例各自保存状态，修改其中一个不会影响另一个；
3. limit=0 是有效状态，不能被替换或丢失。

不要修改测试预期来绕过失败。
"""

import unittest

from day10_query_task import QueryTask


class QueryTaskTests(unittest.TestCase):
    def test_builds_payload_from_initial_state(self):
        task = QueryTask("orders", 10)

        self.assertEqual(task.to_payload(), {"table_name": "orders", "limit": 10})

    def test_instances_keep_independent_state(self):
        task_a = QueryTask("orders", 10)
        task_b = QueryTask("events", 5)

        task_a.limit = 20

        self.assertEqual(task_a.to_payload(), {"table_name": "orders", "limit": 20})
        self.assertEqual(task_b.to_payload(), {"table_name": "events", "limit": 5})

    def test_preserves_zero_limit(self):
        task = QueryTask("events", 0)

        self.assertEqual(task.to_payload(), {"table_name": "events", "limit": 0})


if __name__ == "__main__":
    unittest.main(verbosity=2)
