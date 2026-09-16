"""Day 19 异常日志应用入口。"""

import logging

from day19_exception_logging import parse_query_limit


logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )

    valid_limit = parse_query_limit("25")
    invalid_limit = parse_query_limit("abc")
    logger.info(
        "parsing demo finished: valid_limit=%s invalid_limit=%s",
        valid_limit,
        invalid_limit,
    )


if __name__ == "__main__":
    main()
