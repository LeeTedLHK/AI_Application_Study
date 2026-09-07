"""Day 7 亲手练习：读取 JSON 查询配置，核心函数由学习者实现。"""

import json


def load_query_config(path):
    """读取指定文件，把解析后的配置字典返回给调用方。

    业务目标：为后端服务 / Agent 工具加载查询配置。
    输入：path 是已有文件的路径字符串；文件为 UTF-8 编码，
          内容是合法 JSON object，假设存在且可读。
    输出：dict，保留全部字段、值、嵌套内容及解析后应有的类型。

    示例：文件内容为 {"table_name": "orders", "limit": 20, "active": true}，
          返回对应的 Python 字典，而不是路径、JSON 字符串或 None。
    边界：limit=0、active=false、label="False" 与中文内容应原样保留其含义。

    约束：
    - 使用传入的 path，不把某个固定路径或配置结果写死在函数内部；
    - 使用刚学过的 with、open 只读模式、UTF-8 与 json.load；
    - 通过 return 提供结果，函数内部不 print；不改写源文件；
    - 不使用 eval；本题不要求处理不存在的文件或非法 JSON。

    动手顺序：先写 2～3 行中文伪代码，再实现核心逻辑并移除占位。
    验收：同目录 test_day07_load_query_config.py 的三个测试均通过，
          并能解释返回字典和文件关闭之间的关系。
    """
    # 使用 with 语句打开文件
    # 用 json.load 读取文件内容

    # json.loads 处理字符串，json.load 处理文件
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)


def main():
    path = "E:/Project/AI_Application_Study/learning/python/demo/data/day07_query_config.json"
    result = load_query_config(path)
    print(result)


if __name__ == "__main__":
    main()
