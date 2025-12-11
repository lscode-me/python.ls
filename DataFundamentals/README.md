# Data Fundamentals for Life Sciences
## Essential Concepts: Data Formats, Encodings, and File Handling

---

## 📚 About This Course

This course covers fundamental data concepts that every life science professional should understand. We explore essential topics that are often sources of problems and confusion: character encodings, file formats, structured data, compression, and more.

Understanding these fundamentals is crucial for bioinformatics, healthcare data engineering, and computational biology work, where data integrity and proper format handling can make or break your analysis pipeline.

### Target Audience

- **Bioinformaticians** - Work with genomic data files (FASTA, FASTQ, VCF, BAM)
- **Life Science Researchers** - Process experimental data and lab results
- **Healthcare Data Engineers** - Handle medical records and clinical data
- **Computational Biologists** - Build data analysis pipelines
- **Data Scientists in Life Sciences** - Analyze biological and medical datasets

### Prerequisites

- Basic computer literacy
- Command-line experience (recommended)
- Understanding of basic programming concepts (recommended)
- No biology background required - we'll explain biological context where needed

---

## 🗺️ Course Structure

### Section 1: Data Representation Fundamentals

| Module | Topic | Description |
|--------|-------|-------------|
| [01_Intro](./01_Intro/) | Introduction | What are data, information, and formats |
| [02_NumberSystems](./02_NumberSystems/) | Number Systems | Bits, bytes, hex, binary, endianness |
| [03_Encodings](./03_Encodings/) | Character Encodings | ASCII, Unicode, UTF-8, history and problems |

### Section 2: File Formats

| Module | Topic | Description |
|--------|-------|-------------|
| [04_FileFormats](./04_FileFormats/) | File Formats | Text vs binary, magic numbers, MIME types |
| [05_JSON](./05_JSON/) | JSON | Syntax, validation, tools (jq) |
| [06_YAML](./06_YAML/) | YAML | Syntax, features, comparison with JSON |

### Section 3: Markup and Configuration

| Module | Topic | Description |
|--------|-------|-------------|
| [07_Markup](./07_Markup/) | Markup Languages | HTML, XML, Markdown |
| [08_ConfigFiles](./08_ConfigFiles/) | Configuration Files | INI, TOML, .env, properties |

### Section 4: Working with Data

| Module | Topic | Description |
|--------|-------|-------------|
| [09_TabularData](./09_TabularData/) | Tabular Data | CSV, TSV, parsing and generation |
| [10_Compression](./10_Compression/) | Data Compression | gzip, bzip2, tar, archives |
| [11_Checksums](./11_Checksums/) | Hashes and Checksums | MD5, SHA, applications |
| [12_DataTransfer](./12_DataTransfer/) | Transfer Encoding | Base64, URL encoding, MIME types |

---

## 🎯 Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                  Data Fundamentals Course                        │
└─────────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌─────────┐         ┌─────────┐         ┌─────────┐
    │  Intro  │─────────│ Number  │─────────│Encodings│
    │  Data   │         │ Systems │         │ (UTF-8) │
    └─────────┘         └─────────┘         └─────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌─────────┐         ┌─────────┐         ┌─────────┐
    │  File   │─────────│  JSON   │─────────│  YAML   │
    │ Formats │         │         │         │         │
    └─────────┘         └─────────┘         └─────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌─────────┐         ┌─────────┐         ┌─────────┐
    │ Markup  │─────────│ Config  │─────────│ Tabular │
    │(HTML/MD)│         │ Files   │         │  Data   │
    └─────────┘         └─────────┘         └─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌───────────┐   ┌───────────┐   ┌───────────┐
        │Compression│   │ Checksums │   │  Data     │
        │ (gzip/tar)│   │  (SHA256) │   │ Transfer  │
        └───────────┘   └───────────┘   └───────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Apply to Life   │
                    │  Science Data    │
                    │  (Python/Linux)  │
                    └──────────────────┘
```

---

## 📋 Module Format

Each module contains:

```
XX_ModuleName/
├── lecture.md    # Main lecture material
└── quiz.md       # Self-assessment questions
```

### Lecture Structure

- **Prerequisites** — What you need to know before starting
- **Learning Objectives** — What you'll learn
- **Main Content** — Theory with practical examples
- **Life Science Applications** — How this applies to bioinformatics
- **Key Takeaways** — Main conclusions
- **Next Steps** — What to study next
- **Additional Resources** — Further reading and tools

### Quiz

- 15-20 multiple-choice questions
- Answers with explanations
- Performance recommendations

---

## 🔬 Life Science Applications

### Why Data Fundamentals Matter in Life Sciences

#### Genomic Data Formats
- **FASTA/FASTQ** files use ASCII encoding - encoding errors corrupt sequences
- **VCF/BCF** files use text and binary formats - understanding both is crucial
- **BAM/SAM** files are compressed binary - compression knowledge is essential

#### Clinical and Lab Data
- **Electronic Health Records** often use JSON/XML - format knowledge is critical
- **Laboratory instruments** output CSV/TSV - proper parsing prevents analysis errors
- **Configuration files** for bioinformatics tools use YAML/TOML - understanding formats enables customization

#### Data Integrity
- **Checksums (MD5/SHA256)** verify data integrity in genomic databases
- **Compression** reduces storage costs for large sequencing datasets
- **Encoding issues** can corrupt patient names and medical records

---

## 🛠️ Practical Requirements

### Recommended Environment

- Linux, macOS, or WSL on Windows
- Terminal with bash or zsh
- Text editor (VS Code, Vim, etc.)

### Command Reference

This course uses Linux/Unix commands. Below is a brief description of each:

#### File Viewing

| Command | Description |
|---------|-------------|
| `cat` | Display entire file contents |
| `head` | Show first N lines of a file (default 10) |
| `tail` | Show last N lines of a file |
| `less` | Paginated viewing with scrolling (exit: `q`) |
| `file` | Determine file type by contents (magic numbers) |

#### Hex Viewing and Editing

| Command | Description |
|---------|-------------|
| `xxd` | Create hex dump of a file (show bytes in hexadecimal) |
| `hexdump` | Alternative to xxd for hex viewing |
| `od` | Octal dump - view file in octal, hex, or other bases |
| `hexedit` | Interactive binary file editor in hex mode |

#### Encodings and Text

| Command | Description |
|---------|-------------|
| `iconv` | Convert file from one encoding to another |
| `locale` | Show current system locale settings |
| `dos2unix` | Convert Windows line endings (CRLF) to Unix (LF) |

#### Data Processing

| Command | Description |
|---------|-------------|
| `jq` | JSON parser and processor - filter, extract, transform |
| `yq` | YAML processor (like jq for YAML files) |
| `sed` | Stream editor - search and replace text in files |

#### Compression and Archiving

| Command | Description |
|---------|-------------|
| `gzip` / `gunzip` | Compress/decompress files with gzip (.gz) |
| `bzip2` / `bunzip2` | Compress/decompress with bzip2 (.bz2) - better compression, slower |
| `xz` / `unxz` | Compress/decompress with LZMA (.xz) - best compression |
| `zcat` | View contents of .gz file without decompressing |
| `tar` | Combine files into archive (no compression), often with gzip/bzip2/xz |
| `zip` / `unzip` | Create/extract ZIP archives |
| `zipinfo` | Show information about ZIP archive contents |

#### Hashes and Checksums

| Command | Description |
|---------|-------------|
| `md5sum` | Calculate MD5 hash of file (128-bit, deprecated) |
| `sha1sum` | Calculate SHA-1 hash (160-bit, deprecated) |
| `sha256sum` | Calculate SHA-256 hash - recommended standard |
| `sha512sum` | Calculate SHA-512 hash (512-bit) |
| `shasum` | Universal SHA command (macOS), use `-a` flag to select algorithm |

#### File Operations

| Command | Description |
|---------|-------------|
| `chmod` | Change file permissions (rwx for owner/group/others) |
| `cp` | Copy files and directories |
| `mv` | Move or rename files |
| `find` | Search for files by name, type, size, and other criteria |
| `strings` | Extract text strings from binary files |

#### Binary File Analysis

| Command | Description |
|---------|-------------|
| `binwalk` | Analyze binary files, find embedded files and signatures |
| `exiftool` | Read and edit metadata from images and media files |
| `readelf` | Show information about ELF files (Linux executables) |
| `objdump` | Disassembler and object file analyzer |
| `nm` | Show symbols (functions, variables) in object files |

#### Output and Formatting

| Command | Description |
|---------|-------------|
| `echo` | Print text to terminal |
| `printf` | Formatted text output (like C) |
| `man` | Show manual page for a command (exit: `q`) |

#### Network and Download

| Command | Description |
|---------|-------------|
| `curl` | HTTP client for downloading files and working with APIs |
| `wget` | Download files from the internet |

#### Data Encoding

| Command | Description |
|---------|-------------|
| `base64` | Encode/decode data in Base64 |

> **💡 Tip:** Use `man <command>` for detailed help on any command, e.g., `man tar`.

### Tool Installation

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y jq file xxd coreutils vim-common  # vim-common contains xxd
sudo apt install -y dos2unix exiftool binwalk         # additional utilities

# macOS
brew install jq coreutils exiftool binwalk

# yq (YAML processor) - install separately
# https://github.com/mikefarah/yq/releases

# Python libraries (optional, for practice)
pip install chardet pyyaml
```

> **Note:** Most basic commands (`cat`, `head`, `tail`, `tar`, `gzip`, `file`, `chmod`, `find`, `md5sum`, `sha256sum`) are pre-installed on Linux and macOS.

---

## ⏱️ Time Commitment

| Section | Modules | Reading Time | Practice Time |
|---------|---------|--------------|---------------|
| Data Representation Fundamentals | 1-3 | 2-3 hours | 2-3 hours |
| File Formats | 4-6 | 2-3 hours | 3-4 hours |
| Markup and Configuration | 7-8 | 1.5-2 hours | 2-3 hours |
| Working with Data | 9-12 | 2-3 hours | 3-4 hours |

**Total Time:** ~18-25 hours (including practice)

---

## 🎓 After Completing This Course

You will be able to:

✅ Explain differences between encodings and choose the correct one

✅ Diagnose and fix encoding problems (mojibake/garbled text)

✅ Distinguish and work with text and binary files

✅ Read, edit, and validate JSON and YAML

✅ Understand and use HTML, XML, and Markdown

✅ Work with configuration files in different formats

✅ Parse and generate CSV files

✅ Compress and decompress data

✅ Calculate and verify checksums

✅ Encode data in Base64 and understand MIME types

---

## 🔗 Connections to Other Courses

### → Python Course

After completing Data Fundamentals, the Python course teaches you to:
- Parse and manipulate these file formats programmatically
- Handle encoding issues in Python
- Build data processing pipelines
- Work with BioPython for genomic file formats (FASTA, FASTQ, GenBank)

**Recommended modules:** 03_Files, 06_Streams, 11_Bioinformatics

### → Linux Course

Data Fundamentals prepares you for the Linux course where you'll:
- Process structured data with command-line tools (jq, yq, csvkit)
- Build streaming ETL pipelines for large datasets
- Compress and archive genomic data efficiently
- Validate data integrity with checksums in pipelines

**Recommended modules:** 06_Structured_Data, 08_Log_Processing, 10_Streams_IPC

---

## 📚 Additional Resources

### Books

- "The Absolute Minimum Every Software Developer Must Know About Unicode" — Joel Spolsky
- "Pro Git" by Scott Chacon — excellent explanation of binary formats
- "Bioinformatics Data Skills" by Vince Buffalo — data formats in bioinformatics

### Online Resources

- [Unicode Consortium](https://unicode.org/)
- [JSON.org](https://www.json.org/)
- [YAML Specification](https://yaml.org/spec/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [NCBI File Formats](https://www.ncbi.nlm.nih.gov/sra/docs/submitformats/) - Genomic data formats

### Tools

- [jq play](https://jqplay.org/) — Online sandbox for jq
- [YAML Lint](https://www.yamllint.com/) — YAML validator
- [Base64 Encode/Decode](https://www.base64encode.org/)
- [Hex Editor](https://hexed.it/) — Online hex editor

---

## 📝 Version and Updates

**Version:** 1.0  
**Created:** December 2024  
**Last Updated:** December 2024

This course is maintained and kept up to date. If you find outdated information, please create an issue or pull request.

---
