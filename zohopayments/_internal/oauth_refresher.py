"""Exchanges a Zoho OAuth refresh token for a new access token."""

from __future__ import annotations

import json
from urllib.parse import urlencode

import requests

from zohopayments.auth.oauth_token import OAuthToken
from zohopayments.edition import Edition
from zohopayments.exceptions import ConnectionException, ZohoPaymentsException

CONNECT_TIMEOUT = 30.0
REQUEST_TIMEOUT = 60.0
MAX_ERROR_BODY_SNIPPET = 500
DEFAULT_EXPIRES_IN = 3600


def generate_access_token(
    refresh_token: str,
    client_id: str,
    client_secret: str,
    redirect_uri: str,
    edition: Edition,
) -> OAuthToken:
    if refresh_token is None or refresh_token == "":
        raise ValueError("refresh_token must not be null or empty")
    if client_id is None or client_id == "":
        raise ValueError("client_id must not be null or empty")
    if client_secret is None or client_secret == "":
        raise ValueError("client_secret must not be null or empty")
    if redirect_uri is None or redirect_uri == "":
        raise ValueError("redirect_uri must not be null or empty")
    if edition is None:
        raise ValueError("edition must not be null")

    url = f"{edition.accounts_url}/oauth/v2/token"
    form = {
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "refresh_token",
    }

    try:
        response = requests.post(
            url,
            data=urlencode(form),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=(CONNECT_TIMEOUT, REQUEST_TIMEOUT),
        )
    except requests.exceptions.Timeout as exc:
        raise ConnectionException(f"Token refresh timed out: {exc}") from exc
    except requests.exceptions.ConnectionError as exc:
        raise ConnectionException(
            f"Token refresh connection error: {exc}"
        ) from exc
    except requests.exceptions.RequestException as exc:
        raise ConnectionException(
            f"Token refresh transport failure: {exc}"
        ) from exc

    body = response.text or ""
    snippet = body[:MAX_ERROR_BODY_SNIPPET]

    if not (200 <= response.status_code < 300):
        raise ZohoPaymentsException(
            f"Token refresh failed with HTTP {response.status_code}: {snippet}"
        )

    try:
        parsed = json.loads(body) if body else {}
    except ValueError as exc:
        raise ZohoPaymentsException(
            f"Token refresh response was not valid JSON: {snippet}"
        ) from exc

    if "error" in parsed and "access_token" not in parsed:
        raise ZohoPaymentsException(
            f"Token refresh failed: {parsed.get('error')}"
        )

    access_token = parsed.get("access_token")
    if not access_token:
        raise ZohoPaymentsException(
            f"Token refresh response missing 'access_token': {snippet}"
        )

    expires_in_raw = parsed.get("expires_in_sec")
    if expires_in_raw is None:
        expires_in_raw = parsed.get("expires_in")
    if expires_in_raw is None:
        expires_in = DEFAULT_EXPIRES_IN
    else:
        try:
            expires_in = int(expires_in_raw)
        except (TypeError, ValueError):
            expires_in = DEFAULT_EXPIRES_IN

    return OAuthToken(access_token, expires_in)
