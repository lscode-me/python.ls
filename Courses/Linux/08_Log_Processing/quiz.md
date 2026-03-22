# Log Processing & Real-World Pipelines - Quiz

## Questions

## Question 1: What is the main advantage

What is the main advantage of JSONL format for logs?

A) Smaller file size
B) One JSON object per line, easy to stream
C) Better compression
D) Faster parsing


## Question 2: Which command streams a gzip-compressed

Which command streams a gzip-compressed file without decompressing it to disk?

A) `gunzip logs.gz | cat`
B) `zcat logs.gz`
C) `cat logs.gz | gunzip`
D) `gzip -d logs.gz | less`


## Question 3: How do you filter JSONL

How do you filter JSONL entries where level equals "ERROR"?

A) `jq 'filter(.level == "ERROR")' app.jsonl`
B) `jq -c 'select(.level == "ERROR")' app.jsonl`
C) `grep '"level":"ERROR"' app.jsonl`
D) Both B and C


## Question 4: Which curl option makes the

Which curl option makes the output silent (no progress bar)?

A) `-q`
B) `-s`
C) `-silent`
D) `-n`


## Question 5: How do you process multiple

How do you process multiple gzip files in one pipeline?

A) `zcat file1.gz file2.gz file3.gz | grep ERROR`
B) `zcat *.gz | grep ERROR`
C) Both A and B
D) `cat *.gz | gunzip | grep ERROR`


## Question 6: Whats the correct markdown table

What's the correct markdown table row format?

A) `[Name] [Age] [City]`
B) `| Name | Age | City |`
C) `Name,Age,City`
D) `Name\tAge\tCity`


## Question 7: How do you fetch JSON

How do you fetch JSON from an API and pretty-print it?

A) `curl 'https://api.example.com/data' | json`
B) `curl -s 'https://api.example.com/data' | jq '.'`
C) `wget 'https://api.example.com/data' | jq`
D) `http 'https://api.example.com/data'`


## Question 8: Which command adds 05 second

Which command adds 0.5 second delay between API requests?

A) `wait 0.5`
B) `sleep 0.5`
C) `delay 500`
D) `pause 0.5`


## Question 9: How do you group JSONL

How do you group JSONL entries by a field and count them?

A) `jq '.field' file.jsonl | sort | uniq -c`
B) `jq -r '.field' file.jsonl | sort | uniq -c`
C) Both A and B
D) `jq -s 'group_by(.field) | map(length)' file.jsonl`


## Question 10: Whats the best format for

What's the best format for streaming logs?

A) Pretty-printed JSON with newlines
B) JSONL (one object per line)
C) XML
D) CSV


## Question 11: Which command decompresses xz-compressed...

Which command decompresses xz-compressed logs and searches for errors?

A) `xzcat logs.xz | grep ERROR`
B) `xz -d logs.xz | grep ERROR`
C) `unxz logs.xz && grep ERROR logs`
D) `zcat logs.xz | grep ERROR`


## Question 12: How do you use to

How do you use `tee` to save API response while processing it?

A) `curl -s 'api.com' | tee response.json | jq '.'`
B) `curl -s 'api.com' > tee response.json | jq '.'`
C) `curl -s 'api.com' | save response.json | jq '.'`
D) `curl -s 'api.com' && tee response.json | jq '.'`


## Question 13: What does do

What does `jq -s 'group_by(.level) | map({level: .[0].level, count: length})'` do?

A) Sorts by level
B) Filters by level
C) Groups JSONL entries by level and counts each group
D) Selects only the level field


## Question 14: How do you compress pipeline

How do you compress pipeline output on the fly?

A) `command | gzip > output.gz`
B) `command > output.txt && gzip output.txt`
C) `command | compress > output.gz`
D) `command --gzip > output.gz`


## Question 15: Whats the correct way to

What's the correct way to generate a markdown heading with a variable date?

A) `echo "# Report - $(date +%Y-%m-%d)"`
B) `echo "# Report - {date}"`
C) `printf "# Report - %s" date`
D) `echo "# Report - $date"`


---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | JSONL has one object per line, perfect for streaming with `grep`, `jq -c` |
| 2 | B | `zcat` streams gzip to stdout without extracting |
| 3 | D | Both `jq -c select()` and `grep` work (jq is more reliable) |
| 4 | B | `-s` flag silences curl progress bar |
| 5 | C | Both `zcat file1.gz file2.gz` and `zcat *.gz` work |
| 6 | B | Markdown table row format is `| val | val | val |` |
| 7 | B | `curl -s` fetches silently, `jq '.'` pretty-prints |
| 8 | B | `sleep N` delays for N seconds (accepts decimals) |
| 9 | B | `-r` for raw output, then `sort | uniq -c` |
| 10 | B | JSONL is standard for streaming logs |
| 11 | A | `xzcat` decompresses xz files to stdout (like `zcat` for gzip) |
| 12 | A | `tee` writes to file and passes through to stdout for further processing |
| 13 | C | `-s` slurps all inputs into array, `group_by` groups by field, `map` aggregates counts |
| 14 | A | Pipe directly to `gzip` to compress output as it's generated |
| 15 | A | Use command substitution `$(date +%Y-%m-%d)` to embed current date |

---

## Scoring Guide

- **13-15 correct**: Excellent! You're ready for production log processing.
- **10-12 correct**: Good job! Review compression tools and jq aggregations.
- **7-9 correct**: Fair understanding. Practice more with JSONL and API workflows.
- **Below 7**: Study the lecture materials and complete hands-on exercises.
