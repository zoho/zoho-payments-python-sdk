"""Payout response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_int, opt_list, opt_obj, opt_str


@dataclass(frozen=True)
class PayoutBankAccountDetails:
    bank_name: Optional[str] = None
    account_number_last_four_digits: Optional[str] = None
    account_holder_name: Optional[str] = None
    routing_number: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PayoutBankAccountDetails":
        return PayoutBankAccountDetails(
            bank_name=opt_str(data, "bank_name"),
            account_number_last_four_digits=opt_str(
                data, "account_number_last_four_digits"
            ),
            account_holder_name=opt_str(data, "account_holder_name"),
            routing_number=opt_str(data, "routing_number"),
        )


@dataclass(frozen=True)
class Payout:
    payout_id: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    failure_code: Optional[str] = None
    failure_message: Optional[str] = None
    statement_descriptor: Optional[str] = None
    payout_method: Optional[str] = None
    initiated_time: Optional[int] = None
    arrival_date: Optional[str] = None
    processed_date: Optional[str] = None
    type: Optional[str] = None
    payout_bank_reference_id: Optional[str] = None
    bank_account_details: Optional[PayoutBankAccountDetails] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Payout":
        return Payout(
            payout_id=opt_str(data, "payout_id"),
            amount=opt_str(data, "amount"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
            failure_code=opt_str(data, "failure_code"),
            failure_message=opt_str(data, "failure_message"),
            statement_descriptor=opt_str(data, "statement_descriptor"),
            payout_method=opt_str(data, "payout_method"),
            initiated_time=opt_int(data, "initiated_time"),
            arrival_date=opt_str(data, "arrival_date"),
            processed_date=opt_str(data, "processed_date"),
            type=opt_str(data, "type"),
            payout_bank_reference_id=opt_str(data, "payout_bank_reference_id"),
            bank_account_details=opt_obj(
                data, "bank_account_details", PayoutBankAccountDetails
            ),
        )


@dataclass(frozen=True)
class PayoutTypeSummary:
    transaction_type: Optional[str] = None
    transaction_type_formatted: Optional[str] = None
    count: Optional[int] = None
    net_amount: Optional[str] = None
    net_amount_formatted: Optional[str] = None
    fee: Optional[str] = None
    fee_formatted: Optional[str] = None
    amount: Optional[str] = None
    amount_formatted: Optional[str] = None
    tax: Optional[str] = None
    tax_formatted: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PayoutTypeSummary":
        return PayoutTypeSummary(
            transaction_type=opt_str(data, "transaction_type"),
            transaction_type_formatted=opt_str(data, "transaction_type_formatted"),
            count=opt_int(data, "count"),
            net_amount=opt_str(data, "net_amount"),
            net_amount_formatted=opt_str(data, "net_amount_formatted"),
            fee=opt_str(data, "fee"),
            fee_formatted=opt_str(data, "fee_formatted"),
            amount=opt_str(data, "amount"),
            amount_formatted=opt_str(data, "amount_formatted"),
            tax=opt_str(data, "tax"),
            tax_formatted=opt_str(data, "tax_formatted"),
        )


@dataclass(frozen=True)
class PayoutTransactionSummary:
    charge: Optional[PayoutTypeSummary] = None
    refund: Optional[PayoutTypeSummary] = None
    adjustment: Optional[PayoutTypeSummary] = None
    total_amount: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PayoutTransactionSummary":
        return PayoutTransactionSummary(
            charge=opt_obj(data, "charge", PayoutTypeSummary),
            refund=opt_obj(data, "refund", PayoutTypeSummary),
            adjustment=opt_obj(data, "adjustment", PayoutTypeSummary),
            total_amount=opt_str(data, "total_amount"),
        )


@dataclass(frozen=True)
class PayoutAccountDetails:
    bank_name: Optional[str] = None
    account_holder: Optional[str] = None
    account_number_last_four_digits: Optional[str] = None
    routing_number: Optional[str] = None
    type: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PayoutAccountDetails":
        return PayoutAccountDetails(
            bank_name=opt_str(data, "bank_name"),
            account_holder=opt_str(data, "account_holder"),
            account_number_last_four_digits=opt_str(
                data, "account_number_last_four_digits"
            ),
            routing_number=opt_str(data, "routing_number"),
            type=opt_str(data, "type"),
            country=opt_str(data, "country"),
            currency=opt_str(data, "currency"),
        )


@dataclass(frozen=True)
class PayoutComment:
    comment_id: Optional[str] = None
    amount: Optional[str] = None
    operation_type: Optional[str] = None
    action_type: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    created_by: Optional[str] = None
    created_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PayoutComment":
        return PayoutComment(
            comment_id=opt_str(data, "comment_id"),
            amount=opt_str(data, "amount"),
            operation_type=opt_str(data, "operation_type"),
            action_type=opt_str(data, "action_type"),
            type=opt_str(data, "type"),
            description=opt_str(data, "description"),
            created_by=opt_str(data, "created_by"),
            created_time=opt_int(data, "created_time"),
        )


@dataclass(frozen=True)
class PayoutDetail:
    payout_id: Optional[str] = None
    amount: Optional[str] = None
    processing_fee: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    failure_code: Optional[str] = None
    failure_message: Optional[str] = None
    statement_descriptor: Optional[str] = None
    payout_method: Optional[str] = None
    initiated_time: Optional[int] = None
    arrival_date: Optional[str] = None
    processed_date: Optional[str] = None
    type: Optional[str] = None
    fee: Optional[str] = None
    fee_rate: Optional[str] = None
    fixed_fee: Optional[str] = None
    tax_amount: Optional[str] = None
    tax_rate: Optional[str] = None
    payout_bank_reference_id: Optional[str] = None
    comments: List[PayoutComment] = field(default_factory=list)
    transaction_summary: Optional[PayoutTransactionSummary] = None
    account_details: Optional[PayoutAccountDetails] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PayoutDetail":
        return PayoutDetail(
            payout_id=opt_str(data, "payout_id"),
            amount=opt_str(data, "amount"),
            processing_fee=opt_str(data, "processing_fee"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
            failure_code=opt_str(data, "failure_code"),
            failure_message=opt_str(data, "failure_message"),
            statement_descriptor=opt_str(data, "statement_descriptor"),
            payout_method=opt_str(data, "payout_method"),
            initiated_time=opt_int(data, "initiated_time"),
            arrival_date=opt_str(data, "arrival_date"),
            processed_date=opt_str(data, "processed_date"),
            type=opt_str(data, "type"),
            fee=opt_str(data, "fee"),
            fee_rate=opt_str(data, "fee_rate"),
            fixed_fee=opt_str(data, "fixed_fee"),
            tax_amount=opt_str(data, "tax_amount"),
            tax_rate=opt_str(data, "tax_rate"),
            payout_bank_reference_id=opt_str(data, "payout_bank_reference_id"),
            comments=opt_list(data, "comments", PayoutComment.from_dict),
            transaction_summary=opt_obj(
                data, "transaction_summary", PayoutTransactionSummary
            ),
            account_details=opt_obj(data, "account_details", PayoutAccountDetails),
        )


@dataclass(frozen=True)
class PayoutTransaction:
    payout_id: Optional[str] = None
    transaction_id: Optional[str] = None
    parent_transaction_id: Optional[str] = None
    net_amount: Optional[str] = None
    amount: Optional[str] = None
    fee: Optional[str] = None
    tax: Optional[str] = None
    transaction_type: Optional[str] = None
    transaction_time: Optional[int] = None
    currency: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    description: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "PayoutTransaction":
        return PayoutTransaction(
            payout_id=opt_str(data, "payout_id"),
            transaction_id=opt_str(data, "transaction_id"),
            parent_transaction_id=opt_str(data, "parent_transaction_id"),
            net_amount=opt_str(data, "net_amount"),
            amount=opt_str(data, "amount"),
            fee=opt_str(data, "fee"),
            tax=opt_str(data, "tax"),
            transaction_type=opt_str(data, "transaction_type"),
            transaction_time=opt_int(data, "transaction_time"),
            currency=opt_str(data, "currency"),
            customer_id=opt_str(data, "customer_id"),
            customer_name=opt_str(data, "customer_name"),
            description=opt_str(data, "description"),
        )
