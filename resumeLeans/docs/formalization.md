# Formal model index

Each stage has a separate language and responsibility. This index links the complete stage definitions and explains their composition.

## 1. Regular-expression extraction

[Regex specification](regex_extraction.md) defines each pattern, recognized forms, examples and limitations. The implementation uses Python `re` on text and returns original substrings. Bounded lookarounds enforce lexical boundaries; no backreferences are used. Extraction does not decide equivalence or qualification acceptance.

## 2. Finite-state transduction

[FST definitions and transition diagrams](Transducers/Definiciones%20formales%20transducers.md) provide the seven-tuple, transition/output tables and graphical representation for each output-token component. The combined runtime FST is their union with disjoint internal states and shared initial/final states.

The transition relation consumes one character per edge; its associated output word is empty except at the last character of an alias. Alternative case edges and consuming whitespace loops recognize equivalent representations. There are no epsilon-input transitions. Nondeterminism allows aliases to share an initial character without sharing routes. All accepting paths for a supported alias must agree on the output token.

`normalizar_skills` collects outputs in a set and returns an alphabetically sorted list. This is distinct from the profile-specific preparation in Stage 3. Regenerate the reference after changing aliases or construction:

```bash
python -m scripts.document_transducers
```

## 3. Finite automata

[Profile patterns](automata/profile_patterns.md) and [five-tuples, transitions and diagrams](automata/finite_automata.md) specify the four DFAs. Their transition functions are partial in code: a missing transition rejects. A total mathematical DFA is obtained by adding a nonaccepting sink for all missing transitions and looping the sink over the alphabet.

Before recognition, the wrapper removes duplicates, ignores symbols outside the profile alphabet and orders the remaining symbols by category. Thus the DFA recognizes the prepared sequence, not the resume's original ordering. Category self-loops accept several alternatives in the same category. Acceptance requires every category in order; extra unrelated skills do not disqualify a candidate.

## 4. Candidate-profile grammar

[CFG and EBNF specification](CFG%20design.md) identifies terminals, nonterminals, ordered sections and repetition. `src/dsl/grammar.tx` implements the concrete syntax in textX. Parsing and application validation are distinct: uppercase unique skill IDs and exactly four unique evaluation names are checked in Python. Validation does not prove a stated qualification is true or recompute a manually supplied evaluation.

The renderer consumes validated structured data and HTML-escapes candidate text. Rendering does not participate in the formal classification model.
