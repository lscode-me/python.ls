# Coreutils: Data Transformation Utilities

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

## Overview
GNU coreutils provide essential stream processing tools for data transformation. This lecture covers utilities that reshape, reorder, and format streaming data.

## Core Transformation Tools

### 1. `cut` — Column Extraction
Extract specific fields/characters from each line:

```bash
# Extract columns 2,4 from CSV
cut -d',' -f2,4 data.csv

# Character positions 1-10
cut -c1-10 file.txt

# Everything except column 1
cut -d',' -f2- data.csv
```

**Key Options:**
- `-d DELIM`: Field delimiter (default: TAB)
- `-f LIST`: Field numbers (1-indexed)
- `-c LIST`: Character positions
- `--complement`: Invert selection

### 2. `paste` — Column Merging
Join files side-by-side:

```bash
# Merge two files with TAB separator
paste file1.txt file2.txt

# Use comma separator
paste -d',' ids.txt names.txt ages.txt > people.csv

# Serial mode: convert rows to columns
paste -s -d',' data.txt
```

### 3. `tr` — Character Translation
Translate or delete characters:

```bash
# Convert case
tr '[:lower:]' '[:upper:]' < input.txt

# Delete characters
tr -d '[:punct:]' < text.txt

# Squeeze repeats
tr -s ' ' < text.txt  # collapse spaces

# ROT13 encoding
tr 'A-Za-z' 'N-ZA-Mn-za-m' < secret.txt
```

**Character Classes:**
- `[:alnum:]`, `[:alpha:]`, `[:digit:]`
- `[:lower:]`, `[:upper:]`
- `[:space:]`, `[:punct:]`

### 4. `sort` — Ordering Data
Sort lines efficiently:

```bash
# Default alphabetical sort
sort file.txt

# Numeric sort
sort -n numbers.txt

# Reverse order
sort -r file.txt

# Sort by second field (CSV)
sort -t',' -k2,2 data.csv

# Sort by numeric field (descending)
sort -t',' -k3,3nr data.csv

# Unique sort
sort -u file.txt

# Parallel sort (faster)
sort --parallel=4 -S 2G huge.txt
```

**Key Options:**
- `-t DELIM`: Field delimiter
- `-k POS`: Key position (field.char)
- `-n`: Numeric sort
- `-r`: Reverse
- `-u`: Unique
- `-s`: Stable sort
- `--parallel=N`: Use N cores
- `-S SIZE`: Memory buffer

### 5. `uniq` — Deduplication
Remove or count adjacent duplicates:

```bash
# Remove duplicates (requires sorted input)
sort file.txt | uniq

# Count occurrences
sort file.txt | uniq -c

# Show only duplicates
sort file.txt | uniq -d

# Show only unique
sort file.txt | uniq -u

# Case-insensitive
sort -f file.txt | uniq -i
```

### 6. `split` — File Splitting
Split large files:

```bash
# Split by lines (1000 per file)
split -l 1000 large.txt chunk_

# Split by size (100MB)
split -b 100M large.csv part_

# Numeric suffixes
split -l 1000 -d large.txt chunk_

# Custom suffix length
split -l 1000 -d -a 4 large.txt chunk_  # chunk_0000
```

### 7. `pv` — Progress Viewer
Monitor pipeline throughput:

```bash
# Show progress for file copy
pv large.csv | gzip > large.csv.gz

# Rate limit (1MB/s)
pv -L 1m large.csv > output.csv

# ETA and progress bar
pv -W large.csv | wc -l

# Multi-file progress
pv file1 file2 file3 | tar -cz > archive.tar.gz
```

### 8. `stdbuf` — Buffer Control
Control I/O buffering:

```bash
# Disable output buffering
stdbuf -oL python slow_script.py | tee log.txt

# Line-buffered output
stdbuf -oL grep ERROR /var/log/app.log

# Disable all buffering
stdbuf -i0 -o0 -e0 command
```

## Practical Examples

### Example 1: CSV Column Reordering
```bash
# Reorder columns: 3,1,2,4
cut -d',' -f3,1,2,4 data.csv
```

### Example 2: Join Two Files
```bash
# Create people.csv from separate files
paste -d',' ids.txt names.txt ages.txt > people.csv
```

### Example 3: Top 10 Most Frequent Lines
```bash
sort data.txt | uniq -c | sort -rn | head -10
```

### Example 4: Split and Process in Parallel
```bash
# Split large file
split -l 10000 -d large.csv chunk_

# Process in parallel
for chunk in chunk_*; do
    process_chunk.sh "$chunk" &
done
wait

# Merge results
cat chunk_*.processed > output.csv
rm chunk_*
```

### Example 5: Progress-Monitored Pipeline
```bash
pv access.log | \
  grep -E '^[0-9]' | \
  cut -d' ' -f1,7 | \
  sort | uniq -c | \
  sort -rn > top_ips.txt
```

## Best Practices

1. **Use `sort` before `uniq`**: `uniq` only removes adjacent duplicates
2. **Specify numeric sort** with `-n` for numbers
3. **Use `--parallel`** for large sorts
4. **Buffer large sorts** with `-S` memory option
5. **Use `pv`** for long-running pipelines
6. **Disable buffering** with `stdbuf -oL` for real-time output
7. **Split large files** before parallel processing
8. **Use stable sort** (`-s`) when field order matters

## Common Patterns

### Pattern 1: Frequency Analysis
```bash
# Count occurrences, show top 10
cut -d',' -f2 data.csv | sort | uniq -c | sort -rn | head -10
```

### Pattern 2: Column Swap
```bash
# Swap columns 1 and 2
awk -F',' '{print $2","$1","$3}' data.csv
# OR
cut -d',' -f2,1,3 data.csv
```

### Pattern 3: Deduplication by Key
```bash
# Keep first occurrence of each ID
sort -t',' -k1,1 -u data.csv
```

### Pattern 4: Parallel Processing
```bash
# Split, process, merge
split -l 1000 -d input.csv chunk_
for f in chunk_*; do process.sh "$f" > "$f.out" & done
wait
cat chunk_*.out > output.csv
rm chunk_*
```

## Performance Tips

1. **Sort optimization:**
   - Use `--parallel` and `-S` for large files
   - Set `TMPDIR` to fast storage
   - Use `-k` to sort by specific fields only

2. **Cut vs Awk:**
   - Use `cut` for simple column extraction
   - Use `awk` for complex field manipulation

3. **Pipe vs Temp Files:**
   - Use pipes for streaming
   - Use temp files for multiple passes

4. **Buffer control:**
   - Use `stdbuf -oL` for line-buffered output
   - Helps with real-time monitoring

## Summary

| Tool | Purpose | Key Use Case |
|------|---------|--------------|
| `cut` | Extract columns | Column selection |
| `paste` | Join files horizontally | Merge columns |
| `tr` | Character translation | Case conversion, deletion |
| `sort` | Order lines | Sorting, deduplication prep |
| `uniq` | Remove duplicates | Frequency counting |
| `split` | Divide files | Parallel processing |
| `pv` | Progress monitoring | Pipeline visibility |
| `stdbuf` | Buffer control | Real-time output |

## Next Steps
- Practice combining these tools in pipelines
- Explore `awk` for more complex transformations
- Learn `join` for database-like joins
- Study `comm` and `diff` for set operations
