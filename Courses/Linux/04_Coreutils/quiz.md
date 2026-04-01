# Coreutils: Data Transformation Utilities - Quiz

Test your knowledge of "Coreutils: Data Transformation Utilities".

---

## Question 1: Column Extraction

Which command extracts the 2nd and 4th columns from a CSV file?

A) `cut -d',' -f2-4 file.csv`

B) `cut -d',' -f2,4 file.csv`

C) `awk -F',' '{print $2","$4}' file.csv`

D) Both B and C

---

## Question 2: Paste Command

What does `paste -d',' file1.txt file2.txt` do?

A) Appends file2.txt to the end of file1.txt

B) Merges lines from both files side-by-side with comma separator

C) Pastes content of file2.txt into file1.txt

D) Creates a CSV file from two text files

---

## Question 3: Character Translation

Which command converts all lowercase letters to uppercase?

A) `tr 'a-z' 'A-Z'`

B) `tr '[:lower:]' '[:upper:]'`

C) Both A and B

D) `sed 's/[a-z]/[A-Z]/g'`

---
   - D) `awk '{print toupper($0)}'`

## Question 4: Sort Key Options

What does `sort -t',' -k3,3nr data.csv` do?

A) Sorts by 3rd column alphabetically
B) Sorts by 3rd column numerically in ascending order
C) Sorts by 3rd column numerically in descending order
D) Sorts by 3rd character of each line


## Question 5: Sort Before Uniq

Why must you run `sort` before `uniq`?

A) To make `uniq` run faster
B) Because `uniq` only removes adjacent duplicate lines
C) Because `sort` is required by `uniq` syntax
D) To ensure alphabetical order


## Question 6: Which command splits a file

Which command splits a file into 1000-line chunks with numeric suffixes?

A) `split -l 1000 data.txt`
B) `split -l 1000 -d data.txt chunk_`
C) `split -n 1000 data.txt`
D) `csplit -l 1000 data.txt`


## Question 7: Progress Viewer

What does `pv large.csv | gzip > large.csv.gz` do?

A) Compresses the file
B) Compresses the file and shows progress
C) Views the file and compresses it
D) Pipes file through gzip with verification


## Question 8: Which command shows only duplicate

Which command shows only duplicate lines (those that appear more than once)?

A) `sort data.txt | uniq`
B) `sort data.txt | uniq -u`
C) `sort data.txt | uniq -d`
D) `sort data.txt | uniq --duplicates`


## Question 9: Buffer Control

What does `stdbuf -oL grep ERROR app.log` do?

A) Buffers output for better performance
B) Uses line-buffered output for real-time visibility
C) Limits output to L lines
D) Logs errors to a buffer file


## Question 10: Which command counts the frequency

Which command counts the frequency of each line and shows the top 5?

A) `sort data.txt | uniq | head -5`
B) `sort data.txt | uniq -c | head -5`
C) `sort data.txt | uniq -c | sort -rn | head -5`
D) `uniq -c data.txt | sort -rn | head -5`

---

## Question 11: Cut Complement

What does `cut -d',' --complement -f1 file.csv` do?

A) Extracts only the first column
B) Extracts all columns except the first
C) Counts the number of columns
D) Removes all commas from the file

---

## Question 12: Split by Size

Which command splits a file into 100MB chunks?

A) `split -l 100 file.txt`
B) `split -b 100M file.txt part_`
C) `split -n 100 file.txt`
D) `split --size=100MB file.txt`

---

## Question 13: Character Deletion

What does `tr -d '[:digit:]'` do?

A) Translates digits to letters
B) Removes all digits from input
C) Duplicates all digits
D) Counts all digits

---

## Question 14: Serial Paste

What does `paste -s -d',' file.txt` do?

A) Sorts and pastes file content
B) Converts all rows into a single comma-separated line
C) Pastes content into system clipboard
D) Serializes file content to JSON

---

## Question 15: Parallel Sort

What does `sort --parallel=4 -S 2G huge.txt` do?

A) Sorts 4 files in parallel with 2GB output
B) Sorts using 4 CPU cores and 2GB memory buffer
C) Splits file into 4 parts of 2GB each
D) Creates 4 sorted copies of the file

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Both `cut -f2,4` and awk can extract specific columns |
| 2 | B | `paste` merges files horizontally line-by-line with the specified delimiter |
| 3 | C | Both `tr 'a-z' 'A-Z'` and `tr '[:lower:]' '[:upper:]'` convert to uppercase |
| 4 | C | `-k3,3nr` sorts by 3rd column numerically in reverse (descending) order |
| 5 | B | `uniq` only removes adjacent duplicate lines, so data must be sorted first |
| 6 | B | `-l 1000` sets line count, `-d` uses numeric suffixes, prefix is specified |
| 7 | B | `pv` (pipe viewer) shows progress while passing data through to gzip |
| 8 | C | `uniq -d` shows only duplicated lines (those appearing more than once) |
| 9 | B | `stdbuf -oL` sets stdout to line-buffered mode for real-time output |
| 10 | C | Must count with `uniq -c`, sort by count descending, then take top 5 |
| 11 | B | `--complement` inverts selection, extracting all columns except specified |
| 12 | B | `-b 100M` splits by size (100 megabytes) with specified prefix |
| 13 | B | `tr -d` deletes characters matching the specified class (digits) |
| 14 | B | `-s` serial mode joins all lines into one, `-d','` uses comma separator |
| 15 | B | `--parallel=4` uses 4 cores, `-S 2G` sets 2GB memory buffer for sorting |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **2-3 correct (67-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **2-1 correct (67-33%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **1-1 correct (33-33%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 1 correct (<33%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
