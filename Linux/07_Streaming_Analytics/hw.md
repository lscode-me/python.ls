# Homework: Streaming Analytics

## Assignment 1: Inner Join
Join two CSV files on a common ID column.
- Input: `customers.csv` (id,name), `orders.csv` (order_id,customer_id,amount)
- Command: Sort and use `join` or `mlr join`
- Output: Combined data

## Assignment 2: Group-By Sum
Calculate total orders per customer.
- Input: `orders.csv`
- Command: `mlr --csv stats1 -a sum -f amount -g customer_id orders.csv`
- Output: customer_id, amount_sum

## Assignment 3: Top-K by Group
Find top 3 products by revenue in each category.
- Input: `sales.csv` (product,category,revenue)
- Use: `mlr --csv top -n 3 -f revenue -g category`

## Assignment 4: Hash Join with awk
Implement a hash join using awk.
- Input: `lookup.csv` (id,name), `data.csv` (id,value)
- Load lookup into hash, join with data
- Hint: `awk 'NR==FNR {h[$1]=$2;next} {print $0","h[$1]}'`

## Assignment 5: Running Total
Calculate cumulative sum of a column.
- Input: `daily_sales.txt` (one number per line)
- Command: `awk '{sum += $1; print $0, sum}'`
- Output: Original value and running total

## Assignment 6: Moving Average
Calculate 5-day moving average.
- Input: `prices.txt`
- Use: awk with circular buffer
- Output: Moving average for each day

## Assignment 7: Aggregate JSON Stream
From JSONL events, calculate total revenue per user.
- Input: `events.jsonl` with user_id and amount
- Use: jq with `-s` and `group_by`
- Output: user_id, total_amount

## Assignment 8: Time-Series Aggregation
Count events per hour from log file.
- Input: `access.log`
- Extract hour from timestamp
- Use: `awk` to extract, `sort | uniq -c`

## Assignment 9: Multi-Key Aggregation
Calculate average order value per customer per month.
- Input: `orders.csv` (customer_id, date, amount)
- Group by customer_id and month
- Calculate average
- Use: mlr or awk

## Assignment 10: Left Outer Join
Perform left outer join to find customers with no orders.
- Input: `customers.csv`, `orders.csv`
- Use: `mlr --csv join --ul -f customers.csv -j id orders.csv`
- Filter for NULL order_id

## DuckDB Analytics Assignments

### Assignment 11: Multi-Way Join with DuckDB
Join users, orders, and products in one query.
- Input: `users.csv`, `orders.csv`, `products.csv`
- Command: Three-way join using DuckDB
- Output: Complete order details with customer and product names
- Hint: `SELECT u.name, p.name as product, o.amount FROM 'users.csv' u JOIN 'orders.csv' o ON ... JOIN 'products.csv' p ON ...`

### Assignment 12: Window Functions - Ranking
Rank products by price within each category.
- Input: `products.csv`
- Use: `ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC)`
- Output: Products with rank column

### Assignment 13: Running Totals with DuckDB
Calculate cumulative revenue per customer over time.
- Input: `orders.csv`
- Use: `SUM(amount) OVER (PARTITION BY customer_id ORDER BY date)`
- Output: Each order with running total

### Assignment 14: Top-N per Group
Find top 2 most expensive products in each category.
- Input: `products.csv`
- Use: CTE with ROW_NUMBER and WHERE clause
- Output: Top 2 products per category

### Assignment 15: Time-Series Analytics
Analyze daily order trends.
- Input: `orders.csv`
- Calculate: daily totals, moving averages, day-over-day changes
- Use: LAG function for previous day comparison
- Output: Daily analytics report

### Assignment 16: Percentile Calculations
Calculate price percentiles per category.
- Input: `products.csv`
- Use: `PERCENTILE_CONT(0.5)` for median, `PERCENTILE_CONT(0.95)` for 95th percentile
- Output: Category-level price statistics

## Bonus Challenges

### Bonus 1: Cohort Analysis
Calculate user retention by signup cohort.
- Input: User activity data with signup_date and activity_date
- Group by signup_month and activity_month
- Count active users per cohort

### Bonus 2: Window Function - Rank
Rank products by sales within each category.
- Add rank column (1 = highest sales in category)
- Use awk or mlr

### Bonus 3: Self-Join
Find pairs of products often bought together.
- Input: `transactions.csv` (transaction_id, product_id)
- Join table with itself on transaction_id
- Count product pairs

### Bonus 4: Pivot Table
Create pivot table: rows=products, columns=months, values=sum of sales.
- Input: `sales.csv` (date, product, amount)
- Output: Matrix with products and monthly totals
- Use: awk with 2D hash

### Bonus 5: Streaming Percentiles
Calculate median and 95th percentile from streaming data.
- Use: qsort or approximate algorithms
- Implement in awk

### Bonus 6: DuckDB vs awk Performance
Compare DuckDB and awk for large dataset:
- Create 10M row CSV file
- Perform complex aggregation (multi-key GROUP BY)
- Measure time and memory
- Document when to use each tool

### Bonus 7: Complex Window Analytics
Implement advanced analytics pipeline:
- Calculate customer lifetime value (CLV)
- Identify churn patterns (gaps in order dates)
- Rank customers by recency, frequency, monetary value (RFM)
- Use multiple window functions in single query
- Input: `orders.csv`
- Output: Customer analytics table

### Bonus 8: Gap Analysis with GENERATE_SERIES
Find missing dates in time series data.
- Generate complete date range
- LEFT JOIN with actual data
- Identify gaps (dates with no orders)
- Use: `GENERATE_SERIES` and `UNNEST` in DuckDB
- Output: Report of inactive days

## Submission Guidelines
- Submit all commands and scripts
- Include sample input/output
- Document join keys and aggregation logic
- Test on various data sizes
