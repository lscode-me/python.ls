# Week 6 — File Handling in Python
## Reading, Writing, and Processing Files

---

## 1. Opening and Closing Files

### Basic File Operations

```python
# Open a file
file = open('data.txt', 'r')
content = file.read()
file.close()

# Better: using with statement (automatic cleanup)
with open('data.txt', 'r') as file:
    content = file.read()
# File is automatically closed
```

### File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) - file must exist |
| `'w'` | Write - creates new or truncates existing |
| `'a'` | Append - creates new or appends to existing |
| `'x'` | Exclusive creation - fails if file exists |
| `'r+'` | Read and write |
| `'w+'` | Write and read (truncates) |
| `'a+'` | Append and read |
| `'b'` | Binary mode (e.g., `'rb'`, `'wb'`) |
| `'t'` | Text mode (default, e.g., `'rt'`) |

```python
# Text mode
with open('text.txt', 'r') as f:
    content = f.read()

# Binary mode
with open('image.png', 'rb') as f:
    data = f.read()

# Write mode
with open('output.txt', 'w') as f:
    f.write('Hello, World!')

# Append mode
with open('log.txt', 'a') as f:
    f.write('New log entry\n')
```

---

## 2. Reading Files

### read() - Read Entire File

```python
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Read specific number of characters
with open('data.txt', 'r') as file:
    chunk = file.read(100)  # Read first 100 characters
```

### readline() - Read One Line

```python
with open('data.txt', 'r') as file:
    first_line = file.readline()
    second_line = file.readline()
    print(first_line)
    print(second_line)
```

### readlines() - Read All Lines as List

```python
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

### Iterating Over File (Best Practice)

```python
# Most memory-efficient way
with open('large_file.txt', 'r') as file:
    for line in file:
        process(line.strip())
```

---

## 3. Writing Files

### write() - Write String

```python
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('Second line\n')
```

### writelines() - Write List of Strings

```python
lines = ['First line\n', 'Second line\n', 'Third line\n']

with open('output.txt', 'w') as file:
    file.writelines(lines)
```

### Appending to Files

```python
with open('log.txt', 'a') as file:
    file.write('New log entry\n')
```

---

## 4. File Positions and Seeking

### tell() - Get Current Position

```python
with open('data.txt', 'r') as file:
    print(file.tell())      # 0
    file.read(10)
    print(file.tell())      # 10
```

### seek() - Move to Position

```python
with open('data.txt', 'r') as file:
    file.seek(10)           # Move to byte 10
    data = file.read(5)     # Read 5 bytes
    
    file.seek(0)            # Move to beginning
    
    file.seek(0, 2)         # Move to end (0 bytes from end)
```

Seek reference points:
- `0` - beginning of file
- `1` - current position
- `2` - end of file

---

## 5. Working with Text Encodings

### Specifying Encoding

```python
# UTF-8 (default in Python 3)
with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Other encodings
with open('legacy.txt', 'r', encoding='latin-1') as file:
    content = file.read()

# Handle encoding errors
with open('data.txt', 'r', encoding='utf-8', errors='ignore') as file:
    content = file.read()
```

### Common Encoding Error Handlers

- `'strict'` - raise UnicodeDecodeError (default)
- `'ignore'` - ignore errors
- `'replace'` - replace with `�`
- `'backslashreplace'` - replace with escape sequences

---

## 6. Binary Files

### Reading Binary Data

```python
with open('image.png', 'rb') as file:
    data = file.read()
    print(f"File size: {len(data)} bytes")
    print(f"First 10 bytes: {data[:10]}")
```

### Writing Binary Data

```python
data = bytes([0x89, 0x50, 0x4E, 0x47])  # PNG header

with open('test.png', 'wb') as file:
    file.write(data)
```

### Copying Binary Files

```python
def copy_file(source, destination):
    with open(source, 'rb') as src:
        with open(destination, 'wb') as dst:
            dst.write(src.read())

copy_file('image.png', 'image_copy.png')
```

---

## 7. Context Managers for Files

### Multiple Files

```python
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line.upper())
```

### Custom File Context Manager

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with FileManager('data.txt', 'r') as file:
    content = file.read()
```

---

## 8. File System Operations with pathlib

### Path Objects

```python
from pathlib import Path

# Create path objects
path = Path('data.txt')
path = Path('/home/user/documents/file.txt')
path = Path.home() / 'documents' / 'file.txt'

# Path properties
print(path.name)        # file.txt
print(path.stem)        # file
print(path.suffix)      # .txt
print(path.parent)      # /home/user/documents
print(path.absolute())  # absolute path
```

### Reading and Writing with pathlib

```python
from pathlib import Path

path = Path('data.txt')

# Read text
content = path.read_text(encoding='utf-8')

# Read bytes
data = path.read_bytes()

# Write text
path.write_text('Hello, World!', encoding='utf-8')

# Write bytes
path.write_bytes(b'\x00\x01\x02')
```

### Checking File Properties

```python
from pathlib import Path

path = Path('data.txt')

print(path.exists())        # True/False
print(path.is_file())       # True/False
print(path.is_dir())        # True/False
print(path.stat().st_size)  # File size in bytes
print(path.stat().st_mtime) # Modification time
```

---

## 9. Directory Operations

### Creating Directories

```python
from pathlib import Path

# Create directory
path = Path('new_directory')
path.mkdir()

# Create with parents
path = Path('parent/child/grandchild')
path.mkdir(parents=True, exist_ok=True)
```

### Listing Directory Contents

```python
from pathlib import Path

path = Path('.')

# List all items
for item in path.iterdir():
    print(item)

# List only files
for file in path.glob('*.txt'):
    print(file)

# Recursive search
for file in path.rglob('*.py'):
    print(file)
```

### Walking Directory Tree

```python
from pathlib import Path

def walk_directory(path):
    for item in Path(path).rglob('*'):
        if item.is_file():
            print(f"File: {item}")
        elif item.is_dir():
            print(f"Dir:  {item}")

walk_directory('.')
```

---

## 10. File and Directory Operations with os

### Basic Operations

```python
import os

# Get current directory
print(os.getcwd())

# Change directory
os.chdir('/home/user')

# List directory
print(os.listdir('.'))

# Create directory
os.mkdir('new_dir')
os.makedirs('parent/child', exist_ok=True)

# Remove file
os.remove('file.txt')

# Remove directory
os.rmdir('empty_dir')

# Rename/move
os.rename('old.txt', 'new.txt')
```

### File Information

```python
import os

# Check existence
print(os.path.exists('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('directory'))

# Get file info
print(os.path.getsize('file.txt'))      # Size in bytes
print(os.path.getmtime('file.txt'))     # Modification time
print(os.path.getatime('file.txt'))     # Access time

# Path operations
print(os.path.join('dir', 'subdir', 'file.txt'))
print(os.path.split('/path/to/file.txt'))
print(os.path.splitext('file.txt'))     # ('file', '.txt')
print(os.path.basename('/path/to/file.txt'))  # file.txt
print(os.path.dirname('/path/to/file.txt'))   # /path/to
```

---

## 11. Working with CSV Files

### Reading CSV

```python
import csv

# Read with csv.reader
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row)

# Read with csv.DictReader
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['age'])
```

### Writing CSV

```python
import csv

# Write with csv.writer
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'NYC'])
    writer.writerow(['Bob', 25, 'LA'])

# Write with csv.DictWriter
with open('output.csv', 'w', newline='') as file:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30, 'city': 'NYC'})
    writer.writerow({'name': 'Bob', 'age': 25, 'city': 'LA'})
```

---

## 12. Working with JSON Files

### Reading JSON

```python
import json

# Read JSON file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Parse JSON string
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
```

### Writing JSON

```python
import json

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC',
    'hobbies': ['reading', 'hiking']
}

# Write JSON file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=2)

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
```

### Custom JSON Encoding

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {'timestamp': datetime.now()}
json_string = json.dumps(data, cls=DateTimeEncoder)
```

---

## 13. Temporary Files

### Using tempfile Module

```python
import tempfile

# Temporary file
with tempfile.TemporaryFile(mode='w+') as temp:
    temp.write('Hello, World!')
    temp.seek(0)
    print(temp.read())
# File is deleted automatically

# Named temporary file
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
    temp.write('Hello')
    temp_name = temp.name

# Temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Created temporary directory: {temp_dir}")
    # Use temp_dir
# Directory is deleted automatically
```

---

## 14. File Compression

### Working with ZIP Files

```python
import zipfile

# Create ZIP archive
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')
    zipf.write('folder/file3.txt')

# Extract ZIP archive
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted_files')

# List contents
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    print(zipf.namelist())
```

### Working with GZIP Files

```python
import gzip

# Write compressed file
with gzip.open('file.txt.gz', 'wt') as f:
    f.write('Hello, World!')

# Read compressed file
with gzip.open('file.txt.gz', 'rt') as f:
    content = f.read()
    print(content)
```

---

## 15. File I/O Best Practices

### 1. Always Use Context Managers

```python
# Good
with open('file.txt', 'r') as f:
    content = f.read()

# Bad
f = open('file.txt', 'r')
content = f.read()
f.close()  # May not execute if exception occurs
```

### 2. Read Large Files Line by Line

```python
# Good - memory efficient
with open('large_file.txt', 'r') as f:
    for line in f:
        process(line)

# Bad - loads entire file in memory
with open('large_file.txt', 'r') as f:
    lines = f.readlines()  # Loads everything
    for line in lines:
        process(line)
```

### 3. Specify Encoding Explicitly

```python
# Good
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# May cause issues on different systems
with open('file.txt', 'r') as f:
    content = f.read()
```

### 4. Handle Errors Gracefully

```python
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except IOError as e:
    print(f"I/O error: {e}")
```

### 5. Use pathlib for Modern Code

```python
from pathlib import Path

# Modern approach
path = Path('data.txt')
if path.exists():
    content = path.read_text()

# Old approach
import os
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()
```

---

## 16. Buffering and Performance

### Controlling Buffer Size

```python
# Default buffering
with open('file.txt', 'r') as f:
    content = f.read()

# Custom buffer size
with open('file.txt', 'r', buffering=8192) as f:
    content = f.read()

# No buffering (binary mode only)
with open('file.bin', 'rb', buffering=0) as f:
    data = f.read()

# Line buffering (text mode)
with open('file.txt', 'w', buffering=1) as f:
    f.write('Line 1\n')  # Flushed immediately
```

### Flushing Buffers

```python
with open('log.txt', 'w') as f:
    f.write('Important message')
    f.flush()  # Ensure data is written to disk
```

---
