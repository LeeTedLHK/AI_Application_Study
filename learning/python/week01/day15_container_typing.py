"""Day 15：list / dict 容器类型标注。

第一阶段（先在对话中回答，不运行）：
1. 预测 summarize_limits([3, 5, 0]) 的返回值及其类型。
2. 预测 summarize_limits([]) 的返回值，并说明 sum([]) 的结果。
3. 下面调用传入字符串，类型标注会自动把它转换为整数吗？
       summarize_limits(["3", "5"])

第二阶段（回答后再实现）：
补齐 summarize_limits 的函数体，要求：
- 参数标注为 list[int]，返回值标注为 dict[str, int]；
- 返回字典恰有 count 和 total 两个键；
- count 是列表长度，total 是所有整数之和；
- 空列表合法，返回 {"count": 0, "total": 0}；
- 本练习不要求新增运行时类型校验，不要把字符串转换为整数。

验收：三次预测准确；亲手实现后用 [3, 5, 0]、[] 验证；能解释容器标注与运行时校验的分工。
模块导入必须无输出。核心实现由学习者完成，文件不提供标准答案。
"""


def summarize_limits(limits: list[int]) -> dict[str, int]:
    return {"count": len(limits), "total": sum(limits)}


if __name__ == "__main__":
    print(summarize_limits([3, 5, 0]))
    print(summarize_limits([]))
    try:
        print(summarize_limits(["3", "5"]))
    except TypeError as exc:
        print(type(exc).__name__, exc)