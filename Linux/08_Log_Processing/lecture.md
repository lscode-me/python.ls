# Log Processing & Real-World Pipelines

## Overview
Process logs, APIs, and generate reports using Unix pipelines. This lecture covers JSONL logs, compressed streams, API integration, and markdown generation.

## JSONL Log Processing

### Structure of JSONL Logs
```bash
# One JSON object per line
{"timestamp":"2024-03-15T10:30:00Z","level":"INFO","message":"Request processed"}
{"timestamp":"2024-03-15T10:30:05Z","level":"ERROR","message":"Database timeout"}
```

### Processing JSONL
```bash
# Filter by level
jq -c 'select(.level == "ERROR")' app.jsonl

# Extract fields
jq -r '[.timestamp, .level, .message] | @csv' app.jsonl

# Time-based filter
jq -c 'select(.timestamp >= "2024-03-15T10:00:00Z")' app.jsonl

# Aggregate errors by type
jq -s 'group_by(.error_type) | map({type: .[0].error_type, count: length})' errors.jsonl
```

## Compressed Log Streaming

### Processing gzip without decompressing
```bash
# Stream through gzip
zcat logs.gz | grep "ERROR"

# Pipe to other tools
zcat access.log.gz | awk '{print $1}' | sort | uniq -c

# Multiple compressed files
zcat logs.*.gz | grep "ERROR" | wc -l

# Compress output on the fly
grep "ERROR" app.log | gzip > errors.log.gz
```

### Using xz, bz2
```bash
# xz (better compression)
xzcat logs.xz | jq -c 'select(.level == "ERROR")'

# bz2
bzcat logs.bz2 | grep "WARN"
```

## API Integration

### Fetching Data from APIs
```bash
# Simple GET request
curl -s 'https://api.example.com/users' | jq '.'

# With headers
curl -s -H "Authorization: Bearer $TOKEN" 'https://api.example.com/data' | jq '.'

# POST request
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"query":"data"}' \
  'https://api.example.com/search' | jq '.'

# Paginated API
for page in {1..10}; do
  curl -s "https://api.example.com/items?page=$page" | jq '.items[]'
done
```

### Rate-Limited API Calls
```bash
# Sleep between requests
for id in {1..100}; do
  curl -s "https://api.example.com/user/$id" | jq '.'
  sleep 0.5  # 2 requests/second
done

# Parallel with rate limit (using GNU parallel)
seq 1 100 | parallel -j5 --delay 0.2 \
  'curl -s "https://api.example.com/user/{}" | jq "."'
```

## Markdown Report Generation

### Generate Markdown Tables
```bash
# From CSV to markdown table
echo "| Name | Age | City |"
echo "|------|-----|------|"
awk -F',' 'NR > 1 {printf "| %s | %s | %s |\n", $1, $2, $3}' data.csv

# Using miller
mlr --csv --omd cat data.csv
```

### Template-Based Reports
```bash
# Generate report from template
cat report_template.md | \
  sed "s/{{TOTAL}}/$total/g" | \
  sed "s/{{DATE}}/$(date)/g" > report.md
```

### Full Report Example
```bash
#!/bin/bash
# Generate daily report

{
  echo "# Daily Report - $(date +%Y-%m-%d)"
  echo ""
  echo "## Summary"
  echo "- Total Requests: $(wc -l < access.log)"
  echo "- Errors: $(grep -c ERROR app.log)"
  echo "- Active Users: $(cut -d',' -f1 users.csv | sort -u | wc -l)"
  echo ""
  echo "## Top 10 IPs"
  echo "| IP | Requests |"
  echo "|-----|----------|"
  awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10 | \
    awk '{printf "| %s | %d |\n", $2, $1}'
  echo ""
  echo "## Error Distribution"
  echo "| Error Type | Count |"
  echo "|------------|-------|"
  jq -r '.error_type' errors.jsonl | sort | uniq -c | sort -rn | \
    awk '{printf "| %s | %d |\n", $2, $1}'
} > daily_report.md
```

## Complete ETL Pipeline Example

### Example: API → Processing → Database Simulation
```bash
#!/bin/bash
# Fetch data from API, process, save

# Fetch
curl -s 'https://api.github.com/repos/torvalds/linux/commits?per_page=100' | \
  jq -c '.[] | {
    sha: .sha,
    author: .commit.author.name,
    date: .commit.author.date,
    message: .commit.message
  }' > commits.jsonl

# Process: Count commits per author
jq -r '.author' commits.jsonl | \
  sort | uniq -c | sort -rn > author_stats.txt

# Generate report
{
  echo "# Git Commit Report"
  echo ""
  echo "Generated: $(date)"
  echo ""
  echo "## Top 10 Contributors"
  echo "| Rank | Author | Commits |"
  echo "|------|--------|---------|"
  head -10 author_stats.txt | \
    awk '{printf "| %d | %s | %d |\n", NR, $2, $1}'
} > git_report.md

# Open report
open git_report.md || cat git_report.md
```

## Log Analysis Patterns

### Pattern 1: Error Rate Over Time
```bash
# Errors per hour
jq -r '.timestamp[:13]' errors.jsonl | sort | uniq -c
```

### Pattern 2: Slow Query Detection
```bash
# Find queries taking > 1 second
jq -c 'select(.duration_ms > 1000)' queries.jsonl | \
  jq -r '[.query, .duration_ms] | @csv' > slow_queries.csv
```

### Pattern 3: User Session Analysis
```bash
# Session duration by user
jq -s 'group_by(.user_id) | map({
  user: .[0].user_id,
  sessions: length,
  total_duration: map(.duration) | add,
  avg_duration: (map(.duration) | add) / length
})' sessions.jsonl
```

## Best Practices

1. **Use JSONL** for logs (one object per line)
2. **Stream compressed files** with zcat/xzcat
3. **Respect API rate limits**
4. **Cache API responses** when possible
5. **Generate reports** in markdown for readability
6. **Add timestamps** to all log processing
7. **Handle errors gracefully** in pipelines
8. **Test on samples** before processing all data

## Summary

| Task | Tool | Example |
|------|------|---------|
| JSONL filter | jq | `jq -c 'select(.level == "ERROR")'` |
| Compressed logs | zcat | `zcat logs.gz \| grep ERROR` |
| API fetch | curl | `curl -s 'https://api...' \| jq '.'` |
| Markdown table | awk | `awk '{printf "\| %s \| %s \|\\n", $1, $2}'` |

## Next Steps
- Practice JSONL processing with jq
- Build complete ETL pipeline
- Generate automated reports
- Integrate with monitoring systems
