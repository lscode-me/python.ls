# JSON - Quiz

Test your knowledge on "JSON: Syntax, Validation, and Tools" with a bioinformatics focus.

---

## Question 1: JSON Data Types

How many data types does JSON support?

A) 10

B) 4

C) 8

D) 6

---

## Question 2: Strings in JSON

Which quotes are used for strings in JSON?

A) Double quotes `"`

B) Backticks `` ` ``

C) Any quotes

D) Single quotes `'`

---

## Question 3: Comments

Does standard JSON support comments?

A) Yes, with /* */

B) No, comments are not supported

C) Yes, with #

D) Yes, with //

---

## Question 4: Trailing Comma

Which JSON is valid?

A) `{"name": "Alice", "age": 30,}`

B) `{'name': 'Alice', 'age': 30}`

C) `{name: "Alice", age: 30}`

D) `{"name": "Alice", "age": 30}`

---

## Question 5: Numbers in JSON

Which number is NOT valid in JSON?

A) 3.14

B) 0xFF

C) 42

D) 1e10

---

## Question 6: Null in JSON

How is null written in JSON?

A) Null

B) NULL

C) None

D) null

---

## Question 7: Object Keys

Which object key is valid in JSON?

A) 'name'

B) @name

C) "name"

D) name

---

## Question 8: jq Formatting

Which jq command formats JSON?

A) `jq . file.json`

B) `jq --pretty file.json`

C) `jq -p file.json`

D) `jq -f file.json`

---

## Question 9: jq Field Extraction

How do you extract the `name` field from JSON using jq?

A) jq [name] file.json

B) jq get name file.json

C) jq name file.json

D) jq .name file.json

---

## Question 10: jq Raw Output

Which jq flag outputs strings without quotes?

A) -r

B) `-s`

C) `-c`

D) `-n`

---

## Question 11: Python JSON Serialization

Which method converts a Python dict to a JSON string?

A) `json.loads()`

B) json.dumps()

C) `json.dump()`

D) `json.load()`

---

## Question 12: Python Reading Files

Which method reads JSON from a file?

A) `json.read(file)`

B) `json.parse(file)`

C) json.load(file)

D) `json.loads(file)`

---

## Question 13: Escape Characters

How do you write a newline in a JSON string?

A) "line1\\nline2"

B) "line1

C) "line1/nline2"

D) "line1\nline2"

---

## Question 14: Boolean Values

How are boolean values written in JSON?

A) `True` / `False`

B) `1` / `0`

C) true / false

D) `TRUE` / `FALSE`

---

## Question 15: Arrays

Which array is valid in JSON?

A) `{1, 2, 3}`

B) [1, 2, 3]

C) `[1, 2, 3,]`

D) `(1, 2, 3)`

---

## Question 16: JSON Schema

What is JSON Schema used for?

A) Converting JSON to XML

B) Validating the structure of JSON documents

C) Compressing JSON

D) Encrypting JSON

---

## Question 17: ISO 8601 Dates

In which format is it recommended to store dates in JSON?

A) "01/15/2024"

B) "2024-01-15T10:30:00Z"

C) "January 15, 2024"

D) 1705312200

---

## Question 18: JSON Encoding

What is the standard encoding for JSON?

A) ASCII

B) Latin-1

C) UTF-16

D) UTF-8

---

## Question 19: jq Select Filter

How do you filter array elements with a condition in jq?

A) `jq '.[] | if .active'`

B) `jq '.[] | where(.active)'`

C) jq '.[] | select(.active == true)'

D) `jq '.[] | filter(.active)'`

---

## Question 20: JSON Lines

What is JSON Lines (JSONL)?

A) A format where each line is a separate JSON object

B) JSON with comments

C) JSON split into parts

D) Compressed JSON

---

## Question 21: 🧬 Gene Annotation JSON

Which JSON correctly represents a gene annotation?

A) `{gene_name: BRCA2, chromosome: "chr13"}`

B) `{"gene_name": "BRCA2", "chromosome": "chr13"}`

C) `{'gene_name': 'BRCA2', 'chromosome': 'chr13'}`

D) `{"gene_name": "BRCA2", "chromosome": "chr13",}`

---

## Question 22: 🧬 Sample ID Format

For a bioinformatics pipeline, which is the best way to store sample IDs?

A) As numbers: `{"sample_id": 123}`

B) As strings: `{"sample_id": "SAM123"}`

C) As arrays: `{"sample_id": ["SAM", 123]}`

D) As booleans: `{"sample_id": true}`

---

## Question 23: 🧬 Quality Scores

Which JSON correctly stores Phred quality scores?

A) `{"quality": [35, 37, 39, 40]}`

B) `{"quality": "35,37,39,40"}`

C) `{"quality": {35, 37, 39, 40}}`

D) `{"quality": (35, 37, 39, 40)}`

---

## Question 24: 🧬 jq Filtering Variants

You have variants in JSON. How would you extract only pathogenic variants using jq?

```json
[
  {"id": "rs123", "significance": "pathogenic"},
  {"id": "rs456", "significance": "benign"}
]
```

A) `jq '.[] | select(.significance == "pathogenic")'`

B) `jq 'filter(.significance == "pathogenic")'`

C) `jq 'where .significance == "pathogenic"'`

D) `jq '.pathogenic'`

---

## Question 25: 🧬 Python Sample Metadata

Which Python code correctly writes sample metadata to JSON?

A) 
```python
json.dump(sample, "metadata.json")
```

B) 
```python
with open("metadata.json", "w") as f:
    json.dump(sample, f)
```

C) 
```python
json.write(sample, "metadata.json")
```

D) 
```python
with open("metadata.json", "w") as f:
    f.write(sample)
```

---

## Question 26: 🧬 Gene Symbols with Special Characters

How should you store a gene symbol like "TNF-α" in JSON?

A) Escape the α: `{"gene": "TNF-\\u03B1"}`

B) Use UTF-8 directly: `{"gene": "TNF-α"}`

C) Replace with Latin: `{"gene": "TNF-a"}`

D) Use HTML entity: `{"gene": "TNF-&alpha;"}`

---

## Question 27: 🧬 Coverage Null vs Zero

A sample has no coverage data available yet. What's the best representation?

A) `{"coverage": 0}`

B) `{"coverage": null}`

C) `{"coverage": ""}`

D) `{"coverage": "N/A"}`

---

## Question 28: 🧬 jq Average Coverage

Given samples with coverage data, how do you calculate average coverage in jq?

```json
[
  {"sample": "S1", "coverage": 30},
  {"sample": "S2", "coverage": 35}
]
```

A) `jq 'avg(.coverage)'`

B) `jq '[.[].coverage] | add / length'`

C) `jq '.coverage | mean'`

D) `jq 'sum(.coverage) / count'`

---

## Question 29: 🧬 Experimental Timestamps

Which is the correct way to store an experiment timestamp in JSON?

A) `{"date": "2024/01/15 10:30"}`

B) `{"date": 1705312200}`

C) `{"date": "2024-01-15T10:30:00Z"}`

D) `{"date": "January 15, 2024"}`

---

## Question 30: 🧬 JSON Lines for Large Data

Why would you use JSON Lines (.jsonl) for variant calling results?

A) It's more compressed than regular JSON

B) It allows processing large files line-by-line without loading everything into memory

C) It's faster to parse than JSON

D) It supports comments

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | JSON supports 6 types: string, number, boolean, null, array, object. |
| 2 | A | JSON uses only double quotes for strings. |
| 3 | B | Standard JSON does not support comments. JSONC and JSON5 do. |
| 4 | D | Trailing comma and unquoted keys are invalid in JSON. |
| 5 | B | Hexadecimal numbers (`0xFF`) are not supported in JSON. |
| 6 | D | Null is written in lowercase: `null` (not NULL, not None). |
| 7 | C | Object keys ALWAYS in double quotes: `"name"`. |
| 8 | A | `jq .` formats and validates JSON. |
| 9 | D | `.name` — jq syntax for accessing a field. |
| 10 | A | `-r` (raw output) prints strings without quotes. |
| 11 | B | `json.dumps()` — dump string, converts to string. |
| 12 | C | `json.load(file)` reads from file object. `loads()` — from string. |
| 13 | D | `\n` — escape sequence for newline. |
| 14 | C | JSON uses lowercase `true` and `false` (not Python True/False). |
| 15 | B | Trailing comma in arrays is invalid in JSON. |
| 16 | B | JSON Schema describes structure for validating JSON documents. |
| 17 | B | ISO 8601 (`2024-01-15T10:30:00Z`) — standard date format. |
| 18 | D | Per RFC 8259, JSON must be in UTF-8 (without BOM). |
| 19 | C | `select(.condition)` filters elements in jq. |
| 20 | A | JSON Lines — format where each line is a separate JSON object. |
| 21 | B | 🧬 Correct: double quotes, no trailing comma. |
| 22 | B | 🧬 Sample IDs should be strings to preserve leading zeros and format. |
| 23 | A | 🧬 Array of numbers is correct for quality scores. |
| 24 | A | 🧬 `select()` with equality condition filters variants. |
| 25 | B | 🧬 Correct: use file handle with `json.dump()`. |
| 26 | B | 🧬 UTF-8 encoding in JSON handles special characters naturally. |
| 27 | B | 🧬 Use `null` when data is unavailable; 0 means zero coverage (different meaning). |
| 28 | B | 🧬 Extract coverage values into array, sum, and divide by length. |
| 29 | C | 🧬 ISO 8601 format is standard for timestamps. |
| 30 | B | 🧬 JSON Lines allows streaming/line-by-line processing for large datasets. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **27-30 correct (90-100%)** | 🏆 Excellent! | You know JSON well! Move on to YAML. |
| **21-26 correct (70-89%)** | ✅ Good | Good result! Practice more with jq and bioinformatics examples. |
| **15-20 correct (50-69%)** | ⚠️ Satisfactory | Review the syntax and error sections, especially bioinformatics use cases. |
| **Less than 15 correct (<50%)** | 📚 Needs Review | Recommended to re-read the lecture and practice with real biological data. |

---

## 🧬 Bioinformatics JSON Practice Ideas

1. **Query Ensembl API**: Use `curl` and `jq` to fetch and parse gene annotations
2. **Sample Tracking**: Create a JSON schema for sample metadata validation
3. **Variant Filtering**: Write jq queries to filter variants by quality, depth, or clinical significance
4. **Pipeline Configuration**: Design a JSON config file for a bioinformatics pipeline
5. **JSON Lines Processing**: Process large variant files in JSONL format using Python generators

---
