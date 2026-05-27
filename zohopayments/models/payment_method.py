from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from zohopayments.models._base import opt_int, opt_obj, opt_str

@dataclass(frozen=True)
class CardChecks:
    address_line_check: Optional[str] = None
    postal_code_check: Optional[str] = None
    cvc_check: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "CardChecks":
        return CardChecks(
            address_line_check=opt_str(data, "address_line_check"),
            postal_code_check=opt_str(data, "postal_code_check"),
            cvc_check=opt_str(data, "cvc_check"),
        )


@dataclass(frozen=True)
class SavedCardDetail:
    card_holder_name: Optional[str] = None
    last_four_digits: Optional[str] = None
    expiry_month: Optional[str] = None
    expiry_year: Optional[str] = None
    brand: Optional[str] = None
    funding: Optional[str] = None
    country: Optional[str] = None
    card_checks: Optional[CardChecks] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "SavedCardDetail":
        return SavedCardDetail(
            card_holder_name=opt_str(data, "card_holder_name"),
            last_four_digits=opt_str(data, "last_four_digits"),
            expiry_month=opt_str(data, "expiry_month"),
            expiry_year=opt_str(data, "expiry_year"),
            brand=opt_str(data, "brand"),
            funding=opt_str(data, "funding"),
            country=opt_str(data, "country"),
            card_checks=opt_obj(data, "card_checks", CardChecks),
        )


@dataclass(frozen=True)
class CardDetail:
    card_holder_name: Optional[str] = None
    last_four_digits: Optional[str] = None
    expiry_month: Optional[str] = None
    expiry_year: Optional[str] = None
    brand: Optional[str] = None
    funding: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "CardDetail":
        return CardDetail(
            card_holder_name=opt_str(data, "card_holder_name"),
            last_four_digits=opt_str(data, "last_four_digits"),
            expiry_month=opt_str(data, "expiry_month"),
            expiry_year=opt_str(data, "expiry_year"),
            brand=opt_str(data, "brand"),
            funding=opt_str(data, "funding"),
        )


@dataclass(frozen=True)
class AchDebitDetail:
    account_holder_name: Optional[str] = None
    last_four_digits: Optional[str] = None
    account_holder_type: Optional[str] = None
    account_type: Optional[str] = None
    bank_name: Optional[str] = None
    routing_number: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "AchDebitDetail":
        return AchDebitDetail(
            account_holder_name=opt_str(data, "account_holder_name"),
            last_four_digits=opt_str(data, "last_four_digits"),
            account_holder_type=opt_str(data, "account_holder_type"),
            account_type=opt_str(data, "account_type"),
            bank_name=opt_str(data, "bank_name"),
            routing_number=opt_str(data, "routing_number"),
        )


@dataclass(frozen=True)
class AddressDetail:
    name: Optional[str] = None
    address_id: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "AddressDetail":
        return AddressDetail(
            name=opt_str(data, "name"),
            address_id=opt_str(data, "address_id"),
            address_line1=opt_str(data, "address_line1"),
            address_line2=opt_str(data, "address_line2"),
            city=opt_str(data, "city"),
            state=opt_str(data, "state"),
            postal_code=opt_str(data, "postal_code"),
            country=opt_str(data, "country"),
        )


# IN-only nested payment-method details

@dataclass(frozen=True)
class Upi:
    upi_id: Optional[str] = None
    channel: Optional[str] = None
    account_type: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Upi":
        return Upi(
            upi_id=opt_str(data, "upi_id"),
            channel=opt_str(data, "channel"),
            account_type=opt_str(data, "account_type"),
        )


@dataclass(frozen=True)
class NetBanking:
    bank_name: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "NetBanking":
        return NetBanking(bank_name=opt_str(data, "bank_name"))


@dataclass(frozen=True)
class BankTransfer:
    virtual_account_number: Optional[str] = None
    mode: Optional[str] = None
    payer_name: Optional[str] = None
    payer_account_no: Optional[str] = None
    payer_ifsc_code: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "BankTransfer":
        return BankTransfer(
            virtual_account_number=opt_str(data, "virtual_account_number"),
            mode=opt_str(data, "mode"),
            payer_name=opt_str(data, "payer_name"),
            payer_account_no=opt_str(data, "payer_account_no"),
            payer_ifsc_code=opt_str(data, "payer_ifsc_code"),
        )


@dataclass(frozen=True)
class PaymentMethodDetail:
    """Payment method snapshot attached to payments, mandates, etc."""

    type: Optional[str] = None
    mandate_id: Optional[str] = None
    card: Optional[CardDetail] = None
    ach_debit: Optional[AchDebitDetail] = None
    upi: Optional[Upi] = None
    net_banking: Optional[NetBanking] = None
    bank_transfer: Optional[BankTransfer] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentMethodDetail":
        return PaymentMethodDetail(
            type=opt_str(data, "type"),
            mandate_id=opt_str(data, "mandate_id"),
            card=opt_obj(data, "card", CardDetail),
            ach_debit=opt_obj(data, "ach_debit", AchDebitDetail),
            upi=opt_obj(data, "upi", Upi),
            net_banking=opt_obj(data, "net_banking", NetBanking),
            bank_transfer=opt_obj(data, "bank_transfer", BankTransfer),
        )


# Saved payment method (/paymentmethods)


@dataclass(frozen=True)
class PaymentMethod:
    payment_method_id: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    currency: Optional[str] = None
    source: Optional[str] = None
    created_time: Optional[int] = None
    last_modified_time: Optional[int] = None
    card: Optional[SavedCardDetail] = None
    ach_debit: Optional[AchDebitDetail] = None
    billing_address: Optional[AddressDetail] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentMethod":
        return PaymentMethod(
            payment_method_id=opt_str(data, "payment_method_id"),
            customer_id=opt_str(data, "customer_id"),
            customer_name=opt_str(data, "customer_name"),
            customer_email=opt_str(data, "customer_email"),
            type=opt_str(data, "type"),
            status=opt_str(data, "status"),
            currency=opt_str(data, "currency"),
            source=opt_str(data, "source"),
            created_time=opt_int(data, "created_time"),
            last_modified_time=opt_int(data, "last_modified_time"),
            card=opt_obj(data, "card", SavedCardDetail),
            ach_debit=opt_obj(data, "ach_debit", AchDebitDetail),
            billing_address=opt_obj(data, "billing_address", AddressDetail),
        )


@dataclass(frozen=True)
class PaymentMethodSessionDetail:
    payment_method_id: Optional[str] = None
    status: Optional[str] = None
    created_time: Optional[int] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentMethodSessionDetail":
        return PaymentMethodSessionDetail(
            payment_method_id=opt_str(data, "payment_method_id"),
            status=opt_str(data, "status"),
            created_time=opt_int(data, "created_time"),
            type=opt_str(data, "type"),
        )


@dataclass(frozen=True)
class PaymentMethodSession:
    payment_method_session_id: Optional[str] = None
    customer_id: Optional[str] = None
    description: Optional[str] = None
    created_time: Optional[int] = None
    status: Optional[str] = None
    payment_method: Optional[PaymentMethodSessionDetail] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PaymentMethodSession":
        return PaymentMethodSession(
            payment_method_session_id=opt_str(data, "payment_method_session_id"),
            customer_id=opt_str(data, "customer_id"),
            description=opt_str(data, "description"),
            created_time=opt_int(data, "created_time"),
            status=opt_str(data, "status"),
            payment_method=opt_obj(
                data, "payment_method", PaymentMethodSessionDetail
            ),
        )
