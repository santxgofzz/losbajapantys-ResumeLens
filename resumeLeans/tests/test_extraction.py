"""Behavior tests for resume extraction (standard library only)."""

from pathlib import Path
import unittest

from src.extraction import regex_extractor


class ContactExtractionTests(unittest.TestCase):
    def test_email_examples(self):
        cases = [
            ("Contact: <Wednesday.Addams@example.com>.", ["Wednesday.Addams@example.com"]),
            ("first.last+jobs@careers.example.co.uk", ["first.last+jobs@careers.example.co.uk"]),
            ("first_last@my-company.org", ["first_last@my-company.org"]),
            ("Write to\na@example.com, or b@example.org.", ["a@example.com", "b@example.org"]),
            ("", []),
            ("Python and React.js", []),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_emails(text), expected)

    def test_email_preserves_order_case_and_repetitions(self):
        self.assertEqual(
            regex_extractor.extract_emails("B@example.org a@example.com B@example.org"),
            ["B@example.org", "a@example.com", "B@example.org"],
        )

    def test_email_rejects_common_malformed_addresses(self):
        for text in [
            "name@", "@example.com", "name@example", "name@example.c",
            "first..last@example.com", ".name@example.com", "name.@example.com",
            "name@@example.com", "name@-example.com", "name@example-.com",
            "name@exam_ple.com", "name@example..com", "name@example.com123",
        ]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_emails(text), [])

    def test_phone_examples(self):
        for phone in [
            "3001234567", "300 123 4567", "300-123-4567",
            "+573001234567", "+57 300 123 4567", "+57-300-123-4567",
            "6021234567", "602 123 4567", "+57 601 234 5678",
        ]:
            with self.subTest(phone=phone):
                self.assertEqual(regex_extractor.extract_phones(f"Contact: {phone}."), [phone])

    def test_phone_preserves_order_format_and_repetitions(self):
        self.assertEqual(
            regex_extractor.extract_phones("300-123-4567; +57 602 123 4567; 300-123-4567"),
            ["300-123-4567", "+57 602 123 4567", "300-123-4567"],
        )

    def test_phone_in_prose_without_heading(self):
        self.assertEqual(
            regex_extractor.extract_phones("You can reach me at\n300 123 4567."),
            ["300 123 4567"],
        )

    def test_phone_rejects_unsupported_or_embedded_numbers(self):
        for text in [
            "", "3 years of experience", "2023-2026", "300123456",
            "30012345678", "13001234567", "300 123 45678",
            "3001234567 8", "2001234567", "+58 300 123 4567",
            "57 300 123 4567", "ID3001234567", "3001234567abc",
            "300\n123\n4567",
        ]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_phones(text), [])

    def test_sample_resume(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        text = sample.read_text(encoding="utf-8")
        self.assertEqual(regex_extractor.extract_emails(text), ["Wednesday.Addams@example.com"])
        self.assertEqual(regex_extractor.extract_phones(text), ["+57 300 123 4567"])


class ProgrammingLanguageExtractionTests(unittest.TestCase):
    def test_supported_names_and_case_variants(self):
        text = "JavaScript JS javascript js TypeScript TS typescript ts Python PYTHON Java JAVA"
        self.assertEqual(
            regex_extractor.extract_programming_languages(text),
            ["JavaScript", "JS", "javascript", "js", "TypeScript", "TS",
             "typescript", "ts", "Python", "PYTHON", "Java", "JAVA"],
        )

    def test_preserves_order_and_repetitions_in_prose(self):
        self.assertEqual(
            regex_extractor.extract_programming_languages("I use python and JS. I teach python."),
            ["python", "JS", "python"],
        )

    def test_punctuation_and_line_breaks(self):
        self.assertEqual(
            regex_extractor.extract_programming_languages("(JAVA), PYTHON;\nTS/JS."),
            ["JAVA", "PYTHON", "TS", "JS"],
        )

    def test_excludes_longer_words_and_other_categories(self):
        for text in [
            "Pythonista JavaScriptCore Python3 my_python",
            "React.js Node.js NodeJS Postgres Git", "", "No technical skills listed.",
        ]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_programming_languages(text), [])

    def test_sample_resume(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        self.assertEqual(
            regex_extractor.extract_programming_languages(sample.read_text(encoding="utf-8")),
            ["JS"],
        )


class FrameworkExtractionTests(unittest.TestCase):
    def test_web_variants(self):
        self.assertEqual(
            regex_extractor.extract_frameworks(
                "React, React.js, ReactJS, Angular, Vue, Vue.js, NodeJS, Node.js, Django, Spring Boot"
            ),
            ["React", "React.js", "ReactJS", "Angular", "Vue", "Vue.js",
             "NodeJS", "Node.js", "Django", "Spring Boot"],
        )

    def test_data_and_machine_learning_variants(self):
        self.assertEqual(
            regex_extractor.extract_frameworks(
                "Pandas, NumPy, Scikit-learn, sklearn, scikit learn, TensorFlow, Tensor Flow, PyTorch, Py Torch"
            ),
            ["Pandas", "NumPy", "Scikit-learn", "sklearn", "scikit learn",
             "TensorFlow", "Tensor Flow", "PyTorch", "Py Torch"],
        )

    def test_preserves_case_order_and_repetitions_in_prose(self):
        self.assertEqual(
            regex_extractor.extract_frameworks("I use react.js and PANDAS. I also teach react.js."),
            ["react.js", "PANDAS", "react.js"],
        )

    def test_separators_and_sentence_punctuation(self):
        self.assertEqual(
            regex_extractor.extract_frameworks("(Django),\nVue.js/NumPy; Spring Boot."),
            ["Django", "Vue.js", "NumPy", "Spring Boot"],
        )

    def test_rejects_longer_words_and_unlisted_variants(self):
        for text in [
            "Reactive ReactJSExtra Angularity Vue.jsExtra my_Django Pandas2",
            "React.jsx ReactXjs Vue.jsx NodeXjs scikitXlearn",
            "Spring\nBoot Tensor\nFlow Py\nTorch scikit\nlearn",
            "Python JS Postgres Git", "", "No technologies listed.",
        ]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_frameworks(text), [])

    def test_sample_resume(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        self.assertEqual(
            regex_extractor.extract_frameworks(sample.read_text(encoding="utf-8")),
            ["React.js", "NodeJS"],
        )


if __name__ == "__main__":
    unittest.main()
