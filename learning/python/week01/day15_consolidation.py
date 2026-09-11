"""Day 15 闭卷巩固，约 10～15 分钟。

任务：不看讲义、不运行代码，先在对话中按 Q1/Q2/Q3 回答。
约束：只使用已学的 list / dict 标注、默认值、sum、TypeError 和边界校验。
验收：Q1 输出与类型准确；Q2 标注层级修正准确；Q3 能指出运行时校验位置。
首次作答后再运行核对；本文件不提供标准答案。

Q1（3 分）：写出返回值及其类型。

    def pack_counts(counts: list[int]) -> dict[str, int]:
        return {"count": len(counts), "total": sum(counts)}

    result = pack_counts([2, 0, 4])

Q2（3 分）：需求是“列表中的每一项是一条记录；每条记录的 code 是字符串，count 是整数”。
下面哪个标注更准确？解释另一种标注表达了什么。

    A. list[dict[str, int]]
    B. dict[str, list[int]]

Q3（4 分）：函数签名写成 `rows: list[dict[str, int]]`，但调用方传入
`[{"code": "A", "count": "2"}]`。类型标注会自动拒绝或转换吗？
在 AI 工具函数中，输入校验和输出校验分别适合放在哪里？
"""
