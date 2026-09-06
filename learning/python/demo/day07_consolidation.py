'''Day 7 收尾巩固：文件读取、JSON 类型、函数与模块。

用时：约 10～15 分钟，包含作答与反馈。
要求：先不运行、不看讲义，在聊天中回答；本文件只有题面，不会读取文件。
不需要修改已验收的 load_query_config 实现，不引入新核心概念。
用途：AI 后端读取配置时，正确区分值类型、文件状态与函数返回约定。
验收：三题的输出、类型、失败位置及理由正确；有误先纠正再判定章节完成。

题 1：JSON 值与类型（假设 path 指向存在、可读的 UTF-8 JSON 文件）

文件内容：
    {"active": false, "label": "false", "limit": 0}

预测代码：
    import json

    def load_config(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    config = load_config(path)
    print(config["active"])
    print(config["label"])
    print(config["limit"])

问题：三行输出依次是什么？三个字段值分别是什么 Python 类型？

题 2：最小改错（文件条件与题 1 相同）

作答记录：以下代码已由学习者修正；原题 return json.load(f) 与 with 同级。
保留原问题用于回顾，原题会失败，修正后的运行结果记录在当日 session notes。

预测代码：
    import json

    def load_config(path):
        with open(path, "r", encoding="utf-8") as f:
            print("opened")
            return json.load(f)

    config = load_config(path)
    print("done")

问题：程序停止前会打印什么？哪一行出错，原因是什么？
亲手写出只调整缩进后的函数，让调用方拿到解析后的数据；保留两条 print。
不需要写出异常名称。

题 3：导入、显式参数与返回值

假设两个文件放在同一目录，在新的 Python 进程执行 python app.py。
config_tools.py 内容：
    print("loading")

    def build_config(limit=100):
        print(limit)

    if __name__ == "__main__":
        build_config()

app.py 内容：
    from config_tools import build_config

    result = build_config(0)
    print(result)

问题：精确输出顺序是什么？result 保存什么？默认值 100 会打印吗，为什么？
'''
