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

## Answer Key

1. B - Read and write mode (file must exist)
2. B - It automatically closes the file, even if an exception occurs
3. A - `Path('/home') / 'user' / 'file.txt'`
4. D - `csv`
5. C - Converts a Python object to a JSON string
6. A - `'rb'`
7. D - UTF-8
8. B - `tempfile`
9. C - `Path('file.txt').exists()`
10. D - `zipfile`

---

## Scoring Guide

- **9-10 correct**: Excellent! You're a file handling pro.
- **7-8 correct**: Great job! You understand file operations well.
- **5-6 correct**: Good start. Practice with different file formats.
- **Below 5**: Review file handling concepts and try practical exercises.
