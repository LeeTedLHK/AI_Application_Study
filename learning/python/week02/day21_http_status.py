"""Day 21 编码练习：HTTP GET、状态码与 timeout。

业务目标：智能取数服务向元数据 HTTP 服务请求表信息时，要区分成功、
服务明确返回错误，以及请求过程超时。本章只练一次同步 GET，不加入 retry。

请亲手实现 fetch_status(url: str, timeout: float = 3.0) -> int：
1. 使用 httpx.get 向 url 发起 GET，并传入 timeout 参数。
2. 收到响应后调用 response.raise_for_status()；非 2xx 不返回状态码。
3. 成功时返回 response.status_code。
4. 不吞掉 HTTPStatusError 或 TimeoutException，不打印、不在导入时发请求。

输入与预期：
- 服务返回 200、timeout=2.5：返回整数 200，且客户端收到 timeout=2.5。
- 服务返回 404：向调用方传播 httpx.HTTPStatusError。
- 请求读取超时：向调用方传播 httpx.ReadTimeout。

约束：只修改本文件的核心函数；不改测试或业务结果来获得绿色结果。
测试使用替身 httpx.get，不访问真实网络。

在仓库根目录运行：
    python -m pytest -q learning/python/week02/test_day21_http_status.py

验收：三个测试通过；能解释 404 是收到错误响应后由 raise_for_status()
抛出的异常，ReadTimeout 是请求阶段未及时得到数据而抛出的异常。
"""

import httpx


def fetch_status(url: str, timeout: float = 3.0) -> int:
    """向元数据服务发起 GET，成功时返回状态码。"""
    respond = httpx.get(url, timeout=timeout)
    respond.raise_for_status()
    return respond.status_code
