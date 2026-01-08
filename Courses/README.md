# Python and Linux for Life Science Developers

A comprehensive course designed for life science professionals looking to develop programming and computational skills. This course covers data fundamentals, Python programming, Linux command line essentials, and practical applications for bioinformatics and healthcare data analysis.

---

## 📚 Courses

### 📊 Data Fundamentals for Life Sciences

**12 modules** covering essential data concepts, encodings, file formats, and data processing fundamentals.

Master character encodings, JSON/YAML/CSV formats, compression, checksums, and data transfer protocols. This foundational course prepares you for the Python and Linux tracks.

**→ [Data Fundamentals Course](DataFundamentals/README.md)** - Full course contents, learning path, and materials

---

### 🐍 Python for Life Science Developers

**11 modules** covering Python fundamentals, OOP, functional programming, coroutines, and bioinformatics applications.

From objects and memory management to coroutines and data pipelines, culminating in BioPython and sequence analysis. Learn to write clean, efficient, Pythonic code for life science applications.

**→ [Python Course](Python/README.md)** - Full course contents, learning path, and materials

---

### 🐧 Linux for Developers: Unix & Data Pipelines

**14 modules** teaching Unix tools, shell scripting, and CLI-based data processing.

Master stream processing, structured data formats, performance optimization, and build production-ready ETL pipelines.

**→ [Linux Course](Linux/README.md)** - Full course contents, learning path, and materials

**→ [Sample Data](Linux/data/DataSamples.md)** - Unified practice datasets for all modules

---

## 📚 Course Structure

Each topic includes:
- **lecture.md** - Theory and examples
- **hw.md** - Homework assignments
- **links.md** - Additional resources
- **quiz.md** - Self-assessment questions

---

## 🎯 Target Audience

This curriculum is specifically designed for:
- **Bioinformaticians** - Process genomic data, analyze sequences, build pipelines
- **Life Science Researchers** - Automate lab data processing and analysis
- **Healthcare Data Engineers** - Work with medical records, clinical data, and health informatics
- **Computational Biologists** - Develop tools for biological data analysis

---

## 🗺️ Learning Path

### Recommended Progression

```
┌─────────────────────────────────────────────────────────────────┐
│                    Data Fundamentals (12 modules)                │
│  Encodings → File Formats → JSON/YAML → CSV → Compression       │
└─────────────────┬───────────────────────────────────────────────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
┌─────────────────┐  ┌─────────────────┐
│  Python Track   │  │  Linux Track    │
│  (11 modules)   │  │  (14 modules)   │
└────────┬────────┘  └────────┬────────┘
         │                    │
         └─────────┬──────────┘
                   ▼
         ┌──────────────────┐
         │  Bioinformatics  │
         │  Applications    │
         └──────────────────┘
```

### Three Tracks

1. **Start with Data Fundamentals** (if new to data formats)
   - Learn about encodings, file formats, and data structures
   - Understand JSON, YAML, CSV, and compression
   - Foundation for both Python and Linux tracks

2. **Python Track** (for programming and bioinformatics)
   - Master Python for data analysis and bioinformatics
   - Build computational tools and pipelines
   - Culminates in BioPython and sequence analysis

3. **Linux Track** (for data engineering and pipelines)
   - Master Unix tools and shell scripting
   - Build streaming ETL pipelines
   - Integrate Unix tools with Python

### Course Connections

- **DataFundamentals → Python**: Learn file formats, then process them with Python
- **DataFundamentals → Linux**: Understand data structures, then manipulate with Unix tools
- **Python + Linux**: Build hybrid pipelines combining both approaches
- **All Three → Bioinformatics**: Apply everything to genomic data analysis

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Linux/macOS terminal (or WSL on Windows)
- Text editor or IDE (VS Code, PyCharm recommended)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/orasul/python.ls.git
cd python.ls

# Recommended: Start with Data Fundamentals
cd DataFundamentals
# Read README → Start with 01_Intro

# Or jump to Python or Linux tracks if you have the foundation
```

---

## 📖 How to Use This Curriculum

### For Beginners
1. Complete **Data Fundamentals** first
2. Choose **Python** or **Linux** based on your goals
3. Complete the other track
4. Work on integrated projects

### For Experienced Developers
- Skip to topics you need
- Use as a reference
- Focus on bioinformatics modules

### For Each Module
1. Read lecture notes (theory and examples)
2. Complete homework assignments (hands-on practice)
3. Explore additional resources
4. Take the quiz (self-assessment)

---

## 💡 Real-World Applications

### Bioinformatics
- Sequence alignment and analysis
- Variant calling pipelines
- Gene expression analysis
- Phylogenetic tree construction
- FASTA/FASTQ file processing
- Integration with NCBI, UniProt, Ensembl

### Healthcare Data Engineering
- Electronic health record (EHR) processing
- Clinical data pipelines
- Medical image metadata handling
- Lab result automation
- Healthcare data format conversion

### Data Science
- Experimental data analysis
- Automated reporting
- Data cleaning and validation
- Statistical analysis pipelines
- Visualization for publications

---

Happy learning! 🎓
