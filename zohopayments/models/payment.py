"""Payment response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_float, opt_int, opt_list, opt_obj, opt_str
from zohopayments.models.common import MetaData
from zohopayments.models.payment_method import PaymentMethodDetail

@dataclass(frozen=True)
class _PaymentMethodSummary:
    """Minimal {payment_method_id, type} block used in list responses."""

    payment_method_id: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "_PaymentMethodSummary":
        return _PaymentMethodSummary(
            payment_method_id=opt_str(data, "payment_method_id"),
            type=opt_str(data, "type"),
        )


@dataclass(frozen=True)
class PaymentSummary:
    payment_id: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    receipt_email: Optional[str] = None
    reference_number: Optional[str] = None
    amount_captured: Optional[str] = None
    amount_refunded: Optional[str] = None
    fee_amount: Optional[str] = None
    net_amount: Optional[str] = None
    status: Optional[str] = None
    date: Optional[int] = None
    payment_method: Optional[_PaymentMethodSummary] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentSummary":
        return PaymentSummary(
            payment_id=opt_str(data, "payment_id"),
            amount=opt_str(data, "amount"),
            currency=opt_str(data, "currency"),
            receipt_email=opt_str(data, "receipt_email"),
            reference_number=opt_str(data, "reference_number"),
            amount_captured=opt_str(data, "amount_captured"),
            amount_refunded=opt_str(data, "amount_refunded"),
            fee_amount=opt_str(data, "fee_amount"),
            net_amount=opt_str(data, "net_amount"),
            status=opt_str(data, "status"),
            date=opt_int(data, "date"),
            payment_method=opt_obj(data, "payment_method", _PaymentMethodSummary),
        )


@dataclass(frozen=True)
class Payment:
    payment_id: Optional[str] = None
    phone: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    payments_session_id: Optional[str] = None
    receipt_email: Optional[str] = None
    reference_number: Optional[str] = None
    transaction_reference_number: Optional[str] = None
    invoice_number: Optional[str] = None
    amount_captured: Optional[str] = None
    amount_refunded: Optional[str] = None
    fee_amount: Optional[str] = None
    net_tax_amount: Optional[str] = None
    total_fee_amount: Optional[str] = None
    net_amount: Optional[str] = None
    status: Optional[str] = None
    exchange_rate: Optional[float] = None
    statement_descriptor: Optional[str] = None
    description: Optional[str] = None
    date: Optional[int] = None
    payment_method: Optional[PaymentMethodDetail] = None
    meta_data: List[MetaData] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Payment":
        return Payment(
            payment_id=opt_str(data, "payment_id"),
            phone=opt_str(data, "phone"),
            amount=opt_str(data, "amount"),
            currency=opt_str(data, "currency"),
            payments_session_id=opt_str(data, "payments_session_id"),
            receipt_email=opt_str(data, "receipt_email"),
            reference_number=opt_str(data, "reference_number"),
            transaction_reference_number=opt_str(
                data, "transaction_reference_number"
            ),
            invoice_number=opt_str(data, "invoice_number"),
            amount_captured=opt_str(data, "amount_captured"),
            amount_refunded=opt_str(data, "amount_refunded"),
            fee_amount=opt_str(data, "fee_amount"),
            net_tax_amount=opt_str(data, "net_tax_amount"),
            total_fee_amount=opt_str(data, "total_fee_amount"),
            net_amount=opt_str(data, "net_amount"),
            status=opt_str(data, "status"),
            exchange_rate=opt_float(data, "exchange_rate"),
            statement_descriptor=opt_str(data, "statement_descriptor"),
            description=opt_str(data, "description"),
            date=opt_int(data, "date"),
            payment_method=opt_obj(data, "payment_method", PaymentMethodDetail),
            meta_data=opt_list(data, "meta_data", MetaData.from_dict),
        )
