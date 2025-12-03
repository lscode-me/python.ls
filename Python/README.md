# Python for Life Science Developers

A comprehensive Python course designed for life science professionals. This course covers Python fundamentals, object-oriented programming, functional programming, and practical applications for bioinformatics and data analysis.

## Course Overview

This course takes you from Python basics to advanced concepts, with a focus on writing clean, efficient, and Pythonic code. Each lecture includes theory, practical examples, homework assignments, and curated resources.

---

## 📚 Course Contents (11 Modules)

### 1. Objects, References, Memory, Types

Understanding Python's object model, memory management, and core data types.

**Topics Covered:**
- Python object model and references
- Built-in data types (immutable and mutable)
- Reference counting and garbage collection
- Memory management in CPython
- Identity vs equality (`is` vs `==`)
- Common pitfalls (mutable default arguments)

**Materials:**
- [Lecture](01_Objects/lecture.md) - Core concepts and theory
- [Homework Assignments](01_Objects/hw.md) - 6 practical exercises
- [Resources](01_Objects/links.md) - Curated learning materials
- [Quiz](01_Objects/quiz.md) - Test your knowledge

---

### 2. Functions and Functional Programming

From basic functions to advanced functional programming patterns.

**Topics Covered:**
- Function arguments (*args, **kwargs)
- Scope and namespaces
- Lambda functions
- Closures and factory functions
- Decorators
- Higher-order functions (map, filter, reduce)
- Generator functions
- Recursion
- Type hints and annotations
- Functional programming concepts

**Materials:**
- [Lecture](02_Functions/lecture.md) - Complete function guide
- [Homework Assignments](02_Functions/hw.md) - 8 functional programming challenges
- [Resources](02_Functions/links.md) - FP learning resources
- [Quiz](02_Functions/quiz.md) - Test your knowledge

---

### 3. File Handling

Comprehensive file I/O operations and data format handling.

**Topics Covered:**
- File modes and operations
- Reading and writing files
- Text encodings
- Binary files
- pathlib for modern path operations
- Directory operations
- CSV and JSON file handling
- Temporary files
- File compression (ZIP, GZIP)
- Performance and buffering

**Materials:**
- [Lecture](03_Files/lecture.md) - Complete file handling guide
- [Homework Assignments](03_Files/hw.md) - 10 file processing projects
- [Resources](03_Files/links.md) - File I/O resources
- [Quiz](03_Files/quiz.md) - Test your knowledge

---

### 4. Testing in Python

Writing reliable code with pytest, unittest, and Test-Driven Development.

**Topics Covered:**
- unittest vs pytest
- Writing effective tests
- Fixtures and setup/teardown
- Parametrized tests
- Mocking and patching
- Test coverage
- Test-Driven Development (TDD)
- Integration vs unit tests
- Best practices and patterns
- Continuous Integration

**Materials:**
- [Lecture](04_Testing/lecture.md) - Complete testing guide
- [Homework Assignments](04_Testing/hw.md) - 12 testing challenges
- [Resources](04_Testing/links.md) - Testing frameworks and tools
- [Quiz](04_Testing/quiz.md) - Test your knowledge

---

### 5. Iteration Protocol

Master iterators, generators, and efficient data processing.

**Topics Covered:**
- Iterator protocol (\_\_iter\_\_ and \_\_next\_\_)
- Creating custom iterators
- Generator functions and yield
- Generator expressions
- Generator methods (send, throw, close)
- yield from delegation
- itertools module mastery
- Lazy evaluation and memory efficiency
- Infinite sequences
- Real-world iteration patterns

**Materials:**
- [Lecture](05_Iteration/lecture.md) - Complete iteration guide
- [Homework Assignments](05_Iteration/hw.md) - 10 iteration challenges
- [Resources](05_Iteration/links.md) - Iteration learning materials
- [Quiz](05_Iteration/quiz.md) - Test your knowledge

---

### 6. Streams and Unix I/O

Learn to write Unix-style command-line utilities in Python.

**Topics Covered:**
- Unix philosophy applied to Python
- Standard streams (stdin, stdout, stderr)
- Reading from stdin efficiently
- Writing to stdout and stderr correctly
- Command-line argument parsing with argparse
- Building pipeable filters and processors
- Buffering and performance considerations
- Signal handling (SIGINT, BrokenPipeError, KeyboardInterrupt)
- Creating composable Unix-style utilities
- Working with CSV, JSON, and structured data streams
- Creating pipelines in Python
- Binary data handling
- Progress monitoring and logging
- Best practices and templates for CLI tools

**Materials:**
- [Lecture](06_Streams/lecture.md) - Complete Unix I/O guide
- [Homework Assignments](06_Streams/hw.md) - 10 CLI utility projects
- [Resources](06_Streams/links.md) - CLI tools and Unix resources
- [Quiz](06_Streams/quiz.md) - Test your knowledge

---

### 7. Coroutines and Data Pipelines

Master coroutines for building push-based data processing pipelines.

**Topics Covered:**
- From generators to coroutines
- The `send()` pattern and coroutine priming
- Bidirectional communication (yield for both producing and consuming)
- Push vs Pull data processing models
- Building coroutine-based pipelines (filter → map → sink)
- Pipeline components: filters, mappers, broadcasters (tee), sinks
- Stateful data processing with coroutines
- Real-time log processing and ETL pipelines
- Windowing, batching, and aggregation patterns
- Error handling and pipeline cleanup
- Branching and multi-consumer pipelines
- Performance optimization for streaming data
- Comparison with iterator-based (pull) pipelines
- Production-ready pipeline patterns

**Materials:**
- [Lecture](07_Coroutines/lecture.md) - Complete coroutines and pipeline guide
- [Homework Assignments](07_Coroutines/hw.md) - 8 pipeline projects (basic to expert)
- [Resources](07_Coroutines/links.md) - David Beazley's tutorials and more
- [Quiz](07_Coroutines/quiz.md) - Test your knowledge

---

### 8. Object-Oriented Programming (OOP)

Master classes, inheritance, encapsulation, and design patterns.

**Topics Covered:**
- Classes and objects
- Instance vs class attributes
- Methods (instance, class, static)
- Inheritance and polymorphism
- Encapsulation and access control
- Abstract base classes
- Special methods (magic methods)
- Properties and descriptors
- Composition vs inheritance
- Advanced OOP (decorators, dataclasses, metaclasses, slots)

**Materials:**
- [Lecture](08_OOP/lecture.md) - Core OOP concepts and advanced patterns
- [Homework Assignments](08_OOP/hw.md) - 8 comprehensive projects
- [Resources](08_OOP/links.md) - OOP learning materials
- [Quiz](08_OOP/quiz.md) - Test your knowledge

---

### 9. Pythonic Code

Write beautiful, idiomatic Python code following best practices.

**Topics Covered:**
- The Zen of Python
- PEP 8 style guide
- List comprehensions and generator expressions
- Context managers (with statement)
- EAFP vs LBYL
- Pythonic idioms (enumerate, zip, unpacking)
- Code quality tools (Black, pylint, mypy)
- Performance optimization
- Common anti-patterns to avoid

**Materials:**
- [Lecture](09_Pythonic/lecture.md) - Writing idiomatic Python
- [Homework Assignments](09_Pythonic/hw.md) - Code refactoring exercises
- [Resources](09_Pythonic/links.md) - Extensive Pythonic resources
- [Quiz](09_Pythonic/quiz.md) - Test your knowledge

---

### 10. Protocols and Interfaces

Understanding Python's protocol system and creating flexible interfaces.

**Topics Covered:**
- Duck typing philosophy
- Built-in protocols (sequence, iterator, container, callable)
- Context manager protocol
- Numeric and comparison protocols
- typing.Protocol (structural subtyping)
- Abstract Base Classes (ABC)
- Collections ABCs
- Protocols vs ABC: when to use each

**Materials:**
- [Lecture](10_Protocols/lecture.md) - Protocol system explained
- [Homework Assignments](10_Protocols/hw.md) - 8 protocol implementation tasks
- [Resources](10_Protocols/links.md) - Protocol and interface resources
- [Quiz](10_Protocols/quiz.md) - Test your knowledge

---

### 11. Python for Bioinformatics

Apply Python to real-world bioinformatics problems and biological data analysis.

**Topics Covered:**
- DNA, RNA, and protein sequence analysis
- Genetic code and translation
- FASTA and FASTQ file parsing
- Sequence alignment algorithms (Needleman-Wunsch, Smith-Waterman)
- BioPython library essentials
- Working with biological databases (NCBI, UniProt)
- Sequence motif finding
- Open Reading Frame (ORF) detection
- Multiple sequence alignment
- Phylogenetic analysis basics
- Real-world bioinformatics workflows

**Materials:**
- [Lecture](11_Bioinformatics/lecture.md) - Python for biological data
- [Homework Assignments](11_Bioinformatics/hw.md) - 12 practical bioinformatics projects
- [Resources](11_Bioinformatics/links.md) - Comprehensive bioinformatics resources
- [Quiz](11_Bioinformatics/quiz.md) - Test your knowledge

---

## 🎯 Learning Path

### Recommended Order
1. **Objects** - Understand Python's foundation
2. **Functions** - Learn functional programming
3. **Files** - Handle real-world data
4. **Testing** - Write reliable, testable code
5. **Iteration** - Master efficient data processing
6. **Streams** - Build Unix-style command-line tools
7. **Coroutines** - Master push-based data pipelines
8. **OOP** - Master object-oriented design
9. **Pythonic** - Polish your Python skills
10. **Protocols** - Understand Python's interface system
11. **Bioinformatics** - Apply Python to life sciences (capstone)

### Prerequisites
- Basic programming knowledge
- Python 3.8+ installed
- Text editor or IDE (VS Code, PyCharm recommended)

---

## 📖 How to Use This Course

### For Each Topic:
1. **Read the lecture notes** (.md files) - Theory and examples
2. **Complete homework assignments** (hw.md) - Hands-on practice
3. **Explore resources** (links.md) - Deepen your understanding
4. **Take the quiz** (quiz.md) - Test your knowledge
4. **Build projects** - Apply what you've learned

### Study Tips:
- Code along with examples
- Experiment in Python REPL or Jupyter notebooks
- Complete all homework assignments
- Review and refactor your code
- Read other people's code (GitHub, open source)

---

## 🛠️ Tools and Resources

### Essential Tools
- **Python 3.8+** - Latest Python version
- **pip** - Package manager
- **venv** - Virtual environments
- **IPython/Jupyter** - Interactive development
- **VS Code/PyCharm** - IDEs with Python support

### Code Quality Tools
- **Black** - Code formatter
- **pylint** - Code analysis
- **flake8** - Style checker
- **mypy** - Static type checker
- **isort** - Import organizer

### Useful Libraries
- **pytest** - Testing framework
- **requests** - HTTP library
- **pandas** - Data analysis
- **numpy** - Numerical computing
- **matplotlib** - Visualization

---

## 🧪 Practice and Projects

### Mini Projects by Topic
1. **Objects** - Memory profiler tool
2. **Functions** - Data processing pipeline
3. **Files** - File-based database
4. **Testing** - Test suite for existing project
5. **Iteration** - Log file analyzer
6. **Streams** - Unix-style text processing toolkit
7. **Coroutines** - Real-time log monitoring system
8. **OOP** - Library management system
9. **Pythonic** - Code refactoring tool
10. **Protocols** - Custom collection classes
11. **Bioinformatics** - Sequence analysis pipeline

### Final Project Ideas
- Complete genomic sequence analyzer with visualization
- NGS data quality control and filtering pipeline
- Phylogenetic tree builder with multiple alignment
- Protein structure analyzer and property predictor
- Gene finder with functional annotation
- BLAST-like sequence similarity search tool
- Laboratory data management system with database integration

---

## 📚 Recommended Books

1. **"Fluent Python"** by Luciano Ramalho - Deep dive into Python
2. **"Effective Python"** by Brett Slatkin - 90 best practices
3. **"Python Tricks"** by Dan Bader - Practical tips
4. **"Python Cookbook"** by David Beazley - Problem-solving recipes

---

## 🌐 Online Resources

### Official Documentation
- [Python.org Documentation](https://docs.python.org/3/)
- [Python PEPs](https://www.python.org/dev/peps/)
- [Python Standard Library](https://docs.python.org/3/library/)

### Learning Platforms
- [Real Python](https://realpython.com/)
- [Python Morsels](https://www.pythonmorsels.com/)
- [Exercism - Python Track](https://exercism.org/tracks/python)

### Community
- [r/learnpython](https://www.reddit.com/r/learnpython/)
- [Python Discord](https://discord.gg/python)
- [Stack Overflow - Python](https://stackoverflow.com/questions/tagged/python)

---

## 💡 Tips for Life Science Developers

### Relevant Applications
- Sequence analysis and alignment
- Statistical analysis of experimental data
- Data visualization for publications
- Automated data processing pipelines
- Integration with lab instruments
- Database management for research data

### Domain-Specific Libraries
- **BioPython** - Biological computation (covered in detail)
- **scipy/numpy** - Scientific computing
- **pandas** - Data manipulation and analysis
- **matplotlib/seaborn** - Visualization
- **scikit-learn** - Machine learning
- **pysam** - SAM/BAM file handling
- **PyVCF** - Variant calling format
- **HTSeq** - High-throughput sequencing analysis

---

## 🤝 Contributing

Found an error or have a suggestion? Feel free to:
- Open an issue
- Submit a pull request
- Share your feedback

---

## 📝 License

This course material is provided for educational purposes.

---

## 🚀 Next Steps

After completing this Python course:
1. Explore the **Linux for Developers** section
2. Build real-world projects
3. Contribute to open source
4. Apply skills to your research
5. Share knowledge with others

Happy coding! 🐍
