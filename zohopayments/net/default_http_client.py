from __future__ import annotations

import threading
import requests

from zohopayments._internal.defaults import (
    DEFAULT_CONNECT_TIMEOUT,
    DEFAULT_REQUEST_TIMEOUT,
)
from zohopayments.exceptions import ConnectionException
from zohopayments.net.http_client_interface import HttpClientInterface
from zohopayments.net.request import ZohoRequest
from zohopayments.net.response import ZohoResponse

class DefaultHttpClient(HttpClientInterface):
    def __init__(
        self,
        connect_timeout: float = DEFAULT_CONNECT_TIMEOUT,
        default_timeout: float = DEFAULT_REQUEST_TIMEOUT,
    ) -> None:
        self._connect_timeout = float(connect_timeout)
        self._default_timeout = float(default_timeout)
        self._session: requests.Session = requests.Session()
        self._closed = threading.Event()
        self._close_lock = threading.Lock()

    def execute(self, request: ZohoRequest) -> ZohoResponse:
        if self._closed.is_set():
            raise ConnectionException("HTTP client has been closed")

        # Flatten multi-valued headers to comma-joined strings (RFC 7230 §3.2.2)
        flat_headers = {k: ", ".join(v) for k, v in request.headers.items()}

        body = request.body
        timeout = request.timeout if request.timeout is not None else self._default_timeout

        try:
            resp = self._session.request(
                method=request.method.value,
                url=request.url,
                headers=flat_headers,
                data=body.encode("utf-8") if body else None,
                timeout=(self._connect_timeout, timeout),
            )
        except requests.exceptions.Timeout as exc:
            raise ConnectionException(f"Request timed out: {exc}") from exc
        except requests.exceptions.ConnectionError as exc:
            raise ConnectionException(f"Connection error: {exc}") from exc
        except requests.exceptions.RequestException as exc:
            raise ConnectionException(f"Transport failure: {exc}") from exc

        # Re-expand headers into list form (ZohoResponse contract)
        response_headers = {name: [value] for name, value in resp.headers.items()}
        text_body = resp.text if resp.content else None

        return ZohoResponse(
            status_code=resp.status_code,
            headers=response_headers,
            body=text_body,
        )

    def close(self) -> None:
        with self._close_lock:
            if self._closed.is_set():
                return
            self._closed.set()
        try:
            self._session.close()
        except Exception:  # pragma: no cover
            pass
