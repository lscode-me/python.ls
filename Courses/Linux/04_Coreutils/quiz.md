# Coreutils: Data Transformation Utilities - Quiz

Test your knowledge of "Coreutils: Data Transformation Utilities".

---

## Question 1: Column Extraction

Which command extracts the 2nd and 4th columns from a CSV file?

A) `cut -d',' -f2-4 file.csv`

B) `cut -d',' -f2,4 file.csv`

C) `awk -F',' '{print $2,$4}' file.csv`

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

4. What does `sort -t',' -k3,3nr data.csv` do?
   - A) Sorts by 3rd column alphabetically
   - B) Sorts by 3rd column numerically in ascending order
   - C) Sorts by 3rd column numerically in descending order
   - D) Sorts by 3rd character of each line

5. Why must you run `sort` before `uniq`?
   - A) To make `uniq` run faster
   - B) Because `uniq` only removes adjacent duplicate lines
   - C) Because `sort` is required by `uniq` syntax
   - D) To ensure alphabetical order

6. Which command splits a file into 1000-line chunks with numeric suffixes?
   - A) `split -l 1000 file.txt`
   - B) `split -l 1000 -d file.txt chunk_`
   - C) `split -n 1000 file.txt`
   - D) `csplit -l 1000 file.txt`

7. What does `pv large.csv | gzip > large.csv.gz` do?
   - A) Compresses the file
   - B) Compresses the file and shows progress
   - C) Views the file and compresses it
   - D) Pipes file through gzip with verification

8. Which command shows only duplicate lines (those that appear more than once)?
   - A) `sort file.txt | uniq`
   - B) `sort file.txt | uniq -u`
   - C) `sort file.txt | uniq -d`
   - D) `sort file.txt | uniq -c | grep -v ' 1 '`

9. What does `stdbuf -oL grep ERROR app.log` do?
   - A) Buffers output for better performance
   - B) Uses line-buffered output for real-time visibility
   - C) Limits output to L lines
   - D) Logs errors to a buffer file

10. Which command counts the frequency of each line and shows the top 5?
    - A) `sort file.txt | uniq | head -5`
    - B) `sort file.txt | uniq -c | head -5`
    - C) `sort file.txt | uniq -c | sort -rn | head -5`
    - D) `uniq -c file.txt | sort -rn | head -5`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Both formats work: `cut -f2,4` and awk |
| 2 | B | `paste` merges files horizontally with delimiter |
| 3 | C | Both `a-z` → `A-Z` and character classes work |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **2-3 correct (67-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **2-1 correct (67-33%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **1-1 correct (33-33%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 1 correct (<33%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
