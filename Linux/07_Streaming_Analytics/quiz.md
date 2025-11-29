# Streaming Analytics: Join, Group-By, Map/Reduce - Quiz

## Questions

1. What must you do before using the `join` command on two files?
   - A) Convert them to CSV
   - B) Sort both files by the join key
   - C) Remove duplicates
   - D) Count the lines

2. Which tool performs hash joins efficiently on small lookup tables?
   - A) join
   - B) sort
   - C) awk
   - D) uniq

3. How do you calculate the sum of column 3 grouped by column 1 using awk?
   - A) `awk '{sum[$1] += $3} END {for (k in sum) print k, sum[k]}'`
   - B) `awk '{sum($1, $3)}'`
   - C) `awk 'group by $1 sum $3'`
   - D) `awk '{print $1, sum($3)}'`

4. Which miller command performs a left outer join?
   - A) `mlr join --left`
   - B) `mlr join --ul`
   - C) `mlr join -l`
   - D) `mlr join --outer`

5. What does `datamash -t',' -s -g 1 sum 3` do?
   - A) Sums column 3
   - B) Groups by column 1 and sums column 3 (requires sorted input)
   - C) Groups by column 3 and sums column 1
   - D) Sorts by column 1 and sums column 3

6. How do you calculate a running total with awk?
   - A) `awk '{sum++; print sum}'`
   - B) `awk '{sum += $1; print sum}'`
   - C) `awk '{total = total + $1}'`
   - D) `awk 'BEGIN {sum=0} {sum=$1}'`

7. What is the map phase in map/reduce?
   - A) Sorting data
   - B) Transforming each record independently
   - C) Aggregating results
   - D) Reducing data size

8. Which command calculates the top 5 products by revenue in each category?
   - A) `mlr --csv top -n 5 -f revenue`
   - B) `mlr --csv sort -nr revenue | head -5`
   - C) `mlr --csv top -n 5 -f revenue -g category`
   - D) `mlr --csv stats1 -a top(5) -f revenue -g category`

9. What is a hash join best suited for?
   - A) Large files on both sides
   - B) Small lookup table joined with large data file
   - C) Sorted data
   - D) Multiple join keys

10. How do you perform a moving average of 5 values in awk?
    - A) Keep last 5 values in array, sum and divide by 5
    - B) Use `sum($1, 5)`
    - C) Use `awk 'moving_avg(5)'`
    - D) Sort and take average

11. How do you join three CSV files using DuckDB?
    - A) Run three separate join commands
    - B) Use nested SELECT statements
    - C) Use multiple JOIN clauses in one query
    - D) You can't join more than two files

12. What does `ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC)` do?
    - A) Counts total rows
    - B) Assigns sequential numbers within each category by price
    - C) Orders by price and category
    - D) Partitions data into numbered buckets

13. Which DuckDB window function returns the previous row's value?
    - A) `PREV()`
    - B) `PREVIOUS()`
    - C) `LAG()`
    - D) `LAST()`

14. How do you calculate the median in DuckDB?
    - A) `MEDIAN(column)`
    - B) `AVG(column)`
    - C) `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY column)`
    - D) `MIDDLE(column)`

15. When should you use DuckDB over awk for analytics?
    - A) For simple line-by-line processing
    - B) For complex queries with multiple aggregations and window functions
    - C) For text pattern matching
    - D) For quick one-liners

---

## Answer Key
1. B - `join` requires both files to be sorted by join key
2. C - awk loads small file into hash, fast lookups
3. A - Associative array accumulates sum by key
4. B - `--ul` means "unpaired left" (left outer join)
5. B - `-g 1` groups by column 1, `sum 3` sums column 3, `-s` means sorted input
6. B - Accumulate into `sum` variable, print each iteration
7. B - Map phase transforms each input record independently
8. C - `top` with `-n 5` and `-g category` finds top-K per group
9. B - Hash join optimal for small lookup, large data
10. A - Maintain circular buffer of last N values
11. C - DuckDB supports multiple JOIN clauses in a single SELECT query
12. B - ROW_NUMBER assigns sequential numbers within each partition (category)
13. C - LAG() returns the value from the previous row in the window
14. C - PERCENTILE_CONT(0.5) calculates the median (50th percentile)
15. B - DuckDB is better for SQL-style analytical queries with complex logic
