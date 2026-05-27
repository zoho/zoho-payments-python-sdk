"""Virtual account (Collect) response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_float, opt_int, opt_list, opt_obj, opt_str
from zohopayments.models.common import MetaData

@dataclass(frozen=True)
class _VirtualAccountPaymentMethod:
    payment_method_id: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "_VirtualAccountPaymentMethod":
        return _VirtualAccountPaymentMethod(
            payment_method_id=opt_str(data, "payment_method_id"),
            type=opt_str(data, "type"),
        )


@dataclass(frozen=True)
class VirtualAccount:
    virtual_account_id: Optional[str] = None
    account_number: Optional[str] = None
    ifsc_code: Optional[str] = None
    beneficiary_name: Optional[str] = None
    description: Optional[str] = None
    customer_id: Optional[str] = None
    reference_number: Optional[str] = None
    status: Optional[str] = None
    expires_at: Optional[str] = None
    created_time: Optional[int] = None
    last_modified_time: Optional[int] = None
    meta_data: List[MetaData] = field(default_factory=list)
    minimum_amount: Optional[float] = None
    maximum_amount: Optional[float] = None
    amount_paid: Optional[float] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "VirtualAccount":
        return VirtualAccount(
            virtual_account_id=opt_str(data, "virtual_account_id"),
            account_number=opt_str(data, "account_number"),
            ifsc_code=opt_str(data, "ifsc_code"),
            beneficiary_name=opt_str(data, "beneficiary_name"),
            description=opt_str(data, "description"),
            customer_id=opt_str(data, "customer_id"),
            reference_number=opt_str(data, "reference_number"),
            status=opt_str(data, "status"),
            expires_at=opt_str(data, "expires_at"),
            created_time=opt_int(data, "created_time"),
            last_modified_time=opt_int(data, "last_modified_time"),
            meta_data=opt_list(data, "meta_data", MetaData.from_dict),
            minimum_amount=opt_float(data, "minimum_amount"),
            maximum_amount=opt_float(data, "maximum_amount"),
            amount_paid=opt_float(data, "amount_paid"),
        )


@dataclass(frozen=True)
class VirtualAccountPayment:
    payment_id: Optional[str] = None
    customer_id: Optional[str] = None
    virtual_account_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    amount: Optional[str] = None
    receipt_email: Optional[str] = None
    dialing_code: Optional[str] = None
    phone: Optional[str] = None
    reference_number: Optional[str] = None
    transaction_reference_number: Optional[str] = None
    payment_type: Optional[str] = None
    currency: Optional[str] = None
    balance: Optional[str] = None
    amount_captured: Optional[str] = None
    amount_refunded: Optional[str] = None
    fee_amount: Optional[str] = None
    status: Optional[str] = None
    transaction_type: Optional[str] = None
    fraud_alert: Optional[str] = None
    failure_reason: Optional[str] = None
    failure_category: Optional[str] = None
    next_action: Optional[str] = None
    tip: Optional[str] = None
    date: Optional[int] = None
    payment_method: Optional[_VirtualAccountPaymentMethod] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "VirtualAccountPayment":
        return VirtualAccountPayment(
            payment_id=opt_str(data, "payment_id"),
            customer_id=opt_str(data, "customer_id"),
            virtual_account_id=opt_str(data, "virtual_account_id"),
            customer_name=opt_str(data, "customer_name"),
            customer_email=opt_str(data, "customer_email"),
            amount=opt_str(data, "amount"),
            receipt_email=opt_str(data, "receipt_email"),
            dialing_code=opt_str(data, "dialing_code"),
            phone=opt_str(data, "phone"),
            reference_number=opt_str(data, "reference_number"),
            transaction_reference_number=opt_str(
                data, "transaction_reference_number"
            ),
            payment_type=opt_str(data, "payment_type"),
            currency=opt_str(data, "currency"),
            balance=opt_str(data, "balance"),
            amount_captured=opt_str(data, "amount_captured"),
            amount_refunded=opt_str(data, "amount_refunded"),
            fee_amount=opt_str(data, "fee_amount"),
            status=opt_str(data, "status"),
            transaction_type=opt_str(data, "transaction_type"),
            fraud_alert=opt_str(data, "fraud_alert"),
            failure_reason=opt_str(data, "failure_reason"),
            failure_category=opt_str(data, "failure_category"),
            next_action=opt_str(data, "next_action"),
            tip=opt_str(data, "tip"),
            date=opt_int(data, "date"),
            payment_method=opt_obj(
                data, "payment_method", _VirtualAccountPaymentMethod
            ),
        )
