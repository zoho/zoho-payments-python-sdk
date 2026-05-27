from __future__ import annotations

import threading


class TokenManager:
    """Stores the current OAuth access token with thread-safe updates."""

    def __init__(self, access_token: str) -> None:
        if access_token is None or access_token == "":
            raise ValueError("access_token must not be null or empty")
        self._lock = threading.Lock()
        self._access_token = access_token

    def get_access_token(self) -> str:
        with self._lock:
            return self._access_token

    def update_token(self, new_access_token: str) -> None:
        if new_access_token is None or new_access_token == "":
            raise ValueError("new_access_token must not be null or empty")
        with self._lock:
            self._access_token = new_access_token
