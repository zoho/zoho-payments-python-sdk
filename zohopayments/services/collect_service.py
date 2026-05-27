"""Collect / virtual accounts service (IN only)."""

from __future__ import annotations

from typing import Optional

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.list_response import ListResponse
from zohopayments.models.virtual_account import (
    VirtualAccount,
    VirtualAccountPayment,
)
from zohopayments.params.virtual_account import (
    VirtualAccountCreateParams,
    VirtualAccountPaymentListParams,
    VirtualAccountUpdateParams,
)
from zohopayments.services._query_builder import query_from


class CollectService:
    """Requires :attr:`Edition.IN`."""

    _SINGLE_ENVELOPE = "virtual_account"
    _PAYMENTS_ENVELOPE = "payments"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def create(self, params: VirtualAccountCreateParams) -> VirtualAccount:
        return self._http.post_object(
            "/virtualaccounts", params.to_dict(), VirtualAccount, self._SINGLE_ENVELOPE
        )

    def update(
        self, virtual_account_id: str, params: VirtualAccountUpdateParams
    ) -> VirtualAccount:
        path = f"/virtualaccounts/{encode_path(virtual_account_id)}"
        return self._http.put_object(
            path, params.to_dict(), VirtualAccount, self._SINGLE_ENVELOPE
        )

    def get(self, virtual_account_id: str) -> VirtualAccount:
        path = f"/virtualaccounts/{encode_path(virtual_account_id)}"
        return self._http.get_object(path, VirtualAccount, self._SINGLE_ENVELOPE)

    def list_payments(
        self,
        virtual_account_id: str,
        params: Optional[VirtualAccountPaymentListParams] = None,
    ) -> ListResponse[VirtualAccountPayment]:
        path = f"/virtualaccounts/{encode_path(virtual_account_id)}/payments"
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            path,
            query,
            VirtualAccountPayment.from_dict,
            self._PAYMENTS_ENVELOPE,
        )

    def close(self, virtual_account_id: str) -> None:
        path = f"/virtualaccounts/{encode_path(virtual_account_id)}/close"
        self._http.put(path, None)
