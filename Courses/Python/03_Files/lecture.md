# File Handling in Python
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

### Encoding and Decoding Binary Data

```python
# Read binary data and decode to text
with open('data.txt', 'rb') as file:
    binary_data = file.read()
    text = binary_data.decode('utf-8')
    print(f"Binary: {binary_data[:20]}")
    print(f"Text: {text[:20]}")

# Encode text to binary and write
text = "Привет, мир! Hello, World!"
binary_data = text.encode('utf-8')

with open('encoded.bin', 'wb') as file:
    file.write(binary_data)

# Read binary, decode with different encodings
with open('data.txt', 'rb') as file:
    data = file.read()
    
    # Try UTF-8
    try:
        text_utf8 = data.decode('utf-8')
        print(f"UTF-8: {text_utf8}")
    except UnicodeDecodeError:
        print("Not valid UTF-8")
    
    # Try Latin-1 (always succeeds)
    text_latin1 = data.decode('latin-1')
    print(f"Latin-1: {text_latin1}")
```

### Encoding with Error Handling

```python
# Read binary with error handling
with open('data.txt', 'rb') as file:
    binary_data = file.read()
    
    # Ignore errors
    text = binary_data.decode('utf-8', errors='ignore')
    
    # Replace errors with �
    text = binary_data.decode('utf-8', errors='replace')
    
    # Replace with escape sequences
    text = binary_data.decode('utf-8', errors='backslashreplace')
    print(text)

# Encode with error handling
text = "Hello 🌍 World"

# Strict (raises error for incompatible chars)
try:
    binary = text.encode('ascii')
except UnicodeEncodeError as e:
    print(f"Cannot encode: {e}")

# Ignore incompatible characters
binary = text.encode('ascii', errors='ignore')
print(binary)  # b'Hello  World'

# Replace with ?
binary = text.encode('ascii', errors='replace')
print(binary)  # b'Hello ? World'

# Use XML entities
binary = text.encode('ascii', errors='xmlcharrefreplace')
print(binary)  # b'Hello &#127757; World'
```

### Converting Between Encodings

```python
# Read file in one encoding, write in another
with open('input_cp1251.txt', 'rb') as file:
    data = file.read()
    text = data.decode('cp1251')  # Windows Cyrillic

# Write as UTF-8
with open('output_utf8.txt', 'wb') as file:
    utf8_data = text.encode('utf-8')
    file.write(utf8_data)

# One-liner conversion
with open('old.txt', 'rb') as f:
    content = f.read().decode('latin-1').encode('utf-8')
    with open('new.txt', 'wb') as out:
        out.write(content)
```

### Working with Binary Strings

```python
# Creating bytes objects
b1 = b'Hello'                          # Bytes literal
b2 = bytes([72, 101, 108, 108, 111])   # From list of integers
b3 = 'Hello'.encode('utf-8')           # From string

print(b1 == b2 == b3)  # True

# Bytes operations
data = b'Hello, World!'
print(data[0])           # 72 (ASCII code for 'H')
print(data[0:5])         # b'Hello'
print(data.split(b','))  # [b'Hello', b' World!']

# Converting bytes to string
binary = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
text = binary.decode('utf-8')
print(text)  # Привет

# Hex representation
data = b'\x00\x01\x02\xff'
print(data.hex())           # 000102ff
print(bytes.fromhex('48656c6c6f'))  # b'Hello'
```

---

## 7. The io Module and File Objects

### Understanding open() and io.open()

```python
import io

# open() is actually io.open() in Python 3
# These are equivalent:
file1 = open('data.txt', 'r')
file2 = io.open('data.txt', 'r')

# open is an alias to io.open
print(open is io.open)  # True in Python 3
```

### io Module Classes Hierarchy

```python
import io

# io.IOBase - Base class for all I/O classes
# ├── io.RawIOBase - Raw binary I/O
# │   └── io.FileIO - Low-level file I/O
# ├── io.BufferedIOBase - Buffered binary I/O
# │   ├── io.BufferedReader - Buffered reading
# │   ├── io.BufferedWriter - Buffered writing
# │   └── io.BufferedRandom - Buffered random access
# └── io.TextIOBase - Text I/O
#     └── io.TextIOWrapper - Text wrapper around binary streams

# What open() actually returns:
text_file = open('data.txt', 'r')
print(type(text_file))  # <class '_io.TextIOWrapper'>

binary_file = open('data.bin', 'rb')
print(type(binary_file))  # <class '_io.BufferedReader'>

write_file = open('out.txt', 'w')
print(type(write_file))  # <class '_io.TextIOWrapper'>
```

### Working with StringIO (In-Memory Text Streams)

```python
import io

# Create in-memory text stream
output = io.StringIO()
output.write('First line\n')
output.write('Second line\n')

# Get the entire contents
contents = output.getvalue()
print(contents)

# Seek and read
output.seek(0)
print(output.read())

# Close when done
output.close()

# Using with statement
with io.StringIO() as f:
    f.write('Hello, World!')
    f.seek(0)
    print(f.read())

# Initialize with existing string
input_stream = io.StringIO('Line 1\nLine 2\nLine 3')
for line in input_stream:
    print(line.strip())
```

### Working with BytesIO (In-Memory Binary Streams)

```python
import io

# Create in-memory binary stream
output = io.BytesIO()
output.write(b'Binary data\n')
output.write(b'\x00\x01\x02\x03')

# Get contents
data = output.getvalue()
print(data)
print(f"Size: {len(data)} bytes")

# Seek and read
output.seek(0)
chunk = output.read(6)
print(chunk)  # b'Binary'

output.close()

# Initialize with existing bytes
binary_input = io.BytesIO(b'\x89PNG\r\n\x1a\n')
header = binary_input.read(4)
print(header)  # b'\x89PNG'
```

### Practical Use Cases for StringIO and BytesIO

```python
import io
import csv

# CSV writing to string instead of file
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(['Name', 'Age', 'City'])
writer.writerow(['Alice', 30, 'NYC'])
csv_string = output.getvalue()
print(csv_string)

# Testing file operations without actual files
def process_file(file_obj):
    """Function that works with file-like objects"""
    for line in file_obj:
        print(line.upper().strip())

# Test with StringIO instead of real file
test_data = io.StringIO('line 1\nline 2\nline 3')
process_file(test_data)

# Converting between formats
import json
data = {'name': 'Alice', 'age': 30}
json_str = json.dumps(data)
json_file = io.StringIO(json_str)
loaded_data = json.load(json_file)
print(loaded_data)
```

### TextIOWrapper - Wrapping Binary Streams

```python
import io

# Open binary file and wrap with text interface
binary_file = open('data.txt', 'rb')
text_wrapper = io.TextIOWrapper(binary_file, encoding='utf-8')

for line in text_wrapper:
    print(line.strip())

text_wrapper.close()

# Custom text wrapper with specific encoding
with open('legacy.txt', 'rb') as binary_stream:
    text_stream = io.TextIOWrapper(
        binary_stream,
        encoding='cp1251',
        errors='replace',
        newline='\r\n'
    )
    content = text_stream.read()
    print(content)
```

### BufferedReader and BufferedWriter

```python
import io

# Low-level file I/O (unbuffered)
raw = io.FileIO('data.bin', 'r')
print(type(raw))  # <class '_io.FileIO'>

# Wrap with buffered reader
buffered = io.BufferedReader(raw, buffer_size=8192)
data = buffered.read(100)
buffered.close()

# Buffered writer
with io.FileIO('output.bin', 'w') as raw_file:
    buffered_writer = io.BufferedWriter(raw_file)
    buffered_writer.write(b'Hello, World!')
    buffered_writer.flush()  # Ensure data is written
    buffered_writer.close()
```

### File-like Objects and Duck Typing

```python
import io

class UpperCaseFile:
    """Custom file-like object that converts to uppercase"""
    def __init__(self, filename):
        self.file = open(filename, 'r')
    
    def read(self, size=-1):
        return self.file.read(size).upper()
    
    def readline(self):
        return self.file.readline().upper()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line.upper()
    
    def close(self):
        self.file.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

# Use custom file object
with UpperCaseFile('data.txt') as f:
    for line in f:
        print(line.strip())
```

### Checking File Object Properties

```python
import io

# Check what type of file object you have
def inspect_file_object(f):
    print(f"Type: {type(f)}")
    print(f"Readable: {f.readable()}")
    print(f"Writable: {f.writable()}")
    print(f"Seekable: {f.seekable()}")
    print(f"Closed: {f.closed}")
    if hasattr(f, 'mode'):
        print(f"Mode: {f.mode}")
    if hasattr(f, 'name'):
        print(f"Name: {f.name}")
    if hasattr(f, 'encoding'):
        print(f"Encoding: {f.encoding}")

# Inspect different file types
with open('data.txt', 'r') as f:
    inspect_file_object(f)

with io.StringIO('test') as f:
    inspect_file_object(f)

with open('data.bin', 'rb') as f:
    inspect_file_object(f)
```

### Advanced: Creating Custom Streams

```python
import io

class CountingIO(io.StringIO):
    """StringIO that counts bytes written"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bytes_written = 0
    
    def write(self, s):
        result = super().write(s)
        self.bytes_written += len(s)
        return result

# Use custom stream
stream = CountingIO()
stream.write('Hello')
stream.write(' ')
stream.write('World')
print(f"Total characters written: {stream.bytes_written}")
print(f"Content: {stream.getvalue()}")
```

### Sockets as File-like Objects

```python
import socket
import io

# Create a socket - it's a file-like object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Check file-like properties
print(f"Has fileno: {hasattr(sock, 'fileno')}")  # True
print(f"File descriptor: {sock.fileno()}")

# Socket can be used with makefile() to get a file object
# Example: HTTP client
sock.connect(('example.com', 80))

# Wrap socket in file object for easier reading/writing
file_obj = sock.makefile('rwb')
print(type(file_obj))  # <class '_io.BufferedRWPair'>

# Write HTTP request
file_obj.write(b'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n')
file_obj.flush()

# Read response line by line
for i, line in enumerate(file_obj):
    print(line.decode('utf-8', errors='ignore').strip())
    if i > 10:  # Print first few lines
        break

file_obj.close()
sock.close()
```

### Socket File Objects - Text Mode

```python
import socket

# Create socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))

# Text mode wrapper
with sock.makefile('r', encoding='utf-8', newline='\r\n') as f:
    # Write request (need to access socket directly for writing)
    sock.sendall(b'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n')
    
    # Read response as text
    status_line = f.readline()
    print(f"Status: {status_line.strip()}")
    
    # Read headers
    headers = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        headers.append(line)
    
    print(f"Found {len(headers)} headers")

sock.close()
```

### Socket with TextIOWrapper

```python
import socket
import io

# Create socket and wrap with text interface
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('httpbin.org', 80))

# Wrap socket's binary stream with text wrapper
sock_file = sock.makefile('rwb')
text_wrapper = io.TextIOWrapper(
    sock_file,
    encoding='utf-8',
    line_buffering=True
)

# Send HTTP request
text_wrapper.write('GET /get HTTP/1.1\r\n')
text_wrapper.write('Host: httpbin.org\r\n')
text_wrapper.write('Connection: close\r\n')
text_wrapper.write('\r\n')
text_wrapper.flush()

# Read response
response = text_wrapper.read()
print(response[:500])  # Print first 500 characters

text_wrapper.close()
sock.close()
```

### Using Sockets with File Operations

```python
import socket
import os

def send_file_over_socket(filename, host, port):
    """Send a file over a socket connection"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        
        with open(filename, 'rb') as f:
            # Read and send in chunks
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                sock.sendall(chunk)
    
    print(f"Sent {filename} to {host}:{port}")

def receive_file_from_socket(output_filename, host, port):
    """Receive a file from a socket connection"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(1)
        conn, addr = sock.accept()
        
        with conn:
            with open(output_filename, 'wb') as f:
                while True:
                    data = conn.recv(8192)
                    if not data:
                        break
                    f.write(data)
    
    print(f"Received file saved as {output_filename}")
```

---

## 8. Context Managers for Files

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

## 9. File System Operations with pathlib

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

## 10. Directory Operations

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

## 11. File and Directory Operations with os

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

## 12. Working with CSV Files

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

## 13. Working with JSON Files

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

## 14. Temporary Files

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

## 15. File Compression

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

## 16. File I/O Best Practices

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

## 17. Zero-Copy File Operations with sendfile()

### Understanding sendfile()

`sendfile()` is a system call that copies data between file descriptors without transferring it through user space - a technique called "zero-copy". This is much more efficient for sending files over networks.

```python
import os
import socket

# Traditional approach - data copied to user space and back
def send_file_traditional(filename, sock):
    """Traditional file sending - multiple copies"""
    with open(filename, 'rb') as f:
        # Data flow: Disk -> Kernel -> User Space -> Kernel -> Network
        while True:
            data = f.read(8192)  # Copy from kernel to user space
            if not data:
                break
            sock.sendall(data)    # Copy from user space to kernel

# Zero-copy approach - data stays in kernel space
def send_file_zerocopy(filename, sock):
    """Zero-copy file sending using sendfile()"""
    with open(filename, 'rb') as f:
        # Data flow: Disk -> Kernel -> Network (no user space copy!)
        offset = 0
        file_size = os.path.getsize(filename)
        
        while offset < file_size:
            # sendfile(out_fd, in_fd, offset, count)
            sent = os.sendfile(sock.fileno(), f.fileno(), offset, file_size - offset)
            offset += sent
```

### Practical Example: HTTP File Server with sendfile()

```python
import os
import socket

def serve_file_with_sendfile(filename, client_socket):
    """Serve a file using zero-copy sendfile()"""
    try:
        # Get file size
        file_size = os.path.getsize(filename)
        
        # Send HTTP headers
        headers = (
            f"HTTP/1.1 200 OK\r\n"
            f"Content-Length: {file_size}\r\n"
            f"Content-Type: application/octet-stream\r\n"
            f"\r\n"
        )
        client_socket.sendall(headers.encode())
        
        # Send file using sendfile (zero-copy)
        with open(filename, 'rb') as f:
            offset = 0
            while offset < file_size:
                sent = os.sendfile(
                    client_socket.fileno(),
                    f.fileno(),
                    offset,
                    file_size - offset
                )
                if sent == 0:
                    break
                offset += sent
        
        print(f"Sent {offset} bytes using zero-copy")
        
    except FileNotFoundError:
        response = b"HTTP/1.1 404 Not Found\r\n\r\n"
        client_socket.sendall(response)
    except OSError as e:
        print(f"Error: {e}")
```

### sendfile() vs Traditional Copy - Performance Comparison

```python
import os
import socket
import time

def benchmark_file_transfer(filename, host, port):
    """Compare traditional vs sendfile() performance"""
    file_size = os.path.getsize(filename)
    
    # Traditional method
    start = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(65536)
                if not chunk:
                    break
                sock.sendall(chunk)
    traditional_time = time.time() - start
    
    # sendfile() method
    start = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        with open(filename, 'rb') as f:
            os.sendfile(sock.fileno(), f.fileno(), 0, file_size)
    sendfile_time = time.time() - start
    
    print(f"File size: {file_size / (1024*1024):.2f} MB")
    print(f"Traditional: {traditional_time:.3f}s")
    print(f"sendfile(): {sendfile_time:.3f}s")
    print(f"Speedup: {traditional_time/sendfile_time:.2f}x")
```

### Platform Considerations

```python
import os
import sys

def send_file_cross_platform(filename, sock):
    """Cross-platform file sending"""
    if hasattr(os, 'sendfile'):
        # Linux, BSD, macOS (Python 3.3+)
        with open(filename, 'rb') as f:
            offset = 0
            file_size = os.path.getsize(filename)
            while offset < file_size:
                sent = os.sendfile(sock.fileno(), f.fileno(), offset, file_size - offset)
                offset += sent
    else:
        # Windows - fallback to traditional method
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(65536)
                if not chunk:
                    break
                sock.sendall(chunk)
```

---

## 18. Understanding Buffers and Buffering

### What is a Buffer?

A **buffer** is a temporary storage area in memory used to hold data while it's being transferred between two places. Buffering improves performance by reducing the number of system calls.

```python
# Without buffer (hypothetical - every write is a system call)
# write('H') -> system call
# write('e') -> system call
# write('l') -> system call
# write('l') -> system call
# write('o') -> system call
# Total: 5 system calls!

# With buffer (actual behavior)
# write('H') -> buffer
# write('e') -> buffer
# write('l') -> buffer
# write('l') -> buffer
# write('o') -> buffer
# flush()    -> system call (writes all at once)
# Total: 1 system call!
```

### Buffer Types and Modes

```python
import io

# buffering=-1 (default): Use default buffer size
with open('file.txt', 'w', buffering=-1) as f:
    # Text files: line buffered if interactive, else block buffered
    # Binary files: block buffered (usually 8192 bytes)
    f.write('data')

# buffering=0: No buffering (binary mode only)
with open('file.bin', 'wb', buffering=0) as f:
    # Each write() immediately goes to disk
    f.write(b'data')  # Immediately written

# buffering=1: Line buffering (text mode only)
with open('file.txt', 'w', buffering=1) as f:
    f.write('Line 1\n')  # Flushed immediately (contains newline)
    f.write('Line 2')    # Stays in buffer (no newline yet)

# buffering>1: Custom buffer size in bytes
with open('file.txt', 'w', buffering=4096) as f:
    # Buffer holds up to 4096 bytes before flushing
    f.write('data')
```

### How Buffering Works Internally

```python
import io
import time

class DebugBuffer(io.BufferedWriter):
    """BufferedWriter with debug output"""
    def write(self, b):
        print(f"Writing {len(b)} bytes to buffer")
        result = super().write(b)
        print(f"Buffer size: {len(self._write_buf)} bytes")
        return result
    
    def flush(self):
        print(f"Flushing {len(self._write_buf)} bytes to disk")
        super().flush()

# Demonstrate buffering behavior
raw = io.FileIO('debug.bin', 'w')
buffered = DebugBuffer(raw, buffer_size=100)

buffered.write(b'a' * 50)   # Goes to buffer
buffered.write(b'b' * 40)   # Still in buffer (total: 90)
buffered.write(b'c' * 20)   # Triggers flush! (110 > 100)

buffered.close()
```

### Buffer Performance Impact

```python
import time
import os

def write_without_buffer(filename, data, chunk_size=1):
    """Write data without buffering - very slow!"""
    start = time.time()
    with open(filename, 'wb', buffering=0) as f:
        for i in range(0, len(data), chunk_size):
            f.write(data[i:i+chunk_size])
    return time.time() - start

def write_with_buffer(filename, data, buffer_size=8192):
    """Write data with buffering - much faster!"""
    start = time.time()
    with open(filename, 'wb', buffering=buffer_size) as f:
        f.write(data)
    return time.time() - start

# Benchmark
data = b'x' * 1000000  # 1 MB of data

time_no_buffer = write_without_buffer('no_buffer.bin', data, 1)
time_buffered = write_with_buffer('buffered.bin', data)

print(f"Without buffer (1 byte at a time): {time_no_buffer:.3f}s")
print(f"With buffer: {time_buffered:.3f}s")
print(f"Speedup: {time_no_buffer/time_buffered:.0f}x")

# Cleanup
os.remove('no_buffer.bin')
os.remove('buffered.bin')
```

### Read Buffering

```python
import io

# Reading also uses buffers
with open('large_file.txt', 'r', buffering=4096) as f:
    # First read() loads 4096 bytes into buffer
    char1 = f.read(1)  # Reads from buffer (fast!)
    char2 = f.read(1)  # Reads from buffer (fast!)
    
    # After buffer is exhausted, next read loads another 4096 bytes
    chunk = f.read(5000)  # Loads new data from disk

# Demonstrate with binary buffering
class InstrumentedFile:
    """File wrapper that counts actual disk reads"""
    def __init__(self, filename, buffer_size):
        self.raw_file = io.FileIO(filename, 'r')
        self.buffered = io.BufferedReader(self.raw_file, buffer_size)
        self.disk_reads = 0
    
    def read(self, size):
        # Monitor raw file reads (actual disk I/O)
        initial_pos = self.raw_file.tell()
        data = self.buffered.read(size)
        if self.raw_file.tell() != initial_pos:
            self.disk_reads += 1
        return data
    
    def close(self):
        self.buffered.close()

# Test buffering effect
file = InstrumentedFile('test.txt', buffer_size=4096)
for _ in range(100):
    file.read(10)  # Read 10 bytes, 100 times
print(f"Disk reads: {file.disk_reads}")  # Much less than 100!
file.close()
```

### Explicit Buffer Control

```python
import sys

# Flush buffer explicitly
with open('important.log', 'w') as f:
    f.write('Critical data\n')
    f.flush()  # Ensure written to disk immediately
    # Continue with non-critical operations...

# Flush all open files
sys.stdout.flush()
sys.stderr.flush()

# Force OS to write to physical disk (fsync)
import os
with open('critical.dat', 'wb') as f:
    f.write(b'important data')
    f.flush()            # Flush Python buffer to OS
    os.fsync(f.fileno()) # Force OS to write to physical disk
```

### Buffer Gotchas and Best Practices

```python
# GOTCHA 1: Line buffering only works on newlines
with open('file.txt', 'w', buffering=1) as f:
    f.write('No newline')  # Stays in buffer!
    f.write(' more text')  # Still in buffer!
    f.write('\n')          # NOW it flushes!

# GOTCHA 2: Binary mode doesn't support line buffering
try:
    f = open('file.bin', 'wb', buffering=1)
except ValueError as e:
    print(f"Error: {e}")  # line buffering not supported for binary

# GOTCHA 3: Reading and writing with buffering
with open('file.txt', 'r+', buffering=8192) as f:
    f.write('Hello')
    # Buffer not flushed yet!
    f.seek(0)
    content = f.read()  # Might not see what we just wrote!
    
    # Solution: flush before reading
    f.seek(0)
    f.write('Hello')
    f.flush()  # Flush write buffer
    f.seek(0)
    content = f.read()  # Now we see the data

# BEST PRACTICE: Use appropriate buffer sizes
# Small files: default buffering is fine
# Large files, sequential access: larger buffer (64KB - 1MB)
# Random access: smaller buffer or no buffering

# Good for large file processing
with open('huge_file.dat', 'rb', buffering=1024*1024) as f:
    data = f.read()

# Good for database/log writing
with open('database.log', 'a', buffering=1) as f:
    f.write('Transaction committed\n')  # Immediate flush
```

### Understanding Buffer Layers

```python
"""
Complete I/O stack with buffers:

Application
    ↓
Python Buffer (io.BufferedWriter/Reader)
    ↓ flush()
OS Kernel Buffer (page cache)
    ↓ fsync() / sync()
Disk Controller Buffer
    ↓
Physical Disk
"""

import os
import io

def demonstrate_buffer_layers(filename):
    """Show all buffer layers"""
    with open(filename, 'wb', buffering=8192) as f:
        # Layer 1: Python buffer (8192 bytes)
        f.write(b'x' * 100)
        print("Data in Python buffer")
        
        # Layer 2: OS kernel buffer
        f.flush()
        print("Data flushed to OS kernel buffer")
        
        # Layer 3: Force to physical disk
        os.fsync(f.fileno())
        print("Data synchronized to physical disk")
```

---
