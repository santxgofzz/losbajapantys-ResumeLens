"""Extract original contact information and technical terms using re."""

import re


EMAIL_PATTERN = (
    r"(?<![\w.%+@-])"
    r"[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*"
    r"@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,}"
    r"(?![\w@+-]|\.\w)"
)

def extract_emails(text: str) -> list[str]:
    """Return common ASCII email addresses, preserving case, order and repeats.

    The input must be a string. This is extraction, not mailbox validation.
    """
    return re.findall(EMAIL_PATTERN, text)

PHONE_PATTERN = (
    r"(?<![\w+])(?<![0-9][ -])"
    r"(?:\+57[ -]?)?"
    r"(?:3[0-9]{2}|60[0-9])[ -]?[0-9]{3}[ -]?[0-9]{4}"
    r"(?!\w|[ -]?[0-9])"
)


def extract_phones(text: str) -> list[str]:
    """Return supported Colombian-style numbers with original formatting.

    Match ten digits starting with 3 or 60, optional +57, and optional spaces
    or hyphens. Preserve order and repeats; do not verify number allocation.
    """
    return re.findall(PHONE_PATTERN, text)


PROGRAMMING_LANGUAGES_PATTERN = r"(?<![\w.])(?:JavaScript|JS|TypeScript|TS|Python|Java)\b"


def extract_programming_languages(text: str) -> list[str]:
    """Return supported language mentions with original case, order and repeats.

    Match JavaScript/JS, TypeScript/TS, Python and Java throughout the text.
    Exclude longer words and dotted suffixes such as the js in React.js.
    """
    return re.findall(PROGRAMMING_LANGUAGES_PATTERN, text, flags=re.IGNORECASE)


FRAMEWORKS_PATTERN = (
    r"(?<![\w.])"
    r"(?:React(?:\.js|JS)?|Angular|Vue(?:\.js)?|Node(?:JS|\.js)|"
    r"Django|Spring Boot|Pandas|NumPy|Scikit[- ]learn|sklearn|"
    r"Tensor ?Flow|Py ?Torch)"
    r"(?!\w|\.\w)"
)


def extract_frameworks(text: str) -> list[str]:
    """Return supported frameworks, libraries and runtimes as originally written.

    Search the entire text without normalizing case or spelling. Preserve
    order and repetitions. Multiword variants use a single literal space.
    """
    return re.findall(FRAMEWORKS_PATTERN, text, flags=re.IGNORECASE)


DATABASES_PATTERN = r"(?<![\w.])(?:PostgreSQL|Postgres|MySQL|MongoDB)(?!\w|\.\w)"


def extract_databases(text: str) -> list[str]:
    """Return supported database names with original case, order and repeats.

    Recognize PostgreSQL, Postgres, MySQL and MongoDB throughout the text.
    Do not normalize aliases or infer a database from SQL/NoSQL mentions.
    """
    return re.findall(DATABASES_PATTERN, text, flags=re.IGNORECASE)


TOOLS_PATTERN = r"(?<![\w.])(?:Git|Docker)(?!\w|\.\w)"


def extract_tools(text: str) -> list[str]:
    """Return Git and Docker mentions with original case, order and repeats.

    Search the entire text; do not infer Git from GitHub or GitLab mentions.
    """
    return re.findall(TOOLS_PATTERN, text, flags=re.IGNORECASE)
