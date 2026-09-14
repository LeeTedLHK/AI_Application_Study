"""Day 18：显式加载 .env，观察已有环境变量优先。

依赖：python-dotenv，已安装版本 1.2.2。
前置：从仓库根目录运行；day18_config/.env 保存 DAY18_QUERY_LIMIT=25。
若刚克隆仓库，先将同目录 .env.example 复制为 .env。本练习无真实密钥。
.env 是 KEY=VALUE 文本；加载后值仍是字符串，不自动转为 int。
load_dotenv(path, override=False) 将文件值填入缺失的环境变量，已有值保留。
.env 保存本地值并由 Git 忽略；.env.example 保存可提交的无密钥示例。

演示先为当前进程设置 DAY18_QUERY_LIMIT="60"，再加载文件并读取。
闭卷预测：文件始终为 25，override=False，读取默认值为 "100"：
1. 若加载前已有环境变量值 "0"，最终得到什么值和类型？
2. 若加载前不存在该变量，最终得到什么值和类型？
3. 若加载前值为 "abc"，文件中的 25 会不会修复它？
首次回答不运行变体。验收：能解释已有环境变量、文件值、读取默认值的优先级，
并区分加载配置和验证配置。仅改变当前进程演示变量，不改永久系统环境。
运行：python -X utf8 -B learning/python/week01/day18_dotenv_demo.py
来源：https://bbc2.github.io/python-dotenv/
"""

import os
from dotenv import load_dotenv


if __name__ == "__main__":
    os.environ["DAY18_QUERY_LIMIT"] = "60"
    load_dotenv("learning/python/week01/day18_config/.env", override=False)
    raw = os.getenv("DAY18_QUERY_LIMIT", "100")
    print(raw)
    print(type(raw).__name__)
