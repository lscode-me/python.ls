# File Formats - Quiz

Test your knowledge on "File Formats: Text, Binary, and Magic Numbers".

---

## Question 1: File Types

Which statement is true about text files?

A) They contain only ASCII characters

B) They always have a .txt extension

C) They are always smaller than binary files

D) They contain characters in a specific encoding and are human-readable

---

## Question 2: Binary Files

Which file is binary?

A) config.json

B) image.png

C) index.html

D) script.py

---

## Question 3: Magic Numbers

What are magic numbers in files?

A) Fixed bytes at the beginning of a file to identify the format

B) File checksum

C) File size in bytes

D) Random numbers for encryption

---

## Question 4: PNG Signature

Which bytes start a PNG file?

A) `50 4B 03 04`

B) `FF D8 FF`

C) `89 50 4E 47`

D) `25 50 44 46`

---

## Question 5: JPEG Signature

Which bytes start a JPEG file?

A) `47 49 46 38`

B) `FF D8 FF`

C) `50 4B 03 04`

D) `89 50 4E 47`

---

## Question 6: ZIP Format

Which file format has the same signature (PK) as ZIP?

A) RAR

B) DOCX

C) TAR

D) 7z

---

## Question 7: file Command

Which command is used to determine the MIME type of a file?

A) `file -i document.txt`

B) `file -m document.txt`

C) `file -x document.txt`

D) `file -t document.txt`

---

## Question 8: JSON MIME Type

What is the correct MIME type for a JSON file?

A) `text/json`

B) `text/javascript`

C) `data/json`

D) `application/json`

---

## Question 9: PNG MIME Type

What is the MIME type for a PNG image?

A) graphics/png

B) image/png

C) application/png

D) binary/png

---

## Question 10: Security

Why shouldn't you trust file extensions to determine file type?

A) Extension can be changed while content remains the same

B) They take up too much space

C) Some systems don't support extensions

D) Extensions are outdated

---

## Question 11: Opening Mode

How do you correctly open a binary file in Python?

A) `open('file.bin', 'r')`

B) `open('file.bin', 'binary')`

C) `open('file.bin', 'b')`

D) `open('file.bin', 'rb')`

---

## Question 12: PNG Structure

What does a PNG file consist of after the signature?

A) Chunks with type, length, data, and CRC

B) Compressed JPEG data

C) Continuous stream of pixels

D) XML metadata

---

## Question 13: PDF Signature

How does a PDF file start?

A) %PDF-

B) @PDF@

C) #PDF#

D) !PDF!

---

## Question 14: ELF Format

Which operating system uses the ELF format?

A) Windows

B) DOS

C) Linux

D) macOS

---

## Question 15: tar Format

What does the tar command do?

A) Encrypts files

B) Converts formats

C) Combines files into one archive without compression

D) Compresses files

---

## Question 16: gzip vs bzip2

Which statement is true about gzip and bzip2?

A) They give the same compression

B) gzip compresses better but is slower

C) bzip2 compresses better but is slower

D) bzip2 doesn't support large files

---

## Question 17: HTTP Content-Type

Which HTTP header specifies the content type?

A) Data-Format

B) File-Type

C) Content-Type

D) MIME-Type

---

## Question 18: python-magic

Which Python library determines file type by content?

A) python-magic (magic)

B) file-type

C) format-check

D) mime-detect

---

## Question 19: xxd Command

What does the command `xxd -l 8 file.bin` show?

A) 8 random bytes

B) File size in octal

C) Last 8 lines of file

D) First 8 bytes of file in hex format

---

## Question 20: Endianness in Files

Which byte order does PNG use for numbers?

A) System-dependent

B) Little-Endian

C) Big-Endian

D) No multi-byte numbers

---

## Question 21: BAM Magic Number

What are the first 4 bytes of a BAM file?

A) `53 41 4D 01` (SAM.)

B) `42 41 4D 01` (BAM.)

C) `56 43 46 01` (VCF.)

D) `1F 8B 08 00` (gzip)

---

## Question 22: FASTA Format

Which statement is true about FASTA files?

A) They are binary files

B) They start with '>' character

C) They contain quality scores

D) They are compressed by default

---

## Question 23: BAM vs SAM

What is the relationship between BAM and SAM?

A) They are completely different formats

B) BAM is the compressed binary version of SAM

C) SAM is encrypted, BAM is plaintext

D) BAM is older and deprecated

---

## Question 24: VCF Compression

Which compression is commonly used for VCF files?

A) ZIP

B) RAR

C) gzip (.vcf.gz)

D) bzip2

---

## Question 25: BGZF

What is special about BGZF compression used in BAM files?

A) It's faster than regular gzip

B) It allows random access while still being compressed

C) It's a text-based compression

D) It doesn't actually compress the data

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Text files contain characters in encoding (UTF-8, ASCII, etc.) and are human-readable. |
| 2 | B | PNG is a binary image format. JSON, Python, HTML are text formats. |
| 3 | A | Magic numbers are fixed bytes at the beginning of a file for format identification. |
| 4 | C | PNG starts with `89 50 4E 47 0D 0A 1A 0A` (.PNG....). |
| 5 | B | JPEG starts with `FF D8 FF`. |
| 6 | B | DOCX, XLSX, PPTX are ZIP archives with XML inside, starting with `50 4B` (PK). |
| 7 | A | `file -i` shows MIME type and encoding. |
| 8 | D | Correct MIME for JSON: `application/json`. |
| 9 | B | PNG has MIME type `image/png`. |
| 10 | A | Extension is part of filename, can be changed without changing content. Critical for security! |
| 11 | D | For binary files, use `'rb'` mode (read binary). |
| 12 | A | PNG consists of signature and chunks (IHDR, IDAT, IEND, etc.) with length, type, data, CRC. |
| 13 | A | PDF starts with `%PDF-` (bytes: 25 50 44 46 2D). |
| 14 | C | ELF (Executable and Linkable Format) is the executable file format for Linux. |
| 15 | C | tar only combines files. For compression, use gzip/bzip2 (tar.gz, tar.bz2). |
| 16 | C | bzip2 gives better compression but works slower than gzip. |
| 17 | C | `Content-Type` is the HTTP header for specifying MIME type. |
| 18 | A | `python-magic` (imported as `magic`) determines type by content. |
| 19 | D | `xxd -l 8` shows first 8 bytes in hex format. |
| 20 | C | PNG uses Big-Endian (network byte order) for all numeric values. |
| 21 | B | BAM files start with `42 41 4D 01` (BAM\x01). This distinguishes them from text SAM files. |
| 22 | B | FASTA files are text format starting with '>' followed by sequence identifier. |
| 23 | B | BAM is the binary, compressed version of SAM. Same data, ~5x smaller and faster to parse. |
| 24 | C | VCF files are commonly compressed with gzip (.vcf.gz) for distribution and storage. |
| 25 | B | BGZF (blocked gzip) allows random access to compressed data, crucial for indexed BAM files with tools like samtools. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **23-25 correct (92-100%)** | 🏆 Excellent! | Outstanding understanding of file formats! Move to JSON module. |
| **20-22 correct (80-91%)** | ✅ Very Good | Great work! Review magic numbers and MIME types. |
| **16-19 correct (64-79%)** | ⚠️ Good | Re-read sections on binary file structure and genomic formats. |
| **12-15 correct (48-63%)** | 📚 Needs Review | Review file command usage and bioinformatics file formats. |
| **Less than 12 correct (<48%)** | 🔄 Study Again | Carefully re-read the lecture and practice with the file command. |

---

## Next Steps

### If you scored 80% or higher:
- Move to [Module 05: JSON](../05_JSON/)
- Practice with real genomic files (FASTA, FASTQ, BAM, VCF)
- Try the Linux Course (Module 06_Structured_Data)
- Experiment with samtools and bcftools

### If you scored 50-79%:
- Review lecture sections on magic numbers and file structures
- Practice with `file`, `xxd`, and `xxd` commands
- Download sample genomic files and examine their headers
- Work through Python examples for binary file reading

### If you scored below 50%:
- Re-read the lecture step by step
- Focus on understanding text vs binary distinction
- Practice with command-line tools
- Start with simple examples before genomic formats

---

## Practice Exercises

To solidify your understanding:

1. **Magic Number Detective**: Use `xxd` to find magic numbers in various files
2. **Format Validator**: Write a Python script to validate file types by checking magic numbers
3. **BAM Header Parser**: Create a tool to extract reference sequences from BAM headers
4. **FASTA Validator**: Write a validator that checks FASTA file structure
5. **Compression Comparison**: Compare file sizes and speed of gzip vs bzip2 vs xz on genomic data
6. **MIME Type Detector**: Build a tool that determines MIME types for bioinformatics files
7. **File Converter**: Create a script to convert between SAM and BAM formats using pysam

---

## Bioinformatics Applications

### Verify File Integrity
```bash
# Check if file is actually what extension claims
file aligned.bam
# aligned.bam: data

# View magic number
xxd -l 4 aligned.bam
# 00000000: 4241 4d01                                BAM.

# Check gzipped FASTQ
file reads.fastq.gz
# reads.fastq.gz: gzip compressed data

# Verify it's actually FASTQ inside
zcat reads.fastq.gz | head -1
# Should start with @
```

### File Format Detection
```python
def identify_genomic_format(filepath):
    """Identify genomic file format by magic number and content."""
    import magic
    
    # Check magic number
    with open(filepath, 'rb') as f:
        header = f.read(4)
    
    if header == b'BAM\x01':
        return 'BAM'
    elif header == b'BCF\x02':
        return 'BCF'
    elif header == b'CRAM':
        return 'CRAM'
    elif header[:2] == b'\x1f\x8b':
        # gzipped file
        if filepath.endswith('.fastq.gz'):
            return 'FASTQ (gzipped)'
        elif filepath.endswith('.vcf.gz'):
            return 'VCF (gzipped)'
        return 'gzip compressed'
    else:
        # Check text formats
        try:
            with open(filepath, 'r') as f:
                first_line = f.readline()
                if first_line.startswith('>'):
                    return 'FASTA'
                elif first_line.startswith('@'):
                    return 'FASTQ'
                elif first_line.startswith('##fileformat=VCF'):
                    return 'VCF'
        except:
            pass
    
    return 'Unknown'

# Test
print(identify_genomic_format('sequences.fasta'))  # FASTA
print(identify_genomic_format('aligned.bam'))      # BAM
```

### Validate Uploaded Files
```python
def validate_genomic_upload(filepath, expected_format):
    """Validate uploaded genomic file is actually what it claims to be."""
    
    # Don't trust extension!
    detected_format = identify_genomic_format(filepath)
    
    if detected_format != expected_format:
        raise ValueError(
            f"File claims to be {expected_format} but is actually {detected_format}"
        )
    
    return True

# Usage in upload handler
try:
    validate_genomic_upload('uploaded_file.bam', 'BAM')
    process_bam(uploaded_file)
except ValueError as e:
    print(f"Security warning: {e}")
```

---
