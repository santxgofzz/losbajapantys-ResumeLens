from src.main import process_resume


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