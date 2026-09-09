"""Day 13 行为验收：运行本文件，验证资源状态、异常传播及导入静默。

运行：python -B learning/python/week01/test_day13_query_session.py
这些测试不访问数据库，也不修改学习者的实现。
"""

import io
import unittest
from contextlib import redirect_stdout


import_output = io.StringIO()
with redirect_stdout(import_output):
    from day13_query_session import QuerySession


class QuerySessionTests(unittest.TestCase):
    def test_normal_lifecycle(self):
        session = QuerySession()
        self.assertIs(session.closed, True)
        with session:
            self.assertIs(session.closed, False)
        self.assertIs(session.closed, True)

    def test_as_returns_same_instance(self):
        session = QuerySession()
        with session as active:
            self.assertIs(active, session)

    def test_exception_propagates_after_cleanup(self):
        session = QuerySession()
        error = ValueError("bad query")
        with self.assertRaises(ValueError) as caught:
            with session:
                raise error
        self.assertIs(caught.exception, error)
        self.assertIs(session.closed, True)

    def test_instance_state_is_independent(self):
        first = QuerySession()
        second = QuerySession()
        with first:
            self.assertIs(first.closed, False)
            self.assertIs(second.closed, True)
        self.assertIs(first.closed, True)
        self.assertIs(second.closed, True)

    def test_import_is_silent(self):
        self.assertEqual(import_output.getvalue(), "", "导入模块不应执行演示打印")


if __name__ == "__main__":
    unittest.main(verbosity=2)
