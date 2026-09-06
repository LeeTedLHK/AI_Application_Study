"""导师提供的验收脚手架，本课不要求学习 unittest、pathlib 或 tempfile。

运行：python -X utf8 learning/python/week01/test_day07_load_query_config.py
只在临时目录创建测试配置并在结束后清理，不改动仓库里的配置样例。
测试意图：捕获返回文本/None、忽略路径参数或改变字段类型、文件改写/打印副作用。
不要为了通过测试而修改验收要求或测试预期。
"""

import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from day07_load_query_config import load_query_config


class LoadQueryConfigTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="day07-json-")
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "query.json"
        self.path.write_text(
            '{"table_name": "orders", "limit": 20, "active": true}',
            encoding="utf-8",
        )

    def test_returns_parsed_config_dict(self):
        actual = load_query_config(str(self.path))
        self.assertIsInstance(actual, dict, "应返回解析后的字典，不是字符串或 None")
        self.assertEqual(actual, {"table_name": "orders", "limit": 20, "active": True})
        self.assertIs(actual["active"], True)

    def test_uses_supplied_path_and_preserves_values(self):
        alternate_path = Path(self.directory.name) / "另一份配置.json"
        alternate_path.write_text(
            '{"table_name": "customers", "limit": 0, "active": false, '
            '"label": "False", "note": "客户查询", "filters": {"status": "paid"}}',
            encoding="utf-8",
        )
        actual = load_query_config(str(alternate_path))
        self.assertIsInstance(actual, dict, "应返回解析后的字典")
        self.assertEqual(actual, {
            "table_name": "customers",
            "limit": 0,
            "active": False,
            "label": "False",
            "note": "客户查询",
            "filters": {"status": "paid"},
        })
        self.assertIs(actual["active"], False)
        self.assertIsInstance(actual["label"], str)
        self.assertIs(type(actual["limit"]), int)

    def test_reading_has_no_file_or_print_side_effects(self):
        before = self.path.read_bytes()
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            actual = load_query_config(str(self.path))
        self.assertEqual(self.path.read_bytes(), before, "读取函数不能改写源文件")
        self.assertEqual(captured.getvalue(), "", "业务函数不应打印，结果由 return 交给调用方")
        self.assertIsInstance(actual, dict, "无副作用之外，还必须返回配置字典")


if __name__ == "__main__":
    unittest.main(verbosity=2)
