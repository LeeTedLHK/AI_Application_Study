"""Day 13 开场复测：decorator（约 2 分钟）。

目标：闭卷区分函数对象、调用时机和返回值，再进入 context manager。
输入：下方固定的 query_count()，不需要外部文件或依赖。
任务（先不运行，在聊天中回答）：
1. 按顺序写出整个程序的输出。
2. wrapped 保存的是哪个函数对象？执行 wrapped = query_logger(query_count)
   时，query_count 的函数体是否已经执行？
3. 如果仅删除 wrapper 中的 return result，最后一行 print 会输出什么？
约束：首次回答不查讲义、不运行；先预测，再实际运行核对。
验收：输出顺序正确；能区分返回函数对象与返回业务结果；能解释题 3。
首次作答前不提供标准输出。此练习不连接数据库。

反馈后口述复核：wrapped() 执行哪个函数的函数体？其中 func() 又调用哪个函数？
验收：能分别说清两层调用，不需要修改代码。
"""


def query_logger(func):
    print("decorate")

    def wrapper():
        print("start")
        result = func()
        print("finish")
        return result

    return wrapper


def query_count():
    print("query")
    return 3


if __name__ == "__main__":
    wrapped = query_logger(query_count)
    print("ready")
    print(wrapped())
