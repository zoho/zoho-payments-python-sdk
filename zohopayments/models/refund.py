"""Refund response model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_int, opt_list, opt_str
from zohopayments.models.common import MetaData

@dataclass(frozen=True)
class Refund:
    refund_id: Optional[str] = None
    payment_id: Optional[str] = None
    reference_number: Optional[str] = None
    amount: Optional[str] = None
    default_currency_amount: Optional[str] = None
    type: Optional[str] = None
    reason: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    network_reference_number: Optional[str] = None
    failure_reason: Optional[str] = None
    date: Optional[int] = None
    meta_data: List[MetaData] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Refund":
        return Refund(
            refund_id=opt_str(data, "refund_id"),
            payment_id=opt_str(data, "payment_id"),
            reference_number=opt_str(data, "reference_number"),
            amount=opt_str(data, "amount"),
            default_currency_amount=opt_str(data, "default_currency_amount"),
            type=opt_str(data, "type"),
            reason=opt_str(data, "reason"),
            description=opt_str(data, "description"),
            status=opt_str(data, "status"),
            network_reference_number=opt_str(data, "network_reference_number"),
            failure_reason=opt_str(data, "failure_reason"),
            date=opt_int(data, "date"),
            meta_data=opt_list(data, "meta_data", MetaData.from_dict),
        )
