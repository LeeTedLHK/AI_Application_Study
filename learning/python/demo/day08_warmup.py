'''Day 8 开场复测：返回数据与文件关闭时机。

时间：约 2 分钟。
要求：先不运行、不看 Day 7 讲义，在聊天中回答。
用途：确认进入异常与 traceback 前，已经稳定掌握文件读取的正常路径。
验收：准确说明返回对象、文件关闭时机，以及返回值能否继续使用。
本文件只有注释题面，运行不会读写文件或显示答案。

假设 path 指向存在、可读的 UTF-8 JSON 文件，内容为：
    {"active": false, "limit": 0}

代码：
    import json

    def load_config(path):
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config

    result = load_config(path)
    print(result["active"])

问题：
1. 调用方拿到 result 时，result 是什么 Python 类型？f 是否已经关闭？
2. 最后一行输出什么？读取 result["active"] 是否需要重新打开文件？为什么？
'''
