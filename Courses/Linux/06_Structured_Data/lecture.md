# Structured Data Processing (JSON, CSV, YAML, XML)

## Sample Data Files

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

---

## Overview
Modern data comes in structured formats — JSON for APIs, CSV for tabular data, YAML for configuration, XML for legacy systems. This module covers specialized CLI tools for processing these formats in Unix pipelines, enabling structured data processing without the need for loading data into a database or using a full programming environment.

## JSON Processing with jq

`jq` is a lightweight, functional language for processing JSON data. It reads JSON from stdin or a file, applies filters and transformations, and writes JSON (or text) to stdout. Because `jq` streams one value at a time, it can handle large files without loading everything into memory.

### Basic jq Usage
```bash
# Pretty print
echo '{"name":"John","age":30}' | jq '.'

# Extract field
echo '{"name":"John","age":30}' | jq '.name'

# Array access
echo '[1,2,3,4,5]' | jq '.[2]'  # 3

# Pipe data
cat users.json | jq '.[] | .name'
```

### jq Filters
```bash
# Select specific fields
jq '.[] | {name: .name, age: .age}' users.json

# Filter by condition
jq '.[] | select(.age > 25)' users.json

# Map operation
jq '[.[] | .price * 1.1]' products.json

# Group by
jq 'group_by(.category)' products.json

# Sort
jq 'sort_by(.age)' users.json
```

### JSONL (JSON Lines)

JSONL stores one JSON object per line, making it ideal for streaming pipelines. Unlike a JSON array, a JSONL file can be processed line by line without loading the entire file into memory.

```bash
# Stream processing
cat events.jsonl | jq -c 'select(.type == "error")'

# Convert JSON array to JSONL
jq -c '.[]' users.json > users.jsonl

# Convert JSONL to JSON array
jq -s '.' users.jsonl > users.json

# Aggregate total amount across all records
cat sales.jsonl | jq -s 'map(.amount) | add'
```

## CSV Processing

Standard Unix tools like `awk` and `cut` can work with CSV, but they break on quoted fields containing commas. The tools below — `csvkit` and `mlr` (Miller) — are CSV-aware and handle edge cases correctly.

### csvkit Suite
```bash
# csvstat - Summary statistics
csvstat data.csv

# csvlook - Pretty print
csvlook data.csv | head

# csvcut - Extract columns
csvcut -c 1,3,5 data.csv

# csvgrep - Filter rows (use regex for exact match)
csvgrep -c status -r '^active$' users.csv

# csvsort - Sort
csvsort -c age -r data.csv

# csvjoin - Join files
csvjoin -c id left.csv right.csv
```

### Miller (mlr)
```bash
# Pretty print
mlr --csv --opprint cat data.csv

# Filter
mlr --csv filter '$age > 30' data.csv

# Select columns
mlr --csv cut -f name,age data.csv

# Stats
mlr --csv stats1 -a sum,mean -f revenue sales.csv

# Group by
mlr --csv stats1 -a sum -f revenue -g region sales.csv

# Convert CSV to JSON
mlr --csv --ojson cat data.csv > data.json

# Convert JSON to CSV
mlr --json --ocsv cat data.json > data.csv
```

### awk for CSV
```bash
# Safe CSV parsing (handles quoted fields)
mlr --csv cat data.csv | awk -F',' '{print $2}'

# Sum column
mlr --csv cut -f revenue sales.csv | awk 'NR>1 {sum+=$1} END {print sum}'
```

## DuckDB: SQL for Files

DuckDB is an embedded analytical database that can query CSV, JSON, and Parquet files directly using SQL. It's like SQLite but optimized for analytics — it reads files in-place and is optimized for column-oriented analytical queries (aggregations, window functions, joins). It is particularly useful when `mlr` or `awk` one-liners are not expressive enough, or when you need to join multiple files using SQL.

### Installation
```bash
# macOS
brew install duckdb

# Ubuntu/Debian
wget https://github.com/duckdb/duckdb/releases/latest/download/duckdb_cli-linux-amd64.zip
unzip duckdb_cli-linux-amd64.zip

# Check installation
duckdb --version
```

### Basic Usage
```bash
# Query CSV directly
duckdb -c "SELECT * FROM 'users.csv' WHERE status = 'active'"

# Pretty markdown output
duckdb -c ".mode markdown" -c "SELECT * FROM 'users.csv'"

# JSON output
duckdb -c ".mode json" -c "SELECT * FROM 'users.csv'"
```

### Reading Different Formats
```bash
# CSV with auto-detection
duckdb -c "SELECT * FROM read_csv_auto('users.csv')"

# JSON files
duckdb -c "SELECT * FROM read_json_auto('users.json')"

# JSONL (newline-delimited JSON)
duckdb -c "SELECT * FROM read_json_auto('events.jsonl', format='newline_delimited')"

# Parquet files
duckdb -c "SELECT * FROM read_parquet('data.parquet')"
```

### Data Transformations
```bash
# Select specific columns
duckdb -c "SELECT name, email FROM 'users.csv'"

# Filter rows
duckdb -c "SELECT * FROM 'users.csv' WHERE city = 'Moscow' AND status = 'active'"

# Aggregations
duckdb -c "SELECT category, COUNT(*), AVG(price) FROM 'products.csv' GROUP BY category"

# Order results
duckdb -c "SELECT * FROM 'products.csv' ORDER BY price DESC LIMIT 5"
```

### Joins Across Files
```bash
# Join CSV files
duckdb -c "
  SELECT u.name, u.email, o.amount, o.date
  FROM 'users.csv' u
  JOIN 'orders.csv' o ON u.id = o.customer_id
  WHERE u.status = 'active'
"

# Left join
duckdb -c "
  SELECT u.*, o.amount
  FROM 'users.csv' u
  LEFT JOIN 'orders.csv' o ON u.id = o.customer_id
"
```

### Advanced Analytics
```bash
# Window functions
duckdb -c "
  SELECT 
    name, 
    price,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as rank
  FROM 'products.csv'
"

# Common Table Expressions (CTE)
duckdb -c "
  WITH active_users AS (
    SELECT * FROM 'users.csv' WHERE status = 'active'
  )
  SELECT city, COUNT(*) as user_count
  FROM active_users
  GROUP BY city
  ORDER BY user_count DESC
"

# Percentiles
duckdb -c "
  SELECT 
    category,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) as median_price,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY price) as p95_price
  FROM 'products.csv'
  GROUP BY category
"
```

### Export Results
```bash
# Export to CSV
duckdb -c "COPY (
  SELECT * FROM 'users.csv' WHERE status = 'active'
) TO 'active_users.csv' (HEADER, DELIMITER ',')"

# Export to JSON
duckdb -c "COPY (
  SELECT * FROM 'users.csv'
) TO 'users_export.json'"

# Export to Parquet (compressed, fast)
duckdb -c "COPY (
  SELECT * FROM 'users.csv'
) TO 'users.parquet' (FORMAT PARQUET)"
```

### Interactive Mode
```bash
# Start interactive shell
duckdb

# Inside DuckDB shell
D SELECT * FROM 'users.csv';
D .mode markdown
D SELECT city, COUNT(*) FROM 'users.csv' GROUP BY city;
D .quit
```

### DuckDB vs Other Tools

| Feature | DuckDB | mlr | csvkit | jq |
|---------|--------|-----|--------|-----|
| Query Language | SQL | DSL | CLI | JSON DSL |
| Joins | ✅ Complex | ✅ Basic | ✅ Basic | ❌ Manual |
| Window Functions | ✅ Full | ❌ | ❌ | ❌ |
| Performance (GB+) | ✅ Fast | ✅ Fast | ⚠️ Slow | ⚠️ Slow |
| Memory Usage | ✅ Low | ✅ Low | ❌ High | ❌ High |
| Learning Curve | ⚠️ SQL | ⚠️ Medium | ✅ Easy | ⚠️ Medium |

### When to Use Which Tool

**Use DuckDB when:**
- Complex joins across multiple files
- Analytical queries (GROUP BY, window functions)
- Working with large datasets (GB+)
- Need SQL interface
- Want to cache results in a database

**Use mlr/csvkit when:**
- Simple filtering/transformation
- Quick one-liners
- Prefer command-line DSL over SQL

**Use jq when:**
- Working primarily with JSON
- Need streaming processing
- Complex JSON transformations

## YAML Processing with yq

> **Note:** This module uses `yq` v4 (Mike Farah), whose syntax differs from other `yq` implementations. The `yq` package available via `apt` is a Python wrapper around `jq` and is not compatible with options such as `-o json`. Install `yq` v4 using the [official binary](https://github.com/mikefarah/yq) to follow the examples correctly.

```bash
# View YAML
yq '.' config.yaml

# Extract field
yq '.database.host' config.yaml

# Modify field
yq '.database.port = 5432' config.yaml

# Convert YAML to JSON
yq -o json '.' config.yaml

# Convert JSON to YAML
yq -P '.' users.json
```

## XML Processing

### xmlstarlet
```bash
# Pretty print
xmlstarlet format data.xml

# Extract elements
xmlstarlet sel -t -v "//user/name" -n data.xml

# Count elements
xmlstarlet sel -t -v "count(//user)" data.xml

# Filter
xmlstarlet sel -t -m "//user[age>25]" -v "name" -n data.xml

# Transform
xmlstarlet ed -u "//user[@id='1']/name" -v "NewName" data.xml
```

### yq for XML

> **Note:** In recent `yq` v4, XML is handled natively via input format flags. The separate `xq` binary no longer exists.

```bash
# XML to JSON
yq -p xml -o json '.' data.xml

# Extract data
yq -p xml -o json -r '.root.users.user[].name' data.xml
```

## Practical Examples

### Example 1: JSON API → CSV
```bash
curl -s 'https://api.example.com/users' | \
  jq -r '.[] | [.id, .name, .email] | @csv' > users.csv
```

### Example 2: CSV → JSON → Filter → CSV
```bash
mlr --csv --ojson cat users.csv | \
  jq '.[] | select(.status == "active")' | \
  jq -s '.' | \
  mlr --json --ocsv cat > output.csv
```

### Example 3: Aggregate JSON Stream
```bash
cat events.jsonl | \
  jq -s 'group_by(.user_id) | map({user: .[0].user_id, count: length})'
```

### Example 4: Multi-File JSON Merge
```bash
jq -s 'add' file1.json file2.json file3.json > merged.json
```

## Best Practices

1. **Use jq for JSON**: Most powerful and widespread
2. **Use mlr for CSV**: Handles edge cases better than awk
3. **JSONL for streaming**: One object per line
4. **Validate data** before processing
5. **Use `jq -n`** (`--null-input`) when constructing JSON from scratch without reading from a file
6. **Quote field names** in jq filters
7. **Test filters** on small samples first

## Summary

| Format | Tool | Key Command |
|--------|------|-------------|
| JSON | jq | `jq '.[] | select(.age > 30)'` |
| CSV | mlr | `mlr --csv filter '$age > 30'` |
| CSV/JSON/Parquet | DuckDB | `duckdb -c "SELECT * FROM 'data.csv' WHERE age > 30"` |
| YAML | yq | `yq '.database.host'` |
| XML | xmlstarlet | `xmlstarlet sel -t -v "//name"` |

## Next Steps
- Practice jq filters and transformations
- Explore mlr verbs (cut, filter, stats, join)
- Learn DuckDB SQL for analytical queries
- Compare performance: DuckDB vs mlr vs pandas
- Learn schema validation (jsonschema, csvlint)
- Study data serialization formats (Parquet, Arrow)
