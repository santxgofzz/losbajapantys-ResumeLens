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


EDUCATION_PATTERN = (
    r"(?<![\w.])"
    r"(?:(?:Bachelor|Master)['’]s[ \t]+degree|"
    r"(?:Bachelor|Master)[ \t]+of[ \t]+Science|PhD|Ph\.D\.|[BM]Sc|[BM]\.Sc\.)"
    r"[ \t]+in[ \t]+"
    r"(?:Systems[ \t]+Engineering|Computer[ \t]+Science|Software[ \t]+Engineering|"
    r"Computer[ \t]+Engineering|Data[ \t]+Science|Artificial[ \t]+Intelligence|"
    r"Machine[ \t]+Learning|Information[ \t]+Technology)\b"
)


def extract_education(text: str) -> list[str]:
    """Return supported English degree-and-field phrases as originally written.

    Require an explicit degree followed by 'in' and a listed computing field.
    Do not infer completion status, institutions or equivalent qualifications.
    """
    return re.findall(EDUCATION_PATTERN, text, flags=re.IGNORECASE)


EXPERIENCE_PATTERN = (
    r"(?<![\w.+-])[0-9]+(?:\.[0-9]+)?\+?"
    r"[ \t]+(?:years?|months?)[ \t]+(?:of[ \t]+)?"
    r"(?:(?:professional|work)[ \t]+)?experience\b"
)


def extract_experience(text: str) -> list[str]:
    """Return explicit numeric experience durations, preserving original text.

    Support years/months, decimals and a trailing plus sign on the number.
    Do not calculate durations from dates or infer relevance to a job profile.
    """
    return re.findall(EXPERIENCE_PATTERN, text, flags=re.IGNORECASE)


OTHER_QUALIFICATIONS_PATTERN = (
    r"(?<![\w.])"
    r"(?:REST[ \t]+APIs?|NoSQL|SQL|"
    r"machine(?:-|[ \t]+)learning[ \t]+model[ \t]+development)"
    r"(?!\w|\.\w)"
)


def extract_other_qualifications(text: str) -> list[str]:
    """Return explicit mentions of the supported additional qualifications.

    Recognize REST API(s), SQL, NoSQL and machine-learning model development.
    Preserve case, spacing, order and repeats; do not infer skills from products.
    """
    return re.findall(OTHER_QUALIFICATIONS_PATTERN, text, flags=re.IGNORECASE)


def extract_resume_info(text: str) -> dict[str, list[str]]:
    """Return all nine extraction categories, including empty lists.

    Input is resume text, not a file path. Values retain original matched text.
    This function does not normalize, classify, or perform file operations.
    """
    return {
        "emails": extract_emails(text),
        "phones": extract_phones(text),
        "programming_languages": extract_programming_languages(text),
        "frameworks": extract_frameworks(text),
        "databases": extract_databases(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "tools": extract_tools(text),
        "other_qualifications": extract_other_qualifications(text),
    }
