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

# 2. Files, I-nodes & File Descriptors  
### *Understanding Unix File System Architecture*

### Topics
- **I-nodes (index nodes)**  
  - What is an i-node: metadata structure (permissions, timestamps, size, pointers to blocks)  
  - I-node vs filename: hard links point to the same i-node  
  - `ls -i` to view i-node numbers  
  - `stat` command for detailed i-node information  
  
- **File descriptors**  
  - File descriptor = integer handle to open files  
  - Process file descriptor table  
  - Standard descriptors: 0 (stdin), 1 (stdout), 2 (stderr)  
  - `/proc/[pid]/fd/` - view open file descriptors  
  - Redirecting descriptors: `2>&1`, `1>&2`, `3>file`  
  
- **File types in Unix**  
  - Regular files (`-`)  
  - Directories (`d`)  
  - Symbolic links (`l`)  
  - Named pipes/FIFOs (`p`)  
  - Sockets (`s`)  
  - Character devices (`c`)  
  - Block devices (`b`)  
  - Identifying with `ls -l` first character  
  
- **File permissions**  
  - Read (r=4), Write (w=2), Execute (x=1)  
  - User, Group, Other (ugo)  
  - Octal notation: `chmod 755`, `chmod 644`  
  - Symbolic notation: `chmod u+x`, `chmod go-w`  
  - Special bits: setuid (4000), setgid (2000), sticky (1000)  
  - `umask` - default permission mask  
  
- **stdin/stdout/stderr as files**  
  - `/dev/stdin` → `/proc/self/fd/0`  
  - `/dev/stdout` → `/proc/self/fd/1`  
  - `/dev/stderr` → `/proc/self/fd/2`  
  - `/dev/null` - the black hole  
  - `/dev/zero`, `/dev/random`, `/dev/urandom`  
  
- **File data formats**  
  - Text vs binary files  
  - Line endings: `\n` (Unix), `\r\n` (Windows), `\r` (old Mac)  
  - Character encoding: ASCII, UTF-8, UTF-16, Latin-1  
  - `file` command to identify format  
  - Magic bytes and file signatures  

### Learning Goals
- Understand Unix file system abstractions  
- Master file descriptors and redirection  
- Work confidently with permissions  
- Distinguish file types and formats  

### Hands-on Tasks
1. Use `stat` to inspect i-node information for a file and its hard link.  
2. Create a script that redirects stdout to one file and stderr to another.  
3. List all file types in `/dev` using `ls -l | cut -c1 | sort | uniq -c`.  
4. Change permissions on a script: make executable for user, read-only for others.  
5. Read from `/dev/urandom`, pipe through `base64`, save to file.  
6. Use `lsof` or `/proc/self/fd/` to inspect open file descriptors of a running process.  
7. Identify file formats using `file` command on various files.  
8. Create hard link and symbolic link, compare i-node numbers.  
9. Redirect stderr to stdout and pipe both to `grep`.  
10. Set umask and create files to observe default permissions.

### Tools
`stat`, `ls`, `ln`, `chmod`, `umask`, `file`, `lsof`, `cat`, redirection operators (`>`, `>>`, `2>`, `&>`, `2>&1`)

---

# 3. Shell Programming as a Mini-DSL for Data Processing

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

# 4. Coreutils as Building Blocks of Pipelines

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

# 5. grep, sed, and awk — The Core Text Processing Trio

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

# 6. Working with Structured Data: CSV, JSON, YAML, XML

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

# 7. Streaming Analytics & Aggregations

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

# 8. Log Processing & API Data Pipelines

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

# 9. Pipeline Performance, Parallelism & Scaling

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

# 10. Streams, Pseudo-files & IPC (`-`, `p`, `s`)

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

# 11. Bash as a Glue Language

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

# 12. Python & External Languages in Pipelines

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

# 13. Architecture of Complex Pipelines  
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

# 14. Final Project — Data Pipeline Challenge

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
