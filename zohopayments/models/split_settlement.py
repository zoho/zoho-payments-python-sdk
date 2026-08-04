"""Split Settlement response models: Transfers, Transfer Reversals, and Connected Accounts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from zohopayments.models._base import opt_int, opt_list, opt_obj, opt_str


@dataclass(frozen=True)
class ConnectedAccountBankAccount:
    connected_account_bank_account_id: Optional[str] = None
    currency: Optional[str] = None
    routing_number: Optional[str] = None
    last_four_digits: Optional[str] = None
    created_by: Optional[str] = None
    last_modified_by: Optional[str] = None
    created_time: Optional[int] = None
    last_modified_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountBankAccount":
        return ConnectedAccountBankAccount(
            connected_account_bank_account_id=opt_str(
                data, "connected_account_bank_account_id"
            ),
            currency=opt_str(data, "currency"),
            routing_number=opt_str(data, "routing_number"),
            last_four_digits=opt_str(data, "last_four_digits"),
            created_by=opt_str(data, "created_by"),
            last_modified_by=opt_str(data, "last_modified_by"),
            created_time=opt_int(data, "created_time"),
            last_modified_time=opt_int(data, "last_modified_time"),
        )


@dataclass(frozen=True)
class ConnectedAccount:
    """A connected account resource returned by the Retrieve Connected Account API."""

    connected_account_id: Optional[str] = None
    email_id: Optional[str] = None
    account_name: Optional[str] = None
    pan: Optional[str] = None
    mcc: Optional[str] = None
    business_description: Optional[str] = None
    under_writing_status: Optional[str] = None
    transfer_status: Optional[str] = None
    payout_status: Optional[str] = None
    payout_delay_days: Optional[int] = None
    payout_statement_descriptor: Optional[str] = None
    statement_descriptor_restricted_chars: Optional[str] = None
    created_by: Optional[str] = None
    last_modified_by: Optional[str] = None
    created_time: Optional[int] = None
    last_modified_time: Optional[int] = None
    connected_account_bank_accounts: List[ConnectedAccountBankAccount] = field(
        default_factory=list
    )

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccount":
        return ConnectedAccount(
            connected_account_id=opt_str(data, "connected_account_id"),
            email_id=opt_str(data, "email_id"),
            account_name=opt_str(data, "account_name"),
            pan=opt_str(data, "pan"),
            mcc=opt_str(data, "mcc"),
            business_description=opt_str(data, "business_description"),
            under_writing_status=opt_str(data, "under_writing_status"),
            transfer_status=opt_str(data, "transfer_status"),
            payout_status=opt_str(data, "payout_status"),
            payout_delay_days=opt_int(data, "payout_delay_days"),
            payout_statement_descriptor=opt_str(
                data, "payout_statement_descriptor"
            ),
            statement_descriptor_restricted_chars=opt_str(
                data, "statement_descriptor_restricted_chars"
            ),
            created_by=opt_str(data, "created_by"),
            last_modified_by=opt_str(data, "last_modified_by"),
            created_time=opt_int(data, "created_time"),
            last_modified_time=opt_int(data, "last_modified_time"),
            connected_account_bank_accounts=opt_list(
                data,
                "connected_account_bank_accounts",
                ConnectedAccountBankAccount.from_dict,
            ),
        )


@dataclass(frozen=True)
class ConnectedAccountSummary:
    """A connected account summary returned by the List Connected Accounts API."""

    connected_account_id: Optional[str] = None
    account_name: Optional[str] = None
    email_id: Optional[str] = None
    under_writing_status: Optional[str] = None
    transfer_status: Optional[str] = None
    created_by: Optional[str] = None
    last_modified_by: Optional[str] = None
    created_time: Optional[int] = None
    last_modified_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountSummary":
        return ConnectedAccountSummary(
            connected_account_id=opt_str(data, "connected_account_id"),
            account_name=opt_str(data, "account_name"),
            email_id=opt_str(data, "email_id"),
            under_writing_status=opt_str(data, "under_writing_status"),
            transfer_status=opt_str(data, "transfer_status"),
            created_by=opt_str(data, "created_by"),
            last_modified_by=opt_str(data, "last_modified_by"),
            created_time=opt_int(data, "created_time"),
            last_modified_time=opt_int(data, "last_modified_time"),
        )


@dataclass(frozen=True)
class ConnectedAccountPayoutSummaryBankAccountDetails:
    bank_name: Optional[str] = None
    account_number_last_four_digits: Optional[str] = None

    @staticmethod
    def from_dict(
        data: Dict[str, Any]
    ) -> "ConnectedAccountPayoutSummaryBankAccountDetails":
        return ConnectedAccountPayoutSummaryBankAccountDetails(
            bank_name=opt_str(data, "bank_name"),
            account_number_last_four_digits=opt_str(
                data, "account_number_last_four_digits"
            ),
        )


@dataclass(frozen=True)
class ConnectedAccountPayoutSummary:
    """Payout summary."""

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
    bank_account_details: Optional[
        ConnectedAccountPayoutSummaryBankAccountDetails
    ] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountPayoutSummary":
        return ConnectedAccountPayoutSummary(
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
                data,
                "bank_account_details",
                ConnectedAccountPayoutSummaryBankAccountDetails,
            ),
        )


@dataclass(frozen=True)
class ConnectedAccountPayoutComment:
    """A comment entry on a connected account payout."""

    comment_id: Optional[str] = None
    amount: Optional[str] = None
    operation_type: Optional[str] = None
    action_type: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    created_by: Optional[str] = None
    created_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountPayoutComment":
        return ConnectedAccountPayoutComment(
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
class ConnectedAccountPayoutTransactionBreakdown:
    """Transaction breakdown by type (charge, refund, adjustment) within a payout."""

    transaction_type: Optional[str] = None
    count: Optional[int] = None
    net_amount: Optional[str] = None
    fee: Optional[str] = None
    amount: Optional[str] = None
    tax: Optional[str] = None

    @staticmethod
    def from_dict(
        data: Dict[str, Any]
    ) -> "ConnectedAccountPayoutTransactionBreakdown":
        return ConnectedAccountPayoutTransactionBreakdown(
            transaction_type=opt_str(data, "transaction_type"),
            count=opt_int(data, "count"),
            net_amount=opt_str(data, "net_amount"),
            fee=opt_str(data, "fee"),
            amount=opt_str(data, "amount"),
            tax=opt_str(data, "tax"),
        )


@dataclass(frozen=True)
class ConnectedAccountPayoutTransactionSummary:
    """Summary of transactions included in a connected account payout."""

    charge: Optional[ConnectedAccountPayoutTransactionBreakdown] = None
    refund: Optional[ConnectedAccountPayoutTransactionBreakdown] = None
    adjustment: Optional[ConnectedAccountPayoutTransactionBreakdown] = None
    total_amount: Optional[str] = None

    @staticmethod
    def from_dict(
        data: Dict[str, Any]
    ) -> "ConnectedAccountPayoutTransactionSummary":
        return ConnectedAccountPayoutTransactionSummary(
            charge=opt_obj(
                data, "charge", ConnectedAccountPayoutTransactionBreakdown
            ),
            refund=opt_obj(
                data, "refund", ConnectedAccountPayoutTransactionBreakdown
            ),
            adjustment=opt_obj(
                data, "adjustment", ConnectedAccountPayoutTransactionBreakdown
            ),
            total_amount=opt_str(data, "total_amount"),
        )


@dataclass(frozen=True)
class ConnectedAccountPayoutAccountDetails:
    """Bank account details for the connected account receiving the payout."""

    bank_name: Optional[str] = None
    account_number_last_four_digits: Optional[str] = None
    routing_number: Optional[str] = None
    type: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountPayoutAccountDetails":
        return ConnectedAccountPayoutAccountDetails(
            bank_name=opt_str(data, "bank_name"),
            account_number_last_four_digits=opt_str(
                data, "account_number_last_four_digits"
            ),
            routing_number=opt_str(data, "routing_number"),
            type=opt_str(data, "type"),
            country=opt_str(data, "country"),
            currency=opt_str(data, "currency"),
        )


@dataclass(frozen=True)
class ConnectedAccountPayout:
    """Payout detail."""

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
    comments: List[ConnectedAccountPayoutComment] = field(default_factory=list)
    transaction_summary: Optional[ConnectedAccountPayoutTransactionSummary] = None
    account_details: Optional[ConnectedAccountPayoutAccountDetails] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountPayout":
        return ConnectedAccountPayout(
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
            comments=opt_list(
                data, "comments", ConnectedAccountPayoutComment.from_dict
            ),
            transaction_summary=opt_obj(
                data,
                "transaction_summary",
                ConnectedAccountPayoutTransactionSummary,
            ),
            account_details=opt_obj(
                data, "account_details", ConnectedAccountPayoutAccountDetails
            ),
        )


@dataclass(frozen=True)
class ConnectedAccountPayoutTransaction:
    """A transaction entry returned by the List Payout Transactions API."""

    payout_id: Optional[str] = None
    merchant_transaction_id: Optional[str] = None
    transaction_id: Optional[str] = None
    parent_transaction_id: Optional[str] = None
    transaction_type: Optional[str] = None
    transaction_time: Optional[int] = None
    net_amount: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    description: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountPayoutTransaction":
        return ConnectedAccountPayoutTransaction(
            payout_id=opt_str(data, "payout_id"),
            merchant_transaction_id=opt_str(data, "merchant_transaction_id"),
            transaction_id=opt_str(data, "transaction_id"),
            parent_transaction_id=opt_str(data, "parent_transaction_id"),
            transaction_type=opt_str(data, "transaction_type"),
            transaction_time=opt_int(data, "transaction_time"),
            net_amount=opt_str(data, "net_amount"),
            amount=opt_str(data, "amount"),
            currency=opt_str(data, "currency"),
            customer_id=opt_str(data, "customer_id"),
            customer_name=opt_str(data, "customer_name"),
            description=opt_str(data, "description"),
        )


@dataclass(frozen=True)
class ConnectedAccountTransaction:
    """A transaction entry returned by the List Connected Account Transactions API."""

    transaction_id: Optional[str] = None
    parent_transaction_id: Optional[str] = None
    transaction_type: Optional[str] = None
    transaction_time: Optional[int] = None
    net_amount: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    available_on: Optional[int] = None
    settled_time: Optional[int] = None
    payment_method: Optional[str] = None
    card_brand: Optional[str] = None
    card_type: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    description: Optional[str] = None
    refund_reason: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectedAccountTransaction":
        return ConnectedAccountTransaction(
            transaction_id=opt_str(data, "transaction_id"),
            parent_transaction_id=opt_str(data, "parent_transaction_id"),
            transaction_type=opt_str(data, "transaction_type"),
            transaction_time=opt_int(data, "transaction_time"),
            net_amount=opt_str(data, "net_amount"),
            amount=opt_str(data, "amount"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
            available_on=opt_int(data, "available_on"),
            settled_time=opt_int(data, "settled_time"),
            payment_method=opt_str(data, "payment_method"),
            card_brand=opt_str(data, "card_brand"),
            card_type=opt_str(data, "card_type"),
            customer_id=opt_str(data, "customer_id"),
            customer_name=opt_str(data, "customer_name"),
            description=opt_str(data, "description"),
            refund_reason=opt_str(data, "refund_reason"),
        )


@dataclass(frozen=True)
class TransferReversalEntry:
    """An inline reversal entry embedded in a transfer detail response."""

    reversal_id: Optional[str] = None
    total_amount: Optional[str] = None
    net_amount: Optional[str] = None
    fee_amount: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    created_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferReversalEntry":
        return TransferReversalEntry(
            reversal_id=opt_str(data, "reversal_id"),
            total_amount=opt_str(data, "total_amount"),
            net_amount=opt_str(data, "net_amount"),
            fee_amount=opt_str(data, "fee_amount"),
            description=opt_str(data, "description"),
            status=opt_str(data, "status"),
            created_time=opt_int(data, "created_time"),
        )


@dataclass(frozen=True)
class TransferPaymentDetails:
    """Payment details nested in a transfer detail response."""

    amount: Optional[str] = None
    amount_formatted: Optional[str] = None
    currency: Optional[str] = None
    payment_date_formatted: Optional[str] = None
    status_formatted: Optional[str] = None
    payment_date: Optional[int] = None
    status: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferPaymentDetails":
        return TransferPaymentDetails(
            amount=opt_str(data, "amount"),
            amount_formatted=opt_str(data, "amount_formatted"),
            currency=opt_str(data, "currency"),
            payment_date_formatted=opt_str(data, "payment_date_formatted"),
            status_formatted=opt_str(data, "status_formatted"),
            payment_date=opt_int(data, "payment_date"),
            status=opt_str(data, "status"),
        )


@dataclass(frozen=True)
class Transfer:
    """Transfer detail."""

    transfer_id: Optional[str] = None
    payment_id: Optional[str] = None
    total_amount: Optional[str] = None
    net_amount: Optional[str] = None
    fee_amount: Optional[str] = None
    fee_rate: Optional[str] = None
    fee_tax_amount: Optional[str] = None
    fee_tax_rate: Optional[str] = None
    connected_account_id: Optional[str] = None
    connected_account_name: Optional[str] = None
    description: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    failure_code: Optional[str] = None
    reversed_amount: Optional[str] = None
    available_amount_for_reversal: Optional[str] = None
    created_time: Optional[int] = None
    reversals: List[TransferReversalEntry] = field(default_factory=list)
    payment_details: Optional[TransferPaymentDetails] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Transfer":
        return Transfer(
            transfer_id=opt_str(data, "transfer_id"),
            payment_id=opt_str(data, "payment_id"),
            total_amount=opt_str(data, "total_amount"),
            net_amount=opt_str(data, "net_amount"),
            fee_amount=opt_str(data, "fee_amount"),
            fee_rate=opt_str(data, "fee_rate"),
            fee_tax_amount=opt_str(data, "fee_tax_amount"),
            fee_tax_rate=opt_str(data, "fee_tax_rate"),
            connected_account_id=opt_str(data, "connected_account_id"),
            connected_account_name=opt_str(data, "connected_account_name"),
            description=opt_str(data, "description"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
            failure_code=opt_str(data, "failure_code"),
            reversed_amount=opt_str(data, "reversed_amount"),
            available_amount_for_reversal=opt_str(
                data, "available_amount_for_reversal"
            ),
            created_time=opt_int(data, "created_time"),
            reversals=opt_list(data, "reversals", TransferReversalEntry.from_dict),
            payment_details=opt_obj(
                data, "payment_details", TransferPaymentDetails
            ),
        )


@dataclass(frozen=True)
class TransferSummary:
    """Transfer summary."""

    transfer_id: Optional[str] = None
    payment_id: Optional[str] = None
    total_amount: Optional[str] = None
    net_amount: Optional[str] = None
    fee_amount: Optional[str] = None
    fee_rate: Optional[str] = None
    fee_tax_amount: Optional[str] = None
    connected_account_id: Optional[str] = None
    connected_account_name: Optional[str] = None
    description: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    failure_code: Optional[str] = None
    reversed_amount: Optional[str] = None
    created_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferSummary":
        return TransferSummary(
            transfer_id=opt_str(data, "transfer_id"),
            payment_id=opt_str(data, "payment_id"),
            total_amount=opt_str(data, "total_amount"),
            net_amount=opt_str(data, "net_amount"),
            fee_amount=opt_str(data, "fee_amount"),
            fee_rate=opt_str(data, "fee_rate"),
            fee_tax_amount=opt_str(data, "fee_tax_amount"),
            connected_account_id=opt_str(data, "connected_account_id"),
            connected_account_name=opt_str(data, "connected_account_name"),
            description=opt_str(data, "description"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
            failure_code=opt_str(data, "failure_code"),
            reversed_amount=opt_str(data, "reversed_amount"),
            created_time=opt_int(data, "created_time"),
        )


@dataclass(frozen=True)
class TransferSplitResult:
    """A single split result within the create-transfer response."""

    transfer_id: Optional[str] = None
    connected_account_id: Optional[str] = None
    currency: Optional[str] = None
    transfer_amount: Optional[str] = None
    net_transfer_amount: Optional[str] = None
    fee_amount: Optional[str] = None
    fee_tax_amount: Optional[str] = None
    status: Optional[str] = None
    error_code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferSplitResult":
        return TransferSplitResult(
            transfer_id=opt_str(data, "transfer_id"),
            connected_account_id=opt_str(data, "connected_account_id"),
            currency=opt_str(data, "currency"),
            transfer_amount=opt_str(data, "transfer_amount"),
            net_transfer_amount=opt_str(data, "net_transfer_amount"),
            fee_amount=opt_str(data, "fee_amount"),
            fee_tax_amount=opt_str(data, "fee_tax_amount"),
            status=opt_str(data, "status"),
            error_code=opt_str(data, "error_code"),
            message=opt_str(data, "message"),
        )


@dataclass(frozen=True)
class TransferCreateResponse:
    """Create Transfer response."""

    splits: List[TransferSplitResult] = field(default_factory=list)
    status: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferCreateResponse":
        return TransferCreateResponse(
            splits=opt_list(data, "splits", TransferSplitResult.from_dict),
            status=opt_str(data, "status"),
        )


@dataclass(frozen=True)
class TransferReversal:
    """Transfer reversal details."""

    transfer_reversal_id: Optional[str] = None
    currency: Optional[str] = None
    total_amount: Optional[str] = None
    connected_account_id: Optional[str] = None
    connected_account_name: Optional[str] = None
    status: Optional[str] = None
    failure_code: Optional[str] = None
    created_time: Optional[int] = None
    transfer_id: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferReversal":
        return TransferReversal(
            transfer_reversal_id=opt_str(data, "transfer_reversal_id"),
            currency=opt_str(data, "currency"),
            total_amount=opt_str(data, "total_amount"),
            connected_account_id=opt_str(data, "connected_account_id"),
            connected_account_name=opt_str(data, "connected_account_name"),
            status=opt_str(data, "status"),
            failure_code=opt_str(data, "failure_code"),
            created_time=opt_int(data, "created_time"),
            transfer_id=opt_str(data, "transfer_id"),
        )


@dataclass(frozen=True)
class TransferReversalDetail:
    """Transfer reversal detail returned by the Retrieve Transfer Reversal API."""

    transfer_reversal_id: Optional[str] = None
    transfer_id: Optional[str] = None
    payment_id: Optional[str] = None
    refund_id: Optional[str] = None
    total_amount: Optional[str] = None
    connected_account_id: Optional[str] = None
    connected_account_name: Optional[str] = None
    status: Optional[str] = None
    failure_code: Optional[str] = None
    description: Optional[str] = None
    currency: Optional[str] = None
    created_time: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferReversalDetail":
        return TransferReversalDetail(
            transfer_reversal_id=opt_str(data, "transfer_reversal_id"),
            transfer_id=opt_str(data, "transfer_id"),
            payment_id=opt_str(data, "payment_id"),
            refund_id=opt_str(data, "refund_id"),
            total_amount=opt_str(data, "total_amount"),
            connected_account_id=opt_str(data, "connected_account_id"),
            connected_account_name=opt_str(data, "connected_account_name"),
            status=opt_str(data, "status"),
            failure_code=opt_str(data, "failure_code"),
            description=opt_str(data, "description"),
            currency=opt_str(data, "currency"),
            created_time=opt_int(data, "created_time"),
        )


@dataclass(frozen=True)
class TransferReversalCreateResponse:
    """Create transfer reversal response."""

    transfer_reversal_id: Optional[str] = None
    transfer_id: Optional[str] = None
    transfer_reversal_amount: Optional[str] = None
    connected_account_id: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TransferReversalCreateResponse":
        return TransferReversalCreateResponse(
            transfer_reversal_id=opt_str(data, "transfer_reversal_id"),
            transfer_id=opt_str(data, "transfer_id"),
            transfer_reversal_amount=opt_str(data, "transfer_reversal_amount"),
            connected_account_id=opt_str(data, "connected_account_id"),
            currency=opt_str(data, "currency"),
            status=opt_str(data, "status"),
        )
