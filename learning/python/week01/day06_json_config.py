"""Day 6: 修改 JSON 查询配置；核心逻辑由学习者完成。"""

import json


def update_query_limit(json_text, new_limit):
    """返回仅更新 limit 的 JSON 字符串。

    业务目标：调整 API / Tool 的查询条数，同时保留其他配置。
    输入：json_text 是合法 JSON object 文本，包含 limit 字段；
          new_limit 是非负整数，0 也必须原样采用。
    输出：合法 JSON 字符串（str），解析后的 limit 等于 new_limit，
          其他字段及其类型、嵌套内容全部保持不变。

    示例输入：'{"status": "paid", "limit": 100}'，20
    示例输出：'{"status": "paid", "limit": 20}'
    输出的空格和字段顺序不作为验收条件。

    约束：
    - 使用已学 json 转换能力；不要手工拼接或替换 JSON 字符串；
    - 不使用 eval，不硬编码答案，不读取全局业务数据；
    - 通过 return 交回结果，函数内部不要 print；
    - 本题假设输入合法，不要求异常处理、HTTP、文件读写或参数校验。

    动手顺序：先在函数体写 3～4 行中文伪代码，再完成实现并移除占位。
    验收：运行同目录 test_day06_json_config.py，3 个测试均通过，
          并能说明输入、处理过程中和返回时的数据类型。
    """
    # 输入的是 json_text，输出的也是 json_text
    # 用 json.dumps 和 json.loads 进行转换
    # 转换出来的 dict 通过 dict["key"] 进行修改

    data = json.loads(json_text)
    data["limit"] = new_limit
    return json.dumps(data)



def main():
    source_text = '{"status": "paid", "limit": 100}'
    print(update_query_limit(source_text, 20))


if __name__ == "__main__":
    main()
