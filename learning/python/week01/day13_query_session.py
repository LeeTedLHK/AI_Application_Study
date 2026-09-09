"""Day 13 编码任务：模拟查询会话的资源状态。

业务目标：查询正常结束或失败后，会话都处于关闭状态，失败原因仍可被上层捕获。
本题仅维护布尔状态，不连接真实数据库，不需要任何第三方依赖。

先在聊天中用三句话写设计：创建时、进入 with 时、退出 with 时各做什么；
随后自己实现 QuerySession 类（约 10～20 行核心代码）。

需求：
1. QuerySession() 不接收参数；新实例的 closed 属性为 True。
2. 进入 with 后 closed 为 False；as 后变量指向这个会话实例。
3. 正常退出后 closed 为 True。
4. with 块内抛出 ValueError 时，退出后 closed 也为 True，异常继续向外传播。
5. 不打印日志，不硬编码查询结果；本题不要求处理嵌套使用或进入失败。

返回值前置：self 是当前实例；return self 把这个实例返回给调用方，
不会创建新实例。as 接收 __enter__ 的返回值，因此可以访问其 closed 属性。

正常验收用法（在核心实现完成后运行）：
    session = QuerySession()
    print(session.closed)       # True
    with session as active:
        print(active.closed)   # False
    print(session.closed)      # True

失败验收用法：
    session = QuerySession()
    try:
        with session as active:
            raise ValueError("bad query")
    except ValueError:
        print(session.closed)  # True；必须进入这个 except 分支

验收标准：正常与失败两条路径均满足要求；as 得到原实例；两个实例状态独立；
能解释两个特殊方法的返回值分别起什么作用。
核心实现由学习者完成。测试与演示调用放在 __main__ 保护块内，导入不输出。
"""

# 在这里亲手实现 QuerySession。
class QuerySession:
    def __init__(self):
        self.closed = True  # 初始化时会话为关闭状态

    def __enter__(self):
        self.closed = False  # 进入 with 块时会话为打开状态
        return self  # 返回当前实例，供 as 使用

    def __exit__(self, exc_type, exc_value, traceback):
        self.closed = True  # 无论是否异常，退出 with 块时会话为关闭状态
        return False  # 不抑制异常，继续向外传播



if __name__ == "__main__":
    session = QuerySession()
    print(session.closed)       # True
    with session as active:
        print(active.closed)   # False
    print(session.closed)      # True

    # 失败验收用法：
    session = QuerySession()
    try:
        with session as active:
            raise ValueError("bad query")
    # 异常继续向外传播，进入 except 分支
    except ValueError:
        print(session.closed)  # True；必须进入这个 except 分支