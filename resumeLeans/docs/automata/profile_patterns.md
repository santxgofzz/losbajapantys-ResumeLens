# ResumeLens - Qualification Profile Patterns

## Purpose

This document defines the qualification patterns that will be recognized during stage 3 of ResumeLens.

The finite automata do not process the original resume text directly.

The processing pipeline is:

1. Stage 1 extracts relevant information from the resume
2. Stage 2 normalizes equivalent textual representations into canonical symbols
3. Stage 2 organizes the normalized qualifications in a canonical order
4. Stage 3 evaluates the resulting sequence using the automaton associated with esach professional profile

ResumeLens supports four professional profiles:

- Full Stack Developer
- Machine Learning Engineer
- DevOps Engineer
- Data Engineer

The first two profiles are defined by the project statement. DevOps Engineer and Data Engineer are two addittional profiles selected by the team.

---

## General Design Decisions

### Canonical symbols

The automata will only process canonical symbols produced by the normalization stage.

For example:

```text
JS -> JAVASCRIPT
React.js -> REACT
NodeJS -> NODE_JS
Postgres -> POSTGRESQL
```

Therefore, an automaton transition will use JAVASCRIPT, not JS.

### Canonical order

The order in which qualifications appear in a résumé should not determine the classification result.

Before a sequence is processed by an automaton, the relevant normalized qualifications are organized according to the canonical order defined for that professional profile.

For example, the résumé may contain:

```text
Git, Postgres, React.js, JS, NodeJS
```

After extraction, normalization and ordering, the Full Stack Developer automaton may receive:

```text
JAVASCRIPT, REACT, NODE_JS, POSTGRESQL, GIT
```

### Profile-specific evaluation

Each professional profile is evaluated independently.

Qualifications that do not belong to the alphabet of the profile being evaluated are not part of the sequence sent to that profile's automaton.

This allows a candidate to contain additional qualifications without being automatically rejected.

For example, a Data Engineer candidate could also contain DOCKER or REACT. Those qualifications do not invalidate the Data Engineer pattern.

---

## 1. Full Stack Developer

### Description

The Full Stack Developer profile represents a candidate with qualifications in frontend development, backend development, databases, APIs and version control.

### Qualification categories

**Programming language**

Accepted symbols:

- JAVASCRIPT
- TYPESCRIPT

**Frontend technology**

Accepted symbols:

- REACT
- ANGULAR
- VUE

**Backend technology**

Accepted symbols:

- NODE_JS
- DJANGO
- SPRING_BOOT

**Database**

Accepted symbols:

- SQL
- POSTGRESQL
- NOSQL

**API**

Required symbol:

- REST_API

**Version control**

Required symbol:

- GIT

### Canonical pattern

```text
(JAVASCRIPT | TYPESCRIPT)
(REACT | ANGULAR | VUE)
(NODE_JS | DJANGO | SPRING_BOOT)
(SQL | POSTGRESQL | NOSQL)
REST_API
GIT
```

### Example accepted sequence

```text
JAVASCRIPT, REACT, NODE_JS, POSTGRESQL, REST_API, GIT
```

### Example rejected sequence

```text
JAVASCRIPT, REACT, POSTGRESQL, REST_API, GIT
```

The sequence is rejected because it does not contain an accepted backend technology.

---

## 2. Machine Learning Engineer

### Description

The Machine Learning Engineer profile represents a candidate with qualifications in Python programming, data-processing libraries, machine-learning technologies, databases and version control.

### Qualification categories

**Programming language**

Required symbol:

- PYTHON

**Data-processing library**

Accepted symbols:

- PANDAS
- NUMPY

**Machine-learning technology**

Accepted symbols:

- SCIKIT_LEARN
- TENSORFLOW
- PYTORCH

**Database**

Accepted symbols:

- SQL
- POSTGRESQL

**Version control**

Required symbol:

- GIT

### Canonical pattern

```text
PYTHON
(PANDAS | NUMPY)
(SCIKIT_LEARN | TENSORFLOW | PYTORCH)
(SQL | POSTGRESQL)
GIT
```

### Additional qualification

MACHINE_LEARNING may also be extracted and normalized when the résumé explicitly mentions machine-learning model development.

However, it is not mandatory in the initial acceptance pattern because the reference qualification sequence can be recognized using the technical qualifications defined above.

### Example accepted sequence

```text
PYTHON, PANDAS, TENSORFLOW, SQL, GIT
```

### Example rejected sequence

```text
PYTHON, PANDAS, SQL, GIT
```

The sequence is rejected because it does not contain an accepted machine-learning technology.

---

## 3. DevOps Engineer

### Description

The DevOps Engineer profile represents a candidate with qualifications related to operating systems, containerization, orchestration, continuous integration and deployment, cloud platforms, infrastructure as code and version control.

### Qualification categories

**Operating system**

Required symbol:

- LINUX

**Containerization**

Required symbol:

- DOCKER

**Container orchestration**

Required symbol:

- KUBERNETES

**CI/CD technology**

Accepted symbols:

- JENKINS
- GITHUB_ACTIONS
- GITLAB_CI

**Cloud platform**

Accepted symbols:

- AWS
- AZURE
- GCP

**Infrastructure as Code**

Required symbol:

- TERRAFORM

**Version control**

Required symbol:

- GIT

### Canonical pattern

```text
LINUX
DOCKER
KUBERNETES
(JENKINS | GITHUB_ACTIONS | GITLAB_CI)
(AWS | AZURE | GCP)
TERRAFORM
GIT
```

### Example accepted sequence

```text
LINUX, DOCKER, KUBERNETES, GITHUB_ACTIONS, AWS, TERRAFORM, GIT
```

### Example rejected sequence

```text
LINUX, DOCKER, GITHUB_ACTIONS, AWS, TERRAFORM, GIT
```

The sequence is rejected because it does not contain KUBERNETES.

---

## 4. Data Engineer

### Description

The Data Engineer profile represents a candidate with qualifications related to programming, databases, data integration, distributed data technologies, workflow orchestration, data warehouses and version control.

### Qualification categories

**Programming language**

Required symbol:

- PYTHON

**Database/query technology**

Accepted symbols:

- SQL
- POSTGRESQL

**Data integration**

Required symbol:

- ETL

**Distributed data technology**

Accepted symbols:

- SPARK
- KAFKA

**Workflow orchestration**

Required symbol:

- AIRFLOW

**Data storage architecture**

Required symbol:

- DATA_WAREHOUSE

**Version control**

Required symbol:

- GIT

### Canonical pattern

```text
PYTHON
(SQL | POSTGRESQL)
ETL
(SPARK | KAFKA)
AIRFLOW
DATA_WAREHOUSE
GIT
```

### Example accepted sequence

```text
PYTHON, SQL, ETL, SPARK, AIRFLOW, DATA_WAREHOUSE, GIT
```

### Example rejected sequence

```text
PYTHON, SQL, SPARK, AIRFLOW, DATA_WAREHOUSE, GIT
```

The sequence is rejected because it does not contain ETL.

---

## Summary of Qualification Patterns

| Profile | Accepted Pattern |
|---|---|
| Full Stack Developer | Language -> Frontend -> Backend -> Database -> REST API -> Git |
| Machine Learning Engineer | Python -> Data Library -> ML Technology -> Database -> Git |
| DevOps Engineer | Linux -> Docker -> Kubernetes -> CI/CD -> Cloud -> Terraform -> Git |
| Data Engineer | Python -> Database -> ETL -> Distributed Data Technology -> Airflow -> Data Warehouse -> Git |

These patterns will be formally represented and implemented as finite automata in the following development stages.