# Test design and reproducible results

Run from `resumeLeans/` with the project environment active:

```bash
python -B -m pytest -q -p no:cacheprovider
```

## Scenarios

| Area | Scenario | Expected result | Automated evidence |
|---|---|---|---|
| Extraction | Valid and malformed contacts; bounded technical words; repeated mentions | Only supported matches, with original case, order and repetitions | `tests/test_extraction.py` |
| Extraction | Numeric ranges and compound experience; compound academic fields | Complete supported phrases, no truncated supported compounds | `tests/test_extraction.py` |
| Normalization | Lowercase/mixed-case aliases and repeated spaces/tabs | Same canonical token from the FST | `tests/test_normalization.py` |
| Normalization | Java, MySQL, MongoDB, RESTful APIs, model-development phrases | JAVA, MYSQL, MONGODB, REST_API, MACHINE_LEARNING | `tests/test_normalization.py` |
| Normalization | Unknown terms, suffixes, newline-separated names, concatenated skills | No accepting path | `tests/test_normalization.py` |
| Normalization | Duplicate equivalent mentions and nontechnical fields | Unique sorted skills; input unchanged; contacts/education not treated as skills | `tests/test_normalization.py` |
| Classification | Accepted patterns, missing categories, multiple alternatives, irrelevant tokens and reordered skills | Acceptance exactly according to the declared profile pattern | `tests/test_automata.py` |
| Integration | Full Stack, ML, DevOps and Data profiles with variant spellings and reversed input order | Target profile accepted; DSL parses; HTML includes its result | `tests/test_integration.py` |
| Integration | Remove each required category from each complete fixture | Target profile rejected | `tests/test_integration.py` |
| DevOps integration | CI/CD, Jenkins, GitHub Actions and GitLab CI; AWS, GCP and Azure variants | Compatible tokens across extraction, FST and DFA | `tests/test_integration.py` |
| DSL | Correct/incorrect syntax, repeated records, invalid evaluations and escaping | Valid models accepted, malformed representations rejected | `tests/test_dsl.py` |
| HTML | Candidate fields and script-like candidate text | Values displayed, script markup escaped | `tests/test_visualization.py` |

## Interpretation

The tests use examples created for the project. They check expected outputs and previously found errors. Accuracy on real resumes has not been measured. The latest recorded results are below; run the command above to check the current version.

To check the generated page: run `python -m src.main`, open `output/candidate_profile.html`, verify contacts and qualifications against `data/resume_example.txt`, check all four evaluation statuses and inspect the intended display width. The bundled example lacks REST API, so Full Stack rejection is expected. Review presentation appearance separately from HTML string tests.

## Verification recorded on 2026-10-11

- New normalization/integration regressions initially reproduced 19 failures (14 other selected cases passed) before the FST fix.
- After correction, the full suite passed: 135 tests and 150 subtests.
- An additional direct FST probe checked all 124 dictionary entries in original, lowercase, uppercase, swapped case and repeated horizontal-spacing forms; every output matched its declared token.
- The entry point generated DSL and HTML in a temporary directory. The DSL parsed into four evaluations and the HTML contained the example candidate. The page still needs a visual check in a browser.
- `git diff --check` found no whitespace errors. Git reported line-ending conversion notices for some Windows working-tree files.
