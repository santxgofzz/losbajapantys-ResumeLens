# ResumeLens

ResumeLens is a project developed for the course **Computación y Estructuras Discretas III** at Universidad Icesi.

The main idea of the project is to process résumé text and identify if a candidate matches different professional profiles using concepts seen in class such as regular expressions, finite-state transducers, finite automata and context-free grammars.

The system works with four profiles:

- Full Stack Developer
- Machine Learning Engineer
- DevOps Engineer
- Data Engineer

ResumeLens does not rank candidates or make hiring decisions. It only checks if the qualifications found in a résumé match the patterns defined for each profile.

---

## How it works

The project is divided into different stages:

1. **Information extraction**
   - Regular expressions are used to find information from the résumé.
   - This includes emails, phone numbers, programming languages, frameworks, databases, education, experience and technologies.

2. **Normalization**
   - Finite-state transducers are used to convert different ways of writing the same technology into one standard form.
   - For example:

```text
JS -> JAVASCRIPT
React.js -> REACT
NodeJS -> NODE_JS
Postgres -> POSTGRESQL
Amazon Web Services -> AWS
```

3. **Profile classification**
   - Deterministic finite automata are used to check if the normalized skills match the qualification pattern of each profile.

4. **Candidate profile language**
   - A small DSL was created using a context-free grammar and textX.
   - It stores the candidate information, normalized skills and classification results.

5. **HTML visualization**
   - After the candidate profile is validated, the project generates a simple HTML file with the candidate information and the result of the classifications.

The general flow is:

```text
Resume text
    ↓
Regular Expressions
    ↓
Finite-State Transducers
    ↓
Finite Automata
    ↓
Candidate Profile DSL
    ↓
textX Validation
    ↓
HTML
```

---

## Project structure

```text
resumeLeans/
│
├── data/
│   ├── resume_example.txt
│   └── candidate_example.dsl
│
├── docs/
│   ├── automata/
│   ├── Transducers/
│   ├── regex_extraction.md
│   ├── CFG design.md
│   ├── design.md
│   ├── formalization.md
│   ├── test-cases.md
│   └── literature_review.md
│
├── src/
│   ├── extraction/
│   │   └── regex_extractor.py
│   │
│   ├── normalization/
│   │   └── transducers.py
│   │
│   ├── automata/
│   │   ├── classifiers.py
│   │   └── profile_definitions.py
│   │
│   ├── dsl/
│   │   ├── grammar.tx
│   │   ├── candidate_parser.py
│   │   └── visualizer.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_extraction.py
│   ├── test_normalization.py
│   ├── test_automata.py
│   ├── test_dsl.py
│   ├── test_visualization.py
│   └── test_integration.py
│
├── requirements.txt
└── README.md
```

---

## Requirements

To run the project you need:

- Python 3
- pip

The project also uses the libraries listed in `requirements.txt`.

---

## Create the virtual environment

From the repository root, enter the Python project folder first:

```bash
cd resumeLeans
```

Then create the virtual environment:

```bash
python -m venv .venv
```

### Activate it on Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

If it worked, the terminal should show something similar to:

```text
(.venv)
```

---

## Install dependencies

With the virtual environment activated, install the required libraries:

```bash
python -m pip install -r requirements.txt
```

The main external libraries used in the project are:

- `pyformlang`
- `textX`
- `pytest`

The Python `re` module is also used for regular expressions, but it is already included with Python.

---

## Run the project

To run the complete ResumeLens pipeline:

```bash
python -m src.main
```

The program uses the example résumé stored in:

```text
data/resume_example.txt
```

During execution, ResumeLens:

```text
extracts information
        ↓
normalizes qualifications
        ↓
evaluates the four profiles
        ↓
generates the candidate DSL
        ↓
validates it
        ↓
generates an HTML file
```

The generated files are stored in:

```text
output/candidate_profile.dsl
output/candidate_profile.html
```

---

## Open the generated HTML

On Windows PowerShell, the generated HTML can be opened with:

```powershell
start .\output\candidate_profile.html
```

It can also be opened manually from the `output` folder.

---

## Run the tests

To run all the tests:

```bash
python -m pytest -v
```

There are tests for:

- regular expression extraction
- skill normalization
- finite automata
- candidate-profile grammar
- HTML generation
- complete pipeline integration

---

## Supported profiles

### Full Stack Developer

The candidate must contain qualifications related to:

```text
Programming Language
Frontend
Backend
Database
REST API
Git
```

### Machine Learning Engineer

The candidate must contain qualifications related to:

```text
Python
Data Library
Machine Learning Technology
Database
Git
```

### DevOps Engineer

The candidate must contain qualifications related to:

```text
Linux
Docker
Kubernetes
CI/CD
Cloud
Terraform
Git
```

### Data Engineer

The candidate must contain qualifications related to:

```text
Python
Database
ETL
Distributed Data Technology
Airflow
Data Warehouse
Git
```

---

## Examples of normalization

Some examples of the normalization stage are:

```text
JS -> JAVASCRIPT
Javascript -> JAVASCRIPT

React.js -> REACT

NodeJS -> NODE_JS

Postgres -> POSTGRESQL

K8s -> KUBERNETES

GitHub Actions -> GITHUB_ACTIONS

Amazon Web Services -> AWS

Google Cloud Platform -> GCP
```

---

## Documentation

More detailed information about each part of the project can be found inside the `docs` folder.

Some of the main files are:

```text
docs/regex_extraction.md
docs/automata/finite_automata.md
docs/automata/profile_patterns.md
docs/CFG design.md
docs/design.md
docs/formalization.md
docs/test-cases.md
docs/literature_review.md
```

---

## Team

- Santiago Florez
- Juan Pablo Cubillos
- Juan Felipe Zuñiga

---

## Course

**Computación y Estructuras Discretas III**  
Universidad Icesi  
2026-2

## Integration notes

The FST recognizes ASCII case variants and repeated horizontal spaces/tabs in supported multiword aliases. Original extraction values are unchanged. Unknown aliases have no output. Java, MySQL and MongoDB are retained as JAVA, MYSQL and MONGODB; they do not imply a different skill or change the profile requirements.

The bundled example does not mention REST API, which is mandatory in the team's Full Stack pattern, so its rejection is expected. `main.py` supplies example personal data manually. For another candidate, call `process_resume(resume_text, personal_info)`; see [module contracts](docs/design.md).

The current FST definitions and Mermaid diagrams are generated from the implementation:

```bash
python -m scripts.document_transducers
```

The older PNG diagrams in `docs/Transducers/GRAPHICS` are historical; use the [generated reference](docs/Transducers/Definiciones%20formales%20transducers.md) for the current model.

See [test scenarios](docs/test-cases.md), [formalization](docs/formalization.md), and [technical sources](docs/literature_review.md) for more detail.
