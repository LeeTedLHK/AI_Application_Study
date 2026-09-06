"""Day 9 亲手练习：为 JSON 配置加载增加精确异常处理。

业务目标：
后端或 Agent 启动时加载查询配置。合法配置正常返回；文件不存在或 JSON
格式非法时，返回结构化错误，使调用方能够根据 error 字段采取不同动作。

输入：
- path：JSON 配置文件路径；
- 文件存在时使用 UTF-8；
- 合法文件的顶层内容是 JSON object。

输出契约：
- 成功：{"ok": True, "data": <解析后的字典>, "error": None}
- 文件不存在：{"ok": False, "data": None, "error": "file_not_found"}
- JSON 非法：{"ok": False, "data": None, "error": "invalid_json"}

约束：
- 复用 day07_load_query_config.load_query_config，不重复写 open / json.load；
- 使用一个 try 和两个精确的 except 分支；
- 只处理 FileNotFoundError 与 json.JSONDecodeError；
- 不使用 except Exception、裸 except、print 或写死业务配置；
- 不修改 Day 7 函数及测试预期。

动手顺序：
1. 先写三行中文伪代码，描述成功、文件缺失、JSON 非法三条路径；
2. 再替换函数中的占位 return；
3. 运行 test_day09_safe_config_loader.py。

验收：
三个测试全部通过，并能解释为什么未知异常仍应继续抛出。
"""

import json

from day07_load_query_config import load_query_config


def load_query_config_safely(path):
    """按模块说明中的固定结构返回成功数据或已知错误。"""
    # 复用 day07_load_query_config.load_query_config(path) 读取配置
    # 如果成功，返回 {"ok": True, "data": <解析后的字典>, "error": None}
    # 如果文件不存在，返回 {"ok": False, "data": None, "error": "file_not_found"}
    # 如果 JSON 非法，返回 {"ok": False, "data": None, "error": "invalid_json"}

    try:
        data = load_query_config(path)
        return {"ok": True, "data": data, "error": None}
    except FileNotFoundError:
        return {"ok": False, "data": None, "error": "file_not_found"}
    except json.JSONDecodeError:
        return {"ok": False, "data": None, "error": "invalid_json"}
