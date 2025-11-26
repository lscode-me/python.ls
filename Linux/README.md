# Unix & Data Pipelines  
### **A Practical Course for Engineers**

---

## **Course Overview**

This course teaches engineers to use Unix tools, shell scripting, and CLI-based data processing as a powerful DSL (domain-specific language) for building data pipelines.  
Students learn to work with large datasets, transform structured and unstructured data, orchestrate multi-step pipelines, and integrate Unix tools with Python.

The curriculum progresses **from core concepts → to stream processing → to structured data → to scaling → to complex pipeline architecture**.

---

# 1. Unix as a Language of Data & Streams

### Topics
- Unix philosophy for data-intensive tasks  
- Streams, pipes, stdin/stdout  
- Filter → Transform → Aggregate workflow  
- Text as the universal data interface  

### Learning Goals
- Think in terms of *data flowing through transformations*  
- Build simple analytical pipelines  

### Hands-on Tasks
1. Fetch a CSV using `curl`, filter by date, show top 10 entries.  
2. Count unique column values using pipelines.  
3. Compute most frequent values in a log or CSV.

### Tools
`curl`, `cut`, `grep`, `sort`, `uniq`, `head`  

---

# 2. Shell Programming as a Mini-DSL for Data Processing

### Topics
- Command substitution `$(...)`  
- Streaming loops: `while read`  
- Arrays, strings, arithmetic  
- Functions, exit codes, `set -euo pipefail`  
- Process substitution `<(cmd)` and `>(cmd)`  

### Learning Goals
- Write safe, reusable data-processing scripts  

### Hands-on Tasks
1. Script that reads JSONL from stdin → filters with `jq` → outputs CSV.  
2. Streaming loop calculating mean/median of a field.  
3. Join two transformed streams using process substitution.

### Tools
`bash`, `jq`, `awk`, `printf`

---

# 3. Coreutils as Building Blocks of Pipelines

### Topics
- Streaming utilities  
- Field manipulation with `cut`, `paste`, `tr`  
- Sorting & merging large files  
- Splitting datasets  
- Stream buffering (`stdbuf`) & monitoring (`pv`)  

### Learning Goals
- Efficiently work with multi-gigabyte datasets  

### Hands-on Tasks
1. Split a large CSV into chunks, then merge them back.  
2. Count lines/words/characters across files.  
3. Use `pv` + `stdbuf` to process a 10GB file smoothly.

### Tools
`cat`, `cut`, `paste`, `sort`, `uniq`, `split`, `pv`, `stdbuf`

---

# 4. grep, sed, and awk — The Core Text Processing Trio

### Topics
- Regular expressions  
- Filtering with `grep`  
- Stream editing with `sed`  
- Field-based analytics with `awk`  

### Learning Goals
- Perform non-trivial text transformations and aggregations  

### Hands-on Tasks
1. Extract all requests with status 500.  
2. Anonymize emails using `sed`.  
3. Compute average response time per IP with `awk`.

### Tools
`grep`, `sed`, `awk`

---

# 5. Working with Structured Data: CSV, JSON, YAML, XML

### Topics
- Structured formats overview  
- JSON parsing with `jq`  
- CSV processing with `csvkit`, `mlr`, `datamash`  
- YAML (`yq`) and XML (`xmlstarlet`) processing  

### Learning Goals
- Transform and analyze structured data streams  

### Hands-on Tasks
1. Convert JSON → CSV → aggregated CSV → YAML report.  
2. Compute diffs between YAML files.  
3. Extract data from XML and convert to JSON.

### Tools
`jq`, `csvkit`, `mlr`, `yq`, `xmlstarlet`

---

# 6. Streaming Analytics & Aggregations

### Topics
- Streaming join, group-by, reduce  
- Textual map/reduce patterns  
- Column statistics: mean, median, stdev  
- Multi-field grouping  

### Learning Goals
- Analytical queries using CLI tools  
- Processing large datasets without loading into memory  

### Hands-on Tasks
1. Group by a categorical column and show top N groups.  
2. Compute mean and median with `datamash`.  
3. Join two large CSV files.

### Tools
`awk`, `datamash`, `mlr`, `sort`, `join`

---

# 7. Log Processing & API Data Pipelines

### Topics
- JSONL (one JSON per line)  
- Gzip streaming (`zcat`, `bzcat`, `xzcat`)  
- REST API pipelines  
- Markdown table generation  

### Learning Goals
- Transform and analyze log data and API responses  

### Hands-on Tasks
1. Stream-process gzip logs and compute IP frequencies.  
2. Query a REST API with `curl`, compute statistics using `jq`.  
3. Generate Markdown tables using `column -t`.

### Tools
`curl`, `jq`, `zcat`, `datamash`, `column`

---

# 8. Pipeline Performance, Parallelism & Scaling

### Topics
- GNU parallel  
- `xargs -P` parallel execution  
- External sorting (`sort -S`, `--parallel`)  
- Profiling: `time`, `dstat`, `pv`  

### Learning Goals
- Break large jobs into parallel chunks  
- Improve performance of data pipelines  

### Hands-on Tasks
1. Process 100 CSV files in parallel.  
2. Tune sorting performance using buffer size.  
3. Measure pipeline throughput with `pv`.

### Tools
`parallel`, `xargs`, `pv`, `time`, `dstat`, `sort`

---

# 9. Streams, Pseudo-files & IPC (`-`, `p`, `s`)

### Topics
- `-` as stdin/stdout pseudo-file  
- Named pipes (FIFO) using `mkfifo`  
- UNIX domain sockets  
- Shell ↔ Python IPC  

### Learning Goals
- Build multi-process pipelines and IPC-driven flows  

### Hands-on Tasks
1. Use `-` to build multi-stage pipelines without files.  
2. Create a FIFO pipe sending JSON to another process.  
3. Python UNIX socket server + Bash client (`socat`).  

### Tools
`mkfifo`, `socat`, `jq`, `cat`, Python’s `socket`

---

# 10. Bash as a Glue Language

### Topics
- Combining many tools  
- Error handling with `trap`, `pipefail`  
- `.env`-based configuration  
- Temporary files & directories  

### Learning Goals
- Write robust multi-step processing scripts  

### Hands-on Tasks
1. ETL job: API → JSON → CSV → SQLite → Markdown report.  
2. Add `trap`-based cleanup and error-handling.  
3. Parameterize commands via environment variables.

### Tools
`bash`, `jq`, `sqlite3`, `env`, `trap`

---

# 11. Python & External Languages in Pipelines

### Topics
- Python as a stream filter  
- Reading stdin, writing stdout  
- pandas CLI vs Miller (`mlr`)  
- Hybrid Bash ↔ Python pipelines  

### Learning Goals
- Seamlessly integrate Python into Unix workflows  

### Hands-on Tasks
1. Python script reading JSONL from stdin and outputting a summary.  
2. Replace a slow CLI step with Python for comparison.  
3. Compare pandas vs Miller performance.

### Tools
`python`, `jq`, `mlr`, `pandas`

---

# 12. Architecture of Complex Pipelines  
### *Map/Reduce, Temporary Files, Dependency Flow*

### Topics
- Unix-style map/reduce  
- Temporary staging files (`mktemp`)  
- Checkpoints & `.done` markers  
- Makefile-based orchestration  
- Reproducibility & restartability  

### Learning Goals
- Architect large, restartable, debuggable pipelines  
- Balance pipes vs temporary files  
- Manage dependencies explicitly  

### Hands-on Tasks
1. Build a chunked map/reduce pipeline using `split` + `parallel`.  
2. Add `.done` checkpoints for restartability.  
3. Write a Makefile orchestrating multi-stage processing.

### Tools
`parallel`, `split`, `datamash`, `make`, temporary directories

---

# 13. Final Project — Data Pipeline Challenge

### Project Summary
Build a complete ETL pipeline that:

- Processes **5GB of JSONL or CSV**  
- Uses streaming and parallel processing  
- Converts between formats (JSON ↔ CSV ↔ Markdown)  
- Uses checkpoints & logging  
- Integrates Bash with Python  

### Evaluation Criteria
- Correctness  
- Performance  
- Architecture clarity  
- Error handling & safety  
- Clean code & documentation  

---

**End of syllabus.**
