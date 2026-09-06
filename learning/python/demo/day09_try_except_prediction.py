"""Day 9 阅读预测：先不要运行，闭卷回答文件末尾的三个问题。"""

import json


def parse_config(json_text):
    try:
        data = json.loads(json_text)
        return data
    except json.JSONDecodeError:
        return None


valid_result = parse_config('{"limit": 20}')
invalid_result = parse_config('{"limit": 20,}')


"""
请回答：

1. valid_result 保存什么？try 中执行到哪一行，except 是否执行？
2. invalid_result 保存什么？第二次调用时，data 赋值和 try 中的 return
   是否执行？为什么？
3. 如果 try 中抛出 FileNotFoundError，这个 except 会处理它吗？
   程序会继续返回 None，还是异常继续向外传播？

答完后再运行：
    python -X utf8 -B learning/python/week01/day09_try_except_prediction.py

注意：文件本身没有 print，因此直接运行不会显示结果。需要先做代码预测。
"""
