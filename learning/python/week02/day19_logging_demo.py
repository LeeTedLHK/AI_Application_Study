"""Day 19 最小示例：日志级别、模块 logger 与入口配置。

从仓库根目录运行：
    python learning/python/week02/day19_logging_demo.py

预期：INFO 和 WARNING 出现，DEBUG 被 INFO 门槛过滤。
导入本模块时不配置日志、不调用演示函数，因此没有输出。
"""

import logging


logger = logging.getLogger(__name__)


def log_query_events() -> None:
    logger.debug("query prepared")
    logger.info("query started")
    logger.warning("query limit is high")


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )
    log_query_events()


if __name__ == "__main__":
    main()
