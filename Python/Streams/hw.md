# Homework: Input/Output Streams in Python

## Exercise 1: Basic Filter ⭐

Create a program `uppercase.py` that reads text from stdin and outputs it in UPPERCASE.

**Requirements:**
- Read line by line from stdin
- Output to stdout
- Handle both English and non-English text

**Example usage:**
```bash
echo "hello world" | python uppercase.py
# HELLO WORLD

cat file.txt | python uppercase.py
```

<details>
<summary>Hint</summary>

```python
import sys

for line in sys.stdin:
    print(line.rstrip().upper())
```
</details>

---

## Exercise 2: Filter with Arguments ⭐⭐

Create a program `filter_lines.py` that filters lines by pattern.

**Requirements:**
- First argument — search pattern
- Option `-i` or `--ignore-case` — ignore case
- Option `-v` or `--invert` — show lines WITHOUT the pattern
- Option `-n` or `--line-number` — show line numbers

**Example usage:**
```bash
# Find lines containing "error"
cat app.log | python filter_lines.py error

# Ignore case
cat app.log | python filter_lines.py -i ERROR

# Show lines WITHOUT "test"
cat data.txt | python filter_lines.py -v test

# With line numbers
cat file.txt | python filter_lines.py -n python
```

<details>
<summary>Hint</summary>

Use `argparse` for argument parsing:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pattern')
parser.add_argument('-i', '--ignore-case', action='store_true')
parser.add_argument('-v', '--invert', action='store_true')
parser.add_argument('-n', '--line-number', action='store_true')
args = parser.parse_args()
```
</details>

---

## Exercise 3: Text Statistics ⭐⭐

Create a program `textstats.py` that analyzes text.

**Requirements:**
- Count lines, words, characters
- Option `-l` — only lines
- Option `-w` — only words  
- Option `-c` — only characters
- Without options — show all
- Work with files and stdin

**Example usage:**
```bash
# From stdin
cat file.txt | python textstats.py
#      42     256    1844

# From file
python textstats.py file.txt
#      42     256    1844  file.txt

# Only line count
cat file.txt | python textstats.py -l
#      42

# Multiple files
python textstats.py file1.txt file2.txt file3.txt
#      42     256    1844  file1.txt
#      15      89     512  file2.txt
#      28     178     987  file3.txt
#      85     523    3343  total
```

---

## Exercise 4: CSV Filter ⭐⭐⭐

Create a program `csvfilter.py` for working with CSV files.

**Requirements:**
- Option `-c COLUMN` — column number or name for filtering
- Option `-v VALUE` — value to filter by
- Option `-d DELIMITER` — delimiter (default `,`)
- Show header if present
- Filter rows where specified column equals value

**Example usage:**
```bash
# users.csv:
# name,age,city
# Alice,25,Moscow
# Bob,30,London
# Charlie,25,Paris

# Filter by age
cat users.csv | python csvfilter.py -c age -v 25
# name,age,city
# Alice,25,Moscow
# Charlie,25,Paris

# Filter by column name
cat users.csv | python csvfilter.py -c city -v Moscow
# name,age,city
# Alice,25,Moscow

# With different delimiter
cat data.tsv | python csvfilter.py -d $'\t' -c 2 -v value
```

<details>
<summary>Hint</summary>

Use the `csv` module:

```python
import csv
import sys

reader = csv.DictReader(sys.stdin, delimiter=delimiter)
writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)

writer.writeheader()
for row in reader:
    if row[column] == value:
        writer.writerow(row)
```
</details>

---

## Exercise 5: JSON Processor ⭐⭐⭐

Create a program `jsonfilter.py` for working with JSON Lines (JSONL).

**Requirements:**
- Read JSONL from stdin (each line is a separate JSON object)
- Option `-k KEY` — extract value by key
- Option `-f FIELD=VALUE` — filter by field
- Option `--pretty` — pretty print JSON

**Example usage:**
```bash
# data.jsonl:
# {"name": "Alice", "age": 25, "city": "Moscow"}
# {"name": "Bob", "age": 30, "city": "London"}
# {"name": "Charlie", "age": 25, "city": "Paris"}

# Extract names
cat data.jsonl | python jsonfilter.py -k name
# Alice
# Bob
# Charlie

# Filter by age
cat data.jsonl | python jsonfilter.py -f age=25
# {"name": "Alice", "age": 25, "city": "Moscow"}
# {"name": "Charlie", "age": 25, "city": "Paris"}

# Pretty print
cat data.jsonl | python jsonfilter.py -f city=Moscow --pretty
# {
#   "name": "Alice",
#   "age": 25,
#   "city": "Moscow"
# }
```

---

## Exercise 6: Data Aggregation ⭐⭐⭐

Create a program `aggregate.py` for calculating field statistics.

**Requirements:**
- Read CSV from stdin
- Option `-g COLUMN` — group by column
- Option `-a FUNC:COLUMN` — aggregate (count, sum, avg, min, max)
- Support multiple aggregations

**Example usage:**
```bash
# sales.csv:
# product,quantity,price
# Apple,10,50
# Orange,5,30
# Apple,15,50
# Banana,8,20
# Orange,10,30

# Count by product
cat sales.csv | python aggregate.py -g product -a count:product
# product,count
# Apple,2
# Orange,2
# Banana,1

# Sum quantity by product
cat sales.csv | python aggregate.py -g product -a sum:quantity
# product,sum_quantity
# Apple,25
# Orange,15
# Banana,8

# Multiple aggregations
cat sales.csv | python aggregate.py -g product -a sum:quantity -a avg:price
# product,sum_quantity,avg_price
# Apple,25,50.0
# Orange,15,30.0
# Banana,8,20.0
```

---

## Exercise 7: Log Analyzer ⭐⭐⭐⭐

Create a program `loganalyzer.py` for web server log analysis.

**Requirements:**
- Parse logs in Apache/Nginx format:
  ```
  127.0.0.1 - - [01/Jan/2024:12:00:00 +0000] "GET /api/users HTTP/1.1" 200 1234
  ```
- Option `--status CODE` — filter by HTTP status
- Option `--method METHOD` — filter by HTTP method
- Option `--stats` — show statistics
- Option `--top N` — top N IP addresses

**Example usage:**
```bash
# Only 404 errors
cat access.log | python loganalyzer.py --status 404

# Only POST requests
cat access.log | python loganalyzer.py --method POST

# Statistics
cat access.log | python loganalyzer.py --stats
# Total requests: 1000
# Total bytes: 1234567
# By status:
#   200: 850
#   404: 100
#   500: 50
# Top IPs:
#   192.168.1.1: 250
#   192.168.1.2: 180
#   ...

# Combined filters
cat access.log | python loganalyzer.py --status 500 --top 5
```

<details>
<summary>Parsing hint</summary>

```python
import re
from collections import Counter

pattern = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) (\S+)" (\d+) (\d+)'

for line in sys.stdin:
    match = re.match(pattern, line)
    if match:
        ip = match.group(1)
        timestamp = match.group(2)
        method = match.group(3)
        path = match.group(4)
        status = int(match.group(6))
        size = int(match.group(7))
        # ...
```
</details>

---

## Exercise 8: Pipeline Utility ⭐⭐⭐⭐

Create a program `pipeline.py` that runs multiple commands in a pipeline.

**Requirements:**
- Accept commands as arguments (separated by `--`)
- Connect them in a pipeline
- Pass stdin to first command
- Output result of last command to stdout

**Example usage:**
```bash
# Equivalent to: cat file.txt | grep error | wc -l
cat file.txt | python pipeline.py grep error -- wc -l

# Equivalent to: ps aux | grep python | awk '{print $2}'
ps aux | python pipeline.py grep python -- awk '{print $2}'
```

<details>
<summary>Hint</summary>

```python
import subprocess
import sys

# Split arguments into separate commands
commands = []
current_cmd = []
for arg in sys.argv[1:]:
    if arg == '--':
        commands.append(current_cmd)
        current_cmd = []
    else:
        current_cmd.append(arg)
if current_cmd:
    commands.append(current_cmd)

# Create pipeline
processes = []
stdin = sys.stdin

for cmd in commands:
    proc = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE)
    processes.append(proc)
    stdin = proc.stdout

# Read final output
for line in stdin:
    sys.stdout.buffer.write(line)
```
</details>

---

## Exercise 9: Progress Monitor ⭐⭐⭐

Create a program `progress.py` that shows stream processing progress.

**Requirements:**
- Pass data through unchanged
- Show in stderr: number of processed lines and speed
- Update every second
- Option `--bytes` — count bytes instead of lines
- Option `--quiet` — don't show progress

**Example usage:**
```bash
cat huge_file.log | python progress.py | grep ERROR > errors.txt
# Progress in stderr:
# Processed 10000 lines (15234 lines/sec)
# Processed 20000 lines (16891 lines/sec)
# ...
# Total: 1000000 lines in 62.3 sec

# With byte counting
cat file.bin | python progress.py --bytes | gzip > file.gz
# Processed 1.2 MB (450 KB/sec)
```

---

## Exercise 10: Universal Converter ⭐⭐⭐⭐⭐

Create a program `convert.py` for converting between different formats.

**Requirements:**
- Option `--from FORMAT` — input format (json, csv, tsv, jsonl)
- Option `--to FORMAT` — output format (json, csv, tsv, jsonl)
- Automatic structure detection
- Preserve headers when converting

**Example usage:**
```bash
# CSV to JSON
cat data.csv | python convert.py --from csv --to json
# [
#   {"name": "Alice", "age": "25"},
#   {"name": "Bob", "age": "30"}
# ]

# JSON to CSV
cat data.json | python convert.py --from json --to csv
# name,age
# Alice,25
# Bob,30

# JSONL to TSV
cat data.jsonl | python convert.py --from jsonl --to tsv
# name	age
# Alice	25
# Bob	30

# All together in pipeline
cat data.csv | python convert.py --from csv --to jsonl | \
  python jsonfilter.py -f age=25 | \
  python convert.py --from jsonl --to csv
```

---

## Bonus Exercise: Create Your Own Utility ⭐⭐⭐⭐⭐

Design and implement your own Unix utility in Python.

**Ideas:**
- Markdown to HTML converter
- Test data generator
- Calculator in `bc` style
- Simple SQL processor for CSV
- Data visualizer in terminal (ASCII graphs)
- Stream encryptor/decryptor
- Programming language detector from code

**Requirements:**
- Follow Unix philosophy
- Work with stdin/stdout
- Proper error handling
- Documentation (help via `--help`)
- Usage examples

---

## Testing Your Programs

Create tests for your utilities:

```python
#!/usr/bin/env python3
"""Tests for utilities"""
import subprocess
import sys

def run_command(cmd, input_data):
    """Run command with input data"""
    result = subprocess.run(
        cmd,
        input=input_data,
        capture_output=True,
        text=True,
        shell=True
    )
    return result.stdout, result.stderr, result.returncode

def test_uppercase():
    """Test for uppercase.py"""
    output, _, code = run_command(
        'python uppercase.py',
        'hello world\n'
    )
    assert output == 'HELLO WORLD\n'
    assert code == 0
    print("✓ uppercase.py test passed")

def test_filter_lines():
    """Test for filter_lines.py"""
    input_data = "line with error\nline without\nanother error\n"
    output, _, code = run_command(
        'python filter_lines.py error',
        input_data
    )
    assert 'line with error' in output
    assert 'another error' in output
    assert 'line without' not in output
    assert code == 0
    print("✓ filter_lines.py test passed")

if __name__ == "__main__":
    test_uppercase()
    test_filter_lines()
    print("\n✓ All tests passed!")
```

---

## Grading Criteria

- ⭐ — Basic level (required)
- ⭐⭐ — Intermediate level (recommended)
- ⭐⭐⭐ — Advanced level (for deeper understanding)
- ⭐⭐⭐⭐ — Expert level (for ambitious learners)
- ⭐⭐⭐⭐⭐ — Master level (creative assignment)

**What we're checking:**
1. Correct work with stdin/stdout/stderr
2. Command-line argument handling
3. Proper exit codes
4. Error handling (BrokenPipeError, KeyboardInterrupt)
5. Code readability and structure
6. Documentation and usage examples

Good luck! 🚀
