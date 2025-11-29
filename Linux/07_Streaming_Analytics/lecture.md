# Streaming Analytics: Join, Group-By, Map/Reduce

## Overview
Perform database-like operations on streams: joins, aggregations, group-by operations, and map/reduce patterns.

## Sample Data Files

📁 **[Sample Data](../data/DataSamples.md)** — sample data files for practice

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

## DuckDB for Analytics

DuckDB provides SQL interface for complex analytical queries on files. Perfect for joins, aggregations, and window functions.

### Analytical Joins
```bash
# Inner join with aggregation
duckdb -c "
  SELECT 
    u.name,
    u.city,
    COUNT(o.order_id) as order_count,
    SUM(o.amount) as total_spent
  FROM 'users.csv' u
  JOIN 'orders.csv' o ON u.id = o.customer_id
  GROUP BY u.name, u.city
  ORDER BY total_spent DESC
"

# Multi-way join
duckdb -c "
  SELECT 
    u.name,
    p.name as product,
    o.quantity,
    o.amount,
    o.date
  FROM 'orders.csv' o
  JOIN 'users.csv' u ON o.customer_id = u.id
  JOIN 'products.csv' p ON o.product_id = p.id
  WHERE u.status = 'active'
"

# Self-join for comparisons
duckdb -c "
  SELECT 
    a.name as product1,
    b.name as product2,
    a.price - b.price as price_diff
  FROM 'products.csv' a
  JOIN 'products.csv' b ON a.category = b.category
  WHERE a.id < b.id
"
```

### Complex Aggregations
```bash
# Multiple aggregations per group
duckdb -c "
  SELECT 
    category,
    COUNT(*) as product_count,
    MIN(price) as min_price,
    MAX(price) as max_price,
    AVG(price) as avg_price,
    STDDEV(price) as price_stddev,
    SUM(price) as total_value
  FROM 'products.csv'
  GROUP BY category
"

# Conditional aggregations
duckdb -c "
  SELECT 
    customer_id,
    COUNT(*) as total_orders,
    COUNT(CASE WHEN amount > 500 THEN 1 END) as large_orders,
    AVG(amount) as avg_order_value,
    SUM(CASE WHEN date >= '2024-03-17' THEN amount ELSE 0 END) as recent_revenue
  FROM 'orders.csv'
  GROUP BY customer_id
"

# HAVING clause for filtered aggregations
duckdb -c "
  SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(amount) as total_spent
  FROM 'orders.csv'
  GROUP BY customer_id
  HAVING COUNT(*) >= 2 AND SUM(amount) > 1000
"
```

### Window Functions
```bash
# Row number and ranking
duckdb -c "
  SELECT 
    name,
    category,
    price,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as rank,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) as dense_rank
  FROM 'products.csv'
"

# Running totals
duckdb -c "
  SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg_3
  FROM 'orders.csv'
  ORDER BY date
"

# LAG and LEAD for time-series
duckdb -c "
  SELECT 
    date,
    customer_id,
    amount,
    LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY date) as prev_order,
    LEAD(amount, 1) OVER (PARTITION BY customer_id ORDER BY date) as next_order,
    amount - LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY date) as change
  FROM 'orders.csv'
"

# Percentiles within groups
duckdb -c "
  SELECT 
    category,
    name,
    price,
    PERCENT_RANK() OVER (PARTITION BY category ORDER BY price) as price_percentile
  FROM 'products.csv'
"
```

### Advanced Patterns
```bash
# Top-N per group
duckdb -c "
  WITH ranked AS (
    SELECT 
      category,
      name,
      price,
      ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as rn
    FROM 'products.csv'
  )
  SELECT category, name, price
  FROM ranked
  WHERE rn <= 2
"

# Pivot with CASE WHEN
duckdb -c "
  SELECT 
    customer_id,
    SUM(CASE WHEN product_id = 1 THEN quantity ELSE 0 END) as phone_count,
    SUM(CASE WHEN product_id = 2 THEN quantity ELSE 0 END) as laptop_count,
    SUM(CASE WHEN product_id = 3 THEN quantity ELSE 0 END) as shirt_count
  FROM 'orders.csv'
  GROUP BY customer_id
"

# Gap analysis
duckdb -c "
  WITH date_series AS (
    SELECT UNNEST(GENERATE_SERIES(
      DATE '2024-03-15',
      DATE '2024-03-19',
      INTERVAL 1 DAY
    )) as date
  )
  SELECT 
    ds.date,
    COALESCE(COUNT(o.order_id), 0) as order_count
  FROM date_series ds
  LEFT JOIN 'orders.csv' o ON ds.date = o.date
  GROUP BY ds.date
  ORDER BY ds.date
"
```

### Streaming from stdin
```bash
# Process piped data
cat orders.csv | duckdb -c "
  SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(amount) as total
  FROM read_csv_auto('/dev/stdin')
  GROUP BY customer_id
"

# Chain with other tools
grep "active" users.csv | duckdb -c "
  SELECT city, COUNT(*) 
  FROM read_csv_auto('/dev/stdin')
  GROUP BY city
" -markdown
```

### Materialized Results
```bash
# Create temporary database with results
duckdb temp.db <<EOF
CREATE TABLE user_stats AS
  SELECT 
    u.id,
    u.name,
    COUNT(o.order_id) as order_count,
    SUM(o.amount) as lifetime_value
  FROM read_csv_auto('users.csv') u
  LEFT JOIN read_csv_auto('orders.csv') o ON u.id = o.customer_id
  GROUP BY u.id, u.name;

-- Query the materialized table
SELECT * FROM user_stats WHERE lifetime_value > 1000;

-- Export results
COPY user_stats TO 'user_stats.csv' (HEADER);
EOF

# Remove temp database
rm temp.db
```

### Performance Tips
```bash
# Use COPY for large exports (faster than SELECT)
duckdb -c "COPY (
  SELECT u.*, COUNT(o.order_id) as orders
  FROM 'users.csv' u
  LEFT JOIN 'orders.csv' o ON u.id = o.customer_id
  GROUP BY u.id, u.name, u.email, u.city, u.status
) TO 'user_orders.csv'"

# Use Parquet for intermediate results (compressed, columnar)
duckdb -c "COPY (
  SELECT * FROM 'large_file.csv' WHERE status = 'active'
) TO 'filtered.parquet' (FORMAT PARQUET)"

# Read Parquet in next step (much faster)
duckdb -c "SELECT * FROM 'filtered.parquet'"
```

### DuckDB vs Traditional Tools

| Operation | Traditional | DuckDB |
|-----------|-------------|--------|
| Join 2 files | `mlr --csv join -f left.csv -j id right.csv` | `duckdb -c "SELECT * FROM 'left.csv' l JOIN 'right.csv' r ON l.id=r.id"` |
| Group-by sum | `mlr --csv stats1 -a sum -f amount -g customer orders.csv` | `duckdb -c "SELECT customer, SUM(amount) FROM 'orders.csv' GROUP BY customer"` |
| Top-N | `mlr --csv sort -nr amount \| head -5` | `duckdb -c "SELECT * FROM 'data.csv' ORDER BY amount DESC LIMIT 5"` |
| Window function | Complex awk script | `duckdb -c "SELECT *, LAG(value) OVER (ORDER BY date) FROM 'data.csv'"` |

### When to Use DuckDB

**Use DuckDB for:**
- ✅ Complex multi-way joins
- ✅ Window functions (LAG, LEAD, ROW_NUMBER)
- ✅ Advanced aggregations (percentiles, stddev)
- ✅ Large datasets (GB+) with columnar efficiency
- ✅ SQL-familiar teams
- ✅ Reusable analytical queries

**Use traditional tools (awk/mlr) for:**
- ✅ Simple filters and transformations
- ✅ Quick one-liners
- ✅ Streaming processing
- ✅ When SQL is overkill

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
| Join (SQL) | DuckDB | `duckdb -c "SELECT * FROM 'left.csv' l JOIN 'right.csv' r ON l.id=r.id"` |
| Group-By | mlr | `mlr --csv stats1 -a sum -f amount -g customer` |
| Group-By (SQL) | DuckDB | `duckdb -c "SELECT customer, SUM(amount) FROM 'orders.csv' GROUP BY customer"` |
| Aggregation | datamash | `datamash -t',' -s -g 1 sum 3` |
| Hash Join | awk | `awk 'NR==FNR {h[$1]=$2;next} {print $0,h[$1]}'` |
| Window Functions | DuckDB | `duckdb -c "SELECT *, LAG(value) OVER (ORDER BY date) FROM 'data.csv'"` |

## Next Steps
- Practice join operations on real datasets
- Master DuckDB window functions (LAG, LEAD, ROW_NUMBER)
- Compare DuckDB performance vs traditional tools
- Implement window functions with awk for streaming
- Study distributed map/reduce (Hadoop, Spark)
- Explore columnar formats (Parquet, Arrow)
