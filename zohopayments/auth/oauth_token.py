class OAuthToken:
    def __init__(self, access_token: str, expires_in: int) -> None:
        if access_token is None or access_token == "":
            raise ValueError("access_token must not be null or empty")
        self._access_token = access_token
        self._expires_in = int(expires_in)

    @property
    def access_token(self) -> str:
        return self._access_token

    @property
    def expires_in(self) -> int:
        return self._expires_in
