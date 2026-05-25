"""URL query-string builder."""

from __future__ import annotations

from typing import List, Optional, Tuple, Union
from urllib.parse import quote

class QueryParams:
    """Ordered, URL-encoded, repeat-tolerant query string builder.

    ``None`` values are silently dropped. Booleans are lowercased.
    """

    def __init__(self) -> None:
        self._entries: List[Tuple[str, str]] = []

    def add(
        self,
        key: str,
        value: Union[str, int, float, bool, None],
    ) -> "QueryParams":
        if value is None:
            return self
        if isinstance(value, bool):
            self._entries.append((key, "true" if value else "false"))
        else:
            self._entries.append((key, str(value)))
        return self

    def add_all(self, other: Optional["QueryParams"]) -> "QueryParams":
        if other is not None:
            self._entries.extend(other._entries)
        return self

    def is_empty(self) -> bool:
        return not self._entries

    def to_query_string(self) -> str:
        return "&".join(
            f"{quote(k, safe='')}={quote(v, safe='')}" for k, v in self._entries
        )
