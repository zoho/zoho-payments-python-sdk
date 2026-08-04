"""Request/query parameters for the Split Settlement APIs: Transfers
(``/transfers``), Transfer Reversals (``/transferreversals``), and Connected
Accounts (``/connectedaccounts``)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from zohopayments.params.common import PaginationParams, ParamValidator, _require


class ConnectedAccountBankAccountParams:
    """Bank account details for the connected account being created."""

    def __init__(
        self,
        *,
        routing_number: str,
        account_number: str,
    ) -> None:
        _require(routing_number, "routing_number")
        _require(account_number, "account_number")

        self._routing_number = routing_number
        self._account_number = account_number

    def to_dict(self) -> Dict[str, Any]:
        return {
            "routing_number": self._routing_number,
            "account_number": self._account_number,
        }


class ConnectedAccountCreateParams:
    """Body for ``POST /connectedaccounts``."""

    def __init__(
        self,
        *,
        account_name: str,
        email_id: str,
        pan: str,
        mcc: str,
        business_description: str,
        connected_account_bank_account: ConnectedAccountBankAccountParams,
    ) -> None:
        _require(account_name, "account_name")
        _require(email_id, "email_id")
        _require(pan, "pan")
        _require(mcc, "mcc")
        _require(business_description, "business_description")
        _require(connected_account_bank_account, "connected_account_bank_account")

        self._account_name = account_name
        self._email_id = email_id
        self._pan = pan
        self._mcc = mcc
        self._business_description = business_description
        self._connected_account_bank_account = connected_account_bank_account

    def to_dict(self) -> Dict[str, Any]:
        return {
            "account_name": self._account_name,
            "email_id": self._email_id,
            "pan": self._pan,
            "mcc": self._mcc,
            "business_description": self._business_description,
            "connected_account_bank_account": (
                self._connected_account_bank_account.to_dict()
            ),
        }


class ConnectedAccountListParams(PaginationParams):
    """Query parameters for ``GET /connectedaccounts``."""

    def __init__(
        self,
        *,
        connected_account_id: Optional[str] = None,
        filter_by: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._connected_account_id = connected_account_id
        self._filter_by = filter_by
        self._from_date = from_date
        self._to_date = to_date
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "connected_account_id": self._connected_account_id,
            "filter_by": self._filter_by,
            "from_date": self._from_date,
            "to_date": self._to_date,
            "per_page": self._per_page,
            "page": self._page,
        }


class ConnectedAccountTransactionListParams(PaginationParams):
    """Query parameters for ``GET /connectedaccounts/{id}/transactions``."""

    def __init__(
        self,
        *,
        sort_column: Optional[str] = None,
        transaction_type: Optional[str] = None,
        transaction_id: Optional[str] = None,
        filter_by: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        payment_method_type: Optional[str] = None,
        card_brand: Optional[str] = None,
        card_type: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._sort_column = sort_column
        self._transaction_type = transaction_type
        self._transaction_id = transaction_id
        self._filter_by = filter_by
        self._from_date = from_date
        self._to_date = to_date
        self._payment_method_type = payment_method_type
        self._card_brand = card_brand
        self._card_type = card_type
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "sort_column": self._sort_column,
            "transaction_type": self._transaction_type,
            "transaction_id": self._transaction_id,
            "filter_by": self._filter_by,
            "from_date": self._from_date,
            "to_date": self._to_date,
            "payment_method_type": self._payment_method_type,
            "card_brand": self._card_brand,
            "card_type": self._card_type,
            "per_page": self._per_page,
            "page": self._page,
        }


class TransferSplitParams:
    """A single split entry within a transfer request."""

    def __init__(
        self,
        *,
        connected_account_id: str,
        amount: str,
        description: Optional[str] = None,
    ) -> None:
        _require(connected_account_id, "connected_account_id")
        _require(amount, "amount")
        ParamValidator.validate_description(description)

        self._connected_account_id = connected_account_id
        self._amount = amount
        self._description = description

    def to_dict(self) -> Dict[str, Any]:
        return {
            "connected_account_id": self._connected_account_id,
            "amount": self._amount,
            "description": self._description,
        }


class TransferCreateParams:
    """Body for ``POST /transfers``."""

    def __init__(
        self,
        *,
        payment_id: str,
        transfer_split: List[TransferSplitParams],
    ) -> None:
        _require(payment_id, "payment_id")
        if not transfer_split:
            raise ValueError("transfer_split is required")

        self._payment_id = payment_id
        self._transfer_split = list(transfer_split)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "payment_id": self._payment_id,
            "transfer_split": [s.to_dict() for s in self._transfer_split],
        }


class TransferListParams(PaginationParams):
    """Query parameters for ``GET /transfers``."""

    def __init__(
        self,
        *,
        status: Optional[str] = None,
        filter_by: Optional[str] = None,
        payment_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        sort_column: Optional[str] = None,
        sort_order: Optional[str] = None,
        search_text: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._status = status
        self._filter_by = filter_by
        self._payment_id = payment_id
        self._connected_account_id = connected_account_id
        self._from_date = from_date
        self._to_date = to_date
        self._sort_column = sort_column
        self._sort_order = sort_order
        self._search_text = search_text
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "status": self._status,
            "filter_by": self._filter_by,
            "payment_id": self._payment_id,
            "connected_account_id": self._connected_account_id,
            "from_date": self._from_date,
            "to_date": self._to_date,
            "sort_column": self._sort_column,
            "sort_order": self._sort_order,
            "search_text": self._search_text,
            "per_page": self._per_page,
            "page": self._page,
        }


class TransferReversalCreateParams:
    """Body for ``POST /transferreversals``."""

    def __init__(
        self,
        *,
        transfer_id: str,
        reversal_amount: str,
        description: Optional[str] = None,
    ) -> None:
        _require(transfer_id, "transfer_id")
        _require(reversal_amount, "reversal_amount")
        ParamValidator.validate_description(description)

        self._transfer_id = transfer_id
        self._reversal_amount = reversal_amount
        self._description = description

    def to_dict(self) -> Dict[str, Any]:
        return {
            "transfer_id": self._transfer_id,
            "reversal_amount": self._reversal_amount,
            "description": self._description,
        }


class TransferReversalListParams(PaginationParams):
    """Query parameters for ``GET /transferreversals``."""

    def __init__(
        self,
        *,
        status: Optional[str] = None,
        filter_by: Optional[str] = None,
        payment_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        transfer_id: Optional[str] = None,
        refund_id: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        sort_column: Optional[str] = None,
        sort_order: Optional[str] = None,
        search_text: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
    ) -> None:
        self._status = status
        self._filter_by = filter_by
        self._payment_id = payment_id
        self._connected_account_id = connected_account_id
        self._transfer_id = transfer_id
        self._refund_id = refund_id
        self._from_date = from_date
        self._to_date = to_date
        self._sort_column = sort_column
        self._sort_order = sort_order
        self._search_text = search_text
        self._per_page = per_page
        self._page = page

    def get_per_page(self) -> Optional[int]:
        return self._per_page

    def get_page(self) -> Optional[int]:
        return self._page

    def to_query(self) -> Dict[str, Any]:
        return {
            "status": self._status,
            "filter_by": self._filter_by,
            "payment_id": self._payment_id,
            "connected_account_id": self._connected_account_id,
            "transfer_id": self._transfer_id,
            "refund_id": self._refund_id,
            "from_date": self._from_date,
            "to_date": self._to_date,
            "sort_column": self._sort_column,
            "sort_order": self._sort_order,
            "search_text": self._search_text,
            "per_page": self._per_page,
            "page": self._page,
        }