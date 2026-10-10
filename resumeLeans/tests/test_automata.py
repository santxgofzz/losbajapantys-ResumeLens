import pytest

from src.automata.classifiers import (
    is_data_engineer,
    is_devops_engineer,
    is_full_stack_developer,
    is_machine_learning_engineer,
)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "JAVASCRIPT",
            "REACT",
            "NODE_JS",
            "POSTGRESQL",
            "REST_API",
            "GIT",
        ],
        [
            "TYPESCRIPT",
            "ANGULAR",
            "DJANGO",
            "SQL",
            "REST_API",
            "GIT",
        ],
        [
            "JAVASCRIPT",
            "TYPESCRIPT",
            "REACT",
            "VUE",
            "SPRING_BOOT",
            "NOSQL",
            "REST_API",
            "GIT",
        ],
    ],
)
def test_full_stack_accepts_valid_qualification_patterns(qualifications):
    assert is_full_stack_developer(qualifications)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "JAVASCRIPT",
            "REACT",
            "POSTGRESQL",
            "REST_API",
            "GIT",
        ],
        [
            "JAVASCRIPT",
            "NODE_JS",
            "POSTGRESQL",
            "REST_API",
            "GIT",
        ],
        [
            "JAVASCRIPT",
            "REACT",
            "NODE_JS",
            "POSTGRESQL",
            "GIT",
        ],
    ],
)
def test_full_stack_rejects_incomplete_qualification_patterns(qualifications):
    assert not is_full_stack_developer(qualifications)


def test_full_stack_ignores_unrelated_qualifications_and_input_order():
    qualifications = [
        "GIT",
        "DOCKER",
        "POSTGRESQL",
        "NODE_JS",
        "REACT",
        "REST_API",
        "JAVASCRIPT",
        "PYTHON",
    ]

    assert is_full_stack_developer(qualifications)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "PYTHON",
            "PANDAS",
            "TENSORFLOW",
            "SQL",
            "GIT",
        ],
        [
            "PYTHON",
            "NUMPY",
            "SCIKIT_LEARN",
            "POSTGRESQL",
            "GIT",
        ],
        [
            "PYTHON",
            "PANDAS",
            "NUMPY",
            "TENSORFLOW",
            "PYTORCH",
            "SQL",
            "GIT",
        ],
    ],
)
def test_machine_learning_accepts_valid_qualification_patterns(qualifications):
    assert is_machine_learning_engineer(qualifications)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "PANDAS",
            "TENSORFLOW",
            "SQL",
            "GIT",
        ],
        [
            "PYTHON",
            "PANDAS",
            "SQL",
            "GIT",
        ],
        [
            "PYTHON",
            "TENSORFLOW",
            "SQL",
            "GIT",
        ],
    ],
)
def test_machine_learning_rejects_incomplete_qualification_patterns(
    qualifications,
):
    assert not is_machine_learning_engineer(qualifications)


def test_machine_learning_ignores_unrelated_qualifications_and_input_order():
    qualifications = [
        "GIT",
        "DOCKER",
        "PYTORCH",
        "POSTGRESQL",
        "PYTHON",
        "REACT",
        "NUMPY",
    ]

    assert is_machine_learning_engineer(qualifications)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "LINUX",
            "DOCKER",
            "KUBERNETES",
            "GITHUB_ACTIONS",
            "AWS",
            "TERRAFORM",
            "GIT",
        ],
        [
            "LINUX",
            "DOCKER",
            "KUBERNETES",
            "JENKINS",
            "AZURE",
            "TERRAFORM",
            "GIT",
        ],
        [
            "LINUX",
            "DOCKER",
            "KUBERNETES",
            "GITLAB_CI",
            "GCP",
            "TERRAFORM",
            "GIT",
        ],
    ],
)
def test_devops_accepts_valid_qualification_patterns(qualifications):
    assert is_devops_engineer(qualifications)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "LINUX",
            "DOCKER",
            "GITHUB_ACTIONS",
            "AWS",
            "TERRAFORM",
            "GIT",
        ],
        [
            "LINUX",
            "KUBERNETES",
            "GITHUB_ACTIONS",
            "AWS",
            "TERRAFORM",
            "GIT",
        ],
        [
            "LINUX",
            "DOCKER",
            "KUBERNETES",
            "GITHUB_ACTIONS",
            "TERRAFORM",
            "GIT",
        ],
    ],
)
def test_devops_rejects_incomplete_qualification_patterns(qualifications):
    assert not is_devops_engineer(qualifications)


def test_devops_accepts_multiple_tools_and_ignores_unrelated_qualifications():
    qualifications = [
        "GIT",
        "AWS",
        "REACT",
        "GITHUB_ACTIONS",
        "LINUX",
        "DOCKER",
        "AZURE",
        "KUBERNETES",
        "TERRAFORM",
        "JENKINS",
    ]

    assert is_devops_engineer(qualifications)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "PYTHON",
            "SQL",
            "ETL",
            "SPARK",
            "AIRFLOW",
            "DATA_WAREHOUSE",
            "GIT",
        ],
        [
            "PYTHON",
            "POSTGRESQL",
            "ETL",
            "KAFKA",
            "AIRFLOW",
            "DATA_WAREHOUSE",
            "GIT",
        ],
        [
            "PYTHON",
            "SQL",
            "POSTGRESQL",
            "ETL",
            "SPARK",
            "KAFKA",
            "AIRFLOW",
            "DATA_WAREHOUSE",
            "GIT",
        ],
    ],
)
def test_data_engineer_accepts_valid_qualification_patterns(qualifications):
    assert is_data_engineer(qualifications)


@pytest.mark.parametrize(
    "qualifications",
    [
        [
            "PYTHON",
            "SQL",
            "SPARK",
            "AIRFLOW",
            "DATA_WAREHOUSE",
            "GIT",
        ],
        [
            "PYTHON",
            "SQL",
            "ETL",
            "AIRFLOW",
            "DATA_WAREHOUSE",
            "GIT",
        ],
        [
            "PYTHON",
            "SQL",
            "ETL",
            "SPARK",
            "DATA_WAREHOUSE",
            "GIT",
        ],
    ],
)
def test_data_engineer_rejects_incomplete_qualification_patterns(
    qualifications,
):
    assert not is_data_engineer(qualifications)


def test_data_engineer_ignores_unrelated_qualifications_and_input_order():
    qualifications = [
        "GIT",
        "DOCKER",
        "AIRFLOW",
        "SPARK",
        "PYTHON",
        "POSTGRESQL",
        "DATA_WAREHOUSE",
        "REACT",
        "ETL",
    ]

    assert is_data_engineer(qualifications)