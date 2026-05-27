"""Payment session request params."""

from __future__ import annotations
from typing import Any, Dict, List, Optional

from zohopayments.params.common import (
    ConfigurationsParams,
    MetaDataParams,
    MetaDataValidator,
    ParamValidator,
    _meta_data_to_list,
    _require,
)

class PaymentSessionCreateParams:
    def __init__(
        self,
        *,
        amount: float,
        currency: str,
        description: str,
        expires_in: Optional[int] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
        invoice_number: Optional[str] = None,
        reference_number: Optional[str] = None,
        max_retry_count: Optional[int] = None,
        configurations: Optional[ConfigurationsParams] = None,
    ) -> None:
        _require(amount, "amount")
        _require(currency, "currency")
        _require(description, "description")
        if expires_in is not None and not (300 <= expires_in <= 900):
            raise ValueError("expires_in must be between 300 and 900 seconds")
        if max_retry_count is not None and not (1 <= max_retry_count <= 5):
            raise ValueError("max_retry_count must be between 1 and 5")
        ParamValidator.validate_description(description)
        ParamValidator.validate_invoice_number(invoice_number)
        ParamValidator.validate_reference_number(reference_number)
        MetaDataValidator.validate(meta_data)

        self._amount = amount
        self._currency = currency
        self._description = description
        self._expires_in = expires_in
        self._meta_data = meta_data
        self._invoice_number = invoice_number
        self._reference_number = reference_number
        self._max_retry_count = max_retry_count
        self._configurations = configurations

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self._amount,
            "currency": self._currency,
            "description": self._description,
            "expires_in": self._expires_in,
            "meta_data": _meta_data_to_list(self._meta_data),
            "invoice_number": self._invoice_number,
            "reference_number": self._reference_number,
            "max_retry_count": self._max_retry_count,
            "configurations": (
                self._configurations.to_dict()
                if self._configurations is not None
                else None
            ),
        }
