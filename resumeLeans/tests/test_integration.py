from src.main import process_resume
from src.dsl.candidate_parser import candidate_profile_to_dict
from src.dsl.visualizer import generate_candidate_html
import pytest


@pytest.mark.parametrize("profile,terms", [
    ("FULL_STACK_DEVELOPER", ["js", "react.js", "Spring  Boot", "postgres", "RESTful APIs", "git"]),
    ("MACHINE_LEARNING_ENGINEER", ["PYTHON", "NUMPY", "scikit-learn", "sql", "git"]),
    ("DEVOPS_ENGINEER", ["linux", "docker", "k8s", "CI/CD", "Amazon  Web Services", "terraform", "git"]),
    ("DEVOPS_ENGINEER", ["linux", "docker", "k8s", "jenkins", "Google Cloud Platform", "terraform", "git"]),
    ("DEVOPS_ENGINEER", ["linux", "docker", "k8s", "github actions", "azure", "terraform", "git"]),
    ("DEVOPS_ENGINEER", ["linux", "docker", "k8s", "gitlab ci", "aws", "terraform", "git"]),
    ("DATA_ENGINEER", ["python", "sql", "etl", "spark", "airflow", "data warehouse", "git"]),
])
def test_profiles_through_dsl_and_html_and_missing_requirements(profile, terms):
    _, skills, evaluations, dsl = process_resume(", ".join(reversed(terms)))
    assert evaluations[profile] is True
    data = candidate_profile_to_dict(dsl)
    assert data["skills"] == skills
    assert {"profile": profile, "status": "ACCEPTED"} in data["evaluations"]
    assert profile in generate_candidate_html(dsl)
    for missing in range(len(terms)):
        _, _, evaluations, _ = process_resume(", ".join(terms[:missing] + terms[missing + 1:]))
        assert evaluations[profile] is False, (profile, terms[missing])


def test_complete_resume_pipeline():
    resume = """
    Alex Smith

    Email: alex@example.com
    Phone: +57 300 123 4567

    Bachelor's degree in Systems Engineering.

    3 years of experience developing web applications.

    Technical Skills:
    JS, React.js, NodeJS, Postgres, REST API, Git.
    """

    personal_info = {
        "name": "Alex Smith",
        "current_role": "Software Developer",
        "location": "Cali",
        "summary": "Example candidate used for integration testing.",
    }

    (
        extracted,
        normalized_skills,
        evaluations,
        dsl_text,
    ) = process_resume(
        resume,
        personal_info,
    )

    assert "JS" in extracted["programming_languages"]
    assert "JAVASCRIPT" in normalized_skills
    assert "REACT" in normalized_skills
    assert "NODE_JS" in normalized_skills
    assert "POSTGRESQL" in normalized_skills
    assert "REST_API" in normalized_skills
    assert "GIT" in normalized_skills

    assert evaluations["FULL_STACK_DEVELOPER"] is True

    assert 'CANDIDATE: "Alex Smith"' in dsl_text
    assert "FULL_STACK_DEVELOPER" in dsl_text
    assert "Qualification pattern: ACCEPTED" in dsl_text
