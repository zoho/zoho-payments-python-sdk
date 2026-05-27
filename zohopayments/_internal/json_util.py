"""JSON helpers: serialization and envelope unwrapping.

Field naming follows snake_case conventions. Envelope helpers extract
typed objects from ``{"payment": {...}}`` style API response payloads.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Type, TypeVar

from zohopayments.exceptions import ZohoPaymentsException
from zohopayments.models.page_context import PageContext

T = TypeVar("T")


def to_json(obj: Any) -> str:
    """Serialize a dict/list/primitive into a JSON string, dropping ``None`` values."""
    return json.dumps(_strip_nones(obj), separators=(",", ":"))


def _strip_nones(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _strip_nones(v) for k, v in value.items() if v is not None}
    if isinstance(value, list):
        return [_strip_nones(v) for v in value]
    return value


def parse_object(text: str) -> Dict[str, Any]:
    """Parse a JSON string, requiring a JSON object at the root."""
    try:
        data = json.loads(text)
    except ValueError as exc:
        raise ZohoPaymentsException(f"Invalid JSON in response: {exc}") from exc
    if not isinstance(data, dict):
        raise ZohoPaymentsException("Expected JSON object in response")
    return data


def get_object(
    body: Optional[Dict[str, Any]], *keys: str
) -> Optional[Dict[str, Any]]:
    """Return the first matching JSON object value from ``body`` by key, or ``None``."""
    if not body:
        return None
    for key in keys:
        value = body.get(key)
        if isinstance(value, dict):
            return value
    return None


def get_object_required(
    body: Optional[Dict[str, Any]], *keys: str
) -> Dict[str, Any]:
    obj = get_object(body, *keys)
    if obj is None:
        joined = ", ".join(keys)
        raise ZohoPaymentsException(
            f"Expected JSON object under one of keys: {joined}"
        )
    return obj


def list_from_body(
    body: Optional[Dict[str, Any]], *keys: str
) -> List[Any]:
    """Return the first JSON array value found under any of the candidate keys."""
    if not body:
        return []
    for key in keys:
        value = body.get(key)
        if isinstance(value, list):
            return value
    return []


def unwrap(response_body: Dict[str, Any], type_: Type[T], *candidate_keys: str) -> T:
    """Extract the single-resource envelope and deserialize into ``type_``.

    The response is expected to look like ``{"payment": {...}, ...}``. We take
    the first key in ``candidate_keys`` that points to a JSON object and feed
    that to ``type_.from_dict``.
    """
    inner = get_object_required(response_body, *candidate_keys)
    from_dict = getattr(type_, "from_dict", None)
    if from_dict is None:
        raise ZohoPaymentsException(
            f"Type {type_.__name__} does not support from_dict deserialization"
        )
    return from_dict(inner)  # type: ignore[no-any-return]


def read_page_context(body: Optional[Dict[str, Any]]) -> PageContext:
    pc = get_object(body, "page_context")
    if pc is None:
        return PageContext()
    return PageContext.from_dict(pc)
