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

## Question 11: Custom File Descriptors

How do you open a file for writing on file descriptor 4?

A) `exec 4> output.txt`  
B) `open 4 > output.txt`  
C) `fd 4 = output.txt`  
D) `4> output.txt`  

---

## Question 12: Device Files

What's the difference between `/dev/zero` and `/dev/urandom`?

A) Both generate random data  
B) `/dev/zero` produces null bytes, `/dev/urandom` produces pseudo-random data  
C) `/dev/zero` is faster  
D) They're the same file  

---

## Question 13: Setgid on Directories

What happens when the setgid bit (2000) is set on a directory?

A) Only owner can access the directory  
B) New files inherit the directory's group ownership  
C) Directory becomes read-only  
D) Directory is shared across users  

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | File metadata and pointers to data blocks |
| 2 | B | Both filenames point to the same i-node |
| 3 | C | 2 |
| 4 | C | Named pipe (FIFO) |
| 5 | A | rwxr-xr-x |
| 6 | C | Redirects stderr to stdout |
| 7 | B | Symlinks are a separate file with a path, hard links share the same i-node |
| 8 | C | 644 |
| 9 | B | Discarding unwanted output |
| 10 | B | Allows the file to run with owner's permissions |
| 11 | A | `exec 4> output.txt` opens file descriptor 4 for writing |
| 12 | B | `/dev/zero` provides infinite null bytes, `/dev/urandom` provides pseudo-random data |
| 13 | B | Setgid on directories makes new files inherit the directory's group (useful for shared directories) |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **11-13 correct (85-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **9-10 correct (69-77%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **6-8 correct (46-62%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 6 correct (<46%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
