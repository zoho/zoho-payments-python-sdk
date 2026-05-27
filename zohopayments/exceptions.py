"""SDK exception hierarchy.

ZohoPaymentsException             - base SDK exception
  ConnectionException             - network/IO failure
  ZohoPaymentsAPIException        - base for HTTP non-2xx responses
    AuthenticationException       - 401
    PermissionException           - 403
    ResourceNotFoundException     - 404
    InvalidRequestException       - 400 / 422
    RateLimitException            - 429
"""

from typing import Optional


class ZohoPaymentsException(Exception):
    """Base SDK exception."""

    def __init__(self, message: str, cause: Optional[BaseException] = None) -> None:
        super().__init__(message)
        if cause is not None:
            self.__cause__ = cause


class ConnectionException(ZohoPaymentsException):
    """Network/IO failure during a request."""


class ZohoPaymentsAPIException(ZohoPaymentsException):
    """Base for HTTP non-2xx API responses."""

    def __init__(
        self,
        http_status_code: int,
        code_string: Optional[str],
        error_message: Optional[str],
    ) -> None:
        message = (
            f"API error (HTTP {http_status_code}): "
            f"code={code_string}, message={error_message}"
        )
        super().__init__(message)
        self._http_status_code = http_status_code
        self._code_string = code_string
        self._error_message = error_message

    @property
    def http_status_code(self) -> int:
        return self._http_status_code

    @property
    def code_string(self) -> Optional[str]:
        return self._code_string

    @property
    def api_error_message(self) -> Optional[str]:
        return self._error_message


class AuthenticationException(ZohoPaymentsAPIException):
    """HTTP 401 - invalid or expired OAuth token."""

    def __init__(
        self, code_string: Optional[str], error_message: Optional[str]
    ) -> None:
        super().__init__(401, code_string, error_message)


class PermissionException(ZohoPaymentsAPIException):
    """HTTP 403 - insufficient permissions."""

    def __init__(
        self, code_string: Optional[str], error_message: Optional[str]
    ) -> None:
        super().__init__(403, code_string, error_message)


class ResourceNotFoundException(ZohoPaymentsAPIException):
    """HTTP 404 - resource not found."""

    def __init__(
        self, code_string: Optional[str], error_message: Optional[str]
    ) -> None:
        super().__init__(404, code_string, error_message)


class InvalidRequestException(ZohoPaymentsAPIException):
    """HTTP 400 or 422 - malformed request or validation error."""

    def __init__(
        self,
        http_status_code: int,
        code_string: Optional[str],
        error_message: Optional[str],
    ) -> None:
        super().__init__(http_status_code, code_string, error_message)


class RateLimitException(ZohoPaymentsAPIException):
    """HTTP 429 - too many requests."""

    def __init__(
        self, code_string: Optional[str], error_message: Optional[str]
    ) -> None:
        super().__init__(429, code_string, error_message)
