# Shell Programming as a Mini-DSL for Data Processing - Homework


## Assignment 1: Command Substitution

1. Store current date in a variable using `$(date)`
2. Count files in a directory and store in variable
3. Create a script that uses nested command substitution
4. Calculate disk usage of a directory and format output
5. Build a filename using today's date: `backup_$(date +%Y%m%d).tar.gz`

## Assignment 2: Streaming Loop - Basic

Write a script using `while read` that:
1. Reads lines from a text file
2. Counts total lines processed
3. Filters lines matching a pattern
4. Transforms each line (e.g., uppercase)
5. Writes results to output file

## Assignment 3: CSV Processing with while read

Create a script that:
1. Reads a CSV file line by line
2. Splits each line into fields using IFS
3. Filters rows based on a column value
4. Calculates sum/average of a numeric column
5. Generates a summary report

## Assignment 4: JSONL to CSV Converter

Write a bash script that:
1. Reads JSON Lines from stdin
2. Uses `jq` to extract specific fields
3. Outputs properly formatted CSV with header
4. Handles missing fields gracefully
5. Processes large files without loading all into memory

## Assignment 5: Arrays and String Operations

1. Create an array of filenames
2. Loop through array and process each file
3. Use `readarray` to load file contents into array
4. Perform string operations: substring, replace, case conversion
5. Join array elements with a delimiter

## Assignment 6: Arithmetic Operations

Write scripts that:
1. Calculate sum of numbers from 1 to N
2. Compute average of values in a file
3. Use `bc` for floating-point calculations
4. Generate random numbers in a range
5. Implement simple calculator with +, -, *, /

## Assignment 7: Functions and Modularity

Create a script with functions for:
1. Reading configuration from a file
2. Logging messages with timestamps
3. Validating input parameters
4. Processing data (reusable function)
5. Main function that orchestrates everything

## Assignment 8: Error Handling

Write a robust script that:
1. Uses `set -euo pipefail`
2. Checks if required files exist
3. Validates number of arguments
4. Has meaningful error messages
5. Exits with appropriate exit codes
6. Uses `trap` for cleanup

## Assignment 9: Process Substitution - Basic

1. Compare outputs of two commands using `diff <(cmd1) <(cmd2)`
2. Join two sorted data streams
3. Use `paste` with process substitution
4. Feed command output to `while read` with `< <(command)`
5. Split output to multiple processes with `tee`

## Assignment 10: Process Substitution - Advanced

Create pipelines using process substitution:
1. Join two CSV files after transformation
2. Process multiple data sources in parallel
3. Branch pipeline output to multiple destinations
4. Implement map-reduce pattern with process substitution
5. Combine results from independent transformations

## Bonus Challenge 1: Complete ETL Script

Build a production-ready script that:
1. Fetches data from an API or file
2. Validates and cleans the data
3. Transforms data format (JSON to CSV, etc.)
4. Calculates statistics
5. Generates a report
6. Includes logging and error handling
7. Uses functions for modularity
8. Accepts configuration via arguments/env vars

Requirements:
- Use `set -euo pipefail`
- Add proper error messages
- Include usage information
- Handle edge cases
- Add comments

## Bonus Challenge 2: Streaming Statistics

Write a script that:
1. Reads numeric data from stdin
2. Calculates running statistics (mean, median, min, max, stdev)
3. Updates statistics as data arrives (streaming)
4. Outputs results every N lines
5. Uses efficient algorithms (don't store all data)
6. Handles large datasets

## Bonus Challenge 3: Configuration File Parser

Create a script that:
1. Reads key=value configuration from a file
2. Validates configuration values
3. Sets defaults for missing values
4. Exports as environment variables
5. Supports comments and blank lines in config
6. Has error handling for invalid syntax

Example config:
```
# Database configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydb
```

## Bonus Challenge 4: Parallel File Processor

Build a script that:
1. Takes a directory of files as input
2. Processes each file independently
3. Uses background jobs for parallelism
4. Limits concurrent jobs (e.g., max 4 at a time)
5. Collects results from all jobs
6. Handles failures gracefully
7. Shows progress

Hint: Use `wait`, background jobs `&`, job control

## Bonus Challenge 5: Template Engine

Implement a simple template processor:
1. Reads template file with placeholders: `{{VARIABLE}}`
2. Replaces placeholders with values from environment/config
3. Supports default values: `{{VARIABLE:default}}`
4. Handles multiple templates
5. Can read values from CSV/JSON
6. Outputs processed files

Example template:
```
Hello {{NAME}},
Your order {{ORDER_ID:UNKNOWN}} is ready.
```

## Submission Guidelines

For each assignment:
1. Write clean, commented code
2. Include usage examples
3. Test with various inputs
4. Handle errors appropriately
5. Document any assumptions
6. Show sample output

## Tips

- Always quote variables: `"$var"`
- Use `shellcheck` to validate scripts
- Test edge cases: empty input, missing files, etc.
- Use meaningful variable and function names
- Start simple, add features incrementally
- Read man pages: `man bash`, `man read`, `man test`
