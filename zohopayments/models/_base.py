"""Helpers shared by all response model classes."""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

T = TypeVar("T")


def opt_str(d: Dict[str, Any], key: str) -> Optional[str]:
    v = d.get(key)
    return str(v) if v is not None else None


def opt_int(d: Dict[str, Any], key: str) -> Optional[int]:
    v = d.get(key)
    if v is None:
        return None
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def opt_float(d: Dict[str, Any], key: str) -> Optional[float]:
    v = d.get(key)
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def opt_bool(d: Dict[str, Any], key: str) -> Optional[bool]:
    v = d.get(key)
    if v is None:
        return None
    return bool(v)


def opt_obj(
    d: Dict[str, Any], key: str, type_: Type[T]
) -> Optional[T]:
    v = d.get(key)
    if not isinstance(v, dict):
        return None
    from_dict = getattr(type_, "from_dict", None)
    if from_dict is None:
        return None
    return from_dict(v)  # type: ignore[no-any-return]


def opt_list(
    d: Dict[str, Any], key: str, element_from_dict: Callable[[Dict[str, Any]], T]
) -> List[T]:
    v = d.get(key)
    if not isinstance(v, list):
        return []
    return [element_from_dict(item) for item in v if isinstance(item, dict)]


def opt_str_list(d: Dict[str, Any], key: str) -> List[str]:
    v = d.get(key)
    if not isinstance(v, list):
        return []
    return [str(item) for item in v if item is not None]
