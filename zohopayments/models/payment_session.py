"""Payment session response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_int, opt_list, opt_obj, opt_str
from zohopayments.models.common import Configurations, MetaData

@dataclass(frozen=True)
class PaymentSessionPayment:
    payment_id: Optional[str] = None
    status: Optional[str] = None
    created_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentSessionPayment":
        return PaymentSessionPayment(
            payment_id=opt_str(data, "payment_id"),
            status=opt_str(data, "status"),
            created_time=opt_int(data, "created_time"),
        )


@dataclass(frozen=True)
class PaymentSession:
    payments_session_id: Optional[str] = None
    access_key: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[str] = None
    status: Optional[str] = None
    created_time: Optional[int] = None
    expiry_time: Optional[int] = None
    payments: List[PaymentSessionPayment] = field(default_factory=list)
    meta_data: List[MetaData] = field(default_factory=list)
    description: Optional[str] = None
    invoice_number: Optional[str] = None
    reference_number: Optional[str] = None
    max_retry_count: Optional[int] = None
    configurations: Optional[Configurations] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentSession":
        return PaymentSession(
            payments_session_id=opt_str(data, "payments_session_id"),
            access_key=opt_str(data, "access_key"),
            currency=opt_str(data, "currency"),
            amount=opt_str(data, "amount"),
            status=opt_str(data, "status"),
            created_time=opt_int(data, "created_time"),
            expiry_time=opt_int(data, "expiry_time"),
            payments=opt_list(data, "payments", PaymentSessionPayment.from_dict),
            meta_data=opt_list(data, "meta_data", MetaData.from_dict),
            description=opt_str(data, "description"),
            invoice_number=opt_str(data, "invoice_number"),
            reference_number=opt_str(data, "reference_number"),
            max_retry_count=opt_int(data, "max_retry_count"),
            configurations=opt_obj(data, "configurations", Configurations),
        )
