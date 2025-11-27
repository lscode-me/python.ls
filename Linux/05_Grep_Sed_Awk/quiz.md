# Quiz: Grep, Sed & Awk

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
