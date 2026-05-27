from __future__ import annotations

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.payment_link import PaymentLink
from zohopayments.params.payment_link import (
    PaymentLinkCreateParams,
    PaymentLinkUpdateParams,
)

class PaymentLinkService:
    _ENVELOPE = "payment_links"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def create(self, params: PaymentLinkCreateParams) -> PaymentLink:
        return self._http.post_object(
            "/paymentlinks", params.to_dict(), PaymentLink, self._ENVELOPE
        )

    def get(self, payment_link_id: str) -> PaymentLink:
        path = f"/paymentlinks/{encode_path(payment_link_id)}"
        return self._http.get_object(path, PaymentLink, self._ENVELOPE)

    def update(
        self, payment_link_id: str, params: PaymentLinkUpdateParams
    ) -> PaymentLink:
        path = f"/paymentlinks/{encode_path(payment_link_id)}"
        return self._http.put_object(
            path, params.to_dict(), PaymentLink, self._ENVELOPE
        )

    def cancel(self, payment_link_id: str) -> PaymentLink:
        path = f"/paymentlinks/{encode_path(payment_link_id)}/cancel"
        return self._http.put_object(path, None, PaymentLink, self._ENVELOPE)
