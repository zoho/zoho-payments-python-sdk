"""Payment methods service (US only)."""

from __future__ import annotations

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.payment_method import PaymentMethod
from zohopayments.params.payment_method import PaymentMethodUpdateParams


class PaymentMethodService:
    """Requires :attr:`Edition.US`."""

    _ENVELOPE = "payment_method"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def get(self, payment_method_id: str) -> PaymentMethod:
        path = f"/paymentmethods/{encode_path(payment_method_id)}"
        return self._http.get_object(path, PaymentMethod, self._ENVELOPE)

    def update(
        self, payment_method_id: str, params: PaymentMethodUpdateParams
    ) -> PaymentMethod:
        path = f"/paymentmethods/{encode_path(payment_method_id)}"
        return self._http.put_object(
            path, params.to_dict(), PaymentMethod, self._ENVELOPE
        )

    def delete(self, payment_method_id: str) -> None:
        path = f"/paymentmethods/{encode_path(payment_method_id)}"
        self._http.delete(path)
