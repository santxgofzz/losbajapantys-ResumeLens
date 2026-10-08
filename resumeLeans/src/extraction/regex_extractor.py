"""Extract original contact information from resume text using re."""

import re


EMAIL_PATTERN = (
    r"(?<![\w.%+@-])"
    r"[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*"
    r"@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,}"
    r"(?![\w@+-]|\.\w)"
)

PHONE_PATTERN = (
    r"(?<![\w+])(?<![0-9][ -])"
    r"(?:\+57[ -]?)?"
    r"(?:3[0-9]{2}|60[0-9])[ -]?[0-9]{3}[ -]?[0-9]{4}"
    r"(?!\w|[ -]?[0-9])"
)


def extract_emails(text: str) -> list[str]:
    """Return common ASCII email addresses, preserving case, order and repeats.

    The input must be a string. This is extraction, not mailbox validation.
    """
    return re.findall(EMAIL_PATTERN, text)


def extract_phones(text: str) -> list[str]:
    """Return supported Colombian-style numbers with original formatting.

    Match ten digits starting with 3 or 60, optional +57, and optional spaces
    or hyphens. Preserve order and repeats; do not verify number allocation.
    """
    return re.findall(PHONE_PATTERN, text)
