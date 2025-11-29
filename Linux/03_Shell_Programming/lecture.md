# Shell Programming as a Mini-DSL for Data Processing

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

## Introduction

Bash isn't just a command interpreter — it's a powerful programming language designed for text processing and pipeline orchestration. When used correctly, shell scripts become a domain-specific language (DSL) for data transformation.

In this module, we'll learn to write safe, efficient data-processing scripts that leverage the full power of the shell.

---

## Command Substitution

Command substitution allows you to capture the output of a command and use it as a value.

### Modern Syntax: `$(...)`

```bash
# Capture command output
current_date=$(date +%Y-%m-%d)
echo "Today is $current_date"

# Use in pipelines
total_lines=$(cat data.csv | wc -l)
echo "File has $total_lines lines"

# Nested substitution
files_count=$(ls -1 $(pwd) | wc -l)

# In arithmetic
age=$((2024 - $(date +%Y)))
```

### Old Syntax: Backticks (avoid)

```bash
# Old style - harder to nest
result=`command`

# Prefer $(...) instead
result=$(command)
```

---

## Streaming Loops: `while read`

The `while read` loop processes data line by line, perfect for streaming large files without loading everything into memory.

### Basic Pattern

```bash
# Read from file
while read line; do
    echo "Processing: $line"
done < data.txt

# Read from pipe
cat data.txt | while read line; do
    process "$line"
done

# Read multiple fields
while IFS=',' read col1 col2 col3; do
    echo "$col1: $col2 = $col3"
done < data.csv
```

### Practical Examples

**Example 1: Calculate average**
```bash
#!/bin/bash
sum=0
count=0

while read value; do
    sum=$((sum + value))
    count=$((count + 1))
done < numbers.txt

average=$(echo "scale=2; $sum / $count" | bc)
echo "Average: $average"
```

**Example 2: Filter and transform CSV**
```bash
#!/bin/bash
# Extract high-value transactions

while IFS=',' read date amount category; do
    if [[ $amount -gt 100 ]]; then
        printf "%s\t%s\t%s\n" "$date" "$amount" "$category"
    fi
done < transactions.csv
```

**Example 3: JSONL to CSV**
```bash
#!/bin/bash
# Convert JSON Lines to CSV

echo "name,age,city"
while read line; do
    name=$(echo "$line" | jq -r '.name')
    age=$(echo "$line" | jq -r '.age')
    city=$(echo "$line" | jq -r '.city')
    echo "$name,$age,$city"
done < data.jsonl
```

---

## Arrays, Strings, and Arithmetic

### Arrays

```bash
# Declare array
fruits=("apple" "banana" "cherry")

# Access elements
echo "${fruits[0]}"  # apple
echo "${fruits[@]}"  # all elements
echo "${#fruits[@]}" # length

# Add elements
fruits+=("date")

# Loop through array
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# Read into array
mapfile -t lines < file.txt
# or
readarray -t lines < file.txt
```

### String Operations

```bash
text="Hello, World!"

# Length
echo "${#text}"  # 13

# Substring
echo "${text:0:5}"  # Hello
echo "${text:7}"    # World!

# Replace
echo "${text/World/Bash}"  # Hello, Bash!
echo "${text//o/0}"        # Hell0, W0rld!

# Case conversion
echo "${text^^}"  # HELLO, WORLD!
echo "${text,,}"  # hello, world!

# Trim whitespace
text="  data  "
trimmed="${text#"${text%%[![:space:]]*}"}"
trimmed="${trimmed%"${trimmed##*[![:space:]]}"}"

# Check if string contains substring
if [[ "$text" == *"World"* ]]; then
    echo "Found!"
fi
```

### Arithmetic

```bash
# Arithmetic expansion
x=5
y=3
echo $((x + y))    # 8
echo $((x * y))    # 15
echo $((x ** y))   # 125 (power)

# Increment/decrement
((x++))
((y--))
((x += 10))

# Comparison in arithmetic context
if ((x > y)); then
    echo "x is greater"
fi

# Floating point with bc
result=$(echo "scale=2; 10 / 3" | bc)
echo "$result"  # 3.33

# Random numbers
random=$((RANDOM % 100))  # 0-99
```

---

## Functions

### Basic Functions

```bash
# Define function
greet() {
    echo "Hello, $1!"
}

# Call function
greet "Alice"  # Hello, Alice!

# Function with return value
add() {
    local result=$(($1 + $2))
    echo "$result"
}

sum=$(add 5 3)
echo "Sum: $sum"

# Function with multiple outputs
stats() {
    local sum=0
    local count=0
    
    while read num; do
        sum=$((sum + num))
        count=$((count + 1))
    done
    
    echo "$sum $count"
}

read sum count < <(seq 1 10 | stats)
echo "Sum: $sum, Count: $count"
```

### Local Variables

```bash
process_data() {
    local input_file="$1"
    local output_file="$2"
    local temp_file=$(mktemp)
    
    # Process data
    cat "$input_file" | transform > "$temp_file"
    mv "$temp_file" "$output_file"
}
```

---

## Exit Codes and Error Handling

### Exit Codes

```bash
# Check last command exit code
ls /nonexistent
echo $?  # Non-zero indicates error

# Successful command
ls /tmp
echo $?  # 0 indicates success

# Set exit code in script
exit 0  # Success
exit 1  # Error
```

### Conditional Execution

```bash
# Run if previous command succeeded
command1 && command2

# Run if previous command failed
command1 || command2

# Chain conditionally
command1 && command2 || command3

# Multiple conditions
if command1 && command2; then
    echo "Both succeeded"
fi
```

### Error Handling with `set`

```bash
#!/bin/bash

# Exit on error
set -e

# Exit on undefined variable
set -u

# Fail on pipe errors
set -o pipefail

# Combine all (recommended)
set -euo pipefail

# Now any error stops the script
curl https://api.example.com/data | jq '.results[]' | process
```

### Custom Error Handling

```bash
#!/bin/bash
set -euo pipefail

error_exit() {
    echo "ERROR: $1" >&2
    exit 1
}

# Use in script
[ -f "data.csv" ] || error_exit "data.csv not found"

# With cleanup
cleanup() {
    rm -f "$temp_file"
}

trap cleanup EXIT

temp_file=$(mktemp)
process_data "$temp_file" || error_exit "Processing failed"
```

---

## Process Substitution

Process substitution creates temporary named pipes for command output, allowing you to use command output as if it were a file.

### Syntax

```bash
# Output as file: <(command)
# Input as file: >(command)
```

### Reading from Process Substitution

```bash
# Compare outputs of two commands
diff <(ls dir1) <(ls dir2)

# Use command output as file
while read line; do
    echo "Line: $line"
done < <(curl -s https://api.example.com/data | jq -r '.[]')

# Multiple inputs
paste <(cut -d',' -f1 file1.csv) <(cut -d',' -f2 file2.csv)
```

### Writing to Process Substitution

```bash
# Split output to multiple processes
command > >(process1) 2> >(process2)

# Tee to multiple destinations
echo "data" | tee >(process1) >(process2) >(process3)

# Log and process simultaneously
./script.sh 2>&1 | tee >(grep ERROR > errors.log) >(wc -l > linecount.txt)
```

### Practical Examples

**Example 1: Join transformed data streams**
```bash
#!/bin/bash
# Join two CSV files after transformation

join -t',' \
    <(sort -t',' -k1 file1.csv) \
    <(sort -t',' -k1 file2.csv)
```

**Example 2: Parallel processing**
```bash
#!/bin/bash
# Process two data sources in parallel

while read line1 <&3 && read line2 <&4; do
    echo "Combined: $line1 + $line2"
done 3< <(process_source1) 4< <(process_source2)
```

**Example 3: Complex pipeline with branches**
```bash
#!/bin/bash
# Split pipeline into multiple outputs

curl -s https://api.example.com/data | \
    jq -r '.results[]' | \
    tee \
        >(grep "ERROR" > errors.log) \
        >(grep "WARN" > warnings.log) \
        >(grep "INFO" | wc -l > info_count.txt) \
    > all_logs.txt
```

---

## Practical Data Processing Scripts

### Example 1: CSV Filter and Aggregate

```bash
#!/bin/bash
set -euo pipefail

# Filter CSV by date range and compute statistics

input_file="${1:-data.csv}"
start_date="${2:-2024-01-01}"
end_date="${3:-2024-12-31}"

echo "Processing $input_file from $start_date to $end_date"

# Skip header, filter by date, calculate stats
tail -n +2 "$input_file" | \
while IFS=',' read date amount category; do
    if [[ "$date" > "$start_date" && "$date" < "$end_date" ]]; then
        echo "$date,$amount,$category"
    fi
done | \
awk -F',' '{
    sum += $2
    count++
    if ($2 > max) max = $2
    if (min == 0 || $2 < min) min = $2
}
END {
    printf "Count: %d\n", count
    printf "Sum: %.2f\n", sum
    printf "Average: %.2f\n", sum/count
    printf "Min: %.2f\n", min
    printf "Max: %.2f\n", max
}'
```

### Example 2: JSONL to CSV Converter

```bash
#!/bin/bash
set -euo pipefail

# Convert JSONL to CSV with field selection

input="${1:-/dev/stdin}"
fields="${2:-name,age,city}"

# Extract field names
IFS=',' read -ra field_array <<< "$fields"

# Print CSV header
echo "$fields"

# Process each JSON line
while read -r line; do
    values=()
    for field in "${field_array[@]}"; do
        value=$(echo "$line" | jq -r ".$field // \"\"")
        values+=("$value")
    done
    
    # Join with commas
    IFS=','
    echo "${values[*]}"
done < "$input"
```

### Example 3: Streaming Calculator

```bash
#!/bin/bash
set -euo pipefail

# Calculate mean and median from streaming data

declare -a values=()
sum=0
count=0

while read -r num; do
    values+=("$num")
    sum=$(echo "$sum + $num" | bc)
    ((count++))
done

# Calculate mean
mean=$(echo "scale=2; $sum / $count" | bc)

# Calculate median
IFS=$'\n' sorted=($(sort -n <<<"${values[*]}"))
mid=$((count / 2))

if ((count % 2 == 0)); then
    median=$(echo "scale=2; (${sorted[$mid-1]} + ${sorted[$mid]}) / 2" | bc)
else
    median=${sorted[$mid]}
fi

echo "Count: $count"
echo "Mean: $mean"
echo "Median: $median"
```

---

## Best Practices

### 1. Always Use Quotes

```bash
# BAD: breaks on spaces
file=$1
cat $file

# GOOD
file="$1"
cat "$file"
```

### 2. Check Arguments

```bash
#!/bin/bash
set -euo pipefail

if [ $# -lt 2 ]; then
    echo "Usage: $0 <input> <output>" >&2
    exit 1
fi

input="$1"
output="$2"
```

### 3. Use Meaningful Variable Names

```bash
# BAD
f="data.csv"
n=$(cat $f | wc -l)

# GOOD
input_file="data.csv"
line_count=$(wc -l < "$input_file")
```

### 4. Add Comments

```bash
#!/bin/bash
# Process sales data and generate daily report
# Usage: ./process_sales.sh <input.csv> <output.txt>

set -euo pipefail

# Configuration
readonly MIN_AMOUNT=100
readonly DATE_FORMAT="%Y-%m-%d"

# Functions
filter_high_value() {
    awk -F',' -v min="$MIN_AMOUNT" '$2 >= min'
}
```

### 5. Use `readonly` for Constants

```bash
readonly API_URL="https://api.example.com"
readonly MAX_RETRIES=3
readonly TIMEOUT=30
```

---

## Summary

In this module, you learned:

- ✅ **Command substitution**: `$(...)` to capture output
- ✅ **Streaming loops**: `while read` for memory-efficient processing
- ✅ **Arrays and strings**: Data structures and manipulation
- ✅ **Arithmetic**: Integer and floating-point calculations
- ✅ **Functions**: Reusable code blocks
- ✅ **Exit codes**: Error detection and handling
- ✅ **`set -euo pipefail`**: Safe script execution
- ✅ **Process substitution**: `<(cmd)` and `>(cmd)` for advanced pipelines

### Next Steps

In the next module, we'll explore **Coreutils** — the essential building blocks for efficient data pipeline construction.
