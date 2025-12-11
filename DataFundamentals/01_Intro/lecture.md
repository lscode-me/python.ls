# Data Fundamentals for Life Sciences
## Introduction: Data, Information, and Formats

---

## 📋 Prerequisites

Before starting this module, you should:

- Be able to use a computer at a user level
- Have a general understanding of files and folders
- Understand that computers work with zeros and ones (basic concept)

> **💡 Tip:** This course uses Linux/Unix command-line tools (`cat`, `xxd`, `file`, `chmod`, and others). You'll find a brief description of each command in the [Command Reference](../README.md#command-reference) in the course README.

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Explain the difference between data and information
- Describe the abstraction levels of data representation in computers
- Distinguish between structured, semi-structured, and unstructured data
- Explain why there are so many data formats
- Apply these concepts to biological and healthcare data

---

## 1. What Is Data

### 1.1 Data vs Information

**Data** are raw facts, numbers, symbols without context. Data alone carries no meaning.

**Information** is data that has been processed and presented in a context that makes it understandable and useful.

**Example:**

```
Data:    42, 37.5, "Smith", 2024-12-08
```

These numbers and strings mean nothing without context.

```
Information:
  Patient: Smith
  Visit Date: 2024-12-08
  Age: 42 years
  Temperature: 37.5°C
```

Now the data has meaning — this is a patient's medical record.

**Life Science Example:**

```
Data:    ATCGATCG, 125, 0.75
```

These values are meaningless without context.

```
Information:
  DNA Sequence: ATCGATCG
  Read Quality: 125 (Phred score)
  GC Content: 0.75 (75%)
```

Now it's clear — this is genomic sequencing data.

### 1.2 Data Lifecycle

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Creation   │───►│   Storage   │───►│ Processing  │───►│    Usage    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
       ▲                                                        │
       └────────────────────────────────────────────────────────┘
```

At each stage, it's important to understand:

- **How** data is represented (format)
- **Where** data is located (storage)
- **How** to work with it (tools)

**Bioinformatics Pipeline Example:**

```
Creation:     DNA Sequencer → FASTQ files
Storage:      Store raw reads (compressed .fastq.gz)
Processing:   Align reads → BAM files
Usage:        Variant calling → VCF files
              Analysis → CSV reports
```

---

## 2. Abstraction Levels

### 2.1 From Bits to Applications

Computers work only with binary data — zeros and ones. But we see text, images, hear music. How does this work?

```
┌────────────────────────────────────────────────────────────────┐
│                     Abstraction Levels                          │
├────────────────────────────────────────────────────────────────┤
│  7. Application     │  Text editor, browser, player, IGV       │
├─────────────────────┼──────────────────────────────────────────┤
│  6. Data Format     │  JSON, YAML, Markdown, MP3, JPEG, FASTQ  │
├─────────────────────┼──────────────────────────────────────────┤
│  5. Encoding        │  UTF-8, ASCII, Base64, Phred+33          │
├─────────────────────┼──────────────────────────────────────────┤
│  4. Bytes           │  8-bit blocks: 01001000 = 0x48 = 72      │
├─────────────────────┼──────────────────────────────────────────┤
│  3. Bits            │  0 and 1                                 │
├─────────────────────┼──────────────────────────────────────────┤
│  2. Electronics     │  High/low voltage                        │
├─────────────────────┼──────────────────────────────────────────┤
│  1. Physics         │  Electrons, magnetic domains             │
└─────────────────────┴──────────────────────────────────────────┘
```

**Example: Letter "H"**

```
Application level:    H (letter on screen)
         ↓
Format level:         Part of HTML tag <H1> or JSON string
         ↓
Encoding level:       UTF-8 encodes as 0x48
         ↓
Byte level:           01001000
         ↓
Bit level:            0, 1, 0, 0, 1, 0, 0, 0
```

**Bioinformatics Example: Quality Score "I"**

```
Application level:    Quality 40 (very high confidence)
         ↓
Format level:         Part of FASTQ quality line
         ↓
Encoding level:       Phred+33: ASCII 'I' = 73 - 33 = 40
         ↓
Byte level:           01001001 (0x49)
         ↓
Bit level:            0, 1, 0, 0, 1, 0, 0, 1
```

### 2.2 Why This Matters

When something doesn't work, the problem can be at any level:

| Level | Typical Problem | Life Science Example |
|-------|----------------|----------------------|
| Format | "Invalid JSON" — syntax error | Malformed VCF file |
| Encoding | "Mojibake" — wrong encoding | Patient names garbled |
| Bytes | Corrupted file | Incomplete BAM file |
| Bits | Disk read error | Failed sequencing run |

Understanding levels helps localize and fix problems.

---

## 3. Data Classification

### 3.1 By Degree of Structure

Data is divided into three categories by how organized it is:

**Structured Data**

Data with a clear, predefined schema.

```
┌────────┬─────────────┬───────┐
│ ID     │ Name        │ Age   │
├────────┼─────────────┼───────┤
│ 1      │ Alice       │ 30    │
│ 2      │ Bob         │ 25    │
│ 3      │ Charlie     │ 35    │
└────────┴─────────────┴───────┘
```

Examples:

- Relational databases (PostgreSQL, MySQL)
- Excel tables with fixed columns
- CSV with headers

**Life Science Examples:**

- Variant call tables (CHR, POS, REF, ALT)
- Gene expression matrices
- Clinical trial data
- Laboratory measurements

Advantages:

- Easy to query (SQL)
- Easy to validate
- Efficient storage

**Semi-Structured Data**

Data with a flexible schema embedded in the data itself.

```json
{
  "id": 1,
  "name": "Alice",
  "age": 30,
  "skills": ["Python", "SQL"],
  "address": {
    "city": "Moscow",
    "zip": "101000"
  }
}
```

Examples:

- JSON
- YAML
- XML

**Life Science Examples:**

- VCF files (header + structured records)
- JSON from bioinformatics APIs (NCBI, UniProt)
- Configuration files for analysis pipelines
- Metadata for sequencing experiments

Advantages:

- Schema flexibility
- Self-describing
- Easily extensible

**Unstructured Data**

Data without a predefined model.

```
Hello! This is plain text. There's no structure here,
just a sequence of characters. This could be an email,
article, comment, or any other free-form text.
```

Examples:

- Free-form text (emails, articles)
- Images
- Audio and video
- Unstructured logs

**Life Science Examples:**

- Clinical notes from doctors
- Scientific paper abstracts
- Microscopy images
- Lab notebook entries
- Patient interview transcripts

Challenges:

- Difficult to analyze automatically
- No standard query method
- Requires NLP/ML for information extraction

### 3.2 Data Type Comparison

| Characteristic | Structured | Semi-structured | Unstructured |
|----------------|------------|-----------------|--------------|
| Schema | Strict, external | Flexible, embedded | Absent |
| Queries | SQL, simple | JSONPath, XPath | Full-text search |
| Examples | RDBMS, CSV | JSON, YAML, XML | Text, media |
| Volume in world | ~20% | ~10% | ~70% |
| Analysis | Simple | Medium | Complex |

**Life Science Context:**

| Data Type | Examples | Analysis Tools |
|-----------|----------|----------------|
| Structured | Variant tables, expression matrices | SQL, pandas, R dataframes |
| Semi-structured | VCF, GFF, JSON APIs | BioPython, jq, custom parsers |
| Unstructured | Clinical notes, images | NLP tools, image analysis, OCR |

---

## 4. Data Formats

### 4.1 Why Formats Are Needed

**Format** is an agreement on how data is represented and interpreted.

Without formats, computers couldn't:

- Understand each other
- Open files created by other programs
- Transmit data over networks

**Example of the problem without standards:**

```
Program A saves date as: 2024-12-08
Program B expects date as:   08/12/2024
Program C expects date as:   12/08/2024

Result: chaos and errors
```

**Bioinformatics Example:**

Different sequencing platforms historically used different quality encodings:

```
Sanger:    Phred+33 (ASCII 33-126)
Illumina:  Phred+64 (ASCII 64-126) [older versions]
Solexa:    Solexa+64 (different calculation)

Result: Quality scores misinterpreted if format not specified!
```

### 4.2 Text vs Binary Formats

**Text Formats:**

```json
{"name": "Alice", "age": 30}
```

- Human-readable
- Easy to edit in text editor
- Larger size
- Examples: JSON, YAML, XML, CSV, Markdown, FASTA, VCF

**Binary Formats:**

```
00000000: 7b22 6e61 6d65 223a 2022 416c 6963 6522  {"name": "Alice"
00000010: 2c20 2261 6765 223a 2033 307d            , "age": 30}
```

(this is hex representation, actual storage is bytes)

- Compact
- Faster to parse
- Not readable without special tools
- Examples: Protocol Buffers, MessagePack, JPEG, MP3, BAM, BCF

**Bioinformatics Formats:**

| Format Type | Text | Binary |
|-------------|------|--------|
| Sequences | FASTA, FASTQ | HDF5 |
| Alignments | SAM, MAF | BAM, CRAM |
| Variants | VCF, GFF | BCF |
| Expression | CSV, TSV | HDF5, Loom |

### 4.3 Format Selection

| Scenario | Recommended Format | Why |
|----------|-------------------|------|
| Configuration | YAML, TOML | Readability, comments |
| API responses | JSON | Standard, wide support |
| Documentation | Markdown | Simplicity, conversion |
| Table exchange | CSV | Universal |
| High performance | Protocol Buffers | Compact, speed |
| Web pages | HTML | Browser standard |

**Life Science Scenarios:**

| Scenario | Format | Why |
|----------|--------|-----|
| Raw sequencing data | FASTQ (gzipped) | Standard, quality info |
| Aligned reads | BAM | Binary, indexed, efficient |
| Variant calls | VCF | Standard, widely supported |
| Gene annotations | GFF3/GTF | Standard for genomic features |
| Expression data | CSV/TSV or HDF5 | Simple or high-performance |
| Experimental metadata | JSON/YAML | Flexible, self-describing |

---

## 5. Text and Binary Files

### 5.1 What Is a Text File

**Text file** is a sequence of characters (letters, digits, symbols) encoded in a specific encoding.

```bash
# View text file
cat hello.txt
```

```
Hello, World!
Привет, мир!
```

Characteristics:

- Consists of printable characters
- Has line breaks (`\n` or `\r\n`)
- Readable in any text editor
- Encoding matters for correct display

**FASTA Example (text file):**

```
>seq1 description
ATCGATCGATCGATCG
GCTAGCTAGCTAGCTA
```

### 5.2 What Is a Binary File

**Binary file** is a sequence of bytes not intended for direct human reading.

```bash
# View binary file as text (meaningless)
cat image.png
```

```
�PNG
▒
IHDR...(garbage)...
```

```bash
# View in hex mode (makes sense)
xxd image.png | head -3
```

```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0100 0000 0100 0802 0000 00d3 1025  ...............%
00000020: 0000 0006 624b 4744 0000 ff00 00ff 00ff  ....bKGD........
```

Characteristics:

- Can contain any bytes (0-255)
- Requires special programs for interpretation
- Often has magic numbers at the beginning
- Examples: images, executables, archives

**BAM File Example (binary):**

```bash
# View BAM as text (meaningless)
cat aligned_reads.bam
# Output: garbage

# View with specialized tool
samtools view aligned_reads.bam | head
# Output: readable alignment records
```

### 5.3 How to Determine File Type

```bash
# The file command analyzes contents
file document.txt
# document.txt: UTF-8 Unicode text

file image.png
# image.png: PNG image data, 256 x 256, 8-bit/color RGB

file archive.zip
# archive.zip: Zip archive data
```

**Bioinformatics Examples:**

```bash
file sample.fasta
# sample.fasta: ASCII text

file sample.fastq.gz
# sample.fastq.gz: gzip compressed data

file aligned.bam
# aligned.bam: data

file variants.vcf
# variants.vcf: ASCII text
```

The `file` command looks at:

1. Magic numbers (signatures) at the beginning of the file
2. Data structure
3. Heuristics for text files

---

## 6. Magic Numbers

### 6.1 What Are Magic Numbers

**Magic numbers** are special bytes at the beginning of a file that identify its format.

| Format | Magic bytes (hex) | ASCII representation |
|--------|-------------------|---------------------|
| PNG | 89 50 4E 47 | `.PNG` |
| JPEG | FF D8 FF | (non-printable) |
| PDF | 25 50 44 46 | `%PDF` |
| ZIP | 50 4B 03 04 | `PK..` |
| GIF | 47 49 46 38 | `GIF8` |
| ELF (Linux exe) | 7F 45 4C 46 | `.ELF` |
| Gzip | 1F 8B | (non-printable) |
| BAM | 42 41 4D 01 | `BAM` + version |

### 6.2 Why Magic Numbers Are Needed

1. **Format identification** — programs can determine file type regardless of extension

2. **Validation** — if magic numbers are wrong, the file is corrupted or replaced

3. **Security** — helps prevent file substitution

```bash
# Example: rename PNG to .txt
mv image.png fake.txt

# file will still detect correctly
file fake.txt
# fake.txt: PNG image data, 256 x 256, 8-bit/color RGB
```

**Bioinformatics Example:**

```bash
# BAM file disguised as TXT
mv aligned.bam data.txt

# file command still identifies it
file data.txt
# data.txt: data

# View magic numbers
xxd -l 8 data.txt
# 00000000: 4241 4d01 ...  BAM.
```

### 6.3 Viewing Magic Numbers

```bash
# First 16 bytes of PNG file
xxd -l 16 image.png
```

```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

Breakdown:

- `89 50 4E 47` — PNG magic number
- `0D 0A 1A 0A` — special bytes for damage detection
- `00 00 00 0D` — length of next chunk
- `49 48 44 52` — "IHDR" (image header)

**FASTQ.GZ Example:**

```bash
# First 16 bytes of gzipped FASTQ
xxd -l 16 sample.fastq.gz
```

```
00000000: 1f8b 0800 0000 0000 0003 ...  ............
```

- `1F 8B` — gzip magic number
- `08` — compression method (deflate)

---

## 7. Encodings: Preview

### 7.1 Why Encodings Are Needed

**Encoding** is a mapping table between characters and numbers (bytes).

Computers understand only numbers. To store text, each character is assigned a number:

```
A → 65
B → 66
C → 67
...
```

Problem: different countries created their own tables:

- USA: ASCII (Latin)
- Russia: KOI8-R, Windows-1251, CP866
- Japan: Shift-JIS, EUC-JP
- And hundreds more...

### 7.2 "Mojibake" — A Typical Problem

```
Expected:  Hello, world!
Got:       ����, �����!
```

This happens when:

1. File saved in one encoding (UTF-8)
2. Opened in another (Windows-1251)

**Life Science Impact:**

Patient names, drug names, and clinical notes can be corrupted:

```
Expected:  Müller (German patient name)
Got:       M├╝ller (wrong encoding)

Expected:  Iñigo (Spanish name)
Got:       IÃ±igo (wrong encoding)
```

This can lead to serious medical record errors!

### 7.3 Solution: Unicode and UTF-8

**Unicode** is a unified table of all characters from all world languages.

**UTF-8** is a way to encode Unicode that:

- Is compatible with ASCII
- Supports all characters
- Is the internet standard

We'll cover this in detail in module [03_Encodings](../03_Encodings/).

---

## 8. Course Format Overview

### 8.1 Structured Data Formats

| Format | Purpose | Features |
|--------|---------|----------|
| **JSON** | APIs, configs | Web standard, simple |
| **YAML** | Configs, DevOps | Readable, comments |
| **XML** | Documents, legacy | Verbose, powerful |
| **CSV** | Tables | Simple, universal |
| **TOML** | Configs | Clear, typed |

### 8.2 Document Formats

| Format | Purpose | Features |
|--------|---------|----------|
| **Markdown** | Documentation | Simple syntax |
| **HTML** | Web pages | Browser standard |
| **reStructuredText** | Technical docs | Powerful, Python world |

### 8.3 Service Formats

| Format | Purpose | Features |
|--------|---------|----------|
| **INI** | Windows configs | Simple, sections |
| **Properties** | Java configs | Key=value |
| **.env** | Environment variables | Simple, security |

---

## 9. Data Working Tools

### 9.1 Command Line

```bash
# File viewing
cat file.txt          # Entire file
head -n 10 file.txt   # First 10 lines
tail -n 10 file.txt   # Last 10 lines
less file.txt         # Paginated viewing

# Type and encoding detection
file document.txt
file -i document.txt  # With MIME type and encoding

# Hex viewing
xxd file.bin | head
hexdump -C file.bin | head

# Encoding conversion
iconv -f WINDOWS-1251 -t UTF-8 input.txt > output.txt
```

### 9.2 Specialized Tools

```bash
# JSON
jq '.' file.json      # Formatting
jq '.name' file.json  # Extract field

# YAML
yq '.' file.yaml      # Formatting

# CSV
csvtool col 1,3 file.csv    # Select columns
csvstat file.csv            # Statistics

# Compression
gzip file.txt         # Compress
gunzip file.txt.gz    # Decompress

# Hashes
md5sum file.txt
sha256sum file.txt
```

**Bioinformatics Tools:**

```bash
# FASTA/FASTQ
seqtk seq -A input.fastq > output.fasta  # Convert to FASTA
bioawk -c fastx '{print $name, length($seq)}' reads.fasta  # Sequence lengths

# BAM/SAM
samtools view aligned.bam | head     # View alignments
samtools flagstat aligned.bam        # Alignment statistics

# VCF
bcftools view variants.vcf.gz        # View VCF
bcftools stats variants.vcf.gz       # Variant statistics

# GFF/GTF
grep "gene" annotations.gff          # Filter features
awk '$3=="gene"' annotations.gff     # Filter by feature type
```

### 9.3 Editors

| Editor | Best For |
|--------|----------|
| VS Code | Universal, JSON/YAML highlighting, extensions |
| Vim/Neovim | Fast terminal editing |
| Sublime Text | Working with large files |
| IGV | Viewing genomic data (BAM, VCF, BED) |

---

## 10. Common Pitfalls

### 10.1 Ignoring Encodings

❌ **Error:** Opening files without checking encoding

```bash
# File in Windows-1251, opened as UTF-8
cat russian.txt
# Result: Ð�Ñ€Ð¸Ð²ÐµÑ‚!
```

✅ **Solution:** Always check encoding

```bash
file -i russian.txt
# russian.txt: text/plain; charset=iso-8859-1

# Convert if needed
iconv -f WINDOWS-1251 -t UTF-8 russian.txt
```

### 10.2 Trusting File Extensions

❌ **Error:** Trusting file extensions

```bash
# Someone renamed virus.exe to picture.jpg
file picture.jpg
# picture.jpg: PE32 executable (GUI) Intel 80386
```

✅ **Solution:** Use `file` to verify

### 10.3 Editing Binary Files

❌ **Error:** Opening binary file in text editor and saving

```bash
# This will corrupt the file!
nano database.db
nano aligned.bam  # Don't do this!
```

✅ **Solution:** Use specialized tools

```bash
# Hex editor for binary files
hexedit file.bin

# Use specialized bioinformatics tools
samtools view -h aligned.bam > aligned.sam  # Convert to text
```

### 10.4 Mixing Line Endings

❌ **Error:** Mixing Windows (`\r\n`) and Unix (`\n`) line endings

```bash
# File with mixed endings
file mixed.txt
# mixed.txt: ASCII text, with CRLF, LF line terminators
```

✅ **Solution:** Convert to one format

```bash
# Windows → Unix
sed -i 's/\r$//' file.txt

# Or use dos2unix
dos2unix file.txt
```

**Bioinformatics Impact:**

Mixed line endings can break:
- FASTA parsing (split sequences incorrectly)
- Shell scripts in pipelines
- Python/Perl parsers

---

## 💡 Key Takeaways

- **Data ≠ Information**: Data becomes information only in context. Format and representation are critical. In bioinformatics, a sequence without quality scores or annotations is just data.

- **Abstraction Levels**: From bits to applications — understanding levels helps diagnose problems. When a BAM file won't open, is it a format issue, encoding problem, or file corruption?

- **Three Data Types**: Structured (SQL tables), semi-structured (JSON/YAML/VCF), unstructured (text/images) — each requires a different approach. Choose the right format for your analysis pipeline.

- **Text vs Binary**: Text files are human-readable (FASTA, VCF), binary requires special tools (BAM, BCF). Use `file` to determine type. Binary formats are more efficient for large datasets.

- **Encodings Matter**: "Mojibake" is encoding mismatch. UTF-8 is the modern standard. Critical for patient names and international collaboration.

- **Magic Numbers**: Don't trust file extensions. Use `file` command to verify actual format. Important for data integrity in pipelines.

---

## 🚀 Next Steps

**Related Modules:**

- [Number Systems](../02_NumberSystems/) — bits, bytes, number systems
- [Encodings](../03_Encodings/) — deep dive into encodings
- [File Formats](../04_FileFormats/) — detailed format analysis

**Practice Ideas:**

1. Use `file` command to determine types of various files in your system
2. Open a binary file (PNG, ZIP, or BAM) in hex editor and find magic numbers
3. Create a text file, save in UTF-8, then open with wrong encoding to see mojibake
4. Download a FASTQ file and examine its structure with `head`, `xxd`, and `file`
5. Compare file sizes: FASTA vs FASTQ, SAM vs BAM, VCF vs BCF

**Going Deeper:**

- Study PNG format at low level (chunks, CRC)
- Examine how ELF files work (Linux executables)
- Understand BAM/CRAM compression algorithms
- Learn about BGZF (blocked gzip) used in bioinformatics

**Connections to Other Courses:**

- **Python Course**: Module 03_Files teaches how to handle these formats programmatically
- **Linux Course**: Module 06_Structured_Data teaches command-line tools for data formats

---

## 📚 Additional Resources

**Articles:**

- [The Absolute Minimum About Unicode](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [What Every Programmer Should Know About Memory](https://www.akkadia.org/drepper/cpumemory.pdf)

**Bioinformatics Standards:**

- [SAM/BAM Format Specification](https://samtools.github.io/hts-specs/SAMv1.pdf)
- [VCF Format Specification](https://samtools.github.io/hts-specs/VCFv4.2.pdf)
- [FASTQ Format](https://en.wikipedia.org/wiki/FASTQ_format)
- [GFF3 Specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)

**Tools:**

- [file command manual](https://man7.org/linux/man-pages/man1/file.1.html)
- [xxd manual](https://linux.die.net/man/1/xxd)
- [Magic file format](https://man7.org/linux/man-pages/man5/magic.5.html)
- [samtools](http://www.htslib.org/)
- [bcftools](http://www.htslib.org/doc/bcftools.html)

**Wikipedia:**

- [Character encoding](https://en.wikipedia.org/wiki/Character_encoding)
- [Binary file](https://en.wikipedia.org/wiki/Binary_file)
- [Magic number (programming)](https://en.wikipedia.org/wiki/Magic_number_(programming))
- [FASTQ format](https://en.wikipedia.org/wiki/FASTQ_format)

---
