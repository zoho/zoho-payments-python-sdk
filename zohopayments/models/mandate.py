from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from zohopayments.models._base import opt_int, opt_obj, opt_str

@dataclass(frozen=True)
class MandateUpi:
    upi_id: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "MandateUpi":
        return MandateUpi(upi_id=opt_str(data, "upi_id"))


@dataclass(frozen=True)
class MandatePaymentMethod:
    """Payment method on a mandate (UPI only)."""

    type: Optional[str] = None
    upi: Optional[MandateUpi] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "MandatePaymentMethod":
        return MandatePaymentMethod(
            type=opt_str(data, "type"),
            upi=opt_obj(data, "upi", MandateUpi),
        )


@dataclass(frozen=True)
class Mandate:
    mandate_id: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    amount_rule: Optional[str] = None
    frequency: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    debit_day: Optional[int] = None
    debit_rule: Optional[str] = None
    start_date: Optional[int] = None
    end_date: Optional[int] = None
    payment_method: Optional[MandatePaymentMethod] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Mandate":
        return Mandate(
            mandate_id=opt_str(data, "mandate_id"),
            customer_id=opt_str(data, "customer_id"),
            customer_name=opt_str(data, "customer_name"),
            customer_email=opt_str(data, "customer_email"),
            customer_phone=opt_str(data, "customer_phone"),
            amount=opt_str(data, "amount"),
            currency=opt_str(data, "currency"),
            amount_rule=opt_str(data, "amount_rule"),
            frequency=opt_str(data, "frequency"),
            status=opt_str(data, "status"),
            description=opt_str(data, "description"),
            debit_day=opt_int(data, "debit_day"),
            debit_rule=opt_str(data, "debit_rule"),
            start_date=opt_int(data, "start_date"),
            end_date=opt_int(data, "end_date"),
            payment_method=opt_obj(data, "payment_method", MandatePaymentMethod),
        )


@dataclass(frozen=True)
class MandateNotification:
    mandate_id: Optional[str] = None
    mandate_notification_id: Optional[str] = None
    customer_id: Optional[str] = None
    mandate_amount: Optional[str] = None
    currency: Optional[str] = None
    amount_rule: Optional[str] = None
    notification_amount: Optional[str] = None
    notification_status: Optional[str] = None
    description: Optional[str] = None
    invoice_number: Optional[str] = None
    amount: Optional[str] = None
    notification_date: Optional[int] = None
    execution_date: Optional[int] = None
    payment_method: Optional[MandatePaymentMethod] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "MandateNotification":
        return MandateNotification(
            mandate_id=opt_str(data, "mandate_id"),
            mandate_notification_id=opt_str(data, "mandate_notification_id"),
            customer_id=opt_str(data, "customer_id"),
            mandate_amount=opt_str(data, "mandate_amount"),
            currency=opt_str(data, "currency"),
            amount_rule=opt_str(data, "amount_rule"),
            notification_amount=opt_str(data, "notification_amount"),
            notification_status=opt_str(data, "notification_status"),
            description=opt_str(data, "description"),
            invoice_number=opt_str(data, "invoice_number"),
            amount=opt_str(data, "amount"),
            notification_date=opt_int(data, "notification_date"),
            execution_date=opt_int(data, "execution_date"),
            payment_method=opt_obj(data, "payment_method", MandatePaymentMethod),
        )


@dataclass(frozen=True)
class _MandatePaymentPaymentMethod:
    """Minimal {type} block on MandatePayment.payment_method."""

    type: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "_MandatePaymentPaymentMethod":
        return _MandatePaymentPaymentMethod(type=opt_str(data, "type"))


@dataclass(frozen=True)
class MandatePayment:
    payments_session_id: Optional[str] = None
    invoice_number: Optional[str] = None
    customer_id: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    statement_descriptor: Optional[str] = None
    description: Optional[str] = None
    reference_number: Optional[str] = None
    date: Optional[int] = None
    payment_method: Optional[_MandatePaymentPaymentMethod] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "MandatePayment":
        return MandatePayment(
            payments_session_id=opt_str(data, "payments_session_id"),
            invoice_number=opt_str(data, "invoice_number"),
            customer_id=opt_str(data, "customer_id"),
            amount=opt_str(data, "amount"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
            statement_descriptor=opt_str(data, "statement_descriptor"),
            description=opt_str(data, "description"),
            reference_number=opt_str(data, "reference_number"),
            date=opt_int(data, "date"),
            payment_method=opt_obj(
                data, "payment_method", _MandatePaymentPaymentMethod
            ),
        )
