"""Day 18：环境变量读取，先理解再预测。

os.environ 是当前进程的环境变量映射，键和值是字符串。
os.getenv(name, default) 读取变量；不存在时返回 default，不指定 default 时为 None。
环境变量存在但为空字符串，并不等于不存在。读取本身不会转换整数或校验范围。
本例设置的 DAY18_QUERY_LIMIT 仅用于当前进程演示，不修改永久系统配置，不读取密钥。

正常输入：DAY18_QUERY_LIMIT="25"。运行观察 raw 的值与类型。
闭卷预测：对 os.getenv("DAY18_QUERY_LIMIT", "100")，独立考虑：
1. 变量值为 "0"，结果是什么值和类型？
2. 变量不存在，结果是什么值和类型？
3. 变量值为 ""，会不会采用默认值 "100"？为什么？
首次回答不运行变体；验收为区分字符串读取、缺失默认值和空字符串。
运行：python -X utf8 -B learning/python/week01/day18_env_reading.py
来源：https://docs.python.org/3.11/library/os.html#os.getenv
"""

import os


if __name__ == "__main__":
    os.environ["DAY18_QUERY_LIMIT"] = "25"
    raw = os.getenv("DAY18_QUERY_LIMIT", "100")
    print(raw)
    print(type(raw).__name__)
