"""Payments service."""

from __future__ import annotations

from typing import Optional

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.edition import Edition
from zohopayments.models.list_response import ListResponse
from zohopayments.models.payment import Payment, PaymentSummary
from zohopayments.params.payment import PaymentCreateParams, PaymentListParams
from zohopayments.services._query_builder import query_from


class PaymentService:
    _SINGLE_ENVELOPE = "payment"
    _LIST_ENVELOPE = "payments"

    def __init__(self, http: ZohoHttpClient, edition: Edition) -> None:
        self._http = http
        self._edition = edition

    def create(self, params: PaymentCreateParams) -> Payment:
        if not self._edition.is_us():
            raise NotImplementedError(
                "payments.create() is available only on Edition.US"
            )
        return self._http.post_object(
            "/payments", params.to_dict(), Payment, self._SINGLE_ENVELOPE
        )

    def get(self, payment_id: str) -> Payment:
        path = f"/payments/{encode_path(payment_id)}"
        return self._http.get_object(path, Payment, self._SINGLE_ENVELOPE)

    def list(
        self, params: Optional[PaymentListParams] = None
    ) -> ListResponse[PaymentSummary]:
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            "/payments",
            query,
            PaymentSummary.from_dict,
            self._LIST_ENVELOPE,
        )
