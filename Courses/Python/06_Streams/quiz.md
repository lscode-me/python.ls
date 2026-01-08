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

## Answer Key

1. **B** - stdin, stdout, stderr
   - These are the three standard Unix streams accessible in Python via `sys.stdin`, `sys.stdout`, `sys.stderr`

2. **C** - `for line in sys.stdin:`
   - Most efficient because it doesn't load entire file into memory, uses buffering, processes lines as read, and works with infinite streams

3. **B** - To stderr
   - Errors and diagnostic messages should go to stderr because it separates normal output from errors, can be redirected separately, follows Unix conventions, and keeps pipelines working

4. **A** - 0
   - Unix exit code 0 means success. Other codes: 1 = general error, 2 = incorrect usage, 130 = interrupted (Ctrl+C)

5. **B** - Exception when writing to a closed pipe
   - Occurs when a program tries to write to a pipe and the program on the other end has already terminated (e.g., `./script.py | head -10`)

6. **B** - Sets flag to True if option is specified, False otherwise
   - Creates a boolean flag: if `-v` is specified, `args.verbose == True`, otherwise `False`. Doesn't require a value after the flag

7. **C** - Use fileinput or check for arguments
   - Pattern: use `nargs='*'` for files argument, read from stdin if no files specified, otherwise process each file

8. **B** - Output is buffered
   - Python buffers output for efficiency. Output appears when buffer fills, `\n` encountered (line buffering), program terminates, or `flush()` called

9. **C** - Zero or more values
   - `nargs='*'` means the argument can have 0 or more values and creates a list. Compare: `nargs='?'` (0-1), `nargs='+'` (1+), `nargs=N` (exactly N)

10. **B** - script.py reads content through stdin
    - In pipeline: `cat` writes to stdout → becomes stdin for `script.py` → script.py output goes to `grep` → grep to `head`. script.py doesn't know about file.txt

11. **C** - Variant C
    - Correct structure uses `if __name__ == "__main__":` guard, allows importing without execution, easier to test, follows Python best practices

12. **B** - `sys.stdin.buffer.read()`
    - For binary data use `.buffer` attribute. `sys.stdin` works with text (str), `sys.stdin.buffer` works with bytes

13. **A** - Variant A
    - `sys.stdin` is already a file object, can be passed directly to `csv.reader()` or `csv.DictReader()`. No need to read all data into memory first

14. **B** - Interrupt signal (Ctrl+C)
    - SIGINT is sent when Ctrl+C is pressed. Should exit with code 130 (128 + 2, where 2 is SIGINT number)

15. **C** - Create GUI for every program
    - Unix philosophy: do one thing well, programs work together, use text streams as universal interface. GUIs are fine but not required for Unix approach

---

## Practical Exercise

Find errors in this code:

```python
import sys

for line in sys.stdin.readlines():
    result = process(line)
    print(result, file=sys.stdout)
    print(f"Processed line", file=sys.stdout)
```

**Errors:**
1. `readlines()` loads entire file into memory — bad for large files (use `for line in sys.stdin:`)
2. Diagnostic messages in stdout — should go to stderr
3. `file=sys.stdout` is redundant — stdout is default
4. No exception handling — need BrokenPipeError and KeyboardInterrupt

**Fixed version:**
```python
import sys

try:
    for line in sys.stdin:
        result = process(line)
        print(result)  # To stdout
        print("Processed line", file=sys.stderr)  # To stderr
except BrokenPipeError:
    sys.stderr.close()
    sys.exit(0)
except KeyboardInterrupt:
    sys.exit(130)
```

---

## Scoring Guide

- **13-15 correct**: Excellent! You understand Unix approach in Python 🏆
- **10-12 correct**: Good! Minor gaps remain 👍
- **7-9 correct**: Not bad, need more practice 📚
- **Below 7**: Re-read the lecture and do homework 💪

**Tip:** The best way to learn is to write code! Create your own utilities and use them in daily work.
