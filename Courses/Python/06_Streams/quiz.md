# Streams and Unix I/O - Quiz

Test your knowledge of Python streams, standard I/O, and Unix-style programming.

---

## Question 1: Standard Streams

What are the three standard streams in Unix?

A) input, output, error  
B) stdin, stdout, stderr  
C) read, write, log  
D) in, out, err  

---

## Question 2: Reading from stdin

Which method of reading from stdin is most efficient for large files?

A) `data = sys.stdin.read()`  
B) `lines = sys.stdin.readlines()`  
C) `for line in sys.stdin:`  
D) `while True: line = sys.stdin.readline()`  

---

## Question 3: Error Output

Where should error messages be written in a Unix utility?

A) To stdout  
B) To stderr  
C) To a file error.log  
D) To stdout with "ERROR:" prefix  

---

## Question 4: Exit Codes

What exit code should be used on successful program termination?

A) 0  
B) 1  
C) 200  
D) -1  

---

## Question 5: BrokenPipeError

What is BrokenPipeError and when does it occur?

A) Error reading a corrupted file  
B) Exception when writing to a closed pipe  
C) Network error on connection drop  
D) Error using wrong delimiter  

---

## Question 6: argparse Actions

What does `action='store_true'` do in argparse?

```python
parser.add_argument('-v', '--verbose', action='store_true')
```

A) Stores value True in a variable  
B) Sets flag to True if option is specified, False otherwise  
C) Requires specifying true or false value  
D) Prints True to console  

---

## Question 7: Universal File Input

How to make a utility work with both files and stdin?

A) Always read from sys.stdin  
B) Always require filename  
C) Use fileinput or check for arguments  
D) Create two different programs  

---

## Question 8: Buffering

Why might program output not appear immediately?

```python
for i in range(10):
    print(f"Step {i}")
    time.sleep(1)
```

A) Python runs slowly  
B) Output is buffered  
C) print() works asynchronously  
D) Bug in code  

---

## Question 9: nargs Parameter

What does `nargs='*'` mean in argparse?

```python
parser.add_argument('files', nargs='*')
```

A) Exactly one value  
B) At least one value  
C) Zero or more values  
D) Any number but not zero  

---

## Question 10: Pipeline Mechanics

What happens in this pipeline?

```bash
cat file.txt | python script.py | grep ERROR | head -5
```

A) script.py receives file.txt as argument  
B) script.py reads content through stdin  
C) Error occurs  
D) script.py receives nothing  

---

## Question 11: Program Structure

Which structure is considered correct for a CLI utility?

```python
# Variant A
print("Hello")

# Variant B
def main():
    print("Hello")
main()

# Variant C
def main():
    print("Hello")
    
if __name__ == "__main__":
    main()
```

A) Variant A  
B) Variant B  
C) Variant C  
D) All variants are the same  

---

## Question 12: Binary Data

How to correctly read binary data from stdin?

A) `sys.stdin.read()`  
B) `sys.stdin.buffer.read()`  
C) `sys.stdin.readb()`  
D) `open('/dev/stdin', 'rb').read()`  

---

## Question 13: CSV Processing

How to correctly read CSV from stdin?

```python
import sys
import csv

# Variant A
reader = csv.reader(sys.stdin)

# Variant B
data = sys.stdin.read()
reader = csv.reader(data.split('\n'))

# Variant C
with open(sys.stdin) as f:
    reader = csv.reader(f)
```

A) Variant A  
B) Variant B  
C) Variant C  
D) All are incorrect  

---

## Question 14: Signal Handling

What is SIGINT and when is it sent?

A) System shutdown signal  
B) Interrupt signal (Ctrl+C)  
C) Timeout signal  
D) Network error signal  

---

## Question 15: Unix Philosophy

Which principle is NOT part of Unix philosophy?

A) Do one thing well  
B) Programs should work together  
C) Create GUI for every program  
D) Use text streams as universal interface  

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | stdin, stdout, stderr |
| 2 | C | `for line in sys.stdin:` |
| 3 | B | To stderr |
| 4 | A | 0 |
| 5 | B | Exception when writing to a closed pipe |
| 6 | B | Sets flag to True if option is specified, False otherwise |
| 7 | C | Use fileinput or check for arguments |
| 8 | B | Output is buffered |
| 9 | C | Zero or more values |
| 10 | B | script.py reads content through stdin |
| 11 | C | Variant C |
| 12 | B | `sys.stdin.buffer.read()` |
| 13 | A | Variant A |
| 14 | B | Interrupt signal (Ctrl+C) |
| 15 | C | Create GUI for every program |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **13-15 correct (87-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **10-12 correct (67-80%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **7-9 correct (47-60%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 7 correct (<47%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
