"""Mandate service (IN only)."""

from __future__ import annotations

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.models.mandate import Mandate, MandateNotification, MandatePayment
from zohopayments.models.payment_session import PaymentSession
from zohopayments.params.mandate import (
    MandateEnrollmentSessionCreateParams,
    MandateExecuteParams,
    MandateExecutionSessionCreateParams,
    MandateNotifyParams,
)


class MandateService:
    """Requires :attr:`Edition.IN`."""

    _SESSION_ENVELOPE = "payments_session"
    _NOTIFICATION_ENVELOPE = "mandate_notification"
    _PAYMENT_ENVELOPE = "payment"
    _MANDATE_ENVELOPE = "mandate"

    def __init__(self, http: ZohoHttpClient) -> None:
        self._http = http

    def create_enrollment_session(
        self, params: MandateEnrollmentSessionCreateParams
    ) -> PaymentSession:
        return self._http.post_object(
            "/paymentsessions",
            params.to_dict(),
            PaymentSession,
            self._SESSION_ENVELOPE,
        )

    def create_execution_session(
        self, params: MandateExecutionSessionCreateParams
    ) -> PaymentSession:
        return self._http.post_object(
            "/paymentsessions",
            params.to_dict(),
            PaymentSession,
            self._SESSION_ENVELOPE,
        )

    def send_notification(
        self, params: MandateNotifyParams
    ) -> MandateNotification:
        return self._http.post_object(
            "/mandates/notify",
            params.to_dict(),
            MandateNotification,
            self._NOTIFICATION_ENVELOPE,
        )

    def execute(self, params: MandateExecuteParams) -> MandatePayment:
        return self._http.post_object(
            "/mandates/execute",
            params.to_dict(),
            MandatePayment,
            self._PAYMENT_ENVELOPE,
        )

    def get_notification(
        self, mandate_notification_id: str
    ) -> MandateNotification:
        path = f"/mandates/notifications/{encode_path(mandate_notification_id)}"
        return self._http.get_object(
            path, MandateNotification, self._NOTIFICATION_ENVELOPE
        )

    def get(self, mandate_id: str) -> Mandate:
        path = f"/mandates/{encode_path(mandate_id)}"
        return self._http.get_object(path, Mandate, self._MANDATE_ENVELOPE)
