"""Day 10 需求修改测试：update_limit 更新当前实例并隐式返回 None。

本课不要求学习 unittest；它只是验收脚手架。

运行：
    python -X utf8 -B learning/python/week01/test_day10_update_limit.py

行为契约：
- task_a.update_limit(25) 只更新 task_a；
- task_b 的状态保持不变；
- update_limit 没有业务返回值，调用结果为 None。
"""

import unittest

from day10_query_task import QueryTask


class QueryTaskUpdateLimitTests(unittest.TestCase):
    def test_update_limit_changes_only_current_instance(self):
        task_a = QueryTask("orders", 10)
        task_b = QueryTask("events", 5)

        result = task_a.update_limit(25)

        self.assertIsNone(result)
        self.assertEqual(task_a.to_payload(), {"table_name": "orders", "limit": 25})
        self.assertEqual(task_b.to_payload(), {"table_name": "events", "limit": 5})


if __name__ == "__main__":
    unittest.main(verbosity=2)
