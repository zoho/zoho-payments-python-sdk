"""Refund request params."""

from __future__ import annotations
from typing import Any, Dict, List, Optional

from zohopayments.params.common import (
    MetaDataParams,
    MetaDataValidator,
    ParamValidator,
    _meta_data_to_list,
    _require,
)

class RefundCreateParams:
    def __init__(
        self,
        *,
        amount: float,
        reason: str,
        type: str,
        description: Optional[str] = None,
        meta_data: Optional[List[MetaDataParams]] = None,
    ) -> None:
        _require(amount, "amount")
        _require(reason, "reason")
        _require(type, "type")
        ParamValidator.validate_description(description)
        MetaDataValidator.validate(meta_data)

        self._amount = amount
        self._reason = reason
        self._type = type
        self._description = description
        self._meta_data = meta_data

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self._amount,
            "reason": self._reason,
            "type": self._type,
            "description": self._description,
            "meta_data": _meta_data_to_list(self._meta_data),
        }
