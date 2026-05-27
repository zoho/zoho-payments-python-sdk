from __future__ import annotations

from typing import Any, Dict, Optional


class ApiResponse:
    def __init__(self, status_code: int, body: Optional[Dict[str, Any]]) -> None:
        self._status_code = status_code
        self._body = body if body is not None else {}

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def body(self) -> Dict[str, Any]:
        return self._body

    def get_code_string(self) -> Optional[str]:
        code = self._body.get("code")
        if code is None:
            return None
        return str(code)

    def get_message(self) -> Optional[str]:
        message = self._body.get("message")
        if message is None:
            return None
        return str(message)

    def is_success(self) -> bool:
        return 200 <= self._status_code < 300
