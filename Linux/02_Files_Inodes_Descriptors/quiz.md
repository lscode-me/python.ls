# Files, I-nodes & File Descriptors - Quiz

Test your knowledge of Unix file system architecture.

---

## Question 1: I-node Purpose

What information does an i-node contain?

A) Filename and file content  
B) File metadata and pointers to data blocks  
C) Only the file size  
D) Directory structure  

---

## Question 2: Hard Links

What happens when you create a hard link to a file?

A) A new i-node is created with copied data  
B) Both filenames point to the same i-node  
C) A shortcut file is created  
D) The original file is moved  

---

## Question 3: File Descriptors

Which file descriptor number represents stderr?

A) 0  
B) 1  
C) 2  
D) 3  

---

## Question 4: File Types

What does the first character 'p' indicate in `ls -l` output?

A) Permission file  
B) Python script  
C) Named pipe (FIFO)  
D) Process file  

---

## Question 5: chmod Octal

What permissions does `chmod 755 file.sh` set?

A) rwxr-xr-x  
B) rwxrwxrwx  
C) rw-r--r--  
D) r-xr-xr-x  

---

## Question 6: Redirection

What does `command 2>&1` do?

A) Redirects stdout to stderr  
B) Redirects stdin to stdout  
C) Redirects stderr to stdout  
D) Duplicates both streams  

---

## Question 7: Symbolic Links

What's the key difference between hard links and symbolic links?

A) Hard links work across filesystems, symlinks don't  
B) Symlinks are a separate file with a path, hard links share the same i-node  
C) Symlinks are faster than hard links  
D) There is no difference  

---

## Question 8: umask

With `umask 022`, what are the default permissions for new files?

A) 777  
B) 755  
C) 644  
D) 022  

---

## Question 9: Special Files

What is `/dev/null` used for?

A) Generating random data  
B) Discarding unwanted output  
C) Creating empty files  
D) Testing file operations  

---

## Question 10: Special Bits

What does the setuid bit (4000) do?

A) Makes a file read-only  
B) Allows the file to run with owner's permissions  
C) Prevents file deletion  
D) Enables group access  

---

## Answer Key

1. B - File metadata and pointers to data blocks
2. B - Both filenames point to the same i-node
3. C - 2
4. C - Named pipe (FIFO)
5. A - rwxr-xr-x
6. C - Redirects stderr to stdout
7. B - Symlinks are a separate file with a path, hard links share the same i-node
8. C - 644
9. B - Discarding unwanted output
10. B - Allows the file to run with owner's permissions

---

## Scoring Guide

- **9-10 correct**: Excellent! You understand Unix file systems deeply.
- **7-8 correct**: Good job! Review the concepts you missed.
- **5-6 correct**: Fair understanding. Practice more with file operations.
- **Below 5**: Study the lecture materials and complete the homework assignments.
