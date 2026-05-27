"""Central HTTP client: authenticated request dispatch, envelope handling, and error mapping.

Instances are created by the ``ZohoPaymentsClient`` builder and shared across services.
"""

from __future__ import annotations

import threading
from typing import Any, Callable, Dict, List, Mapping, Optional, Type, TypeVar
from urllib.parse import quote

from zohopayments._version import SDK_NAME, SDK_VERSION
from zohopayments._internal.api_response import ApiResponse
from zohopayments._internal.json_util import (
    list_from_body,
    parse_object,
    read_page_context,
    to_json,
    unwrap,
)
from zohopayments._internal.query_params import QueryParams
from zohopayments._internal.token_manager import TokenManager
from zohopayments.edition import Edition
from zohopayments.exceptions import (
    AuthenticationException,
    ConnectionException,
    InvalidRequestException,
    PermissionException,
    RateLimitException,
    ResourceNotFoundException,
    ZohoPaymentsAPIException,
    ZohoPaymentsException,
)
from zohopayments.models.list_response import ListResponse
from zohopayments.net.http_client_interface import HttpClientInterface
from zohopayments.net.request import ZohoRequest
from zohopayments.net.request_method import RequestMethod

T = TypeVar("T")

MAX_ERROR_BODY_SNIPPET = 500
USER_AGENT = f"{SDK_NAME}/{SDK_VERSION}"


def encode_path(segment: str) -> str:
    """Percent-encode a path segment for safe inclusion in a URL path."""
    if segment is None:
        raise ValueError("path segment must not be None")
    # quote defaults to safe='/', we want nothing safe in a single segment
    return quote(segment, safe="")


class ZohoHttpClient:
    """Authenticated client bound to a specific account + edition."""

    def __init__(
        self,
        transport: HttpClientInterface,
        token_manager: TokenManager,
        edition: Edition,
        account_id: str,
        request_timeout: Optional[float],
        default_headers: Optional[Mapping[str, str]],
    ) -> None:
        self._transport = transport
        self._token_manager = token_manager
        self._edition = edition
        self._account_id = account_id
        self._request_timeout = request_timeout
        self._default_headers: Dict[str, str] = dict(default_headers or {})
        self._closed = threading.Event()
        self._close_lock = threading.Lock()


    def get(
        self, path: str, query: Optional[QueryParams] = None
    ) -> ApiResponse:
        return self.request(RequestMethod.GET, path, query, None)

    def post(self, path: str, body: Optional[Dict[str, Any]]) -> ApiResponse:
        return self.request(RequestMethod.POST, path, None, body)

    def put(
        self, path: str, body: Optional[Dict[str, Any]] = None
    ) -> ApiResponse:
        return self.request(RequestMethod.PUT, path, None, body)

    def delete(self, path: str) -> ApiResponse:
        return self.request(RequestMethod.DELETE, path, None, None)

    def request(
        self,
        method: RequestMethod,
        path: str,
        query: Optional[QueryParams],
        body: Optional[Dict[str, Any]],
    ) -> ApiResponse:
        if self._closed.is_set():
            raise ZohoPaymentsException("HTTP client has been closed")

        url = self._build_url(path, query)

        builder = ZohoRequest.builder().method(method).url(url)
        # User-provided default headers first (lower priority)
        for name, value in self._default_headers.items():
            builder.set_header(name, value)
        # SDK-managed headers override user defaults
        builder.set_header(
            "Authorization",
            f"Zoho-oauthtoken {self._token_manager.get_access_token()}",
        )
        builder.set_header("User-Agent", USER_AGENT)
        builder.set_header("Accept", "application/json")

        body_json: Optional[str] = None
        if body is not None:
            body_json = to_json(body)
            builder.set_header("Content-Type", "application/json")
            builder.body(body_json)

        if self._request_timeout is not None:
            builder.timeout(self._request_timeout)

        try:
            response = self._transport.execute(builder.build())
        except ConnectionException:
            raise
        except Exception as exc:  # pragma: no cover - transport may raise anything
            raise ConnectionException(f"Transport failure: {exc}") from exc

        raw_body = response.body
        parsed: Dict[str, Any] = {}
        if raw_body:
            try:
                parsed = parse_object(raw_body)
            except ZohoPaymentsException:
                # Non-JSON body on an error response - build synthetic object
                parsed = {}

        api_response = ApiResponse(response.status_code, parsed)

        if not api_response.is_success():
            self._raise_for_status(api_response, raw_body)

        return api_response


    def get_object(
        self,
        path: str,
        type_: Type[T],
        *envelope_keys: str,
    ) -> T:
        return unwrap(self.get(path).body, type_, *envelope_keys)

    def post_object(
        self,
        path: str,
        body: Optional[Dict[str, Any]],
        type_: Type[T],
        *envelope_keys: str,
    ) -> T:
        return unwrap(self.post(path, body).body, type_, *envelope_keys)

    def put_object(
        self,
        path: str,
        body: Optional[Dict[str, Any]],
        type_: Type[T],
        *envelope_keys: str,
    ) -> T:
        return unwrap(self.put(path, body).body, type_, *envelope_keys)

    def list_objects(
        self,
        path: str,
        query: Optional[QueryParams],
        item_from_dict: Callable[[Dict[str, Any]], T],
        *envelope_keys: str,
    ) -> ListResponse[T]:
        response = self.get(path, query)
        entries = list_from_body(response.body, *envelope_keys)
        items: List[T] = [item_from_dict(e) for e in entries if isinstance(e, dict)]
        page_context = read_page_context(response.body)
        return ListResponse(items, page_context)


    def _build_url(self, path: str, query: Optional[QueryParams]) -> str:
        base = self._edition.base_url
        if not path.startswith("/"):
            path = "/" + path

        qs = QueryParams()
        if query is not None:
            qs.add_all(query)
        qs.add("account_id", self._account_id)

        url = base + path
        if not qs.is_empty():
            url = f"{url}?{qs.to_query_string()}"
        return url

    def _raise_for_status(
        self, api_response: ApiResponse, raw_body: Optional[str]
    ) -> None:
        status = api_response.status_code
        code_string = api_response.get_code_string()
        message = api_response.get_message()

        if status in (400, 422):
            raise InvalidRequestException(status, code_string, message)
        if status == 401:
            raise AuthenticationException(code_string, message)
        if status == 403:
            raise PermissionException(code_string, message)
        if status == 404:
            raise ResourceNotFoundException(code_string, message)
        if status == 429:
            raise RateLimitException(code_string, message)
        raise ZohoPaymentsAPIException(status, code_string, message)

    def close(self) -> None:
        with self._close_lock:
            if self._closed.is_set():
                return
            self._closed.set()
        try:
            self._transport.close()
        except Exception:  # pragma: no cover
            pass
