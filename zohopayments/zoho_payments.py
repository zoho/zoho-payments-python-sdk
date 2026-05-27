"""Top-level factory for the Zoho Payments SDK."""

from __future__ import annotations

from zohopayments._internal.oauth_refresher import (
    generate_access_token as _generate_access_token,
)
from zohopayments.auth.oauth_token import OAuthToken
from zohopayments.client import ZohoPaymentsClientBuilder
from zohopayments.edition import Edition


class ZohoPayments:
    @staticmethod
    def builder() -> ZohoPaymentsClientBuilder:
        return ZohoPaymentsClientBuilder()

    @staticmethod
    def generate_access_token(
        refresh_token: str,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        edition: Edition,
    ) -> OAuthToken:
        """Generate a new OAuth access token by exchanging the supplied refresh token.

        The SDK does not refresh tokens automatically — callers push the new
        token into a running client via :meth:`ZohoPaymentsClient.update_token`.
        """
        return _generate_access_token(
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            edition=edition,
        )
