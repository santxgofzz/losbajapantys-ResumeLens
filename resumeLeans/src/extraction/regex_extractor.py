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


PROGRAMMING_LANGUAGES_PATTERN = (
    r"(?<![\w.])(?:JavaScript|JS|TypeScript|TS|Python|py(?![ \t]+Torch\b)|Java)\b"
)


def extract_programming_languages(text: str) -> list[str]:
    """Return supported language mentions with original case, order and repeats.

    Match JavaScript/JS, TypeScript/TS, Python/py and Java throughout the text.
    Exclude longer words and dotted suffixes such as the js in React.js.
    """
    return re.findall(PROGRAMMING_LANGUAGES_PATTERN, text, flags=re.IGNORECASE)


FRAMEWORKS_PATTERN = (
    r"(?<![\w.])"
    r"(?:React(?:\.js|JS)?|Angular(?:\.js|JS)?|Vue(?:\.js|JS)?|Node(?:JS|\.js)?|"
    r"Django|Spring(?:[ \t]*Boot|(?!\s+Boot))|Pandas|NumPy|Scikit[- ]learn|sklearn|"
    r"Tensor ?Flow|tf|Py ?Torch)"
    r"(?!\w|\.\w)"
)


def extract_frameworks(text: str) -> list[str]:
    """Return supported frameworks, libraries and runtimes as originally written.

    Search the entire text without normalizing case or spelling. Preserve
    order and repetitions. Spring Boot allows horizontal whitespace; other
    multiword variants use a single literal space.
    """
    return re.findall(FRAMEWORKS_PATTERN, text, flags=re.IGNORECASE)


DATABASES_PATTERN = r"(?<![\w.])(?:PostgreSQL|Postgres|MySQL|MongoDB)(?!\w|\.\w)"


def extract_databases(text: str) -> list[str]:
    """Return supported database names with original case, order and repeats.

    Recognize PostgreSQL, Postgres, MySQL and MongoDB throughout the text.
    Do not normalize aliases or infer a database from SQL/NoSQL mentions.
    """
    return re.findall(DATABASES_PATTERN, text, flags=re.IGNORECASE)


TOOLS_PATTERN = (
    r"(?<![\w.])"
    r"(?:GitHub[ \t]+Actions|GitLab[ \t]+CI|Git|Docker|Linux|Kubernetes|K8s|Jenkins|"
    r"AWS|Amazon[ \t]+Web[ \t]+Services|GCP|"
    r"Google[ \t]+Cloud(?:[ \t]+Platform|(?![ \t]+Platform))|"
    r"(?:Microsoft[ \t]+)?Azure|Terraform|"
    r"(?:Apache[ \t]+)?(?:Spark|Airflow|Kafka)|PySpark)"
    r"(?!\w|\.\w)"
)


def extract_tools(text: str) -> list[str]:
    """Return supported development, DevOps and data tools as originally written.

    Include cloud platforms and data-processing technologies. Search the entire
    text; preserve complete names such as GitHub Actions without inferring Git.
    """
    return re.findall(TOOLS_PATTERN, text, flags=re.IGNORECASE)


EDUCATION_FIELD_PATTERN = (
    r"(?:Systems[ \t]+Engineering|Computer[ \t]+Science|Software[ \t]+Engineering|"
    r"Computer[ \t]+Engineering|Data[ \t]+Science|Artificial[ \t]+Intelligence|"
    r"Machine[ \t]+Learning|Information[ \t]+Technology)"
)

EDUCATION_PATTERN = (
    r"(?<![\w.])"
    r"(?:(?:Bachelor|Master)['’]s[ \t]+degree|"
    r"(?:Bachelor|Master)[ \t]+of[ \t]+(?:Science|Engineering)|PhD|Ph\.D\.|[BM]Sc|[BM]\.Sc\.)"
    r"[ \t]+in[ \t]+"
    + EDUCATION_FIELD_PATTERN
    + r"(?:[ \t]*(?:\band\b|&|/)[ \t]*(?:"
    + EDUCATION_FIELD_PATTERN + r"|Mathematics))*\b"
    r"(?![ \t]*(?:\band\b|&|/))"
)


def extract_education(text: str) -> list[str]:
    """Return supported English degree-and-field phrases as originally written.

    Require a degree followed by 'in' and a listed computing field. Preserve
    supported compound fields; reject a following unsupported and/&/ component.
    Do not infer completion status, institutions or equivalent qualifications.
    """
    return re.findall(EDUCATION_PATTERN, text, flags=re.IGNORECASE)


EXPERIENCE_PATTERN = (
    r"(?<![\w.+−–—-])[0-9]+(?:\.[0-9]+)?\+?"
    r"(?:[ \t]*(?:[-–—]|\bto\b)[ \t]*[0-9]+(?:\.[0-9]+)?)?"
    r"[ \t]+(?:years?|months?)"
    r"(?:[ \t]+and[ \t]+[0-9]+(?:\.[0-9]+)?[ \t]+(?:years?|months?))*"
    r"[ \t]+(?:of[ \t]+)?"
    r"(?:(?:professional|work)[ \t]+)?experience\b"
)


def extract_experience(text: str) -> list[str]:
    """Return explicit numeric experience durations, preserving original text.

    Support years/months, decimals, plus signs, numeric ranges and durations
    joined by 'and', preserving the entire supported expression.
    Do not calculate durations from dates or infer relevance to a job profile.
    """
    return re.findall(EXPERIENCE_PATTERN, text, flags=re.IGNORECASE)


OTHER_QUALIFICATIONS_PATTERN = (
    r"(?<![\w.])"
    r"(?:REST(?:ful)?[ \t]+APIs?|No[ \t]*SQL|SQL|ML|"
    r"machine(?:-|[ \t]+)learning(?:[ \t]+model[ \t]+development|(?![ \t]+model\b))|"
    r"CI[/-]CD|ETL|Extract[ \t]+Transform[ \t]+Load|Data[ \t]+Warehouse|DWH|DW)"
    r"(?!\w|\.\w)"
)


def extract_other_qualifications(text: str) -> list[str]:
    """Return explicit mentions of the supported additional qualifications.

    Recognize REST API(s), SQL, NoSQL, machine-learning model development,
    CI/CD, ETL and data warehouse mentions, including supported aliases.
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
