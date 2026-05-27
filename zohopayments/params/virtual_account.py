from __future__ import annotations

from typing import Any, Dict, List, Optional

from zohopayments.params.common import (
    MetaDataParams,
    MetaDataValidator,
    PaginationParams,
    ParamValidator,
    _meta_data_to_list,
    _require,
    _require_any_field,
)


class VirtualAccountCreateParams:
    def __init__(
        self,
        *,
        description: str,
        customer_id: Optional[str] = None,
        minimum_amount: Optional[float] = None,
        maximum_amount: Optional[float] = None,
        expires_at: Optional[str] = None,
        reference_number: Optional[str] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
    ) -> None:
        _require(description, "description")
        ParamValidator.validate_description(description)
        ParamValidator.validate_reference_number(reference_number)
        MetaDataValidator.validate(meta_data)

        self._description = description
        self._customer_id = customer_id
        self._minimum_amount = minimum_amount
        self._maximum_amount = maximum_amount
        self._expires_at = expires_at
        self._reference_number = reference_number
        self._meta_data = meta_data

    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self._description,
            "customer_id": self._customer_id,
            "minimum_amount": self._minimum_amount,
            "maximum_amount": self._maximum_amount,
            "expires_at": self._expires_at,
            "reference_number": self._reference_number,
            "meta_data": _meta_data_to_list(self._meta_data),
        }


class VirtualAccountUpdateParams:
    """All fields are optional, but at least one must be provided."""

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        minimum_amount: Optional[float] = None,
        maximum_amount: Optional[float] = None,
        expires_at: Optional[str] = None,
        reference_number: Optional[str] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
    ) -> None:
        _require_any_field(
            {
                "description": description,
                "minimum_amount": minimum_amount,
                "maximum_amount": maximum_amount,
                "expires_at": expires_at,
                "reference_number": reference_number,
                "meta_data": meta_data,
            }
        )
        ParamValidator.validate_description(description)
        ParamValidator.validate_reference_number(reference_number)
        MetaDataValidator.validate(meta_data)

        self._description = description
        self._minimum_amount = minimum_amount
        self._maximum_amount = maximum_amount
        self._expires_at = expires_at
        self._reference_number = reference_number
        self._meta_data = meta_data

    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self._description,
            "minimum_amount": self._minimum_amount,
            "maximum_amount": self._maximum_amount,
            "expires_at": self._expires_at,
            "reference_number": self._reference_number,
            "meta_data": _meta_data_to_list(self._meta_data),
        }


class VirtualAccountPaymentListParams(PaginationParams):
    def __init__(
        self,
        *,
        status: Optional[str] = None,
        sort_column: Optional[str] = None,
        sort_order: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._status = status
        self._sort_column = sort_column
        self._sort_order = sort_order
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "status": self._status,
            "sort_column": self._sort_column,
            "sort_order": self._sort_order,
            "per_page": self._per_page,
            "page": self._page,
        }
