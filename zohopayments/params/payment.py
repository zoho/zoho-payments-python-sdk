"""Payment request params (US edition)."""

from __future__ import annotations
from typing import Any, Dict, List, Optional

from zohopayments.params.common import (
    MetaDataParams,
    MetaDataValidator,
    PaginationParams,
    ParamValidator,
    PostalAddressParams,
    _meta_data_to_list,
    _require,
)

class BrowserInfo:
    """Browser metadata for 3DS / customer-on-session flows."""

    def __init__(
        self,
        *,
        user_agent: Optional[str] = None,
        accept_header: Optional[str] = None,
        screen_height: Optional[int] = None,
        screen_width: Optional[int] = None,
        language: Optional[str] = None,
        time_zone_offset: Optional[int] = None,
        color_depth: Optional[int] = None,
    ) -> None:
        self._user_agent = user_agent
        self._accept_header = accept_header
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._language = language
        self._time_zone_offset = time_zone_offset
        self._color_depth = color_depth

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_agent": self._user_agent,
            "accept_header": self._accept_header,
            "screen_height": self._screen_height,
            "screen_width": self._screen_width,
            "language": self._language,
            "time_zone_offset": self._time_zone_offset,
            "color_depth": self._color_depth,
        }


class PaymentCreateParams:
    def __init__(
        self,
        *,
        customer_id: str,
        payment_method_id: str,
        amount: float,
        currency: str,
        customer_on_session: Optional[bool] = None,
        browser_info: Optional[BrowserInfo] = None,
        statement_descriptor: Optional[str] = None,
        description: Optional[str] = None,
        shipping_address: Optional[PostalAddressParams] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
    ) -> None:
        _require(customer_id, "customer_id")
        _require(payment_method_id, "payment_method_id")
        _require(amount, "amount")
        _require(currency, "currency")
        ParamValidator.validate_description(description)
        MetaDataValidator.validate(meta_data)

        self._customer_id = customer_id
        self._payment_method_id = payment_method_id
        self._amount = amount
        self._currency = currency
        self._customer_on_session = customer_on_session
        self._browser_info = browser_info
        self._statement_descriptor = statement_descriptor
        self._description = description
        self._shipping_address = shipping_address
        self._meta_data = meta_data

    def to_dict(self) -> Dict[str, Any]:
        return {
            "customer_id": self._customer_id,
            "payment_method_id": self._payment_method_id,
            "amount": self._amount,
            "currency": self._currency,
            "customer_on_session": self._customer_on_session,
            "browser_info": (
                self._browser_info.to_dict()
                if self._browser_info is not None
                else None
            ),
            "statement_descriptor": self._statement_descriptor,
            "description": self._description,
            "shipping_address": (
                self._shipping_address.to_dict()
                if self._shipping_address is not None
                else None
            ),
            "meta_data": _meta_data_to_list(self._meta_data),
        }


class PaymentListParams(PaginationParams):
    def __init__(
        self,
        *,
        status: Optional[str] = None,
        search_text: Optional[str] = None,
        filter_by: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        payment_method_type: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._status = status
        self._search_text = search_text
        self._filter_by = filter_by
        self._from_date = from_date
        self._to_date = to_date
        self._payment_method_type = payment_method_type
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "status": self._status,
            "search_text": self._search_text,
            "filter_by": self._filter_by,
            "from_date": self._from_date,
            "to_date": self._to_date,
            "payment_method_type": self._payment_method_type,
            "per_page": self._per_page,
            "page": self._page,
        }
