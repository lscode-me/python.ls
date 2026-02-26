# YAML - Quiz

Test your knowledge on "YAML: Data Format for Configurations" with a bioinformatics focus.

---

## Question 1: YAML Acronym

What does the acronym YAML stand for?

A) Yet Another Markup Language

B) YAML Advanced Modeling Language

C) Your Application Markup Language

D) YAML Ain't Markup Language

---

## Question 2: Comments

How do you write a comment in YAML?

A) # comment

B) `/* comment */`

C) `-- comment`

D) `// comment`

---

## Question 3: Indentation

Which characters can be used for indentation in YAML?

A) Only tabs

B) Tabs and spaces

C) Any whitespace characters

D) Only spaces

---

## Question 4: Boolean Values

Which value is NOT interpreted as boolean in YAML 1.1?

A) `maybe`

B) `no`

C) `on`

D) `yes`

---

## Question 5: Norway Problem

What happens with `country: NO` in YAML 1.1?

A) Null

B) Syntax error

C) String "NO"

D) Boolean false

---

## Question 6: Multi-line Strings

Which syntax preserves line breaks in multi-line text?

A) `'''`

B) `>`

C) | 

D) `"""`

---

## Question 7: Flow Style

How do you write the list `[1, 2, 3]` in YAML flow style?

A) `items: (1, 2, 3)`

B) `items: {1, 2, 3}`

C) items: [1, 2, 3]

D) `items: <1, 2, 3>`

---

## Question 8: Anchors and Aliases

What is the purpose of `&name` and `*name` syntax in YAML?

A) For regular expressions

B) For comments

C) For environment variables

D) For anchors (definition) and aliases (usage)

---

## Question 9: Multiple Documents

What delimiter is used between documents in YAML?

A) ---

B) `===`

C) `***`

D) `~~~`

---

## Question 10: YAML vs JSON

Which statement is true?

A) YAML is a superset of JSON (from version 1.2)

B) They are incompatible

C) YAML is a binary format

D) JSON is a superset of YAML

---

## Question 11: Python safe_load

Why should you use `yaml.safe_load()` instead of `yaml.load()`?

A) yaml.load can execute arbitrary code

B) `safe_load` is faster

C) `safe_load` formats output better

D) `safe_load` supports more types

---

## Question 12: Data Types

How does YAML interpret the value `1.0` without quotes?

A) Integer 1

B) Floating-point number 1.0

C) Boolean true

D) String "1.0"

---

## Question 13: Null Values

Which variant is NOT null in YAML?

A) `value: ~`

B) `value:`

C) `value: null`

D) value: ""

---

## Question 14: Strings with Colons

How do you correctly write the string "Error: file not found"?

A) message: "Error: file not found"

B) `message: Error file not found`

C) `message: Error: file not found`

D) `message: Error\: file not found`

---

## Question 15: yq Command

Which command extracts the value of `port` from `server.port` using yq?

A) `yq get server.port file.yaml`

B) `yq select .server.port file.yaml`

C) yq eval '.server.port' file.yaml

D) `yq eval 'server.port' file.yaml`

---

## Question 16: Kubernetes

Which tool most commonly uses YAML?

A) Kubernetes

B) PostgreSQL

C) MySQL

D) Apache HTTP Server

---

## Question 17: YAML Version

Which YAML version solves the "Norway Problem"?

A) YAML 1.2

B) YAML 2.0

C) YAML 1.1

D) YAML 1.0

---

## Question 18: Validation

Which tool is used to check YAML file style?

A) jsonlint

B) yamlcheck

C) yamlvalidate

D) yamllint

---

## Question 19: Block vs Flow

Which style is recommended for configuration files?

A) JSON-compatible

B) Mixed

C) Block style (indentation)

D) Flow style (`{}`, `[]`)

---

## Question 20: Docker Compose

What is the default Docker Compose filename?

A) `compose.yaml` or `docker-compose.yml`

B) `docker.yaml`

C) `Dockerfile`

D) `container.yml`

---

## Question 21: 🧬 Snakemake Configuration

Which format does Snakemake primarily use for configuration?

A) JSON

B) YAML

C) TOML

D) INI

---

## Question 22: 🧬 Sample ID as String

You have a sample ID `001`. How should you write it in YAML to preserve leading zeros?

A) `sample_id: 001`

B) `sample_id: "001"`

C) `sample_id: !!int 001`

D) `sample_id: 0x001`

---

## Question 23: 🧬 Genome Version

You need to store genome version `38.0`. What's the correct way?

A) `genome_version: 38.0`

B) `genome_version: "38.0"`

C) `genome_version: !!str 38.0`

D) Both B and C are correct

---

## Question 24: 🧬 Gene Response Field

A field contains gene response status "NO". What happens in YAML 1.1?

A) Interpreted as string "NO"

B) Interpreted as boolean false

C) Interpreted as null

D) Syntax error

---

## Question 25: 🧬 Multi-line Sequence

You need to store a DNA sequence with line breaks preserved. Which syntax?

```yaml
sequence: |
  ATGCGATCGATCG
  ATCGATCGATCGA
```

A) `>` (folded)

B) | (literal)

C) `"""`

D) `'''`

---

## Question 26: 🧬 Conda Environment

Which file defines a Conda environment for bioinformatics tools?

A) `requirements.txt`

B) `Pipfile`

C) `environment.yaml`

D) `setup.py`

---

## Question 27: 🧬 Pipeline Anchors

You want to reuse alignment parameters for multiple samples. Which YAML feature?

A) Imports

B) Includes

C) Anchors and aliases

D) Templates

---

## Question 28: 🧬 yq Extract Sample IDs

Given a YAML config with samples, how do you extract all sample IDs?

```yaml
samples:
  - sample_id: PAT001
  - sample_id: PAT002
```

A) `yq eval '.samples.sample_id' config.yaml`

B) `yq eval '.samples[].sample_id' config.yaml`

C) `yq eval 'samples.*.sample_id' config.yaml`

D) `yq eval '.samples[*].sample_id' config.yaml`

---

## Question 29: 🧬 Quality Score Field

You store a Phred quality score. Which is correct?

A) `quality: 30` (number)

B) `quality: "30"` (string)

C) `quality: !!int 30`

D) A is correct for numeric operations

---

## Question 30: 🧬 CWL Workflow

Common Workflow Language (CWL) uses which format?

A) JSON only

B) YAML only

C) Both JSON and YAML

D) XML

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | YAML Ain't Markup Language — recursive acronym. |
| 2 | A | Comments in YAML start with `#`. |
| 3 | A | YAML allows ONLY spaces for indentation, tabs are forbidden. |
| 4 | A | `maybe` is a string. `yes`, `no`, `on`, `off` are boolean in YAML 1.1. |
| 5 | D | `NO` is interpreted as false in YAML 1.1 (Norway Problem). |
| 6 | A | `|` (literal block) preserves line breaks, `>` (folded) converts them to spaces. |
| 7 | C | Flow style uses `[]` for lists and `{}` for objects, like JSON. |
| 8 | D | `&name` creates an anchor, `*name` references it (alias). |
| 9 | A | `---` separates documents in YAML. |
| 10 | A | Valid JSON is valid YAML (starting with YAML 1.2). |
| 11 | A | `yaml.load()` can execute arbitrary Python code via tags. |
| 12 | B | `1.0` without quotes is a floating-point number. For string: `"1.0"`. |
| 13 | D | Empty string `""` is a string, not null. Others are null. |
| 14 | A | Quotes are needed for strings with `: ` (colon + space). |
| 15 | C | `.server.port` — yq syntax (leading dot is required). |
| 16 | A | Kubernetes widely uses YAML for manifests. |
| 17 | A | YAML 1.2 does not interpret `yes/no/on/off` as boolean. |
| 18 | D | yamllint is a linter for checking YAML files. |
| 19 | C | Block style (with indentation) is more readable for configurations. |
| 20 | A | `docker-compose.yml` or `compose.yaml` (new name). |
| 21 | B | 🧬 Snakemake uses YAML for `config.yaml` and workflow definitions. |
| 22 | B | 🧬 Quote to preserve leading zeros: `"001"`. |
| 23 | D | 🧬 Both quoting and explicit type tag work to preserve as string. |
| 24 | A | 🧬 "NO" is interpreted as false in YAML 1.1 — use quotes! |
| 25 | B | 🧬 `|` (literal block) preserves line breaks for sequences. |
| 26 | C | 🧬 `environment.yaml` defines Conda environments. |
| 27 | C | 🧬 Anchors (`&name`) and aliases (`*name`) allow parameter reuse. |
| 28 | B | 🧬 `.samples[]` iterates over array elements, `.sample_id` extracts field. |
| 29 | D | 🧬 Numeric quality scores should be numbers for calculations. |
| 30 | C | 🧬 CWL supports both JSON and YAML formats. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **27-30 correct (90-100%)** | 🏆 Excellent! | You know YAML well! Move on to Markup formats. |
| **21-26 correct (70-89%)** | ✅ Good | Good result! Review gotchas and data types. |
| **15-20 correct (50-69%)** | ⚠️ Satisfactory | Re-read the section on pitfalls and bioinformatics examples. |
| **Less than 15 correct (<50%)** | 📚 Needs Review | Recommended to re-read the lecture and practice with pipeline configs. |

---

## 🧬 Bioinformatics YAML Practice Ideas

1. **Snakemake Config**: Write a complete `config.yaml` for an RNA-Seq pipeline
2. **Conda Environment**: Create `environment.yaml` with bioinformatics tools (STAR, samtools, bcftools)
3. **Sample Sheet**: Design a YAML sample sheet with metadata (ID, condition, files)
4. **CWL Workflow**: Write a simple CWL workflow definition in YAML
5. **Tool Parameters**: Use anchors and aliases to share parameters across pipeline steps
6. **yq Practice**: Extract and modify values from pipeline configs using yq

---
