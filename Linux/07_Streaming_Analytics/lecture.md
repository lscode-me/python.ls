# Streaming Analytics: Join, Group-By, Map/Reduce

## Overview
Perform database-like operations on streams: joins, aggregations, group-by operations, and map/reduce patterns.

## Sample Data Files

📁 **[DataSamples.md](DataSamples.md)** — sample data files for practice (customers.csv, orders.csv, events.jsonl, etc.)

---

## Stream Joins

### Using `join` Command
```bash
# Inner join on first field
sort -k1 file1.txt > sorted1.txt
sort -k1 file2.txt > sorted2.txt
join sorted1.txt sorted2.txt

# Join CSV files
join -t',' -1 1 -2 1 sorted1.csv sorted2.csv

# Left outer join
join -a1 -t',' sorted1.csv sorted2.csv
```

### Using Miller (mlr)
```bash
# Inner join
mlr --csv join -f left.csv -j id right.csv

# Left join
mlr --csv join --ul -f left.csv -j id right.csv

# Multiple join keys
mlr --csv join -f left.csv -j id,date right.csv
```

### Using awk for Hash Joins
```bash
# Load second file into hash, join with first
awk -F',' 'NR==FNR {a[$1]=$2; next} $1 in a {print $0","a[$1]}' lookup.csv data.csv
```

## Group-By Aggregations

### Using awk
```bash
# Sum by group
awk -F',' '{sum[$1] += $3} END {for (k in sum) print k, sum[k]}' data.csv

# Count by group
awk -F',' '{count[$2]++} END {for (k in count) print k, count[k]}' data.csv

# Multiple aggregations
awk -F',' '{
    sum[$1] += $3
    count[$1]++
}
END {
    for (k in sum) print k, sum[k], count[k], sum[k]/count[k]
}' data.csv
```

### Using Miller
```bash
# Sum by group
mlr --csv stats1 -a sum -f amount -g customer_id orders.csv

# Multiple aggregations
mlr --csv stats1 -a sum,mean,count -f amount -g customer_id orders.csv

# Top-K per group
mlr --csv top -n 5 -f amount -g category products.csv
```

### Using datamash
```bash
# Group by and sum
datamash -t',' -s -g 1 sum 3 < data.csv

# Multiple operations
datamash -t',' -s -g 1 sum 3 mean 3 count 3 < data.csv

# Transpose
datamash -t',' transpose < matrix.csv
```

## Map/Reduce Patterns

### Map Phase: Transform Each Record
```bash
# Extract and transform
cat events.jsonl | \
  jq -c '{user: .user_id, value: .amount, hour: .timestamp[:13]}'
```

### Reduce Phase: Aggregate
```bash
# Group and sum
cat transformed.jsonl | \
  jq -s 'group_by(.hour) | map({hour: .[0].hour, total: map(.value) | add})'
```

### Full Map/Reduce Pipeline
```bash
# Count events per user per hour
cat events.jsonl | \
  jq -c '{user: .user_id, hour: .timestamp[:13]}' | \
  sort | uniq -c | \
  awk '{print $2, $1}' | \
  jq -Rn '[inputs | split(" ") | {user: .[0], hour: .[1], count: .[2]|tonumber}]'
```

## Window Functions

### Rolling Aggregations
```bash
# 5-line moving average
awk '{
    sum += $1
    arr[NR] = $1
    if (NR > 5) sum -= arr[NR-5]
    if (NR >= 5) print sum/5
    else print sum/NR
}' numbers.txt
```

### Running Totals
```bash
# Cumulative sum
awk '{sum += $1; print $0, sum}' data.txt
```

## Streaming Analytics Examples

### Example 1: Top Products by Revenue
```bash
mlr --csv stats1 -a sum -f revenue -g product sales.csv | \
  mlr --csv sort -nr revenue_sum | \
  head -10
```

### Example 2: User Session Analytics
```bash
# Group events by session, calculate metrics
cat events.jsonl | \
  jq -c '{session: .session_id, duration: .duration, pages: .page_count}' | \
  jq -s 'group_by(.session) | map({
    session: .[0].session,
    total_duration: map(.duration) | add,
    total_pages: map(.pages) | add,
    event_count: length
  })'
```

### Example 3: Time-Series Aggregation
```bash
# Events per minute
cat access.log | \
  awk '{print substr($4, 2, 16)}' | \
  sort | uniq -c | \
  sort -k2
```

### Example 4: Cohort Analysis
```bash
# Users by signup month and activity month
awk -F',' '
NR > 1 {
    signup_month = substr($2, 1, 7)
    activity_month = substr($3, 1, 7)
    cohort[signup_month][activity_month]++
}
END {
    for (sm in cohort) {
        for (am in cohort[sm]) {
            print sm, am, cohort[sm][am]
        }
    }
}' user_activity.csv
```

## Performance Patterns

### Pre-Aggregation
```bash
# Aggregate before joining (reduces join size)
mlr --csv stats1 -a sum -f amount -g customer_id orders.csv > order_totals.csv
mlr --csv join -f customers.csv -j customer_id order_totals.csv
```

### Hash Join vs Sort-Merge
```bash
# Hash join (awk): Fast for small lookup tables
# Sort-merge (join): Better for large sorted files
```

### Streaming Group-By
```bash
# Assumes sorted input, processes in constant memory
sort -k1 data.csv | \
  awk -F',' '
    $1 != prev {
        if (NR > 1) print prev, sum
        prev = $1
        sum = 0
    }
    {sum += $3}
    END {print prev, sum}
  '
```

## Best Practices

1. **Sort before join** for `join` command
2. **Use hash joins** (awk) for small lookup tables
3. **Pre-aggregate** before expensive operations
4. **Use Miller** for complex CSV operations
5. **Stream when possible** to avoid memory issues
6. **Index large datasets** before repeated queries
7. **Profile queries** to find bottlenecks

## Summary

| Operation | Tool | Command |
|-----------|------|---------|
| Join | mlr | `mlr --csv join -f left.csv -j id right.csv` |
| Group-By | mlr | `mlr --csv stats1 -a sum -f amount -g customer` |
| Aggregation | datamash | `datamash -t',' -s -g 1 sum 3` |
| Hash Join | awk | `awk 'NR==FNR {h[$1]=$2;next} {print $0,h[$1]}'` |

## Next Steps
- Practice join operations on real datasets
- Implement window functions
- Study distributed map/reduce (Hadoop, Spark)
- Explore SQL-like tools (q, textql)
