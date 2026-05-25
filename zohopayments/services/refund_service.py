"""Refunds service."""

from __future__ import annotations

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.refund import Refund
from zohopayments.params.refund import RefundCreateParams


class RefundService:
    _ENVELOPE = "refund"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def create(self, payment_id: str, params: RefundCreateParams) -> Refund:
        path = f"/payments/{encode_path(payment_id)}/refunds"
        return self._http.post_object(
            path, params.to_dict(), Refund, self._ENVELOPE
        )

    def get(self, refund_id: str) -> Refund:
        path = f"/refunds/{encode_path(refund_id)}"
        return self._http.get_object(path, Refund, self._ENVELOPE)
