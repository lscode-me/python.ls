# Homework: Coreutils Data Transformation

## Assignment 1: Column Extraction (cut)
Extract the 2nd and 4th columns from a CSV file.
- Input: `products.csv` with columns: id,name,price,category
- Output: name and category only
- Hint: Use `cut -d',' -f2,4`

## Assignment 2: File Merging (paste)
Combine three files into one CSV:
- `ids.txt`: user IDs (one per line)
- `names.txt`: names
- `ages.txt`: ages
- Output: `users.csv` with format: id,name,age
- Hint: Use `paste -d','`

## Assignment 3: Case Conversion (tr)
Convert all text to uppercase and remove punctuation.
- Input: `article.txt`
- Steps:
  1. Remove punctuation with `tr -d`
  2. Convert to uppercase with `tr '[:lower:]' '[:upper:]'`
- Hint: Chain two `tr` commands

## Assignment 4: Frequency Analysis (sort + uniq)
Find the 10 most frequent words in a text file.
- Input: `book.txt`
- Steps:
  1. Convert to lowercase
  2. Replace spaces with newlines (one word per line)
  3. Sort
  4. Count with `uniq -c`
  5. Sort numerically and show top 10
- Hint: `tr ' ' '\n' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn | head -10`

## Assignment 5: CSV Sorting (sort -t)
Sort a CSV file by the price column (3rd field) in descending numeric order.
- Input: `products.csv` with: id,name,price,category
- Output: Sorted by price (highest first)
- Hint: `sort -t',' -k3,3nr`

## Assignment 6: Deduplication (sort + uniq)
Remove duplicate lines from a file and save unique lines only.
- Input: `emails.txt` with duplicate email addresses
- Output: `unique_emails.txt`
- Hint: `sort emails.txt | uniq > unique_emails.txt`

## Assignment 7: File Splitting (split)
Split a large CSV file into chunks of 1000 lines each.
- Input: `large_dataset.csv` (10,000 lines)
- Output: Files named `chunk_00`, `chunk_01`, etc.
- Hint: `split -l 1000 -d large_dataset.csv chunk_`

## Assignment 8: Progress Monitoring (pv)
Compress a large file while showing progress.
- Input: `large_file.csv`
- Output: `large_file.csv.gz` with progress bar
- Hint: `pv large_file.csv | gzip > large_file.csv.gz`

## Assignment 9: Column Reordering (cut + paste)
Reorder CSV columns from (id,name,age,city) to (name,city,age,id).
- Input: `people.csv`
- Output: `reordered.csv`
- Hint: Use `cut` multiple times or `awk`

## Assignment 10: Real-Time Log Monitoring (stdbuf + grep)
Monitor a log file for ERROR lines with unbuffered output.
- Command: Tail a log and grep for errors with immediate output
- Hint: `tail -f app.log | stdbuf -oL grep ERROR`

## Bonus Challenges

### Bonus 1: Parallel File Processing
Split a large CSV into 10 chunks, process each in parallel (e.g., count lines), then merge results.
- Use `split`, background jobs with `&`, `wait`, and merge with `cat`

### Bonus 2: CSV Column Statistics
Calculate min, max, and average of a numeric column in a CSV.
- Use `cut` to extract column, `sort -n`, `head`/`tail` for min/max, `awk` for average

### Bonus 3: Top-K Frequency Analysis
Create a script that takes a file and number K, returns the K most frequent lines.
- Example: `top_k_freq.sh file.txt 5`
- Use `sort | uniq -c | sort -rn | head -n $K`

### Bonus 4: CSV Join Simulation
Given two CSV files with a common key column, create a joined output.
- `users.csv`: id,name
- `orders.csv`: user_id,amount
- Output: id,name,amount
- Hint: Use `join` command or `awk`

### Bonus 5: Progress-Monitored ETL Pipeline
Create a pipeline that:
1. Reads a large CSV with `pv`
2. Filters rows with `grep`
3. Sorts by a column
4. Removes duplicates
5. Saves to output
- Show progress at each step

## Submission Guidelines
- Submit all scripts and commands used
- Include sample input and output files
- Document performance metrics (time, memory) for large file operations
- Explain any challenges encountered
