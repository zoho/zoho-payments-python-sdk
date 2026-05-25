"""Customer response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_int, opt_list, opt_obj, opt_str
from zohopayments.models.common import MetaData

@dataclass(frozen=True)
class CustomerSummary:
    """Customer summary returned in list API responses (US only)."""

    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_status: Optional[str] = None
    created_time: Optional[int] = None
    last_modified_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "CustomerSummary":
        return CustomerSummary(
            customer_id=opt_str(data, "customer_id"),
            customer_name=opt_str(data, "customer_name"),
            customer_email=opt_str(data, "customer_email"),
            customer_phone=opt_str(data, "customer_phone"),
            customer_status=opt_str(data, "customer_status"),
            created_time=opt_int(data, "created_time"),
            last_modified_time=opt_int(data, "last_modified_time"),
        )


@dataclass(frozen=True)
class _CustomerCard:
    card_holder_name: Optional[str] = None
    last_four_digits: Optional[str] = None
    expiry_month: Optional[str] = None
    expiry_year: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "_CustomerCard":
        return _CustomerCard(
            card_holder_name=opt_str(data, "card_holder_name"),
            last_four_digits=opt_str(data, "last_four_digits"),
            expiry_month=opt_str(data, "expiry_month"),
            expiry_year=opt_str(data, "expiry_year"),
        )


@dataclass(frozen=True)
class _CustomerAchDebit:
    account_holder_name: Optional[str] = None
    last_four_digits: Optional[str] = None
    account_holder_type: Optional[str] = None
    account_type: Optional[str] = None
    bank_name: Optional[str] = None
    routing_number: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "_CustomerAchDebit":
        return _CustomerAchDebit(
            account_holder_name=opt_str(data, "account_holder_name"),
            last_four_digits=opt_str(data, "last_four_digits"),
            account_holder_type=opt_str(data, "account_holder_type"),
            account_type=opt_str(data, "account_type"),
            bank_name=opt_str(data, "bank_name"),
            routing_number=opt_str(data, "routing_number"),
        )


@dataclass(frozen=True)
class CustomerPaymentMethod:
    payment_method_id: Optional[str] = None
    type: Optional[str] = None
    brand: Optional[str] = None
    last_four_digits: Optional[str] = None
    expiry_month: Optional[str] = None
    expiry_year: Optional[str] = None
    card: Optional[_CustomerCard] = None
    ach_debit: Optional[_CustomerAchDebit] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "CustomerPaymentMethod":
        return CustomerPaymentMethod(
            payment_method_id=opt_str(data, "payment_method_id"),
            type=opt_str(data, "type"),
            brand=opt_str(data, "brand"),
            last_four_digits=opt_str(data, "last_four_digits"),
            expiry_month=opt_str(data, "expiry_month"),
            expiry_year=opt_str(data, "expiry_year"),
            card=opt_obj(data, "card", _CustomerCard),
            ach_debit=opt_obj(data, "ach_debit", _CustomerAchDebit),
        )


@dataclass(frozen=True)
class Customer:
    customer_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    dialing_code: Optional[str] = None
    created_time: Optional[int] = None
    last_modified_time: Optional[int] = None
    meta_data: List[MetaData] = field(default_factory=list)
    payment_methods: List[CustomerPaymentMethod] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Customer":
        return Customer(
            customer_id=opt_str(data, "customer_id"),
            name=opt_str(data, "name"),
            email=opt_str(data, "email"),
            phone=opt_str(data, "phone"),
            dialing_code=opt_str(data, "dialing_code"),
            created_time=opt_int(data, "created_time"),
            last_modified_time=opt_int(data, "last_modified_time"),
            meta_data=opt_list(data, "meta_data", MetaData.from_dict),
            payment_methods=opt_list(
                data, "payment_methods", CustomerPaymentMethod.from_dict
            ),
        )
