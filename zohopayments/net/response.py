from __future__ import annotations

from types import MappingProxyType
from typing import Dict, List, Mapping, Optional

class ZohoResponse:
    def __init__(
        self,
        status_code: int,
        headers: Dict[str, List[str]],
        body: Optional[str],
    ) -> None:
        self._status_code = status_code
        frozen: Dict[str, List[str]] = {}
        for k, v in headers.items():
            frozen[k] = tuple(v)  # type: ignore[assignment]
        self._headers: Mapping[str, List[str]] = MappingProxyType(frozen)  # type: ignore[arg-type]
        self._body = body

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def headers(self) -> Mapping[str, List[str]]:
        return self._headers

    @property
    def body(self) -> Optional[str]:
        return self._body
