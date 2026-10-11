"""Syntax tests for the agreed candidate-profile grammar."""

from pathlib import Path
import unittest

from textx import TextXSyntaxError
from src.dsl import candidate_parser
from src.automata.profile_definitions import SUPPORTED_PROFILES


MINIMAL_PROFILE = "CONTACT: EDUCATION: EXPERIENCE: NORMALIZED_SKILLS: EVALUATION:"


class CandidateParserTests(unittest.TestCase):
    def test_repeated_fields_from_example(self):
        path = Path(__file__).resolve().parents[1] / "data" / "candidate_example.dsl"
        model = candidate_parser.parse_candidate_profile(path.read_text(encoding="utf-8"))
        self.assertEqual(model.name, "Example Candidate")
        self.assertEqual([x.email for x in model.emails], ["candidate@example.com", "candidate@example.org"])
        self.assertEqual([x.phone for x in model.phones], ["+57 300 123 4567", "+57 601 234 5678"])
        self.assertEqual([x.degree for x in model.education],
                         ["Bachelor's degree in Systems Engineering", "Master's degree in Computer Science"])
        self.assertEqual([x.duration for x in model.experiences],
                         ["3 years of experience", "6 months of work experience"])
        self.assertEqual([x.name for x in model.skills],
                         ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "REST_API", "GIT"])
        self.assertEqual([x.status for x in model.evaluations], ["ACCEPTED", "REJECTED", "REJECTED", "REJECTED"])

    def test_optional_fields_and_empty_lists(self):
        model = candidate_parser.parse_candidate_profile(MINIMAL_PROFILE)
        for field in ["emails", "phones", "education", "experiences", "skills", "evaluations"]:
            self.assertEqual(getattr(model, field), [])

    def test_invalid_syntax_reports_location(self):
        invalid = [
            "", MINIMAL_PROFILE.replace("EDUCATION:", ""),
            'CANDIDATE: "Unclosed\n' + MINIMAL_PROFILE,
            MINIMAL_PROFILE + '\n- Profile evaluated: "FULL_STACK_DEVELOPER"\nQualification pattern: MAYBE',
            MINIMAL_PROFILE + "\nUNKNOWN: value",
            MINIMAL_PROFILE.replace("NORMALIZED_SKILLS:", "NORMALIZED_SKILLS: - 123BAD"),
        ]
        for text in invalid:
            with self.subTest(text=text), self.assertRaises(TextXSyntaxError) as caught:
                candidate_parser.parse_candidate_profile(text)
            self.assertIsNotNone(caught.exception.line)
            self.assertIsNotNone(caught.exception.col)

    def test_rejects_non_text_input(self):
        with self.assertRaises(TypeError):
            candidate_parser.parse_candidate_profile(None)


class CandidatePipelineTests(unittest.TestCase):
    def setUp(self):
        self.extracted = {
            "emails": ["a@example.com", "b@example.org"],
            "phones": ["+57 300 123 4567"],
            "education": ["Bachelor's degree in Systems Engineering", "PhD in Data Science"],
            "experience": ["3 years of experience", "6 months experience"],
            "programming_languages": ["JS"],
        }
        self.evaluations = {name: False for name in SUPPORTED_PROFILES}
        self.evaluations["FULL_STACK_DEVELOPER"] = True

    def test_generation_validation_and_html_dictionary(self):
        text = candidate_parser.generate_candidate_profile(
            self.extracted, ["JAVASCRIPT", "REACT"], self.evaluations,
            {"name": "Ana", "location": "Cali"},
        )
        result = candidate_parser.candidate_profile_to_dict(text)
        self.assertEqual(result, {
            "name": "Ana", "current_role": None, "location": "Cali", "summary": None,
            "emails": ["a@example.com", "b@example.org"], "phones": ["+57 300 123 4567"],
            "education": ["Bachelor's degree in Systems Engineering", "PhD in Data Science"],
            "experience": ["3 years of experience", "6 months experience"],
            "skills": ["JAVASCRIPT", "REACT"],
            "evaluations": [
                {"profile": "FULL_STACK_DEVELOPER", "status": "ACCEPTED"},
                {"profile": "MACHINE_LEARNING_ENGINEER", "status": "REJECTED"},
                {"profile": "DEVOPS_ENGINEER", "status": "REJECTED"},
                {"profile": "DATA_ENGINEER", "status": "REJECTED"},
            ],
        })
        self.assertEqual(self.extracted["programming_languages"], ["JS"])

    def test_missing_optional_information_stays_absent(self):
        text = candidate_parser.generate_candidate_profile({}, [], self.evaluations)
        self.assertNotIn("CANDIDATE:", text)
        result = candidate_parser.candidate_profile_to_dict(text)
        self.assertIsNone(result["name"])
        self.assertEqual(result["education"], [])
        self.assertEqual(result["skills"], [])

    def test_quotes_backslashes_unicode_and_newlines_round_trip(self):
        name = 'Ana "María" \\ test'
        summary = 'First line\nSecond\tline <script>alert("x")</script>'
        text = candidate_parser.generate_candidate_profile({}, [], self.evaluations,
                                                          {"name": name, "summary": summary})
        result = candidate_parser.candidate_profile_to_dict(text)
        self.assertEqual(result["name"], name)
        self.assertEqual(result["summary"], summary)

    def test_rejects_invalid_evaluation_inputs(self):
        for values in [{}, {**self.evaluations, "UNKNOWN": True},
                       {**self.evaluations, "FULL_STACK_DEVELOPER": "False"},
                       {**self.evaluations, "FULL_STACK_DEVELOPER": 1}]:
            with self.subTest(values=values), self.assertRaises((ValueError, TypeError)):
                candidate_parser.generate_candidate_profile({}, [], values)

    def test_semantic_validation_rejects_missing_duplicate_and_unknown_profiles(self):
        text = candidate_parser.generate_candidate_profile({}, [], self.evaluations)
        invalid = [MINIMAL_PROFILE,
                   text.replace('"DATA_ENGINEER"', '"UNKNOWN"'),
                   text.replace('"DATA_ENGINEER"', '"DEVOPS_ENGINEER"')]
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(ValueError):
                candidate_parser.candidate_profile_to_dict(value)

    def test_rejects_invalid_skills_and_input_shapes(self):
        for skills in [["JS", "JS"], ["python"], ["BAD-TOKEN"], [42], "PYTHON"]:
            with self.subTest(skills=skills), self.assertRaises((ValueError, TypeError)):
                candidate_parser.generate_candidate_profile({}, skills, self.evaluations)
        for extracted in [{"emails": "a@example.com"}, {"education": [3]}, {"phones": [""]}]:
            with self.subTest(extracted=extracted), self.assertRaises((ValueError, TypeError)):
                candidate_parser.generate_candidate_profile(extracted, [], self.evaluations)

    def test_handwritten_dsl_also_checks_skills(self):
        text = candidate_parser.generate_candidate_profile({}, ["PYTHON"], self.evaluations)
        for value in [text.replace("- PYTHON", "- python"),
                      text.replace("- PYTHON", "- PYTHON\n- PYTHON")]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                candidate_parser.validate_candidate_profile(value)


if __name__ == "__main__":
    unittest.main()
