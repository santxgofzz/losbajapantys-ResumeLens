"""Finite automata used to classify normalized résumé qualifications."""

from collections.abc import Iterable

from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    State,
    Symbol,
)

from src.automata.profile_definitions import (
    prepare_qualifications_for_profile,
)


FULL_STACK_PROFILE = "FULL_STACK_DEVELOPER"
MACHINE_LEARNING_PROFILE = "MACHINE_LEARNING_ENGINEER"


def build_full_stack_automaton() -> DeterministicFiniteAutomaton:
    """
    Build the deterministic finite automaton for the Full Stack Developer profile.

    Expected qualification categories, in canonical order:

    programming language
        -> frontend
        -> backend
        -> database
        -> REST API
        -> version control
    """

    automaton = DeterministicFiniteAutomaton()

    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")
    q4 = State("q4")
    q5 = State("q5")
    q6 = State("q6")

    automaton.add_start_state(q0)
    automaton.add_final_state(q6)

    programming_languages = (
        "JAVASCRIPT",
        "TYPESCRIPT",
    )

    frontend_technologies = (
        "REACT",
        "ANGULAR",
        "VUE",
    )

    backend_technologies = (
        "NODE_JS",
        "DJANGO",
        "SPRING_BOOT",
    )

    databases = (
        "SQL",
        "POSTGRESQL",
        "NOSQL",
    )

    # q0 -> q1:
    # At least one programming language is required.
    for qualification in programming_languages:
        automaton.add_transition(
            q0,
            Symbol(qualification),
            q1,
        )

        # More than one programming language is allowed.
        automaton.add_transition(
            q1,
            Symbol(qualification),
            q1,
        )

    # q1 -> q2:
    # At least one frontend technology is required.
    for qualification in frontend_technologies:
        automaton.add_transition(
            q1,
            Symbol(qualification),
            q2,
        )

        # More than one frontend technology is allowed.
        automaton.add_transition(
            q2,
            Symbol(qualification),
            q2,
        )

    # q2 -> q3:
    # At least one backend technology is required.
    for qualification in backend_technologies:
        automaton.add_transition(
            q2,
            Symbol(qualification),
            q3,
        )

        # More than one backend technology is allowed.
        automaton.add_transition(
            q3,
            Symbol(qualification),
            q3,
        )

    # q3 -> q4:
    # At least one database technology is required.
    for qualification in databases:
        automaton.add_transition(
            q3,
            Symbol(qualification),
            q4,
        )

        # More than one database technology is allowed.
        automaton.add_transition(
            q4,
            Symbol(qualification),
            q4,
        )

    # REST API is required.
    automaton.add_transition(
        q4,
        Symbol("REST_API"),
        q5,
    )

    # Git completes the accepted qualification pattern.
    automaton.add_transition(
        q5,
        Symbol("GIT"),
        q6,
    )

    return automaton


def is_full_stack_developer(
    qualifications: Iterable[str],
) -> bool:
    """
    Return True if the normalized qualifications satisfy the
    Full Stack Developer qualification pattern.
    """

    prepared_qualifications = prepare_qualifications_for_profile(
        qualifications,
        FULL_STACK_PROFILE,
    )

    automaton = build_full_stack_automaton()

    return automaton.accepts(prepared_qualifications)

def build_machine_learning_automaton() -> DeterministicFiniteAutomaton:
    """
    Build the deterministic finite automaton for the
    Machine Learning Engineer profile.

    Expected qualification categories, in canonical order:

    Python
        -> data-processing library
        -> machine-learning technology
        -> database
        -> version control
    """

    automaton = DeterministicFiniteAutomaton()

    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")
    q4 = State("q4")
    q5 = State("q5")

    automaton.add_start_state(q0)
    automaton.add_final_state(q5)

    data_processing_libraries = (
        "PANDAS",
        "NUMPY",
    )

    machine_learning_technologies = (
        "SCIKIT_LEARN",
        "TENSORFLOW",
        "PYTORCH",
    )

    databases = (
        "SQL",
        "POSTGRESQL",
    )

    # Python is required as the programming language.
    automaton.add_transition(
        q0,
        Symbol("PYTHON"),
        q1,
    )

    # q1 -> q2:
    # At least one data-processing library is required.
    for qualification in data_processing_libraries:
        automaton.add_transition(
            q1,
            Symbol(qualification),
            q2,
        )

        # More than one data-processing library is allowed.
        automaton.add_transition(
            q2,
            Symbol(qualification),
            q2,
        )

    # q2 -> q3:
    # At least one machine-learning technology is required.
    for qualification in machine_learning_technologies:
        automaton.add_transition(
            q2,
            Symbol(qualification),
            q3,
        )

        # More than one machine-learning technology is allowed.
        automaton.add_transition(
            q3,
            Symbol(qualification),
            q3,
        )

    # q3 -> q4:
    # At least one database technology is required.
    for qualification in databases:
        automaton.add_transition(
            q3,
            Symbol(qualification),
            q4,
        )

        # More than one database technology is allowed.
        automaton.add_transition(
            q4,
            Symbol(qualification),
            q4,
        )

    # Git completes the accepted qualification pattern.
    automaton.add_transition(
        q4,
        Symbol("GIT"),
        q5,
    )

    return automaton


def is_machine_learning_engineer(
    qualifications: Iterable[str],
) -> bool:
    """
    Return True if the normalized qualifications satisfy the
    Machine Learning Engineer qualification pattern.
    """

    prepared_qualifications = prepare_qualifications_for_profile(
        qualifications,
        MACHINE_LEARNING_PROFILE,
    )

    automaton = build_machine_learning_automaton()

    return automaton.accepts(prepared_qualifications)