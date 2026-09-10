"""Day 14 闭卷巩固，约 10～15 分钟。

任务：不看讲义、不运行代码，先在对话中按 Q1/Q2/Q3 回答。
以下代码作为题面放在本 docstring 中，不会在导入时执行。
约束：只使用已学的标注、默认值、异常、return 和上下文管理器知识。
验收：Q1 输出及类型准确；Q2 亲手修复并解释；Q3 顺序、返回类型准确。
首次作答后再核对与运行；本文件不提供标准答案。

Q1（3 分）：写出两行输出以及各自返回结果的类型。

    def echo_limit(limit: int = 8) -> int:
        return limit

    print(echo_limit(0))
    print(echo_limit("6"))

Q2（3 分）：要求 0 保留为 0，只有省略参数才用默认值。
指出下面的错误，把修复后的完整函数写到对话中，并解释原因。

    def keep_limit(limit: int = 8) -> int:
        if not limit:
            return 8
        return limit

Q3（4 分）：写出完整输出顺序和 result 的实际类型；解释原因。

    class Session:
        def __enter__(self):
            print("open")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print("close")
            return False

    def fetch_limit() -> int:
        with Session():
            return "4"
        print("after")

    result = fetch_limit()
    print(result)
"""
