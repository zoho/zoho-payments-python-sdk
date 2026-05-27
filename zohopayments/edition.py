from enum import Enum

class Edition(Enum):
    IN = ("https://payments.zoho.in/api/v1", "https://accounts.zoho.in")
    IN_SANDBOX = ("https://paymentssandbox.zoho.in/api/v1", "https://accounts.zoho.in")
    US = ("https://payments.zoho.com/api/v1", "https://accounts.zoho.com")

    def __init__(self, base_url: str, accounts_url: str) -> None:
        self._base_url = base_url
        self._accounts_url = accounts_url

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def accounts_url(self) -> str:
        return self._accounts_url

    def is_us(self) -> bool:
        return self is Edition.US

    def is_in(self) -> bool:
        return self in (Edition.IN, Edition.IN_SANDBOX)

    @classmethod
    def from_string(cls, name: str) -> "Edition":
        if name is None or name == "":
            raise ValueError("edition name must not be null or empty")
        try:
            return cls[name.upper()]
        except KeyError:
            raise ValueError(
                f"unknown edition: {name!r}. Expected one of: "
                f"{', '.join(e.name for e in cls)}"
            ) from None
