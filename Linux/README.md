# Unix & Data Pipelines
### A Practical Course for Engineers

A course that teaches engineers to use Unix tools, shell scripting, and CLI-based data processing as a powerful DSL for building data pipelines. Students learn to work with large datasets, transform structured and unstructured data, and integrate Unix tools with Python.

---

## 📚 Course Contents

### 1. Unix as a Language of Data & Streams

Introduction to Unix philosophy and stream-based data processing.

**Topics:** Streams, pipes, stdin/stdout, Filter→Transform→Aggregate workflow

**Materials:**
- [Lecture](01_Unix_Streams/lecture.md) - Unix philosophy for data processing
- [Sample Data](01_Unix_Streams/DataSamples.md) - Practice datasets
- [Homework](01_Unix_Streams/hw.txt) - 10 assignments + bonus ETL project
- [Resources](01_Unix_Streams/links.txt)

**Tools:** `curl`, `cut`, `grep`, `sort`, `uniq`, `head`, `tail`

---

### 2. Files, I-nodes & File Descriptors

Understanding Unix file system architecture.

**Topics:** I-nodes, file descriptors, file types, permissions, special files

**Materials:**
- [Lecture](02_Files_Inodes_Descriptors/lecture.md) - Complete file system guide
- [Homework](02_Files_Inodes_Descriptors/hw.txt) - 10 assignments + 4 bonus challenges
- [Resources](02_Files_Inodes_Descriptors/links.txt)

**Tools:** `stat`, `ls`, `ln`, `chmod`, `umask`, `file`, `lsof`, redirections

---

### 3. Shell Programming

Bash as a domain-specific language for data processing.

**Topics:** Command substitution, `while read`, arrays, functions, `set -euo pipefail`, process substitution

**Materials:**
- [Lecture](03_Shell_Programming/lecture.md) - Shell scripting for data pipelines
- [Homework](03_Shell_Programming/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](03_Shell_Programming/links.txt)

**Tools:** `bash`, `jq`, `awk`, `printf`

---

### 4. Coreutils Data Transformation

Building blocks for efficient data pipelines.

**Topics:** Field manipulation, sorting, splitting datasets, stream buffering & monitoring

**Materials:**
- [Lecture](04_Coreutils/lecture.md) - Coreutils for data processing
- [Homework](04_Coreutils/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](04_Coreutils/links.txt)

**Tools:** `cat`, `cut`, `paste`, `tr`, `sort`, `uniq`, `split`, `pv`, `stdbuf`

---

### 5. grep, sed, awk — The Text Processing Trio

Master text filtering, transformation, and analytics.

**Topics:** Regular expressions, stream editing, field-based analytics

**Materials:**
- [Lecture](05_Grep_Sed_Awk/lecture.md) - Complete text processing guide
- [Sample Data](05_Grep_Sed_Awk/DataSamples.md) - Practice datasets
- [Homework](05_Grep_Sed_Awk/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](05_Grep_Sed_Awk/links.txt)

**Tools:** `grep`, `sed`, `awk`

---

### 6. Structured Data: CSV, JSON, YAML, XML

Working with structured data formats.

**Topics:** JSON parsing with jq, CSV with csvkit/mlr, YAML with yq, XML with xmlstarlet

**Materials:**
- [Lecture](06_Structured_Data/lecture.md) - Structured data processing
- [Sample Data](06_Structured_Data/DataSamples.md) - Practice datasets
- [Homework](06_Structured_Data/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](06_Structured_Data/links.txt)

**Tools:** `jq`, `csvkit`, `mlr`, `yq`, `xmlstarlet`

---

### 7. Streaming Analytics & Aggregations

Analytical queries using CLI tools.

**Topics:** Streaming joins, group-by, reduce, column statistics, multi-field grouping

**Materials:**
- [Lecture](07_Streaming_Analytics/lecture.md) - Analytics without loading into memory
- [Sample Data](07_Streaming_Analytics/DataSamples.md) - Practice datasets
- [Homework](07_Streaming_Analytics/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](07_Streaming_Analytics/links.txt)

**Tools:** `awk`, `datamash`, `mlr`, `sort`, `join`

---

### 8. Log Processing & API Pipelines

Working with logs and REST APIs.

**Topics:** JSONL format, gzip streaming, REST API pipelines, report generation

**Materials:**
- [Lecture](08_Log_Processing/lecture.md) - Log and API data processing
- [Sample Data](08_Log_Processing/DataSamples.md) - Practice datasets
- [Homework](08_Log_Processing/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](08_Log_Processing/links.txt)

**Tools:** `curl`, `jq`, `zcat`, `datamash`, `column`

---

### 9. Performance & Parallelism

Optimizing pipeline performance.

**Topics:** GNU parallel, xargs -P, external sorting optimization, profiling

**Materials:**
- [Lecture](09_Performance_Parallelism/lecture.md) - Performance optimization techniques
- [Homework](09_Performance_Parallelism/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](09_Performance_Parallelism/links.txt)

**Tools:** `parallel`, `xargs`, `pv`, `time`, `dstat`, `sort`

---

### 10. Streams, IPC & Unix Sockets

Inter-process communication and advanced streaming.

**Topics:** Named pipes (FIFO), Unix domain sockets, Shell↔Python IPC, buffering control

**Materials:**
- [Lecture](10_Streams_IPC/lecture.md) - IPC and advanced streaming
- [Homework](10_Streams_IPC/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](10_Streams_IPC/links.txt)

**Tools:** `mkfifo`, `socat`, `nc`, Python `socket`

---

### 11. Bash as a Glue Language

Writing robust production scripts.

**Topics:** Error handling with `trap`, `.env` configuration, temporary files, signal handling

**Materials:**
- [Lecture](11_Bash_Glue/lecture.md) - Production-ready scripting
- [Homework](11_Bash_Glue/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](11_Bash_Glue/links.txt)

**Tools:** `bash`, `trap`, `mktemp`, `env`

---

### 12. Python in Pipelines

Integrating Python into Unix workflows.

**Topics:** Python as stream filter, stdin/stdout, pandas vs mlr, hybrid pipelines

**Materials:**
- [Lecture](12_Python_Pipelines/lecture.md) - Python integration patterns
- [Homework](12_Python_Pipelines/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](12_Python_Pipelines/links.txt)

**Tools:** `python`, `jq`, `mlr`, `pandas`

---

### 13. Complex Pipeline Architecture

Building large, maintainable pipelines.

**Topics:** Map/reduce patterns, checkpoints, staging, Makefile orchestration, reproducibility

**Materials:**
- [Lecture](13_Complex_Pipelines/lecture.md) - Production pipeline architecture
- [Homework](13_Complex_Pipelines/hw.txt) - 10 assignments + 5 bonus challenges
- [Resources](13_Complex_Pipelines/links.txt)

**Tools:** `parallel`, `split`, `make`, `mktemp`

---

### 14. Final Project — Data Pipeline Challenge

Build a complete production-ready ETL pipeline.

**Requirements:**
- Process 5GB+ of JSONL or CSV data
- Use streaming and parallel processing
- Convert between formats (JSON↔CSV↔Markdown)
- Implement checkpoints & logging
- Integrate Bash with Python

**Materials:**
- [Project Requirements](14_Final_Project/lecture.md) - Full project specification
- [Homework](14_Final_Project/hw.txt) - Deliverables checklist

**Evaluation:** Correctness (40%), Performance (20%), Code Quality (20%), Documentation (20%)

---

## 🎯 Learning Path

### Progression
```
Core Concepts → Stream Processing → Structured Data → Scaling → Complex Architecture
```

1. **Unix Streams** - Think in terms of data flows
2. **Files & I-nodes** - Understand the file system
3. **Shell Programming** - Write reusable scripts
4. **Coreutils** - Master the building blocks
5. **grep/sed/awk** - Text processing power
6. **Structured Data** - Handle JSON, CSV, YAML
7. **Analytics** - Aggregate without loading into memory
8. **Logs & APIs** - Real-world data sources
9. **Performance** - Parallelize and optimize
10. **IPC** - Advanced inter-process communication
11. **Bash Glue** - Production-ready scripts
12. **Python Pipes** - Hybrid workflows
13. **Architecture** - Large pipeline design
14. **Final Project** - Apply everything

---

## 📖 How to Use This Course

### For Each Module:
1. **Read the lecture** (lecture.md) - Theory and examples
2. **Practice with sample data** (DataSamples.md) - Where available
3. **Complete homework** (hw.txt) - 10 assignments per module
4. **Explore resources** (links.txt) - Deepen understanding
5. **Take the quiz** (quiz.md) - Self-assessment

### Study Tips:
- Start with small data samples, then scale up
- Test each pipeline stage independently
- Use `head` to limit output during development
- Save intermediate results when debugging

---

## 🛠️ Prerequisites

### Required Tools
- Linux/macOS terminal (or WSL on Windows)
- `bash` 4.0+
- Core utilities: `grep`, `sed`, `awk`, `sort`, `uniq`, `cut`

### Recommended Tools
- `jq` - JSON processor
- `mlr` (Miller) - CSV/JSON Swiss Army knife
- `parallel` - GNU Parallel
- `pv` - Pipe Viewer
- Python 3.8+ with `pandas`

### Installation (Ubuntu/Debian)
```bash
sudo apt install jq miller parallel pv csvkit
pip install pandas
```

### Installation (macOS)
```bash
brew install jq miller parallel pv csvkit
pip install pandas
```

---

## 📚 Recommended Resources

- [Data Science at the Command Line](https://datascienceatthecommandline.com/)
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
- [Bash Hackers Wiki](https://wiki.bash-hackers.org/)
- `man` pages: `man bash`, `man awk`, `man jq`

---

Happy piping! 🚀
