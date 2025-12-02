# File Handling - Quiz

Test your knowledge of file I/O operations, formats, and best practices.

---

## Question 1: File Modes

What does the file mode `'r+'` do?

A) Read-only mode  
B) Read and write mode (file must exist)  
C) Write mode (creates new file)  
D) Append mode  

---

## Question 2: Context Manager

What is the advantage of using `with open()` for file operations?

A) It's faster than regular open()  
B) It automatically closes the file, even if an exception occurs  
C) It allows multiple files to be opened  
D) It prevents file corruption  

---

## Question 3: pathlib

Which is the correct way to join paths using pathlib?

A) `Path('/home') / 'user' / 'file.txt'`  
B) `Path('/home') + 'user' + 'file.txt'`  
C) `Path('/home').join('user', 'file.txt')`  
D) `Path.join('/home', 'user', 'file.txt')`  

---

## Question 4: CSV Reading

Which module is used for reading and writing CSV files in Python?

A) `csvfile`  
B) `pandas`  
C) `spreadsheet`  
D) `csv`  

---

## Question 5: JSON Serialization

What does `json.dumps()` do?

A) Loads JSON from a file  
B) Dumps JSON to a file  
C) Converts a Python object to a JSON string  
D) Validates JSON syntax  

---

## Question 6: Binary Files

Which mode should you use to read a binary file?

A) `'rb'`  
B) `'r'`  
C) `'binary'`  
D) `'b'`  

---

## Question 7: File Encoding

What is the default encoding for text files in Python 3?

A) ASCII  
B) Latin-1  
C) UTF-16  
D) UTF-8  

---

## Question 8: Temporary Files

Which module provides functionality for creating temporary files?

A) `temp`  
B) `tempfile`  
C) `tmpfile`  
D) `temporary`  

---

## Question 9: File Existence

Using pathlib, how do you check if a file exists?

A) `Path('file.txt').exists()`  
B) `Path.exists('file.txt')`  
C) `os.path.exists('file.txt')`  
D) `file.exists('file.txt')`  

---

## Question 10: ZIP Files

Which module is used to work with ZIP archives in Python?

A) `zip`  
B) `archive`  
C) `compress`  
D) `zipfile`  

---

## Question 11: io.open() vs open()

In Python 3, what is the relationship between `open()` and `io.open()`?

A) They are completely different functions  
B) `open()` is an alias to `io.open()`  
C) `io.open()` is deprecated  
D) `open()` is faster than `io.open()`  

---

## Question 12: StringIO

What is `io.StringIO` used for?

A) Reading strings from files  
B) Creating in-memory text streams  
C) Converting strings to bytes  
D) Compressing text data  

---

## Question 13: File Object Type

What type of object does `open('file.txt', 'r')` return in Python 3?

A) `io.FileIO`  
B) `io.BufferedReader`  
C) `io.TextIOWrapper`  
D) `io.StringIO`  

---

## Question 14: File Seeking

What does `file.seek(0, 2)` do?

A) Moves to the beginning of the file  
B) Moves 2 bytes forward  
C) Moves to the end of the file  
D) Moves to byte position 2  

---

## Question 15: Encoding Errors

Which error handler replaces unencodable characters with XML entities?

A) `'ignore'`  
B) `'replace'`  
C) `'xmlcharrefreplace'`  
D) `'backslashreplace'`  

---

## Question 16: BytesIO

What is the correct way to read data from a `BytesIO` object after writing to it?

A) `bytesio.read()`  
B) `bytesio.seek(0)` then `bytesio.read()`  
C) `bytesio.getvalue()`  
D) Both B and C are correct  

---

## Question 17: File Modes

Which file mode creates a new file and fails if the file already exists?

A) `'w'`  
B) `'x'`  
C) `'a'`  
D) `'w+'`  

---

## Question 18: CSV DictReader

What does `csv.DictReader` return for each row?

A) A list  
B) A tuple  
C) A dictionary  
D) A string  

---

## Question 19: JSON Load vs Loads

What's the difference between `json.load()` and `json.loads()`?

A) `load()` reads from a file, `loads()` reads from a string  
B) `load()` is faster than `loads()`  
C) `loads()` is deprecated  
D) They are identical  

---

## Question 20: File Buffering

What does `buffering=0` mean when opening a file?

A) Use default buffering  
B) No buffering (only for binary mode)  
C) Maximum buffering  
D) Line buffering  

---

## Question 21: TextIOWrapper

What does `io.TextIOWrapper` do?

A) Compresses text files  
B) Wraps a binary stream to provide text interface  
C) Creates temporary text files  
D) Validates text encoding  

---

## Question 22: Path Operations

Which pathlib method recursively finds all files matching a pattern?

A) `glob()`  
B) `rglob()`  
C) `find()`  
D) `search()`  

---

## Question 23: File Properties

How do you get a file's size using pathlib?

A) `path.size()`  
B) `path.filesize()`  
C) `path.stat().st_size`  
D) `len(path)`  

---

## Question 24: Reading Lines

Which is the most memory-efficient way to read a large file line by line?

A) `file.readlines()`  
B) `file.read().split('\n')`  
C) `for line in file:`  
D) `list(file)`  

---

## Question 25: Byte Operations

What does `b'Hello'.decode('utf-8')` return?

A) `b'Hello'`  
B) `'Hello'`  
C) `[72, 101, 108, 108, 111]`  
D) An error  

---

## Question 26: File Context

Which magic methods are needed to create a file context manager?

A) `__init__` and `__del__`  
B) `__enter__` and `__exit__`  
C) `__open__` and `__close__`  
D) `__start__` and `__stop__`  

---

## Question 27: GZIP Files

Which mode should you use to read a compressed text file with gzip?

A) `'r'`  
B) `'rb'`  
C) `'rt'`  
D) `'text'`  

---

## Question 28: Path Properties

Which pathlib property gives you the file extension?

A) `path.extension`  
B) `path.ext`  
C) `path.suffix`  
D) `path.type`  

---

## Question 29: File Object Methods

Which method checks if a file object is readable?

A) `file.isreadable()`  
B) `file.can_read()`  
C) `file.readable()`  
D) `file.read_mode()`  

---

## Question 30: Writing CSV

What parameter should you set when opening a CSV file for writing to avoid blank lines on Windows?

A) `encoding='utf-8'`  
B) `newline=''`  
C) `mode='wb'`  
D) `buffering=0`  

---

## Question 31: Socket as File Object

What method converts a socket to a file-like object?

A) `socket.tofile()`  
B) `socket.makefile()`  
C) `socket.fileno()`  
D) `socket.convert()`  

---

## Question 32: sendfile() Benefit

What is the main advantage of `os.sendfile()` over traditional file reading and sending?

A) It compresses data automatically  
B) It uses zero-copy technology (no user-space copy)  
C) It encrypts data in transit  
D) It works on all operating systems  

---

## Question 33: Buffer Flushing

What does `file.flush()` do?

A) Closes the file  
B) Clears the file contents  
C) Writes buffered data to disk  
D) Reads data into buffer  

---

## Question 34: Line Buffering

When does a line-buffered file flush automatically?

A) After every write  
B) When a newline character is written  
C) When the buffer is full  
D) Every second  

---

## Question 35: Unbuffered Binary I/O

What buffering value should you use for unbuffered binary I/O?

A) `buffering=-1`  
B) `buffering=0`  
C) `buffering=1`  
D) `buffering=None`  

---

## Answer Key

1. B - Read and write mode (file must exist)
2. B - It automatically closes the file, even if an exception occurs
3. A - `Path('/home') / 'user' / 'file.txt'`
4. D - `csv`
5. C - Converts a Python object to a JSON string
6. A - `'rb'`
7. D - UTF-8
8. B - `tempfile`
9. A - `Path('file.txt').exists()`
10. D - `zipfile`
11. B - `open()` is an alias to `io.open()`
12. B - Creating in-memory text streams
13. C - `io.TextIOWrapper`
14. C - Moves to the end of the file
15. C - `'xmlcharrefreplace'`
16. D - Both B and C are correct
17. B - `'x'`
18. C - A dictionary
19. A - `load()` reads from a file, `loads()` reads from a string
20. B - No buffering (only for binary mode)
21. B - Wraps a binary stream to provide text interface
22. B - `rglob()`
23. C - `path.stat().st_size`
24. C - `for line in file:`
25. B - `'Hello'`
26. B - `__enter__` and `__exit__`
27. C - `'rt'`
28. C - `path.suffix`
29. C - `file.readable()`
30. B - `newline=''`
31. B - `socket.makefile()`
32. B - It uses zero-copy technology (no user-space copy)
33. C - Writes buffered data to disk
34. B - When a newline character is written
35. B - `buffering=0`

---

## Scoring Guide

- **32-35 correct**: Excellent! You're a file handling expert.
- **28-31 correct**: Great job! You have strong file I/O skills.
- **23-27 correct**: Good understanding. Keep practicing.
- **18-22 correct**: Decent foundation. Review advanced topics.
- **13-17 correct**: Basic knowledge. More practice needed.
- **Below 13**: Review file handling concepts thoroughly and try practical exercises.
