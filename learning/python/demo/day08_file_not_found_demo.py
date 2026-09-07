"""Day 8 阅读示例：制造一个可重复的 FileNotFoundError。

用途：练习阅读 traceback，不处理异常、不修改任何文件。
运行：python -X utf8 learning/python/demo/day08_file_not_found_demo.py
预期：先打印 before load，然后在 open 所在行抛出 FileNotFoundError；
      after load 不会打印。
"""

import json


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    print("before load")
    config = load_config("missing-config.json")
    print("after load")
    return config


if __name__ == "__main__":
    main()
