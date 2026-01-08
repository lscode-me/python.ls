# Final Project: Build a Complete ETL Pipeline - Quiz

## Knowledge Assessment Questions

Before starting your final project, answer these questions to assess your understanding of ETL concepts and best practices.

---

## Question 1: ETL Pipeline Architecture

What is the recommended order of operations in an ETL pipeline?

A) Load → Transform → Extract
B) Transform → Extract → Load
C) Extract → Transform → Load
D) Extract → Load → Transform

---

## Question 2: Error Handling

What is the best practice for handling errors in a production ETL pipeline?

A) Let errors propagate and stop the entire pipeline
B) Silently ignore all errors to keep the pipeline running
C) Log errors, route to error sink, and continue processing valid records
D) Retry indefinitely until the error is resolved

---

## Question 3: Data Quality

Which approach best ensures data quality in an ETL pipeline?

A) Trust the source data and process as-is
B) Validate only at the final loading step
C) Implement validation at extraction, transformation, and loading stages
D) Fix data quality issues manually after loading

---

## Question 4: Performance Optimization

When processing large datasets (5GB+), which technique is most effective?

A) Load all data into memory at once
B) Use streaming/chunked processing with parallel execution
C) Process records one at a time sequentially
D) Increase swap space to handle memory overflow

---

## Question 5: Testing Strategy

What is the recommended testing approach for ETL pipelines?

A) Only test the final output
B) Test each stage independently, then test integration
C) Manual verification is sufficient
D) Testing is optional for one-time data loads

---

## Question 6: Streaming vs Batch Processing

When should you choose streaming over batch processing in an ETL pipeline?

A) When data arrives in large daily batches
B) When processing historical data archives
C) When low latency and real-time insights are required
D) When memory is unlimited

---

## Question 7: Pipeline Monitoring

What metrics are most important to monitor in a production ETL pipeline?

A) Only the final record count
B) Throughput, error rate, latency, and resource utilization
C) Just CPU usage
D) Only disk space

---

## Question 8: Checkpointing

Why is checkpointing important in long-running ETL pipelines?

A) It makes the code look more professional
B) It allows resuming from failure without reprocessing all data
C) It's required by all data formats
D) It improves network bandwidth

---

## Question 9: Data Validation Location

At which stage should data validation primarily occur in an ETL pipeline?

A) Only at the final loading stage
B) Only during extraction
C) At all stages (extract, transform, and load)
D) Validation is not necessary if the source is trusted

---

## Question 10: Parallel Processing

Which tool is most appropriate for parallelizing shell commands across multiple files?

A) cat
B) GNU parallel or xargs -P
C) echo
D) grep

---

## Question 11: Makefile Usage

Why is Makefile useful for ETL pipeline orchestration?

A) It's the only way to run shell scripts
B) It provides dependency tracking and incremental builds
C) It makes code run faster
D) It's required for Python scripts

---

## Question 12: Memory Efficiency

Which approach is most memory-efficient for processing a 10GB CSV file?

A) Load entire file into memory
B) Use streaming with line-by-line processing
C) Copy the file multiple times
D) Compress the file first, then load into memory

---

## Question 13: Error Sinks

What is an "error sink" in ETL terminology?

A) A syntax error in the code
B) A destination where rejected/invalid records are stored for review
C) A memory leak
D) A hardware failure

---

## Question 14: Idempotency

Why is idempotency important in ETL pipelines?

A) It's a naming convention
B) Running the same pipeline multiple times produces the same result
C) It makes code shorter
D) It's only needed for real-time processing

---

## Question 15: Log Aggregation

What is the best practice for logging in a distributed ETL pipeline?

A) Print to stdout only
B) Log to separate files per component with timestamps and correlation IDs
C) Disable logging for better performance
D) Log only errors, ignore all other information

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | ETL stands for Extract, Transform, Load - the standard order of operations |
| 2 | B | Production pipelines should handle errors gracefully without losing valid data |
| 3 | B | Validate at each stage to catch issues early and maintain data integrity |
| 4 | A | Streaming and parallelism prevent memory issues and improve throughput |
| 5 | B | Test components individually first, then verify they work together correctly |
| 6 | D | Streaming is ideal for real-time processing where low latency is critical |
| 7 | D | Comprehensive monitoring includes throughput, errors, latency, and resources |
| 8 | A | Checkpointing enables recovery from failures without full reprocessing |
| 9 | C | Validation at all stages catches issues early and ensures data quality |
| 10 | C | GNU parallel and xargs -P enable parallel execution of commands |
| 11 | C | Makefile tracks dependencies and only rebuilds what's necessary |
| 12 | A | Streaming processes data line-by-line without loading entire file |
| 13 | D | Error sink stores invalid records for later analysis and reprocessing |
| 14 | A | Idempotency ensures consistent results regardless of retry count |
| 15 | C | Structured logging with timestamps and IDs enables debugging and tracing |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **13-15 correct (87-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the final project. |
| **10-12 correct (67-80%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **7-9 correct (47-60%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 7 correct (<47%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
