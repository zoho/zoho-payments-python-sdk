from __future__ import annotations

from typing import Any, Dict, List, Optional

from zohopayments.params.common import (
    HostedPageParams,
    MetaDataParams,
    MetaDataValidator,
    ParamValidator,
    _meta_data_to_list,
    _require,
)

class MandateDetailsParams:
    def __init__(
        self,
        *,
        payment_method_type: str,
        frequency: str,
        description: str,
        amount_rule: str,
        max_amount: Optional[float] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        debit_day: Optional[int] = None,
        debit_rule: Optional[str] = None,
    ) -> None:
        _require(payment_method_type, "payment_method_type")
        _require(frequency, "frequency")
        _require(description, "description")
        _require(amount_rule, "amount_rule")
        if amount_rule == "variable" and max_amount is None:
            raise ValueError(
                "max_amount is required when amount_rule is 'variable'"
            )
        ParamValidator.validate_description(description)

        self._payment_method_type = payment_method_type
        self._frequency = frequency
        self._description = description
        self._amount_rule = amount_rule
        self._max_amount = max_amount
        self._start_date = start_date
        self._end_date = end_date
        self._debit_day = debit_day
        self._debit_rule = debit_rule

    def to_dict(self) -> Dict[str, Any]:
        return {
            "payment_method_type": self._payment_method_type,
            "frequency": self._frequency,
            "description": self._description,
            "amount_rule": self._amount_rule,
            "max_amount": self._max_amount,
            "start_date": self._start_date,
            "end_date": self._end_date,
            "debit_day": self._debit_day,
            "debit_rule": self._debit_rule,
        }


class MandateConfigurationsParams:
    def __init__(
        self, *, hosted_page_parameters: Optional[HostedPageParams] = None
    ) -> None:
        self._hosted_page_parameters = hosted_page_parameters

    def to_dict(self) -> Dict[str, Any]:
        return {
            "hosted_page_parameters": (
                self._hosted_page_parameters.to_dict()
                if self._hosted_page_parameters is not None
                else None
            )
        }


class MandateEnrollmentSessionCreateParams:
    _TYPE = "mandate_enrollment"

    def __init__(
        self,
        *,
        amount: float,
        currency: str,
        customer_id: str,
        description: str,
        mandate_details: MandateDetailsParams,
        invoice_number: Optional[str] = None,
        max_retry_count: Optional[int] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
        configurations: Optional[MandateConfigurationsParams] = None,
    ) -> None:
        _require(amount, "amount")
        _require(currency, "currency")
        _require(customer_id, "customer_id")
        _require(description, "description")
        if mandate_details is None:
            raise ValueError("mandate_details is required")
        if max_retry_count is not None and not (1 <= max_retry_count <= 3):
            raise ValueError("max_retry_count must be between 1 and 3")
        ParamValidator.validate_description(description)
        ParamValidator.validate_invoice_number(invoice_number)
        MetaDataValidator.validate(meta_data)

        self._amount = amount
        self._currency = currency
        self._customer_id = customer_id
        self._description = description
        self._mandate_details = mandate_details
        self._invoice_number = invoice_number
        self._max_retry_count = max_retry_count
        self._meta_data = meta_data
        self._configurations = configurations

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self._TYPE,
            "amount": self._amount,
            "currency": self._currency,
            "customer_id": self._customer_id,
            "description": self._description,
            "mandate_details": self._mandate_details.to_dict(),
            "invoice_number": self._invoice_number,
            "max_retry_count": self._max_retry_count,
            "meta_data": _meta_data_to_list(self._meta_data),
            "configurations": (
                self._configurations.to_dict()
                if self._configurations is not None
                else None
            ),
        }


class MandateExecutionSessionCreateParams:
    _TYPE = "mandate_execution"

    def __init__(
        self,
        *,
        amount: float,
        currency: str,
        customer_id: str,
        description: str,
        invoice_number: str,
        max_retry_count: Optional[int] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
    ) -> None:
        _require(amount, "amount")
        _require(currency, "currency")
        _require(customer_id, "customer_id")
        _require(description, "description")
        _require(invoice_number, "invoice_number")
        if max_retry_count is not None and not (1 <= max_retry_count <= 3):
            raise ValueError("max_retry_count must be between 1 and 3")
        ParamValidator.validate_description(description)
        ParamValidator.validate_invoice_number(invoice_number)
        MetaDataValidator.validate(meta_data)

        self._amount = amount
        self._currency = currency
        self._customer_id = customer_id
        self._description = description
        self._invoice_number = invoice_number
        self._max_retry_count = max_retry_count
        self._meta_data = meta_data

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self._TYPE,
            "amount": self._amount,
            "currency": self._currency,
            "customer_id": self._customer_id,
            "description": self._description,
            "invoice_number": self._invoice_number,
            "max_retry_count": self._max_retry_count,
            "meta_data": _meta_data_to_list(self._meta_data),
        }


class MandateNotifyParams:
    def __init__(
        self,
        *,
        mandate_id: str,
        amount: float,
        execution_date: str,
        description: str,
        invoice_number: str,
    ) -> None:
        _require(mandate_id, "mandate_id")
        _require(amount, "amount")
        _require(execution_date, "execution_date")
        _require(description, "description")
        _require(invoice_number, "invoice_number")
        ParamValidator.validate_description(description)
        ParamValidator.validate_invoice_number(invoice_number)

        self._mandate_id = mandate_id
        self._amount = amount
        self._execution_date = execution_date
        self._description = description
        self._invoice_number = invoice_number

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mandate_id": self._mandate_id,
            "amount": self._amount,
            "execution_date": self._execution_date,
            "description": self._description,
            "invoice_number": self._invoice_number,
        }


class MandateExecuteParams:
    def __init__(
        self,
        *,
        customer_id: str,
        mandate_id: str,
        payments_session_id: str,
        invoice_number: str,
        amount: float,
        mandate_notification_id: Optional[str] = None,
        receipt_email: Optional[str] = None,
        phone: Optional[str] = None,
        phone_country_code: Optional[str] = None,
        description: Optional[str] = None,
        reference_number: Optional[str] = None,
    ) -> None:
        _require(customer_id, "customer_id")
        _require(mandate_id, "mandate_id")
        _require(payments_session_id, "payments_session_id")
        _require(invoice_number, "invoice_number")
        _require(amount, "amount")
        ParamValidator.validate_description(description)
        ParamValidator.validate_invoice_number(invoice_number)
        ParamValidator.validate_reference_number(reference_number)

        self._customer_id = customer_id
        self._mandate_id = mandate_id
        self._payments_session_id = payments_session_id
        self._invoice_number = invoice_number
        self._amount = amount
        self._mandate_notification_id = mandate_notification_id
        self._receipt_email = receipt_email
        self._phone = phone
        self._phone_country_code = phone_country_code
        self._description = description
        self._reference_number = reference_number

    def to_dict(self) -> Dict[str, Any]:
        return {
            "customer_id": self._customer_id,
            "mandate_id": self._mandate_id,
            "payments_session_id": self._payments_session_id,
            "invoice_number": self._invoice_number,
            "amount": self._amount,
            "mandate_notification_id": self._mandate_notification_id,
            "receipt_email": self._receipt_email,
            "phone": self._phone,
            "phone_country_code": self._phone_country_code,
            "description": self._description,
            "reference_number": self._reference_number,
        }
