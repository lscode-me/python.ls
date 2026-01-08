# Data Fundamentals: Introduction - Quiz

Test your knowledge on "Introduction: Data, Information, and Formats".

---

## Question 1: Data vs Information

What distinguishes data from information?

A) Data is for computers, information is for humans

B) Data are raw facts without context, information is data in context

C) Data is stored in files, information in databases

D) Data is binary, information is textual

---

## Question 2: Structured Data

Which of the following examples represents structured data?

A) JSON file with nested objects

B) Table in a relational database with fixed columns

C) Vacation photo

D) Email from a colleague

---

## Question 3: Semi-Structured Data

Which format belongs to semi-structured data?

A) JSON document

B) MP3 audio file

C) PostgreSQL table

D) JPEG image

---

## Question 4: Text Files

What characterizes a text file?

A) File can be opened in Microsoft Word

B) Extension .txt

C) File consists of printable characters in a specific encoding

D) File contains only ASCII characters

---

## Question 5: Binary Files

Which of these files is binary?

A) photo.png

B) README.md

C) index.html

D) config.yaml

---

## Question 6: Magic Numbers

What are magic numbers used for in files?

A) To encrypt file contents

B) To store author metadata

C) To identify file format regardless of extension

D) To calculate file size

---

## Question 7: PNG Signature

What bytes are at the beginning of a PNG file?

A) `25 50 44 46`

B) `FF D8 FF`

C) `50 4B 03 04`

D) `89 50 4E 47`

---

## Question 8: file Command

What does the command `file document.txt` do in Linux?

A) Shows file size

B) Creates a new file

C) Determines file type by its contents

D) Opens file for editing

---

## Question 9: File Encoding

Which command shows the encoding of a text file?

A) `cat -e file.txt`

B) `ls -la file.txt`

C) `head file.txt`

D) `file -i file.txt`

---

## Question 10: Encoding Problem

Why might text display as "Ð�Ñ€Ð¸Ð²ÐµÑ‚" instead of "Привет"?

A) File saved in UTF-8 but opened with Windows-1251 encoding

B) File is too large

C) Text contains forbidden characters

D) File is corrupted

---

## Question 11: Abstraction Levels

Which abstraction level is between "bytes" and "data format"?

A) Application

B) Bits

C) Electronics

D) Encoding

---

## Question 12: File Extension

Can you fully trust file extension to determine its type?

A) Only for text files

B) Yes, extension always matches file type

C) No, extension can be changed while contents remain the same

D) Only in Windows

---

## Question 13: Hex Viewing

Which command is used to view a file in hex format?

A) `stat file`

B) `xxd file`

C) `cat -x file`

D) `more file`

---

## Question 14: Encoding Conversion

Which command converts a file from Windows-1251 to UTF-8?

A) `convert -from win -to utf8 file.txt`

B) `charset -c utf8 file.txt`

C) `recode win..utf8 file.txt`

D) `iconv -f WINDOWS-1251 -t UTF-8 file.txt`

---

## Question 15: Line Endings

What does `\r\n` mean in the context of text files?

A) Escape sequence for Unicode

B) Comment character

C) Line ending in Windows style (CR+LF)

D) Tab and space

---

## Question 16: JSON vs CSV

What advantage does JSON have over CSV?

A) Support for nested data structures

B) Parses faster

C) Better human readability

D) Smaller file size

---

## Question 17: Configuration Format

Which format is best suited for configuration files with comments?

A) YAML

B) CSV

C) Binary

D) JSON

---

## Question 18: Unstructured Data

What percentage of world data is unstructured?

A) ~40%

B) ~20%

C) ~70%

D) ~50%

---

## Question 19: xxd Command

What does the output of `xxd -l 8 file.png` show?

A) Last 8 lines of file

B) 8 random lines of file

C) File size in octal

D) First 8 bytes of file in hex format

---

## Question 20: Text Format

Which of these formats is NOT text-based?

A) XML

B) Markdown

C) YAML

D) Protocol Buffers

---

## Question 21: FASTQ Quality Encoding

What encoding is typically used for quality scores in FASTQ files?

A) UTF-16

B) Phred+33 (ASCII offset)

C) Base64

D) Binary integers

---

## Question 22: BAM Files

What is the relationship between SAM and BAM files?

A) They are completely different formats

B) BAM is the compressed binary version of SAM

C) SAM is encrypted, BAM is plaintext

D) They use different coordinate systems

---

## Question 23: VCF Format

VCF (Variant Call Format) is an example of:

A) Purely structured data (like SQL table)

B) Semi-structured data (text with embedded structure)

C) Unstructured data

D) Binary format only

---

## Question 24: FASTA Magic Numbers

Does a FASTA file have magic numbers like PNG or JPEG?

A) Yes, it starts with specific hex bytes

B) No, it's a simple text format starting with '>'

C) Only compressed FASTA files have magic numbers

D) It depends on the sequence type

---

## Question 25: Genomic Data Integrity

Why are checksums (MD5/SHA256) important when downloading genomic data?

A) To compress the files

B) To encrypt sensitive data

C) To verify data wasn't corrupted during transfer

D) To convert file formats

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Data are raw facts (42, "Smith"), information is data with context ("Patient Smith, 42 years old"). |
| 2 | B | Relational tables with fixed schema are structured data. JSON is semi-structured. |
| 3 | A | JSON has flexible schema embedded in the data itself — it's semi-structured. |
| 4 | C | Text file is a sequence of printable characters in specific encoding, independent of extension. |
| 5 | A | PNG is binary image format. YAML, HTML, Markdown are text formats. |
| 6 | C | Magic numbers identify file format by first bytes, regardless of extension. |
| 7 | D | PNG starts with `89 50 4E 47` (`.PNG` in ASCII). `FF D8 FF` is JPEG, `50 4B` is ZIP, `25 50 44 46` is PDF. |
| 8 | C | The `file` command analyzes file contents and determines its type. |
| 9 | D | `file -i` shows MIME type and file encoding. |
| 10 | A | "Mojibake" appears when file encoding doesn't match the encoding used to read it. |
| 11 | D | Levels: bits → bytes → encoding → data format → application. |
| 12 | C | Extension is just part of filename, can be changed without changing contents. |
| 13 | B | `xxd` outputs hex dump of file with ASCII representation. |
| 14 | D | `iconv` is standard utility for encoding conversion with `-f` (from) and `-t` (to) flags. |
| 15 | C | `\r\n` (CRLF) is Windows-style line ending. Unix uses `\n` (LF). |
| 16 | A | JSON supports nested objects and arrays, CSV only flat tables. |
| 17 | A | YAML supports comments (#), JSON does not. |
| 18 | C | Estimates suggest ~70% of world data is unstructured (text, media). |
| 19 | D | `xxd -l 8` outputs first 8 bytes of file in hex format. |
| 20 | D | Protocol Buffers is binary serialization format from Google. |
| 21 | B | FASTQ quality scores use Phred+33 encoding (ASCII 33-126). Modern Illumina uses this standard. |
| 22 | B | BAM is compressed binary version of SAM (Sequence Alignment/Map). Same data, different format. |
| 23 | B | VCF is text-based with structured header and data rows — semi-structured format. |
| 24 | B | FASTA is simple text format starting with '>'. However, gzipped FASTA (.fa.gz) has gzip magic numbers. |
| 25 | C | Checksums verify data integrity. Critical for large genomic files (GB-TB) to ensure no corruption during download. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **23-25 correct (92-100%)** | 🏆 Excellent! | Outstanding! You have solid understanding of data fundamentals. Ready for Number Systems module. |
| **20-22 correct (80-91%)** | ✅ Very Good | Great work! Review sections on encodings and bioinformatics formats. |
| **16-19 correct (64-79%)** | ⚠️ Good | Decent understanding. Review data types, file formats, and life science examples. |
| **12-15 correct (48-63%)** | 📚 Needs Review | Re-read lecture sections on structured data and encodings. |
| **Less than 12 correct (<48%)** | 🔄 Study Again | Carefully re-read the entire lecture and try hands-on examples. |

---

## Next Steps

### If you scored 80% or higher:
- Move to [Module 02: Number Systems](../02_NumberSystems/)
- Try the practice exercises with real bioinformatics files
- Explore the Python Course (Module 03_Files)

### If you scored 50-79%:
- Review lecture sections you missed
- Practice with command-line tools (`file`, `xxd`, `iconv`)
- Download sample FASTQ/VCF files and examine them

### If you scored below 50%:
- Re-read the lecture carefully
- Work through examples step by step
- Ask questions in study groups or forums
- Focus on understanding core concepts before moving forward

---

## Practice Exercises

To solidify your understanding:

1. **File Type Detective**: Use `file` and `xxd` to examine different files in your system
2. **Encoding Practice**: Create text files in different encodings and convert them
3. **Bioinformatics Files**: Download a FASTQ file and examine its structure
4. **Magic Numbers**: Create a script that identifies file types by magic numbers
5. **Format Comparison**: Compare sizes and parsing of FASTA vs FASTQ, SAM vs BAM

---
