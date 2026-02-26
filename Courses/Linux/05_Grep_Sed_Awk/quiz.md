# Grep, Sed & Awk: Text Processing Power Tools - Quiz

## Questions

## Question 1: Which grep option shows only

Which grep option shows only the matching part of a line (not the entire line)?

A) `-l`
B) `-h`
C) `-o`
D) `-m`


## Question 2: What does the regex pattern

What does the regex pattern `^ERROR` match?

A) Lines containing "ERROR" anywhere
B) Lines starting with "ERROR"
C) Lines ending with "ERROR"
D) The word "ERROR" only


## Question 3: Which sed command replaces all

Which sed command replaces all occurrences of "cat" with "dog" in a file?

A) `sed 's/cat/dog/' file.txt`
B) `sed 's/cat/dog/g' file.txt`
C) `sed 'g/cat/dog/s' file.txt`
D) `sed 'replace cat dog' file.txt`


## Question 4: What does do

What does `sed '/pattern/d' file.txt` do?

A) Deletes the pattern from matching lines
B) Deletes lines that match the pattern
C) Duplicates lines matching the pattern
D) Displays only matching lines


## Question 5: In awk what does represent

In awk, what does `$0` represent?

A) The first field
B) The number of fields
C) The entire current line
D) Zero (the number)


## Question 6: Which awk command prints the

Which awk command prints the 2nd and 4th columns of a CSV file?

A) `awk -F',' '{print $2 $4}' file.csv`
B) `awk -F',' '{print $2, $4}' file.csv`
C) `awk -F',' 'print $2,$4' file.csv`
D) `awk '{print 2,4}' file.csv`


## Question 7: What does represent in awk

What does `NR` represent in awk?

A) Number of records (line number)
B) New record
C) Numeric result
D) Next row


## Question 8: Which command extracts all email

Which command extracts all email addresses from a text file?

A) `grep '@' file.txt`
B) `grep -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' file.txt`
C) `grep 'email' file.txt`
D) `sed '/email/p' file.txt`


## Question 9: How do you sum the

How do you sum the 3rd column in a CSV file (skipping the header) with awk?

A) `awk -F',' '{sum += $3} END {print sum}' file.csv`
B) `awk -F',' 'NR > 1 {sum += $3} END {print sum}' file.csv`
C) `awk -F',' 'sum($3)' file.csv`
D) `awk -F',' 'print sum $3' file.csv`


## Question 10: What is the correct order

What is the correct order for this pipeline: filter lines with "ERROR", extract the timestamp, and count occurrences per hour?

A) `sed → grep → sort → uniq -c`
B) `grep → sed → sort → uniq -c`
C) `sort → grep → sed → uniq -c`
D) `grep → sort → sed → uniq -c`


## Question 11: What does do

What does `grep -C 3 "pattern" file.txt` do?

A) Shows 3 lines before the match
B) Shows 3 lines after the match
C) Shows 3 lines before and after the match
D) Shows only the 3rd match


## Question 12: How do you use backreferences

How do you use backreferences in sed to swap date format from YYYY-MM-DD to DD/MM/YYYY?

A) `sed 's/[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/\3\/\2\/\1/'`
B) `sed 's/\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\)/\3\/\2\/\1/'`
C) `sed 's/(\d{4})-(\d{2})-(\d{2})/\3\/\2\/\1/'`
D) `sed 's/(.*)-(.*)-(.*)/\3\/\2\/\1/'`


## Question 13: What does do

What does `awk '{count[$1]++} END {for (key in count) print key, count[key]}'` do?

A) Counts total lines in the file
B) Counts occurrences of each unique value in the first field
C) Counts fields in each line
D) Counts words in the file


## Question 14: Which sed command performs multiple

Which sed command performs multiple substitutions on each line?

A) `sed 's/foo/bar/' 's/old/new/' file.txt`
B) `sed 's/foo/bar/; s/old/new/' file.txt`
C) `sed -e 's/foo/bar/' -e 's/old/new/' file.txt`
D) Both B and C


## Question 15: What does output

What does `awk -F',' '{print NF}' data.csv` output?

A) The number of records (lines) in the file
B) The number of fields in each line
C) The last field of each line
D) The field separator


## Question 16: What is the main difference

What is the main difference between regex and shell globbing?

A) They are the same thing
B) Regex is for text pattern matching, globbing is for file matching
C) Globbing is more powerful than regex
D) Regex only works in Python


## Question 17: In shell globbing what does

In shell globbing, what does `*.txt` match?

A) Zero or more occurrences of any character followed by ".txt"
B) Any files ending in .txt
C) Files with names containing an asterisk
D) The literal string "*.txt"


## Question 18: What does the regex pattern

What does the regex pattern `.*\.txt$` match?

A) Files ending in .txt (same as globbing)
B) Lines ending in .txt (any characters before it)
C) The literal string "*.txt"
D) All text files


## Question 19: Which regex pattern correctly matches

Which regex pattern correctly matches a valid IPv4 address with range validation (0-255)?

A) `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}`
B) `(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)`
C) `\d+\.\d+\.\d+\.\d+`
D) `[0-9].[0-9].[0-9].[0-9]`


## Question 20: Which regex pattern matches a

Which regex pattern matches a valid DNA sequence (only A, T, G, C)?

A) `^[ATGC]+$`
B) `[ATGC]*`
C) `^DNA[ATGC]$`
D) `\b[ATGC]\b`


## Question 21: What is the difference between

What is the difference between `*` in shell globbing vs regex?

A) No difference
B) Globbing: any characters; Regex: zero or more of previous character
C) Regex: any characters; Globbing: zero or one character
D) They both mean "optional"


## Question 22: Which command extracts all URLs

Which command extracts all URLs starting with http or https from a file?

A) `grep 'http' file.txt`
B) `grep -Eo 'https?://[^ ]+' file.txt`
C) `grep 'http*' file.txt`
D) `sed '/http/p' file.txt`


## Question 23: What does the regex pattern

What does the regex pattern `^[AUGC]+$` validate?

A) DNA sequences
B) RNA sequences
C) Protein sequences
D) Email addresses


## Question 24: Which sed command removes all

Which sed command removes all HTML tags from a file?

A) `sed 's/<.*>//g' file.html`
B) `sed 's/<[^>]*>//g' file.html`
C) `sed 's/html//g' file.html`
D) `sed '/</d' file.html`


## Question 25: What does do

What does `grep -v "pattern" file.txt` do?

A) Shows only lines matching the pattern
B) Shows lines NOT matching the pattern (inverts match)
C) Shows the pattern with context
D) Validates the pattern


## Question 26: Which regex pattern matches a

Which regex pattern matches a UUID?

A) `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
B) `[A-Z]{8}-[A-Z]{4}`
C) `\d{8}-\d{4}-\d{4}`
D) `[0-9]{32}`


## Question 27: In shell globbing what does

In shell globbing, what does `?` mean, and how is it different from regex `?`?

A) Both mean "optional"
B) Globbing: one character; Regex: zero or one of previous
C) Globbing: any characters; Regex: one character
D) No difference


## Question 28: What does do

What does `awk 'BEGIN {FS=","} {print $1, $3}' file.csv` do?

A) Prints fields 1 and 3 using comma as separator
B) Prints "BEGIN" and "FS"
C) Sets field separator and prints first and third fields
D) Prints only the first line


## Question 29: Which command finds all lines

Which command finds all lines containing either "ERROR" or "FATAL"?

A) `grep "ERROR FATAL" file.txt`
B) `grep -E "ERROR|FATAL" file.txt`
C) `grep "ERROR+FATAL" file.txt`
D) `grep "ERROR,FATAL" file.txt`


## Question 30: What is the correct regex

What is the correct regex to match a MAC address like `00:1A:2B:3C:4D:5E`?

A) `[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}`
B) `([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}`
C) `[0-9a-f]:*`
D) `\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}`


---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `-o` shows only matching text, not full lines |
| 2 | B | `^` anchors pattern to start of line |
| 3 | B | `/g` flag makes replacement global (all occurrences) |
| 4 | A | `/pattern/d` deletes entire lines matching pattern |
| 5 | C | `$0` is the entire current line/record |
| 6 | B | Need comma separator in print for space-separated output |
| 7 | A | NR is the current record (line) number |
| 8 | B | Comprehensive email regex pattern with word boundaries |
| 9 | B | `NR > 1` skips header row, accumulates in END block |
| 10 | A | Filter first (grep), transform (sed), then aggregate (sort | uniq -c) |
| 11 | C | `-C` shows context lines both before and after (combines -A and -B) |
| 12 | D | Need escaped parentheses for capturing groups, reference with `\1` `\2` `\3` |
| 13 | B | Associative array counts occurrences of each unique first field value |
| 14 | D | Both semicolon separation and multiple `-e` flags work |
| 15 | B | NF is the number of fields in the current record/line |
| 16 | B | Regex is for text pattern matching, globbing is for file name matching |
| 17 | B | Shell globbing `*.txt` matches any filenames ending in .txt |
| 18 | B | In regex, `.*` means any characters, `\.` is literal dot, `$` is end of line |
| 19 | B | Full validation requires checking each octet is 0-255 using alternation |
| 20 | A | `^` ensures start of string, `[ATGC]+` matches valid DNA bases, `$` ensures end |
| 21 | B | Globbing `*` = any characters; regex `*` = zero or more of PREVIOUS character |
| 22 | B | `-E` for extended regex, `-o` for only matching part |
| 23 | B | RNA uses AUGC (Uracil instead of Thymine); DNA uses ATGC |
| 24 | B | `[^>]*` matches any character except `>`, preventing greedy matching |
| 25 | B | `-v` inverts the match, showing non-matching lines |
| 26 | C | Standard UUID format: 8-4-4-4-12 hexadecimal characters |
| 27 | B | Globbing `?` matches exactly one character; regex `?` means zero or one |
| 28 | B | BEGIN block sets field separator, then prints fields 1 and 3 |
| 29 | B | `-E` enables extended regex with `|` for alternation (OR logic) |
| 30 | B | Uses repetition `{5}` for first 5 pairs, case-insensitive hex |

---

## Scoring Guide

- **27-30 correct**: Outstanding! Expert-level mastery of grep, sed, awk, and regex.
- **23-26 correct**: Excellent! Strong understanding of text processing and pattern matching.
- **19-22 correct**: Very Good! You grasp most concepts; review regex vs globbing differences.
- **15-18 correct**: Good! Solid foundation; practice more with advanced regex patterns.
- **11-14 correct**: Fair! Review regex fundamentals and the difference between regex and shell globbing.
- **Below 11**: Study the lecture materials carefully and complete hands-on exercises.
