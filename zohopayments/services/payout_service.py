"""Payouts service (``/payouts``). Available on all editions."""

from __future__ import annotations

from typing import Optional

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.list_response import ListResponse
from zohopayments.models.payout import Payout, PayoutDetail, PayoutTransaction
from zohopayments.params.common import _require
from zohopayments.params.payout import PayoutListParams, PayoutTransactionListParams
from zohopayments.services._query_builder import query_from


class PayoutService:
    _SINGLE_ENVELOPE = "payout"
    _LIST_ENVELOPE = "payouts"
    _TRANSACTION_LIST_ENVELOPE = "transactions"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def get(self, payout_id: str) -> PayoutDetail:
        _require(payout_id, "payout_id")
        path = f"/payouts/{encode_path(payout_id)}"
        return self._http.get_object(path, PayoutDetail, self._SINGLE_ENVELOPE)

    def list(self, params: Optional[PayoutListParams] = None) -> ListResponse[Payout]:
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            "/payouts", query, Payout.from_dict, self._LIST_ENVELOPE
        )

    def list_transactions(
        self,
        payout_id: str,
        params: Optional[PayoutTransactionListParams] = None,
    ) -> ListResponse[PayoutTransaction]:
        _require(payout_id, "payout_id")
        path = f"/payouts/{encode_path(payout_id)}/transactions"
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            path,
            query,
            PayoutTransaction.from_dict,
            self._TRANSACTION_LIST_ENVELOPE,
        )