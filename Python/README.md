# Python for Life Science Developers

A comprehensive Python course designed for life science professionals. This course covers Python fundamentals, object-oriented programming, functional programming, and practical applications for bioinformatics and data analysis.

## Course Overview

This course takes you from Python basics to advanced concepts, with a focus on writing clean, efficient, and Pythonic code. Each lecture includes theory, practical examples, homework assignments, and curated resources.

---

## 📚 Course Contents

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
- [Objects.md](Objects/Objects.md) - Core concepts and theory
- [Operations.md](Objects/Operations.md) - Working with Python objects
- [Homework Assignments](Objects/hw.txt) - 6 practical exercises
- [Resources](Objects/links.txt) - Curated learning materials

---

### 2. Object-Oriented Programming (OOP)

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
- [AttributesAndMethods.md](OOP/AttributesAndMethods.md) - Attributes and methods deep dive
- [OOP_Basics.md](OOP/OOP_Basics.md) - Core OOP concepts
- [Advanced_OOP.md](OOP/Advanced_OOP.md) - Advanced patterns and techniques
- [Homework Assignments](OOP/hw.txt) - 8 comprehensive projects
- [Resources](OOP/links.txt) - OOP learning materials

---

### 3. Functions and Functional Programming

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
- [Functions.md](Functions/Functions.md) - Complete function guide
- [Homework Assignments](Functions/hw.txt) - 8 functional programming challenges
- [Resources](Functions/links.txt) - FP learning resources

---

### 4. Protocols and Interfaces

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
- [Protocols.md](Protocols/Protocols.md) - Protocol system explained
- [Homework Assignments](Protocols/hw.txt) - 8 protocol implementation tasks
- [Resources](Protocols/links.txt) - Protocol and interface resources

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
- [Iteration.md](Iteration/Iteration.md) - Complete iteration guide
- [Homework Assignments](Iteration/hw.txt) - 10 iteration challenges
- [Resources](Iteration/links.txt) - Iteration learning materials

---

### 6. File Handling

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
- [Files.md](Files/Files.md) - Complete file handling guide
- [Homework Assignments](Files/hw.txt) - 10 file processing projects
- [Resources](Files/links.txt) - File I/O resources

---

### 7. Streams and Unix I/O

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
- [Streams.md](Streams/Streams.md) - Complete Unix I/O guide
- [Homework Assignments](Streams/hw.md) - 10 CLI utility projects
- [Quiz](Streams/quiz.md) - Test your knowledge
- [Resources](Streams/links.md) - CLI tools and Unix resources

---

### 8. Pythonic Code

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
- [Pythonic.md](Pythonic/Pythonic.md) - Writing idiomatic Python
- [Homework Assignments](Pythonic/hw.txt) - Code refactoring exercises
- [Resources](Pythonic/links.txt) - Extensive Pythonic resources

---

### 9. Python for Bioinformatics

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
- [Bioinformatics.md](Bioinformatics/Bioinformatics.md) - Python for biological data
- [Homework Assignments](Bioinformatics/hw.txt) - 12 practical bioinformatics projects
- [Resources](Bioinformatics/links.txt) - Comprehensive bioinformatics resources

---

## 🎯 Learning Path

### Recommended Order
1. **Objects** - Understand Python's foundation
2. **OOP** - Master object-oriented design
3. **Functions** - Learn functional programming
4. **Protocols** - Understand Python's interface system
5. **Iteration** - Master efficient data processing
6. **Files** - Handle real-world data
7. **Streams** - Build Unix-style command-line tools
8. **Pythonic** - Polish your Python skills
9. **Bioinformatics** - Apply Python to life sciences (capstone)

### Prerequisites
- Basic programming knowledge
- Python 3.8+ installed
- Text editor or IDE (VS Code, PyCharm recommended)

---

## 📖 How to Use This Course

### For Each Topic:
1. **Read the lecture notes** (.md files) - Theory and examples
2. **Complete homework assignments** (hw.txt) - Hands-on practice
3. **Explore resources** (links.txt) - Deepen your understanding
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
2. **OOP** - Library management system
3. **Functions** - Data processing pipeline
4. **Protocols** - Custom collection classes
5. **Iteration** - Log file analyzer
6. **Files** - File-based database
7. **Streams** - Unix-style text processing toolkit
8. **Pythonic** - Code refactoring tool
9. **Bioinformatics** - Sequence analysis pipeline

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
