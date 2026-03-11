# Unix as a Language of Data & Streams - Quiz

Test your knowledge of Unix streams, pipes, and data processing fundamentals.

---

## Question 1: Standard Streams

What are the three standard streams in Unix?

A) input, output, log  
B) read, write, execute  
C) file, socket, pipe  
D) stdin, stdout, stderr  

---

## Question 2: Pipe Operator

What does the pipe operator `|` do?

A) Creates a new file  
B) Connects stdout of one command to stdin of the next  
C) Runs commands in parallel  
D) Appends output to a file  

---

## Question 3: Output Redirection

Which command redirects both stdout and stderr to a file?

A) `command > file`  
B) `command 2> file`  
C) `command &> file`  
D) `command | file`  

---

## Question 4: uniq Command

Why does `uniq` require sorted input?

A) It's faster with sorted data  
B) It only removes adjacent duplicate lines  
C) The Unix standard requires it  
D) It doesn't actually require sorting  

---

## Question 5: cut Command

What does `cut -d',' -f2 data.csv` do?

A) Deletes the second column  
B) Extracts the second field using comma as delimiter  
C) Cuts 2 characters from each line  
D) Removes commas from the file  

---

## Question 6: Filter-Transform-Aggregate

Which represents the correct order in the Unix data processing pattern?

A) Aggregate → Filter → Transform  
B) Transform → Filter → Aggregate  
C) Filter → Aggregate → Transform  
D) Filter → Transform → Aggregate  

---

## Question 7: head and tail

What does `tail -f logfile.txt` do?

A) Shows the last line of the file  
B) Continuously monitors the file for new lines  
C) Reverses the order of lines  
D) Shows the first 10 lines  

---

## Question 8: sort Options

Which `sort` option sorts numerically instead of alphabetically?

A) `-a`  
B) `-n`  
C) `-r`  
D) `-u`  

---

## Question 9: grep Behavior

What does `grep -v "pattern" file.txt` do?

A) Shows lines matching pattern  
B) Shows line numbers  
C) Shows lines NOT matching pattern  
D) Shows only the matching text  

---

## Question 10: curl Usage

Which `curl` option follows HTTP redirects?

A) `-f`  
B) `-s`  
C) `-L`  
D) `-O`  

---

## Question 11: tee Command

What does `command | tee output.txt | process` do?

A) Writes output to file only  
B) Writes to output.txt AND passes data to process  
C) Replaces process output with output.txt  
D) Appends to output.txt  

---

## Question 12: Named Pipes

What happens when you write to a FIFO before a reader connects?

A) Data is lost  
B) Write operation blocks until a reader connects  
C) Error is thrown immediately  
D) Data is written to disk  

---

## Question 13: Buffering

Why use `grep --line-buffered` in a real-time pipeline?

A) To make grep faster  
B) To process multiple lines at once  
C) To output each matching line immediately instead of buffering  
D) To limit memory usage  

---

## Question 14: /dev/fd/

What is `/dev/fd/0`?

A) The first file in the current directory  
B) A reference to the standard input (stdin)  
C) A temporary file  
D) A device file  

---

## Question 15: tee Multiple Outputs

Which command saves data to three files AND displays it on screen?

A) `command | tee file1 file2 file3`  
B) `command > file1 > file2 > file3`  
C) `command | tee file1 | tee file2 | tee file3`  
D) `command >> file1 file2 file3`  

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | stdin, stdout, stderr |
| 2 | B | Connects stdout of one command to stdin of the next |
| 3 | C | `command &> file` |
| 4 | B | It only removes adjacent duplicate lines |
| 5 | B | Extracts the second field using comma as delimiter |
| 6 | D | Filter → Transform → Aggregate |
| 7 | B | Continuously monitors the file for new lines |
| 8 | B | `-n` |
| 9 | C | Shows lines NOT matching pattern |
| 10 | C | `-L` |
| 11 | B | `tee` writes to file and passes data through to next command in pipeline |
| 12 | B | FIFO write blocks until reader connects (synchronization mechanism) |
| 13 | C | `--line-buffered` forces immediate output, crucial for real-time monitoring (like `tail -f | grep`) |
| 14 | B | `/dev/fd/0` is a symbolic link to stdin (file descriptor 0) |
| 15 | A | `tee` can write to multiple files in one command and still output to stdout |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **13-15 correct (87-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **10-12 correct (67-80%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **7-9 correct (47-60%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 7 correct (<47%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
