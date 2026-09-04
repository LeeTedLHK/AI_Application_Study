"""Day 8 动手 Debug：依次修复路径错误和非法 JSON。

业务场景：后端启动时读取一份查询配置。
当前状态：程序包含两个彼此独立的问题；第一次运行只能先看到第一个异常。

动手流程：
1. 运行本文件，按 traceback 说明异常类型、调用位置和失败位置；
2. 只修复当前异常的根因，再次运行；
3. 阅读第二个 traceback，只修复第二个根因；
4. 最后运行同目录 test_day08_debug_challenge.py 验收。

约束：
- 每次只修改一个根因，不同时猜改两个地方；
- 不修改 day07_load_query_config.py；
- 不增加 try / except，不删除读取逻辑或 print；
- 不把配置字典直接写死在 Python 中。

最终输出：
    start
    {'table_name': 'events', 'limit': 0, 'active': False}
    finish

验收：测试通过，并能分别说明两次异常为什么发生、各修改了哪里。
"""

from day07_load_query_config import load_query_config


def main():
    print("start")
    path = "E:/Project/AI_Application_Study/learning/python/week01/data/day08_debug_config.json"
    config = load_query_config(path)
    print(config)
    print("finish")
    return config


if __name__ == "__main__":
    main()
