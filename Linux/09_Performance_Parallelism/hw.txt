# Homework: Performance & Parallelism

## Assignment 1: Basic Parallel Execution
Use GNU parallel to process 100 files in parallel.
- Create 100 test files: `seq 1 100 | xargs -I {} touch file_{}.txt`
- Task: Count lines in each file and sum results
- Command: `ls file_*.txt | parallel wc -l {} | awk '{sum+=$1} END {print sum}'`
- Requirement: Use 4 parallel jobs with `-j 4`

## Assignment 2: Sort Optimization
Sort a large CSV file (100MB+) with optimization flags.
- Input: Generate test data with `seq 1 1000000 | awk '{print rand()","rand()","rand()}' > large.csv`
- Task: Sort by second column numerically
- Requirements:
  - Use `--parallel=4` for parallel sorting
  - Use `-S 2G` to allocate 2GB memory
  - Set `TMPDIR` to fast storage
  - Measure time with `/usr/bin/time -v`
- Compare: Sort with and without optimization, document speedup

## Assignment 3: Parallel API Fetching
Fetch data from JSONPlaceholder API in parallel.
- Task: Fetch users 1-50 from `https://jsonplaceholder.typicode.com/users/{id}`
- Requirements:
  - Use GNU parallel with `-j 10` (10 concurrent requests)
  - Add `--delay 0.1` to rate-limit (100ms between starts)
  - Save each response to `user_{id}.json`
  - Use `--bar` to show progress
- Command template: `seq 1 50 | parallel -j 10 --delay 0.1 --bar 'curl -s "https://jsonplaceholder.typicode.com/users/{}" > user_{}.json'`

## Assignment 4: xargs Parallelism
Use xargs with `-P` flag to process files in parallel.
- Task: Find all `.txt` files and count words in each
- Command: `find . -name "*.txt" -print0 | xargs -0 -P 4 -I {} wc -w {}`
- Requirements:
  - Use `-print0` and `-0` for safe filename handling
  - Process 4 files at a time
  - Aggregate total word count

## Assignment 5: Performance Profiling
Profile a pipeline to identify bottlenecks.
- Pipeline: `cat large.csv | grep "pattern" | sort | uniq -c | sort -rn > output.txt`
- Tasks:
  1. Use `/usr/bin/time -v` to measure overall performance
  2. Add `pv` to monitor throughput at each stage
  3. Document: CPU time, wall time, max memory (RSS)
  4. Identify bottleneck (CPU vs I/O bound)
- Hint: Use `time` on each component separately

## Assignment 6: CSV Split-Process-Merge
Implement parallel processing of a large CSV.
- Input: Create 100,000 line CSV: `seq 1 100000 | awk -F',' '{print NR","rand()*100","rand()*1000}' > data.csv`
- Steps:
  1. Split into 10 chunks: `split -l 10000 -d data.csv chunk_`
  2. Process each chunk in parallel (calculate sum of column 3)
  3. Merge results: sum all chunk totals
- Use: `ls chunk_* | parallel "mlr --csv stats1 -a sum -f 3 {} > {}.result"`
- Requirement: Show progress with `pv` or `--bar`

## Assignment 7: Optimized Grep
Speed up grep by using parallel processing.
- Task: Search for "ERROR" in 20 log files
- Compare:
  - Sequential: `grep "ERROR" *.log | wc -l`
  - Parallel: `ls *.log | parallel grep "ERROR" {} | wc -l`
  - Parallel with threads: `grep -r --include="*.log" "ERROR" .` (uses threads internally)
- Measure time for each approach
- Document: Which is fastest and why?

## Assignment 8: Memory-Efficient Sort
Sort a file larger than available RAM using external sort.
- Input: Generate 500MB file
- Task: Sort without loading entire file into memory
- Commands:
  - `sort --parallel=4 -S 100M huge.txt > sorted.txt` (limits memory to 100MB)
  - Set `TMPDIR=/fast/tmp` for temp files
- Monitor: Use `iostat -x 2` during sort to watch I/O
- Document: Temp file usage and I/O patterns

## Assignment 9: Parallel Data Download
Download multiple files in parallel with rate limiting.
- Task: Download 20 files from a website
- Requirements:
  - Use GNU parallel with `-j 5` (5 concurrent downloads)
  - Add retry logic: `--retries 3`
  - Show progress: `--bar`
  - Log errors: `2> errors.log`
- Example: `cat urls.txt | parallel -j 5 --retries 3 --bar wget -q {}`

## Assignment 10: Pipeline Optimization Challenge
Optimize a slow pipeline.
- Given pipeline:
  ```bash
  for file in *.csv; do
    cat "$file" | grep "active" | cut -d',' -f2 | sort | uniq >> results.txt
  done
  sort results.txt | uniq > final.txt
  ```
- Task: Rewrite using parallelism and optimization
- Requirements:
  - Use parallel processing
  - Eliminate unnecessary intermediate files
  - Use efficient sorting
  - Measure before/after performance
- Hint: `ls *.csv | parallel "grep active {} | cut -d',' -f2" | sort -u > final.txt`

## Bonus Challenges

### Bonus 1: Dynamic Load Balancing
Use GNU parallel's `--load` option to avoid overloading system.
- Task: Process 1000 tasks with automatic load balancing
- Command: `seq 1 1000 | parallel --load 80% --bar heavy_task.sh {}`
- Requirement: Parallel should pause when system load > 80%
- Monitor: Watch `uptime` or `htop` during execution

### Bonus 2: Parallel Pipeline with Named Pipes
Create a parallel pipeline using FIFOs.
- Architecture:
  ```
  Producer → FIFO1 → Worker1 ─┐
  Producer → FIFO2 → Worker2 ─┼→ Aggregator
  Producer → FIFO3 → Worker3 ─┘
  ```
- Implementation:
  - Create 3 named pipes
  - Distribute work among 3 workers
  - Aggregate results
- Use: Round-robin distribution or hash-based partitioning

### Bonus 3: Benchmark Sorting Algorithms
Compare performance of different sort optimizations.
- Test cases:
  1. Default sort: `sort data.txt`
  2. Parallel sort: `sort --parallel=8 data.txt`
  3. Memory-optimized: `sort --parallel=8 -S 4G data.txt`
  4. Fast TMPDIR: `TMPDIR=/fast/ssd sort --parallel=8 -S 4G data.txt`
- Measure: Time, memory, I/O for each
- Graph: Create comparison chart (ASCII or real chart)

### Bonus 4: Parallel Log Analysis
Analyze 1 year of logs (365 files) in parallel.
- Task: Extract statistics from each log file
  - Total requests
  - Error count
  - Unique IPs
  - Average response time
- Requirements:
  - Process all files in parallel
  - Generate daily statistics
  - Aggregate into monthly summary
  - Create markdown report
- Use: GNU parallel for per-file processing, mlr for aggregation

### Bonus 5: Resource-Aware Parallel Execution
Create a script that adapts parallelism based on available resources.
- Auto-detect:
  - Number of CPU cores: `nproc`
  - Available memory: `free -m`
  - Current load: `uptime`
- Logic:
  ```bash
  CPUS=$(nproc)
  LOAD=$(uptime | awk '{print $(NF-2)}' | sed 's/,//')
  if (( $(echo "$LOAD < $CPUS * 0.7" | bc -l) )); then
    JOBS=$CPUS
  else
    JOBS=$(( CPUS / 2 ))
  fi
  parallel -j $JOBS command {}
  ```
- Test: Run under different load conditions

## Submission Guidelines

### Required Deliverables
1. **All scripts and commands** used for each assignment
2. **Performance measurements**:
   - Execution time (wall clock and CPU time)
   - Memory usage (peak RSS)
   - I/O statistics (if applicable)
3. **Before/after comparisons** for optimization tasks
4. **Documentation**:
   - What was the bottleneck?
   - What optimization was applied?
   - What was the speedup achieved?

### Performance Report Template
```markdown
## Assignment X: [Title]

### Original Approach
- Command: `...`
- Time: X.XX seconds
- Memory: XXX MB
- CPU usage: XX%

### Optimized Approach
- Command: `...`
- Time: X.XX seconds
- Memory: XXX MB
- CPU usage: XX%

### Speedup
- Time improvement: XX%
- Analysis: [Why was it faster?]
```

### Testing Requirements
- Test on datasets of varying sizes: 1MB, 100MB, 1GB
- Run each test 3 times, report average
- Use consistent hardware for all tests
- Document: CPU cores, RAM, disk type (HDD/SSD)

### Bonus Points For
- Automated benchmarking scripts
- Visualization of performance metrics
- Comparison with alternative approaches
- Real-world use case examples
- Creative optimization techniques
