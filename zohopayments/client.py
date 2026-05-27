from __future__ import annotations

import threading
from types import TracebackType
from typing import Dict, Optional, Type, Union

from zohopayments._internal.defaults import (
    DEFAULT_CONNECT_TIMEOUT,
    DEFAULT_REQUEST_TIMEOUT,
)

from zohopayments._internal.token_manager import TokenManager
from zohopayments._internal.zoho_http_client import ZohoHttpClient
from zohopayments.auth.oauth_token import OAuthToken
from zohopayments.edition import Edition
from zohopayments.net.http_client_interface import HttpClientInterface
from zohopayments.services.collect_service import CollectService
from zohopayments.services.customer_service import CustomerService
from zohopayments.services.mandate_service import MandateService
from zohopayments.services.payment_link_service import PaymentLinkService
from zohopayments.services.payment_method_service import PaymentMethodService
from zohopayments.services.payment_method_session_service import (
    PaymentMethodSessionService,
)
from zohopayments.services.payment_service import PaymentService
from zohopayments.services.payment_session_service import PaymentSessionService
from zohopayments.services.refund_service import RefundService


class ZohoPaymentsClient:
    def __init__(
        self,
        http_client: ZohoHttpClient,
        token_manager: TokenManager,
        edition: Edition,
    ) -> None:
        self._http_client = http_client
        self._token_manager = token_manager
        self._edition = edition

        self._payment_links = PaymentLinkService(http_client)
        self._payment_sessions = PaymentSessionService(http_client)
        self._customers = CustomerService(http_client, edition)
        self._payments = PaymentService(http_client, edition)
        self._refunds = RefundService(http_client)
        self._payment_methods = PaymentMethodService(http_client)
        self._payment_method_sessions = PaymentMethodSessionService(http_client)
        self._mandates = MandateService(http_client)
        self._collect = CollectService(http_client)

        self._closed = False
        self._close_lock = threading.Lock()


    def payment_links(self) -> PaymentLinkService:
        return self._payment_links

    def payment_sessions(self) -> PaymentSessionService:
        return self._payment_sessions

    def customers(self) -> CustomerService:
        return self._customers

    def payments(self) -> PaymentService:
        return self._payments

    def refunds(self) -> RefundService:
        return self._refunds

    def payment_methods(self) -> PaymentMethodService:
        """Requires :attr:`Edition.US`."""
        if not self._edition.is_us():
            raise NotImplementedError(
                "payment_methods() is available only on Edition.US"
            )
        return self._payment_methods

    def payment_method_sessions(self) -> PaymentMethodSessionService:
        """Requires :attr:`Edition.US`."""
        if not self._edition.is_us():
            raise NotImplementedError(
                "payment_method_sessions() is available only on Edition.US"
            )
        return self._payment_method_sessions

    def mandates(self) -> MandateService:
        """Requires :attr:`Edition.IN`."""
        if not self._edition.is_in():
            raise NotImplementedError(
                "mandates() is available only on Edition.IN / Edition.IN_SANDBOX"
            )
        return self._mandates

    def collect(self) -> CollectService:
        """Requires :attr:`Edition.IN`."""
        if not self._edition.is_in():
            raise NotImplementedError(
                "collect() is available only on Edition.IN / Edition.IN_SANDBOX"
            )
        return self._collect


    def update_token(self, new_access_token: str) -> None:
        """Replace the stored OAuth access token. Thread-safe."""
        self._token_manager.update_token(new_access_token)

    def close(self) -> None:
        """Release transport-level resources. Idempotent."""
        with self._close_lock:
            if self._closed:
                return
            self._closed = True
            self._http_client.close()

    def __enter__(self) -> "ZohoPaymentsClient":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        self.close()

_RESERVED_HEADERS = frozenset(
    {
        "authorization",
        "user-agent",
        "accept",
        "content-type",
        "content-length",
        "host",
    }
)

class ZohoPaymentsClientBuilder:
    DEFAULT_CONNECT_TIMEOUT: float = DEFAULT_CONNECT_TIMEOUT
    DEFAULT_REQUEST_TIMEOUT: float = DEFAULT_REQUEST_TIMEOUT

    def __init__(self) -> None:
        self._account_id: Optional[str] = None
        self._edition: Optional[Edition] = None
        self._access_token: Optional[str] = None
        self._http_client: Optional[HttpClientInterface] = None
        self._connect_timeout: Optional[float] = None
        self._request_timeout: Optional[float] = None
        self._default_headers: Dict[str, str] = {}
        self._consumed = False

    def account_id(self, account_id: str) -> "ZohoPaymentsClientBuilder":
        """Zoho account ID for which the SDK makes API calls. Required."""
        self._account_id = account_id
        return self

    def edition(self, edition: Edition) -> "ZohoPaymentsClientBuilder":
        """Target edition: :attr:`Edition.IN`, :attr:`Edition.IN_SANDBOX`, or :attr:`Edition.US`. Required."""
        self._edition = edition
        return self

    def oauth_token(
        self, token: Union[str, OAuthToken]
    ) -> "ZohoPaymentsClientBuilder":
        """Accept either a raw access-token string or an :class:`OAuthToken`."""
        if isinstance(token, OAuthToken):
            self._access_token = token.access_token
        elif isinstance(token, str):
            self._access_token = token
        else:
            raise TypeError("oauth_token must be a str or OAuthToken")
        return self

    def http_client(
        self, http_client: HttpClientInterface
    ) -> "ZohoPaymentsClientBuilder":
        """Supplies a custom HTTP transport. Cannot be combined with :meth:`connect_timeout` — a custom transport controls its own timeouts."""
        self._http_client = http_client
        return self

    def connect_timeout(self, seconds: float) -> "ZohoPaymentsClientBuilder":
        """TCP connect timeout for the default transport, in seconds. Default: 30."""
        self._connect_timeout = float(seconds)
        return self

    def request_timeout(self, seconds: float) -> "ZohoPaymentsClientBuilder":
        """Per-request read timeout, in seconds. Default: 60."""
        self._request_timeout = float(seconds)
        return self

    def add_default_header(
        self, name: str, value: str
    ) -> "ZohoPaymentsClientBuilder":
        """Adds a default header sent with every request. SDK-managed headers (``Authorization``, ``User-Agent``, ``Accept``, ``Content-Type``, ``Content-Length``, ``Host``) are rejected."""
        if name is None or name == "":
            raise ValueError("header name must not be null or empty")
        if name.lower() in _RESERVED_HEADERS:
            raise ValueError(
                f"header {name!r} is managed by the SDK and cannot be overridden"
            )
        self._default_headers[name] = value
        return self

    def build(self) -> ZohoPaymentsClient:
        """Builds a :class:`ZohoPaymentsClient`. The builder is single-use; further calls raise :exc:`RuntimeError`."""
        if self._consumed:
            raise RuntimeError("Builder has already been consumed")
        self._consumed = True

        if self._account_id is None or self._account_id == "":
            raise ValueError("account_id is required")
        if self._edition is None:
            raise ValueError("edition is required")
        if self._access_token is None or self._access_token == "":
            raise ValueError("oauth_token is required")

        if self._http_client is not None and self._connect_timeout is not None:
            raise ValueError(
                "connect_timeout and a custom http_client are mutually exclusive"
            )

        transport: HttpClientInterface
        if self._http_client is not None:
            transport = self._http_client
        else:
            from zohopayments.net.default_http_client import DefaultHttpClient

            connect_timeout = (
                self._connect_timeout
                if self._connect_timeout is not None
                else self.DEFAULT_CONNECT_TIMEOUT
            )
            default_request_timeout = (
                self._request_timeout
                if self._request_timeout is not None
                else self.DEFAULT_REQUEST_TIMEOUT
            )
            transport = DefaultHttpClient(
                connect_timeout=connect_timeout,
                default_timeout=default_request_timeout,
            )

        token_manager = TokenManager(self._access_token)
        http_client = ZohoHttpClient(
            transport=transport,
            token_manager=token_manager,
            edition=self._edition,
            account_id=self._account_id,
            request_timeout=self._request_timeout,
            default_headers=self._default_headers,
        )
        return ZohoPaymentsClient(http_client, token_manager, self._edition)
