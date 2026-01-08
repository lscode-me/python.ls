# Python in Pipelines: Hybrid Shell-Python Workflows - Quiz

## Questions

1. How do you read from stdin in Python line by line?
   - A) `input()`
   - B) `sys.stdin.read()`
   - C) `for line in sys.stdin:`
   - D) `readline()`

2. Why do you need `flush=True` in print() for pipelines?
   - A) To clear memory
   - B) To force immediate output without buffering
   - C) To format output
   - D) To flush errors

3. Which command runs Python script with unbuffered output?
   - A) `python3 -b script.py`
   - B) `python3 -u script.py`
   - C) `python3 --no-buffer script.py`
   - D) `python3 -f script.py`

4. How does pandas read from stdin?
   - A) `pd.read_csv()`
   - B) `pd.read_csv(sys.stdin)`
   - C) `pd.stdin()`
   - D) `pd.from_stdin()`

5. What's the main disadvantage of using pandas in pipelines?
   - A) Slow processing
   - B) Loads entire dataset into memory (not streaming)
   - C) Bad syntax
   - D) Limited functionality

6. Which library enables streaming JSON parsing in Python?
   - A) `json`
   - B) `jsonstream`
   - C) `ijson`
   - D) `streamjson`

7. What's the correct way to write CSV to stdout in Python?
   - A) `print(csv_data)`
   - B) `csv.writer(sys.stdout).writerows(data)`
   - C) `sys.stdout.write(csv)`
   - D) `output_csv(data)`

8. When should you use Python instead of awk in a pipeline?
   - A) Always
   - B) For complex logic (API calls, ML, regex)
   - C) Never
   - D) For simple filtering

9. How do you handle JSONDecodeError when parsing stdin?
   - A) Ignore it
   - B) `try: json.loads(line) except json.JSONDecodeError: pass`
   - C) Stop processing
   - D) Print error and exit

10. What's the memory complexity of streaming processing?
    - A) O(n) - grows with input size
    - B) O(1) - constant memory
    - C) O(log n)
    - D) O(n²)

11. Which is faster for simple CSV aggregation on large files?
    - A) Always pandas
    - B) Always CLI tools (mlr, awk)
    - C) Depends on data size (CLI usually faster and less memory)
    - D) Same speed

12. How do you make Python read CSV headers from stdin?
    - A) `csv.reader(sys.stdin)`
    - B) `csv.DictReader(sys.stdin)`
    - C) `sys.stdin.headers()`
    - D) `csv.read_headers()`

13. What does `sys.stdout.flush()` do?
    - A) Clears stdout
    - B) Forces Python to write buffered output immediately
    - C) Formats output
    - D) Closes stdout

14. How do you send JSON to stdout for piping to jq?
    - A) `print(data)`
    - B) `print(json.dumps(data), flush=True)`
    - C) `sys.stdout.json(data)`
    - D) `output(json(data))`

15. What's a hybrid pipeline?
    - A) Only Python
    - B) Only shell
    - C) Combination of shell and Python for their respective strengths
    - D) Multiple languages

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `for line in sys.stdin:` iterates line-by-line (also `sys.stdin.readlines()` works) |
| 2 | B | Python buffers output by default; `flush=True` writes immediately |
| 3 | B | `-u` flag forces unbuffered stdout/stderr |
| 4 | B | `pd.read_csv(sys.stdin)` reads CSV from stdin |
| 5 | B | pandas loads entire file into memory; not suitable for streaming large files |
| 6 | C | `ijson` parses JSON incrementally without loading entire file |
| 7 | B | `csv.writer(sys.stdout)` writes to stdout properly |
| 8 | B | Use Python for complex operations (APIs, libraries, logic); awk for simple transforms |
| 9 | B | Wrap in try-except to skip malformed lines gracefully |
| 10 | B | Streaming processes one item at a time: constant memory |
| 11 | C | CLI tools (mlr, awk) are usually faster and more memory-efficient for simple ops |
| 12 | B | `DictReader` parses headers automatically, returns dicts |
| 13 | B | Flushes Python's internal buffer to OS immediately |
| 14 | B | `json.dumps()` serializes, `flush=True` ensures immediate output |
| 15 | C | Hybrid uses shell for orchestration/simple ops, Python for complex logic |
