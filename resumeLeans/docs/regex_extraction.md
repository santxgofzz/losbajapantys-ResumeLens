# Regular-expression extraction

## Objective

Extract explicitly written contact information and technical terms using
Python's standard `re` module. This increment implements emails, Colombian-style
phone numbers, programming languages, frameworks/libraries/runtimes, databases,
and tools below. It does not normalize text or evaluate candidate qualifications. Education, experience,
and other qualifications will be implemented in later increments.

## Step 4: initial programming-language vocabulary

This section defines the vocabulary and behavior of
`extract_programming_languages(text)`. The vocabulary is implemented in the Python pattern;
the function does not read this Markdown file.

| Language | Recognized names and abbreviations | Examples of case variants |
| --- | --- | --- |
| JavaScript | `JavaScript`, `JS` | `Javascript`, `javascript`, `js`, `JS` |
| TypeScript | `TypeScript`, `TS` | `Typescript`, `typescript`, `ts`, `TS` |
| Python | `Python` | `python`, `PYTHON` |
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
profiles. Additional languages can be added in later increments. Abbreviations
such as `JS` and `TS` can be ambiguous in prose; lexical extraction alone does
not prove that a mention represents a candidate's skill or proficiency.

## Functions and storage

All six functions are defined in `src/extraction/regex_extractor.py`:

| Function | Input | Output |
| --- | --- | --- |
| `extract_emails(text)` | Resume text as a `str` | `list[str]` of matching email addresses |
| `extract_phones(text)` | Resume text as a `str` | `list[str]` of matching phone numbers |
| `extract_programming_languages(text)` | Resume text as a `str` | `list[str]` of supported language mentions |
| `extract_frameworks(text)` | Resume text as a `str` | `list[str]` of supported frameworks, libraries and runtimes |
| `extract_databases(text)` | Resume text as a `str` | `list[str]` of supported database names |
| `extract_tools(text)` | Resume text as a `str` | `list[str]` of supported tool names |

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
PROGRAMMING_LANGUAGES_PATTERN = r"(?<![\w.])(?:JavaScript|JS|TypeScript|TS|Python|Java)\b"
```

- `(?<![\w.])` prevents a match immediately after a word character or a dot.
  The dot check prevents extracting `js` from `React.js` or `Node.js`.
- `(?:JavaScript|JS|TypeScript|TS|Python|Java)` lists the supported alternatives
  without capturing subgroups.
- `\b` requires a word boundary at the end, excluding suffixes such as
  `Python3`, `Pythonista`, and `JavaScriptCore`.
- `re.findall(..., flags=re.IGNORECASE)` accepts case variants while returning
  the original matched strings, with no normalization.

The language recognized consists of the six listed spellings in any letter
case, subject to these surrounding-character checks. The vocabulary is finite;
the function does not infer languages that are missing from the list.

The dot guard is a deliberate heuristic: it also excludes a language directly
after a sentence-ending dot without a space, such as `experience.Python`.
Names in URLs or contact details can still be matched in other positions.
Lexical matching does not establish proficiency or handle negation.

## Frameworks, libraries and runtimes

`extract_frameworks(text)` groups the following technologies for extraction.
Node.js is a runtime, not a framework; it is deliberately included in this
category. All listed spellings support case-insensitive matching and retain
their original representation in the output.

| Technology | Supported spellings |
| --- | --- |
| React | `React`, `React.js`, `ReactJS` |
| Angular | `Angular` |
| Vue | `Vue`, `Vue.js` |
| Node.js | `NodeJS`, `Node.js` |
| Django | `Django` |
| Spring Boot | `Spring Boot` |
| Pandas | `Pandas` |
| NumPy | `NumPy` |
| Scikit-learn | `Scikit-learn`, `scikit learn`, `sklearn` |
| TensorFlow | `TensorFlow`, `Tensor Flow` |
| PyTorch | `PyTorch`, `Py Torch` |

```python
FRAMEWORKS_PATTERN = (
    r"(?<![\w.])"
    r"(?:React(?:\.js|JS)?|Angular|Vue(?:\.js)?|Node(?:JS|\.js)|"
    r"Django|Spring Boot|Pandas|NumPy|Scikit[- ]learn|sklearn|"
    r"Tensor ?Flow|Py ?Torch)"
    r"(?!\w|\.\w)"
)
```

- `React(?:\.js|JS)?` accepts the full dotted or joined suffix, or bare `React`.
  `Vue(?:\.js)?` accepts `Vue.js` and `Vue`.
- `Node(?:JS|\.js)` requires a suffix, avoiding a match for the generic word `Node`.
- `Scikit[- ]learn` accepts a single hyphen or space; `sklearn` is another alternative.
- `Tensor ?Flow` and `Py ?Torch` accept zero or one literal space.
- `Spring Boot` requires one literal space. Multiword matches cannot span lines.
- `(?<![\w.])` prevents starting inside a word or after a dot.
- `(?!\w|\.\w)` prevents ending inside a word or immediately before a dotted
  continuation. This avoids partial matches such as `React` from `React.jsx`.
  A sentence-ending dot is allowed when it is not followed by a word character.
- `re.IGNORECASE` allows variants such as `react.js` and `PANDAS` without changing
  their spelling. Noncapturing groups keep each `findall` result a complete match.

The function searches the whole input and preserves order and duplicates.
For `I use React.js, NodeJS and sklearn.`, the result is
`["React.js", "NodeJS", "sklearn"]`. Empty input or no supported terms produces `[]`.

This is a finite initial vocabulary. Unlisted spellings, multiple internal
spaces, and line-wrapped names are unsupported. Word matching cannot distinguish
ordinary prose such as `react` or `pandas` from technology mentions, prove skill,
or interpret negation. Dotted boundary guards can miss names immediately after
a sentence-ending dot without whitespace. Names in URLs can still match.

## Databases and tools

The initial vocabulary is intentionally limited to these names, with any
capitalization. The expressions are defined in Python, not loaded from this document.

| Category | Supported names |
| --- | --- |
| Databases | `PostgreSQL`, `Postgres`, `MySQL`, `MongoDB` |
| Tools | `Git`, `Docker` |

```python
DATABASES_PATTERN = r"(?<![\w.])(?:PostgreSQL|Postgres|MySQL|MongoDB)(?!\w|\.\w)"
TOOLS_PATTERN = r"(?<![\w.])(?:Git|Docker)(?!\w|\.\w)"
```

Both functions use `re.findall` with `re.IGNORECASE`. The recognized language
is the finite set of listed names in any letter case, with boundary checks:

- `(?<![\w.])` excludes a start directly after a word character or dot.
- `(?:...|...)` groups alternative names without capturing subgroups.
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
not included in this database vocabulary. Their treatment as qualifications
can be defined in a later increment. GitHub and GitLab are not aliases for Git.

Limitations: unlisted products and spellings (such as `Mongo DB`) are not
recognized. The dot guard excludes a name immediately after a sentence-ending
dot without a space. A hyphen is a separator, so a supported name within a
hyphenated expression may match. Matching names alone cannot establish
proficiency, interpret negation, or rule out mentions in unrelated contexts.
This initial list still needs review against the team's four profiles.

## Shared regex concepts

Python concatenates adjacent string literals into one pattern. The `r` prefix
keeps backslashes available to the regex engine. `+` means one or more, `*`
means zero or more, `?` means optional, and `{n}` means exactly `n` repetitions.
`{2,}` means at least two. Character classes in `[...]` select one character;
the hyphen is literal when placed last. `|` means alternative. `\.` and `\+`
match literal punctuation. `\w` includes Unicode word characters.

`(?:...)` groups without capturing. Therefore `re.findall(pattern, text)`
returns whole matches as strings. Negative lookbehind `(?<!...)` and negative
lookahead `(?!...)` check surrounding characters without consuming them.
The phone pattern uses literal spaces instead of `\s` so it does not join
digit groups across line breaks.

## Example and execution

`data/resume_example.txt` contains a fictional candidate with contact,
experience, education, and technical skills. Contact information and supported technical terms are
extracted in this increment. Expected results:

```python
emails = ['Wednesday.Addams@example.com']
phones = ['+57 300 123 4567']
programming_languages = ['JS']
frameworks = ['React.js', 'NodeJS']
databases = ['Postgres']
tools = ['Git']
```

From the `resumeLeans` directory, run all current tests:

```powershell
python -B -m unittest discover -s tests -v
```

To try the contact functions on the example file:

```powershell
python -B -c "from pathlib import Path; from src.extraction.regex_extractor import extract_emails, extract_phones; text = Path('data/resume_example.txt').read_text(encoding='utf-8'); print('Emails:', extract_emails(text)); print('Phones:', extract_phones(text))"
```

Python 3.9 or newer is sufficient. No third-party package is required for
this component or its `unittest` tests. Tests also work with pytest when it
is installed in the team's environment.

## Test design

Twenty-seven test methods in `tests/test_extraction.py` cover:

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

## Limitations

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
- Neither extractor determines who owns the contact detail or whether it works.
- PDF reading, OCR correction, normalization, classification and the remaining
  extraction categories are outside this increment.
