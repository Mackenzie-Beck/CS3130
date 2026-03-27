import re
from typing import Pattern

_EMAIL_RE: Pattern[str] = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

def is_valid_email(email: str) -> bool:
    """Return True if the given string is a syntactically valid email address.

    This uses a reasonable regex for common email formats (not a full RFC 5322 parser).
    """
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_RE.fullmatch(email.strip()))

__all__ = ["is_valid_email"]