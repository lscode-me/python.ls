# Coreutils: Data Transformation Utilities - Quiz

## Questions

1. Which command extracts the 2nd and 4th columns from a CSV file?
   - A) `cut -d',' -f2-4 file.csv`
   - B) `cut -d',' -f2,4 file.csv`
   - C) `awk -F',' '{print $2,$4}' file.csv`
   - D) Both B and C

2. What does `paste -d',' file1.txt file2.txt` do?
   - A) Appends file2.txt to the end of file1.txt
   - B) Merges lines from both files side-by-side with comma separator
   - C) Pastes content of file2.txt into file1.txt
   - D) Creates a CSV file from two text files

3. Which command converts all lowercase letters to uppercase?
   - A) `tr 'a-z' 'A-Z'`
   - B) `tr '[:lower:]' '[:upper:]'`
   - C) Both A and B
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

## Answer Key
1. D - Both formats work: `cut -f2,4` and awk
2. B - `paste` merges files horizontally with delimiter
3. C - Both `a-z` → `A-Z` and character classes work
4. C - `-k3,3nr` = sort by field 3, numeric, reverse
5. B - `uniq` only detects adjacent duplicates
6. B - `-d` for numeric suffixes, `-l 1000` for lines
7. B - `pv` shows progress while piping to gzip
8. C - `uniq -d` shows only duplicated lines
9. B - `-oL` enables line-buffered output
10. C - Must sort by count (`-rn`) after `uniq -c`
