"""Day 22 HTTP retry 测试：只验证有限、明确的连接异常重试。

测试使用 monkeypatch 替换 httpx.get，不访问真实网络。
学习者只实现 day22_http_retry.py 中的 fetch_status_with_retry，不能修改预期。
"""

import httpx
import pytest

from day22_http_retry import fetch_status_with_retry


URL = "https://metadata.example.test/tables"


def response(status_code: int) -> httpx.Response:
    return httpx.Response(status_code, request=httpx.Request("GET", URL))


def test_connect_timeout_retries_then_returns_success(monkeypatch) -> None:
    """连接超时两次后成功，最多三次尝试。"""
    outcomes = [
        httpx.ConnectTimeout("connect slow"),
        httpx.ConnectTimeout("connect slow"),
        response(200),
    ]
    calls = 0

    def fake_get(url, *, timeout):
        nonlocal calls
        calls += 1
        outcome = outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(httpx, "get", fake_get)

    assert fetch_status_with_retry(URL, max_attempts=3) == 200
    assert calls == 3


def test_404_does_not_retry(monkeypatch) -> None:
    """资源不存在不是连接类暂时故障，只请求一次。"""
    calls = 0

    def fake_get(url, *, timeout):
        nonlocal calls
        calls += 1
        return response(404)

    monkeypatch.setattr(httpx, "get", fake_get)

    with pytest.raises(httpx.HTTPStatusError):
        fetch_status_with_retry(URL, max_attempts=3)

    assert calls == 1


def test_last_connect_error_propagates_after_max_attempts(monkeypatch) -> None:
    """连接异常持续发生时，达到次数后传播最后一次异常。"""
    calls = 0

    def fake_get(url, *, timeout):
        nonlocal calls
        calls += 1
        raise httpx.ConnectError("network down")

    monkeypatch.setattr(httpx, "get", fake_get)

    with pytest.raises(httpx.ConnectError):
        fetch_status_with_retry(URL, max_attempts=3)

    assert calls == 3


def test_read_timeout_does_not_retry(monkeypatch) -> None:
    """本轮策略只重试连接异常，读取超时直接传播。"""
    calls = 0

    def fake_get(url, *, timeout):
        nonlocal calls
        calls += 1
        raise httpx.ReadTimeout("response stalled")

    monkeypatch.setattr(httpx, "get", fake_get)

    with pytest.raises(httpx.ReadTimeout):
        fetch_status_with_retry(URL, max_attempts=3)

    assert calls == 1


def test_zero_max_attempts_is_rejected() -> None:
    """重试次数必须至少为一次。"""
    with pytest.raises(ValueError, match="max_attempts must be at least 1"):
        fetch_status_with_retry(URL, max_attempts=0)
