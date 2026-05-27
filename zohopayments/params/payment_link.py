from __future__ import annotations

from typing import Any, Dict, List, Optional

from zohopayments.params.common import (
    NotifyCustomerParams,
    ParamValidator,
    _require,
    _require_any_field,
)

class PaymentLinkConfigurationsParams:
    def __init__(
        self, *, allowed_payment_methods: Optional[List[str]] = None
    ) -> None:
        self._allowed_payment_methods = (
            list(allowed_payment_methods) if allowed_payment_methods else None
        )

    def to_dict(self) -> Dict[str, Any]:
        return {"allowed_payment_methods": self._allowed_payment_methods}


class PaymentLinkCreateParams:
    def __init__(
        self,
        *,
        amount: float,
        currency: str,
        description: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        phone_country_code: Optional[str] = None,
        expires_at: Optional[str] = None,
        reference_id: Optional[str] = None,
        return_url: Optional[str] = None,
        notify_customer: Optional[NotifyCustomerParams] = None,
        configurations: Optional[PaymentLinkConfigurationsParams] = None,
    ) -> None:
        _require(amount, "amount")
        _require(currency, "currency")
        _require(description, "description")
        ParamValidator.validate_description(description)
        ParamValidator.validate_reference_number(reference_id)

        self._amount = amount
        self._currency = currency
        self._description = description
        self._email = email
        self._phone = phone
        self._phone_country_code = phone_country_code
        self._expires_at = expires_at
        self._reference_id = reference_id
        self._return_url = return_url
        self._notify_customer = notify_customer
        self._configurations = configurations

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self._amount,
            "currency": self._currency,
            "description": self._description,
            "email": self._email,
            "phone": self._phone,
            "phone_country_code": self._phone_country_code,
            "expires_at": self._expires_at,
            "reference_id": self._reference_id,
            "return_url": self._return_url,
            "notify_customer": (
                self._notify_customer.to_dict()
                if self._notify_customer is not None
                else None
            ),
            "configurations": (
                self._configurations.to_dict()
                if self._configurations is not None
                else None
            ),
        }


class PaymentLinkUpdateParams:
    """All fields are optional, but at least one must be provided."""

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        phone_country_code: Optional[str] = None,
        expires_at: Optional[str] = None,
        reference_id: Optional[str] = None,
        return_url: Optional[str] = None,
        notify_customer: Optional[NotifyCustomerParams] = None,
        configurations: Optional[PaymentLinkConfigurationsParams] = None,
    ) -> None:
        _require_any_field(
            {
                "description": description,
                "email": email,
                "phone": phone,
                "phone_country_code": phone_country_code,
                "expires_at": expires_at,
                "reference_id": reference_id,
                "return_url": return_url,
                "notify_customer": notify_customer,
                "configurations": configurations,
            }
        )
        ParamValidator.validate_description(description)
        ParamValidator.validate_reference_number(reference_id)

        self._description = description
        self._email = email
        self._phone = phone
        self._phone_country_code = phone_country_code
        self._expires_at = expires_at
        self._reference_id = reference_id
        self._return_url = return_url
        self._notify_customer = notify_customer
        self._configurations = configurations

    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self._description,
            "email": self._email,
            "phone": self._phone,
            "phone_country_code": self._phone_country_code,
            "expires_at": self._expires_at,
            "reference_id": self._reference_id,
            "return_url": self._return_url,
            "notify_customer": (
                self._notify_customer.to_dict()
                if self._notify_customer is not None
                else None
            ),
            "configurations": (
                self._configurations.to_dict()
                if self._configurations is not None
                else None
            ),
        }
