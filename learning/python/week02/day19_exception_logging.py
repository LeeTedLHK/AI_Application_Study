"""Day 19 编码练习：记录异常 traceback，并维持明确的返回契约。

业务背景：查询入口暂时接收到文本形式的 limit。这里用一个最小适配函数
练习异常日志；真实 API / Tool 输入后续仍优先交给 Pydantic 校验。

请亲手完成 parse_query_limit(raw_limit: str) -> int | None：
1. 模块使用 logging.getLogger(__name__) 获取 logger。
2. 在 try 中使用 int(raw_limit) 转换整数。
3. 只捕获 ValueError，不使用 except Exception。
4. 转换失败时使用 logger.exception 记录 ERROR 和 traceback；
   消息必须包含 raw_limit，然后返回 None。
5. 转换成功时记录 INFO，消息包含 raw_limit 和转换后的 limit，再返回整数。
6. 本模块不调用 logging.basicConfig，不使用 print，导入时无输出。

验收场景：
- "25"：一条 INFO，返回 25（int）。
- "abc"：一条 ERROR 和 traceback，返回 None；调用方能继续执行。
- 仅 import 本模块：无输出。

完成后请解释：本题为什么会继续运行；如果把 except 中的 return None
替换为 raise，返回值和调用方后续语句会发生什么。
本文件不提供核心实现答案。
"""

import logging


logger = logging.getLogger(__name__)


def parse_query_limit(raw_limit: str) -> int | None:
    """把文本 limit 转成整数；无法解析时记录异常并返回 None。"""
    try:
        limit = int(raw_limit)
    except ValueError:
        logger.exception("limit parsing failed: %s", raw_limit)
        return None

    logger.info("limit parsed successfully: raw=%s limit=%s", raw_limit, limit)
    return limit
