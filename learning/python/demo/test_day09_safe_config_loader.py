"""Day 9 验收测试：为 JSON 配置加载增加精确异常处理。

本课不要求学习 unittest、pathlib 或 tempfile；它们只是测试脚手架。

运行：
    python -X utf8 -B learning/python/week01/test_day09_safe_config_loader.py

三个行为契约：
1. 合法 JSON：ok=True，data 是解析后的字典，error=None；
2. 文件不存在：ok=False，data=None，error="file_not_found"；
3. JSON 非法：ok=False，data=None，error="invalid_json"。

不要修改测试预期来绕过失败。
"""

from pathlib import Path
import tempfile
import unittest

from day09_safe_config_loader import load_query_config_safely


class SafeConfigLoaderTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="day09-config-")
        self.addCleanup(self.directory.cleanup)
        directory = Path(self.directory.name)

        self.valid_path = directory / "valid.json"
        self.valid_path.write_text(
            '{"table_name": "events", "limit": 0, "active": false}',
            encoding="utf-8",
        )

        self.invalid_path = directory / "invalid.json"
        self.invalid_path.write_text(
            '{"table_name": "events", "limit": 0,}',
            encoding="utf-8",
        )
        self.missing_path = directory / "missing.json"

    def test_returns_data_for_valid_json(self):
        actual = load_query_config_safely(str(self.valid_path))

        self.assertEqual(actual, {
            "ok": True,
            "data": {"table_name": "events", "limit": 0, "active": False},
            "error": None,
        })

    def test_returns_file_not_found_for_missing_path(self):
        actual = load_query_config_safely(str(self.missing_path))

        self.assertEqual(actual, {
            "ok": False,
            "data": None,
            "error": "file_not_found",
        })

    def test_returns_invalid_json_for_malformed_content(self):
        actual = load_query_config_safely(str(self.invalid_path))

        self.assertEqual(actual, {
            "ok": False,
            "data": None,
            "error": "invalid_json",
        })


if __name__ == "__main__":
    unittest.main(verbosity=2)
