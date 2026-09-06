"""Day 7 最小示例：从文件读取 JSON 配置，不写入文件。

本文件是导师提供的阅读示例，不作为学习者独立实现的证据。
输入：同一仓库 data/day07_query_config.json 中的合法 JSON object。
输出：依次打印 table_name 和 limit。先预测，再运行核对。
约束：只读，不修改源文件；暂不要求异常处理或编写自己的读取函数。
路径使用本机绝对路径以暂时排除工作目录干扰，后续练习再参数化。

阅读验收：
1. 两行输出分别是什么？config 的类型是什么？
2. 为什么这里使用 json.load(file)，而不是 json.loads(path)？
运行方式：python learning/python/week01/day07_read_json_demo.py
"""

import json


def main():
    path = "E:/Project/AI_Application_Study/learning/python/week01/data/day07_query_config.json"
    with open(path, "r", encoding="utf-8") as file:
        config = json.load(file)

    print(config["table_name"])
    print(config["limit"])


if __name__ == "__main__":
    main()
