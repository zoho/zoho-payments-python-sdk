from __future__ import annotations

from abc import ABC, abstractmethod
from zohopayments.net.request import ZohoRequest
from zohopayments.net.response import ZohoResponse

class HttpClientInterface(ABC):
    """Pluggable HTTP transport.

    Implementations must convert a :class:`ZohoRequest` into an HTTP call
    and return the :class:`ZohoResponse`. Network failures should raise
    :class:`zohopayments.exceptions.ConnectionException`.
    """

    @abstractmethod
    def execute(self, request: ZohoRequest) -> ZohoResponse:
        """Execute the request and return the response."""

    def close(self) -> None:
        """Release any transport-level resources. Safe to call multiple times."""
