"""Helper for turning list-param objects into :class:`QueryParams`."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from zohopayments._internal.query_params import QueryParams

def query_from(params: Optional[Mapping[str, Any]]) -> QueryParams:
    q = QueryParams()
    if params is None:
        return q
    for key, value in params.items():
        q.add(key, value)
    return q
