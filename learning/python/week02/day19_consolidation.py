"""Day 19 每日闭卷巩固：logging、导入副作用与异常契约。

规则：先不运行代码，在聊天中回答三题；反馈后再按需实际验证。
本文件不提供标准答案。

Q1｜级别预测
假设新进程中执行：

    logging.basicConfig(
        level=logging.WARNING,
        format="%(levelname)s | %(message)s",
    )
    logger = logging.getLogger("query")
    logger.debug("prepared")
    logger.info("started")
    logger.warning("limit high")
    logger.error("query failed")

写出全部输出及顺序，并解释 WARNING 门槛的含义。

Q2｜异常控制流

    try:
        limit = int("abc")
    except ValueError:
        logger.exception("invalid limit")
        raise

    print("done")

ERROR 日志和 traceback 是否出现？done 是否出现？limit 是否完成赋值？
分别说明 logger.exception 与 raise 的职责。

Q3｜模块与敏感上下文
业务模块顶层只有 logger = logging.getLogger(__name__) 和函数定义；
应用入口只 import 该业务模块，但不调用函数。

1. 导入时是否会出现业务日志？为什么？
2. 一次失败请求有 request_id、table_name、limit、api_key 四个字段。
   哪些可以作为排查上下文，哪个必须排除？
3. basicConfig 应放在应用入口还是每个业务模块？为什么？

验收：三题均能区分配置、记录、捕获和传播；不泄露敏感字段。
"""

import logging
