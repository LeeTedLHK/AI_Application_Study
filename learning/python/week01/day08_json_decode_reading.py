'''Day 8 练习：读取 JSONDecodeError traceback。

要求：先阅读 0008 讲义，再不运行代码，独立回答下面四问。
用途：区分“路径打不开”和“文件打开了但内容解析失败”。
本文件只有题面，不执行读写，也不包含标准答案。

非法 JSON 文件内容：
    {
      "table_name": "orders",
      "limit": 20,
    }

真实 traceback 的关键部分：
    File ".../day08_invalid_json_demo.py", line 19, in main
        config = load_config(path)
    File ".../day08_invalid_json_demo.py", line 13, in load_config
        return json.load(f)
    ... Python json 标准库内部调用 ...
    json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 4 column 1 (char 43)

问题：
1. 异常类型是什么？错误详情指向 JSON 文本的第几行、第几列？
2. 我们自己的代码中，哪一行发起 load_config 调用？哪一行触发解析？
3. 这次 open 是否成功？从 traceback 和控制流怎样判断？
4. JSON 文件哪处不合法？只修改一个字符，应删除哪个字符？

验收：准确区分 Python 代码行号与 JSON 文本行列，并说明失败阶段和最小修复。
暂不写 try / except，也不要修改演示用的非法 JSON 文件。
'''
