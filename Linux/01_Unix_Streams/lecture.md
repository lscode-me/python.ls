# Unix as a Language of Data & Streams

## Sample Data Files

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

---

## Introduction

Unix wasn't just designed as an operating system — it was designed as a **philosophy for building composable tools**. At its core is the idea that **data flows through transformations**, and each tool does one thing well.

In this module, we'll learn to think in terms of **streams** — continuous flows of data that can be filtered, transformed, and aggregated using simple, composable commands.

---

## Unix Philosophy for Data

### The Core Principles

1. **Write programs that do one thing and do it well**
2. **Write programs to work together**
3. **Write programs to handle text streams, because that is a universal interface**

### Why This Matters for Data Processing

- **Composability**: Small tools combine into powerful pipelines
- **Streaming**: Process gigabytes without loading into memory
- **Text as Interface**: Universal data format that all tools understand
- **Incremental Development**: Build and test pipelines step by step

---

## Streams, Pipes, and Standard I/O

### The Three Standard Streams

Every Unix process has three standard streams:

- **stdin (0)**: Standard input — where data comes in
- **stdout (1)**: Standard output — where results go out
- **stderr (2)**: Standard error — where errors and logs go

### Pipes: Connecting Streams

The pipe operator `|` connects stdout of one command to stdin of the next:

```bash
# Count lines in a file
cat data.csv | wc -l

# Find unique values
cat data.csv | cut -d',' -f2 | sort | uniq

# Top 10 most frequent items
cat data.csv | cut -d',' -f3 | sort | uniq -c | sort -rn | head -10
```

### Redirection

```bash
# Output to file
command > output.txt

# Append to file
command >> output.txt

# Input from file
command < input.txt

# Redirect stderr
command 2> errors.log

# Redirect both stdout and stderr
command &> all_output.log
```

---

## The Filter → Transform → Aggregate Workflow

This is the fundamental pattern of Unix data processing:

### 1. Filter — Select What You Need

```bash
# Filter lines matching a pattern
grep "ERROR" app.log

# Filter specific fields
cut -d',' -f1,3 data.csv

# Filter by date
grep "2024-11-" access.log
```

### 2. Transform — Change the Data

```bash
# Convert to uppercase
tr '[:lower:]' '[:upper:]'

# Replace text
sed 's/old/new/g'

# Extract and transform fields
awk -F',' '{print $1, $3*2}'
```

### 3. Aggregate — Summarize Results

```bash
# Count occurrences
sort | uniq -c

# Sum values
awk '{sum += $1} END {print sum}'

# Get statistics
datamash mean 1 median 1 < data.txt
```

---

## Text as the Universal Data Interface

### Why Text?

- **Human-readable**: Easy to inspect and debug
- **Tool-compatible**: Every Unix tool can process text
- **Line-oriented**: Natural unit for streaming
- **Flexible**: CSV, JSON, logs, tables — all text-based

### Common Text Formats

```bash
# CSV (Comma-Separated Values)
name,age,city
Alice,30,NYC
Bob,25,LA

# TSV (Tab-Separated Values)
name    age    city
Alice   30     NYC

# JSONL (JSON Lines)
{"name":"Alice","age":30,"city":"NYC"}
{"name":"Bob","age":25,"city":"LA"}

# Log format
2024-11-27 10:23:45 INFO User logged in
2024-11-27 10:24:12 ERROR Connection timeout
```

---

## Building Your First Data Pipeline

### Example: Analyzing Web Server Logs

Given an access log:
```
192.168.1.1 - - [27/Nov/2024:10:23:45] "GET /api/users" 200
192.168.1.2 - - [27/Nov/2024:10:24:12] "GET /api/posts" 404
192.168.1.1 - - [27/Nov/2024:10:25:01] "POST /api/login" 200
```

### Task 1: Count Requests by IP

```bash
cat access.log | \
  awk '{print $1}' | \
  sort | \
  uniq -c | \
  sort -rn
```

**Output:**
```
2 192.168.1.1
1 192.168.1.2
```

### Task 2: Find All 404 Errors

```bash
grep "404" access.log | \
  awk '{print $7}' | \
  sort | \
  uniq -c
```

### Task 3: Top 10 Most Accessed Endpoints

```bash
awk '{print $7}' access.log | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -10
```

---

## Essential Commands for Data Streaming

### `curl` - Fetch Data from URLs

```bash
# Download a file
curl -O https://example.com/data.csv

# Fetch and pipe to processing
curl -s https://api.example.com/data | jq '.results[]'

# Follow redirects
curl -L https://example.com/redirect
```

### `cut` - Extract Columns

```bash
# Extract first column (comma-delimited)
cut -d',' -f1 data.csv

# Extract multiple columns
cut -d',' -f1,3,5 data.csv

# Extract character range
cut -c1-10 data.txt
```

### `grep` - Filter Lines by Pattern

```bash
# Basic search
grep "error" app.log

# Case-insensitive
grep -i "error" app.log

# Invert match (exclude lines)
grep -v "DEBUG" app.log

# Show line numbers
grep -n "error" app.log
```

### `sort` - Order Lines

```bash
# Alphabetically
sort data.txt

# Numerically
sort -n numbers.txt

# Reverse order
sort -r data.txt

# By specific field
sort -t',' -k2 data.csv
```

### `uniq` - Remove Duplicates

```bash
# Remove adjacent duplicates (requires sorted input)
sort data.txt | uniq

# Count occurrences
sort data.txt | uniq -c

# Show only duplicates
sort data.txt | uniq -d
```

### `head` and `tail` - Select First/Last Lines

```bash
# First 10 lines
head data.csv

# First N lines
head -20 data.csv

# Last 10 lines
tail data.csv

# Follow file (useful for logs)
tail -f app.log
```

---

## Practical Examples

### Example 1: Fetch and Analyze CSV

```bash
# Fetch CSV, extract date column, count entries per date
curl -s https://example.com/sales.csv | \
  cut -d',' -f1 | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -10
```

### Example 2: Find Most Frequent Values

```bash
# Most common user agents in logs
awk -F'"' '{print $6}' access.log | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -10
```

### Example 3: Quick Data Validation

```bash
# Count records
wc -l < data.csv

# Check for empty fields
grep ',,' data.csv | wc -l

# Unique values in column
cut -d',' -f2 data.csv | sort -u | wc -l
```

---

## Thinking in Streams

### Mental Model

```
[Data Source] → [Filter] → [Transform] → [Aggregate] → [Output]
```

### Benefits of Streaming

1. **Memory Efficient**: Process any size dataset
2. **Fast Feedback**: See results as they're computed
3. **Composable**: Mix and match tools freely
4. **Debuggable**: Test each stage independently

### When to Break the Pipeline

Sometimes you need intermediate files:
- **Checkpointing**: Save progress for long-running jobs
- **Multiple consumers**: Use same data in multiple pipelines
- **Debugging**: Inspect intermediate results

---

## Best Practices

### 1. Start Simple, Add Complexity

```bash
# Start with basic filter
grep "2024-11" data.log

# Add transformation
grep "2024-11" data.log | awk '{print $1, $5}'

# Add aggregation
grep "2024-11" data.log | awk '{print $5}' | sort | uniq -c
```

### 2. Test Each Stage

```bash
# Test first stage
cat data.csv | cut -d',' -f2 | head

# Test second stage
cat data.csv | cut -d',' -f2 | sort | head

# Test complete pipeline
cat data.csv | cut -d',' -f2 | sort | uniq -c
```

### 3. Use Head for Sampling

```bash
# Process only first 1000 lines for testing
head -1000 huge_file.csv | your_pipeline
```

### 4. Handle Errors Gracefully

```bash
# Check if file exists
[ -f data.csv ] && cat data.csv | process

# Provide default if command fails
curl -s https://api.example.com/data || echo '{"error": "API down"}'
```

---

## Common Pitfalls

### 1. Not Sorting Before `uniq`

```bash
# WRONG: uniq only removes adjacent duplicates
cat data.txt | uniq

# CORRECT: sort first
cat data.txt | sort | uniq
```

### 2. Useless Use of `cat`

```bash
# INEFFICIENT
cat file.txt | grep pattern

# BETTER
grep pattern file.txt

# BUT: cat is fine for pipelines with multiple inputs
cat file1.txt file2.txt | grep pattern
```

### 3. Not Quoting Variables

```bash
# WRONG: breaks on spaces
grep $pattern data.txt

# CORRECT
grep "$pattern" data.txt
```

---

## Summary

In this module, you learned:

- ✅ Unix philosophy: small tools, text streams, composition
- ✅ Standard I/O: stdin, stdout, stderr
- ✅ Pipes and redirection
- ✅ Filter → Transform → Aggregate pattern
- ✅ Essential commands: `curl`, `cut`, `grep`, `sort`, `uniq`, `head`
- ✅ Building and debugging data pipelines

### Next Steps

In the next module, we'll dive deeper into **Files, I-nodes & File Descriptors** to understand how Unix manages data at the system level.

---

## Additional Resources

- `man` pages: `man grep`, `man cut`, `man sort`
- [The Unix Programming Environment](https://en.wikipedia.org/wiki/The_Unix_Programming_Environment)
- [Data Science at the Command Line](https://datascienceatthecommandline.com/)
