"""Parse candidate-profile DSL text using the adjacent textX grammar."""

from pathlib import Path
import ast
import json
import re

from textx import metamodel_from_file
from src.automata.profile_definitions import SUPPORTED_PROFILES


GRAMMAR_PATH = Path(__file__).resolve().with_name("grammar.tx")


def parse_candidate_profile(text: str):
    """Return the textX model for a syntactically valid candidate profile.

    Load grammar.tx on each call so grammar updates take effect immediately.
    Invalid syntax raises textx.TextXSyntaxError with line/column information.
    This does not check profile names, skill vocabulary, or evaluation accuracy.
    """
    if not isinstance(text, str):
        raise TypeError("Candidate profile input must be a string.")
    metamodel = metamodel_from_file(str(GRAMMAR_PATH))
    # Decode quoted literals consistently, including escaped slashes/newlines.
    # literal_eval parses literals only; it does not execute candidate text.
    metamodel.register_obj_processors({"STRING": ast.literal_eval})
    return metamodel.model_from_str(text)


def _check_text(value, field):
    """Require a nonempty string without altering its contents."""
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string.")
    if not value.strip():
        raise ValueError(f"{field} must not be empty.")


def validate_candidate_profile(text: str):
    """Parse and validate a complete profile for presentation.

    Require each supported profile exactly once and unique uppercase skill IDs.
    Status values are syntax-checked, not recomputed against the candidate's skills.
    """
    model = parse_candidate_profile(text)
    profiles = [entry.evaluated_profile for entry in model.evaluations]
    if len(profiles) != len(set(profiles)):
        raise ValueError("Evaluation profiles must not be repeated.")
    if set(profiles) != set(SUPPORTED_PROFILES):
        raise ValueError("Evaluations must contain exactly the four supported profiles.")

    skills = [entry.name for entry in model.skills]
    if any(re.fullmatch(r"[A-Z][A-Z0-9_]*", skill) is None for skill in skills):
        raise ValueError("Normalized skills must be uppercase identifiers.")
    if len(skills) != len(set(skills)):
        raise ValueError("Normalized skills must not be repeated.")

    for entries, attribute in [(model.emails, "email"), (model.phones, "phone"),
                               (model.education, "degree"), (model.experiences, "duration")]:
        for entry in entries:
            _check_text(getattr(entry, attribute), attribute)
    return model


def generate_candidate_profile(
    extracted: dict,
    normalized_skills: list[str],
    evaluations: dict[str, bool],
    personal_info: dict | None = None,
) -> str:
    """Build and validate DSL text from stages 1-3 and optional personal data.

    Missing extraction fields become empty lists. Personal keys are name,
    current_role, location and summary; absent/None values are omitted.
    Evaluation values must be actual bools. No input is modified or inferred.
    """
    if not isinstance(extracted, dict) or not isinstance(evaluations, dict):
        raise TypeError("Extraction and evaluation inputs must be dictionaries.")
    if not isinstance(normalized_skills, list):
        raise TypeError("Normalized skills must be a list of strings.")
    if set(evaluations) != set(SUPPORTED_PROFILES):
        raise ValueError("Provide results for exactly the four supported profiles.")
    if any(type(value) is not bool for value in evaluations.values()):
        raise TypeError("Each evaluation result must be True or False.")
    if personal_info is None:
        personal_info = {}
    if not isinstance(personal_info, dict):
        raise TypeError("Personal information must be a dictionary.")

    personal_labels = {"name": "CANDIDATE:", "current_role": "ROLE:",
                       "location": "LOCATION:", "summary": "SUMMARY:"}
    if set(personal_info) - set(personal_labels):
        raise ValueError("Unknown personal information field.")
    lines = []
    for key, label in personal_labels.items():
        value = personal_info.get(key)
        if value is not None:
            _check_text(value, key)
            lines.append(f"{label} {json.dumps(value, ensure_ascii=False)}")

    lines.append("CONTACT:")
    for key, label, section in [
        ("emails", "Email:", None), ("phones", "Phone:", None),
        ("education", "-", "EDUCATION:"), ("experience", "-", "EXPERIENCE:"),
    ]:
        if section:
            lines.append(section)
        values = extracted.get(key, [])
        if not isinstance(values, list):
            raise TypeError(f"{key} must be a list of strings.")
        for value in values:
            _check_text(value, key)
            lines.append(f"{label} {json.dumps(value, ensure_ascii=False)}")

    lines.append("NORMALIZED_SKILLS:")
    for skill in normalized_skills:
        _check_text(skill, "skill")
        if re.fullmatch(r"[A-Z][A-Z0-9_]*", skill) is None:
            raise ValueError("Normalized skills must be uppercase identifiers.")
        lines.append(f"- {skill}")
    lines.append("EVALUATION:")
    for profile in SUPPORTED_PROFILES:
        lines.append(f'- Profile evaluated: "{profile}"')
        status = "ACCEPTED" if evaluations[profile] else "REJECTED"
        lines.append(f"Qualification pattern: {status}")
    text = "\n".join(lines) + "\n"
    validate_candidate_profile(text)
    return text


def candidate_profile_to_dict(text: str) -> dict:
    """Validate DSL before exposing plain data to an HTML renderer.

    Strings remain raw text. The renderer must HTML-escape them on insertion.
    Missing personal fields become None; repeated data remains in ordered lists.
    """
    model = validate_candidate_profile(text)
    return {
        "name": model.name or None,
        "current_role": model.current_role or None,
        "location": model.location or None,
        "summary": model.summary or None,
        "emails": [entry.email for entry in model.emails],
        "phones": [entry.phone for entry in model.phones],
        "education": [entry.degree for entry in model.education],
        "experience": [entry.duration for entry in model.experiences],
        "skills": [entry.name for entry in model.skills],
        "evaluations": [
            {"profile": entry.evaluated_profile, "status": entry.status}
            for entry in model.evaluations
        ],
    }
