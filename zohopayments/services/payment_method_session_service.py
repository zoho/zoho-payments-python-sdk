"""Payment method sessions service (US only)."""

from __future__ import annotations

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.payment_method import PaymentMethodSession
from zohopayments.params.payment_method import PaymentMethodSessionCreateParams


class PaymentMethodSessionService:
    """Requires :attr:`Edition.US`."""

    _ENVELOPE = "payment_method_session"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def create(
        self, params: PaymentMethodSessionCreateParams
    ) -> PaymentMethodSession:
        return self._http.post_object(
            "/paymentmethodsessions",
            params.to_dict(),
            PaymentMethodSession,
            self._ENVELOPE,
        )

    def get(self, payment_method_session_id: str) -> PaymentMethodSession:
        path = f"/paymentmethodsessions/{encode_path(payment_method_session_id)}"
        return self._http.get_object(path, PaymentMethodSession, self._ENVELOPE)
