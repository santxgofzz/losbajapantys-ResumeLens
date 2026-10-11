"""Main entry point for ResumeLens."""

from pathlib import Path

from src.extraction.regex_extractor import extract_resume_info
from src.normalization.transducers import normalizar_skills
from src.automata.classifiers import (
    is_full_stack_developer,
    is_machine_learning_engineer,
    is_devops_engineer,
    is_data_engineer,
)
from src.dsl.candidate_parser import generate_candidate_profile
from src.dsl.visualizer import save_candidate_html


BASE_DIR = Path(__file__).resolve().parents[1]

DEFAULT_RESUME_PATH = BASE_DIR / "data" / "resume_example.txt"
DEFAULT_DSL_OUTPUT = BASE_DIR / "output" / "candidate_profile.dsl"
DEFAULT_HTML_OUTPUT = BASE_DIR / "output" / "candidate_profile.html"


def classify_profiles(normalized_skills: list[str]) -> dict[str, bool]:
    """Evaluate normalized skills against the four supported profiles."""

    return {
        "FULL_STACK_DEVELOPER": is_full_stack_developer(normalized_skills),
        "MACHINE_LEARNING_ENGINEER": is_machine_learning_engineer(
            normalized_skills
        ),
        "DEVOPS_ENGINEER": is_devops_engineer(normalized_skills),
        "DATA_ENGINEER": is_data_engineer(normalized_skills),
    }


def process_resume(
    resume_text: str,
    personal_info: dict | None = None,
) -> tuple[dict, list[str], dict[str, bool], str]:
    """
    Run the ResumeLens pipeline from résumé text to validated DSL.

    Returns:
        extracted information,
        normalized qualifications,
        profile evaluations,
        generated DSL text.
    """

    extracted = extract_resume_info(resume_text)

    normalized_skills = normalizar_skills(extracted)

    evaluations = classify_profiles(normalized_skills)

    dsl_text = generate_candidate_profile(
        extracted=extracted,
        normalized_skills=normalized_skills,
        evaluations=evaluations,
        personal_info=personal_info,
    )

    return (
        extracted,
        normalized_skills,
        evaluations,
        dsl_text,
    )


def main():
    """Run ResumeLens using the example résumé included in the project."""

    if not DEFAULT_RESUME_PATH.exists():
        raise FileNotFoundError(
            f"Example résumé not found: {DEFAULT_RESUME_PATH}"
        )

    resume_text = DEFAULT_RESUME_PATH.read_text(
        encoding="utf-8",
    )

    personal_info = {
        "name": "Wednesday Addams",
        "current_role": "Software Developer",
        "location": "Cali",
        "summary": (
            "Candidate processed by ResumeLens using "
            "formal language models."
        ),
    }

    (
        extracted,
        normalized_skills,
        evaluations,
        dsl_text,
    ) = process_resume(
        resume_text,
        personal_info,
    )

    DEFAULT_DSL_OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    DEFAULT_DSL_OUTPUT.write_text(
        dsl_text,
        encoding="utf-8",
    )

    save_candidate_html(
        dsl_text,
        DEFAULT_HTML_OUTPUT,
    )

    print("\n=== ResumeLens ===")

    print("\nExtracted information:")
    for category, values in extracted.items():
        print(f"- {category}: {values}")

    print("\nNormalized skills:")
    for skill in normalized_skills:
        print(f"- {skill}")

    print("\nProfile classification:")
    for profile, accepted in evaluations.items():
        status = "ACCEPTED" if accepted else "REJECTED"
        print(f"- {profile}: {status}")

    print("\nGenerated files:")
    print(f"- DSL: {DEFAULT_DSL_OUTPUT}")
    print(f"- HTML: {DEFAULT_HTML_OUTPUT}")


if __name__ == "__main__":
    main()