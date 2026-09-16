"""Day 19 编码练习：为查询任务增加带上下文的日志。

业务背景：智能取数服务需要从日志中判断哪张表、使用什么 limit、
查询执行到哪一步。业务模块只记录事件，全局日志配置由应用入口负责。

请亲手完成 run_query(table_name: str, limit: int) -> dict[str, object]：
1. 模块使用 logging.getLogger(__name__) 获取 logger。
2. 函数开始时记录 INFO，消息包含 table_name 和 limit。
3. 当 limit >= 500 时额外记录 WARNING，消息包含 table_name 和 limit。
4. 构造并返回：
   {"table_name": table_name, "limit": limit, "row_count": 0}
5. 返回前记录 INFO，消息包含 table_name 和 row_count。
6. 本模块不调用 logging.basicConfig，不使用 print，导入时无输出。

验收场景：
- orders / 100：两条 INFO，没有 WARNING，返回值正确。
- orders / 600：两条 INFO，中间一条 WARNING，返回值正确。
- 仅 import 本模块：无输出。

完成后请解释：为什么 basicConfig 属于应用入口，而 logger 属于业务模块。
本文件不提供核心实现答案。
"""

import logging


logger = logging.getLogger(__name__)


def run_query(table_name: str, limit: int) -> dict[str, object]:
    """记录查询生命周期并返回模拟查询结果。"""
    logger.info("query started: table=%s limit=%s", table_name, limit)
    if limit >= 500:
        logger.warning(f"High limit for table: {table_name}, limit: {limit}")

    config = {"table_name": table_name, "limit": limit, "row_count": 0}
    logger.info("query completed: table=%s row_count=%s", table_name, config["row_count"])

    return config
