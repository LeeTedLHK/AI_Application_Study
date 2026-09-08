"""Day 12：亲手完成第一个函数装饰器。

业务背景：多个查询函数都需要统一记录开始和结束，但不希望在每个函数里
重复编写相同的 print。

你的任务：只修改 query_logger。

要求：
1. 在 query_logger 内定义 wrapper(table_name)。
2. wrapper 调用原函数前打印 query start。
3. wrapper 调用 func(table_name)，保存它的返回值。
4. wrapper 调用原函数后打印 query finish。
5. wrapper 把原函数的返回值继续返回给调用方。
6. query_logger 返回 wrapper。

输入：build_query("orders")
返回：{"table_name": "orders"}
输出顺序：query start、query finish，各占一行。

验收：
    python -X utf8 -B learning/python/week01/test_day12_query_logger.py

约束：
- 不修改 build_query。
- 暂不使用 *args、**kwargs、functools.wraps 或带参数装饰器。
- 不修改测试来迎合错误结果。
"""


def query_logger(func):
    def wrapper(table_name):
        print("query start")
        result = func(table_name)
        print("query finish")
        return result
    return wrapper


@query_logger
def build_query(table_name):
    return {"table_name": table_name}
