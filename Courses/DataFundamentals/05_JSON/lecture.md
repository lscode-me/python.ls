# JSON
## Syntax, Validation, and Processing Tools for Bioinformatics

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand text formats (Module 04_FileFormats)
- Know the basics of character encodings (UTF-8)
- Have a basic understanding of data structures

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Read and write valid JSON
- Validate JSON and find syntax errors
- Use `jq` for processing JSON on the command line
- Work with JSON in Python and other languages
- Understand JSON limitations and workarounds
- Process biological data stored in JSON format

---

## 1. What is JSON

### 1.1 Definition

**JSON** (JavaScript Object Notation) — a text-based data interchange format.

- Invented by Douglas Crockford in the early 2000s
- Standardized: ECMA-404, RFC 8259
- Language-independent
- Human-readable

### 1.2 Where JSON is Used

| Domain | Application |
|--------|------------|
| Web APIs | REST API requests and responses |
| Configuration | package.json, tsconfig.json, tool configs |
| Databases | MongoDB, PostgreSQL JSONB columns |
| Logging | Structured logging |
| Data Exchange | Between services, client-server communication |

**🧬 In Bioinformatics:**

| Domain | Application |
|--------|------------|
| APIs | NCBI E-utilities, Ensembl REST API, UniProt API |
| Metadata | Experimental metadata, sample descriptions |
| Tool Config | Bioinformatics pipeline configurations |
| Annotations | Gene annotations, variant annotations |
| Results | Analysis results from tools like bcftools, bedtools |

### 1.3 Example JSON

**Generic Example:**

```json
{
  "name": "Alice",
  "age": 30,
  "isActive": true,
  "balance": null,
  "skills": ["Python", "SQL", "Docker"],
  "address": {
    "city": "Boston",
    "zip": "02101"
  }
}
```

**🧬 Bioinformatics Example (Sample Metadata):**

```json
{
  "sample_id": "PAT001",
  "patient_age": 45,
  "diagnosis": "Type 2 Diabetes",
  "sequenced": true,
  "coverage": 30.5,
  "platform": "Illumina NovaSeq",
  "tissue_types": ["blood", "liver"],
  "quality_metrics": {
    "phred_score": 35,
    "gc_content": 0.42
  },
  "variants_called": null
}
```

---

## 2. JSON Syntax

### 2.1 Data Types

JSON supports **6 data types**:

| Type | Example | Description |
|------|---------|-------------|
| String | `"hello"` | String in double quotes |
| Number | `42`, `3.14`, `-5`, `1e10` | Integer or floating-point |
| Boolean | `true`, `false` | Boolean value |
| Null | `null` | Absence of value |
| Array | `[1, 2, 3]` | Ordered list |
| Object | `{"key": "value"}` | Set of key-value pairs |

### 2.2 Strings

```json
{
  "simple": "Hello, World!",
  "unicode": "Привет, мир! 你好 🎉",
  "escaped": "Line 1\nLine 2\tTabbed",
  "quotes": "He said \"Hello\"",
  "path": "C:\\Users\\name",
  "special": "\u0041",
  "gene": "TNF-α"
}
```

**Escape sequences:**

| Sequence | Meaning |
|----------|---------|
| `\"` | Double quote |
| `\\` | Backslash |
| `\/` | Forward slash (optional) |
| `\n` | Newline |
| `\r` | Carriage return |
| `\t` | Tab |
| `\b` | Backspace |
| `\f` | Form feed |
| `\uXXXX` | Unicode character |

**🧬 Bioinformatics Note:**  
Gene names often contain special characters (TNF-α, IL-1β). UTF-8 encoding in JSON handles these naturally without escape sequences.

### 2.3 Numbers

```json
{
  "integer": 42,
  "negative": -17,
  "float": 3.14159,
  "exponent": 1.5e10,
  "negativeExp": 2.5e-3,
  "coverage": 30.5,
  "quality_score": 35
}
```

**Not supported:**

- Leading zeros: `007` ❌
- Hexadecimal: `0xFF` ❌
- Infinity, NaN ❌
- Octal: `0o755` ❌

**🧬 Note:** Quality scores, coverage values, and p-values are commonly stored as JSON numbers.

### 2.4 Arrays

```json
{
  "numbers": [1, 2, 3, 4, 5],
  "strings": ["apple", "banana", "cherry"],
  "mixed": [1, "two", true, null],
  "nested": [[1, 2], [3, 4]],
  "empty": [],
  "chromosomes": ["chr1", "chr2", "chr3"],
  "gene_ids": ["ENSG00000139618", "ENSG00000141510"],
  "phred_scores": [35, 37, 39, 40]
}
```

### 2.5 Objects

```json
{
  "patient": {
    "id": "PAT001",
    "age": 45,
    "diagnosis": "Type 2 Diabetes"
  },
  "sequencing": {
    "platform": "Illumina",
    "quality": {
      "phred": 35,
      "gc_content": 0.42
    }
  }
}
```

**Rules:**

- Keys ALWAYS in double quotes
- Key order is not guaranteed
- Duplicate keys — undefined behavior

### 2.6 Complete Example (Gene Annotation)

```json
{
  "gene_id": "ENSG00000139618",
  "gene_name": "BRCA2",
  "chromosome": "chr13",
  "start": 32889611,
  "end": 32973805,
  "strand": "+",
  "biotype": "protein_coding",
  "is_canonical": true,
  "expression_level": 125.5,
  "aliases": ["FANCD1", "BRCC2"],
  "description": "BRCA2 DNA repair associated",
  "go_terms": null,
  "variants": [
    {
      "variant_id": "rs80359550",
      "position": 32912299,
      "ref": "A",
      "alt": "G",
      "clinical_significance": "pathogenic"
    },
    {
      "variant_id": "rs80359505",
      "position": 32913055,
      "ref": "C",
      "alt": "T",
      "clinical_significance": "likely_pathogenic"
    }
  ]
}
```

---

## 3. Common Errors

### 3.1 Trailing Comma

❌ **Error:**

```json
{
  "name": "Alice",
  "age": 30,
}
```

✅ **Correct:**

```json
{
  "name": "Alice",
  "age": 30
}
```

### 3.2 Single Quotes

❌ **Error:**

```json
{
  'name': 'Alice'
}
```

✅ **Correct:**

```json
{
  "name": "Alice"
}
```

### 3.3 Comments

❌ **Error:**

```json
{
  "name": "Alice",  // patient name
  /* multi-line comment */
  "age": 30
}
```

✅ **JSON does not support comments!**

> **💡 Pro Tip:**  
> For configurations with comments, use YAML, JSONC (VS Code), or JSON5.

### 3.4 Unquoted Keys

❌ **Error:**

```json
{
  name: "Alice"
}
```

✅ **Correct:**

```json
{
  "name": "Alice"
}
```

### 3.5 Special Numbers

❌ **Error:**

```json
{
  "value": NaN,
  "max": Infinity
}
```

✅ **Alternatives:**

```json
{
  "value": null,
  "max": 1e308
}
```

---

## 4. JSON Validation

### 4.1 Command Line

```bash
# jq — validation and formatting
echo '{"name":"Alice"}' | jq .
# {
#   "name": "Alice"
# }

# Validate a file
jq . config.json

# If JSON is invalid — error
echo '{"name":}' | jq .
# parse error: Invalid numeric literal at line 1, column 9

# python -m json.tool
echo '{"name":"Alice"}' | python3 -m json.tool

# Syntax check
python3 -m json.tool config.json > /dev/null && echo "Valid JSON"
```

**🧬 Bioinformatics Example:**

```bash
# Validate gene annotation JSON
jq . gene_annotations.json

# Validate API response from Ensembl
curl -s "https://rest.ensembl.org/lookup/id/ENSG00000139618?content-type=application/json" | jq .

# Check experimental metadata
jq . experiment_metadata.json > /dev/null && echo "Metadata is valid"
```

### 4.2 Online Tools

- [JSONLint](https://jsonlint.com/) — validation
- [JSON Formatter](https://jsonformatter.org/) — formatting
- [jq play](https://jqplay.org/) — testing jq queries

### 4.3 Python Validation

```python
import json

def validate_json(json_string):
    """Validates a JSON string."""
    try:
        json.loads(json_string)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)

# Examples
valid, error = validate_json('{"name": "Alice"}')
print(f"Valid: {valid}")  # Valid: True

valid, error = validate_json('{"name": }')
print(f"Valid: {valid}, Error: {error}")
# Valid: False, Error: Expecting value: line 1 column 10 (char 9)
```

**🧬 Bioinformatics Example:**

```python
def validate_sample_metadata(metadata_str):
    """Validates sample metadata JSON."""
    try:
        data = json.loads(metadata_str)
        
        # Additional validation
        required_fields = ['sample_id', 'platform', 'coverage']
        missing = [f for f in required_fields if f not in data]
        
        if missing:
            return False, f"Missing required fields: {missing}"
        
        return True, None
    except json.JSONDecodeError as e:
        return False, f"JSON syntax error: {e}"

# Example
metadata = '{"sample_id": "PAT001", "platform": "Illumina", "coverage": 30.5}'
valid, error = validate_sample_metadata(metadata)
print(f"Valid: {valid}")
```

---

## 5. jq — Powerful JSON Tool

### 5.1 jq Basics

```bash
# Pretty print
cat data.json | jq .

# Compact output
jq -c . data.json

# Extract field
echo '{"name":"Alice","age":30}' | jq '.name'
# "Alice"

# Raw output (no quotes)
echo '{"name":"Alice"}' | jq -r '.name'
# Alice
```

**🧬 Bioinformatics Examples:**

```bash
# Extract gene name
echo '{"gene_id":"ENSG00000139618","gene_name":"BRCA2"}' | jq -r '.gene_name'
# BRCA2

# Get quality score
echo '{"sample":"PAT001","phred_score":35}' | jq '.phred_score'
# 35
```

### 5.2 Navigating Structure

```bash
# Nested fields
echo '{"user":{"name":"Alice"}}' | jq '.user.name'
# "Alice"

# Array element
echo '{"items":["a","b","c"]}' | jq '.items[0]'
# "a"

# All array elements
echo '{"items":["a","b","c"]}' | jq '.items[]'
# "a"
# "b"
# "c"

# Last element
echo '[1,2,3,4,5]' | jq '.[-1]'
# 5

# Slice
echo '[1,2,3,4,5]' | jq '.[1:3]'
# [2, 3]
```

**🧬 Bioinformatics Examples:**

```bash
# Extract nested annotation
echo '{"gene":{"annotation":{"function":"DNA repair"}}}' | jq '.gene.annotation.function'
# "DNA repair"

# Get first variant
echo '{"variants":[{"id":"rs123"},{"id":"rs456"}]}' | jq '.variants[0].id'
# "rs123"

# List all chromosomes
echo '{"data":[{"chr":"chr1"},{"chr":"chr2"}]}' | jq '.data[].chr'
# "chr1"
# "chr2"
```

### 5.3 Filtering and Transformation

```bash
# Sample data
cat > samples.json << 'EOF'
[
  {"sample_id": "PAT001", "coverage": 30, "qc_pass": true},
  {"sample_id": "PAT002", "coverage": 15, "qc_pass": false},
  {"sample_id": "PAT003", "coverage": 35, "qc_pass": true}
]
EOF

# Filter by condition
jq '.[] | select(.qc_pass == true)' samples.json
# {"sample_id": "PAT001", "coverage": 30, "qc_pass": true}
# {"sample_id": "PAT003", "coverage": 35, "qc_pass": true}

# Extract fields
jq '.[].sample_id' samples.json
# "PAT001"
# "PAT002"
# "PAT003"

# Create new object
jq '.[] | {id: .sample_id, cov: .coverage}' samples.json

# Convert to array
jq '[.[] | .sample_id]' samples.json
# ["PAT001", "PAT002", "PAT003"]

# High coverage samples
jq '[.[] | select(.coverage > 20)]' samples.json
```

**🧬 Advanced Filtering:**

```bash
# Genes on specific chromosome
cat > genes.json << 'EOF'
[
  {"gene": "BRCA1", "chr": "chr17", "length": 81189},
  {"gene": "BRCA2", "chr": "chr13", "length": 84195},
  {"gene": "TP53", "chr": "chr17", "length": 19149}
]
EOF

jq '[.[] | select(.chr == "chr17")]' genes.json

# Long genes (> 50kb)
jq '[.[] | select(.length > 50000) | .gene]' genes.json
# ["BRCA1", "BRCA2"]
```

### 5.4 Data Modification

```bash
# Add field
echo '{"name":"Alice"}' | jq '. + {age: 30}'
# {"name": "Alice", "age": 30}

# Update field
echo '{"name":"Alice","age":30}' | jq '.age = 31'
# {"name": "Alice", "age": 31}

# Delete field
echo '{"name":"Alice","age":30}' | jq 'del(.age)'
# {"name": "Alice"}

# Update nested
echo '{"user":{"name":"Alice"}}' | jq '.user.name = "Bob"'
# {"user": {"name": "Bob"}}
```

**🧬 Bioinformatics Examples:**

```bash
# Add QC status
echo '{"sample":"PAT001","coverage":30}' | jq '. + {qc_status: "pass"}'

# Update annotation
echo '{"gene":"BRCA2","function":null}' | jq '.function = "DNA repair"'

# Add calculated field
echo '{"reads":1000000,"mapped":950000}' | \
  jq '. + {mapping_rate: (.mapped / .reads * 100)}'
```

### 5.5 Aggregation

```bash
# Count elements
jq 'length' samples.json
# 3

# Sum
echo '[1,2,3,4,5]' | jq 'add'
# 15

# Average coverage
jq '[.[].coverage] | add / length' samples.json
# 26.67

# Sort
jq 'sort_by(.coverage)' samples.json

# Group
jq 'group_by(.qc_pass)' samples.json

# Unique values
echo '["chr1","chr2","chr1","chr3","chr2"]' | jq 'unique'
# ["chr1", "chr2", "chr3"]
```

**🧬 Statistical Analysis:**

```bash
# Total sequencing coverage
cat > experiments.json << 'EOF'
[
  {"sample": "S1", "reads": 1000000},
  {"sample": "S2", "reads": 1500000},
  {"sample": "S3", "reads": 1200000}
]
EOF

jq '[.[].reads] | add' experiments.json
# 3700000

# Average read count
jq '[.[].reads] | add / length' experiments.json
# 1233333.33

# Samples with above-average reads
jq 'map(select(.reads > 1233333))' experiments.json
```

### 5.6 Practical Examples

```bash
# Extract all emails from API response
curl -s https://api.example.com/users | jq '.[].email'

# Convert JSON to CSV
jq -r '.[] | [.sample_id, .coverage] | @csv' samples.json
# "PAT001",30
# "PAT002",15
# "PAT003",35

# Find high coverage samples
jq '[.[] | select(.coverage > 25)]' samples.json

# Count by condition
jq '[.[] | select(.qc_pass)] | length' samples.json
# 2

# Format for report
jq -r '.[] | "Sample: \(.sample_id), Coverage: \(.coverage)x"' samples.json
# Sample: PAT001, Coverage: 30x
# Sample: PAT002, Coverage: 15x
# Sample: PAT003, Coverage: 35x
```

**🧬 Real Bioinformatics Workflows:**

```bash
# Query Ensembl API and extract gene info
curl -s "https://rest.ensembl.org/lookup/id/ENSG00000139618?content-type=application/json" | \
  jq '{gene: .display_name, chr: .seq_region_name, start: .start, end: .end}'

# Process variant calling results
jq '[.variants[] | select(.quality > 30 and .depth > 20)]' variants.json

# Extract pathogenic variants
jq '[.variants[] | select(.clinical_significance == "pathogenic")]' clinvar.json

# Generate sample summary
jq 'group_by(.qc_pass) | map({status: .[0].qc_pass, count: length})' samples.json
```

---

## 6. JSON in Python

### 6.1 Basic Operations

```python
import json

# Python dict → JSON string
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"]
}

json_string = json.dumps(data)
print(json_string)
# {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}

# With formatting
pretty_json = json.dumps(data, indent=2)
print(pretty_json)
# {
#   "name": "Alice",
#   "age": 30,
#   "skills": ["Python", "SQL"]
# }

# JSON string → Python dict
parsed = json.loads(json_string)
print(parsed["name"])  # Alice
```

**🧬 Bioinformatics Example:**

```python
# Sample metadata
sample = {
    "sample_id": "PAT001",
    "age": 45,
    "diagnosis": "Type 2 Diabetes",
    "sequencing_platform": "Illumina NovaSeq",
    "coverage": 30.5,
    "qc_pass": True
}

# Export to JSON
json_string = json.dumps(sample, indent=2)
print(json_string)

# Parse from string
parsed_sample = json.loads(json_string)
print(f"Sample {parsed_sample['sample_id']} coverage: {parsed_sample['coverage']}x")
```

### 6.2 Working with Files

```python
import json

# Write to file
data = {"samples": [{"id": "PAT001"}, {"id": "PAT002"}]}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Read from file
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)
```

**🧬 Bioinformatics Example:**

```python
# Save gene annotations
annotations = {
    "gene_id": "ENSG00000139618",
    "gene_name": "BRCA2",
    "chromosome": "chr13",
    "variants": [
        {"id": "rs80359550", "clinical_significance": "pathogenic"},
        {"id": "rs80359505", "clinical_significance": "likely_pathogenic"}
    ]
}

with open("brca2_annotation.json", "w", encoding="utf-8") as f:
    json.dump(annotations, f, indent=2, ensure_ascii=False)

# Load annotations
with open("brca2_annotation.json", "r", encoding="utf-8") as f:
    gene_data = json.load(f)
    print(f"Gene: {gene_data['gene_name']}")
    print(f"Variants: {len(gene_data['variants'])}")
```

### 6.3 Error Handling

```python
import json

def safe_parse_json(json_string):
    """Safely parse JSON."""
    try:
        return json.loads(json_string), None
    except json.JSONDecodeError as e:
        return None, {
            "error": str(e),
            "line": e.lineno,
            "column": e.colno,
            "position": e.pos
        }

# Example
data, error = safe_parse_json('{"name": invalid}')
if error:
    print(f"Error at line {error['line']}, column {error['column']}: {error['error']}")
```

### 6.4 Custom Serialization

```python
import json
from datetime import datetime, date
from decimal import Decimal

class CustomEncoder(json.JSONEncoder):
    """Custom encoder for types not natively supported by JSON."""
    
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

# Usage
data = {
    "timestamp": datetime.now(),
    "price": Decimal("19.99"),
    "tags": {"python", "json"}
}

json_string = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_string)
```

**🧬 Bioinformatics Example:**

```python
from datetime import datetime
from decimal import Decimal

class BioinfoEncoder(json.JSONEncoder):
    """Encoder for bioinformatics data types."""
    
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, set):
            return sorted(list(obj))  # Sort for reproducibility
        return super().default(obj)

# Experimental results
experiment = {
    "experiment_id": "EXP001",
    "date": datetime.now(),
    "p_value": Decimal("0.00123"),
    "significant_genes": {"BRCA1", "BRCA2", "TP53"},
    "fold_changes": [1.5, 2.3, -1.8]
}

json_output = json.dumps(experiment, cls=BioinfoEncoder, indent=2)
print(json_output)
```

### 6.5 Working with Large Files

```python
import json

# For very large files — line-by-line reading (JSON Lines)
def read_jsonl(filepath):
    """Reads a JSON Lines file (one JSON object per line)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

# Write JSON Lines
def write_jsonl(filepath, items):
    """Writes an iterable as JSON Lines."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(json.dumps(item) + '\n')

# Usage
users = [{"name": "Alice"}, {"name": "Bob"}]
write_jsonl("users.jsonl", users)

for user in read_jsonl("users.jsonl"):
    print(user)
```

**🧬 Bioinformatics Example (Processing Large Variant Files):**

```python
def process_variants_jsonl(input_file, output_file, min_quality=30):
    """
    Filter variants from JSON Lines format.
    Useful for large variant calling results.
    """
    filtered_count = 0
    
    with open(output_file, 'w', encoding='utf-8') as out:
        for variant in read_jsonl(input_file):
            if variant.get('quality', 0) >= min_quality:
                out.write(json.dumps(variant) + '\n')
                filtered_count += 1
    
    return filtered_count

# Usage
# Process millions of variants without loading all into memory
count = process_variants_jsonl("all_variants.jsonl", "high_quality_variants.jsonl")
print(f"Filtered {count} high-quality variants")
```

---

## 7. JSON Schema

### 7.1 What is JSON Schema

**JSON Schema** — a way to describe the structure of a JSON document for validation.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "age": {
      "type": "integer",
      "minimum": 0,
      "maximum": 150
    },
    "email": {
      "type": "string",
      "format": "email"
    }
  },
  "required": ["name", "email"]
}
```

**🧬 Bioinformatics Example (Sample Metadata Schema):**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Sample Metadata",
  "type": "object",
  "properties": {
    "sample_id": {
      "type": "string",
      "pattern": "^[A-Z]{3}[0-9]{3}$"
    },
    "patient_age": {
      "type": "integer",
      "minimum": 0,
      "maximum": 120
    },
    "coverage": {
      "type": "number",
      "minimum": 0
    },
    "platform": {
      "type": "string",
      "enum": ["Illumina NovaSeq", "Illumina HiSeq", "PacBio", "Oxford Nanopore"]
    },
    "qc_pass": {
      "type": "boolean"
    }
  },
  "required": ["sample_id", "platform", "coverage"]
}
```

### 7.2 Schema Validation in Python

```python
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["name"]
}

# Valid data
valid_data = {"name": "Alice", "age": 30}
validate(valid_data, schema)  # OK

# Invalid data
invalid_data = {"age": -5}
try:
    validate(invalid_data, schema)
except ValidationError as e:
    print(f"Validation error: {e.message}")
    # Validation error: 'name' is a required property
```

**🧬 Bioinformatics Example:**

```python
from jsonschema import validate, ValidationError

sample_schema = {
    "type": "object",
    "properties": {
        "sample_id": {
            "type": "string",
            "pattern": "^[A-Z]{3}[0-9]{3}$"
        },
        "coverage": {
            "type": "number",
            "minimum": 10,
            "maximum": 100
        },
        "platform": {
            "type": "string",
            "enum": ["Illumina NovaSeq", "Illumina HiSeq", "PacBio"]
        }
    },
    "required": ["sample_id", "platform", "coverage"]
}

# Valid sample
valid_sample = {
    "sample_id": "PAT001",
    "platform": "Illumina NovaSeq",
    "coverage": 30.5
}

try:
    validate(valid_sample, sample_schema)
    print("✓ Sample metadata is valid")
except ValidationError as e:
    print(f"✗ Validation error: {e.message}")

# Invalid sample (bad sample ID format)
invalid_sample = {
    "sample_id": "invalid_id",
    "platform": "Illumina NovaSeq",
    "coverage": 30.5
}

try:
    validate(invalid_sample, sample_schema)
except ValidationError as e:
    print(f"✗ Validation error: {e.message}")
    # 'invalid_id' does not match '^[A-Z]{3}[0-9]{3}$'
```

---

## 8. Alternatives to JSON

### 8.1 When JSON is Not Suitable

| Limitation | Alternative |
|------------|-------------|
| No comments | YAML, TOML, JSON5 |
| Verbose for configs | YAML, TOML |
| No binary data | Base64 encoding, BSON |
| Slow parsing | MessagePack, Protocol Buffers |
| No schema | JSON Schema, TypeScript types |

**🧬 In Bioinformatics:**

| Use Case | Format | Reason |
|----------|--------|--------|
| Large genomic data | Binary (BAM, BCF) | Compact, fast |
| Pipeline configs | YAML | Readable, comments |
| API responses | JSON | Standard, interoperable |
| Metadata exchange | JSON | Universal support |
| High-performance data transfer | Protocol Buffers, MessagePack | Speed |

### 8.2 JSON5

```javascript
// JSON5 supports:
{
  // Comments
  name: 'Alice',  // Single quotes
  age: 30,        // Trailing comma OK
  'special-key': true,
}
```

### 8.3 JSONC (JSON with Comments)

```jsonc
{
  // VS Code uses JSONC for settings.json
  "editor.fontSize": 14,
  /* Multi-line
     comments too */
  "editor.tabSize": 2,
}
```

---

## 9. Best Practices

### 9.1 Key Naming

```json
// ✅ camelCase (JavaScript style)
{"firstName": "Alice", "lastName": "Smith"}

// ✅ snake_case (Python style)
{"first_name": "Alice", "last_name": "Smith"}

// ❌ Mixing styles
{"firstName": "Alice", "last_name": "Smith"}

// ❌ Spaces in keys
{"first name": "Alice"}
```

**🧬 Bioinformatics Convention:**  
Use `snake_case` for consistency with file formats (VCF, GFF) and Python code.

```json
{
  "sample_id": "PAT001",
  "gene_name": "BRCA2",
  "clinical_significance": "pathogenic"
}
```

### 9.2 Dates and Times

```json
// ✅ ISO 8601 format
{
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00+03:00",
  "experiment_date": "2024-01-15"
}

// ❌ Non-standard formats
{
  "date": "01/15/2024",
  "time": "10:30 AM"
}
```

### 9.3 Nullable Fields

```json
// ✅ Explicit null
{
  "middle_name": null,
  "variants_called": null
}

// ✅ Or omit the field
{
  "first_name": "Alice"
}

// ❌ Empty string instead of null
{
  "middle_name": ""
}
```

### 9.4 Numeric IDs

```json
// ⚠️ Large numbers may lose precision in JavaScript
{
  "id": 9007199254740993
}

// ✅ String IDs for large numbers
{
  "id": "9007199254740993",
  "gene_id": "ENSG00000139618"
}
```

**🧬 Note:** Gene IDs, transcript IDs, and patient IDs should always be strings to preserve leading zeros and avoid precision issues.

---

## 10. Common Pitfalls

### 10.1 File Encoding

❌ **Error:** Saving JSON in non-UTF-8 encoding

```python
# Always specify encoding
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
```

**🧬 Important for Bioinformatics:**  
Gene names with Greek letters (TNF-α, IL-1β) and patient names with diacritics require UTF-8.

### 10.2 Unescaped Strings

❌ **Error:**

```json
{"message": "Line 1
Line 2"}
```

✅ **Correct:**

```json
{"message": "Line 1\nLine 2"}
```

### 10.3 Decimal and Float

❌ **Problem:**

```python
import json
from decimal import Decimal

# Error!
json.dumps({"price": Decimal("19.99")})
# TypeError: Object of type Decimal is not JSON serializable
```

✅ **Solution:**

```python
json.dumps({"price": Decimal("19.99")}, default=str)
# or use CustomEncoder from section 6.4
```

**🧬 Important for p-values:**

```python
# P-values and statistical results
results = {
    "p_value": Decimal("0.00000123"),
    "fold_change": Decimal("2.5")
}

# Convert to float for JSON
json.dumps(results, default=float)
```

### 10.4 Circular References

❌ **Problem:**

```python
a = {"b": None}
b = {"a": a}
a["b"] = b

json.dumps(a)
# ValueError: Circular reference detected
```

✅ **Solution:** Avoid circular structures or use specialized libraries.

---

## 💡 Key Takeaways

- **JSON is a simple format**: 6 data types, strict syntax, no comments.

- **Validation is important**: Use `jq .` or `python -m json.tool` for validation.

- **jq is powerful**: Filtering, transformation, aggregation on the command line.

- **Encoding — UTF-8**: Always use UTF-8 and `ensure_ascii=False` for non-Latin characters.

- **Dates — ISO 8601**: Standard format `2024-01-15T10:30:00Z`.

- **🧬 Bioinformatics Applications**:
  - API responses from NCBI, Ensembl, UniProt
  - Experimental metadata and sample tracking
  - Tool configuration files
  - Structured logging for pipelines
  - Gene and variant annotations

---

## 🚀 Next Steps

**Related Modules:**

- [YAML](../06_YAML/) — more readable alternative for configurations
- [Data Transfer](../12_DataTransfer/) — Base64 for binary data in JSON

**Practice Ideas:**

1. Write a JSON validator for sample metadata with informative error messages
2. Create jq filters to process real APIs (Ensembl, NCBI E-utilities)
3. Implement a JSON → CSV converter for variant calling results
4. Write a JSON Schema for your bioinformatics project metadata

**Going Deeper:**

- Learn JSON Patch (RFC 6902) for partial updates
- Explore JSONPath as an alternative to jq
- Study BSON (Binary JSON) used in MongoDB for genomic databases

---

## 📚 Additional Resources

**Documentation:**

- [JSON.org](https://www.json.org/)
- [RFC 8259](https://datatracker.ietf.org/doc/html/rfc8259)
- [jq Manual](https://stedolan.github.io/jq/manual/)

**Tools:**

- [jq play](https://jqplay.org/)
- [JSON Schema](https://json-schema.org/)
- [JSONLint](https://jsonlint.com/)

**Bioinformatics APIs:**

- [Ensembl REST API](https://rest.ensembl.org/)
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [UniProt REST API](https://www.uniprot.org/help/api)

**Learning:**

- [jq Cookbook](https://github.com/stedolan/jq/wiki/Cookbook)
- [JSON Schema Tutorial](https://json-schema.org/learn/getting-started-step-by-step)

---
