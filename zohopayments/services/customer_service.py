"""Customers service."""

from __future__ import annotations

from typing import Optional

from zohopayments._internal.zoho_http_client import ZohoHttpClient, encode_path
from zohopayments.edition import Edition
from zohopayments.models.customer import Customer, CustomerSummary
from zohopayments.models.list_response import ListResponse
from zohopayments.params.customer import CustomerCreateParams, CustomerListParams
from zohopayments.services._query_builder import query_from


class CustomerService:
    _SINGLE_ENVELOPE = "customer"
    _LIST_ENVELOPE = "customers"

    def __init__(self, http: ZohoHttpClient, edition: Edition) -> None:
        self._http = http
        self._edition = edition

    def create(self, params: CustomerCreateParams) -> Customer:
        return self._http.post_object(
            "/customers", params.to_dict(), Customer, self._SINGLE_ENVELOPE
        )

    def get(self, customer_id: str) -> Customer:
        path = f"/customers/{encode_path(customer_id)}"
        return self._http.get_object(path, Customer, self._SINGLE_ENVELOPE)

    def list(
        self, params: Optional[CustomerListParams] = None
    ) -> ListResponse[CustomerSummary]:
        if not self._edition.is_us():
            raise NotImplementedError(
                "customers.list() is available only on Edition.US"
            )
        query = query_from(params.to_query() if params else None)
        return self._http.list_objects(
            "/customers",
            query,
            CustomerSummary.from_dict,
            self._LIST_ENVELOPE,
        )

    def delete(self, customer_id: str) -> None:
        if not self._edition.is_us():
            raise NotImplementedError(
                "customers.delete() is available only on Edition.US"
            )
        path = f"/customers/{encode_path(customer_id)}"
        self._http.delete(path)
