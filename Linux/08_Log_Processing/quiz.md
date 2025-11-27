# Quiz: Log Processing

## Questions

1. What is the main advantage of JSONL format for logs?
   - A) Smaller file size
   - B) One JSON object per line, easy to stream
   - C) Better compression
   - D) Faster parsing

2. Which command streams a gzip-compressed file without decompressing it to disk?
   - A) `gunzip logs.gz | cat`
   - B) `zcat logs.gz`
   - C) `cat logs.gz | gunzip`
   - D) `gzip -d logs.gz | less`

3. How do you filter JSONL entries where level equals "ERROR"?
   - A) `jq 'filter(.level == "ERROR")' app.jsonl`
   - B) `jq -c 'select(.level == "ERROR")' app.jsonl`
   - C) `grep '"level":"ERROR"' app.jsonl`
   - D) Both B and C

4. Which curl option makes the output silent (no progress bar)?
   - A) `-q`
   - B) `-s`
   - C) `-silent`
   - D) `-n`

5. How do you process multiple gzip files in one pipeline?
   - A) `zcat file1.gz file2.gz file3.gz | grep ERROR`
   - B) `zcat *.gz | grep ERROR`
   - C) Both A and B
   - D) `cat *.gz | gunzip | grep ERROR`

6. What's the correct markdown table row format?
   - A) `[Name] [Age] [City]`
   - B) `| Name | Age | City |`
   - C) `Name,Age,City`
   - D) `Name\tAge\tCity`

7. How do you fetch JSON from an API and pretty-print it?
   - A) `curl 'https://api.example.com/data' | json`
   - B) `curl -s 'https://api.example.com/data' | jq '.'`
   - C) `wget 'https://api.example.com/data' | jq`
   - D) `http 'https://api.example.com/data'`

8. Which command adds 0.5 second delay between API requests?
   - A) `wait 0.5`
   - B) `sleep 0.5`
   - C) `delay 500`
   - D) `pause 0.5`

9. How do you group JSONL entries by a field and count them?
   - A) `jq '.field' file.jsonl | sort | uniq -c`
   - B) `jq -r '.field' file.jsonl | sort | uniq -c`
   - C) Both A and B
   - D) `jq -s 'group_by(.field) | map(length)' file.jsonl`

10. What's the best format for streaming logs?
    - A) Pretty-printed JSON with newlines
    - B) JSONL (one object per line)
    - C) XML
    - D) CSV

---

## Answer Key
1. B - JSONL has one object per line, perfect for streaming with `grep`, `jq -c`
2. B - `zcat` streams gzip to stdout without extracting
3. D - Both `jq -c select()` and `grep` work (jq is more reliable)
4. B - `-s` flag silences curl progress bar
5. C - Both `zcat file1.gz file2.gz` and `zcat *.gz` work
6. B - Markdown table row format is `| val | val | val |`
7. B - `curl -s` fetches silently, `jq '.'` pretty-prints
8. B - `sleep N` delays for N seconds (accepts decimals)
9. B - `-r` for raw output, then `sort | uniq -c`
10. B - JSONL is standard for streaming logs
