"""Day 22 编码练习：为 HTTP GET 增加有限的连接异常重试。

业务目标：元数据服务可能暂时无法建立连接；对幂等 GET，可以在明确上限内
重试连接类异常，但不能把 404 或读取超时都伪装成可重试故障。

请亲手实现 fetch_status_with_retry(
    url: str,
    timeout: float = 3.0,
    max_attempts: int = 3,
) -> int：
1. 每次尝试都使用 httpx.get(url, timeout=timeout)。
2. 收到响应后调用 response.raise_for_status()，成功时返回状态码。
3. 只捕获并重试 httpx.ConnectError、httpx.ConnectTimeout。
4. 404 等 HTTPStatusError 不重试；本轮 ReadTimeout 也不重试，直接传播。
5. 达到 max_attempts 后传播最后一次连接异常；不能无限重试。
6. 不访问真实服务之外的副作用，不打印，不加入 retry、退避或 POST 逻辑。

测试使用 monkeypatch 替换 httpx.get，不访问真实网络。
运行：
    python -m pytest -q learning/python/week02/test_day22_http_retry.py

验收：四项测试通过，并能解释为什么 404 与 ReadTimeout 各只调用一次。
"""

import httpx


def fetch_status_with_retry(
    url: str,
    timeout: float = 3.0,
    max_attempts: int = 3,
) -> int:
    """有限重试连接类异常，成功时返回 HTTP 状态码。"""
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    count = 0
    while count < max_attempts:
        try:
            response = httpx.get(url, timeout=timeout)
            response.raise_for_status()
            return response.status_code
        except (httpx.ConnectError, httpx.ConnectTimeout) as error:
            count += 1
            if count >= max_attempts:
                raise error