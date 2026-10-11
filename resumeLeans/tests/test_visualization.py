from src.dsl.visualizer import generate_candidate_html


VALID_DSL = """
CANDIDATE: "Test Candidate"
ROLE: "Software Developer"
LOCATION: "Cali"
SUMMARY: "Candidate used for visualization testing."
CONTACT:
Email: "candidate@example.com"
Phone: "+57 300 123 4567"
EDUCATION:
- "Bachelor's degree in Systems Engineering"
EXPERIENCE:
- "3 years of experience"
NORMALIZED_SKILLS:
- JAVASCRIPT
- REACT
- NODE_JS
- POSTGRESQL
- REST_API
- GIT
EVALUATION:
- Profile evaluated: "FULL_STACK_DEVELOPER"
Qualification pattern: ACCEPTED
- Profile evaluated: "MACHINE_LEARNING_ENGINEER"
Qualification pattern: REJECTED
- Profile evaluated: "DEVOPS_ENGINEER"
Qualification pattern: REJECTED
- Profile evaluated: "DATA_ENGINEER"
Qualification pattern: REJECTED
"""


def test_html_contains_candidate_information():
    html = generate_candidate_html(VALID_DSL)

    assert "Test Candidate" in html
    assert "candidate@example.com" in html
    assert "JAVASCRIPT" in html
    assert "Full Stack Developer" in html
    assert "ACCEPTED" in html


def test_html_escapes_candidate_text():
    dangerous_dsl = VALID_DSL.replace(
        '"Test Candidate"',
        '"<script>alert(1)</script>"',
    )

    html = generate_candidate_html(dangerous_dsl)

    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html