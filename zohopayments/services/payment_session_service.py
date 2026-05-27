"""Payment sessions service."""

from __future__ import annotations

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.payment_session import PaymentSession
from zohopayments.params.payment_session import PaymentSessionCreateParams


class PaymentSessionService:
    _ENVELOPE = "payments_session"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def create(self, params: PaymentSessionCreateParams) -> PaymentSession:
        return self._http.post_object(
            "/paymentsessions", params.to_dict(), PaymentSession, self._ENVELOPE
        )

    def get(self, payment_session_id: str) -> PaymentSession:
        path = f"/paymentsessions/{encode_path(payment_session_id)}"
        return self._http.get_object(path, PaymentSession, self._ENVELOPE)
