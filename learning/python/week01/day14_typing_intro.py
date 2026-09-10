"""Day 14：类型标注阅读预测（先回答，再运行）。

目标：区分参数标注、返回值标注、默认值与实际运行行为。
前置：name: str 表示期望字符串；-> str 表示期望返回字符串。
标注本身不会自动校验或转换值；= 10 才是默认参数值。
参考：https://docs.python.org/3.11/library/typing.html

任务：独立预测下面三个 print 的输出，并写出各自结果类型。
再解释 limit: int、-> int、= 10 分别表达什么。
约束：首次回答前不要运行，不改代码；本题故意包含不符合标注的调用。
验收：三次输出与类型判断准确，能说明标注是否自动转换字符串。
边界：对比省略参数、显式传入 0 与传入字符串。
答案直接回复对话即可；本文件不包含标准答案。
"""


def query_limit(limit: int = 10) -> int:
    return limit


if __name__ == "__main__":
    print(query_limit())
    print(query_limit(0))
    print(query_limit("20"))
