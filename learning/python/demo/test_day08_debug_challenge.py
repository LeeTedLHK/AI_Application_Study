"""Day 8 Debug 验收脚手架；本课不要求学习 unittest。

运行：python -X utf8 learning/python/demo/test_day08_debug_challenge.py
验收：路径修复后能读取指定配置；JSON 修复后保留 0 和 false 的类型；
      main 精确输出 start、字典、finish，并返回 dict。
不要修改测试预期来绕过失败。
"""

import contextlib
import io
import unittest

import day08_debug_challenge


class DebugChallengeTests(unittest.TestCase):
    def test_main_loads_config_and_finishes(self):
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            actual = day08_debug_challenge.main()

        self.assertEqual(actual, {
            "table_name": "events",
            "limit": 0,
            "active": False,
        })
        self.assertIs(type(actual["limit"]), int)
        self.assertIs(actual["active"], False)
        self.assertEqual(
            captured.getvalue(),
            "start\n{'table_name': 'events', 'limit': 0, 'active': False}\nfinish\n",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
