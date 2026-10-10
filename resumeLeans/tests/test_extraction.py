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


class DatabaseExtractionTests(unittest.TestCase):
    def test_supported_names_preserve_case_order_and_repetitions(self):
        self.assertEqual(
            regex_extractor.extract_databases("Postgres PostgreSQL mysql MongoDB Postgres POSTGRESQL"),
            ["Postgres", "PostgreSQL", "mysql", "MongoDB", "Postgres", "POSTGRESQL"],
        )

    def test_prose_punctuation_and_line_breaks(self):
        self.assertEqual(
            regex_extractor.extract_databases("I used (MySQL),\nMongoDB/Postgres."),
            ["MySQL", "MongoDB", "Postgres"],
        )

    def test_no_matches_or_partial_names(self):
        for text in ["", "Python React.js Git SQL NoSQL", "PostgreSQLExtra MySQL8 my_MongoDB",
                     "Postgres.js prefix.MySQL", "Mongo DB"]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_databases(text), [])

    def test_sample_resume(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        self.assertEqual(
            regex_extractor.extract_databases(sample.read_text(encoding="utf-8")), ["Postgres"]
        )


class ToolExtractionTests(unittest.TestCase):
    def test_supported_names_preserve_case_order_and_repetitions(self):
        self.assertEqual(
            regex_extractor.extract_tools("Docker git GIT docker Git"),
            ["Docker", "git", "GIT", "docker", "Git"],
        )

    def test_prose_punctuation_and_line_breaks(self):
        self.assertEqual(
            regex_extractor.extract_tools("I use (Git),\nDocker. Git/Docker"),
            ["Git", "Docker", "Git", "Docker"],
        )

    def test_no_matches_or_partial_names(self):
        for text in ["", "Python React.js Postgres", "GitHub GitLab Dockerfile digital",
                     "my_Git Docker2 Git.exe prefix.Docker"]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_tools(text), [])

    def test_sample_resume(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        self.assertEqual(
            regex_extractor.extract_tools(sample.read_text(encoding="utf-8")), ["Git"]
        )


class EducationExtractionTests(unittest.TestCase):
    def test_supported_degrees_and_fields(self):
        for phrase in [
            "Bachelor's degree in Systems Engineering", "Bachelor of Science in Computer Science",
            "Master's degree in Data Science", "Master of Science in Software Engineering",
            "PhD in Artificial Intelligence", "Ph.D. in Machine Learning",
            "BSc in Computer Engineering", "B.Sc. in Information Technology",
            "MSc in Data Science", "M.Sc. in Computer Science",
        ]:
            with self.subTest(phrase=phrase):
                self.assertEqual(regex_extractor.extract_education(phrase + "."), [phrase])

    def test_preserves_case_spacing_apostrophe_and_repetitions(self):
        phrase = "MASTER’S  degree in data science"
        self.assertEqual(regex_extractor.extract_education(phrase + "; " + phrase), [phrase, phrase])

    def test_stops_before_institution_and_following_prose(self):
        self.assertEqual(
            regex_extractor.extract_education(
                "I earned a PhD in Computer Science at Example University. I use Python.\n"
                "Master's degree in Data Science, 2024."
            ),
            ["PhD in Computer Science", "Master's degree in Data Science"],
        )

    def test_no_matches_for_unsupported_or_incomplete_phrases(self):
        for text in ["", "Computer Science", "Bachelor's degree", "PhD in History",
                     "NotPhD in Computer Science", "PhD in Computer ScienceExtra",
                     "Master of ceremonies", "PhD\nin Computer Science"]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_education(text), [])

    def test_sample_resume(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        self.assertEqual(regex_extractor.extract_education(sample.read_text(encoding="utf-8")),
                         ["Bachelor's degree in Systems Engineering"])


class ExperienceExtractionTests(unittest.TestCase):
    def test_supported_durations(self):
        for phrase in ["3 years of experience", "1 year of experience", "6 months of experience",
                       "1 month experience", "2.5 years of experience", "5+ years of experience",
                       "4 years of professional experience", "12 months of work experience"]:
            with self.subTest(phrase=phrase):
                self.assertEqual(regex_extractor.extract_experience(phrase + "."), [phrase])

    def test_preserves_case_spacing_order_and_repetitions(self):
        self.assertEqual(
            regex_extractor.extract_experience("3 YEARS  OF EXPERIENCE; 6 months experience; 3 YEARS  OF EXPERIENCE"),
            ["3 YEARS  OF EXPERIENCE", "6 months experience", "3 YEARS  OF EXPERIENCE"],
        )

    def test_prose_without_heading(self):
        self.assertEqual(regex_extractor.extract_experience(
            "I have 3 years of experience developing web applications and 6 months experience testing."),
            ["3 years of experience", "6 months experience"])

    def test_does_not_infer_duration_from_dates(self):
        self.assertEqual(regex_extractor.extract_experience("Software Engineer, 2020-2024. Python and Git."), [])

    def test_no_matches_for_unsupported_or_incomplete_phrases(self):
        for text in ["", "3 years", "experience", "three years of experience",
                     "-3 years of experience", "3-5 years of experience", "v3 years of experience",
                     "3 years of experienced", "3\nyears of experience"]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_experience(text), [])

    def test_sample_resume(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        self.assertEqual(regex_extractor.extract_experience(sample.read_text(encoding="utf-8")),
                         ["3 years of experience"])


class OtherQualificationExtractionTests(unittest.TestCase):
    def test_supported_concepts_and_variants(self):
        self.assertEqual(regex_extractor.extract_other_qualifications(
            "REST APIs; REST API; SQL; NoSQL; machine-learning model development; "
            "machine learning model development"),
            ["REST APIs", "REST API", "SQL", "NoSQL", "machine-learning model development",
             "machine learning model development"])

    def test_preserves_case_spacing_order_and_repetitions(self):
        self.assertEqual(regex_extractor.extract_other_qualifications(
            "I build rest  apis using sql. I also teach sql."),
            ["rest  apis", "sql", "sql"])

    def test_does_not_infer_from_products_or_partial_words(self):
        for text in ["", "MySQL PostgreSQL TensorFlow Python Git", "NoSQLExtra REST APIservice",
                     "SQLAlchemy my_SQL SQL.js", "machine learning", "REST\nAPIs"]:
            with self.subTest(text=text):
                self.assertEqual(regex_extractor.extract_other_qualifications(text), [])


class ResumeInfoExtractionTests(unittest.TestCase):
    def test_sample_resume_complete_dictionary(self):
        sample = Path(__file__).resolve().parents[1] / "data" / "resume_example.txt"
        self.assertEqual(regex_extractor.extract_resume_info(sample.read_text(encoding="utf-8")), {
            "emails": ["Wednesday.Addams@example.com"], "phones": ["+57 300 123 4567"],
            "programming_languages": ["JS"], "frameworks": ["React.js", "NodeJS"],
            "databases": ["Postgres"], "education": ["Bachelor's degree in Systems Engineering"],
            "experience": ["3 years of experience"], "tools": ["Git"], "other_qualifications": [],
        })

    def test_empty_text_keeps_all_categories(self):
        self.assertEqual(regex_extractor.extract_resume_info(""), {
            "emails": [], "phones": [], "programming_languages": [], "frameworks": [],
            "databases": [], "education": [], "experience": [], "tools": [],
            "other_qualifications": [],
        })

    def test_mixed_text_keeps_categories_and_original_variants(self):
        self.assertEqual(regex_extractor.extract_resume_info(
            "python, sklearn, PostgreSQL, git, SQL, NoSQL, REST APIs, python. "
            "PhD in Data Science; 2 years of experience."), {
            "emails": [], "phones": [], "programming_languages": ["python", "python"],
            "frameworks": ["sklearn"], "databases": ["PostgreSQL"],
            "education": ["PhD in Data Science"], "experience": ["2 years of experience"],
            "tools": ["git"], "other_qualifications": ["SQL", "NoSQL", "REST APIs"],
        })


if __name__ == "__main__":
    unittest.main()
