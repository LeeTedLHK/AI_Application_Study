"""Agent 提供的验收脚手架，本课不要求学习 unittest。

从仓库根目录运行：
python learning/python/demo/test_day06_json_config.py

只修改 day06_json_config.py 的核心函数，不修改测试迎合错误结果。
三个测试分别捕获：未更新或返回 dict、错误忽略零值、丢失其他字段。
"""

import json
import unittest

from day06_json_config import update_query_limit


class QueryConfigTests(unittest.TestCase):
    def test_updates_limit_and_returns_json_text(self):
        actual = update_query_limit('{"status": "paid", "limit": 100}', 20)
        self.assertIsInstance(actual, str, "必须通过 return 返回 JSON 字符串")
        self.assertEqual(json.loads(actual), {"status": "paid", "limit": 20})

    def test_preserves_explicit_zero(self):
        actual = update_query_limit('{"limit": 50}', 0)
        self.assertIsInstance(actual, str, "必须返回 JSON 字符串")
        self.assertEqual(json.loads(actual), {"limit": 0})

    def test_keeps_other_fields_and_types(self):
        source = '{"limit": 100, "active": true, "filters": {"departments": ["sales", "tech"]}, "note": null}'
        actual = update_query_limit(source, 7)
        self.assertIsInstance(actual, str, "必须返回 JSON 字符串")
        decoded = json.loads(actual)
        self.assertEqual(decoded, {
            "limit": 7,
            "active": True,
            "filters": {"departments": ["sales", "tech"]},
            "note": None,
        })
        self.assertIs(decoded["active"], True)
        self.assertIsNone(decoded["note"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
