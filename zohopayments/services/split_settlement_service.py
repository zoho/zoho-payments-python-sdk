"""Split Settlement service: Transfers (``/transfers``), Transfer Reversals
(``/transferreversals``), and Connected Accounts (``/connectedaccounts``).

Requires :attr:`Edition.IN`.
"""

from __future__ import annotations

from typing import Optional

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.list_response import ListResponse
from zohopayments.models.split_settlement import (
    ConnectedAccount,
    ConnectedAccountPayout,
    ConnectedAccountPayoutSummary,
    ConnectedAccountPayoutTransaction,
    ConnectedAccountSummary,
    ConnectedAccountTransaction,
    Transfer,
    TransferCreateResponse,
    TransferReversal,
    TransferReversalCreateResponse,
    TransferReversalDetail,
    TransferSummary,
)
from zohopayments.params.common import _require
from zohopayments.params.split_settlement import (
    ConnectedAccountCreateParams,
    ConnectedAccountListParams,
    ConnectedAccountTransactionListParams,
    TransferCreateParams,
    TransferListParams,
    TransferReversalCreateParams,
    TransferReversalListParams,
)
from zohopayments.services._query_builder import query_from


class SplitSettlementService:
    """Requires :attr:`Edition.IN`."""

    _TRANSFER_ENVELOPE = "transfer_details"
    _TRANSFER_LIST_ENVELOPE = "transfers"
    _TRANSFER_REVERSAL_ENVELOPE = "transfer_reversal_details"
    _TRANSFER_REVERSAL_LIST_ENVELOPE = "transfer_reversals"
    _CONNECTED_ACCOUNT_ENVELOPE = "connected_account"
    _CONNECTED_ACCOUNT_LIST_ENVELOPE = "connected_accounts"
    _PAYOUT_ENVELOPE = "payout"
    _PAYOUT_LIST_ENVELOPE = "payouts"
    _TRANSACTION_LIST_ENVELOPE = "transactions"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    # Transfers

    def create_transfer(self, params: TransferCreateParams) -> TransferCreateResponse:
        _require(params, "params")
        return self._http.post_object(
            "/transfers",
            params.to_dict(),
            TransferCreateResponse,
            "data",
            self._TRANSFER_LIST_ENVELOPE,
        )

    def get_transfer(self, transfer_id: str) -> Transfer:
        _require(transfer_id, "transfer_id")
        path = f"/transfers/{encode_path(transfer_id)}"
        return self._http.get_object(path, Transfer, self._TRANSFER_ENVELOPE)

    def list_transfers(
        self, params: Optional[TransferListParams] = None
    ) -> ListResponse[TransferSummary]:
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            "/transfers",
            query,
            TransferSummary.from_dict,
            self._TRANSFER_LIST_ENVELOPE,
        )

    def create_transfer_reversal(
        self, params: TransferReversalCreateParams
    ) -> TransferReversalCreateResponse:
        _require(params, "params")
        return self._http.post_object(
            "/transferreversals",
            params.to_dict(),
            TransferReversalCreateResponse,
            "data",
            "transfer_reversal",
        )

    def get_transfer_reversal(
        self, transfer_reversal_id: str
    ) -> TransferReversalDetail:
        _require(transfer_reversal_id, "transfer_reversal_id")
        path = f"/transferreversals/{encode_path(transfer_reversal_id)}"
        return self._http.get_object(
            path, TransferReversalDetail, self._TRANSFER_REVERSAL_ENVELOPE
        )

    def list_transfer_reversals(
        self, params: Optional[TransferReversalListParams] = None
    ) -> ListResponse[TransferReversal]:
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            "/transferreversals",
            query,
            TransferReversal.from_dict,
            self._TRANSFER_REVERSAL_LIST_ENVELOPE,
        )

    # Connected Accounts

    def create_connected_account(self, params: ConnectedAccountCreateParams) -> None:
        _require(params, "params")
        self._http.post("/connectedaccounts", params.to_dict())

    def list_connected_accounts(
        self, params: Optional[ConnectedAccountListParams] = None
    ) -> ListResponse[ConnectedAccountSummary]:
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            "/connectedaccounts",
            query,
            ConnectedAccountSummary.from_dict,
            self._CONNECTED_ACCOUNT_LIST_ENVELOPE,
        )

    def get_connected_account(self, connected_account_id: str) -> ConnectedAccount:
        _require(connected_account_id, "connected_account_id")
        path = f"/connectedaccounts/{encode_path(connected_account_id)}"
        return self._http.get_object(
            path, ConnectedAccount, self._CONNECTED_ACCOUNT_ENVELOPE
        )

    def list_connected_account_payouts(
        self, connected_account_id: str
    ) -> ListResponse[ConnectedAccountPayoutSummary]:
        _require(connected_account_id, "connected_account_id")
        path = f"/connectedaccounts/{encode_path(connected_account_id)}/payouts"
        return self._http.list_objects(
            path,
            None,
            ConnectedAccountPayoutSummary.from_dict,
            self._PAYOUT_LIST_ENVELOPE,
        )

    def get_connected_account_payout(
        self, connected_account_id: str, payout_id: str
    ) -> ConnectedAccountPayout:
        _require(connected_account_id, "connected_account_id")
        _require(payout_id, "payout_id")
        path = (
            f"/connectedaccounts/{encode_path(connected_account_id)}"
            f"/payouts/{encode_path(payout_id)}"
        )
        return self._http.get_object(
            path, ConnectedAccountPayout, self._PAYOUT_ENVELOPE
        )

    def list_connected_account_payout_transactions(
        self, connected_account_id: str, payout_id: str
    ) -> ListResponse[ConnectedAccountPayoutTransaction]:
        _require(connected_account_id, "connected_account_id")
        _require(payout_id, "payout_id")
        path = (
            f"/connectedaccounts/{encode_path(connected_account_id)}"
            f"/payouts/{encode_path(payout_id)}/transactions"
        )
        return self._http.list_objects(
            path,
            None,
            ConnectedAccountPayoutTransaction.from_dict,
            self._TRANSACTION_LIST_ENVELOPE,
        )

    def list_connected_account_transactions(
        self,
        connected_account_id: str,
        params: Optional[ConnectedAccountTransactionListParams] = None,
    ) -> ListResponse[ConnectedAccountTransaction]:
        _require(connected_account_id, "connected_account_id")
        path = f"/connectedaccounts/{encode_path(connected_account_id)}/transactions"
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            path,
            query,
            ConnectedAccountTransaction.from_dict,
            self._TRANSACTION_LIST_ENVELOPE,
        )