# Regular-expression extraction

## Objective

Extract explicitly written contact information and technical terms using
Python's standard `re` module. The module implements emails, Colombian-style
phone numbers, programming languages, frameworks/libraries/runtimes, databases,
tools, academic qualifications, and explicit experience durations below.
It does not normalize text or evaluate candidate qualifications.
Additional qualifications and a combined dictionary interface are also implemented.
The initial vocabulary now includes the team's DevOps and Data Engineer profiles.
End-to-end regression tests now exercise normalization, the four classifiers, DSL validation and HTML generation.

## Requirement sources and implementation decisions

Source: *Integrative-Task1-2026-2_CyED3.pdf*, printed page 2 (reference profiles),
page 3 (Project Goal 1), and page 4 (illustrative normalization variants).
The assignment requires extraction categories, regular expressions with
explanations, Python `re` implementations, and storage in a file or data
structure. It does not prescribe these exact patterns or a complete vocabulary.
Profile examples are illustrative, not mandatory requirements for every candidate.

| Source/status | Vocabulary or decision |
| --- | --- |
| Full Stack reference profile and example, page 2 | JavaScript/JS, TypeScript, React/React.js, Angular, Vue, Node.js/NodeJS, Django, Spring Boot, SQL/NoSQL, REST APIs, Postgres, Git |
| Machine Learning reference profile and example, page 2 | Python, Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch, machine-learning model development, SQL, Git |
| Normalization examples, page 4 | ReactJS, PostgreSQL, sklearn, scikit learn, Tensor Flow, Py Torch and case variants illustrate alternative spellings; extraction preserves them rather than performing the transformations. |
| Additional vocabulary proposed during implementation | Java, MySQL and MongoDB are not explicitly named in those reference lists. They are optional extensions already implemented, not assignment requirements. They are stored as separate skills and do not change the profile requirements. |
| Team-selected profiles | DevOps Engineer and Data Engineer are defined in `src/automata/profile_definitions.py` and `docs/automata/profile_patterns.md`. Docker now has an explicit basis in the team's DevOps profile. Additional tool names and concepts below come from these files; aliases come from `TRANSFORMACIONES` in `src/normalization/transducers.py`. |
| Additional spelling choices | TS, Vue.js, singular REST API, case-insensitive matching and whitespace handling are implementation choices, not an exhaustive spelling list specified by the assignment. |
| Contact format choices | The practical ASCII email subset and Colombian-style phone formats are implementation choices. The assignment does not restrict contact extraction to those formats. |
| Education and experience choices | The English degree/field vocabulary, required `in`, numeric years/months and accepted modifiers are implementation choices. The assignment does not prescribe these degrees, fields or duration thresholds. |
| Category/interface choices | Node.js is grouped with frameworks/libraries as a runtime; SQL/NoSQL are in other qualifications. Nine dictionary keys represent eight assignment categories because contact information is split into emails and phones. |

The fictional sample's email, phone and education were created for testing;
they are not facts supplied by the assignment. The supported vocabulary is listed below; words outside this list are not extracted.

The alias-alignment update also accepts `py`, `Angular.js`, `AngularJS`, `VueJS`,
`Node`, `Spring`, `SpringBoot`, `tf`, `No SQL`, `RESTful API`, `ML` and short
machine-learning phrases because these appear in the team's normalization
dictionary. Bare Node/Spring, short aliases and ML are lexically ambiguous;
their presence is not evidence of proficiency. Longer supported phrases take
precedence, and no canonical spelling is substituted by extraction.

## Initial programming-language vocabulary

This section defines the vocabulary and behavior of
`extract_programming_languages(text)`. The vocabulary is implemented in the Python pattern;
the function does not read this Markdown file.

| Language | Recognized names and abbreviations | Examples of case variants |
| --- | --- | --- |
| JavaScript | `JavaScript`, `JS` | `Javascript`, `javascript`, `js`, `JS` |
| TypeScript | `TypeScript`, `TS` | `Typescript`, `typescript`, `ts`, `TS` |
| Python | `Python`, `py` | `python`, `PYTHON`, `PY` |
| Java | `Java` | `java`, `JAVA` |

Matching is case-insensitive; the case variants above are examples, not
an exhaustive list. The language column organizes this document only: it is
not a mapping used to normalize the extracted strings.

Recognition rules:

- Search the entire resume, including prose outside a skills section.
- Return the exact matched text, preserving case, order, and repetitions.
- Recognize complete names or abbreviations, not parts of longer words:
  `JavaScript` must not also produce `Java`, and `Pythonista` must not
  produce `Python`. Adjacent letters, digits, or underscores prevent a
  complete-word match (for example, `Python3` and `my_python`).
- Accept surrounding separators such as spaces, commas, parentheses, and
  line breaks.
- Return an empty list when no supported language is present.
- Keep `React.js`, `NodeJS`, `Postgres`, and `Git` outside this category.

Expected examples:

| Input text | Expected list |
| --- | --- |
| `JS, React.js, NodeJS, Postgres, Git.` | `["JS"]` |
| `I use JS and python. I also know JavaScript, Java and React.js.` | `["JS", "python", "JavaScript", "Java"]` |
| `TypeScript, TS, typescript, ts` | `["TypeScript", "TS", "typescript", "ts"]` |
| `Python, Python` | `["Python", "Python"]` |
| `(JAVA), PYTHON` | `["JAVA", "PYTHON"]` |
| `Pythonista, JavaScriptCore, Python3, my_python` | `[]` |
| `React.js, NodeJS, Postgres, Git` | `[]` |
| Empty text | `[]` |

This is an initial vocabulary, not complete coverage of all four professional
profiles. Additional languages can be added as needed. Abbreviations
such as `JS` and `TS` can be ambiguous in prose; lexical extraction alone does
not prove that a mention represents a candidate's skill or proficiency.

## Functions and storage

All functions are defined in `src/extraction/regex_extractor.py`:

| Function | Input | Output |
| --- | --- | --- |
| `extract_emails(text)` | Resume text as a `str` | `list[str]` of matching email addresses |
| `extract_phones(text)` | Resume text as a `str` | `list[str]` of matching phone numbers |
| `extract_programming_languages(text)` | Resume text as a `str` | `list[str]` of supported language mentions |
| `extract_frameworks(text)` | Resume text as a `str` | `list[str]` of supported frameworks, libraries and runtimes |
| `extract_databases(text)` | Resume text as a `str` | `list[str]` of supported database names |
| `extract_tools(text)` | Resume text as a `str` | `list[str]` of supported tool names |
| `extract_education(text)` | Resume text as a `str` | `list[str]` of supported degree-and-field phrases |
| `extract_experience(text)` | Resume text as a `str` | `list[str]` of explicit numeric experience phrases |
| `extract_other_qualifications(text)` | Resume text as a `str` | `list[str]` of supported additional qualifications |
| `extract_resume_info(text)` | Resume text as a `str` | `dict[str, list[str]]` containing all nine categories |

Each returned list stores the extracted information in memory. Empty input or
text without matches produces `[]`. Matches retain original capitalization,
separators, order, and repeated occurrences. None of the functions reads files,
changes the input, requires a section heading, or removes duplicates.
Inputs other than strings are outside the interface contract.

## Email expression

```python
EMAIL_PATTERN = (
    r"(?<![\w.%+@-])"
    r"[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*"
    r"@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,}"
    r"(?![\w@+-]|\.\w)"
)
```

This recognizes a practical subset of ASCII email syntax: a nonempty local
part, `@`, and a dotted domain ending in at least two ASCII letters.

| Component | Meaning |
| --- | --- |
| `(?<![\w.%+@-])` | Do not start after a word character or the listed address characters; this blocks common malformed local-part fragments. |
| `[A-Za-z0-9_%+-]+` | One or more ASCII letters, digits, underscores, percent signs, plus signs, or hyphens. |
| `(?:\.[A-Za-z0-9_%+-]+)*` | Additional nonempty local-part segments separated by dots. Leading, trailing and consecutive local-part dots are excluded. |
| `@` | Literal local-part/domain separator. |
| `(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+` | One or more domain labels, each followed by a dot. Labels begin and end with letters or digits and may contain internal hyphens. |
| `[A-Za-z]{2,}` | Final domain label with at least two letters. |
| `(?![\w@+-]|\.\w)` | Avoid ending inside a longer address-like token; allow prose punctuation such as a sentence-ending period. |

## Phone expression

```python
PHONE_PATTERN = (
    r"(?<![\w+])(?<![0-9][ -])"
    r"(?:\+57[ -]?)?"
    r"(?:3[0-9]{2}|60[0-9])[ -]?[0-9]{3}[ -]?[0-9]{4}"
    r"(?!\w|[ -]?[0-9])"
)
```

This recognizes ten-digit national numbers beginning with `3` or `60`, with
an optional literal `+57` prefix. National digits use a 3-3-4 grouping, with
zero or one space/hyphen at each separator. Separators may differ. This is a
chosen extraction heuristic, not a complete telephone numbering validator.

| Component | Meaning |
| --- | --- |
| `(?<![\w+])` | Do not start immediately inside a word, a longer number, or after a plus sign. |
| `(?<![0-9][ -])` | Do not extract a suffix after another digit and separator, such as the national portion of `+58 300 123 4567`. |
| `(?:\+57[ -]?)?` | Optional country prefix, followed by an optional space or hyphen. |
| `(?:3[0-9]{2}|60[0-9])` | First three digits: either `3` plus two digits, or `60` plus one digit. |
| `[ -]?[0-9]{3}[ -]?[0-9]{4}` | Remaining seven digits, optionally separated into groups of three and four. |
| `(?!\w|[ -]?[0-9])` | Do not end before a word character or another digit, even with one intervening separator. |

## Programming-language expression

```python
PROGRAMMING_LANGUAGES_PATTERN = (
    r"(?<![\w.])(?:JavaScript|JS|TypeScript|TS|Python|py(?![ \t]+Torch\b)|Java)\b"
)
```

- `(?<![\w.])` prevents a match immediately after a word character or a dot.
  The dot check prevents extracting `js` from `React.js` or `Node.js`.
- The alternatives list the supported names without capturing subgroups.
  `py(?![ \t]+Torch\b)` avoids treating `py` inside `Py Torch` as Python.
- `\b` requires a word boundary at the end, excluding suffixes such as
  `Python3`, `Pythonista`, and `JavaScriptCore`.
- `re.findall(..., flags=re.IGNORECASE)` accepts case variants while returning
  the original matched strings, with no normalization.

The language recognized consists of the seven listed spellings in any letter
case, subject to these surrounding-character checks. The vocabulary is finite;
the function does not infer languages that are missing from the list.

The dot guard is a deliberate heuristic: it also excludes a language directly
after a sentence-ending dot without a space, such as `experience.Python`.
Names in URLs or contact details can still be matched in other positions.
Lexical matching does not establish proficiency or handle negation.
Unlike the framework/database/tool patterns, the final language boundary is
only `\b`: `Python.js` produces `Python`. The leading dot guard prevents
`js` being extracted from `React.js`; it is not a general filename filter.

## Frameworks, libraries and runtimes

`extract_frameworks(text)` groups the following technologies for extraction.
Node.js is a runtime, not a framework; it is deliberately included in this
category. All listed spellings support case-insensitive matching and retain
their original representation in the output.

| Technology | Supported spellings |
| --- | --- |
| React | `React`, `React.js`, `ReactJS` |
| Angular | `Angular`, `Angular.js`, `AngularJS` |
| Vue | `Vue`, `Vue.js`, `VueJS` |
| Node.js | `NodeJS`, `Node.js`, `Node` |
| Django | `Django` |
| Spring Boot | `Spring Boot`, `SpringBoot`, `Spring` |
| Pandas | `Pandas` |
| NumPy | `NumPy` |
| Scikit-learn | `Scikit-learn`, `scikit learn`, `sklearn` |
| TensorFlow | `TensorFlow`, `Tensor Flow`, `tf` |
| PyTorch | `PyTorch`, `Py Torch` |

```python
FRAMEWORKS_PATTERN = (
    r"(?<![\w.])"
    r"(?:React(?:\.js|JS)?|Angular(?:\.js|JS)?|Vue(?:\.js|JS)?|Node(?:JS|\.js)?|"
    r"Django|Spring(?:[ \t]*Boot|(?!\s+Boot))|Pandas|NumPy|Scikit[- ]learn|sklearn|"
    r"Tensor ?Flow|tf|Py ?Torch)"
    r"(?!\w|\.\w)"
)
```

- `React(?:\.js|JS)?` accepts the full dotted or joined suffix, or bare `React`.
  Angular and Vue likewise accept bare, dotted-js and joined-JS variants.
- `Node(?:JS|\.js)?` accepts Node with or without its suffix, as the team
  normalization dictionary does. Bare Node is ambiguous in nontechnical prose.
- `Scikit[- ]learn` accepts a single hyphen or space; `sklearn` is another alternative.
- `Tensor ?Flow` and `Py ?Torch` accept zero or one literal space.
- Spring accepts joined or horizontally separated Boot, or the bare name.
  Its guard prevents falling back to bare Spring before an unsupported Boot
  continuation or a line break followed by Boot. These terms remain ambiguous.
- `(?<![\w.])` prevents starting inside a word or after a dot.
- `(?!\w|\.\w)` prevents ending inside a word or immediately before a dotted
  continuation. This avoids partial matches such as `React` from `React.jsx`.
  A sentence-ending dot is allowed when it is not followed by a word character.
- `re.IGNORECASE` allows variants such as `react.js` and `PANDAS` without changing
  their spelling. Noncapturing groups keep each `findall` result a complete match.

The function searches the whole input and preserves order and duplicates.
For `I use React.js, NodeJS and sklearn.`, the result is
`["React.js", "NodeJS", "sklearn"]`. Empty input or no supported terms produces `[]`.

This is a finite initial vocabulary. Unlisted spellings and line-wrapped names
are unsupported. Framework names other than Spring Boot retain their documented
single-space forms. Word matching cannot distinguish
ordinary prose such as `react` or `pandas` from technology mentions, prove skill,
or interpret negation. Dotted boundary guards can miss names immediately after
a sentence-ending dot without whitespace. Names in URLs can still match.

## Databases and tools

The initial vocabulary is intentionally limited to these names, with any
capitalization. The expressions are defined in Python, not loaded from this document.

| Category | Supported names |
| --- | --- |
| Databases | `PostgreSQL`, `Postgres`, `MySQL`, `MongoDB` |
| Development and DevOps tools/platforms | `Git`, `Docker`, `Linux`, `Kubernetes`, `K8s`, `Jenkins`, `GitHub Actions`, `GitLab CI`, `AWS`, `Amazon Web Services`, `GCP`, `Google Cloud`, `Google Cloud Platform`, `Azure`, `Microsoft Azure`, `Terraform` |
| Data tools/technologies | `Spark`, `Apache Spark`, `PySpark`, `Airflow`, `Apache Airflow`, `Kafka`, `Apache Kafka` |

```python
DATABASES_PATTERN = r"(?<![\w.])(?:PostgreSQL|Postgres|MySQL|MongoDB)(?!\w|\.\w)"
TOOLS_PATTERN = (
    r"(?<![\w.])"
    r"(?:GitHub[ \t]+Actions|GitLab[ \t]+CI|Git|Docker|Linux|Kubernetes|K8s|Jenkins|"
    r"AWS|Amazon[ \t]+Web[ \t]+Services|GCP|"
    r"Google[ \t]+Cloud(?:[ \t]+Platform|(?![ \t]+Platform))|"
    r"(?:Microsoft[ \t]+)?Azure|Terraform|"
    r"(?:Apache[ \t]+)?(?:Spark|Airflow|Kafka)|PySpark)"
    r"(?!\w|\.\w)"
)
```

Both functions use `re.findall` with `re.IGNORECASE`. The recognized language
is the finite set of listed names in any letter case, with boundary checks:

- `(?<![\w.])` excludes a start directly after a word character or dot.
- `(?:...|...)` groups alternative names without capturing subgroups.
- Multiword tool names use `[ \t]+`, preserving spaces/tabs and excluding
  line breaks. Optional `Apache` and `Microsoft` prefixes remain in the match.
  `GitHub Actions` and `GitLab CI` match as complete names, never as `Git`.
  The Google Cloud alternatives prefer the full `Google Cloud Platform` name;
  the negative lookahead prevents falling back to `Google Cloud` when an invalid
  longer `Platform...` suffix follows.
- `(?!\w|\.\w)` excludes a continuation with a word character or a dot followed
  by a word character. Thus `MySQL8`, `my_MongoDB`, `GitHub`, `GitLab`,
  `Dockerfile`, and `Git.exe` do not produce partial matches.
- Whitespace, commas, parentheses, slashes, and sentence-ending periods can
  delimit matches. A terminal period is excluded from the returned string.

Search covers the entire resume. Output preserves spelling, capitalization,
order, and repetitions. Empty input or no supported names produces `[]`.

```python
extract_databases("I use Postgres, POSTGRESQL and MongoDB.")
# ['Postgres', 'POSTGRESQL', 'MongoDB']
extract_tools("I use git and Docker. I teach git.")
# ['git', 'Docker', 'git']
```

`Postgres` is not converted to `PostgreSQL`; normalization belongs to the next
component. `SQL` and `NoSQL` do not identify a specific database product and are
not included in this database vocabulary. They are extracted by
`extract_other_qualifications`. GitHub and GitLab are not aliases for Git.

Limitations: unlisted products and spellings (such as `Mongo DB`) are not
recognized. The dot guard excludes a name immediately after a sentence-ending
dot without a space. A hyphen is a separator, so a supported name within a
hyphenated expression may match. Matching names alone cannot establish
proficiency, interpret negation, or rule out mentions in unrelated contexts.
The list covers the database names supported by the extractor. Profile requirements are defined separately in `src/automata/profile_definitions.py`.

The `tools` category includes platforms and data-processing technologies, not
only command-line utilities. This keeps Spark/PySpark, Kafka and Airflow in one
documented category; no additional framework or database match is inferred.

## Academic qualifications

`extract_education(text)` recognizes an explicit English degree followed by
`in` and a field from the initial vocabulary. It searches the whole text and
returns original phrases, without requiring an Education heading.

Supported degrees: `Bachelor's degree`, `Master's degree` (straight or curly
apostrophe), `Bachelor of Science`, `Master of Science`, `Bachelor of Engineering`,
`Master of Engineering`, `PhD`, `Ph.D.`,
`BSc`, `B.Sc.`, `MSc`, and `M.Sc.`. Matching ignores letter case.

Supported fields: Systems Engineering, Computer Science, Software Engineering,
Computer Engineering, Data Science, Artificial Intelligence, Machine Learning,
and Information Technology. A finite field list avoids greedily swallowing
institutions or arbitrary prose after the qualification.

```python
EDUCATION_FIELD_PATTERN = (
    r"(?:Systems[ \t]+Engineering|Computer[ \t]+Science|Software[ \t]+Engineering|"
    r"Computer[ \t]+Engineering|Data[ \t]+Science|Artificial[ \t]+Intelligence|"
    r"Machine[ \t]+Learning|Information[ \t]+Technology)"
)

EDUCATION_PATTERN = (
    r"(?<![\w.])"
    r"(?:(?:Bachelor|Master)['’]s[ \t]+degree|"
    r"(?:Bachelor|Master)[ \t]+of[ \t]+(?:Science|Engineering)|PhD|Ph\.D\.|[BM]Sc|[BM]\.Sc\.)"
    r"[ \t]+in[ \t]+"
    + EDUCATION_FIELD_PATTERN
    + r"(?:[ \t]*(?:\band\b|&|/)[ \t]*(?:"
    + EDUCATION_FIELD_PATTERN + r"|Mathematics))*\b"
    r"(?![ \t]*(?:\band\b|&|/))"
)
```

- `(?<![\w.])` prevents starting inside a word or directly after a dot.
- Degree alternatives recognize only the listed title spellings. `[BM]`
  chooses B or M; escaped dots in abbreviations are literal.
- `['’]` accepts either apostrophe without replacing it.
- `[ \t]+` accepts one or more spaces/tabs, preserving them in the result;
  it does not cross line breaks.
- Literal `in` connects the degree and required field. The final `\b`
  prevents a field match ending inside a longer word.
- `EDUCATION_FIELD_PATTERN` is a reusable regex fragment, not a second extraction
  pass. It is concatenated into the main expression. Additional listed fields or
  Mathematics may follow `and`, `&`, or `/`. The final negative lookahead rejects
  a remaining connector so an unsupported compound field is not silently cut off.
  Mathematics is currently supported as an additional field, not a standalone one.

For `PhD in Computer Science at Example University.`, the result is
`["PhD in Computer Science"]`. The institution and sentence period are not
included. `Bachelor's degree in Systems Engineering` is extracted intact
from the example resume.

Limitations: other fields, languages, standalone titles, certifications,
unlisted abbreviations and line-wrapped phrases are not covered yet. The phrase
`PhD in Computer Science and Mathematics` is preserved completely, while
`PhD in Computer Science and History` yields no match. Unsupported connectors
such as `with` or comma-separated fields may still produce a shorter phrase.
Even unrelated prose starting with `and` after a degree may cause rejection;
the guard is conservative. The function cannot establish whether a
degree was completed: a phrase in `pursuing a PhD in Computer Science` still
matches. It does not normalize degrees or infer institutions or dates.

## Professional experience

`extract_experience(text)` recognizes numeric durations explicitly attached to
the word `experience`, anywhere in the text. The function extracts duration
phrases, not complete employment histories, employers, dates or responsibilities.

```python
EXPERIENCE_PATTERN = (
    r"(?<![\w.+−–—-])[0-9]+(?:\.[0-9]+)?\+?"
    r"(?:[ \t]*(?:[-–—]|\bto\b)[ \t]*[0-9]+(?:\.[0-9]+)?)?"
    r"[ \t]+(?:years?|months?)"
    r"(?:[ \t]+and[ \t]+[0-9]+(?:\.[0-9]+)?[ \t]+(?:years?|months?))*"
    r"[ \t]+(?:of[ \t]+)?"
    r"(?:(?:professional|work)[ \t]+)?experience\b"
)
```

- The initial lookbehind prevents starting immediately after a word character,
  dot, plus, minus, hyphen, en dash or em dash. The numeric range branch consumes
  both endpoints instead of searching for a suffix after a range separator.
- `[0-9]+(?:\.[0-9]+)?` recognizes integers or dot-decimal numbers.
- `\+?` accepts an optional plus sign, as in `5+`.
- The optional range branch accepts hyphen, en dash, em dash or the word `to`,
  with optional horizontal whitespace. For example, `3-5` and `3 - 5` remain intact.
- The repeated `and` branch preserves multiple numeric year/month components,
  such as `3 years and 6 months`, without summing or converting them.
- `years?` and `months?` accept singular and plural units.
- `of` is optional, as is one modifier: `professional` or `work`.
- `experience\b` requires the complete final word, not `experienced`.
- `[ \t]+` permits spaces/tabs without crossing lines. Matching uses
  `re.IGNORECASE` and returns the original case, spacing and duplicates.

Examples: `3 years of experience`, `6 months experience`,
`2.5 years of experience`, `5+ years of professional experience`.
For `3 years of experience developing web applications.`, only
`3 years of experience` is returned. Date ranges such as `2020-2024` produce no
duration; the function does not calculate, add, convert or validate durations.

Limitations: spelled-out numbers, possessive forms (`3 years' experience`),
other languages and unlisted constructions such as `between 3 and 5 years`
remain unsupported and can produce suffix matches. The supported range has one
unit after the endpoints; the supported compound uses `and` between number/unit
pairs. This is not a general numeric-expression parser. Qualifiers
such as `at least` are not captured. Numeric grammar is lexical, so implausible
durations or number/unit agreement errors can match. The function does not
distinguish professional from academic experience when the text does not say,
interpret negation, or decide whether experience is relevant to a profile.

## Other relevant qualifications

The assignment's Full Stack reference profile mentions REST APIs and SQL/NoSQL
databases; its Machine Learning reference profile mentions SQL and
machine-learning model development. These concepts supply the initial vocabulary
for `extract_other_qualifications(text)`. This is not a list of new mandatory
requirements for every candidate.

| Concept from the assignment | Accepted textual forms |
| --- | --- |
| REST APIs | `REST API`, `REST APIs`, `RESTful API`, `RESTful APIs` |
| SQL | `SQL` |
| NoSQL | `NoSQL`, `No SQL` (horizontal whitespace preserved) |
| Machine learning mentions | `ML`, `Machine Learning`, `Machine-learning`, `machine-learning model development`, `machine learning model development` |

The team-selected profiles and their normalization dictionary additionally supply:

| Team concept | Accepted textual forms | Output category |
| --- | --- | --- |
| Continuous integration/deployment | `CI/CD`, `CI-CD` | `other_qualifications` |
| Data integration | `ETL`, `Extract Transform Load` | `other_qualifications` |
| Data warehouse architecture | `Data Warehouse`, `DW`, `DWH` | `other_qualifications` |

CI/CD is a general process mention, whereas Jenkins, GitHub Actions and GitLab CI
are extracted as named tools. No tool is inferred from the general process.

Singular/plural API, spacing, hyphen and capitalization handling are extractor
design choices. The output does not convert any variant to a canonical form.
SQL is a query language and NoSQL a database category, not product names.
They are placed here by an explicit interface decision, while named products
remain in `databases`. A mention of `MySQL` does not imply an extra `SQL` match.

```python
OTHER_QUALIFICATIONS_PATTERN = (
    r"(?<![\w.])"
    r"(?:REST(?:ful)?[ \t]+APIs?|No[ \t]*SQL|SQL|ML|"
    r"machine(?:-|[ \t]+)learning(?:[ \t]+model[ \t]+development|(?![ \t]+model\b))|"
    r"CI[/-]CD|ETL|Extract[ \t]+Transform[ \t]+Load|Data[ \t]+Warehouse|DWH|DW)"
    r"(?!\w|\.\w)"
)
```

The boundary guards exclude longer words and dotted continuations, as in the
database/tool patterns. `APIs?` accepts singular/plural; `[ \t]+` accepts spaces
or tabs without joining lines. `(?:-|[ \t]+)` accepts a hyphen or horizontal
whitespace between `machine` and `learning`. Noncapturing alternatives keep
`re.findall` results as complete phrases. Matching uses `re.IGNORECASE`.
`REST(?:ful)?` accepts RESTful as well as REST. `No[ \t]*SQL` is evaluated
before SQL so `No SQL` is returned intact, not reinterpreted as SQL. The long
machine-learning phrase is tried before the short one; the fallback guard avoids
cutting off an unsupported `model...` continuation. `ML` is a separate alias.
`CI[/-]CD` accepts slash or hyphen. ETL and warehouse alternatives preserve
abbreviations and full names instead of converting them. `DW` and `DWH` are
potentially ambiguous outside technical context; this remains lexical extraction.

For `Python SQL ETL Spark Airflow Data Warehouse Git`, the technical outputs are
`programming_languages: ["Python"]`, `tools: ["Spark", "Airflow", "Git"]`, and
`other_qualifications: ["SQL", "ETL", "Data Warehouse"]`. For
`Linux Docker Kubernetes GitHub Actions AWS Terraform Git`, the full seven
mentions are returned in `tools`, in the original order.

### Input to normalization

The normalizer accepts case variants and repeated horizontal spaces/tabs using FST transitions. DevOps shares CI_CD, JENKINS, GITHUB_ACTIONS, GITLAB_CI, AWS, GCP and AZURE with the classifiers. Java, MySQL and MongoDB are retained as separate canonical skills without changing profile requirements. Extraction still returns original strings. See [normalization formalization](formalization.md) and `tests/test_integration.py` for the current cross-stage contract.

For `I build REST APIs using sql and NoSQL.`, output is
`["REST APIs", "sql", "NoSQL"]`. Order, spelling, spacing and repeats are retained.
Limitations: this finite vocabulary does not recognize paraphrases such as
`developing predictive models`, infer SQL from products, or infer model
development from TensorFlow. It cannot interpret negation or prove proficiency.
Line-wrapped phrases and unlisted qualifications require later coverage work.

## Combined extraction interface

`extract_resume_info(text)` calls each of the nine extraction functions once
and returns a new dictionary with stable keys, including empty categories:

```python
{
    "emails": ["Wednesday.Addams@example.com"],
    "phones": ["+57 300 123 4567"],
    "programming_languages": ["JS"],
    "frameworks": ["React.js", "NodeJS"],
    "databases": ["Postgres"],
    "education": ["Bachelor's degree in Systems Engineering"],
    "experience": ["3 years of experience"],
    "tools": ["Git"],
    "other_qualifications": [],
}
```

This is the expected result for the existing sample file. The empty additional
qualifications list is intentional: the sample does not explicitly mention
any of that vocabulary. Empty input returns the same keys with empty lists.
Order is preserved within each category; the dictionary does not encode a
global ordering across categories or source positions.

The input must be the resume's text, not a filename. The function does not
read or write files, normalize aliases, remove duplicates, classify candidates,
or invoke the team's other modules. Its returned dictionary provides in-memory
storage and is JSON-serializable. Downstream modules can consume it; agreeing
and connecting their interfaces is still a separate integration step.

From `resumeLeans`, inspect the full sample result without writing an output file:

```powershell
python -B -c "import json; from pathlib import Path; from src.extraction.regex_extractor import extract_resume_info; text = Path('data/resume_example.txt').read_text(encoding='utf-8'); print(json.dumps(extract_resume_info(text), indent=2, ensure_ascii=False))"
```

## Shared regex concepts

Python concatenates adjacent string literals into one pattern. The `r` prefix
keeps backslashes available to the regex engine. `+` means one or more, `*`
means zero or more, `?` means optional, and `{n}` means exactly `n` repetitions.
`{2,}` means at least two. Character classes in `[...]` select one character;
the hyphen is literal when placed first or last. `|` means alternative. `\.` and `\+`
match literal punctuation. `\w` includes Unicode word characters.

`(?:...)` groups without capturing. Therefore `re.findall(pattern, text)`
returns whole matches as strings. Negative lookbehind `(?<!...)` and negative
lookahead `(?!...)` check surrounding characters without consuming them.
The phone pattern uses literal spaces instead of `\s` so it does not join
digit groups across line breaks.

## Example and execution

`data/resume_example.txt` contains a fictional candidate with contact,
experience, education, and technical skills. Contact information and supported technical terms are
extracted by this module. Expected results:

```python
emails = ['Wednesday.Addams@example.com']
phones = ['+57 300 123 4567']
programming_languages = ['JS']
frameworks = ['React.js', 'NodeJS']
databases = ['Postgres']
tools = ['Git']
education = ["Bachelor's degree in Systems Engineering"]
experience = ['3 years of experience']
other_qualifications = []
```

From the `resumeLeans` directory, run the extraction component's tests:

```powershell
python -B -m unittest discover -s tests -p test_extraction.py -v
```

To try the contact functions on the example file:

```powershell
python -B -c "from pathlib import Path; from src.extraction.regex_extractor import extract_emails, extract_phones; text = Path('data/resume_example.txt').read_text(encoding='utf-8'); print('Emails:', extract_emails(text)); print('Phones:', extract_phones(text))"
```

Python 3.9 or newer is sufficient. No third-party package is required for
this component or its `unittest` tests. The rest of the repository may require
additional dependencies (for example, automata tests import pytest). This
command runs only the extraction tests; use `python -m pytest` to run the full suite. Extraction tests can also be collected
with pytest when it is installed in the team's environment.

## Test design

Sixty-one test methods in `tests/test_extraction.py` cover:

- Common email syntax, subdomains, plus addressing and surrounding punctuation.
- Original email case, order and repeated occurrences.
- Missing email components and common malformed address fragments.
- Compact and separated phones, with and without `+57`, beginning with `3` or `60`.
- Original phone separators, order and repeated occurrences.
- Phone extraction from prose without a contact heading.
- Empty text, dates, incorrect lengths, unsupported prefixes, embedded numbers,
  and digit groups split over lines.
- Both extractors applied to the actual example file.
- Language names and abbreviations with case variations.
- Original language order and repeated occurrences in prose.
- Language separators, punctuation, and line breaks.
- Empty input, longer words, and other technology categories, including `React.js`.
- Language extraction from the actual example file, producing only `["JS"]`.

Expected outputs are literal values, independent of the expressions.

Six framework test methods cover all listed web and data/ML variants, original
case/order/repetitions in prose, punctuation and line breaks between mentions,
longer words, malformed dotted names, unsupported line-wrapped names, empty text,
other categories, and the example resume result `["React.js", "NodeJS"]`.

Eight database/tool test methods cover the supported names, original case,
order and duplicates, prose without headings, punctuation and line breaks,
empty text, other categories, longer words and dotted fragments, and the
example resume results `["Postgres"]` and `["Git"]`.

Five education tests cover degree/field spellings, original case and spacing,
curly apostrophes, repetitions, prose boundaries, unsupported/incomplete phrases,
and the sample resume. Six experience tests cover numeric formats, units,
modifiers, original case/spacing/order/repetitions, prose, date ranges without
inferred durations, invalid or unsupported phrases, and the sample resume.

Three additional-qualification tests cover the listed concepts and variants,
preservation of case/spacing/repeats, absent matches and avoidance of inference
from product names. Three combined-interface tests assert complete dictionaries
for the sample resume, empty input, and mixed prose with repeated mentions.
Expected dictionaries are hand-written independently of the extraction functions.

Seven additional-profile tests cover all added DevOps/data tool aliases,
CI/CD/ETL/warehouse forms, original case and spacing, repetitions, longer-word
false positives, and complete extraction dictionaries for DevOps and Data
Engineer prose. These are extraction tests, not assertions of profile acceptance.

Ten regression tests cover alias alignment, nonoverlapping short/long phrases,
No SQL preservation, py versus Py Torch, numeric ranges, compound durations,
engineering degrees, and rejection of unsupported compound academic fields.

## Documentation review and corrected cases

The following outputs were checked against the implementation during the
2026-10-11 review and subsequent correction. The first four rows now have
automated regression coverage. The remaining rows describe known limitations;
this is not a claim of exhaustive testing.

| Function and input | Actual output | Implication |
| --- | --- | --- |
| Education: `Bachelor of Engineering in Systems Engineering` | `["Bachelor of Engineering in Systems Engineering"]` | Engineering degrees now match. |
| Education: `PhD in Computer Science and Mathematics` | `["PhD in Computer Science and Mathematics"]` | The supported compound field is preserved. |
| Experience: `3 - 5 years of experience` | `["3 - 5 years of experience"]` | Both endpoints are preserved; no exact total is inferred. |
| Experience: `3 years and 6 months of experience` | `["3 years and 6 months of experience"]` | Both components are preserved without aggregation. |
| Languages: `No Python experience. Python.js` | `["Python", "Python"]` | Negation and filenames are not distinguished from affirmative skill mentions. |
| Other qualifications: `2 years of experience developing predictive models and data-processing pipelines.` | `[]` | This wording from the ML example does not match the exact model-development phrase; interpreting equivalent descriptions in prose is outside the current scope. |

The extraction suite contains 61 test methods. Run `python -m pytest` from
`resumeLeans/` to check all modules, including their integration. See
[test cases](test-cases.md) for the latest recorded results.

Documentation completeness: all nine extraction patterns have explanations,
input/output contracts, examples and automated test coverage. The combined
dictionary has integration tests for the extraction functions. This establishes
documented behavior only. Cross-stage fixtures for all four profiles are in
`tests/test_integration.py`; a real-world CV benchmark remains outside this test suite.

## General limitations

- Email extraction does not implement the complete email standard. Quoted local
  parts, several uncommon symbols, internationalized addresses and IP-literal
  domains are unsupported. Length and domain/mailbox existence are not checked.
- Boundary checks prevent common partial matches, but unsupported formats may
  still yield fragments. For example, unsupported local-part punctuation or
  a foreign phone prefix with multiple spaces can bypass the boundary guards.
- Phones with parentheses inside the number, extensions, dots, multiple spaces
  between groups, other country prefixes, or seven-digit local forms are outside
  the supported format. An extension may be left outside a matched base number.
- Phone prefix checks do not verify allocation of individual mobile ranges or
  geographic codes. A matching identification number can be a false positive.
- A preceding digit plus space, such as a numbered list marker, can prevent a
  phone match. This is a tradeoff of the guard against foreign-prefix fragments.
- Neither contact extractor determines who owns a detail or whether it works.
- All eight assignment categories have an initial extractor, but each is limited
  to the documented formats/vocabulary. An empty list means no supported match,
  not proof that the candidate lacks the qualification.
- PDF reading, OCR correction, normalization and classification are outside
  this component. Downstream integration is tested. Wider format coverage remains
  a possible extension; no claim of full assignment completion is made here.
