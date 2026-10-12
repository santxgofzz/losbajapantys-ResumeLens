# Module design

ResumeLens evaluates explicit qualification patterns, not candidate suitability or hiring merit.
Run commands from `resumeLeans/`. The entry point is `python -m src.main`.

## Data flow and contracts

| Module / function | Input | Output / responsibility |
|---|---|---|
| `extraction.regex_extractor.extract_resume_info` | Resume text (`str`) | Dictionary of nine lists: emails, phones, programming_languages, frameworks, databases, education, experience, tools, other_qualifications. Preserves original matches, order and repetitions. |
| `normalization.transducers.normalizar_skills` | Extraction dictionary | Sorted, unique canonical skill strings produced by a pyformlang FST. Reads only the five technical categories. |
| `automata.profile_definitions.prepare_qualifications_for_profile` | Canonical skills and profile name | Relevant unique skills in the profile's category order. Unknown profile names raise `ValueError`. |
| `automata.classifiers.is_*` | Canonical skills | Boolean result of the corresponding DFA after preparation. |
| `main.classify_profiles` | Canonical skills | Four profile names mapped to booleans. |
| `dsl.candidate_parser.generate_candidate_profile` | Extraction, canonical skills, evaluations, optional personal data | Validated DSL string; malformed input raises errors. |
| `dsl.candidate_parser.parse_candidate_profile` | DSL string | textX model; checks syntax. |
| `dsl.candidate_parser.validate_candidate_profile` | DSL string | Model with additional checks for four unique evaluations and uppercase unique skill identifiers. |
| `dsl.candidate_parser.candidate_profile_to_dict` | Validated DSL text | Plain data for rendering. |
| `dsl.visualizer.generate_candidate_html` | DSL string | HTML string with escaped candidate values. |
| `dsl.visualizer.save_candidate_html` | DSL string and output path | Writes UTF-8 HTML, creates parent directories and returns the path. |
| `main.process_resume` | Resume text, optional personal data | Tuple `(extracted, normalized_skills, evaluations, dsl_text)`. No file writes. |
| `main.main` | Bundled example file | Writes `output/candidate_profile.dsl` and `.html`; prints intermediate results. |

## Design decisions

The extractor does not normalize or classify. The FST handles differences in letter case and repeated spaces or tabs. Unknown terms produce no canonical token; unexpected runtime errors propagate rather than being silently suppressed. The FST preserves Java, MySQL and MongoDB as distinct tokens; it does not infer SQL/NoSQL proficiency from a product name. Skills outside a profile's alphabet are ignored by that classifier but remain available in the DSL.

Every profile requires at least one skill from each category in its definition. All four are evaluated independently, so several may be accepted. Education and experience are displayed, but do not affect these technical patterns. Full Stack explicitly requires REST_API: the bundled Wednesday example without an API mention is correctly rejected by this chosen pattern.

Optional personal information uses `name`, `current_role`, `location`, `summary`. The example entry point supplies illustrative values manually; it does not extract them from arbitrary resumes. To process another candidate, call `process_resume(text, personal_info)` and pass its DSL to `save_candidate_html`. There is no upload UI, PDF reader or OCR pipeline.

## Limitations

Vocabulary is finite. Academic and experience patterns target documented English formats; phone extraction targets Colombian-style numbers. The system detects mentions but cannot tell whether a candidate has mastered a skill or is saying they lack it. A hand-edited DSL is structurally validated but its classification status is not recomputed; trusted results come from `process_resume`. The renderer escapes candidate text before inserting it into HTML. Check the generated page in a browser to review its layout.

See [formalization](formalization.md), [test scenarios](test-cases.md), and [source review](literature_review.md).
