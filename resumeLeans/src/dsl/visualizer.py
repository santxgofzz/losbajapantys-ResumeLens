"""Generate HTML visualizations from validated ResumeLens candidate profiles."""

from html import escape
from pathlib import Path

from src.dsl.candidate_parser import candidate_profile_to_dict


PROFILE_LABELS = {
    "FULL_STACK_DEVELOPER": "Full Stack Developer",
    "MACHINE_LEARNING_ENGINEER": "Machine Learning Engineer",
    "DEVOPS_ENGINEER": "DevOps Engineer",
    "DATA_ENGINEER": "Data Engineer",
}


def _render_list(items: list[str], empty_message: str) -> str:
    """Render a list of escaped text values."""

    if not items:
        return f'<p class="empty">{escape(empty_message)}</p>'

    rendered_items = "\n".join(
        f"<li>{escape(item)}</li>"
        for item in items
    )

    return f"<ul>\n{rendered_items}\n</ul>"


def _render_skills(skills: list[str]) -> str:
    """Render normalized skills as visual tags."""

    if not skills:
        return '<p class="empty">No normalized skills available.</p>'

    return "\n".join(
        f'<span class="skill">{escape(skill)}</span>'
        for skill in skills
    )


def _render_evaluations(evaluations: list[dict]) -> str:
    """Render classification results for the supported profiles."""

    rows = []

    for evaluation in evaluations:
        profile = evaluation["profile"]
        status = evaluation["status"]

        profile_label = PROFILE_LABELS.get(
            profile,
            profile.replace("_", " ").title(),
        )

        status_class = (
            "accepted"
            if status == "ACCEPTED"
            else "rejected"
        )

        rows.append(
            f"""
            <div class="evaluation-card">
                <div>
                    <p class="evaluation-profile">
                        {escape(profile_label)}
                    </p>
                    <p class="evaluation-code">
                        {escape(profile)}
                    </p>
                </div>

                <span class="status {status_class}">
                    {escape(status)}
                </span>
            </div>
            """
        )

    return "\n".join(rows)


def generate_candidate_html(dsl_text: str) -> str:
    """
    Validate candidate-profile DSL text and generate an HTML visualization.

    The DSL is validated before rendering. All candidate-provided text is
    HTML-escaped before insertion into the generated document.
    """

    data = candidate_profile_to_dict(dsl_text)

    name = escape(data["name"] or "Candidate")
    current_role = escape(data["current_role"] or "Not specified")
    location = escape(data["location"] or "Not specified")
    summary = escape(data["summary"] or "No summary available.")

    emails = _render_list(
        data["emails"],
        "No email addresses available.",
    )

    phones = _render_list(
        data["phones"],
        "No phone numbers available.",
    )

    education = _render_list(
        data["education"],
        "No education information available.",
    )

    experience = _render_list(
        data["experience"],
        "No professional experience available.",
    )

    skills = _render_skills(data["skills"])

    evaluations = _render_evaluations(
        data["evaluations"],
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>ResumeLens - {name}</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }}

        .page {{
            width: 700px;
            margin: 30px auto;
        }}

        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .brand {{
            font-size: 14px;
        }}

        h1 {{
            margin-bottom: 5px;
        }}

        .role,
        .location {{
            margin: 5px 0;
        }}

        .summary {{
            margin-top: 15px;
        }}

        .grid {{
            display: block;
        }}

        .card {{
            margin-bottom: 25px;
        }}

        h2 {{
            font-size: 20px;
            margin-bottom: 10px;
        }}

        h3 {{
            font-size: 16px;
            margin-bottom: 5px;
        }}

        ul {{
            margin-top: 5px;
        }}

        .empty {{
            color: gray;
        }}

        .skills {{
            margin-top: 10px;
        }}

        .skill {{
            display: block;
            margin-bottom: 5px;
        }}

        .evaluation-card {{
            margin-bottom: 15px;
        }}

        .evaluation-profile {{
            font-weight: bold;
            margin-bottom: 3px;
        }}

        .evaluation-code {{
            margin: 0;
            font-size: 12px;
        }}

        .status {{
            display: block;
            margin-top: 4px;
            font-weight: bold;
        }}

        .accepted {{
            color: green;
        }}

        .rejected {{
            color: red;
        }}

        .footer {{
            text-align: center;
            margin-top: 40px;
            font-size: 12px;
        }}
    </style>
    
</head>

<body>
    <main class="page">

        <header class="header">
            <p class="brand">
                ResumeLens Candidate Profile
            </p>

            <h1>{name}</h1>

            <p class="role">
                {current_role}
            </p>

            <p class="location">
                {location}
            </p>

            <p class="summary">
                {summary}
            </p>
        </header>

        <section class="grid">

            <article class="card">
                <h2>Contact</h2>

                <h3>Email</h3>
                {emails}

                <h3>Phone</h3>
                {phones}
            </article>

            <article class="card">
                <h2>Education</h2>
                {education}
            </article>

            <article class="card full">
                <h2>Professional Experience</h2>
                {experience}
            </article>

            <article class="card full">
                <h2>Normalized Skills</h2>

                <div class="skills">
                    {skills}
                </div>
            </article>

            <article class="card full">
                <h2>Profile Classification</h2>

                <div class="evaluations">
                    {evaluations}
                </div>
            </article>

        </section>

        <footer class="footer">
            Generated by ResumeLens
        </footer>

    </main>
</body>
</html>
"""


def save_candidate_html(
    dsl_text: str,
    output_path: str | Path,
) -> Path:
    """
    Generate and save the candidate HTML visualization.

    Parent directories are created automatically when necessary.
    """

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    html_content = generate_candidate_html(dsl_text)

    output_path.write_text(
        html_content,
        encoding="utf-8",
    )

    return output_path