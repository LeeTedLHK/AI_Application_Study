"""Day 8 阅读示例：文件存在，但 JSON 内容不合法。

用途：比较 JSONDecodeError 与 FileNotFoundError 的 traceback。
运行：python -X utf8 learning/python/demo/day08_invalid_json_demo.py
本例只读取 data/day08_invalid_config.json，不修改文件。
"""

import json


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    print("before parse")
    path = "E:/Project/AI_Application_Study/learning/python/demo/data/day08_invalid_config.json"
    config = load_config(path)
    print("after parse")
    return config


if __name__ == "__main__":
    main()
