from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class ParamValidator:
    MAX_DESCRIPTION_LENGTH = 500
    MAX_INVOICE_NUMBER_LENGTH = 50
    MAX_REFERENCE_LENGTH = 50

    @staticmethod
    def validate_description(description: Optional[str]) -> None:
        if description is None:
            return
        if len(description) > ParamValidator.MAX_DESCRIPTION_LENGTH:
            raise ValueError(
                f"description must be at most "
                f"{ParamValidator.MAX_DESCRIPTION_LENGTH} characters"
            )

    @staticmethod
    def validate_invoice_number(invoice_number: Optional[str]) -> None:
        if invoice_number is None:
            return
        if len(invoice_number) > ParamValidator.MAX_INVOICE_NUMBER_LENGTH:
            raise ValueError(
                f"invoice_number must be at most "
                f"{ParamValidator.MAX_INVOICE_NUMBER_LENGTH} characters"
            )

    @staticmethod
    def validate_reference_number(reference_number: Optional[str]) -> None:
        if reference_number is None:
            return
        if len(reference_number) > ParamValidator.MAX_REFERENCE_LENGTH:
            raise ValueError(
                f"reference number must be at most "
                f"{ParamValidator.MAX_REFERENCE_LENGTH} characters"
            )


class MetaDataValidator:
    MAX_ENTRIES = 5
    MAX_KEY_LENGTH = 20
    MAX_VALUE_LENGTH = 500

    @staticmethod
    def validate(meta_data: Optional[List["MetaDataParams"]]) -> None:
        if meta_data is None:
            return
        if len(meta_data) > MetaDataValidator.MAX_ENTRIES:
            raise ValueError(
                f"meta_data can have at most "
                f"{MetaDataValidator.MAX_ENTRIES} entries"
            )
        for entry in meta_data:
            if entry is None:
                raise ValueError("meta_data entry must not be null")
            key = entry.key
            value = entry.value
            if key is None or key == "":
                raise ValueError("meta_data key must not be null or empty")
            if len(key) > MetaDataValidator.MAX_KEY_LENGTH:
                raise ValueError(
                    f"meta_data key must be at most "
                    f"{MetaDataValidator.MAX_KEY_LENGTH} characters"
                )
            if value is not None and len(value) > MetaDataValidator.MAX_VALUE_LENGTH:
                raise ValueError(
                    f"meta_data value must be at most "
                    f"{MetaDataValidator.MAX_VALUE_LENGTH} characters"
                )



class MetaDataParams:
    """Immutable metadata key-value pair."""

    def __init__(self, key: str, value: Optional[str]) -> None:
        self._key = key
        self._value = value

    @property
    def key(self) -> str:
        return self._key

    @property
    def value(self) -> Optional[str]:
        return self._value

    def to_dict(self) -> Dict[str, Any]:
        return {"key": self._key, "value": self._value}


class PaginationParams(ABC):
    @abstractmethod
    def get_per_page(self) -> Optional[int]: ...

    @abstractmethod
    def get_page(self) -> Optional[int]: ...


class NotifyCustomerParams:
    def __init__(
        self, email: Optional[bool] = None, sms: Optional[bool] = None
    ) -> None:
        self._email = email
        self._sms = sms

    @property
    def email(self) -> Optional[bool]:
        return self._email

    @property
    def sms(self) -> Optional[bool]:
        return self._sms

    def to_dict(self) -> Dict[str, Any]:
        return {"email": self._email, "sms": self._sms}


class PostalAddressParams:
    """Postal address (``country`` is required)."""

    def __init__(
        self,
        *,
        country: str,
        name: Optional[str] = None,
        address_line1: Optional[str] = None,
        address_line2: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        postal_code: Optional[str] = None,
    ) -> None:
        if country is None or country == "":
            raise ValueError("country is required")
        self._country = country
        self._name = name
        self._address_line1 = address_line1
        self._address_line2 = address_line2
        self._city = city
        self._state = state
        self._postal_code = postal_code

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self._name,
            "address_line1": self._address_line1,
            "address_line2": self._address_line2,
            "city": self._city,
            "state": self._state,
            "country": self._country,
            "postal_code": self._postal_code,
        }


class HostedPageParams:
    """Hosted-page configuration. ``description``, ``success_url`` and
    ``failure_url`` are all required."""

    def __init__(
        self,
        *,
        description: str,
        success_url: str,
        failure_url: str,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        phone_country_code: Optional[str] = None,
        udf1: Optional[str] = None,
        udf2: Optional[str] = None,
        udf3: Optional[str] = None,
        udf4: Optional[str] = None,
        udf5: Optional[str] = None,
    ) -> None:
        if description is None or description == "":
            raise ValueError("description is required")
        if success_url is None or success_url == "":
            raise ValueError("success_url is required")
        if failure_url is None or failure_url == "":
            raise ValueError("failure_url is required")
        self._description = description
        self._success_url = success_url
        self._failure_url = failure_url
        self._name = name
        self._email = email
        self._phone = phone
        self._phone_country_code = phone_country_code
        self._udf1 = udf1
        self._udf2 = udf2
        self._udf3 = udf3
        self._udf4 = udf4
        self._udf5 = udf5

    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self._description,
            "success_url": self._success_url,
            "failure_url": self._failure_url,
            "name": self._name,
            "email": self._email,
            "phone": self._phone,
            "phone_country_code": self._phone_country_code,
            "udf1": self._udf1,
            "udf2": self._udf2,
            "udf3": self._udf3,
            "udf4": self._udf4,
            "udf5": self._udf5,
        }


class ConfigurationsParams:
    def __init__(
        self,
        *,
        allowed_payment_methods: Optional[List[str]] = None,
        hosted_page_parameters: Optional[HostedPageParams] = None,
    ) -> None:
        self._allowed_payment_methods = (
            list(allowed_payment_methods) if allowed_payment_methods else None
        )
        self._hosted_page_parameters = hosted_page_parameters

    def to_dict(self) -> Dict[str, Any]:
        return {
            "allowed_payment_methods": self._allowed_payment_methods,
            "hosted_page_parameters": (
                self._hosted_page_parameters.to_dict()
                if self._hosted_page_parameters is not None
                else None
            ),
        }



def _require(value: Any, name: str) -> None:
    """Raise ValueError if value is None or an empty string."""
    if value is None:
        raise ValueError(f"{name} is required")
    if isinstance(value, str) and value == "":
        raise ValueError(f"{name} must not be empty")


def _require_any_field(fields: Dict[str, Any]) -> None:
    """Raise ValueError if every field in ``fields`` is ``None``."""
    if all(v is None for v in fields.values()):
        raise ValueError("at least one field must be provided")


def _meta_data_to_list(
    meta_data: Optional[List[MetaDataParams]],
) -> Optional[List[Dict[str, Any]]]:
    if meta_data is None:
        return None
    return [m.to_dict() for m in meta_data]
