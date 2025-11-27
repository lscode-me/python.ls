# Quiz: Structured Data Processing

## Questions

1. Which command extracts the "name" field from each object in a JSON array?
   - A) `jq '.name'`
   - B) `jq '.[] | .name'`
   - C) `jq 'name'`
   - D) `jq '[].name'`

2. What does the `-r` flag do in jq?
   - A) Reverses the output
   - B) Outputs raw text (no JSON quotes)
   - C) Recursive processing
   - D) Reads from file

3. Which tool is best for processing CSV files with complex field handling?
   - A) awk
   - B) cut
   - C) miller (mlr)
   - D) grep

4. How do you convert a JSON array to CSV using jq?
   - A) `jq '.[] | @csv'`
   - B) `jq -r '.[] | [.field1, .field2] | @csv'`
   - C) `jq 'to_csv'`
   - D) `jq --csv '.'`

5. What format is JSONL (JSON Lines)?
   - A) Pretty-printed JSON
   - B) One JSON object per line
   - C) Compressed JSON
   - D) JSON with line numbers

6. Which csvkit tool extracts specific columns from a CSV?
   - A) `csvcut`
   - B) `csvgrep`
   - C) `csvselect`
   - D) `csvfilter`

7. How do you filter JSON objects where age > 25 using jq?
   - A) `jq 'filter(.age > 25)'`
   - B) `jq '.[] | select(.age > 25)'`
   - C) `jq 'where age > 25'`
   - D) `jq '.age > 25'`

8. Which miller command calculates the sum of a column grouped by another column?
   - A) `mlr sum -f amount -g customer`
   - B) `mlr stats1 -a sum -f amount -g customer`
   - C) `mlr group-by customer sum amount`
   - D) `mlr aggregate sum(amount) by customer`

9. How do you pretty-print XML with xmlstarlet?
   - A) `xmlstarlet print file.xml`
   - B) `xmlstarlet format file.xml`
   - C) `xmlstarlet pretty file.xml`
   - D) `xmlstarlet -p file.xml`

10. What does `jq -s '.'` do?
    - A) Sorts JSON objects
    - B) Selects all fields
    - C) Slurps multiple JSON objects into an array
    - D) Streams JSON output

---

## Answer Key
1. B - `.[]` iterates array, `| .name` extracts name field
2. B - `-r` outputs raw strings without JSON quotes
3. C - Miller handles quoted fields, edge cases better than awk
4. B - Need `-r` for raw output, `[fields]` for array, `@csv` for CSV format
5. B - JSONL has one JSON object per line for streaming
6. A - `csvcut -c columns` extracts specific columns
7. B - `.[]` iterates, `select()` filters by condition
8. B - `stats1 -a sum -f field -g groupby` aggregates
9. B - `format` command pretty-prints XML
10. C - `-s` slurp mode reads all inputs into array
