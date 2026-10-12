"""Regression tests for information lost between extraction and classification."""
from copy import deepcopy

import pytest

from src.normalization.transducers import FST_SKILLS, normalizar_skills


@pytest.mark.parametrize("raw,expected", [
    ("js", "JAVASCRIPT"), ("tYpEsCrIpT", "TYPESCRIPT"),
    ("react.js", "REACT"), ("nodejs", "NODE_JS"), ("postgres", "POSTGRESQL"),
    ("Spring  Boot", "SPRING_BOOT"), ("REST\t API", "REST_API"),
    ("RESTful APIs", "REST_API"), ("No\tSQL", "NOSQL"),
    ("machine learning model development", "MACHINE_LEARNING"),
    ("Machine-learning model development", "MACHINE_LEARNING"),
    ("Java", "JAVA"), ("MySQL", "MYSQL"), ("MongoDB", "MONGODB"),
    ("Amazon  Web\tServices", "AWS"), ("Google Cloud Platform", "GCP"),
    ("github\t actions", "GITHUB_ACTIONS"), ("JENKINS", "JENKINS"),
])
def test_fst_normalizes_complete_aliases(raw, expected):
    assert {"".join(value) for value in FST_SKILLS.translate(raw)} == {expected}


@pytest.mark.parametrize("raw", ["", "Rust", "JavaExtra", "React.jsExtra", "REST\nAPI", "JS Git"])
def test_fst_does_not_accept_unknown_or_partial_terms(raw):
    assert list(FST_SKILLS.translate(raw)) == []


def test_normalization_deduplicates_without_mutating_extraction():
    raw = {"programming_languages": ["JS", "js"], "tools": ["Git", "git"],
           "education": ["Python"], "emails": ["person@example.com"]}
    original = deepcopy(raw)
    assert normalizar_skills(raw) == ["GIT", "JAVASCRIPT"]
    assert raw == original
