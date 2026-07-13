"""Query parameters for the Payouts API (``/payouts``)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from zohopayments.params.common import PaginationParams


class PayoutListParams(PaginationParams):
    def __init__(
        self,
        *,
        status: Optional[str] = None,
        filter_by: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._status = status
        self._filter_by = filter_by
        self._from_date = from_date
        self._to_date = to_date
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "status": self._status,
            "filter_by": self._filter_by,
            "from_date": self._from_date,
            "to_date": self._to_date,
            "per_page": self._per_page,
            "page": self._page,
        }


class PayoutTransactionListParams(PaginationParams):
    def __init__(
        self,
        *,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "per_page": self._per_page,
            "page": self._page,
        }