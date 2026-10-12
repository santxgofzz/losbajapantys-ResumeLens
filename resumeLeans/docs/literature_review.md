# Technical source review

This review summarizes the official documentation used to explain the tools and design choices in ResumeLens.

## Extraction with regular expressions

Python's [regular-expression reference](https://docs.python.org/3/library/re.html) explains matching, alternatives, boundaries, repetitions and flags. ResumeLens uses these facilities to recognize finite vocabularies and explicit contact/qualification forms. Returning matches unchanged preserves the evidence needed by the next stage. This approach is explainable but does not resolve negation or infer expertise from prose.

## Normalization and recognition

The [pyformlang FST documentation](https://pyformlang.readthedocs.io/en/latest/modules/fst.html) exposes character transitions with output sequences and translation of input words. This supports an executable mapping from alias routes to canonical tokens, including case alternatives and whitespace loops. The [finite-automaton reference](https://pyformlang.readthedocs.io/en/latest/modules/finite_automaton.html) supplies deterministic automata and acceptance operations. ResumeLens separates transformation from recognition: the FST produces skill identifiers; each DFA checks a sequence prepared for its profile.

The team defined the qualification categories for each profile. These sources explain how to implement the models; they do not evaluate the chosen job requirements.

## Structured candidate language

The [textX project documentation](https://textx.github.io/textX/) describes building a parser and Python metamodel from a language definition. This supports a concrete DSL with repeated candidate records, followed by Python checks for cross-record constraints. The project's cited paper is Dejanovic, I., Vaderna, R., Milosavljevic, G., and Vukovic, Z. (2017), *TextX: A Python tool for Domain-Specific Languages implementation*, Knowledge-Based Systems 115, 1-4, DOI [10.1016/j.knosys.2016.10.023](https://doi.org/10.1016/j.knosys.2016.10.023). The explanation above is based on the official documentation, which also lists this paper as a reference.

## Design implications

Each tool has a specific role: finding text, normalizing skills, checking profile patterns or reading the candidate language. A finite vocabulary is suitable for demonstrating the formal models, while broader resume understanding would require additional scope and evaluation data. The project does not rank candidates. Tests use synthetic inputs and establish regression behavior, not population-level accuracy. Exact runtime dependencies are listed in `requirements.txt`; online documentation versions may differ from installed packages.
