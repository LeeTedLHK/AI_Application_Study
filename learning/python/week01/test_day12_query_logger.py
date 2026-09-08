"""Day 12 decorator 验收脚手架；本课不要求学习 unittest。

从仓库根目录运行：
    python -X utf8 -B learning/python/week01/test_day12_query_logger.py

行为契约：
1. 调用被装饰的 build_query 时，先输出 query start，再输出 query finish。
2. 装饰器不能吞掉原函数返回值，调用方仍得到原来的字典。

只修改 day12_query_logger.py 的 query_logger；不要修改测试预期。
"""

import io
import unittest
from contextlib import redirect_stdout

from day12_query_logger import build_query


class QueryLoggerTests(unittest.TestCase):
    def test_logs_before_and_after_the_original_function(self):
        output = io.StringIO()

        with redirect_stdout(output):
            build_query("orders")

        self.assertEqual(
            output.getvalue().splitlines(),
            ["query start", "query finish"],
        )

    def test_preserves_the_original_return_value(self):
        with redirect_stdout(io.StringIO()):
            result = build_query("events")

        self.assertEqual(result, {"table_name": "events"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
