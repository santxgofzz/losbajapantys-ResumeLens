# ResumeLens - Qualification Profile Patterns

## Purpose

This document defines the qualification patterns that will be recognized during stage 3 of ResumeLens.

The finite automata do not process the original resume text directly.

The processing pipeline is:

1. Stage 1 extracts relevant information from the resume
2. Stage 2 normalizes equivalent textual representations into canonical symbols
3. Stage 2 organizes the normalized qualifications in a canonical order
4. Stage 3 evaluates the resulting sequence using the automaton associated with each professional profile

ResumeLens supports four professional profiles:

- Full Stack Developer
- Machine Learning Engineer 
- DevOps Engineer
- Data Engineer

The first two profiles are defined by the project statement. DevOps Engineer and Data Engineer are two addittional profiles selected by the team.

# General Design Decisions

## Canonical symbols

The automata will only process canonical symbols produced by the normalization
stage.

For example:

```text
JS -> JAVASCRIPT
React.js -> REACT
NodeJS -> NODE_JS
Postgres -> POSTGRESQL