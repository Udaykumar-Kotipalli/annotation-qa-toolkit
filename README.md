# Annotation QA Toolkit

A small rule-based toolkit for reviewing annotation records before delivery.

The project focuses on a simple idea: **turn written annotation rules into repeatable checks.**

## Checks

- Required fields
- Allowed labels
- Empty annotations
- Confidence score range
- Duplicate record IDs

## Run

```bash
python qa_check.py sample_annotations.csv
```

## Example

```text
ANNOTATION QA
-------------
Records:          8
Invalid labels:   1
Missing text:     1
Bad confidence:   0
Duplicate IDs:    1

Status: REVIEW REQUIRED
```

## Stack

Python · CSV · Rule-based validation
