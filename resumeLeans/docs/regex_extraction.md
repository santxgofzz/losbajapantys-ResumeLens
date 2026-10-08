# Regular-expression extraction: contact information

## Objective

Extract explicitly written contact information using Python's standard `re`
module. This increment implements emails and Colombian-style phone numbers
only. It does not normalize text or evaluate candidate qualifications.
Programming languages, frameworks, databases, education, experience, tools,
and other qualifications will be implemented in later increments.

## Functions and storage

Both functions are defined in `src/extraction/regex_extractor.py`:

| Function | Input | Output |
| --- | --- | --- |
| `extract_emails(text)` | Resume text as a `str` | `list[str]` of matching email addresses |
| `extract_phones(text)` | Resume text as a `str` | `list[str]` of matching phone numbers |

Each returned list stores the extracted information in memory. Empty input or
text without matches produces `[]`. Matches retain original capitalization,
separators, order, and repeated occurrences. Neither function reads files,
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
experience, education, and technical skills. Only contact information is
extracted in this increment. Expected results:

```python
emails = ['Wednesday.Addams@example.com']
phones = ['+57 300 123 4567']
```

From the `resumeLeans` directory, run all current tests:

```powershell
python -B -m unittest discover -s tests -v
```

To try both functions on the example file:

```powershell
python -B -c "from pathlib import Path; from src.extraction.regex_extractor import extract_emails, extract_phones; text = Path('data/resume_example.txt').read_text(encoding='utf-8'); print('Emails:', extract_emails(text)); print('Phones:', extract_phones(text))"
```

Python 3.9 or newer is sufficient. No third-party package is required for
this component or its `unittest` tests. Tests also work with pytest when it
is installed in the team's environment.

## Test design

Eight test methods in `tests/test_extraction.py` cover:

- Common email syntax, subdomains, plus addressing and surrounding punctuation.
- Original email case, order and repeated occurrences.
- Missing email components and common malformed address fragments.
- Compact and separated phones, with and without `+57`, beginning with `3` or `60`.
- Original phone separators, order and repeated occurrences.
- Phone extraction from prose without a contact heading.
- Empty text, dates, incorrect lengths, unsupported prefixes, embedded numbers,
  and digit groups split over lines.
- Both extractors applied to the actual example file.

Expected outputs are literal values, independent of the expressions.

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
