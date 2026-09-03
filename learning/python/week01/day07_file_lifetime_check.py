"""Day 7 文件生命周期追问，无答案。

只预测，不修改已经验收的 load_query_config。
输入：假设 path 指向存在、可读且内容合法的 UTF-8 JSON object 文件。
问题：result 获得什么对象？json.load(result) 是否成功？为什么？
验收：能根据返回对象和文件关闭时机解释结果；不要求具体异常名称。
下面仅为注释题面，运行本文件不会执行读取或泄露答案。
"""

# import json
# def open_config(path):
#     with open(path, "r", encoding="utf-8") as f:
#         return f
# result = open_config(path)
# config = json.load(result)
