# Grep, Sed & Awk: Text Processing Power Tools

## Overview
The trio of `grep`, `sed`, and `awk` form the foundation of Unix text processing. Each tool excels at different tasks:
- **grep**: Search and filter lines
- **sed**: Stream editor for transformations
- **awk**: Pattern scanning and data extraction

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

### Extended Patterns (ERE)
```bash
(pattern)     # Grouping
|             # Alternation (OR)
{n}           # Exactly n times
{n,}          # n or more
{n,m}         # Between n and m
\b            # Word boundary
\d \w \s      # Digit, word, space (in some tools)
```

## Grep: Pattern Matching

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
grep -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' users.txt

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

# Extract all URLs
grep -Eo 'https?://[^ ]+' page.html

# Find failed login attempts
grep "Failed password" /var/log/auth.log | wc -l

# Search for credit card patterns (testing only!)
grep -E '\b[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}\b' data.txt
```

## Sed: Stream Editor

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

### Basic Awk Syntax
```bash
# Print entire line
awk '{print}' file.txt

# Print specific fields
awk '{print $1, $3}' file.txt

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
awk '{if ($3 > 100) print $1, $3}' data.txt

# Calculations
awk '{sum += $3} END {print sum}' numbers.txt

# Average
awk '{sum += $1; count++} END {print sum/count}' numbers.txt

# String operations
awk '{print length($0)}' file.txt    # Line length
awk '{print tolower($1)}' file.txt   # Lowercase
awk '{print substr($1, 1, 5)}' file.txt  # Substring
```

### CSV Processing with Awk
```bash
# Print specific columns
awk -F',' '{print $2, $4}' data.csv

# Skip header
awk -F',' 'NR > 1 {print $0}' data.csv

# Sum column
awk -F',' 'NR > 1 {sum += $3} END {print sum}' sales.csv

# Filter rows
awk -F',' '$3 > 1000 {print $0}' sales.csv

# Group by (simple)
awk -F',' '{sum[$2] += $3} END {for (key in sum) print key, sum[key]}' data.csv
```

### Log Analysis with Awk
```bash
# Count by status code
awk '{print $9}' access.log | sort | uniq -c

# Extract IP and status
awk '{print $1, $9}' access.log

# Calculate response time average
awk '{sum += $10; count++} END {print sum/count}' access.log

# Top 10 IPs by request count
awk '{ip[$1]++} END {for (i in ip) print ip[i], i}' access.log | sort -rn | head -10

# Requests per minute
awk '{print substr($4, 2, 16)}' access.log | uniq -c
```

### Practical Awk Examples

#### Example 1: Generate SQL INSERT Statements
```bash
awk -F',' 'NR > 1 {printf "INSERT INTO users VALUES (\"%s\", \"%s\", %s);\n", $1, $2, $3}' users.csv
```

#### Example 2: Convert CSV to JSON
```bash
awk -F',' 'NR > 1 {printf "{\"id\": \"%s\", \"name\": \"%s\", \"age\": %s}\n", $1, $2, $3}' users.csv
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
# Find errors, extract timestamps, count per hour
grep "ERROR" app.log | \
  sed 's/.*\[\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9]\{2\}\):.*/\1/' | \
  sort | uniq -c
```

### Pattern: Multi-Step Extraction
```bash
# Extract email domains and count
grep -Eo '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' users.txt | \
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
7. **Compile regex** when possible (`grep -P` for PCRE)

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

## Next Steps
- Practice regex on regex101.com
- Study awk programming language features
- Learn Perl for more complex text processing
- Explore ripgrep (rg) for faster searching
