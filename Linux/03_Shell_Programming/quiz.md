# Shell Programming as a Mini-DSL for Data Processing - Quiz

Test your knowledge of bash scripting and data processing.

---

## Question 1: Command Substitution

Which is the modern, preferred syntax for command substitution?

A) `command`  
B) $(command)  
C) ${command}  
D) $[command]  

---

## Question 2: while read Loop

What does `IFS=',' read col1 col2 col3` do?

A) Reads three files  
B) Splits input by comma into three variables  
C) Reads three lines  
D) Concatenates three columns with commas  

---

## Question 3: Arrays

How do you get the length of a bash array named `arr`?

A) `${arr.length}`  
B) `${#arr}`  
C) `${#arr[@]}`  
D) `length($arr)`  

---

## Question 4: String Operations

What does `${text:5:10}` do?

A) Extracts substring starting at position 5, length 10  
B) Replaces 5 characters with 10  
C) Extracts characters from 5 to 10  
D) Repeats text 5 times  

---

## Question 5: set Command

What does `set -euo pipefail` do?

A) Enables verbose output  
B) Exits on error, undefined variables, and pipe failures  
C) Sets environment variables  
D) Enables debugging mode  

---

## Question 6: Exit Codes

What exit code indicates success in bash?

A) 1  
B) -1  
C) 0  
D) 200  

---

## Question 7: Process Substitution

What does `<(command)` create?

A) A temporary file  
B) A temporary named pipe for command output  
C) A background process  
D) A subshell  

---

## Question 8: Arithmetic

Which is the correct way to do arithmetic in bash?

A) `$[5 + 3]`  
B) `$(5 + 3)`  
C) `$((5 + 3))`  
D) `${5 + 3}`  

---

## Question 9: Functions

How do you access the first argument in a bash function?

A) `$arg1`  
B) `$1`  
C) `${args[0]}`  
D) `argv[1]`  

---

## Question 10: Local Variables

What does the `local` keyword do in a function?

A) Makes variable globally accessible  
B) Limits variable scope to the function  
C) Makes variable constant  
D) Exports variable to child processes  

---

## Answer Key

1. B - $(command)
2. B - Splits input by comma into three variables
3. C - `${#arr[@]}`
4. A - Extracts substring starting at position 5, length 10
5. B - Exits on error, undefined variables, and pipe failures
6. C - 0
7. B - A temporary named pipe for command output
8. C - `$((5 + 3))`
9. B - `$1`
10. B - Limits variable scope to the function

---

## Scoring Guide

- **9-10 correct**: Excellent! You're a bash scripting pro.
- **7-8 correct**: Good job! Review the advanced topics.
- **5-6 correct**: Fair understanding. Practice more with scripts.
- **Below 5**: Study the lecture materials and complete homework assignments.
