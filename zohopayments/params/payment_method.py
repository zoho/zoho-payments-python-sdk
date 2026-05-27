"""Payment method request params (US edition)."""

from __future__ import annotations
from typing import Any, Dict, Optional

from zohopayments.params.common import (
    ParamValidator,
    PostalAddressParams,
    _require,
)

class CardUpdate:
    def __init__(
        self,
        *,
        expiry_month: Optional[str] = None,
        expiry_year: Optional[str] = None,
    ) -> None:
        self._expiry_month = expiry_month
        self._expiry_year = expiry_year

    def to_dict(self) -> Dict[str, Any]:
        return {
            "expiry_month": self._expiry_month,
            "expiry_year": self._expiry_year,
        }


class AchDebitUpdate:
    def __init__(self, *, account_holder_type: Optional[str] = None) -> None:
        self._account_holder_type = account_holder_type

    def to_dict(self) -> Dict[str, Any]:
        return {"account_holder_type": self._account_holder_type}


class PaymentMethodUpdateParams:
    def __init__(
        self,
        *,
        type: str,
        card: Optional[CardUpdate] = None,
        ach_debit: Optional[AchDebitUpdate] = None,
        billing_address: Optional[PostalAddressParams] = None,
    ) -> None:
        _require(type, "type")
        self._type = type
        self._card = card
        self._ach_debit = ach_debit
        self._billing_address = billing_address

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self._type,
            "card": self._card.to_dict() if self._card is not None else None,
            "ach_debit": (
                self._ach_debit.to_dict() if self._ach_debit is not None else None
            ),
            "billing_address": (
                self._billing_address.to_dict()
                if self._billing_address is not None
                else None
            ),
        }


class PaymentMethodSessionCreateParams:
    def __init__(
        self, *, customer_id: str, description: Optional[str] = None
    ) -> None:
        _require(customer_id, "customer_id")
        ParamValidator.validate_description(description)

        self._customer_id = customer_id
        self._description = description

    def to_dict(self) -> Dict[str, Any]:
        return {
            "customer_id": self._customer_id,
            "description": self._description,
        }
