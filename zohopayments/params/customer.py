"""Customer request params."""

from __future__ import annotations
from typing import Any, Dict, List, Optional

from zohopayments.params.common import (
    MetaDataParams,
    MetaDataValidator,
    PaginationParams,
    _meta_data_to_list,
    _require,
)

class CustomerCreateParams:
    def __init__(
        self,
        *,
        name: str,
        email: str,
        phone: Optional[str] = None,
        phone_country_code: Optional[str] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
    ) -> None:
        _require(name, "name")
        _require(email, "email")
        MetaDataValidator.validate(meta_data)

        self._name = name
        self._email = email
        self._phone = phone
        self._phone_country_code = phone_country_code
        self._meta_data = meta_data

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self._name,
            "email": self._email,
            "phone": self._phone,
            "phone_country_code": self._phone_country_code,
            "meta_data": _meta_data_to_list(self._meta_data),
        }


class CustomerListParams(PaginationParams):
    def __init__(
        self,
        *,
        filter_by: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
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
            "filter_by": self._filter_by,
            "from_date": self._from_date,
            "to_date": self._to_date,
            "per_page": self._per_page,
            "page": self._page,
        }
