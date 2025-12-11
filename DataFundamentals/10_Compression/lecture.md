# Data Compression
## gzip, bzip2, xz and Archiving for Bioinformatics

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand file formats (Module 04_FileFormats)
- Have experience working with command line
- Know basics of file operations

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Compress and decompress files with gzip, bzip2, xz
- Create and extract tar archives
- Choose appropriate compression algorithm
- Work with compressed data in Python
- Handle compressed bioinformatics data formats (FASTQ.gz, BAM, VCF.gz)

---

## 1. Compression Basics

### 1.1 Lossless vs Lossy

**Lossless (no data loss):**

- gzip, bzip2, xz, ZIP
- Complete data recovery
- For text, code, biological data

**Lossy (with data loss):**

- JPEG, MP3, H.264
- Smaller size, quality loss
- For media (not for biological data!)

**🧬 In Bioinformatics:**

FASTQ, BAM, CRAM files use **lossless** compression to preserve sequence data integrity. Lossy compression is never acceptable for genomic data.

### 1.2 Size/Speed Tradeoff

```
Compression Speed                    Compression Ratio
←─────────────────────────────────────────────────→
lz4   gzip   bzip2   xz/lzma
fast  ←──────────────────→  slow
```

**🧬 Common in Bioinformatics:**

- **FASTQ.gz**: gzip-compressed (standard)
- **BAM**: BGZF (blocked gzip, allows random access)
- **CRAM**: Advanced compression with reference genome
- **VCF.gz**: gzip or bgzip compressed

---

## 2. gzip

### 2.1 gzip Basics

```bash
# Compress (replaces original!)
gzip file.txt
# Result: file.txt.gz

# Decompress
gunzip file.txt.gz
# or
gzip -d file.txt.gz

# Keep original
gzip -k file.txt
# Result: file.txt and file.txt.gz
```

**🧬 Bioinformatics Examples:**

```bash
# Compress FASTQ file
gzip sample_R1.fastq
# Result: sample_R1.fastq.gz

# Decompress for processing
gunzip sample_R1.fastq.gz

# Keep original (safer for valuable data)
gzip -k sample_R1.fastq
```

### 2.2 gzip Options

```bash
# Compression level (1-9, default=6)
gzip -9 file.txt    # Maximum compression
gzip -1 file.txt    # Fast compression

# Recursive
gzip -r directory/

# View information
gzip -l file.txt.gz
```

**🧬 Bioinformatics:**

```bash
# Maximum compression for archival
gzip -9 old_experiment.fastq

# Fast compression for intermediate files
gzip -1 temp_results.txt

# Compress all FASTQ files in directory
gzip -k *.fastq

# Check compression ratio
gzip -l sample_R1.fastq.gz
```

### 2.3 Reading Compressed Files

```bash
# View without decompressing
zcat file.txt.gz
zless file.txt.gz
zgrep "pattern" file.txt.gz
```

**🧬 Bioinformatics Examples:**

```bash
# View first sequences in FASTQ.gz
zcat sample_R1.fastq.gz | head -20

# Search for adapter sequences
zgrep "AGATCGGAAGAGC" sample_R1.fastq.gz

# Count reads in compressed FASTQ
zcat sample_R1.fastq.gz | wc -l
# Divide by 4 for number of reads

# Filter quality scores
zcat sample_R1.fastq.gz | awk 'NR%4==0' | head -1000
```

---

## 3. bzip2

### 3.1 Usage

```bash
# Compress
bzip2 file.txt
# Result: file.txt.bz2

# Decompress
bunzip2 file.txt.bz2
bzip2 -d file.txt.bz2

# Keep original
bzip2 -k file.txt
```

### 3.2 Comparison with gzip

| Aspect | gzip | bzip2 |
|--------|------|-------|
| Compression | ~70% | ~60% |
| Speed | Faster | Slower |
| Memory | Less | More |
| Extension | .gz | .bz2 |

**🧬 In Bioinformatics:**

bzip2 provides better compression but is slower. Less common than gzip for sequencing data. Sometimes used for long-term archival of analysis results.

---

## 4. xz (LZMA)

### 4.1 Usage

```bash
# Compress
xz file.txt
# Result: file.txt.xz

# Decompress
unxz file.txt.xz
xz -d file.txt.xz

# Keep original
xz -k file.txt

# View
xzcat file.txt.xz
```

### 4.2 xz Advantages

- Best compression
- Used for Linux distributions
- Slower but smaller result

**🧬 Bioinformatics:**

xz is excellent for archiving old sequencing data when storage is expensive and decompression time is not critical.

```bash
# Archive old experiment data
xz -9 -k old_rnaseq_results.fastq
# Excellent compression for rarely-accessed data
```

---

## 5. tar (Archiving)

### 5.1 What is tar

**tar** (tape archive) — combines files into one archive WITHOUT compression.

```bash
# Create archive
tar -cvf archive.tar file1.txt file2.txt directory/
# c = create, v = verbose, f = file

# View contents
tar -tvf archive.tar

# Extract
tar -xvf archive.tar
# x = extract

# Extract to specific directory
tar -xvf archive.tar -C /destination/
```

**🧬 Bioinformatics Examples:**

```bash
# Archive entire experiment
tar -cvf experiment_PAT001.tar fastq/ alignments/ variants/

# View archive contents
tar -tvf experiment_PAT001.tar

# Extract specific sample
tar -xvf experiment_PAT001.tar fastq/PAT001_R1.fastq.gz
```

### 5.2 tar + Compression

```bash
# tar.gz (gzip)
tar -czvf archive.tar.gz directory/
tar -xzvf archive.tar.gz

# tar.bz2 (bzip2)
tar -cjvf archive.tar.bz2 directory/
tar -xjvf archive.tar.bz2

# tar.xz (xz)
tar -cJvf archive.tar.xz directory/
tar -xJvf archive.tar.xz
```

**Compression flags:**

- `-z` = gzip
- `-j` = bzip2
- `-J` = xz

**🧬 Bioinformatics Examples:**

```bash
# Archive and compress experiment (most common)
tar -czvf RNA_Seq_2024_01.tar.gz \
    raw_data/ \
    aligned/ \
    results/ \
    metadata.csv

# Maximum compression for archival
tar -cJvf old_experiment_archive.tar.xz old_data/

# Extract compressed archive
tar -xzvf RNA_Seq_2024_01.tar.gz

# Extract to specific location
tar -xzvf RNA_Seq_2024_01.tar.gz -C /archive/2024/
```

---

## 6. ZIP

### 6.1 Usage

```bash
# Create
zip archive.zip file1.txt file2.txt
zip -r archive.zip directory/  # Recursive

# Extract
unzip archive.zip
unzip archive.zip -d /destination/

# View
unzip -l archive.zip
```

### 6.2 ZIP vs tar.gz

| ZIP | tar.gz |
|-----|--------|
| Single file | tar + gzip separate |
| Random access | Sequential |
| Windows standard | Unix standard |
| Built-in compression | Separate compression |

**🧬 In Bioinformatics:**

ZIP is useful for sharing data with Windows users or for archives with many small files that need random access.

```bash
# Create ZIP of results for collaborators
zip -r analysis_results.zip reports/ figures/ tables/

# Extract specific file
unzip analysis_results.zip reports/summary.pdf
```

---

## 7. Python and Compression

### 7.1 gzip

```python
import gzip

# Write
with gzip.open('file.txt.gz', 'wt', encoding='utf-8') as f:
    f.write('Hello, World!')

# Read
with gzip.open('file.txt.gz', 'rt', encoding='utf-8') as f:
    content = f.read()
```

**🧬 Bioinformatics Example:**

```python
import gzip

# Read compressed FASTQ
with gzip.open('sample_R1.fastq.gz', 'rt') as f:
    for i, line in enumerate(f):
        if i % 4 == 0:  # Header lines
            print(line.strip())
        if i >= 20:  # First 5 reads
            break

# Write filtered reads to compressed file
with gzip.open('filtered_R1.fastq.gz', 'wt') as out:
    with gzip.open('sample_R1.fastq.gz', 'rt') as in_file:
        for i, line in enumerate(in_file):
            if some_filter_condition(line):
                out.write(line)

# Process VCF.gz file
import csv
with gzip.open('variants.vcf.gz', 'rt') as f:
    for line in f:
        if line.startswith('#'):  # Skip headers
            continue
        fields = line.strip().split('\t')
        chrom, pos, ref, alt = fields[0], fields[1], fields[3], fields[4]
        print(f"{chrom}:{pos} {ref}>{alt}")
```

### 7.2 tarfile

```python
import tarfile

# Create tar.gz
with tarfile.open('archive.tar.gz', 'w:gz') as tar:
    tar.add('directory/')
    tar.add('file.txt')

# Extract
with tarfile.open('archive.tar.gz', 'r:gz') as tar:
    tar.extractall('destination/')

# View contents
with tarfile.open('archive.tar.gz', 'r:gz') as tar:
    for member in tar.getmembers():
        print(member.name)
```

**🧬 Bioinformatics Example:**

```python
import tarfile
import os

# Archive experiment data
def archive_experiment(experiment_id, output_dir='/archive'):
    archive_name = f"{output_dir}/{experiment_id}.tar.gz"
    
    with tarfile.open(archive_name, 'w:gz') as tar:
        tar.add(f'raw_data/{experiment_id}')
        tar.add(f'results/{experiment_id}')
        tar.add(f'metadata/{experiment_id}.csv')
    
    print(f"Archived to {archive_name}")
    return archive_name

# Extract specific sample from archive
def extract_sample(archive_path, sample_id, output_dir='.'):
    with tarfile.open(archive_path, 'r:gz') as tar:
        # Extract only files matching sample_id
        members = [m for m in tar.getmembers() if sample_id in m.name]
        tar.extractall(output_dir, members=members)
    
    print(f"Extracted {len(members)} files for {sample_id}")

# List archive contents
def list_archive(archive_path):
    with tarfile.open(archive_path, 'r:gz') as tar:
        for member in tar.getmembers():
            size_mb = member.size / (1024 * 1024)
            print(f"{member.name}: {size_mb:.2f} MB")
```

### 7.3 zipfile

```python
import zipfile

# Create
with zipfile.ZipFile('archive.zip', 'w') as zf:
    zf.write('file.txt')
    zf.write('directory/file.txt', arcname='renamed.txt')

# Read
with zipfile.ZipFile('archive.zip', 'r') as zf:
    print(zf.namelist())
    content = zf.read('file.txt')
```

---

## 8. Format Comparison

| Format | Compression | Speed | Use Case |
|--------|-------------|-------|----------|
| gzip | Good | Fast | Web, logs, FASTQ |
| bzip2 | Better | Medium | Archives |
| xz | Best | Slow | Distributions |
| lz4 | Medium | Very fast | Real-time |
| zstd | Excellent | Fast | Modern standard |

**🧬 Bioinformatics Recommendations:**

| Format | Use Case |
|--------|----------|
| **gzip (.gz)** | FASTQ files, VCF files (standard) |
| **bgzip** | BAM files, VCF for tabix indexing |
| **CRAM** | Maximum compression with reference |
| **tar.gz** | Archiving entire experiments |
| **xz** | Long-term cold storage |

---

## 💡 Key Takeaways

- **tar — archiving, not compression**: tar combines files, gzip/bzip2/xz compress.

- **Algorithm choice**: gzip for speed (standard for FASTQ), xz for size, zstd for balance.

- **tar flags**: `-z` (gzip), `-j` (bzip2), `-J` (xz).

- **ZIP for cross-platform**: If Windows compatibility needed.

- **🧬 Bioinformatics**: FASTQ.gz and BAM (bgzip) are universal standards. Always compress sequencing data.

---

## 🚀 Next Steps

**Related Modules:**

- [11_Checksums](../11_Checksums/) — Checksums and hashing
- [12_DataTransfer](../12_DataTransfer/) — Data transfer and encoding

**Practice Ideas:**

1. Compare compression ratios of gzip, bzip2, xz on FASTQ files
2. Create tar.gz archive of experiment and extract it
3. Measure compression time vs size for different algorithms
4. Process compressed FASTQ files without decompression
5. Archive old sequencing data with maximum compression

**Going Deeper:**

- Learn about BGZF (Blocked Gzip Format) used in BAM files
- Study CRAM format for maximum genomic data compression
- Explore zstd (Zstandard) as modern alternative
- Investigate lz4 for fast compression of intermediate files

---

## 📚 Additional Resources

**General:**

- [GNU gzip](https://www.gnu.org/software/gzip/)
- [XZ Utils](https://tukaani.org/xz/)
- [Zstandard](https://facebook.github.io/zstd/)

**Bioinformatics:**

- [SAM/BAM/CRAM Format Specification](https://samtools.github.io/hts-specs/)
- [BGZF Format](https://samtools.github.io/hts-specs/SAMv1.pdf)
- [samtools Documentation](http://www.htslib.org/)
- [pysam Python library](https://pysam.readthedocs.io/)

---
