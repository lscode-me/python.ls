# File Formats
## Text and Binary Files, Magic Numbers, and MIME Types

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand number systems and hex (module 02_NumberSystems)
- Know the basics of encodings (module 03_Encodings)
- Be able to work in command line

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Distinguish between text and binary files
- Determine file type by magic numbers
- Work with the `file` command to identify formats
- Understand and use MIME types
- Analyze binary file structure
- Work with bioinformatics file formats (FASTA, FASTQ, BAM, VCF)

---

## 1. File Classification

### 1.1 Text vs Binary

**Text Files:**

- Contain characters in a specific encoding
- Human-readable in a text editor
- Divided into lines by newlines (`\n` or `\r\n`)
- Examples: `.txt`, `.py`, `.json`, `.html`, `.csv`, `.fasta`, `.vcf`

**Binary Files:**

- Contain arbitrary bytes (0-255)
- Require special programs for interpretation
- Don't have a concept of "lines"
- Examples: `.png`, `.pdf`, `.exe`, `.zip`, `.bam`, `.bcf`

**Bioinformatics Examples:**

| Format | Type | Description |
|--------|------|-------------|
| FASTA | Text | DNA/protein sequences |
| FASTQ | Text | Sequences with quality scores |
| VCF | Text | Variant calls |
| SAM | Text | Sequence alignments |
| BAM | Binary | Compressed SAM |
| BCF | Binary | Compressed VCF |
| CRAM | Binary | Compressed alignment |

### 1.2 How to Determine Type

```bash
# Text file
file README.md
# README.md: UTF-8 Unicode text

# Binary file  
file photo.jpg
# photo.jpg: JPEG image data, JFIF standard 1.01

# Executable file
file /bin/ls
# /bin/ls: Mach-O 64-bit executable arm64

# Bioinformatics examples
file sequences.fasta
# sequences.fasta: ASCII text

file aligned.bam
# aligned.bam: data

file variants.vcf.gz
# variants.vcf.gz: gzip compressed data
```

### 1.3 Viewing Contents

```bash
# Text file — read directly
cat script.py

# Binary file — hex dump
xxd image.png | head -5
```

```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0100 0000 0100 0802 0000 00d3 1025  ...............%
00000020: 0000 0006 624b 4744 0000 ff00 00ff 00ff  ....bKGD........
00000030: 0000 0001 7348 4953 0000 0000 0000 0001  ....sHIS........
00000040: 0100 0101 0001 0000 0001 0000 0001 0100  ................
```

**FASTA (Text):**

```bash
head sequences.fasta
```

```
>NM_007294.3 Homo sapiens BRCA1
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAA
AATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTG
```

**BAM (Binary):**

```bash
xxd aligned.bam | head -3
```

```
00000000: 4241 4d01 3800 0000 4048 4409 5644 3a31  BAM.8...@HD.VD:1
00000010: 2e36 0953 4f72 743a 636f 6f72 6469 6e61  .6.SOrt:coordina
00000020: 7465 0940 5351 0953 4e3a 6368 7231 094c  te.@SQ.SN:chr1.L
```

---

## 2. Magic Numbers

### 2.1 What Are They

**Magic numbers** are fixed bytes at the beginning of a file that identify its format.

```
PNG:  89 50 4E 47 0D 0A 1A 0A  (\x89PNG\r\n\x1a\n)
JPEG: FF D8 FF                 (non-printable)
PDF:  25 50 44 46              (%PDF)
ZIP:  50 4B 03 04              (PK\x03\x04)
GIF:  47 49 46 38              (GIF8)
BAM:  42 41 4D 01              (BAM\x01)
```

> **Note:** Hex viewers like `xxd` display non-printable bytes (outside 0x20–0x7E) as `.` (dot). For example, PNG's first byte `0x89` appears as `.` in `xxd` — so you'll see `.PNG....`, but none of those dots are the real ASCII dot (0x2E).

### 2.2 Popular Signatures

| Format | Magic Bytes (hex) | ASCII | Offset |
|--------|-------------------|-------|--------|
| PNG | `89 50 4E 47 0D 0A 1A 0A` | `\x89PNG\r\n\x1a\n` | 0 |
| JPEG | `FF D8 FF` | non-printable | 0 |
| GIF87a | `47 49 46 38 37 61` | `GIF87a` | 0 |
| GIF89a | `47 49 46 38 39 61` | `GIF89a` | 0 |
| PDF | `25 50 44 46 2D` | `%PDF-` | 0 |
| ZIP | `50 4B 03 04` | `PK\x03\x04` | 0 |
| RAR | `52 61 72 21 1A 07` | `Rar!\x1a\x07` | 0 |
| 7z | `37 7A BC AF 27 1C` | non-printable | 0 |
| ELF | `7F 45 4C 46` | `\x7fELF` | 0 |
| Mach-O | `FE ED FA CE` or `CF FA ED FE` | non-printable | 0 |
| gzip | `1F 8B` | non-printable | 0 |
| bzip2 | `42 5A 68` | `BZh` | 0 |
| tar | `75 73 74 61 72` | `ustar` | 257 |
| SQLite | `53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33` | `SQLite format 3` | 0 |
| MP3 | `FF FB` or `49 44 33` | non-printable / `ID3` | 0 |
| MP4 | `66 74 79 70` | `ftyp` | 4 |
| DOCX/XLSX | `50 4B 03 04` | `PK\x03\x04` | 0 (it's ZIP!) |
| **BAM** | `42 41 4D 01` | `BAM\x01` | 0 |
| **BCF** | `42 43 46 02` | `BCF\x02` | 0 |
| **CRAM** | `43 52 41 4D` | `CRAM` | 0 |

### 2.3 Checking Magic Numbers

```bash
# First 8 bytes of PNG
xxd -l 8 image.png
# 00000000: 8950 4e47 0d0a 1a0a                      .PNG....

# First 3 bytes of JPEG
xxd -l 3 photo.jpg  
# 00000000: ffd8 ff                                  ...

# Check PDF
xxd -l 5 document.pdf
# 00000000: 2550 4446 2d                             %PDF-

# Bioinformatics: Check BAM
xxd -l 4 aligned.bam
# 00000000: 4241 4d01                                BAM.

# Check gzipped FASTQ
xxd -l 2 reads.fastq.gz
# 00000000: 1f8b                                     ..
```

### 2.4 Why File Extension Is Not Reliable

```bash
# Rename PNG to .txt
cp image.png fake.txt

# file will detect correctly!
file fake.txt
# fake.txt: PNG image data, 256 x 256, 8-bit/color RGB

# Attacker can hide malicious file
file dangerous.jpg  # Actually it's EXE
# dangerous.jpg: PE32 executable (GUI) Intel 80386
```

**Bioinformatics Security:**

```bash
# Someone might rename BAM as TXT to bypass filters
mv aligned.bam suspicious.txt

# But file command reveals the truth
file suspicious.txt
# suspicious.txt: data

# Check magic number
xxd -l 4 suspicious.txt
# 00000000: 4241 4d01                                BAM.
```

---

## 3. The file Command

### 3.1 Basic Usage

```bash
# Determine file type
file document.pdf
# document.pdf: PDF document, version 1.4

# Multiple files
file *.txt
# README.txt: UTF-8 Unicode text
# notes.txt: ASCII text

# Recursively for directory
find . -type f -exec file {} \;
```

**Bioinformatics Examples:**

```bash
# Check genomic files
file sequences.fasta
# sequences.fasta: ASCII text

file aligned.bam
# aligned.bam: data

file variants.vcf
# variants.vcf: ASCII text

file reads.fastq.gz
# reads.fastq.gz: gzip compressed data

file annotations.gff3
# annotations.gff3: ASCII text, with very long lines
```

### 3.2 Useful Options

```bash
# MIME type and encoding
file -i document.txt
# document.txt: text/plain; charset=utf-8

# MIME type only
file --mime-type document.pdf
# document.pdf: application/pdf

# Encoding only
file --mime-encoding script.py
# script.py: us-ascii

# Follow symlinks
file -L link_to_file

# Don't show filename
file -b document.pdf
# PDF document, version 1.4

# Read list of files from stdin
find . -name "*.jpg" | file -f -
```

**Bioinformatics Workflow:**

```bash
# Check all files in genomics project
find /data/project -type f | file -f - | grep -E "gzip|ASCII|data"

# Verify FASTA files
file *.fasta *.fa
# sequences.fasta: ASCII text
# reference.fa: ASCII text

# Check compressed files
file *.gz
# reads_R1.fastq.gz: gzip compressed data
# reads_R2.fastq.gz: gzip compressed data
```

### 3.3 How file Works

The `file` command uses:

1. **Magic database** (`/usr/share/misc/magic` or `/usr/share/file/magic`)
2. **Heuristics** for text files
3. **Structure analysis** for binary files

```bash
# View magic database
file -C -m /usr/share/misc/magic

# Magic file version
file -v
```

### 3.4 Writing Custom Magic Rules

```bash
# File: my_magic
# Format: offset type test message

# Define hypothetical format
0 string MYFORMAT My Custom Format
>8 lelong x version %d

# For BAM files (if not in default magic)
0 string BAM\x01 Binary Alignment/Map file
>4 lelong x header length %d
```

```bash
# Use with custom database
file -m my_magic testfile
```

---

## 4. MIME Types

### 4.1 What Is MIME

**MIME** (Multipurpose Internet Mail Extensions) is a standard for describing content type.

Format: `type/subtype`

```
text/plain
text/html
application/json
image/png
audio/mpeg
video/mp4
```

### 4.2 Main Types

| Type | Description | Examples |
|------|-------------|----------|
| text | Text data | text/plain, text/html, text/css |
| image | Images | image/png, image/jpeg, image/gif |
| audio | Audio | audio/mpeg, audio/ogg |
| video | Video | video/mp4, video/webm |
| application | Applications, data | application/json, application/pdf |
| multipart | Compound data | multipart/form-data |

### 4.3 Common MIME Types

| Extension | MIME Type | Notes |
|-----------|-----------|-------|
| .txt | text/plain | |
| .html | text/html | |
| .css | text/css | |
| .js | application/javascript | |
| .json | application/json | |
| .xml | application/xml | |
| .pdf | application/pdf | |
| .zip | application/zip | |
| .png | image/png | |
| .jpg | image/jpeg | |
| .gif | image/gif | |
| .svg | image/svg+xml | |
| .mp3 | audio/mpeg | |
| .mp4 | video/mp4 | |
| .wasm | application/wasm | |
| **Bioinformatics** | | |
| .fasta | text/plain | No official MIME |
| .fastq | text/plain | No official MIME |
| .vcf | text/plain | No official MIME |
| .bam | application/octet-stream | Binary |
| .bcf | application/octet-stream | Binary |

### 4.4 MIME in HTTP

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"message": "Hello"}
```

```http
POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="file"; filename="photo.jpg"
Content-Type: image/jpeg

[binary data]
------WebKitFormBoundary--
```

**Bioinformatics API Example:**

```http
POST /api/analyze HTTP/1.1
Content-Type: application/json

{
  "sequence": "ATCGATCG",
  "format": "fasta",
  "analysis": "blast"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Disposition: attachment; filename="results.vcf"

{
  "status": "complete",
  "results_url": "/download/variants.vcf.gz"
}
```

### 4.5 MIME in Python

```python
import mimetypes

# By extension
print(mimetypes.guess_type('document.pdf'))
# ('application/pdf', None)

print(mimetypes.guess_type('archive.tar.gz'))
# ('application/x-tar', 'gzip')

# By MIME type
print(mimetypes.guess_extension('image/png'))
# '.png'

# With python-magic for content-based detection
import magic

mime = magic.Magic(mime=True)
print(mime.from_file('photo.jpg'))
# 'image/jpeg'
```

**Bioinformatics Example:**

```python
import magic

def detect_genomic_format(filepath):
    """Detect genomic file format."""
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(filepath)
    
    # Check if compressed
    if mime_type == 'application/gzip':
        # Might be .fastq.gz, .vcf.gz, .fasta.gz
        if filepath.endswith('.fastq.gz'):
            return 'FASTQ (gzipped)'
        elif filepath.endswith('.vcf.gz'):
            return 'VCF (gzipped)'
        elif filepath.endswith('.fasta.gz'):
            return 'FASTA (gzipped)'
    
    # Check magic numbers for specific formats
    with open(filepath, 'rb') as f:
        header = f.read(4)
        if header == b'BAM\x01':
            return 'BAM'
        elif header == b'BCF\x02':
            return 'BCF'
        elif header == b'CRAM':
            return 'CRAM'
    
    # Text-based formats
    if mime_type == 'text/plain':
        with open(filepath, 'r') as f:
            first_line = f.readline()
            if first_line.startswith('>'):
                return 'FASTA'
            elif first_line.startswith('@'):
                return 'FASTQ'
            elif first_line.startswith('##fileformat=VCF'):
                return 'VCF'
            elif first_line.startswith('##gff-version'):
                return 'GFF'
    
    return 'Unknown'

# Usage
print(detect_genomic_format('sequences.fasta'))  # FASTA
print(detect_genomic_format('aligned.bam'))      # BAM
print(detect_genomic_format('reads.fastq.gz'))   # FASTQ (gzipped)
```

---

## 5. Binary File Structure

### 5.1 Common Patterns

Most binary formats have:

1. **Header** — metadata at the beginning
2. **Magic number** — format identifier
3. **Chunks/Sections** — data blocks
4. **Footer** — optional data at the end

```
┌─────────────────┐
│  Magic Number   │
├─────────────────┤
│     Header      │
├─────────────────┤
│    Chunk 1      │
├─────────────────┤
│    Chunk 2      │
├─────────────────┤
│      ...        │
├─────────────────┤
│     Footer      │
└─────────────────┘
```

### 5.2 Example: PNG Structure

```
PNG Signature:
89 50 4E 47 0D 0A 1A 0A (8 bytes)

Chunk structure:
┌────────────────────┐
│ Length             │
│ (4 bytes, BE)      │
├────────────────────┤
│ Type               │
│ (4 bytes, ASCII)   │
├────────────────────┤
│ Data               │
│ (Length bytes)     │
├────────────────────┤
│ CRC (4 bytes)      │
└────────────────────┘

Required: IHDR, IDAT, IEND
Optional: tEXt, gAMA, sRGB
```

```bash
# Analyze PNG
xxd image.png | head -10
```

```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
          |_____signature___||len ||__type__|
00000010: 0000 0100 0000 0100 0802 0000 00d3 1025  ...............%
          |width ||height|| | | ||____CRC____|
                            ↓ ↓
                            bit depth, color type
```

### 5.3 Example: BAM Structure

```
BAM File Structure:

┌───────────────────┐
│ Magic: BAM\x01    │
│ (4 bytes)         │
├───────────────────┤
│ Header length     │
│ (4 bytes, LE)     │
├───────────────────┤
│ SAM header text   │
│ (variable)        │
├───────────────────┤
│ # of references   │
│ (4 bytes, LE)     │
├───────────────────┤
│ Reference info    │
│ (variable)        │
├───────────────────┤
│ Alignments        │
│ (BGZF compressed) │
└───────────────────┘

Each alignment:
- block_size (4 bytes)
- refID, pos, flags
- CIGAR, seq, qual, tags
```

```bash
# View BAM header
xxd -l 64 aligned.bam
```

```
00000000: 4241 4d01 3800 0000 4048 4409 5644 3a31  BAM.8...@HD.VD:1
          |_magic_||h_len_||__SAM header text...__|
00000010: 2e36 0953 4f72 743a 636f 6f72 6469 6e61  .6.SOrt:coordina
00000020: 7465 0940 5351 0953 4e3a 6368 7231 094c  te.@SQ.SN:chr1.L
```

### 5.4 Example: VCF vs BCF

**VCF (Text Format):**

```
##fileformat=VCFv4.2
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
chr1    12345   rs123   A       G       30      PASS    DP=10
```

**BCF (Binary Compressed VCF):**

```bash
xxd -l 32 variants.bcf
```

```
00000000: 4243 4602 0200 0000 7800 0000 2323 6669  BCF.....x...##fi
          |_magic_||___header metadata (compressed)___|
```

BCF is ~5x smaller and faster to parse than VCF!

### 5.5 Analyzing Binary Files

**Tools:**

```bash
# binwalk — analyze embedded files
binwalk firmware.bin
# DECIMAL       HEXADECIMAL     DESCRIPTION
# 0             0x0             PNG image, 256 x 256
# 65536         0x10000         gzip compressed data

# strings — extract strings
strings binary_file | head

# exiftool — media file metadata
exiftool photo.jpg

# samtools — BAM file analysis
samtools view -H aligned.bam  # View header
samtools flagstat aligned.bam  # Statistics

# bcftools — VCF/BCF analysis
bcftools view variants.bcf | head  # View as text
bcftools stats variants.bcf        # Statistics
```

**Python:**

```python
import struct

with open('image.png', 'rb') as f:
    # Read PNG signature
    signature = f.read(8)
    print(f"Signature: {signature.hex()}")
    
    # Read first chunk (IHDR)
    length = struct.unpack('>I', f.read(4))[0]
    chunk_type = f.read(4).decode('ascii')
    print(f"Chunk: {chunk_type}, Length: {length}")
    
    # For IHDR: width, height
    if chunk_type == 'IHDR':
        width = struct.unpack('>I', f.read(4))[0]
        height = struct.unpack('>I', f.read(4))[0]
        print(f"Dimensions: {width}x{height}")
```

**Output:**
```
Signature: 89504e470d0a1a0a
Chunk: IHDR, Length: 13
Dimensions: 256x256
```

**BAM Parsing Example:**

```python
import struct

def read_bam_header(filepath):
    """Read BAM file header."""
    with open(filepath, 'rb') as f:
        # Magic number
        magic = f.read(4)
        if magic != b'BAM\x01':
            raise ValueError("Not a BAM file")
        
        # Header text length (little-endian)
        header_len = struct.unpack('<I', f.read(4))[0]
        
        # SAM header text
        sam_header = f.read(header_len).decode('ascii')
        
        # Number of reference sequences
        n_ref = struct.unpack('<I', f.read(4))[0]
        
        return {
            'magic': magic.hex(),
            'sam_header': sam_header,
            'n_references': n_ref
        }

# Usage
info = read_bam_header('aligned.bam')
print(f"BAM file with {info['n_references']} reference sequences")
print(f"Header:\n{info['sam_header']}")
```

---

## 6. Archive Formats

### 6.1 ZIP

**ZIP Structure:**

```
[Local file header 1]
[File data 1]
[Local file header 2]
[File data 2]
...
[Central directory]
[End of central directory record]
```

```bash
# View contents without extracting
unzip -l archive.zip

# File information
zipinfo archive.zip

# DOCX, XLSX, PPTX are ZIP!
unzip -l document.docx
```

### 6.2 tar

**tar** — doesn't compress, only combines files.

```bash
# View contents
tar -tvf archive.tar

# tar.gz (gzip compression)
tar -tzvf archive.tar.gz

# tar.bz2 (bzip2 compression)
tar -tjvf archive.tar.bz2
```

**Bioinformatics:**

```bash
# Archive sequencing data
tar -czf project_data.tar.gz *.fastq.gz *.bam *.vcf

# View archive contents
tar -tzf project_data.tar.gz

# Extract specific file
tar -xzf project_data.tar.gz aligned.bam
```

### 6.3 gzip vs bzip2 vs xz

| Format | Command | Compression | Speed |
|--------|---------|-------------|-------|
| gzip | gzip/gunzip | Good | Fast |
| bzip2 | bzip2/bunzip2 | Better | Slower |
| xz | xz/unxz | Best | Slowest |

```bash
# Size comparison
ls -lh file.txt          # 1000000 bytes
gzip -k file.txt
ls -lh file.txt.gz       # ~350000 bytes (65% reduction)

bzip2 -k file.txt
ls -lh file.txt.bz2      # ~300000 bytes (70% reduction)

xz -k file.txt
ls -lh file.txt.xz       # ~250000 bytes (75% reduction)
```

**Genomics Compression:**

```bash
# FASTQ compression comparison
ls -lh reads.fastq       # 1.2 GB

gzip reads.fastq
ls -lh reads.fastq.gz    # ~300 MB (75% reduction!)

# Decompress for processing
gunzip reads.fastq.gz

# Or stream without decompressing
zcat reads.fastq.gz | head -4
```

**BGZF (Blocked GZIP) for BAM:**

BAM files use BGZF (blocked gzip) which allows:
- Random access (important!)
- Parallel compression/decompression
- Same compression as gzip

```bash
# BAM is BGZF compressed SAM
samtools view aligned.bam | head

# Check if properly BGZF compressed
file aligned.bam
# aligned.bam: data  (not just "gzip compressed")
```

---

## 7. Executable Files

### 7.1 ELF (Linux)

**ELF** (Executable and Linkable Format) — executable file format in Linux.

```bash
# ELF information
file /bin/ls
# /bin/ls: ELF 64-bit LSB pie executable, x86-64

# Detailed information
readelf -h /bin/ls

# Sections
readelf -S /bin/ls

# Symbols
nm /bin/ls
```

### 7.2 Mach-O (macOS)

```bash
# Mach-O information
file /bin/ls
# /bin/ls: Mach-O 64-bit executable arm64

# Detailed information
otool -h /bin/ls
```

### 7.3 PE (Windows)

```bash
# On Linux, you can analyze PE files
file program.exe
# program.exe: PE32+ executable (GUI) x86-64

# With objdump
objdump -x program.exe | head
```

---

## 8. Working with Files in Code

### 8.1 Type Detection in Python

```python
import magic

# Detect by content
def get_file_type(filepath):
    """Determines file type by content."""
    mime = magic.Magic(mime=True)
    file_type = magic.Magic()
    
    return {
        'mime': mime.from_file(filepath),
        'description': file_type.from_file(filepath)
    }

# Check if image
def is_image(filepath):
    """Checks if file is an image."""
    mime = magic.Magic(mime=True)
    return mime.from_file(filepath).startswith('image/')

# Example usage
info = get_file_type('photo.jpg')
print(info)
# {'mime': 'image/jpeg', 'description': 'JPEG image data, JFIF standard 1.01'}
```

**Bioinformatics Example:**

```python
def is_genomic_file(filepath):
    """Check if file is a genomic format."""
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(filepath)
    
    # Check binary formats by magic number
    with open(filepath, 'rb') as f:
        header = f.read(4)
        if header == b'BAM\x01':
            return 'BAM'
        elif header == b'BCF\x02':
            return 'BCF'
        elif header == b'CRAM':
            return 'CRAM'
    
    # Check text formats
    if mime_type.startswith('text/'):
        try:
            with open(filepath, 'r') as f:
                first_line = f.readline()
                if first_line.startswith('>'):
                    return 'FASTA'
                elif first_line.startswith('@'):
                    return 'FASTQ'
                elif first_line.startswith('##fileformat=VCF'):
                    return 'VCF'
                elif first_line.startswith('##gff-version'):
                    return 'GFF'
        except:
            pass
    
    # Check compressed
    if mime_type == 'application/gzip':
        if filepath.endswith('.fastq.gz'):
            return 'FASTQ (gzipped)'
        elif filepath.endswith('.vcf.gz'):
            return 'VCF (gzipped)'
        elif filepath.endswith('.fasta.gz'):
            return 'FASTA (gzipped)'
    
    return None

# Usage
print(is_genomic_file('sequences.fasta'))  # FASTA
print(is_genomic_file('aligned.bam'))      # BAM
print(is_genomic_file('variants.vcf.gz'))  # VCF (gzipped)
```

### 8.2 Safe Upload Validation

```python
import magic
from pathlib import Path

ALLOWED_MIMES = {
    'image/jpeg',
    'image/png',
    'image/gif',
    'application/pdf',
}

def validate_upload(file_path: str) -> bool:
    """
    Validates uploaded file.
    Checks MIME type by content, not extension.
    """
    mime = magic.Magic(mime=True)
    file_mime = mime.from_file(file_path)
    
    if file_mime not in ALLOWED_MIMES:
        return False
    
    # Additionally check magic bytes
    with open(file_path, 'rb') as f:
        header = f.read(8)
        
    # PNG signature
    if file_mime == 'image/png':
        if header[:8] != b'\x89PNG\r\n\x1a\n':
            return False
    
    # JPEG signature
    if file_mime == 'image/jpeg':
        if header[:2] != b'\xff\xd8':
            return False
    
    return True
```

**Bioinformatics Upload Validation:**

```python
ALLOWED_GENOMIC_FORMATS = {
    'fasta': {'text/plain'},
    'fastq': {'text/plain'},
    'vcf': {'text/plain'},
    'bam': {'application/octet-stream'},
    'bcf': {'application/octet-stream'},
}

def validate_genomic_upload(file_path: str, expected_format: str) -> bool:
    """Validate uploaded genomic file."""
    import magic
    
    # Check MIME type
    mime = magic.Magic(mime=True)
    file_mime = mime.from_file(file_path)
    
    # Check magic numbers for binary formats
    with open(file_path, 'rb') as f:
        header = f.read(4)
    
    if expected_format == 'bam':
        if header != b'BAM\x01':
            return False
    elif expected_format == 'bcf':
        if header != b'BCF\x02':
            return False
    elif expected_format == 'fasta':
        # Check first character is '>'
        try:
            with open(file_path, 'r') as f:
                if not f.read(1) == '>':
                    return False
        except:
            return False
    elif expected_format == 'fastq':
        # Check first character is '@'
        try:
            with open(file_path, 'r') as f:
                if not f.read(1) == '@':
                    return False
        except:
            return False
    
    return True

# Usage
if validate_genomic_upload('uploaded_file', 'bam'):
    process_bam_file('uploaded_file')
```

### 8.3 Reading Binary Data

```python
import struct

def read_png_header(filepath):
    """Reads PNG file header."""
    with open(filepath, 'rb') as f:
        # Signature (8 bytes)
        sig = f.read(8)
        if sig != b'\x89PNG\r\n\x1a\n':
            raise ValueError("Not a PNG file")
        
        # IHDR chunk
        length = struct.unpack('>I', f.read(4))[0]
        chunk_type = f.read(4)
        
        if chunk_type != b'IHDR':
            raise ValueError("IHDR chunk not found")
        
        # Parse IHDR data
        data = f.read(length)
        width, height, bit_depth, color_type = struct.unpack('>IIBB', data[:10])
        
        return {
            'width': width,
            'height': height,
            'bit_depth': bit_depth,
            'color_type': color_type
        }

# Usage
info = read_png_header('image.png')
print(f"Image: {info['width']}x{info['height']}")
```

**BAM Header Reading:**

```python
def read_bam_references(filepath):
    """Read reference sequence information from BAM."""
    import struct
    
    with open(filepath, 'rb') as f:
        # Skip magic and header
        magic = f.read(4)
        if magic != b'BAM\x01':
            raise ValueError("Not a BAM file")
        
        # Skip SAM header
        l_text = struct.unpack('<I', f.read(4))[0]
        f.read(l_text)
        
        # Number of reference sequences
        n_ref = struct.unpack('<I', f.read(4))[0]
        
        references = []
        for _ in range(n_ref):
            # Reference name length
            l_name = struct.unpack('<I', f.read(4))[0]
            # Reference name (null-terminated)
            name = f.read(l_name).rstrip(b'\x00').decode('ascii')
            # Reference length
            l_ref = struct.unpack('<I', f.read(4))[0]
            
            references.append({
                'name': name,
                'length': l_ref
            })
        
        return references

# Usage
refs = read_bam_references('aligned.bam')
for ref in refs:
    print(f"{ref['name']}: {ref['length']:,} bp")
```

---

## 9. Creating Custom Formats

### 9.1 Design Principles

1. **Unique signature** — easy to identify
2. **Format version** — for backward compatibility
3. **Self-describing** — sizes, data types in header
4. **Extensibility** — chunk-based structure
5. **Checksums** — data integrity

### 9.2 Simple Format Example

```python
import struct
import hashlib

# Format: MYDATA v1
# Signature: "MYDATA" (6 bytes)
# Version: uint16 (2 bytes)  
# Data length: uint32 (4 bytes)
# Data: variable
# Checksum: MD5 (16 bytes)

class SimpleFormat:
    SIGNATURE = b'MYDATA'
    VERSION = 1
    
    @classmethod
    def write(cls, filepath, data: bytes):
        with open(filepath, 'wb') as f:
            # Signature
            f.write(cls.SIGNATURE)
            # Version
            f.write(struct.pack('>H', cls.VERSION))
            # Data length
            f.write(struct.pack('>I', len(data)))
            # Data
            f.write(data)
            # Checksum
            checksum = hashlib.md5(data).digest()
            f.write(checksum)
    
    @classmethod
    def read(cls, filepath) -> bytes:
        with open(filepath, 'rb') as f:
            # Verify signature
            sig = f.read(6)
            if sig != cls.SIGNATURE:
                raise ValueError("Invalid file signature")
            
            # Read version
            version = struct.unpack('>H', f.read(2))[0]
            if version > cls.VERSION:
                raise ValueError(f"Unsupported version: {version}")
            
            # Read data
            length = struct.unpack('>I', f.read(4))[0]
            data = f.read(length)
            
            # Verify checksum
            expected_checksum = f.read(16)
            actual_checksum = hashlib.md5(data).digest()
            if expected_checksum != actual_checksum:
                raise ValueError("Checksum mismatch")
            
            return data

# Usage
SimpleFormat.write('test.mydata', b'Hello, World!')
content = SimpleFormat.read('test.mydata')
print(content)  # b'Hello, World!'
```

---

## 10. Common Pitfalls

### 10.1 Trusting File Extension

❌ **Error:** Check type only by extension

```python
# Unsafe!
if filename.endswith('.jpg'):
    process_image(filename)
```

✅ **Solution:** Check content

```python
import magic
mime = magic.Magic(mime=True)
if mime.from_file(filename) == 'image/jpeg':
    process_image(filename)
```

**Bioinformatics:**

```python
# Bad
if filename.endswith('.bam'):
    process_bam(filename)

# Good
with open(filename, 'rb') as f:
    if f.read(4) == b'BAM\x01':
        process_bam(filename)
```

### 10.2 Incorrect Binary File Reading

❌ **Error:** Open binary files without 'rb'

```python
# Bad — may corrupt data!
with open('image.png', 'r') as f:
    data = f.read()
```

✅ **Solution:** Always use binary mode

```python
with open('image.png', 'rb') as f:
    data = f.read()
```

### 10.3 Ignoring Endianness

❌ **Error:** Read multi-byte numbers without considering byte order

```python
# Which byte order is in the file?
length = int.from_bytes(f.read(4), 'big')  # or 'little'?
```

✅ **Solution:** Know the format specification

```python
# PNG uses big-endian
length = struct.unpack('>I', f.read(4))[0]

# BAM uses little-endian
length = struct.unpack('<I', f.read(4))[0]
```

### 10.4 Not Checking Magic Numbers

❌ **Error:** Parse file without checking signature

```python
# Dangerous — might not be PNG!
width = struct.unpack('>I', f.read(4))[0]
```

✅ **Solution:** Always check signature

```python
sig = f.read(8)
if sig != b'\x89PNG\r\n\x1a\n':
    raise ValueError("Not a PNG file")
```

---

## 💡 Key Takeaways

- **Text vs Binary**: Text contains characters in encoding, binary contains arbitrary bytes. Use `'rb'` for binary files.

- **Magic numbers more reliable than extensions**: Use `file` or check first bytes to determine type. Don't trust `.bam.txt`!

- **MIME types for web**: Correct Content-Type is critical for HTTP. `application/json`, `image/png`, etc.

- **Understanding structure**: Most formats have header, chunks, footer. Study specifications (PNG, BAM, VCF).

- **Security**: Always check uploaded file type by content, don't trust extension. Critical for genomic data integrity.

- **Bioinformatics specifics**: 
  - FASTA/FASTQ/VCF are text formats (can view with `cat`)
  - BAM/BCF/CRAM are binary (need specialized tools like `samtools`)
  - BGZF compression allows random access in BAM files
  - Always check magic numbers: `BAM\x01`, `BCF\x02`, `CRAM`

---

## 🚀 Next Steps

**Related Modules:**

- [JSON](../05_JSON/) — structure and working with JSON
- [Compression](../10_Compression/) — more details on compression
- [Checksums](../11_Checksums/) — data integrity verification

**Practice Ideas:**

1. Write a script that finds all files with incorrect extensions
2. Analyze JPEG file structure using xxd
3. Create your own simple binary format for task lists
4. Write an upload validator for a web application
5. **Parse a BAM header to extract reference sequences**
6. **Write a tool to detect genomic file formats automatically**
7. **Compare file sizes: FASTA vs FASTQ, SAM vs BAM, VCF vs BCF**

**Going Deeper:**

- Study PNG specification (libpng.org)
- Understand how PDF works
- Learn about ELF format for Linux executables
- **Study SAM/BAM specification thoroughly**
- **Understand BGZF compression used in BAM**
- **Learn about CRAM format for even better compression**

**Connections to Other Courses:**

- **Python Course**: Module 03_Files covers binary file handling in detail
- **Linux Course**: Module 04_Coreutils teaches tools for file manipulation

---

## 📚 Additional Resources

**Tools:**

- [file manual](https://man7.org/linux/man-pages/man1/file.1.html)
- [binwalk](https://github.com/ReFirmLabs/binwalk)
- [python-magic](https://github.com/ahupp/python-magic)
- [samtools](http://www.htslib.org/)
- [bcftools](http://www.htslib.org/doc/bcftools.html)

**Specifications:**

- [PNG Specification](http://www.libpng.org/pub/png/spec/)
- [JPEG Format](https://www.w3.org/Graphics/JPEG/)
- [PDF Reference](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
- [SAM/BAM Specification](https://samtools.github.io/hts-specs/SAMv1.pdf)
- [VCF Specification](https://samtools.github.io/hts-specs/VCFv4.2.pdf)
- [CRAM Format](https://samtools.github.io/hts-specs/CRAMv3.pdf)
- [FASTQ Format](https://en.wikipedia.org/wiki/FASTQ_format)

**Learning:**

- [File Signatures Table](https://www.garykessler.net/library/file_sigs.html)
- [MIME Types Registry](https://www.iana.org/assignments/media-types/)
- [Bioinformatics File Formats](https://genome.ucsc.edu/FAQ/FAQformat.html)

---
