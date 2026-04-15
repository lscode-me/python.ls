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
datamash mean 1 median 1 < numbers.txt
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

## Essential Commands for Data Streaming

### `curl` - Fetch Data from URLs

```bash
# Download a file
curl -O https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv

# Fetch and pipe to processing (GitHub API — public, no auth needed)
curl -s 'https://api.github.com/repos/torvalds/linux/commits?per_page=5' | jq '.[].commit.message'

# Follow redirects
curl -L https://bit.ly/3RhKYbJ
```

> **Tip**: All `curl` examples in this course use real, publicly available URLs you can try right away. GitHub API endpoints work without authentication (with a rate limit of 60 requests/hour).

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

### `awk` - Field-Based Text Processing

`awk` processes text line by line, splitting each line into fields. It's especially powerful for extracting, transforming, and computing data from structured text.

```bash
# Print specific fields (default delimiter: whitespace)
awk '{print $1, $3}' data.txt

# Use comma as delimiter
awk -F',' '{print $2}' data.csv

# Filter lines by a condition
awk -F',' '$3 > 100 {print $1, $3}' data.csv

# Compute a sum
awk -F',' '{sum += $3} END {print "Total:", sum}' data.csv

# Count lines matching a pattern
awk '/ERROR/ {count++} END {print count}' app.log
```

`awk` will be covered in much more depth in Module 5. For now, know that `$1`, `$2`, etc. refer to fields, `-F` sets the delimiter, and `END` runs code after all lines are processed.

### `jq` - JSON Processing

`jq` is a command-line JSON processor — think of it as `sed`/`awk` for JSON data.

```bash
# Pretty-print JSON
curl -s 'https://api.github.com/repos/torvalds/linux' | jq .

# Extract a single field
curl -s 'https://api.github.com/repos/torvalds/linux' | jq '.stargazers_count'

# Extract nested fields
curl -s 'https://api.github.com/repos/torvalds/linux/commits?per_page=3' | \
  jq '.[].commit.message'

# Filter array elements
echo '[{"name":"Alice","age":30},{"name":"Bob","age":25}]' | \
  jq '.[] | select(.age > 27)'

# Transform output format
curl -s 'https://api.github.com/repos/torvalds/linux/commits?per_page=3' | \
  jq -r '.[].commit | "\(.author.name): \(.message)"'
```

`jq` will be covered in depth in Module 6. Key syntax: `.field` extracts a field, `.[]` iterates arrays, `|` pipes within jq, and `-r` outputs raw strings.

### `sort` - Order Lines

```bash
# Alphabetically
sort numbers.txt

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

# Show only unique lines (appear exactly once)
sort data.txt | uniq -u
```

### `head` and `tail` - Select First/Last Lines

```bash
# First 10 lines
head data.csv

# First N lines
head -20 data.csv

# Last 10 lines
tail data.csv

# Follow file in real time (useful for logs)
tail -f app.log
```

### `tee` - Split Output to Multiple Destinations

The `tee` command reads from stdin and writes to both stdout and files simultaneously.

```bash
# Save output to file AND display it
command | tee output.txt

# Append to file instead of overwriting
command | tee -a output.txt

# Write to multiple files
command | tee file1.txt file2.txt file3.txt

# Save intermediate results while continuing pipeline
curl -s 'https://api.github.com/repos/torvalds/linux/commits?per_page=5' | \
  tee raw_data.json | \
  jq '.[].commit.author.name' | \
  tee authors.txt | \
  sort | uniq -c | sort -rn

# Silent tee (write to file but don't show on screen)
command | tee output.txt > /dev/null
```

**Practical Example: Log and Process**
```bash
# Save API response and process it
curl -s 'https://api.github.com/repos/torvalds/linux' | \
  tee api_response.json | \
  jq -r '.stargazers_count'
```

---

## Building Your First Data Pipeline

### Example: Analyzing Web Server Logs

Given an `access.log` (Combined Log Format):
```
192.168.1.10 - alice [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:31:02 +0000] "POST /api/login HTTP/1.1" 200 256 "curl/7.64.1"
192.168.1.10 - alice [15/Mar/2024:10:31:15 +0000] "GET /products?id=42 HTTP/1.1" 200 8901 "Mozilla/5.0"
192.168.1.20 - - [15/Mar/2024:10:32:00 +0000] "GET /admin HTTP/1.1" 403 123 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:32:30 +0000] "GET /api/orders HTTP/1.1" 200 4567 "curl/7.64.1"
192.168.1.25 - - [15/Mar/2024:10:33:45 +0000] "GET /missing.html HTTP/1.1" 404 89 "Googlebot/2.1"
192.168.1.10 - alice [15/Mar/2024:10:34:00 +0000] "GET /api/users HTTP/1.1" 200 2345 "Mozilla/5.0"
192.168.1.30 - carol [15/Mar/2024:10:35:15 +0000] "GET /api/users HTTP/1.1" 200 2345 "Python-urllib/3.9"
192.168.1.15 - bob [15/Mar/2024:10:36:00 +0000] "POST /api/checkout HTTP/1.1" 200 456 "curl/7.64.1"
192.168.1.10 - alice [15/Mar/2024:10:37:22 +0000] "GET /index.html HTTP/1.1" 200 1234 "Mozilla/5.0"
192.168.1.25 - - [15/Mar/2024:10:38:10 +0000] "GET /old-page HTTP/1.1" 404 89 "Googlebot/2.1"
192.168.1.15 - bob [15/Mar/2024:10:39:30 +0000] "GET /api/users HTTP/1.1" 200 2345 "curl/7.64.1"
192.168.1.10 - alice [15/Mar/2024:10:40:05 +0000] "POST /checkout HTTP/1.1" 200 234 "Mozilla/5.0"
192.168.1.30 - carol [15/Mar/2024:10:41:18 +0000] "GET /index.html HTTP/1.1" 200 1234 "Python-urllib/3.9"
192.168.1.25 - - [15/Mar/2024:10:42:55 +0000] "GET /missing.html HTTP/1.1" 404 89 "Googlebot/2.1"
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
5 192.168.1.10
4 192.168.1.15
3 192.168.1.25
2 192.168.1.30
1 192.168.1.20
```

### Task 2: Find and Count All 404 Errors

```bash
grep "404" access.log | \
  awk '{print $7}' | \
  sort | \
  uniq -c
```

**Output:**
```
2 /missing.html
1 /old-page
```

### Task 3: Top 10 Most Accessed Endpoints

```bash
awk '{print $7}' access.log | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -10
```

**Output:**
```
3 /api/users
3 /index.html
2 /missing.html
1 /products?id=42
1 /old-page
1 /checkout
1 /api/orders
1 /api/login
1 /api/checkout
1 /admin
```

---

## Streaming & Inter-Process Communication (IPC)

### Named Pipes (FIFOs) - Introduction

A named pipe behaves like a file, but it doesn't store data; it only passes data through in real time.

Named pipes allow inter-process communication through the filesystem. Named pipes will be covered in more depth in Module 10.

```bash
# Create a named pipe
mkfifo mypipe

# Terminal 1: Write to pipe (blocks until someone reads)
echo "Hello from pipe" > mypipe

# Terminal 2: Read from pipe
cat < mypipe

# Use in pipelines - stream data from gzip into another process through a FIFO
mkfifo data_pipe
gzip -c large_file.txt > data_pipe &
process_data < data_pipe
rm data_pipe
```

**Why use named pipes?**
- Connect independent processes
- Avoid intermediate files
- Enable parallel processing

### `/dev/fd/` - File Descriptor Files

The `/dev/fd/` directory contains special files representing open file descriptors. File descriptors will be covered in more depth in Module 2.

```bash
# View your current file descriptors
ls -l /dev/fd/

# Access stdin, stdout, stderr as files
cat /dev/fd/0  # Same as reading from stdin
echo "test" > /dev/fd/1  # Same as writing to stdout
echo "error" > /dev/fd/2  # Same as writing to stderr

# Use in redirections
diff <(ls /tmp) <(ls /var/tmp)
# Internally uses /dev/fd/N for process substitution
```

### Buffering in Unix Streams

Programs buffer output to improve performance, but this can cause unexpected delays when working with pipelines, especially in real-time scenarios.

#### What is Buffering?

When a program writes output (e.g., via `printf` or `echo`), the data doesn't always go directly to the next command. Instead, it's collected in a memory area called a **buffer** and sent in chunks. This is faster for large data, but means the next command in the pipeline may not receive data immediately.

#### Three Buffering Modes

| Mode | When data is sent | When it's used | Buffer size |
|------|------------------|----------------|-------------|
| **Unbuffered** | Immediately, byte by byte | `stderr` (always) | 0 |
| **Line-buffered** | After each newline (`\n`) | `stdout` → terminal | ~1 KB |
| **Fully-buffered** | When buffer is full | `stdout` → file or pipe | ~4-8 KB |

The key insight: **stdout behavior changes depending on where it's going**:
- If stdout goes to your **terminal** → line-buffered (you see each line immediately)
- If stdout goes to a **pipe or file** → fully-buffered (you see nothing until ~4KB accumulates)

This is why a command that works fine alone may seem "stuck" when piped to another command.

#### The Problem in Action

```bash
# Run this and type lines — you'll see each one immediately:
grep --color "hello" 

# But in a pipeline, grep switches to full buffering:
# Data is delayed until grep's 4KB buffer fills up!
tail -f app.log | grep ERROR | awk '{print $1}'
```

#### Solutions

```bash
# Solution 1: Use --line-buffered with grep
tail -f app.log | grep --line-buffered ERROR | awk '{print $1}'

# Solution 2: Use stdbuf to force line-buffering on any command
# -oL means: output (o) should be Line-buffered (L)
tail -f app.log | stdbuf -oL grep ERROR | awk '{print $1}'

# Solution 3: Python with -u flag (forces unbuffered stdout)
tail -f app.log | python3 -u script.py

# Solution 4: Flush explicitly in Python code
print("output", flush=True)
```

#### Try It Yourself

```bash
# Demo: See buffering in action
# Terminal 1: generate slow output (one line per second)
for i in $(seq 1 20); do echo "line $i"; sleep 1; done > /tmp/slowlog &

# Terminal 2: tail the file through a pipeline
tail -f /tmp/slowlog | grep "line" | cat
# Nothing appears for a while! (fully-buffered grep → cat)

# Now try with --line-buffered:
tail -f /tmp/slowlog | grep --line-buffered "line" | cat
# Lines appear one by one!
```

---

## Practical Examples

### Example 1: Fetch and Analyze CSV

```bash
# Fetch real CSV data, extract country column, count entries per country
curl -s https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv | \
  tail -n +2 | \
  cut -d',' -f2 | \
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

### Example 4: Using tee for Debugging

```bash
# Save intermediate results while debugging pipeline
cat sales.csv | \
  tee 01_raw.csv | \
  grep -v "^#" | \
  tee 02_no_comments.csv | \
  cut -d',' -f1,3 | \
  tee 03_selected_cols.csv | \
  sort | \
  uniq -c > final_result.txt

# Now you can inspect each stage: 01_raw.csv, 02_no_comments.csv, etc.
```

### Example 5: Named Pipe for Parallel Processing

```bash
# Process large file in parallel using named pipes
mkfifo pipe1 pipe2

# Start two processors in background
grep "TYPE_A" < pipe1 | process_a > output_a.txt &
grep "TYPE_B" < pipe2 | process_b > output_b.txt &

# Feed data to both pipes
tee pipe1 pipe2 < large_data.txt > /dev/null

# Wait for completion and cleanup
wait
rm pipe1 pipe2
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
curl -s 'https://api.github.com/repos/torvalds/linux' || echo '{"error": "API down"}'
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
- ✅ Essential commands: `curl`, `cut`, `grep`, `sort`, `uniq`, `head`, `tee`
- ✅ Named pipes (FIFOs) for inter-process communication
- ✅ `/dev/fd/` file descriptor files
- ✅ Buffering modes and how to control them
- ✅ Building and debugging data pipelines

### Next Steps

In the next module, we'll dive deeper into **Files, I-nodes & File Descriptors** to understand how Unix manages data at the system level.

---

## Additional Resources

- `man` pages: `man grep`, `man cut`, `man sort`
- [The Unix Programming Environment](https://en.wikipedia.org/wiki/The_Unix_Programming_Environment)
- [Data Science at the Command Line](https://datascienceatthecommandline.com/)
