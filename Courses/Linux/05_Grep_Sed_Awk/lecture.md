# Grep, Sed & Awk: Text Processing Power Tools

## Sample Data Files

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

---

## Overview
The trio of `grep`, `sed`, and `awk` form the foundation of Unix text processing. Each tool excels at different tasks:
- **grep**: Search and filter lines
- **sed**: Stream editor for transformations
- **awk**: Pattern scanning and data extraction

These three tools are often used in combination: `grep` filters lines, `sed` transforms them, and `awk` processes fields and performs calculations. Together they form a pipeline that can handle most log parsing, data extraction, and text transformation tasks without requiring a full scripting language.

## What is Regex?

**Regular Expressions (regex)** are a formal language for describing text patterns. Regex is used for searching, validating, and manipulating textual data.

### Core Concept
Regex allows you to describe a **pattern**, not a specific string:
- `cat` — matches only the word "cat"
- `c.t` — matches "cat", "cot", "cut", "c3t", etc.
- `[Cc]at` — matches "cat" or "Cat"
- `^cat$` — matches a line containing only "cat"

### Regex vs Shell Globbing

⚠️ **Important!** Regex and shell globbing are **different systems** with different syntax:

| Feature | Shell Globbing | Regex |
|---------|----------------|-------|
| **Purpose** | File matching | Text pattern matching |
| **Context** | Command line (ls, cp, rm) | grep, sed, awk, editors |
| **`*` meaning** | Any characters | Zero or more of **previous** |
| **`?` meaning** | Single character | Zero or one of **previous** |
| **`.` meaning** | Literal dot | Any single character |
| **Character class** | `[abc]` ✓ | `[abc]` ✓ |
| **Range** | `[a-z]` ✓ | `[a-z]` ✓ |
| **Negation** | `[!abc]` | `[^abc]` |
| **Anchors** | ❌ | `^` start, `$` end |
| **Alternation** | `{txt,md}` | BRE: `\(txt\|md\)`, ERE: `(txt|md)` |

### Examples Comparison

```bash
# Shell Globbing (file matching)
ls *.txt          # All files ending in .txt
rm file?.log      # file1.log, fileA.log (? = one char)
cp *.{py,js} dir/ # Copy .py and .js files

# Regex (text pattern matching)
grep ".*\.txt$"   # Lines ending in .txt (. = any char, * = zero or more)
grep "file."      # "file" + any one character
grep -E "(py|js)" # Lines containing "py" or "js"
```

### Common Confusion

```bash
# ❌ Wrong: using globbing syntax in regex
grep "*.txt" file       # Wrong! Means zero or more '*', then ".txt"

# ✓ Correct: proper regex
grep ".*\.txt" file     # Matches: anything + ".txt"

# ❌ Wrong: using regex in shell
ls .*\.txt              # Wrong! Shell sees: .*.txt (hidden files, literal backslash)

# ✓ Correct: proper globbing  
ls *.txt                # Matches: any files ending in .txt
```

### When to Use What?

```bash
# Use Shell Globbing for files:
rm *.tmp
cp src/*.py dest/
for file in *.{jpg,png}; do ...; done

# Use Regex for text content:
grep -E "^[A-Z].*\.$" file.txt      # Lines starting with capital, ending with period
sed 's/[0-9]\{4\}-[0-9]\{2\}/XXXX-XX/' file.txt  # Mask dates
awk '/^ERROR/ {print $0}' app.log    # Lines starting with ERROR
```

> **Note:** Although `grep`, `sed`, and `awk` all support regular expressions, they do not use the same regex syntax by default. `grep` and `sed` use BRE by default (use `-E` for ERE), while `awk` always uses ERE.

## Regular Expressions Primer

### Basic Patterns
```bash
.       # Any single character
^       # Start of line
$       # End of line
*       # Zero or more of previous
+       # One or more (ERE)
?       # Zero or one (ERE)
[abc]   # Character class
[^abc]  # Negated class
[a-z]   # Range
\       # Escape special char
```

> **Note:** `+` and `?` are ERE syntax. In BRE (default `grep`/`sed`), use `\+` and `\?`.

### Extended Patterns (ERE)
```bash
(pattern)     # Grouping
|             # Alternation (OR)
{n}           # Exactly n times
{n,}          # n or more
{n,m}         # Between n and m
\b            # Word boundary
\d \w \s      # Digit, word, space (GNU/PCRE only)
```

> **Note:** `\b`, `\d`, `\w`, `\s` are not POSIX ERE constructs. They are supported in `grep -P` (PCRE mode) and some `awk` variants (e.g., `gawk`).

## Grep: Pattern Matching

`grep` is a line-oriented search tool that matches text using regular expressions. It is ideal for filtering logs, configuration files, and large datasets before passing results to tools like `sed` or `awk`.

### Basic Usage
```bash
# Search for pattern
grep "ERROR" app.log

# Case-insensitive
grep -i "error" app.log

# Show line numbers
grep -n "ERROR" app.log

# Invert match (exclude)
grep -v "DEBUG" app.log

# Count matches
grep -c "ERROR" app.log

# Show only matching part
grep -o "ERROR" app.log
```

### Extended Grep (grep -E or egrep)
```bash
# Match multiple patterns
grep -E "ERROR|FATAL|CRITICAL" app.log

# Match IP addresses
grep -E '\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b' access.log

# Match email addresses
grep -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' users.txt

# Date pattern (YYYY-MM-DD)
grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}' logs.txt
```

### Context and File Options
```bash
# Show 3 lines before match
grep -B 3 "ERROR" app.log

# Show 3 lines after match
grep -A 3 "ERROR" app.log

# Show 3 lines before and after
grep -C 3 "ERROR" app.log

# Recursive search in directory
grep -r "TODO" src/

# Search in specific file types
grep -r --include="*.py" "import pandas" src/

# Search multiple files
grep "ERROR" *.log
```

### Practical Grep Examples
```bash
# Find all Python imports
grep -rh "^import\|^from" --include="*.py" src/ | sort -u

# Extract all URLs (stop at quotes or HTML tags)
grep -Eo 'https?://[^"<>]+' page.html

# Find failed login attempts
grep "Failed password" /var/log/auth.log | wc -l

# Search for credit card patterns (testing only!)
grep -E '\b[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}\b' data.txt
```

### Grep Flags Quick Reference

```bash
# Use -E for extended regex (recommended)
grep -E 'pattern' file.txt

# Case-insensitive
grep -iE 'pattern' file.txt

# Extract only matching parts
grep -Eo 'pattern' file.txt

# Show line numbers
grep -nE 'pattern' file.txt

# Invert match (exclude)
grep -vE 'pattern' file.txt
```

## Sed: Stream Editor

`sed` (stream editor) reads input line by line, applies transformations based on patterns and commands, and writes the result to standard output. By default, it does not edit files in place; transformed lines are printed to stdout unless the `-i` option is used.

### Basic Substitution
```bash
# Replace first occurrence per line
sed 's/old/new/' file.txt

# Replace all occurrences (global)
sed 's/old/new/g' file.txt

# Replace in-place (modify file)
sed -i 's/old/new/g' file.txt  # GNU sed
sed -i '' 's/old/new/g' file.txt  # BSD sed (macOS)

# Replace only on lines matching pattern
sed '/ERROR/s/old/new/g' file.txt
```

### Advanced Substitution
```bash
# Use different delimiter (when pattern contains /)
sed 's|/old/path|/new/path|g' file.txt

# Backreferences
sed 's/\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\)/\3\/\2\/\1/' dates.txt
# 2024-03-15 → 15/03/2024

# Case conversion (GNU sed)
sed 's/.*/\U&/' file.txt  # Uppercase
sed 's/.*/\L&/' file.txt  # Lowercase

# Multiple substitutions
sed -e 's/cat/dog/g' -e 's/mouse/rat/g' file.txt
```

### Line Operations
```bash
# Delete lines
sed '/pattern/d' file.txt        # Delete matching lines
sed '5d' file.txt                 # Delete line 5
sed '2,5d' file.txt               # Delete lines 2-5
sed '/^$/d' file.txt              # Delete empty lines

# Print lines
sed -n '/pattern/p' file.txt      # Print only matching lines
sed -n '10,20p' file.txt          # Print lines 10-20

# Insert/Append
sed '5i\New line before' file.txt   # Insert before line 5
sed '5a\New line after' file.txt    # Append after line 5

# Change lines
sed '/pattern/c\Replacement line' file.txt
```

### Practical Sed Examples
```bash
# Remove HTML tags
sed 's/<[^>]*>//g' page.html

# Convert DOS to Unix line endings
sed 's/\r$//' dos_file.txt

# Add line numbers
sed = file.txt | sed 'N;s/\n/\t/'

# Extract text between patterns
sed -n '/START/,/END/p' file.txt

# Comment out lines
sed 's/^/#/' file.txt

# Remove comments
sed 's/#.*//' file.txt
```

## Awk: Pattern Scanning and Processing

`awk` is a pattern–action language designed for structured text processing. It processes input line by line, splits each line into fields, and applies actions when patterns match. `awk` is especially powerful for working with tabular data, calculations, and aggregation.

### Basic Awk Syntax
```bash
# Print entire line
awk '{print}' data.txt

# Print specific fields (works well with multi-column files like logs)
awk '{print $1, $3}' logs.txt

# Field separator
awk -F',' '{print $2}' data.csv

# Pattern matching
awk '/ERROR/ {print $0}' app.log

# Pattern + action
awk '/ERROR/ {print $1, $3}' app.log
```

### Built-in Variables
```bash
$0      # Entire line
$1, $2  # Fields 1, 2, etc.
NF      # Number of fields
NR      # Current record number (line number)
FS      # Field separator (default: whitespace)
OFS     # Output field separator
RS      # Record separator (default: newline)
ORS     # Output record separator
```

### Awk Programming Constructs
```bash
# BEGIN and END blocks
awk 'BEGIN {print "Start"} {print $1} END {print "Done"}' file.txt

# Conditionals
awk -F',' '{if ($3 > 10) print $2, $3}' sales.csv

# Calculations
awk '{sum += $1} END {print sum}' numbers.txt

# Average
awk '{sum += $1; count++} END {print sum/count}' numbers.txt

# String operations
awk '{print length($0)}' data.txt    # Line length
awk '{print tolower($1)}' data.txt   # Lowercase
awk '{print substr($1, 1, 5)}' data.txt  # Substring
```

### CSV Processing with Awk
```bash
# Print specific columns
awk -F',' '{print $2, $4}' data.csv

# Skip header
awk -F',' 'NR > 1 {print $0}' data.csv

# Sum revenue column
awk -F',' 'NR > 1 {sum += $4} END {print sum}' sales.csv

# Filter by revenue
awk -F',' '$4 > 1000 {print $0}' sales.csv

# Group by (Sum revenue by product)
awk -F',' '{sum[$2] += $4} END {for (key in sum) print key, sum[key]}' sales.csv
```

### Log Analysis with Awk
```bash
# Count by status code
awk '{print $9}' access.log | sort | uniq -c

# Extract IP and status
awk '{print $1, $9}' access.log

# Calculate average response size
awk '{sum += $10; count++} END {print sum/count}' access.log

# Top 10 IPs by request count
awk '{ip[$1]++} END {for (i in ip) print ip[i], i}' access.log | sort -rn | head -10

# Requests per minute
awk '{print substr($4, 2, 16)}' access.log | sort | uniq -c
```

### Practical Awk Examples

#### Example 1: Generate SQL INSERT Statements
```bash
awk -F',' 'NR > 1 {printf "INSERT INTO users VALUES (\"%s\", \"%s\", %s);\n", $1, $2, $3}' users.csv
```

#### Example 2: Convert CSV to JSON
```bash
awk -F',' 'NR > 1 {printf "{\"id\": \"%s\", \"name\": \"%s\", \"age\": %s}\n", $1, $2, $3}' data.csv
```

#### Example 3: Column Statistics
```bash
awk -F',' '
  NR > 1 {
    sum += $3
    if ($3 < min || NR == 2) min = $3
    if ($3 > max) max = $3
  }
  END {
    print "Sum:", sum
    print "Avg:", sum/(NR-1)
    print "Min:", min
    print "Max:", max
  }
' data.csv
```

## Combining Grep, Sed, Awk

### Pattern: Filter → Transform → Aggregate
```bash
# Find errors, extract date+hour, count per hour
grep "ERROR" app.log | \
  sed 's/^\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9]\{2\}\):.*/\1/' | \
  sort | uniq -c
```

### Pattern: Multi-Step Extraction
```bash
# Extract email domains and count
grep -Eo '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' users.txt | \
  sed 's/.*@//' | \
  sort | uniq -c | sort -rn
```

### Pattern: Data Cleaning
```bash
# Remove HTML, extract text, count words
sed 's/<[^>]*>//g' page.html | \
  tr '[:upper:]' '[:lower:]' | \
  tr -cs '[:alnum:]' '\n' | \
  sort | uniq -c | sort -rn | head -20
```

## Performance Tips

1. **Grep is fastest** for simple line filtering
2. **Sed is best** for line-by-line transformations
3. **Awk is powerful** for field processing and calculations
4. **Use grep first** to reduce data volume before sed/awk
5. **Avoid nested loops** in awk for large files
6. **Use -F option** instead of setting FS in awk BEGIN
7. **Use `grep -P`** for Perl-compatible regex (lookaheads, `\d`, `\w`) when available

## Best Practices

1. **Test on small samples** before running on large files
2. **Use `-n` with sed** to print only what you want
3. **Quote patterns** to avoid shell expansion
4. **Escape special characters** properly
5. **Use extended regex** (`grep -E`, `sed -E`) for readability
6. **Combine tools** for complex tasks
7. **Document regex patterns** with comments in scripts

## Summary

| Tool | Best For | Example |
|------|----------|---------|
| `grep` | Line filtering | `grep -E "ERROR\|WARN" app.log` |
| `sed` | Line transformations | `sed 's/old/new/g' file.txt` |
| `awk` | Field processing | `awk -F',' '{sum+=$3} END {print sum}'` |

### Quick Syntax Reminder

| Symbol | Meaning | Example |
|--------|---------|--------|
| `.` | Any single character | `c.t` matches `cat`, `cot`, `c5t` |
| `^` | Start of line | `^Hello` matches lines starting with "Hello" |
| `$` | End of line | `world$` matches lines ending with "world" |
| `*` | Zero or more | `ab*c` matches `ac`, `abc`, `abbc` |
| `+` | One or more | `ab+c` matches `abc`, `abbc` (not `ac`) |
| `?` | Zero or one | `ab?c` matches `ac`, `abc` |
| `[abc]` | Character class | Matches `a`, `b`, or `c` |
| `[^abc]` | Negated class | Matches anything except `a`, `b`, `c` |
| `[a-z]` | Range | Matches any lowercase letter |
| `\|` | Alternation (OR) | `cat\|dog` matches `cat` or `dog` |
| `()` | Grouping | `(ab)+` matches `ab`, `abab`, `ababab` |
| `{n}` | Exactly n times | `[0-9]{3}` matches exactly 3 digits |
| `{n,}` | n or more times | `[0-9]{3,}` matches 3+ digits |
| `{n,m}` | Between n and m | `[0-9]{2,4}` matches 2-4 digits |
| `\b` | Word boundary | `\bcat\b` matches "cat" but not "category" |
| `\d` | Digit (PCRE only) | Equivalent to `[0-9]` |
| `\w` | Word character (PCRE only) | Equivalent to `[A-Za-z0-9_]` |
| `\s` | Whitespace (PCRE only) | Matches space, tab, newline |
| `\\` | Escape character | `\.` matches literal dot |

## Next Steps
- Practice regex on regex101.com
- Study awk programming language features
- Learn Perl for more complex text processing
- Explore ripgrep (rg) for faster searching

---

## Ready-to-Use Regex Patterns

A collection of tested regular expressions for common tasks.

### Network & Web

#### IP Address (IPv4)
```bash
# Basic (permissive)
grep -E '\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b' file.txt

# Strict (validates 0-255 range)
grep -E '\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b' file.txt

# Examples matched: 192.168.1.1, 10.0.0.255, 172.16.0.1
```

#### Email Address
```bash
# Basic (permissive)
grep -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' file.txt

# More strict
grep -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|net|edu|gov|io|dev)\b' file.txt

# Examples matched: user@example.com, john.doe+filter@company.co.uk
```

#### URL
```bash
# HTTP/HTTPS URLs
grep -Eo 'https?://[A-Za-z0-9./_-]+' file.txt

# With query parameters
grep -Eo 'https?://[A-Za-z0-9./?&=_-]+' file.txt

# Full URL with fragments
grep -Eo 'https?://[A-Za-z0-9./?&=_#%-]+' file.txt

# Examples matched: 
# https://example.com/path
# http://site.com/page?id=123&name=test
```

#### Domain Name
```bash
# Basic domain
grep -E '\b[a-z0-9-]+\.[a-z]{2,}\b' file.txt

# With subdomains
grep -E '\b([a-z0-9-]+\.)+[a-z]{2,}\b' file.txt

# Examples matched: example.com, sub.domain.co.uk, my-site.io
```

#### MAC Address
```bash
# Colon-separated
grep -E '\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b' file.txt

# Hyphen-separated
grep -E '\b([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}\b' file.txt

# Examples matched: 00:1A:2B:3C:4D:5E, 00-1A-2B-3C-4D-5E
```

### Date & Time

#### Date (YYYY-MM-DD)
```bash
# ISO 8601 format
grep -E '\b[0-9]{4}-[0-9]{2}-[0-9]{2}\b' file.txt

# With validation (basic)
grep -E '\b[12][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\b' file.txt

# Examples matched: 2024-12-02, 2023-01-15
```

#### Date (DD/MM/YYYY or MM/DD/YYYY)
```bash
# DD/MM/YYYY or MM/DD/YYYY
grep -E '\b[0-9]{2}/[0-9]{2}/[0-9]{4}\b' file.txt

# Examples matched: 02/12/2024, 12/25/2023
```

#### Time (HH:MM:SS)
```bash
# 24-hour format
grep -E '\b([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\b' file.txt

# With optional seconds
grep -E '\b([01][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?\b' file.txt

# Examples matched: 14:30:00, 09:05:23
```

#### Timestamp (ISO 8601)
```bash
# Full ISO timestamp
grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}' file.txt

# With timezone
grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([+-][0-9]{2}:[0-9]{2}|Z)' file.txt

# Examples matched: 
# 2024-12-02T14:30:00
# 2024-12-02T14:30:00Z
# 2024-12-02T14:30:00+03:00
```

### Financial

#### Credit Card (Generic)
```bash
# Generic card number (16 digits with optional separators)
grep -E '\b[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}\b' file.txt

# ⚠️ Use only for testing/education, never log real card numbers!
# Examples matched: 1234-5678-9012-3456, 1234 5678 9012 3456
```

#### Currency Amount
```bash
# USD format with optional cents
grep -E '\$[0-9]{1,3}(,[0-9]{3})*(\.[0-9]{2})?' file.txt

# Generic currency (digits with optional cents)
grep -E '\b[0-9]{1,3}(,[0-9]{3})*(\.[0-9]{2})?\b' file.txt

# Examples matched: $1,234.56, $999, 1,234,567.89
```

### Phone Numbers

#### US Phone Number
```bash
# Various US formats
grep -E '\b(\+1[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b' file.txt

# Examples matched:
# +1-555-123-4567
# (555) 123-4567
# 555.123.4567
# 5551234567
```

#### International Format
```bash
# E.164 format
grep -E '\+[0-9]{1,3}[0-9]{4,14}' file.txt

# Examples matched: +1234567890, +79161234567
```

### Bioinformatics

#### DNA Sequence
```bash
# DNA nucleotides (A, T, G, C)
grep -E '^[ATGC]+$' sequence.txt

# With length constraint (at least 10bp)
grep -E '^[ATGC]{10,}$' sequence.txt

# Case-insensitive
grep -iE '^[ATGC]+$' sequence.txt

# Examples matched: ATGCTAGCTAGC, GGCCAATTGGCC
```

#### RNA Sequence
```bash
# RNA nucleotides (A, U, G, C)
grep -E '^[AUGC]+$' sequence.txt

# With length constraint
grep -E '^[AUGC]{10,}$' sequence.txt

# Examples matched: AUGCUAGCUAGC, GGCCAAUUGGCC
```

#### Protein Sequence (Amino Acids)
```bash
# Single-letter amino acid codes
grep -E '^[ACDEFGHIKLMNPQRSTVWY]+$' protein.txt

# Including ambiguous codes (B, Z, X)
grep -E '^[ACDEFGHIKLMNPQRSTVWYBZX]+$' protein.txt

# Examples matched: MKTAYIAKQR, ACDEFGHIKLMNPQRSTVWY
```

#### FASTA Header
```bash
# Extract FASTA IDs
grep -E '^>[A-Za-z0-9_|.-]+' sequences.fasta

# Extract full header with description
grep -E '^>.*' sequences.fasta

# Examples matched: >seq1, >gi|12345|ref|NM_000001
```

#### Genetic Coordinates
```bash
# Format: chr:start-end
grep -E 'chr[0-9XYM]+:[0-9]+-[0-9]+' coordinates.txt

# Examples matched: chr1:1000-2000, chrX:123456-234567
```

### File & Path

#### File Extensions
```bash
# Common programming files
grep -E '\.(py|js|java|cpp|c|h|go|rs)$' filelist.txt

# Data files
grep -E '\.(csv|json|xml|yaml|txt)$' filelist.txt

# Image files
grep -E '\.(jpg|jpeg|png|gif|svg|webp)$' filelist.txt
```

#### Unix Path
```bash
# Absolute path
grep -E '^/([^/]+/)*[^/]+$' paths.txt

# Relative path
grep -E '^[^/]([^/]+/)*[^/]+$' paths.txt

# Examples matched: /usr/local/bin, ./src/main.py
```

### Identifiers

#### UUID (Universally Unique Identifier)
```bash
# Standard UUID format
grep -E '\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b' file.txt

# Examples matched: 550e8400-e29b-41d4-a716-446655440000
```

#### Hex Color Code
```bash
# 3 or 6 digit hex colors
grep -Eo '#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b' styles.css

# Examples matched: #FF5733, #f00, #BADA55
```

#### Social Security Number (US)
```bash
# SSN format (XXX-XX-XXXX)
grep -E '\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b' file.txt

# ⚠️ Use only for testing, never log real SSNs!
# Examples matched: 123-45-6789
```

### Log & Code Patterns

#### Log Level
```bash
# Common log levels
grep -E '\b(DEBUG|INFO|WARN(ING)?|ERROR|FATAL|CRITICAL)\b' app.log

# With timestamp context (matches app.log format: "2024-03-15 10:23:45 ERROR ...")
grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} (DEBUG|INFO|WARN|ERROR|FATAL)' app.log
```

#### IPv4 CIDR Notation
```bash
# IP with subnet mask
grep -E '\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2}\b' networks.txt

# Examples matched: 192.168.1.0/24, 10.0.0.0/8
```

#### Git Commit Hash
```bash
# Short hash (7 chars)
grep -E '\b[0-9a-f]{7}\b' commits.txt

# Full hash (40 chars)
grep -E '\b[0-9a-f]{40}\b' commits.txt

# Examples matched: a3d5f7e, 1234567890abcdef1234567890abcdef12345678
```

### Practical Usage Examples

```bash
# Extract all emails from text
grep -Eo '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' document.txt > emails.txt

# Find all IP addresses in logs
grep -Eo '\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b' access.log | sort -u

# Extract URLs from HTML
grep -Eo 'https?://[^"<>]+' page.html

# Validate DNA sequences
grep -vE '^[ATGC]+$' sequences.txt  # Show invalid sequences

# Find all dates in logs
grep -Eo '[0-9]{4}-[0-9]{2}-[0-9]{2}' app.log | sort -u

# Extract credit card numbers (for security audit)
grep -Eo '\b[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}\b' suspicious.txt
```

### Testing Your Regex

```bash
# Test regex interactively
echo "test@example.com" | grep -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Show only matching part
echo "IP: 192.168.1.1" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'

# Test with multiple patterns
echo -e "ATGC\nATGX\nGGCC" | grep -E '^[ATGC]+$'

# Use online tools for complex patterns:
# - regex101.com (with explanation)
# - regexr.com (visual testing)
# - debuggex.com (railroad diagrams)
```

### Tips for Creating Your Own Patterns

1. **Start simple** — gradually increase pattern complexity
2. **Test on real data** — validate with actual examples
3. **Consider edge cases** — account for boundary conditions
4. **Use anchors** — `^` and `$` for precise positioning
5. **Escape properly** — escape special characters correctly
6. **Document complex patterns** — add comments in scripts
7. **Balance strictness** — find balance between precision and flexibility

---

## Quick Reference: Common Regex Patterns

| Pattern | Regex | Example Matches |
|---------|-------|-----------------|
| **Email** | `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b` | `user@example.com`, `john.doe@company.co.uk` |
| **IPv4 Address** | `\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b` | `192.168.1.1`, `10.0.0.1` |
| **URL (HTTP/HTTPS)** | `https?://[A-Za-z0-9./?&=_-]+` | `https://example.com/path?id=123` |
| **Domain Name** | `\b([a-z0-9-]+\.)+[a-z]{2,}\b` | `example.com`, `sub.domain.io` |
| **MAC Address** | `([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}` | `00:1A:2B:3C:4D:5E` |
| **Date (ISO 8601)** | `[0-9]{4}-[0-9]{2}-[0-9]{2}` | `2024-12-02`, `2023-01-15` |
| **Date (US/UK)** | `[0-9]{2}/[0-9]{2}/[0-9]{4}` | `12/02/2024`, `02/12/2024` |
| **Time (24h)** | `([01][0-9]\|2[0-3]):[0-5][0-9]:[0-5][0-9]` | `14:30:00`, `09:05:23` |
| **Timestamp (ISO)** | `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}` | `2024-12-02T14:30:00` |
| **Phone (US)** | `\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}` | `(555) 123-4567`, `555-123-4567` |
| **Credit Card** | `[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}` | `1234-5678-9012-3456` |
| **Currency (USD)** | `\$[0-9]{1,3}(,[0-9]{3})*(\.[0-9]{2})?` | `$1,234.56`, `$999` |
| **DNA Sequence** | `^[ATGC]+$` | `ATGCTAGC`, `GGCCAATT` |
| **RNA Sequence** | `^[AUGC]+$` | `AUGCUAGC`, `GGCCAAUU` |
| **Protein Sequence** | `^[ACDEFGHIKLMNPQRSTVWY]+$` | `MKTAYIAKQR`, `ACDEFGH` |
| **UUID** | `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` | `550e8400-e29b-41d4-a716-446655440000` |
| **Hex Color** | `#[0-9A-Fa-f]{6}\|#[0-9A-Fa-f]{3}` | `#FF5733`, `#f00` |
| **IPv4 CIDR** | `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2}` | `192.168.1.0/24`, `10.0.0.0/8` |
| **Git Hash (short)** | `\b[0-9a-f]{7}\b` | `a3d5f7e`, `1234567` |
| **Git Hash (full)** | `\b[0-9a-f]{40}\b` | `1234567890abcdef...` |
| **Log Level** | `\b(DEBUG\|INFO\|WARN(ING)?\|ERROR\|FATAL\|CRITICAL)\b` | `ERROR`, `WARNING`, `INFO` |
| **SSN (US)** | `[0-9]{3}-[0-9]{2}-[0-9]{4}` | `123-45-6789` |
| **Unix Path** | `^/([^/]+/)*[^/]+$` | `/usr/local/bin`, `/home/user/file.txt` |
| **File Extension** | `\.(txt\|csv\|json\|xml\|yaml)$` | `.txt`, `.json`, `.csv` |

### Quick Syntax Reminder

| Symbol | Meaning | Example |
|--------|---------|---------|
| `.` | Any single character | `c.t` matches `cat`, `cot`, `c5t` |
| `^` | Start of line | `^Hello` matches lines starting with "Hello" |
| `$` | End of line | `world$` matches lines ending with "world" |
| `*` | Zero or more | `ab*c` matches `ac`, `abc`, `abbc` |
| `+` | One or more | `ab+c` matches `abc`, `abbc` (not `ac`) |
| `?` | Zero or one | `ab?c` matches `ac`, `abc` |
| `[abc]` | Character class | Matches `a`, `b`, or `c` |
| `[^abc]` | Negated class | Matches anything except `a`, `b`, `c` |
| `[a-z]` | Range | Matches any lowercase letter |
| `\|` | Alternation (OR) | `cat\|dog` matches `cat` or `dog` |
| `()` | Grouping | `(ab)+` matches `ab`, `abab`, `ababab` |
| `{n}` | Exactly n times | `[0-9]{3}` matches exactly 3 digits |
| `{n,}` | n or more times | `[0-9]{3,}` matches 3+ digits |
| `{n,m}` | Between n and m | `[0-9]{2,4}` matches 2-4 digits |
| `\b` | Word boundary | `\bcat\b` matches "cat" but not "category" |
| `\d` | Digit (some tools) | Equivalent to `[0-9]` |
| `\w` | Word character | Equivalent to `[A-Za-z0-9_]` |
| `\s` | Whitespace | Matches space, tab, newline |
| `\\` | Escape character | `\.` matches literal dot |
