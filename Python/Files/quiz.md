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

A) `Path('/home') + 'user' + 'file.txt'`  
B) `Path('/home').join('user', 'file.txt')`  
C) `Path('/home') / 'user' / 'file.txt'`  
D) `Path.join('/home', 'user', 'file.txt')`  

---

## Question 4: CSV Reading

Which module is used for reading and writing CSV files in Python?

A) `csvfile`  
B) `csv`  
C) `pandas`  
D) `spreadsheet`  

---

## Question 5: JSON Serialization

What does `json.dumps()` do?

A) Loads JSON from a file  
B) Converts a Python object to a JSON string  
C) Dumps JSON to a file  
D) Validates JSON syntax  

---

## Question 6: Binary Files

Which mode should you use to read a binary file?

A) `'r'`  
B) `'rb'`  
C) `'binary'`  
D) `'b'`  

---

## Question 7: File Encoding

What is the default encoding for text files in Python 3?

A) ASCII  
B) UTF-8  
C) Latin-1  
D) UTF-16  

---

## Question 8: Temporary Files

Which module provides functionality for creating temporary files?

A) `temp`  
B) `tmpfile`  
C) `tempfile`  
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
B) `zipfile`  
C) `archive`  
D) `compress`  

---

## Answer Key

1. B - Read and write mode (file must exist)
2. B - It automatically closes the file, even if an exception occurs
3. C - `Path('/home') / 'user' / 'file.txt'`
4. B - `csv`
5. B - Converts a Python object to a JSON string
6. B - `'rb'`
7. B - UTF-8
8. C - `tempfile`
9. A - `Path('file.txt').exists()`
10. B - `zipfile`

---

## Scoring Guide

- **9-10 correct**: Excellent! You're a file handling pro.
- **7-8 correct**: Great job! You understand file operations well.
- **5-6 correct**: Good start. Practice with different file formats.
- **Below 5**: Review file handling concepts and try practical exercises.
