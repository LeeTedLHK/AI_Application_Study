"""Day 6 闭卷巩固（10～15 分钟，无答案）。

目标：回忆 JSON 与 Python 的对应关系，并交错复习参数、返回值和导入。
方式：先不运行、不查讲义，在聊天中独立回答三题；答完再验证。
输入：各题给定代码。输出：你预测的输出、类型及理由。
验收：大小写与引号含义准确；区分打印与返回；解释导入和调用顺序。
本文件仅保存注释题面，不会运行题中代码或自动揭示答案。
"""

# 题 1：以下三个 print 分别输出什么？JSON 文本的空格不计分。
# import json
# data = json.loads('{"active": true, "note": null}')
# print(data["active"])
# print(data["note"])
# print(json.dumps(data))

# 题 2：a、b、c 在 Python 中分别是什么类型？
# 哪些能被 json.loads 成功解析？逐一解释不能解析的原因。
# a = "{'active': false}"
# b = '{"active": False}'
# c = '{"active": false}'

# 题 3：假设下面两段代码分别保存在同目录中的两个文件里。
# 在新进程中执行 python app.py，按顺序写出全部输出。
# result 保存什么？默认值 100 是否在这次运行中被用于生成配置？
# 本题不要求你实际创建这两个文件。
#
# config_tools.py:
# import json
# print("loaded")
# def make_config(limit=100):
#     print(json.dumps({"limit": limit}))
# if __name__ == "__main__":
#     make_config()
#
# app.py:
# from config_tools import make_config
# result = make_config(0)
# print(result)
