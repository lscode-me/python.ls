# Performance & Parallelism - Quiz

## Questions

## Question 1: Which flag controls the number

Which flag controls the number of parallel jobs in GNU parallel?

A) `-n`
B) `-j`
C) `-p`
D) `--jobs`


## Question 2: What does do

What does `sort -S 4G` do?

A) Sorts 4GB of data
B) Saves output to 4G file
C) Allocates 4GB of memory for sorting
D) Splits into 4GB chunks


## Question 3: Which command shows progress and

Which command shows progress and throughput in a pipeline?

A) `time`
B) `top`
C) `pv`
D) `watch`


## Question 4: How do you enable parallel

How do you enable parallel sorting with 8 threads?

A) `sort -j 8`
B) `sort -t 8`
C) `sort --threads=8`
D) `sort --parallel=8`


## Question 5: What does do

What does `xargs -P 4` do?

A) Processes 4 arguments at a time
B) Uses 4 parallel processes
C) Prints 4 items
D) Paginates with 4 items per page


## Question 6: Which environment variable sets the

Which environment variable sets the temporary directory for sort?

A) `SORTDIR`
B) `TMPDIR`
C) `TEMPDIR`
D) `TEMP`


## Question 7: What does show

What does `/usr/bin/time -v` show?

A) Current time
B) Verbose output only
C) Detailed resource usage (CPU, memory, I/O)
D) Version information


## Question 8: How do you rate-limit GNU

How do you rate-limit GNU parallel to start 1 job every 0.5 seconds?

A) `parallel --rate 0.5`
B) `parallel --delay 0.5`
C) `parallel --limit 0.5`
D) `parallel --wait 0.5`


## Question 9: What indicates a CPU-bound process

What indicates a CPU-bound process?

A) High CPU usage, low I/O wait
B) Low CPU usage, high I/O wait
C) High memory usage
D) High network usage


## Question 10: Which flag makes GNU parallel

Which flag makes GNU parallel show a progress bar?

A) `-p`
B) `--progress`
C) `--bar`
D) Both B and C


## Question 11: What does do

What does `sort -u` do?

A) Sort in uppercase
B) Sort and remove duplicates (unique)
C) Unix line endings
D) User-defined sort


## Question 12: How do you retry failed

How do you retry failed jobs 3 times in GNU parallel?

A) `--retry 3`
B) `--retries 3`
C) `-r 3`
D) `--tries 3`


## Question 13: Whats the difference between and

What's the difference between `time` and `/usr/bin/time -v`?

A) No difference
B) Shell builtin vs external command with detailed stats
C) One is faster
D) Different time formats


## Question 14: Which tool monitors IO statistics

Which tool monitors I/O statistics in real-time?

A) `top`
B) `ps`
C) `iostat`
D) `vmstat`


## Question 15: What does do

What does `parallel --load 80%` do?

A) Uses 80% CPU
B) Loads 80% of data
C) Pauses when system load exceeds 80% of CPU cores
D) Limits to 80% memory


---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `-j N` controls parallel jobs (e.g., `parallel -j 4`) |
| 2 | A | `-S` allocates memory buffer for sort |
| 3 | C | `pv` (Pipe Viewer) shows progress and throughput |
| 4 | C | `--parallel=N` enables N-threaded sorting |
| 5 | A | `-P N` runs N processes in parallel |
| 6 | B | `TMPDIR` sets temporary directory for sort and other tools |
| 7 | C | `-v` (verbose) shows CPU time, memory, I/O, page faults |
| 8 | C | `--delay` adds delay between job starts for rate limiting |
| 9 | A | CPU-bound = high CPU, low I/O; I/O-bound = opposite |
| 10 | A | Both `--progress` and `--bar` show progress (bar is newer) |
| 11 | B | `-u` sorts and keeps only unique lines (faster than `sort | uniq`) |
| 12 | D | `--retries N` retries failed jobs N times |
| 13 | D | `time` is shell builtin (basic), `/usr/bin/time -v` is external (detailed) |
| 14 | C | `iostat -x 2` monitors I/O statistics every 2 seconds |
| 15 | C | `--load` pauses new jobs when load average is high |
