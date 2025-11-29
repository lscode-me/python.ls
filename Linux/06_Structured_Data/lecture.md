# Structured Data Processing (JSON, CSV, YAML, XML)

## Sample Data Files

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

---

## Overview
Modern data comes in structured formats. This lecture covers tools for processing JSON, CSV, YAML, and XML in Unix pipelines.

## JSON Processing with jq

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
```bash
# Stream processing
cat events.jsonl | jq -c 'select(.type == "error")'

# Convert JSON array to JSONL
jq -c '.[]' users.json > users.jsonl

# Convert JSONL to JSON array
jq -s '.' users.jsonl > users.json

# Aggregate
cat sales.jsonl | jq -s 'map(.amount) | add'
```

## CSV Processing

### csvkit Suite
```bash
# csvstat - Summary statistics
csvstat data.csv

# csvlook - Pretty print
csvlook data.csv | head

# csvcut - Extract columns
csvcut -c 1,3,5 data.csv

# csvgrep - Filter rows
csvgrep -c status -m "active" users.csv

# csvsort - Sort
csvsort -c age -r data.csv

# csvjoin - Join files
csvjoin -c id file1.csv file2.csv
```

### Miller (mlr)
```bash
# Pretty print
mlr --csv --opprint cat data.csv

# Filter
mlr --csv filter '$age > 30' users.csv

# Select columns
mlr --csv cut -f name,age users.csv

# Stats
mlr --csv stats1 -a sum,mean -f price sales.csv

# Group by
mlr --csv stats1 -a sum -f amount -g customer sales.csv

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
mlr --csv cut -f amount sales.csv | awk 'NR>1 {sum+=$1} END {print sum}'
```

## YAML Processing with yq

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
yq -P '.' data.json
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

### xq (yq for XML)
```bash
# XML to JSON
xq '.' data.xml

# Extract data
xq '.root.users.user[] | .name' data.xml
```

## Practical Examples

### Example 1: JSON API → CSV
```bash
curl -s 'https://api.example.com/users' | \
  jq -r '.[] | [.id, .name, .email] | @csv' > users.csv
```

### Example 2: CSV → JSON → Filter → CSV
```bash
mlr --csv --ojson cat input.csv | \
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
5. **Use --null-data** in jq for streaming
6. **Quote field names** in jq filters
7. **Test filters** on small samples first

## Summary

| Format | Tool | Key Command |
|--------|------|-------------|
| JSON | jq | `jq '.[] \| select(.age > 30)'` |
| CSV | mlr | `mlr --csv filter '$age > 30'` |
| YAML | yq | `yq '.database.host'` |
| XML | xmlstarlet | `xmlstarlet sel -t -v "//name"` |

## Next Steps
- Practice jq filters and transformations
- Explore mlr verbs (cut, filter, stats, join)
- Learn schema validation (jsonschema, csvlint)
- Study data serialization formats
