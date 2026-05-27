"""Pagination metadata."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

@dataclass(frozen=True)
class PageContext:
    page: int = 0
    per_page: int = 0
    total: int = 0
    total_pages: int = 0
    has_more_page: bool = False

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PageContext":
        def _int(v: Any, default: int = 0) -> int:
            try:
                return int(v) if v is not None else default
            except (TypeError, ValueError):
                return default

        return PageContext(
            page=_int(data.get("page")),
            per_page=_int(data.get("per_page")),
            total=_int(data.get("total")),
            total_pages=_int(data.get("total_pages")),
            has_more_page=bool(data.get("has_more_page", False)),
        )
