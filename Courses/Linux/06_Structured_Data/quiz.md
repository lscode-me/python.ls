# Structured Data Processing (JSON, CSV, YAML, XML) - Quiz

## Questions

## Question 1: jq Array Iteration

Which command extracts the "name" field from each object in a JSON array?

A) `jq '.[] | .name'`
B) `jq '.name'`
C) `jq 'name'`
D) `jq '[].name'`


## Question 2: jq Raw Output

What does the `-r` flag do in jq?

A) Reverses the output
B) Outputs raw text (no JSON quotes)
C) Recursive processing
D) Reads from file


## Question 3: Which tool is best for

Which tool is best for processing CSV files with complex field handling?

A) awk
B) cut
C) grep
D) miller (mlr)


## Question 4: jq CSV Conversion

How do you convert a JSON array to CSV using jq?

A) jq '.[] | @csv'
B) jq -r '.[] | [.field1, .field2] | @csv'
C) jq 'to_csv'
D) jq --csv '.'


## Question 5: JSONL Format

What format is JSONL (JSON Lines)?

A) Pretty-printed JSON
B) Compressed JSON
C) One JSON object per line
D) JSON with line numbers


## Question 6: csvkit Column Extraction

Which csvkit tool extracts specific columns from a CSV?

A) csvgrep
B) csvselect
C) csvfilter
D) csvcut


## Question 7: jq Filter

How do you filter JSON objects where age > 25 using jq?

A) jq '.[] | select(.age > 25)'
B) jq 'filter(.age > 25)'
C) jq 'where age > 25'
D) jq '.age > 25'


## Question 8: Miller Group By

Which miller command calculates the sum of a column grouped by another column?

A) mlr sum -f amount -g customer
B) mlr group-by customer sum amount
C) mlr --csv stats1 -a sum -f amount -g customer
D) mlr aggregate sum(amount) by customer


## Question 9: XML Pretty Print

How do you pretty-print XML with xmlstarlet?

A) xmlstarlet print file.xml
B) xmlstarlet pretty file.xml
C) xmlstarlet -p file.xml
D) xmlstarlet format file.xml


## Question 10: jq Slurp

What does `jq -s '.'` do?

A) Slurps multiple JSON objects into an array
B) Selects all fields
C) Sorts JSON objects
D) Streams JSON output


## Question 11: DuckDB CSV Query

How do you query a CSV file with DuckDB?

A) duckdb -c "SELECT * FROM csv('users.csv')"
B) duckdb users.csv -q "SELECT *"
C) duckdb -c "SELECT * FROM 'users.csv'"
D) duckdb --query users.csv


## Question 12: DuckDB CSV Auto

Which DuckDB function reads CSV files with automatic schema detection?

A) read_csv('file.csv')
B) read_csv_auto('file.csv')
C) auto_read_csv('file.csv')
D) csv_read('file.csv')


## Question 13: What is the main advantage

What is the main advantage of DuckDB over csvkit for large files?

A) Easier syntax
B) Better error messages
C) More output formats
D) Columnar storage and efficient memory usage


## Question 14: DuckDB Parquet Export

How do you export DuckDB query results to Parquet format?

A) duckdb -c "SELECT * FROM 'data.csv'" > output.parquet
B) duckdb -c "COPY (SELECT * FROM 'data.csv') TO 'output.parquet'"
C) duckdb -c "SELECT * FROM 'data.csv'" -parquet
D) duckdb -c "EXPORT TO PARQUET 'output.parquet'"


## Question 15: When should you use DuckDB

When should you use DuckDB instead of Miller?

A) For simple column selection
B) For quick one-liners
C) For complex multi-way joins and window functions
D) For streaming data


---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | `.[]` iterates over array elements, and `.name` extracts the field from each object |
| 2 | B | `-r` outputs raw strings without JSON quotes |
| 3 | D | Miller handles quoted fields, edge cases better than awk |
| 4 | B | Need `-r` for raw output, `[fields]` for array, `@csv` for CSV format |
| 5 | C | JSONL has one JSON object per line for streaming |
| 6 | D | `csvcut -c columns` extracts specific columns |
| 7 | A | `.[]` iterates, `select()` filters by condition |
| 8 | C | `mlr --csv stats1 -a sum -f field -g groupby` aggregates with `--csv` for proper CSV handling |
| 9 | D | `format` command pretty-prints XML |
| 10 | A | `-s` slurp mode reads all inputs into array |
| 11 | C | DuckDB can read CSV files directly using `'filename.csv'` syntax |
| 12 | B | `read_csv_auto()` automatically detects headers, types, delimiters. Note: `read_csv()` also works in DuckDB v1.0+ |
| 13 | D | DuckDB uses columnar storage and chunked processing, making it significantly more memory-efficient than csvkit for large analytical queries |
| 14 | B | `COPY (query) TO 'file.parquet'` exports to Parquet format |
| 15 | C | DuckDB excels at complex SQL operations, window functions, and analytical queries |
