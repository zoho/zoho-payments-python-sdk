"""Payment link response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_int, opt_list, opt_obj, opt_str
from zohopayments.models.common import Configurations

@dataclass(frozen=True)
class PaymentLinkPayment:
    payment_id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    date: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentLinkPayment":
        return PaymentLinkPayment(
            payment_id=opt_str(data, "payment_id"),
            amount=opt_str(data, "amount"),
            type=opt_str(data, "type"),
            status=opt_str(data, "status"),
            date=opt_int(data, "date"),
        )


@dataclass(frozen=True)
class PaymentLink:
    payment_link_id: Optional[str] = None
    url: Optional[str] = None
    expires_at: Optional[str] = None
    amount: Optional[str] = None
    amount_paid: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    email: Optional[str] = None
    reference_id: Optional[str] = None
    description: Optional[str] = None
    return_url: Optional[str] = None
    phone: Optional[str] = None
    phone_country_code: Optional[str] = None
    created_time: Optional[int] = None
    created_by_id: Optional[str] = None
    created_by: Optional[str] = None
    last_modified_by_id: Optional[str] = None
    last_modified: Optional[str] = None
    configurations: Optional[Configurations] = None
    payments: List[PaymentLinkPayment] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentLink":
        return PaymentLink(
            payment_link_id=opt_str(data, "payment_link_id"),
            url=opt_str(data, "url"),
            expires_at=opt_str(data, "expires_at"),
            amount=opt_str(data, "amount"),
            amount_paid=opt_str(data, "amount_paid"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
            email=opt_str(data, "email"),
            reference_id=opt_str(data, "reference_id"),
            description=opt_str(data, "description"),
            return_url=opt_str(data, "return_url"),
            phone=opt_str(data, "phone"),
            phone_country_code=opt_str(data, "phone_country_code"),
            created_time=opt_int(data, "created_time"),
            created_by_id=opt_str(data, "created_by_id"),
            created_by=opt_str(data, "created_by"),
            last_modified_by_id=opt_str(data, "last_modified_by_id"),
            last_modified=opt_str(data, "last_modified"),
            configurations=opt_obj(data, "configurations", Configurations),
            payments=opt_list(data, "payments", PaymentLinkPayment.from_dict),
        )
