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

## Question 11: Default Values

What does `${var:-default}` do?

A) Sets var to "default" permanently  
B) Uses "default" if var is unset or empty  
C) Compares var to "default"  
D) Appends "default" to var  

---

## Question 12: mapfile/readarray

What does `mapfile -t lines < file.txt` do?

A) Prints lines from file  
B) Counts lines in file  
C) Reads file into an array variable called `lines`  
D) Maps each line to a function  

---

## Question 13: String Replacement

What does `${text//old/new}` do?

A) Replaces first occurrence of "old" with "new"  
B) Replaces all occurrences of "old" with "new"  
C) Removes "old" from text  
D) Searches for "old" in text  

---

## Question 14: Conditional Expressions

What does `[[ -z "$var" ]]` test?

A) If var is set  
B) If var is empty or unset  
C) If var is zero  
D) If var is a file  

---

## Question 15: Here Documents

What does `cat <<EOF ... EOF` do?

A) Reads from a file named EOF  
B) Provides multi-line input to the command  
C) Appends to a file  
D) Creates a named pipe  

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | $(command) is the modern, POSIX-compliant syntax |
| 2 | B | IFS=',' sets the delimiter for read command |
| 3 | C | `${#arr[@]}` gives the count of array elements |
| 4 | A | Extracts substring starting at position 5, length 10 |
| 5 | B | set -euo pipefail: exit on error, undefined vars, and pipe failures |
| 6 | C | Exit code 0 indicates success |
| 7 | B | Process substitution creates a temporary named pipe |
| 8 | C | $((expression)) is arithmetic expansion |
| 9 | B | `$1` is the first positional parameter |
| 10 | B | `local` limits variable scope to the function |
| 11 | B | Returns "default" if var is unset/empty, doesn't modify var |
| 12 | C | mapfile reads lines into an array, -t strips newlines |
| 13 | B | `//` replaces all occurrences (single `/` replaces only first) |
| 14 | B | `-z` tests if the string is empty or variable is unset |
| 15 | B | Here documents provide multi-line input to commands |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **13-15 correct (87-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **10-12 correct (67-80%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **7-9 correct (47-60%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 7 correct (<47%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
