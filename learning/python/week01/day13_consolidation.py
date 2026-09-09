"""Day 13 每日闭卷巩固（约 10～15 分钟，逐题作答后再核对）。

目的：交错复习 context manager、return、异常传播与 decorator。
输入：下列固定片段；不访问数据库。首次回答不运行、不查讲义。
输出要求：按顺序列出打印内容，并解释关键控制流。
验收：三题分别覆盖提前 return 的清理时机、修复吞异常、函数对象绑定。
本文件仅保存题面，导入或直接运行都不会执行题目。

Q1：使用你实现的 QuerySession（__exit__ 只更新 closed，不打印）。
写出输出；print("after") 是否执行？调用方收到返回值时，会话是否已关闭？

    from day13_query_session import QuerySession

    def fetch_label(session):
        with session:
            print("inside")
            return "ok"
        print("after")

    session = QuerySession()
    result = fetch_label(session)
    print(result)
    print(session.closed)

Q2：某人把 QuerySession.__exit__ 改成如下代码（独立变体，不改原实现）：

    def __exit__(self, exc_type, exc_value, traceback):
        self.closed = True
        return True

使用这个变体执行：

    session = QuerySession()
    try:
        with session:
            raise ValueError("bad query")
    except ValueError:
        print("caught")
    print(session.closed)

先预测输出，再指出要让上层捕获错误，应修改哪一行、改成什么。
修改说明写在聊天中，不要把错误变体覆盖到原类。

Q3：交错复习 decorator。写出输出并说明 wrapped 指向哪个函数：

    def add_log(func):
        def wrapper():
            print("start")
            return func()
        return func

    def count_rows():
        print("query")
        return 2

    wrapped = add_log(count_rows)
    print(wrapped())

要让 start 出现，应修改哪一行？
"""
