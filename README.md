# Zoho Payments Python SDK

Official Python SDK for the Zoho Payments API — supports IN, IN Sandbox, and US editions.

API reference:
- **India:** https://www.zoho.com/in/payments/api/v1/introduction/
- **United States:** https://www.zoho.com/us/payments/api/v1/introduction/

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Requirements

- **Python 3.11+**
- **requests 2.32+**

## Installation

```sh
pip install zoho-payments
```

## Quick Start

```python
from zohopayments import ZohoPayments, Edition
from zohopayments.params import PaymentLinkCreateParams

# 1. Build the client
client = (
    ZohoPayments.builder()
    .account_id("23137556")
    .edition(Edition.IN)
    .oauth_token("1000.xxxx.yyyy")
    .build()
)

# 2. Use a service
link = client.payment_links().create(
    PaymentLinkCreateParams(
        amount=500.00,
        currency="INR",
        description="Order #1234",
        email="customer@example.com",
    )
)

print("Created:", link.payment_link_id)

# 3. Close when done (or use as a context manager)
client.close()
```

Or using the client as a context manager:

```python
with (
    ZohoPayments.builder()
    .account_id("23137556")
    .edition(Edition.IN)
    .oauth_token("1000.xxxx.yyyy")
    .build()
) as client:
    link = client.payment_links().get("173000002315107")
```

## Editions

| Edition | Payments API Base URL | OAuth Accounts URL |
|---------|-----------------------|--------------------|
| `Edition.IN` | `https://payments.zoho.in/api/v1` | `https://accounts.zoho.in` |
| `Edition.IN_SANDBOX` | `https://paymentssandbox.zoho.in/api/v1` | `https://accounts.zoho.in` |
| `Edition.US` | `https://payments.zoho.com/api/v1` | `https://accounts.zoho.com` |

Helper methods: `edition.is_in()` returns `True` for both `IN` and `IN_SANDBOX`; `edition.is_us()` returns `True` for `US`.

## Authentication

### Access token only

```python
client = (
    ZohoPayments.builder()
    .account_id("23137556")
    .edition(Edition.IN)
    .oauth_token("1000.access_token_here")
    .build()
)
```

### Token refresh

The SDK does **not** auto-refresh tokens. Use `ZohoPayments.generate_access_token()` when the access token expires, then push the new token into the client:

```python
fresh = ZohoPayments.generate_access_token(
    refresh_token="...",
    client_id="...",
    client_secret="...",
    redirect_uri="...",
    edition=Edition.IN,
)

# Persist the new token in your storage layer
my_store.save(fresh.access_token, fresh.expires_in)

# Update the running client (thread-safe, no rebuild needed)
client.update_token(fresh.access_token)
```

You can also pass an `OAuthToken` directly to the builder:

```python
token = ZohoPayments.generate_access_token(...)
client = (
    ZohoPayments.builder()
    .account_id("23137556")
    .edition(Edition.IN)
    .oauth_token(token)
    .build()
)
```

`OAuthToken` exposes `access_token` and `expires_in` (token lifetime in seconds, as returned by IAM).

## Client configuration

```python
client = (
    ZohoPayments.builder()
    .account_id("23137556")                 # Required
    .edition(Edition.IN)                    # Required
    .oauth_token("1000.xxxx.yyyy")          # Required
    .connect_timeout(15.0)                  # Default: 30 seconds
    .request_timeout(45.0)                  # Default: 60 seconds
    .add_default_header("X-Custom-Header", "value")
    .build()
)
```

Reserved headers (`Authorization`, `User-Agent`, `Accept`, `Content-Type`, `Content-Length`, `Host`) are managed by the SDK and cannot be overridden via `add_default_header`.

## Services

| Accessor | Description | Editions |
|----------|-------------|----------|
| `client.payment_links()` | Payment link CRUD | All |
| `client.payment_sessions()` | Payment sessions | All |
| `client.customers()` | Customers | All (list/delete: US only) |
| `client.payments()` | Payments | All (create: US only) |
| `client.refunds()` | Refunds | All |
| `client.payment_methods()` | Saved payment methods | US only |
| `client.payment_method_sessions()` | Payment-method collection sessions | US only |
| `client.mandates()` | Recurring mandates | IN only |
| `client.collect()` | Virtual accounts (Collect) | IN only |

## Examples

### Payment link

```python
from zohopayments.params import PaymentLinkCreateParams, NotifyCustomerParams

link = client.payment_links().create(
    PaymentLinkCreateParams(
        amount=500.00,
        currency="INR",
        description="Order #1234",
        email="customer@example.com",
        notify_customer=NotifyCustomerParams(email=True, sms=False),
    )
)

# Retrieve
fetched = client.payment_links().get(link.payment_link_id)

# Cancel
cancelled = client.payment_links().cancel(link.payment_link_id)
```

### Customer

```python
from zohopayments.params import CustomerCreateParams, MetaDataParams

customer = client.customers().create(
    CustomerCreateParams(
        name="Jane Doe",
        email="jane@example.com",
        meta_data=[MetaDataParams("source", "web")],
    )
)

fetched = client.customers().get(customer.customer_id)
print(fetched.customer_id, fetched.customer_name)
```

### Refund

```python
from zohopayments.params import RefundCreateParams

refund = client.refunds().create(
    payment_id="1234567",
    params=RefundCreateParams(
        amount=100.00,
        reason="requested_by_customer",
        type="full",
    ),
)
```

### Mandate (IN)

```python
from zohopayments.params import (
    MandateDetailsParams,
    MandateEnrollmentSessionCreateParams,
)

enrollment = client.mandates().create_enrollment_session(
    MandateEnrollmentSessionCreateParams(
        amount=0.00,
        currency="INR",
        customer_id="173000002315107",
        description="SIP enrollment",
        mandate_details=MandateDetailsParams(
            payment_method_type="upi",
            frequency="monthly",
            description="Monthly SIP",
            amount_rule="variable",
            max_amount=5000.00,
        ),
    )
)
```

## Error handling

All API errors raise a subclass of `ZohoPaymentsException`.

| Exception | HTTP |
|-----------|------|
| `AuthenticationException` | 401 |
| `PermissionException` | 403 |
| `ResourceNotFoundException` | 404 |
| `InvalidRequestException` | 400, 422 |
| `RateLimitException` | 429 |
| `ZohoPaymentsAPIException` | Any other non-2xx |
| `ConnectionException` | Network / IO failure |

```python
from zohopayments import (
    AuthenticationException,
    InvalidRequestException,
    ZohoPaymentsAPIException,
)

try:
    client.payments().get("123456789")
except AuthenticationException:
    # refresh the token and retry
    ...
except InvalidRequestException as exc:
    print(exc.code_string, exc.api_error_message)
except ZohoPaymentsAPIException as exc:
    print("other API error:", exc.http_status_code)
```

## Custom HTTP transport

`DefaultHttpClient` wraps a `requests.Session`. To plug in your own retries, proxy, instrumentation, etc., implement `HttpClientInterface`:

```python
from zohopayments.net.http_client_interface import HttpClientInterface
from zohopayments.net.response import ZohoResponse

class MyTransport(HttpClientInterface):
    def execute(self, request):
        # ... send request.method / request.url / request.headers / request.body
        return ZohoResponse(status_code=200, headers={}, body='{...}')

    def close(self):
        pass

client = (
    ZohoPayments.builder()
    .account_id("...")
    .edition(Edition.IN)
    .oauth_token("...")
    .http_client(MyTransport())
    .build()
)
```

When you inject a custom transport you cannot also set `connect_timeout` — the transport manages its own connection lifecycle.

## Thread safety

- `ZohoPaymentsClient` is safe to share across threads.
- `client.update_token()` is atomic; in-flight requests on other threads see either the old or the new token.
- Services are eagerly constructed and stateless beyond the shared HTTP client.

## License

Apache 2.0
