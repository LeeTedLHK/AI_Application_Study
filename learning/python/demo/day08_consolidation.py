"""Day 8 每日巩固：异常与 traceback 阅读。

本文件保留当天闭卷题目和答题后的复盘要点，不参与业务执行。

题目 1
------
traceback 从上到下依次出现：
- app.py 第 12 行：config = load_config(path)
- config_loader.py 第 6 行：return json.load(f)
- 多行 Python 标准库代码
- JSONDecodeError，并给出 JSON 文本第 4 行第 2 列

你会按什么顺序阅读？第一处重点检查的自己代码是哪一行？

题目 2
------
以下程序会输出什么、抛出什么异常、真正失败的操作在哪里？

    print("start")
    config = load_config("missing.json")
    print("finish")

题目 3
------
修改文件路径后程序不再抛异常，但实际结果是 orders / 20，预期是
events / 0 / False。任务完成了吗？下一步如何检查和验证？

作答后复盘
----------
1. 先读最后一行异常类型和详情，再看最靠近底部的自己代码
   return json.load(f)，最后向上追调用与输入。
2. 先输出 start，随后 open 缺失文件时抛出 FileNotFoundError，finish 不执行。
3. 未完成。无异常只代表程序没有在该路径失败；还要核对配置内容、比较
   actual / expected 并运行测试。

当日结果：9/10。下次先做约 2 分钟间隔复测。
"""
