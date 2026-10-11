"""Parse candidate-profile DSL text using the adjacent textX grammar."""

from pathlib import Path

from textx import metamodel_from_file


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
    return metamodel.model_from_str(text)
