"""Day 13：with 的进入与退出（阅读示例，不是真实数据库连接）。

前置：class / self / return / raise / with。
新概念：__enter__ 在进入 with 时运行，返回值交给 as 后的变量；
__exit__ 在退出时运行。其三个参数依次是异常类型、异常对象、traceback，
正常退出时均为 None；返回 False 表示不压制 with 块抛出的异常。
只要 __enter__ 成功返回，正常结束、return 或块内异常退出均会调用 __exit__。

输入：无参数，无外部资源。直接运行可观察正常路径。
任务：先理解正常示例，再闭卷预测以下两个独立变体，不同时修改：
1. 把 print("query") 换成 raise ValueError("bad query")：
   哪些 print 会执行？close 和 done 是否出现？异常是否继续向外传播？
2. 恢复正常路径，仅删除 __enter__ 中的 return "session"：
   connection 会得到什么值？
约束：首次预测不运行变体；在聊天中回答后再修改并验证。
验收：区分退出清理与异常处理，并能说明 as 接收哪个方法的返回值。
运行：python -B learning/python/week01/day13_context_manager_demo.py
来源：https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers
"""


class QuerySession:
    def __enter__(self):
        print("open")
        return "session"

    def __exit__(self, exc_type, exc_value, traceback):
        print("close")
        return False


if __name__ == "__main__":
    with QuerySession() as connection:
        print(connection)
        print("query")
    print("done")
