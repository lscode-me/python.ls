# Grep, Sed & Awk: Text Processing Power Tools - Homework

## Assignment 1: Grep - Pattern Matching
Search a log file for all ERROR and FATAL lines.
- Input: `app.log`
- Command: Use `grep -E` to match both patterns
- Output: Save to `errors.txt`
- Hint: `grep -E "ERROR|FATAL" app.log > errors.txt`

## Assignment 2: Grep - Extract IP Addresses
Extract all IP addresses from an access log.
- Input: `access.log`
- Pattern: `\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b`
- Command: Use `grep -Eo`
- Hint: The `-o` flag shows only the matching part

## Assignment 3: Sed - Replace in File
Replace all occurrences of "http://" with "https://" in a file.
- Input: `urls.txt`
- Command: Use `sed 's|http://|https://|g'`
- Save to `urls_https.txt`

## Assignment 4: Sed - Remove HTML Tags
Strip all HTML tags from a web page.
- Input: `page.html`
- Pattern: `<[^>]*>`
- Command: Use `sed 's/<[^>]*>//g'`
- Output: Plain text

## Assignment 5: Awk - Extract Columns
From a CSV file with (id,name,price,quantity), extract name and price.
- Input: `products.csv`
- Command: `awk -F',' '{print $2, $3}' products.csv`
- Output: Two columns only

## Assignment 6: Awk - Calculate Sum
Calculate the total revenue from a sales CSV.
- Input: `sales.csv` with columns: date,product,price,quantity
- Task: Sum price × quantity for all rows
- Hint: `awk -F',' 'NR > 1 {sum += $3 * $4} END {print sum}'`

## Assignment 7: Awk - Group By
Count the number of orders per customer from an orders CSV.
- Input: `orders.csv` with: order_id,customer_id,amount
- Task: Count orders per customer_id
- Hint: Use associative arrays in awk

## Assignment 8: Combined - Email Domain Analysis
Extract all email addresses, get their domains, and count frequency.
- Input: `users.txt` with text containing email addresses
- Steps:
  1. Use `grep -Eo` to extract emails
  2. Use `sed` to extract domains (everything after @)
  3. Use `sort | uniq -c` to count
  4. Sort by frequency
- Output: List of domains with counts

## Assignment 9: Combined - Log Analysis
From an Apache/Nginx access log, find the top 10 IP addresses by request count.
- Input: `access.log` (standard format)
- Steps:
  1. Use `awk` to extract IP (first field)
  2. Use `sort | uniq -c`
  3. Sort numerically and get top 10
- Hint: `awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10`

## Assignment 10: Combined - Data Cleaning Pipeline
Clean a messy CSV file:
- Remove empty lines
- Remove lines with "NULL" values
- Convert all text to lowercase
- Replace multiple spaces with single space
- Input: `messy_data.csv`
- Use combination of `sed`, `tr`, and `grep`

## Bonus Challenges

### Bonus 1: Regex Validator
Create a script that validates email addresses using grep.
- Input: list of email addresses
- Output: "Valid" or "Invalid" for each
- Use comprehensive email regex pattern

### Bonus 2: Log Parser
Parse a log file to extract:
- Timestamp
- Log level (INFO, ERROR, etc.)
- Message
- Convert to CSV format
- Use awk with complex field parsing

### Bonus 3: Text Report Generator
From a CSV with sales data, generate a formatted text report:
```
# Sales Report

Total Revenue: $12,345.67
Total Orders: 150
Average Order: $82.30
Top Product: Widget A
```
Use awk to calculate all metrics and printf for formatting.

### Bonus 4: Sed Script File
Create a sed script file (`transform.sed`) that:
1. Removes HTML tags
2. Converts to lowercase
3. Removes punctuation
4. Replaces multiple spaces with one
Run it with: `sed -f transform.sed input.html`

### Bonus 5: Advanced Awk - Pivot Table
Create a simple pivot table from sales data:
- Rows: Products
- Columns: Months
- Values: Sum of sales
- Input: `sales.csv` with: date,product,amount
- Output: Pivot table showing product sales by month

## Submission Guidelines
- Submit all commands and scripts
- Include sample input and output files
- Document regex patterns used
- Explain any complex awk logic
- Test on various input sizes
