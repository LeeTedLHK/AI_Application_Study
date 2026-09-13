"""Day 17：Pydantic v2 BaseModel——先预测，再亲手补齐。

第一阶段（先在对话中回答，不运行）：
对下面四个调用分别回答：
1. 返回的字段值与字段类型是什么？
2. 会不会抛出 pydantic.ValidationError？

调用：
1. QueryInput.model_validate({"table_name": "orders"})
2. QueryInput.model_validate({"table_name": "orders", "limit": "20"})
3. QueryInput.model_validate({"table_name": "orders", "limit": -1})
4. QueryInput.model_validate({"limit": 20})

第二阶段（回答后再实现）：
补齐 QueryInput 和 normalize_query。
要求：
- table_name 是必填 str；
- limit 是 int，默认值 100，允许范围为 0 到 1000（含两端）；
- 使用 Pydantic v2 的模型校验方法；
- normalize_query(data: dict) -> QueryInput 返回已验证模型；
- 不在函数内手写 if 做范围校验；不要捕获或吞掉 ValidationError；
- 模块导入无输出；演示应覆盖默认值、字符串数字转换和预期失败。

验收：
- 四个阅读预测准确；
- 能用 model_dump() 得到普通字典；
- 0 和 1000 合法，-1 和 1001 失败；
- "20" 能得到整数 20；
- 缺少 table_name 会失败；
- 完成后亲手修改一个输入案例并解释变化。

核心实现由学习者完成，文件不提供标准答案。
"""

from pydantic import BaseModel, Field, ValidationError


class QueryInput(BaseModel):
    table_name: str
    limit: int = Field(default=100, ge=0, le=1000)


def normalize_query(data: dict) -> QueryInput:
    return QueryInput.model_validate(data)


if __name__ == "__main__":
    # print(str(200) + "abc")
    print(normalize_query({"table_name": "orders"}).model_dump())
    print(normalize_query({"table_name": "orders", "limit": "20"}).model_dump())
    try:
        print(normalize_query({"table_name": "orders", "limit": -1}).model_dump())
    except ValidationError as e:
        print(type(e).__name__, e)
    try:
        print(normalize_query({"limit": 20}).model_dump())
    except ValidationError as e:
        print(type(e).__name__, e)

    # print(normalize_query({"table_name": "orders", "limit": "abc"}).model_dump())