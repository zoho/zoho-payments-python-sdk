from __future__ import annotations

from typing import Generic, Iterator, List, TypeVar

from zohopayments.models.page_context import PageContext

T = TypeVar("T")

class ListResponse(Generic[T]):
    """Immutable paginated list response: items + page context."""

    def __init__(self, data: List[T], page_context: PageContext) -> None:
        self._data = tuple(data)
        self._page_context = page_context

    @property
    def data(self) -> List[T]:
        """Return a new list of items (immutable view)."""
        return list(self._data)

    @property
    def page_context(self) -> PageContext:
        return self._page_context

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)
