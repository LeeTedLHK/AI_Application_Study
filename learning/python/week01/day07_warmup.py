"""Day 7 开场复测：约 2 分钟，先闭卷作答，再运行核对。

目的：跨日回忆 JSON 文本、Python 对象、布尔值与字符串的区别。
输入：下面两道题的代码；假设已 import json。
输出：在聊天中写出预测输出、类型和理由。
验收：输出大小写准确，区分合法 JSON 与合法 Python 字符串，
      区分布尔值与内容相似的字符串；本题不引入文件读写新知识。
题面以注释保存，运行此文件不会揭示答案。
"""

# 题 1：两个 print 分别输出什么？data 与 result 分别是什么类型？
# import json
# text = '{"active": false, "limit": 8}'
# data = json.loads(text)
# data["limit"] = 0
# result = json.dumps(data)
# print(data["active"])
# print(isinstance(result, str))

# 题 2：a、b 哪些能被 json.loads 成功解析？
# 对能解析的项，解析后 active 的值和 Python 类型分别是什么？
# 对不能解析的项，解释原因。
# a = '{"active": False}'
# b = '{"active": "false"}'

# 补测：先闭卷回答，再运行核对；不改原题，不要求写业务函数。
# 两个 print 分别输出什么？enabled 和 label 的 Python 类型分别是什么？
# 验收：分别说明值的显示结果和实际类型，不能只根据外观判断。
# import json
# data = json.loads('{"enabled": false, "label": "False"}')
# print(data["enabled"])
# print(data["label"])
