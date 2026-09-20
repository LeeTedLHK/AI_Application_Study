"""Day 21 HTTP 练习验收：用替身响应测试真实函数，不访问外网。

monkeypatch 在每个测试中临时替换 httpx.get；测试结束后 pytest 自动恢复。
学习者本章只需要实现 day21_http_status.py 中的 fetch_status，不修改测试预期。
"""

import httpx
import pytest

from day21_http_status import fetch_status


URL = "https://metadata.example.test/tables"


def test_success_returns_status_and_forwards_timeout(monkeypatch) -> None:
    """成功响应返回 200，并把显式 timeout 传给 HTTP 客户端。"""
    calls = []

    def fake_get(url, *, timeout):
        calls.append((url, timeout))
        return httpx.Response(200, request=httpx.Request("GET", url))

    monkeypatch.setattr(httpx, "get", fake_get)

    assert fetch_status(URL, timeout=2.5) == 200
    assert calls == [(URL, 2.5)]


def test_404_raises_status_error(monkeypatch) -> None:
    """收到 404 时不当成成功返回。"""
    def fake_get(url, *, timeout):
        return httpx.Response(404, request=httpx.Request("GET", url))

    monkeypatch.setattr(httpx, "get", fake_get)

    with pytest.raises(httpx.HTTPStatusError) as error:
        fetch_status(URL)

    assert error.value.response.status_code == 404


def test_read_timeout_propagates(monkeypatch) -> None:
    """请求超时向调用方传播，不伪装成成功状态。"""
    def fake_get(url, *, timeout):
        raise httpx.ReadTimeout("metadata service was slow", request=httpx.Request("GET", url))

    monkeypatch.setattr(httpx, "get", fake_get)

    with pytest.raises(httpx.ReadTimeout):
        fetch_status(URL, timeout=0.2)


if __name__ == "__main__":
    pytest.main(["-q", __file__])
