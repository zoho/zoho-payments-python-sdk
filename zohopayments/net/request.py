from __future__ import annotations

from types import MappingProxyType
from typing import Dict, List, Mapping, Optional

from zohopayments.net.request_method import RequestMethod

class ZohoRequest:
    def __init__(
        self,
        method: RequestMethod,
        url: str,
        headers: Dict[str, List[str]],
        body: Optional[str],
        timeout: Optional[float],
    ) -> None:
        self._method = method
        self._url = url
        # Deep-unmodifiable copy of headers
        frozen: Dict[str, List[str]] = {}
        for k, v in headers.items():
            frozen[k] = tuple(v)  # type: ignore[assignment]
        self._headers: Mapping[str, List[str]] = MappingProxyType(frozen)  # type: ignore[arg-type]
        self._body = body
        self._timeout = timeout

    @property
    def method(self) -> RequestMethod:
        return self._method

    @property
    def url(self) -> str:
        return self._url

    @property
    def headers(self) -> Mapping[str, List[str]]:
        return self._headers

    @property
    def body(self) -> Optional[str]:
        return self._body

    @property
    def timeout(self) -> Optional[float]:
        """Per-request timeout in seconds, or None for transport default."""
        return self._timeout

    @staticmethod
    def builder() -> "ZohoRequestBuilder":
        return ZohoRequestBuilder()


class ZohoRequestBuilder:
    def __init__(self) -> None:
        self._method: Optional[RequestMethod] = None
        self._url: Optional[str] = None
        self._headers: Dict[str, List[str]] = {}
        self._body: Optional[str] = None
        self._timeout: Optional[float] = None

    def method(self, method: RequestMethod) -> "ZohoRequestBuilder":
        self._method = method
        return self

    def url(self, url: str) -> "ZohoRequestBuilder":
        self._url = url
        return self

    def header(self, name: str, value: str) -> "ZohoRequestBuilder":
        """Append a header value (allows multiple values per name)."""
        self._headers.setdefault(name, []).append(value)
        return self

    def set_header(self, name: str, value: str) -> "ZohoRequestBuilder":
        """Replace any existing values for the header name."""
        self._headers[name] = [value]
        return self

    def headers(self, headers: Mapping[str, str]) -> "ZohoRequestBuilder":
        for k, v in headers.items():
            self.header(k, v)
        return self

    def body(self, body: Optional[str]) -> "ZohoRequestBuilder":
        self._body = body
        return self

    def timeout(self, timeout: Optional[float]) -> "ZohoRequestBuilder":
        self._timeout = timeout
        return self

    def build(self) -> ZohoRequest:
        if self._method is None:
            raise ValueError("method is required")
        if self._url is None or self._url == "":
            raise ValueError("url is required")
        return ZohoRequest(
            method=self._method,
            url=self._url,
            headers=self._headers,
            body=self._body,
            timeout=self._timeout,
        )
