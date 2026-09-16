"""Day 19 应用入口：统一配置日志并调用查询业务模块。"""

import logging

from day19_query_logging import run_query


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )
    run_query("orders", 100)
    run_query("orders", 600)


if __name__ == "__main__":
    main()
