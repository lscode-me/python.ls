# Input/Output Streams in Python: The Unix Approach

## Introduction

One of the key ideas of Unix philosophy is that programs should work together as building blocks, exchanging data through standard streams. In this lecture, we'll learn how to write Python programs that follow this philosophy.

## Unix Philosophy Applied to Python

**Core Principles:**

1. **Do one thing well** — each program solves one task
2. **Use text streams** — a universal interface
3. **Combine programs** — connect simple tools to solve complex problems

Python is ideal for creating such tools!

## Standard Streams

Every Unix program has three standard streams:

- **stdin** (0) — standard input
- **stdout** (1) — standard output  
- **stderr** (2) — standard error

In Python, you can access them through the `sys` module:

```python
import sys

# Read from stdin
data = sys.stdin.read()

# Write to stdout
sys.stdout.write("Result\n")

# Write errors to stderr
sys.stderr.write("Error!\n")
```

## Reading from stdin

### Method 1: Line-by-line Reading

```python
import sys

# Read line by line (most efficient)
for line in sys.stdin:
    # line already contains '\n' at the end
    print(line.rstrip())  # Remove newline
```

**Usage:**
```bash
cat file.txt | python script.py
echo -e "line1\nline2" | python script.py
```

### Method 2: Read All Input

```python
import sys

# Read all input at once
all_data = sys.stdin.read()
print(f"Received {len(all_data)} characters")
```

### Method 3: Read List of Lines

```python
import sys

# Read all lines into a list
lines = sys.stdin.readlines()
for i, line in enumerate(lines, 1):
    print(f"{i}: {line.rstrip()}")
```

## Practical Example: Simple Filter

Let's create a program that numbers lines (like `cat -n`):

```python
#!/usr/bin/env python3
"""Number lines from input stream"""
import sys

def number_lines():
    for i, line in enumerate(sys.stdin, 1):
        print(f"{i:6d}  {line.rstrip()}")

if __name__ == "__main__":
    number_lines()
```

**Usage:**
```bash
chmod +x number_lines.py
cat /etc/passwd | ./number_lines.py
./number_lines.py < file.txt
```

## Writing to stdout and stderr

### Proper Stream Usage

```python
import sys

def process_data():
    try:
        for i, line in enumerate(sys.stdin, 1):
            # Normal output goes to stdout
            print(line.rstrip().upper())
            
            # Progress and debugging go to stderr
            if i % 1000 == 0:
                print(f"Processed {i} lines", file=sys.stderr)
                
    except Exception as e:
        # Errors always go to stderr
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
```

**Why this matters:**
```bash
# Save only results, see errors on screen
./script.py < input.txt > output.txt

# Redirect both results and errors
./script.py < input.txt > output.txt 2> errors.log

# Ignore errors
./script.py < input.txt 2>/dev/null
```

## Working with Command-Line Arguments

### Basic Approach: sys.argv

```python
import sys

if len(sys.argv) < 2:
    print("Usage: script.py <filename>", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]
```

### Professional Approach: argparse

```python
#!/usr/bin/env python3
"""Filter for text processing"""
import sys
import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        description='Filter lines by pattern'
    )
    parser.add_argument(
        'pattern',
        help='Search pattern'
    )
    parser.add_argument(
        '-i', '--ignore-case',
        action='store_true',
        help='Ignore case'
    )
    parser.add_argument(
        '-v', '--invert',
        action='store_true',
        help='Invert match'
    )
    parser.add_argument(
        '-c', '--count',
        action='store_true',
        help='Count matches only'
    )
    return parser

def filter_lines(pattern, ignore_case=False, invert=False, count=False):
    if ignore_case:
        pattern = pattern.lower()
    
    matched = 0
    for line in sys.stdin:
        line_to_check = line.lower() if ignore_case else line
        
        matches = pattern in line_to_check
        if invert:
            matches = not matches
            
        if matches:
            matched += 1
            if not count:
                print(line.rstrip())
    
    if count:
        print(matched)

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        filter_lines(
            args.pattern,
            ignore_case=args.ignore_case,
            invert=args.invert,
            count=args.count
        )
    except KeyboardInterrupt:
        sys.exit(130)  # Standard exit code for Ctrl+C
    except BrokenPipeError:
        # Happens when next program in pipeline terminates
        sys.exit(0)

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
./filter.py python < file.txt
./filter.py -i ERROR < app.log
./filter.py -c "success" < results.txt
./filter.py -v "test" < data.txt | head -10
```

## Reading from Files or stdin

Universal utility that works with both files and stdin:

```python
#!/usr/bin/env python3
"""Word frequency counter"""
import sys
import argparse
from collections import Counter

def count_words(file_obj):
    """Count words from file object"""
    counter = Counter()
    for line in file_obj:
        words = line.lower().split()
        counter.update(words)
    return counter

def main():
    parser = argparse.ArgumentParser(
        description='Count word frequencies'
    )
    parser.add_argument(
        'files',
        nargs='*',  # 0 or more files
        help='Files to process (or stdin if not specified)'
    )
    parser.add_argument(
        '-n', '--top',
        type=int,
        default=10,
        help='Show top N words (default: 10)'
    )
    args = parser.parse_args()
    
    counter = Counter()
    
    if not args.files:
        # If no files specified, read from stdin
        counter.update(count_words(sys.stdin))
    else:
        # Process each file
        for filename in args.files:
            try:
                with open(filename) as f:
                    counter.update(count_words(f))
            except FileNotFoundError:
                print(f"Error: file '{filename}' not found", 
                      file=sys.stderr)
                sys.exit(1)
            except PermissionError:
                print(f"Error: no access to '{filename}'", 
                      file=sys.stderr)
                sys.exit(1)
    
    # Print results
    for word, count in counter.most_common(args.top):
        print(f"{count:8d}  {word}")

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
# From stdin
cat *.txt | ./wordcount.py

# From files
./wordcount.py file1.txt file2.txt

# Combined options
./wordcount.py -n 20 *.log
```

## Buffering

### The Buffering Problem

Python buffers output, which can be problematic for interactive programs:

```python
import sys
import time

# Bad: output appears after 10 seconds
for i in range(10):
    print(f"Step {i}")
    time.sleep(1)
```

### Solutions

**1. Force buffer flush:**
```python
import sys
import time

for i in range(10):
    print(f"Step {i}")
    sys.stdout.flush()  # Force output
    time.sleep(1)
```

**2. Use flush parameter:**
```python
import time

for i in range(10):
    print(f"Step {i}", flush=True)
    time.sleep(1)
```

**3. Disable buffering:**
```bash
# When running the program
python -u script.py

# Or via environment variable
PYTHONUNBUFFERED=1 python script.py
```

**4. In code:**
```python
import sys
import io

# Replace stdout with unbuffered version
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer,
    line_buffering=True
)
```

## Signal Handling

Proper interrupt handling:

```python
#!/usr/bin/env python3
import sys
import signal
import time

def signal_handler(sig, frame):
    """Interrupt signal handler"""
    print("\nProgram interrupted by user", file=sys.stderr)
    sys.exit(130)  # Standard code for SIGINT

# Register handler
signal.signal(signal.SIGINT, signal_handler)

def main():
    try:
        for i, line in enumerate(sys.stdin, 1):
            # Processing...
            print(line.rstrip())
            
    except BrokenPipeError:
        # Normal situation in pipeline
        # For example: ./script.py | head -10
        sys.stderr.close()
        sys.exit(0)
    except KeyboardInterrupt:
        # Alternative way to handle Ctrl+C
        sys.exit(130)

if __name__ == "__main__":
    main()
```

## Practical Examples of Unix Utilities

### 1. Line Filter (grep-like)

```python
#!/usr/bin/env python3
"""Simple grep analog"""
import sys
import re
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern')
    parser.add_argument('-i', '--ignore-case', action='store_true')
    parser.add_argument('-v', '--invert', action='store_true')
    parser.add_argument('-n', '--line-number', action='store_true')
    args = parser.parse_args()
    
    flags = re.IGNORECASE if args.ignore_case else 0
    pattern = re.compile(args.pattern, flags)
    
    for i, line in enumerate(sys.stdin, 1):
        matches = bool(pattern.search(line))
        if args.invert:
            matches = not matches
            
        if matches:
            if args.line_number:
                print(f"{i}:{line.rstrip()}")
            else:
                print(line.rstrip())

if __name__ == "__main__":
    main()
```

### 2. Column Output (column-like)

```python
#!/usr/bin/env python3
"""Format text into columns"""
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--separator', default=None)
    parser.add_argument('-t', '--table', action='store_true')
    args = parser.parse_args()
    
    lines = sys.stdin.readlines()
    
    # Split into fields
    rows = []
    for line in lines:
        if args.separator:
            fields = line.rstrip().split(args.separator)
        else:
            fields = line.split()
        rows.append(fields)
    
    if not rows:
        return
    
    # Find maximum width of each column
    max_cols = max(len(row) for row in rows)
    widths = [0] * max_cols
    
    for row in rows:
        for i, field in enumerate(row):
            widths[i] = max(widths[i], len(field))
    
    # Print aligned data
    for row in rows:
        formatted = []
        for i, field in enumerate(row):
            if i < len(widths):
                formatted.append(field.ljust(widths[i]))
            else:
                formatted.append(field)
        print('  '.join(formatted).rstrip())

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
cat /etc/passwd | ./column.py -s: -t
ls -l | ./column.py
```

### 3. Count Lines/Words/Characters (wc-like)

```python
#!/usr/bin/env python3
"""wc analog - count lines, words, characters"""
import sys
import argparse

def count_stats(file_obj, filename=None):
    """Count statistics for file"""
    lines = 0
    words = 0
    chars = 0
    
    for line in file_obj:
        lines += 1
        words += len(line.split())
        chars += len(line)
    
    return lines, words, chars, filename

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    parser.add_argument('-l', '--lines', action='store_true')
    parser.add_argument('-w', '--words', action='store_true')
    parser.add_argument('-c', '--chars', action='store_true')
    args = parser.parse_args()
    
    # If no flags specified, show everything
    if not (args.lines or args.words or args.chars):
        args.lines = args.words = args.chars = True
    
    results = []
    
    if not args.files:
        # Read from stdin
        results.append(count_stats(sys.stdin))
    else:
        # Read from files
        for filename in args.files:
            try:
                with open(filename) as f:
                    results.append(count_stats(f, filename))
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error: {e}", file=sys.stderr)
                continue
    
    # Print results
    total_lines = total_words = total_chars = 0
    
    for lines, words, chars, filename in results:
        total_lines += lines
        total_words += words
        total_chars += chars
        
        output = []
        if args.lines:
            output.append(f"{lines:8d}")
        if args.words:
            output.append(f"{words:8d}")
        if args.chars:
            output.append(f"{chars:8d}")
        
        result = ' '.join(output)
        if filename:
            result += f"  {filename}"
        print(result)
    
    # If more than one file, show totals
    if len(results) > 1:
        output = []
        if args.lines:
            output.append(f"{total_lines:8d}")
        if args.words:
            output.append(f"{total_words:8d}")
        if args.chars:
            output.append(f"{total_chars:8d}")
        print(' '.join(output) + "  total")

if __name__ == "__main__":
    main()
```

### 4. Data Transformation (JSON to CSV)

```python
#!/usr/bin/env python3
"""JSON to CSV converter"""
import sys
import json
import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delimiter', default=',')
    parser.add_argument('-k', '--keys', help='Comma-separated field list')
    args = parser.parse_args()
    
    try:
        # Read JSON
        data = json.load(sys.stdin)
        
        if not data:
            return
        
        # If data is a list of objects
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        
        # Determine fields
        if args.keys:
            fieldnames = args.keys.split(',')
        else:
            # Collect all unique keys
            fieldnames = set()
            for item in items:
                if isinstance(item, dict):
                    fieldnames.update(item.keys())
            fieldnames = sorted(fieldnames)
        
        # Write CSV
        writer = csv.DictWriter(
            sys.stdout,
            fieldnames=fieldnames,
            delimiter=args.delimiter,
            extrasaction='ignore'
        )
        
        writer.writeheader()
        for item in items:
            if isinstance(item, dict):
                writer.writerow(item)
                
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}", file=sys.stderr)
        sys.exit(1)
    except BrokenPipeError:
        sys.stderr.close()
        sys.exit(0)

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
cat data.json | ./json2csv.py > data.csv
curl -s api.example.com/users | ./json2csv.py -k id,name,email
```

## Advanced Techniques

### Working with Binary Data

```python
import sys

# Binary mode for stdin/stdout
binary_stdin = sys.stdin.buffer
binary_stdout = sys.stdout.buffer

# Read binary data
data = binary_stdin.read()

# Write binary data
binary_stdout.write(b'\x00\xFF\xAA')
```

### Creating Pipelines in Python

```python
import subprocess
import sys

def pipeline_example():
    """Create pipeline: cat file.txt | grep 'pattern' | wc -l"""
    
    # First command
    p1 = subprocess.Popen(
        ['cat', 'file.txt'],
        stdout=subprocess.PIPE
    )
    
    # Second command
    p2 = subprocess.Popen(
        ['grep', 'pattern'],
        stdin=p1.stdout,
        stdout=subprocess.PIPE
    )
    
    # Close our end of the pipe
    p1.stdout.close()
    
    # Third command
    p3 = subprocess.Popen(
        ['wc', '-l'],
        stdin=p2.stdout,
        stdout=subprocess.PIPE
    )
    
    p2.stdout.close()
    
    # Get result
    output, _ = p3.communicate()
    return output.decode().strip()
```

### Progress Bar for Pipeline

```python
#!/usr/bin/env python3
"""Show stream processing progress"""
import sys
import time

def progress_filter():
    count = 0
    start_time = time.time()
    
    for line in sys.stdin:
        count += 1
        sys.stdout.write(line)
        
        # Show statistics in stderr every second
        if count % 1000 == 0:
            elapsed = time.time() - start_time
            rate = count / elapsed if elapsed > 0 else 0
            print(
                f"\rProcessed: {count:,} lines "
                f"({rate:.0f} lines/sec)",
                file=sys.stderr,
                end='',
                flush=True
            )
    
    # Final statistics
    elapsed = time.time() - start_time
    print(
        f"\nTotal: {count:,} lines in {elapsed:.1f} sec",
        file=sys.stderr
    )

if __name__ == "__main__":
    try:
        progress_filter()
    except BrokenPipeError:
        sys.stderr.close()
        sys.exit(0)
```

**Usage:**
```bash
cat huge_file.log | ./progress.py | grep ERROR > errors.txt
```

## Best Practices

### 1. Exit Codes

```python
import sys

# Success
sys.exit(0)

# General error
sys.exit(1)

# Incorrect usage
sys.exit(2)

# Interrupted (Ctrl+C)
sys.exit(130)
```

### 2. Universal Utility Template

```python
#!/usr/bin/env python3
"""
Template for Unix utility in Python
"""
import sys
import argparse
import signal

def signal_handler(sig, frame):
    sys.exit(130)

signal.signal(signal.SIGINT, signal_handler)

def create_parser():
    parser = argparse.ArgumentParser(
        description='Utility description'
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Input files (or stdin)'
    )
    # Add your arguments
    return parser

def process_file(file_obj, args):
    """Process single file/stream"""
    for line in file_obj:
        # Your logic here
        print(line.rstrip())

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        if not args.files:
            # Read from stdin
            process_file(sys.stdin, args)
        else:
            # Process files
            for filename in args.files:
                try:
                    with open(filename) as f:
                        process_file(f, args)
                except FileNotFoundError:
                    print(f"Error: '{filename}' not found", 
                          file=sys.stderr)
                    sys.exit(1)
                except PermissionError:
                    print(f"Error: no access to '{filename}'", 
                          file=sys.stderr)
                    sys.exit(1)
                    
    except BrokenPipeError:
        sys.stderr.close()
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(130)

if __name__ == "__main__":
    main()
```

### 3. Encoding Handling

```python
import sys

# Explicitly specify encoding
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Or when opening a file
with open('file.txt', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())
```

### 4. Testing Utilities

```python
import subprocess
import sys

def test_utility():
    """Test our utility"""
    # Prepare test data
    test_input = "line1\nline2\nline3\n"
    
    # Run utility
    result = subprocess.run(
        ['python', 'my_utility.py'],
        input=test_input,
        capture_output=True,
        text=True
    )
    
    # Check result
    assert result.returncode == 0
    assert result.stdout == expected_output
    
    print("Test passed!")

if __name__ == "__main__":
    test_utility()
```

## Real-World Examples

### Log Processing

```python
#!/usr/bin/env python3
"""Log analyzer with filtering and statistics"""
import sys
import re
from datetime import datetime
from collections import Counter, defaultdict
import argparse

def parse_log_line(line):
    """Parse Apache/Nginx log line"""
    pattern = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) (\S+)" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        return {
            'ip': match.group(1),
            'timestamp': match.group(2),
            'method': match.group(3),
            'path': match.group(4),
            'protocol': match.group(5),
            'status': int(match.group(6)),
            'size': int(match.group(7))
        }
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--status', type=int, 
                       help='Filter by HTTP status')
    parser.add_argument('--stats', action='store_true',
                       help='Show statistics')
    args = parser.parse_args()
    
    stats = {
        'total': 0,
        'by_status': Counter(),
        'by_ip': Counter(),
        'total_bytes': 0
    }
    
    for line in sys.stdin:
        entry = parse_log_line(line)
        if not entry:
            continue
        
        stats['total'] += 1
        stats['by_status'][entry['status']] += 1
        stats['by_ip'][entry['ip']] += 1
        stats['total_bytes'] += entry['size']
        
        # Filtering
        if args.status and entry['status'] != args.status:
            continue
        
        if not args.stats:
            print(line.rstrip())
    
    # Print statistics
    if args.stats:
        print(f"\n=== Statistics ===", file=sys.stderr)
        print(f"Total requests: {stats['total']}", file=sys.stderr)
        print(f"Total bytes: {stats['total_bytes']:,}", file=sys.stderr)
        print(f"\nTop 10 IP addresses:", file=sys.stderr)
        for ip, count in stats['by_ip'].most_common(10):
            print(f"  {ip}: {count}", file=sys.stderr)
        print(f"\nBy status:", file=sys.stderr)
        for status in sorted(stats['by_status'].keys()):
            count = stats['by_status'][status]
            print(f"  {status}: {count}", file=sys.stderr)

if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.stderr.close()
        sys.exit(0)
```

**Usage:**
```bash
# Filter only errors
cat access.log | ./loganalyzer.py -s 404

# Show statistics
cat access.log | ./loganalyzer.py --stats

# Combine with other tools
cat access.log | ./loganalyzer.py -s 500 | grep "api" | wc -l
```

## Conclusion

Python is an excellent tool for creating Unix utilities:

✅ **Simplicity** — easy to read and maintain  
✅ **Rich standard library** — regex, json, csv, argparse  
✅ **Cross-platform** — works everywhere  
✅ **Performance** — sufficient for most tasks  

**Key Takeaways:**
- Use `sys.stdin` for reading streams
- Write results to `stdout`, errors to `stderr`
- Handle `BrokenPipeError` and `KeyboardInterrupt`
- Make utilities universal (files or stdin)
- Follow Unix philosophy: one task, text streams, composability

**Remember:** A good Unix utility in Python can be simpler and clearer than an equivalent bash script, especially for complex logic!
