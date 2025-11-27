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

## Submission Guidelines
- Submit all commands and scripts
- Include sample input/output
- Document join keys and aggregation logic
- Test on various data sizes
