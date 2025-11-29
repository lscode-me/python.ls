# Performance & Parallelism

## Sample Data Files

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

---

## Overview
Optimize pipeline performance through parallelism, efficient sorting, and profiling.

## GNU Parallel

### Basic Parallel Execution
```bash
# Run commands in parallel
seq 1 10 | parallel echo "Processing {}"

# Process files
ls *.txt | parallel wc -l {}

# Multiple CPUs
seq 1 100 | parallel -j 4 heavy_computation.sh {}

# Keep order
seq 1 10 | parallel --keep-order echo {}
```

### Advanced Parallel Patterns
```bash
# With progress bar
seq 1 1000 | parallel --bar process.sh {}

# Retry failed jobs
parallel --retries 3 flaky_script.sh ::: {1..100}

# Load data from file
parallel -a urls.txt wget {}

# Argument combinations
parallel echo {1} {2} ::: A B C ::: 1 2 3
```

## xargs Parallel

```bash
# Basic parallel (-P for processes)
find . -name "*.txt" | xargs -P 4 -I {} wc -l {}

# Batch processing
seq 1 100 | xargs -P 4 -n 10 batch_process.sh

# With null delimiter
find . -name "*.csv" -print0 | xargs -0 -P 4 csvstat
```

## Sort Optimization

### Memory and Parallelism
```bash
# Use more memory
sort -S 2G large.txt

# Parallel sort
sort --parallel=4 large.txt

# Both
sort --parallel=4 -S 4G huge.txt

# Temporary directory (use fast SSD)
TMPDIR=/fast/tmp sort -S 4G huge.txt
```

### Efficient Sorting
```bash
# Sort by specific field only
sort -t',' -k3,3n data.csv

# Unique sort (faster than sort | uniq)
sort -u data.txt

# Numeric sort
sort -n numbers.txt

# Version sort (1.2.10 > 1.2.9)
sort -V versions.txt
```

## Profiling with time, dstat, pv

### time Command
```bash
# Measure execution time
time ./script.sh

# Detailed timing
/usr/bin/time -v ./script.sh

# Output format
/usr/bin/time -f "Time: %E\nMax RSS: %M KB" ./script.sh
```

### pv for Progress
```bash
# Show progress and throughput
pv large.csv | wc -l

# With rate limit
pv -L 1m source.dat > target.dat

# Progress bar
pv -W large.csv | gzip > large.csv.gz

# ETA
pv access.log | grep ERROR > errors.log
```

### iostat and vmstat
```bash
# I/O statistics
iostat -x 2

# Memory and CPU
vmstat 2

# Disk usage monitoring
iotop
```

## Practical Performance Examples

### Example 1: Parallel CSV Processing
```bash
# Split CSV, process in parallel, merge
split -l 10000 -d huge.csv chunk_
ls chunk_* | parallel -j 4 "mlr --csv stats1 -a sum -f amount {} > {}.stats"
cat chunk_*.stats > final_stats.csv
rm chunk_*
```

### Example 2: Parallel API Fetching
```bash
# Fetch 100 users in parallel (10 at a time)
seq 1 100 | parallel -j 10 \
  'curl -s "https://api.example.com/user/{}" | jq -c "."' > users.jsonl
```

### Example 3: Fast Find and Process
```bash
# Find and process files efficiently
find . -name "*.log" -print0 | \
  xargs -0 -P 8 -I {} sh -c 'grep ERROR {} | wc -l' | \
  awk '{sum += $1} END {print sum}'
```

### Example 4: Optimized Sort-Merge
```bash
# Sort large file with all optimizations
TMPDIR=/fast/ssd sort --parallel=8 -S 8G -t',' -k1,1 huge.csv > sorted.csv
```

## Bottleneck Identification

### CPU-Bound
```bash
# Monitor CPU usage
top
htop

# If CPU is bottleneck: use parallelism
parallel -j $(nproc) command ::: input
```

### I/O-Bound
```bash
# Monitor I/O
iostat -x 2
iotop

# If I/O is bottleneck:
# - Use faster storage (SSD)
# - Reduce I/O operations
# - Use compression
# - Batch operations
```

### Memory-Bound
```bash
# Monitor memory
free -h
vmstat 2

# If memory is bottleneck:
# - Stream data (don't load all)
# - Use external sort
# - Split and process
```

## Best Practices

1. **Profile first**: Identify bottleneck before optimizing
2. **Use parallel** for independent tasks
3. **Optimize sort**: Use `-S`, `--parallel`, fast `TMPDIR`
4. **Stream data**: Avoid loading everything in memory
5. **Batch operations**: Reduce overhead
6. **Monitor resources**: Use `time`, `pv`, `iostat`
7. **Test scalability**: Profile with different data sizes

## Performance Checklist

- [ ] Use `parallel` or `xargs -P` for parallelism
- [ ] Allocate more memory to sort with `-S`
- [ ] Use `--parallel` flag for sort
- [ ] Set `TMPDIR` to fast storage
- [ ] Add `pv` to monitor progress
- [ ] Profile with `/usr/bin/time -v`
- [ ] Monitor I/O with `iostat`
- [ ] Check memory with `free -h`
- [ ] Use compression for I/O-heavy tasks
- [ ] Batch API calls to reduce overhead

## Summary

| Tool | Purpose | Example |
|------|---------|---------|
| parallel | Parallel execution | `seq 1 100 \| parallel process {}` |
| xargs -P | Simple parallelism | `find . -name "*.txt" \| xargs -P 4 wc -l` |
| sort -S | Memory for sort | `sort -S 4G huge.txt` |
| sort --parallel | Parallel sort | `sort --parallel=8 large.txt` |
| pv | Progress monitor | `pv large.csv \| wc -l` |
| time | Profile execution | `time ./script.sh` |

## Next Steps
- Practice with GNU parallel
- Profile existing pipelines
- Optimize bottlenecks
- Study parallel algorithms
