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

## Answer Key

1. D - stdin, stdout, stderr
2. B - Connects stdout of one command to stdin of the next
3. C - `command &> file`
4. B - It only removes adjacent duplicate lines
5. B - Extracts the second field using comma as delimiter
6. D - Filter → Transform → Aggregate
7. B - Continuously monitors the file for new lines
8. B - `-n`
9. C - Shows lines NOT matching pattern
10. C - `-L`

---

## Scoring Guide

- **9-10 correct**: Excellent! You understand Unix streams and pipelines.
- **7-8 correct**: Good job! Review the commands you missed.
- **5-6 correct**: Fair understanding. Practice more with hands-on exercises.
- **Below 5**: Study the lecture materials and try the homework assignments.
