# Homework: Structured Data Processing

## Assignment 1: Extract JSON Fields
Extract the "name" and "age" fields from a JSON array of users.
- Input: `users.json` with array of user objects
- Command: Use `jq '.[] | {name, age}'`
- Output: JSON objects with only name and age

## Assignment 2: Filter JSON by Condition
Filter users older than 25 years.
- Input: `users.json`
- Command: `jq '.[] | select(.age > 25)'`
- Output: Filtered JSON array

## Assignment 3: JSON to CSV Conversion
Convert a JSON array to CSV format.
- Input: `products.json` with: id, name, price
- Command: `jq -r '.[] | [.id, .name, .price] | @csv' products.json > products.csv`
- Output: CSV file

## Assignment 4: CSV Column Selection
Extract specific columns from a CSV file.
- Input: `data.csv` with many columns
- Command: Use `csvcut -c name,age,city data.csv` or `mlr --csv cut -f name,age,city data.csv`
- Output: CSV with 3 columns

## Assignment 5: CSV Filtering
Filter CSV rows where price > 100.
- Input: `sales.csv`
- Command: `mlr --csv filter '$price > 100' sales.csv`
- Output: Filtered rows

## Assignment 6: CSV Group-By Aggregation
Calculate total sales per customer.
- Input: `orders.csv` with: order_id, customer_id, amount
- Command: `mlr --csv stats1 -a sum -f amount -g customer_id orders.csv`
- Output: customer_id, amount_sum

## Assignment 7: JSONL Processing
Process a JSON Lines file to extract error events.
- Input: `events.jsonl`
- Command: `jq -c 'select(.type == "error")' events.jsonl`
- Output: JSONL with errors only

## Assignment 8: Multi-Format Pipeline
Download JSON from API, filter, convert to CSV.
- Steps:
  1. `curl -s 'https://jsonplaceholder.typicode.com/users'`
  2. Filter users from specific city: `jq '.[] | select(.address.city == "Gwenborough")'`
  3. Convert to CSV: `jq -r '[.id, .name, .email] | @csv'`
- Output: CSV file

## Assignment 9: XML Data Extraction
Extract all names from an XML file.
- Input: `users.xml`
- Command: `xmlstarlet sel -t -v "//user/name" -n users.xml`
- Output: List of names

## Assignment 10: CSV to JSON and Back
Convert CSV to JSON, filter, convert back to CSV.
- Input: `products.csv`
- Steps:
  1. CSV → JSON: `mlr --csv --ojson cat products.csv`
  2. Filter: `jq '.[] | select(.price < 50)'`
  3. JSON → CSV: `jq -r '[.id, .name, .price] | @csv'`

## DuckDB Assignments

### Assignment 11: Query CSV with SQL
Use DuckDB to query a CSV file with SQL.
- Input: `users.csv`
- Command: `duckdb -c "SELECT name, city FROM 'users.csv' WHERE status = 'active'"`
- Output: Active users with their cities

### Assignment 12: Aggregate with DuckDB
Calculate statistics per category using SQL.
- Input: `products.csv`
- Command: `duckdb -c "SELECT category, COUNT(*), AVG(price), MAX(price) FROM 'products.csv' GROUP BY category"`
- Output: Category statistics

### Assignment 13: Join with DuckDB
Join users and orders using SQL.
- Input: `users.csv`, `orders.csv`
- Command: `duckdb -c "SELECT u.name, COUNT(o.order_id) as orders, SUM(o.amount) as total FROM 'users.csv' u JOIN 'orders.csv' o ON u.id = o.customer_id GROUP BY u.name"`
- Output: User statistics with order counts

### Assignment 14: Export to Parquet
Convert CSV to Parquet format.
- Input: `users.csv`
- Command: `duckdb -c "COPY (SELECT * FROM 'users.csv') TO 'users.parquet' (FORMAT PARQUET)"`
- Output: `users.parquet` file

### Assignment 15: Complex Query
Find top spending customers by city.
- Input: `users.csv`, `orders.csv`
- Use: CTE (Common Table Expression) in DuckDB
- Output: Ranked customers per city

## Bonus Challenges

### Bonus 1: JSON Aggregation
From a JSONL file of sales, calculate:
- Total revenue
- Average order value
- Number of orders
Use jq with `-s` flag.

### Bonus 2: CSV Join
Join two CSV files on a common column.
- `customers.csv`: customer_id, name
- `orders.csv`: order_id, customer_id, amount
- Output: order_id, name, amount
- Hint: Use `csvjoin` or `mlr join`

### Bonus 3: Complex jq Filter
From a nested JSON API response:
1. Extract specific fields
2. Flatten nested objects
3. Filter by multiple conditions
4. Convert to CSV

### Bonus 4: Data Validation
Validate that a JSON file conforms to a schema.
- Use `jsonschema` or jq to check:
  - Required fields present
  - Data types correct
  - Value ranges valid

### Bonus 5: Multi-File Aggregation
Aggregate data from multiple JSON files:
- Read all `.json` files in a directory
- Merge into single array
- Group by category
- Calculate statistics per category

### Bonus 6: DuckDB Performance Comparison
Compare DuckDB vs mlr performance:
- Create a large CSV file (1M+ rows)
- Perform same aggregation with both tools
- Measure execution time using `time` command
- Compare memory usage
- Document results

### Bonus 7: Window Functions with DuckDB
Use DuckDB window functions:
- Input: `orders.csv`
- Calculate running total per customer
- Add row numbers within customer groups
- Find previous and next order amounts (LAG/LEAD)
- Output: Enhanced dataset with analytical columns

## Submission Guidelines
- Submit all commands and scripts
- Include sample input/output files
- Test with various data formats
- Document any edge cases handled
