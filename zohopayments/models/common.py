"""Response models shared across multiple resources."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_bool, opt_obj, opt_str, opt_str_list

@dataclass(frozen=True)
class MetaData:
    key: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "MetaData":
        return MetaData(key=opt_str(data, "key"), value=opt_str(data, "value"))


@dataclass(frozen=True)
class NotifyCustomer:
    email: Optional[bool] = None
    sms: Optional[bool] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "NotifyCustomer":
        return NotifyCustomer(
            email=opt_bool(data, "email"),
            sms=opt_bool(data, "sms"),
        )


@dataclass(frozen=True)
class HostedPageResponse:
    description: Optional[str] = None
    success_url: Optional[str] = None
    failure_url: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    phone_country_code: Optional[str] = None
    udf1: Optional[str] = None
    udf2: Optional[str] = None
    udf3: Optional[str] = None
    udf4: Optional[str] = None
    udf5: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "HostedPageResponse":
        return HostedPageResponse(
            description=opt_str(data, "description"),
            success_url=opt_str(data, "success_url"),
            failure_url=opt_str(data, "failure_url"),
            name=opt_str(data, "name"),
            email=opt_str(data, "email"),
            phone=opt_str(data, "phone"),
            phone_country_code=opt_str(data, "phone_country_code"),
            udf1=opt_str(data, "udf1"),
            udf2=opt_str(data, "udf2"),
            udf3=opt_str(data, "udf3"),
            udf4=opt_str(data, "udf4"),
            udf5=opt_str(data, "udf5"),
        )


@dataclass(frozen=True)
class Configurations:
    allowed_payment_methods: List[str] = field(default_factory=list)
    hosted_page_parameters: Optional[HostedPageResponse] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Configurations":
        return Configurations(
            allowed_payment_methods=opt_str_list(data, "allowed_payment_methods"),
            hosted_page_parameters=opt_obj(
                data, "hosted_page_parameters", HostedPageResponse
            ),
        )
