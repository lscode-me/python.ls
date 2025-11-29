# Python and Linux for Life Science Developers

A comprehensive course designed for life science professionals looking to develop programming and computational skills. This course covers Python fundamentals, Linux command line essentials, and practical applications for bioinformatics and data analysis in life sciences.

---

## 🐍 Python Core Foundations

### 1. Objects, References, Memory, Types
- [Objects](Python/Objects/Objects.md) - Python object model and references
- [Operations](Python/Objects/Operations.md) - Working with Python objects

### 2. OOP (Object-Oriented Programming)
- [Attributes and Methods](Python/OOP/AttributesAndMethods.md) - Deep dive into class members
- [OOP Basics](Python/OOP/OOP_Basics.md) - Classes, inheritance, polymorphism
- [Advanced OOP](Python/OOP/Advanced_OOP.md) - Decorators, dataclasses, metaclasses

### 3. Functions and Functional Programming
- [Functions](Python/Functions/Functions.md) - Arguments, closures, decorators, FP patterns

### 4. Protocols and Interfaces
- [Protocols](Python/Protocols/Protocols.md) - Duck typing, protocols, ABCs

### 5. Iteration Protocol
- [Iteration](Python/Iteration/Iteration.md) - Iterators, generators, itertools

### 6. File Handling
- [Files](Python/Files/Files.md) - File I/O, formats, pathlib

### 7. Pythonic Code
- [Pythonic](Python/Pythonic/Pythonic.md) - Writing idiomatic Python

### 8. Python for Bioinformatics
- [Bioinformatics](Python/Bioinformatics/Bioinformatics.md) - Sequence analysis, BioPython

📖 **[Python Course README](Python/README.md)** - Full course guide with learning path

---

## 🐧 Linux for Developers: Unix & Data Pipelines

### 1. Unix as a Language of Data & Streams
- [Lecture](Linux/01_Unix_Streams/lecture.md) - Unix philosophy, pipes, Filter→Transform→Aggregate
- [Sample Data](Linux/01_Unix_Streams/DataSamples.md)

### 2. Files, I-nodes & File Descriptors
- [Lecture](Linux/02_Files_Inodes_Descriptors/lecture.md) - I-nodes, file descriptors, permissions, file types

### 3. Shell Programming
- [Lecture](Linux/03_Shell_Programming/lecture.md) - Bash as DSL, loops, functions, error handling

### 4. Coreutils Data Transformation
- [Lecture](Linux/04_Coreutils/lecture.md) - cut, paste, sort, uniq, split, pv, stdbuf

### 5. grep, sed, awk — Text Processing Trio
- [Lecture](Linux/05_Grep_Sed_Awk/lecture.md) - Regular expressions, stream editing, analytics
- [Sample Data](Linux/05_Grep_Sed_Awk/DataSamples.md)

### 6. Structured Data: CSV, JSON, YAML, XML
- [Lecture](Linux/06_Structured_Data/lecture.md) - jq, csvkit, mlr, yq, xmlstarlet
- [Sample Data](Linux/06_Structured_Data/DataSamples.md)

### 7. Streaming Analytics & Aggregations
- [Lecture](Linux/07_Streaming_Analytics/lecture.md) - Joins, group-by, reduce, statistics
- [Sample Data](Linux/07_Streaming_Analytics/DataSamples.md)

### 8. Log Processing & API Pipelines
- [Lecture](Linux/08_Log_Processing/lecture.md) - JSONL, gzip streaming, REST APIs
- [Sample Data](Linux/08_Log_Processing/DataSamples.md)

### 9. Performance & Parallelism
- [Lecture](Linux/09_Performance_Parallelism/lecture.md) - GNU parallel, xargs -P, sort tuning, profiling

### 10. Streams, IPC & Unix Sockets
- [Lecture](Linux/10_Streams_IPC/lecture.md) - Named pipes (FIFO), Unix sockets, Shell↔Python IPC

### 11. Bash as a Glue Language
- [Lecture](Linux/11_Bash_Glue/lecture.md) - Error handling, trap, .env config, temp files

### 12. Python in Pipelines
- [Lecture](Linux/12_Python_Pipelines/lecture.md) - Python as stream filter, pandas vs mlr

### 13. Complex Pipeline Architecture
- [Lecture](Linux/13_Complex_Pipelines/lecture.md) - Map/reduce, checkpoints, Makefile orchestration

### 14. Final Project
- [Project Requirements](Linux/14_Final_Project/lecture.md) - Build a complete ETL pipeline (5GB+ data)

📖 **[Linux Course README](Linux/README.md)** - Full course guide with learning path

---

## 📚 Course Structure

Each topic includes:
- **lecture.md** - Theory and examples
- **hw.txt** - Homework assignments
- **links.txt** - Additional resources
- **quiz.md** - Self-assessment questions
- **DataSamples.md** - Sample data for practice (some modules)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Linux/macOS terminal (or WSL on Windows)
- Text editor or IDE

### Quick Start
```bash
# Clone the repository
git clone <repo-url>
cd python.ls

# Start with Python or Linux track
# Read lecture → Complete homework → Explore resources
```

Happy learning! 🎓
