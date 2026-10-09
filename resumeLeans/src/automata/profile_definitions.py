"""Qualification definitions used by the ResumeLens classification automata"""

from collections.abc import Iterable


PROFILE_DEFINITIONS = {
    "FULL_STACK_DEVELOPER": (
        (
            "programming_language",
            ("JAVASCRIPT", "TYPESCRIPT"),
        ),
        (
            "frontend",
            ("REACT", "ANGULAR", "VUE"),
        ),
        (
            "backend",
            ("NODE_JS", "DJANGO", "SPRING_BOOT"),
        ),
        (
            "database",
            ("SQL", "POSTGRESQL", "NOSQL"),
        ),
        (
            "api",
            ("REST_API",),
        ),
        (
            "version_control",
            ("GIT",),
        ),
    ),

    "MACHINE_LEARNING_ENGINEER": (
        (
            "programming_language",
            ("PYTHON",),
        ),
        (
            "data_processing",
            ("PANDAS", "NUMPY"),
        ),
        (
            "machine_learning",
            ("SCIKIT_LEARN", "TENSORFLOW", "PYTORCH"),
        ),
        (
            "database",
            ("SQL", "POSTGRESQL"),
        ),
        (
            "version_control",
            ("GIT",),
        ),
    ),

    "DEVOPS_ENGINEER": (
        (
            "operating_system",
            ("LINUX",),
        ),
        (
            "containerization",
            ("DOCKER",),
        ),
        (
            "orchestration",
            ("KUBERNETES",),
        ),
        (
            "ci_cd",
            ("JENKINS", "GITHUB_ACTIONS", "GITLAB_CI"),
        ),
        (
            "cloud",
            ("AWS", "AZURE", "GCP"),
        ),
        (
            "infrastructure_as_code",
            ("TERRAFORM",),
        ),
        (
            "version_control",
            ("GIT",),
        ),
    ),

    "DATA_ENGINEER": (
        (
            "programming_language",
            ("PYTHON",),
        ),
        (
            "database",
            ("SQL", "POSTGRESQL"),
        ),
        (
            "data_integration",
            ("ETL",),
        ),
        (
            "distributed_data",
            ("SPARK", "KAFKA"),
        ),
        (
            "workflow_orchestration",
            ("AIRFLOW",),
        ),
        (
            "data_storage",
            ("DATA_WAREHOUSE",),
        ),
        (
            "version_control",
            ("GIT",),
        ),
    ),
}


SUPPORTED_PROFILES = tuple(PROFILE_DEFINITIONS.keys())


def get_profile_definition(profile_name: str):
    """Return the qualification categories defined for a professional profile."""

    if profile_name not in PROFILE_DEFINITIONS:
        supported = ", ".join(SUPPORTED_PROFILES)
        raise ValueError(
            f"Unsupported profile '{profile_name}'. "
            f"Supported profiles: {supported}"
        )

    return PROFILE_DEFINITIONS[profile_name]


def get_profile_alphabet(profile_name: str) -> set[str]:
    """Return every canonical qualification accepted by a profile."""

    definition = get_profile_definition(profile_name)

    return {
        symbol
        for _, symbols in definition
        for symbol in symbols
    }


def prepare_qualifications_for_profile(
    qualifications: Iterable[str],
    profile_name: str,
) -> list[str]:
    """
    Filter and order normalized qualifications for a professional profile.

    Qualifications outside the profile alphabet are ignored. Repeated
    qualifications are removed, and the remaining symbols are placed in the
    canonical order defined by the profile.
    """

    definition = get_profile_definition(profile_name)

    canonical_order = {}

    for category_index, (_, symbols) in enumerate(definition):
        for symbol_index, symbol in enumerate(symbols):
            canonical_order[symbol] = (category_index, symbol_index)

    relevant_qualifications = {
        qualification
        for qualification in qualifications
        if qualification in canonical_order
    }

    return sorted(
        relevant_qualifications,
        key=lambda qualification: canonical_order[qualification],
    )