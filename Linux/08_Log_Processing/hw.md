# Log Processing & Real-World Pipelines - Homework

## Assignment 1: Filter JSONL Errors
Extract all ERROR level entries from a JSONL log file.
- Input: `app.jsonl`
- Command: `jq -c 'select(.level == "ERROR")' app.jsonl > errors.jsonl`

## Assignment 2: Compressed Log Analysis
Count ERROR occurrences in a compressed log.
- Input: `app.log.gz`
- Command: `zcat app.log.gz | grep -c ERROR`

## Assignment 3: API Data Fetch
Fetch users from JSONPlaceholder API and extract names.
- URL: `https://jsonplaceholder.typicode.com/users`
- Command: `curl -s 'https://jsonplaceholder.typicode.com/users' | jq -r '.[].name'`

## Assignment 4: Generate Markdown Table
Convert CSV to markdown table format.
- Input: `data.csv`
- Output: Markdown table with headers and rows

## Assignment 5: Time-Based Log Filtering
Extract log entries from a specific hour.
- Input: `app.jsonl` with timestamp field
- Filter: entries from 10:00-11:00
- Use: `jq -c 'select(.timestamp | startswith("2024-03-15T10"))'`

## Assignment 6: Error Aggregation
Count errors by error_type from JSONL.
- Input: `errors.jsonl`
- Command: `jq -r '.error_type' errors.jsonl | sort | uniq -c | sort -rn`

## Assignment 7: Multi-File Processing
Process all gzip logs in a directory, count total errors.
- Command: `zcat logs/*.gz | grep -c ERROR`

## Assignment 8: API Pagination
Fetch multiple pages from an API (pages 1-5).
- Use: for loop with curl and jq
- Combine results into single array

## Assignment 9: Daily Report Generator
Create script that generates markdown report with:
- Total log lines
- Error count
- Top 5 error types
- Timestamp

## Assignment 10: Complete ETL Pipeline
Build pipeline that:
1. Fetches data from API
2. Filters relevant fields
3. Aggregates statistics
4. Generates markdown report
5. Saves to file

## Bonus Challenges

### Bonus 1: Real-Time Log Monitor
Create script that tails a JSONL log and prints ERROR entries in real-time.
- Use: `tail -f | stdbuf -oL jq`

### Bonus 2: Multi-Source Aggregation
Combine data from:
- API endpoint
- Compressed log file
- CSV file
Generate unified markdown report.

### Bonus 3: Rate-Limited API Crawler
Fetch data from paginated API with rate limit (2 req/sec).
- Use: sleep or GNU parallel
- Handle errors gracefully

### Bonus 4: Log Rotation Analyzer
Analyze all rotated logs (app.log, app.log.1.gz, app.log.2.gz, ...).
- Find error trends over time
- Generate time-series report

### Bonus 5: Automated Daily Report
Create cron-ready script that:
- Processes yesterday's logs
- Generates markdown report
- Emails report (using mail command)
- Archives old reports

## Submission Guidelines
- Submit all scripts and commands
- Include sample input/output
- Test with real APIs (JSONPlaceholder, GitHub API)
- Document rate limits and error handling
