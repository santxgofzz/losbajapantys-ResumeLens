"""Syntax tests for the agreed candidate-profile grammar."""

from pathlib import Path
import unittest

from textx import TextXSyntaxError
from src.dsl import candidate_parser


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


if __name__ == "__main__":
    unittest.main()
