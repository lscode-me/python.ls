# Grep, Sed & Awk: Text Processing Power Tools - Quiz

## Questions

1. Which grep option shows only the matching part of a line (not the entire line)?
   - A) `-l`
   - B) `-h`
   - C) `-o`
   - D) `-m`

2. What does the regex pattern `^ERROR` match?
   - A) Lines containing "ERROR" anywhere
   - B) Lines starting with "ERROR"
   - C) Lines ending with "ERROR"
   - D) The word "ERROR" only

3. Which sed command replaces all occurrences of "cat" with "dog" in a file?
   - A) `sed 's/cat/dog/' file.txt`
   - B) `sed 's/cat/dog/g' file.txt`
   - C) `sed 'g/cat/dog/s' file.txt`
   - D) `sed 'replace cat dog' file.txt`

4. What does `sed '/pattern/d' file.txt` do?
   - A) Deletes the pattern from matching lines
   - B) Deletes lines that match the pattern
   - C) Duplicates lines matching the pattern
   - D) Displays only matching lines

5. In awk, what does `$0` represent?
   - A) The first field
   - B) The number of fields
   - C) The entire current line
   - D) Zero (the number)

6. Which awk command prints the 2nd and 4th columns of a CSV file?
   - A) `awk -F',' '{print $2 $4}' file.csv`
   - B) `awk -F',' '{print $2, $4}' file.csv`
   - C) `awk -F',' 'print $2,$4' file.csv`
   - D) `awk '{print 2,4}' file.csv`

7. What does `NR` represent in awk?
   - A) Number of records (line number)
   - B) New record
   - C) Numeric result
   - D) Next row

8. Which command extracts all email addresses from a text file?
   - A) `grep '@' file.txt`
   - B) `grep -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' file.txt`
   - C) `grep 'email' file.txt`
   - D) `sed '/email/p' file.txt`

9. How do you sum the 3rd column in a CSV file (skipping the header) with awk?
   - A) `awk -F',' '{sum += $3} END {print sum}' file.csv`
   - B) `awk -F',' 'NR > 1 {sum += $3} END {print sum}' file.csv`
   - C) `awk -F',' 'sum($3)' file.csv`
   - D) `awk -F',' 'print sum $3' file.csv`

10. What is the correct order for this pipeline: filter lines with "ERROR", extract the timestamp, and count occurrences per hour?
    - A) `sed → grep → sort → uniq -c`
    - B) `grep → sed → sort → uniq -c`
    - C) `sort → grep → sed → uniq -c`
    - D) `grep → sort → sed → uniq -c`

11. What does `grep -C 3 "pattern" file.txt` do?
    - A) Shows 3 lines before the match
    - B) Shows 3 lines after the match
    - C) Shows 3 lines before and after the match
    - D) Shows only the 3rd match

12. How do you use backreferences in sed to swap date format from YYYY-MM-DD to DD/MM/YYYY?
    - A) `sed 's/[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/\3\/\2\/\1/'`
    - B) `sed 's/\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\)/\3\/\2\/\1/'`
    - C) `sed 's/(\d{4})-(\d{2})-(\d{2})/\3\/\2\/\1/'`
    - D) `sed 's/(.*)-(.*)-(.*)/\3\/\2\/\1/'`

13. What does `awk '{count[$1]++} END {for (key in count) print key, count[key]}'` do?
    - A) Counts total lines in the file
    - B) Counts occurrences of each unique value in the first field
    - C) Counts fields in each line
    - D) Counts words in the file

14. Which sed command performs multiple substitutions on each line?
    - A) `sed 's/foo/bar/' 's/old/new/' file.txt`
    - B) `sed 's/foo/bar/; s/old/new/' file.txt`
    - C) `sed -e 's/foo/bar/' -e 's/old/new/' file.txt`
    - D) Both B and C

15. What does `awk -F',' '{print NF}' data.csv` output?
    - A) The number of records (lines) in the file
    - B) The number of fields in each line
    - C) The last field of each line
    - D) The field separator

---

## Answer Key
1. C - `-o` shows only matching text, not full lines
2. B - `^` anchors pattern to start of line
3. B - `/g` flag makes replacement global (all occurrences)
4. B - `/pattern/d` deletes entire lines matching pattern
5. C - `$0` is the entire current line/record
6. B - Need comma separator in print for space-separated output
7. A - NR is the current record (line) number
8. B - Comprehensive email regex pattern with word boundaries
9. B - `NR > 1` skips header row, accumulates in END block
10. B - Filter first (grep), transform (sed), then aggregate (sort | uniq -c)
11. C - `-C` shows context lines both before and after (combines -A and -B)
12. B - Need escaped parentheses `\(` `\)` for capturing groups, reference with `\1` `\2` `\3`
13. B - Associative array counts occurrences of each unique first field value
14. D - Both semicolon separation and multiple `-e` flags work for chaining sed commands
15. B - NF is the number of fields in the current record/line

---

## Scoring Guide

- **13-15 correct**: Excellent! You've mastered grep, sed & awk.
- **10-12 correct**: Good job! Review advanced topics like backreferences and associative arrays.
- **7-9 correct**: Fair understanding. Practice more with regex and awk programming.
- **Below 7**: Study the lecture materials and complete hands-on exercises.
