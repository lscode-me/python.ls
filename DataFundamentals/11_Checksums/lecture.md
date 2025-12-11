# Hashes and Checksums
## MD5, SHA, and Data Integrity Verification

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand binary data (Module 02_NumberSystems)
- Have command-line experience
- **For Bioinformatics**: Work with large genomic datasets that require integrity verification (FASTQ, BAM, VCF files)

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Explain the difference between hashes and encryption
- Compute file checksums
- Verify integrity of downloaded files
- Use hashes for deduplication and comparison
- **For Bioinformatics**: Verify genomic data integrity, ensure data provenance in pipelines

---

## 1. What is a Hash Function

### 1.1 Definition

**Hash function** — transforms data of arbitrary size into a fixed-length string.

```
Input: "Hello"           → MD5:  8b1a9953c4611296a827abf8c47804d7
Input: "Hello World"     → MD5:  b10a8db164e0754105b7a99be72e3fe5
Input: "Hello Worl"      → MD5:  e99c029231c55e55de1dc04a2f1c5e24
```

**Bioinformatics Context:**

```
Input: FASTQ file (10GB)     → SHA-256: 3f4e...9a2c (64 hex chars)
Input: Reference genome      → MD5:     c4d5...8b1f (32 hex chars)
```

Checksums are **critical** in bioinformatics to:
- Verify data integrity after transfer (sequencing data, database downloads)
- Ensure reproducibility (same reference genome = same hash)
- Track data provenance in pipelines

### 1.2 Properties of Hash Functions

1. **Deterministic**: Same input → same output
2. **Fast**: Quick computation
3. **Avalanche effect**: Small input change → large output change
4. **Irreversible**: Cannot recover input from hash
5. **Collision resistant**: Hard to find two inputs with same hash

### 1.3 Hash vs Encryption

| Hash | Encryption |
|------|------------|
| Irreversible | Reversible |
| Fixed length | Depends on input |
| No key | Requires key |
| Integrity verification | Data protection |

---

## 2. Popular Algorithms

### 2.1 MD5 (Deprecated)

- **Length**: 128 bits (32 hex characters)
- **Speed**: Very fast
- **Security**: Compromised, not for cryptography

```bash
echo -n "Hello" | md5sum
# 8b1a9953c4611296a827abf8c47804d7  -
```

**Bioinformatics:** Still used for **non-security** purposes like file identification, but SHA-256 preferred.

### 2.2 SHA-1 (Deprecated)

- **Length**: 160 bits (40 hex characters)
- **Security**: Compromised, used in Git

```bash
echo -n "Hello" | sha1sum
# f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0  -
```

### 2.3 SHA-256 (Recommended)

- **Length**: 256 bits (64 hex characters)
- **Security**: Cryptographically strong

```bash
echo -n "Hello" | sha256sum
# 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969  -
```

**Bioinformatics Standard:** SHA-256 is the **gold standard** for:
- NCBI SRA (Sequence Read Archive) checksums
- ENA (European Nucleotide Archive) data verification
- Reference genome integrity (e.g., GRCh38)

### 2.4 SHA-512

- **Length**: 512 bits (128 hex characters)
- **Security**: More resistant, slower

```bash
echo -n "Hello" | sha512sum
```

### 2.5 Comparison

| Algorithm | Length | Speed | Security |
|----------|--------|-------|----------|
| MD5 | 128 bits | Fast | Compromised |
| SHA-1 | 160 bits | Fast | Compromised |
| SHA-256 | 256 bits | Medium | Strong |
| SHA-512 | 512 bits | Slower | Strong |
| BLAKE3 | 256+ bits | Very fast | Strong |

---

## 3. Command Line

### 3.1 Computing Hashes

```bash
# MD5
md5sum file.txt

# SHA-256
sha256sum file.txt

# SHA-512
sha512sum file.txt

# Multiple files
sha256sum *.txt

# From string (no newline!)
echo -n "text" | sha256sum
```

**Bioinformatics Example:**

```bash
# Verify FASTQ file integrity
sha256sum sample1_R1.fastq.gz
# 3f4e...9a2c  sample1_R1.fastq.gz

# Compute checksums for all BAM files
sha256sum *.bam > checksums.sha256
```

### 3.2 Verifying Hashes

```bash
# Create checksum file
sha256sum *.iso > checksums.sha256

# Verify
sha256sum -c checksums.sha256
# file1.iso: OK
# file2.iso: FAILED
```

**Bioinformatics Pipeline:**

```bash
# Download reference genome with checksum file
wget ftp://ftp.ensembl.org/pub/release-109/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
wget ftp://ftp.ensembl.org/pub/release-109/fasta/homo_sapiens/dna/CHECKSUMS

# Verify
sha256sum -c CHECKSUMS
# Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz: OK
```

### 3.3 macOS

```bash
# On macOS, use shasum
shasum -a 256 file.txt
shasum -a 512 file.txt

# MD5
md5 file.txt
# or
md5 -q file.txt  # Hash only
```

---

## 4. Practical Applications

### 4.1 Verifying Downloads

```bash
# Downloaded Ubuntu ISO, want to verify
# 1. Download checksum file from official site
wget https://releases.ubuntu.com/22.04/SHA256SUMS

# 2. Verify
sha256sum -c SHA256SUMS 2>/dev/null | grep ubuntu-22.04-desktop-amd64.iso
# ubuntu-22.04-desktop-amd64.iso: OK
```

**Bioinformatics:**

```bash
# NCBI SRA provides MD5 checksums
# After downloading SRR123456.fastq.gz
echo "a1b2c3d4e5f6... SRR123456.fastq.gz" > expected.md5
md5sum -c expected.md5
# SRR123456.fastq.gz: OK
```

### 4.2 Comparing Files

```bash
# Fast comparison without byte-by-byte reading
if [ "$(md5sum file1)" == "$(md5sum file2)" ]; then
    echo "Files are identical"
fi
```

**Bioinformatics Use Case:**

```bash
# Check if two BAM files are identical (after transfer)
sha256sum original.bam transferred.bam
# If hashes match → transfer successful
```

### 4.3 Deduplication

```bash
# Find duplicates by hash
find . -type f -exec md5sum {} \; | sort | uniq -d -w32
```

**Bioinformatics:** Useful for identifying duplicate FASTQ files from re-runs.

### 4.4 Caching

```python
import hashlib

def cache_key(data):
    """Generate cache key for data."""
    return hashlib.sha256(data.encode()).hexdigest()[:16]
```

**Bioinformatics:** Cache intermediate results (e.g., alignment metrics) keyed by input file hash.

---

## 5. Python and Hashes

### 5.1 hashlib

```python
import hashlib

# From string
text = "Hello, World!"
md5_hash = hashlib.md5(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print(f"MD5: {md5_hash}")
print(f"SHA-256: {sha256_hash}")
```

### 5.2 File Hash

```python
import hashlib

def file_hash(filepath, algorithm='sha256'):
    """Compute file hash."""
    h = hashlib.new(algorithm)
    
    with open(filepath, 'rb') as f:
        # Read in chunks for large files
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    
    return h.hexdigest()

# Usage
print(file_hash('large_file.iso'))
print(file_hash('file.txt', 'md5'))
```

**Bioinformatics Example:**

```python
import hashlib
import gzip

def fastq_hash(filepath):
    """Compute SHA-256 hash of gzipped FASTQ file."""
    h = hashlib.sha256()
    
    with gzip.open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    
    return h.hexdigest()

# Verify sequencing data
hash_val = fastq_hash('sample_R1.fastq.gz')
print(f"FASTQ hash: {hash_val}")

# Compare with expected hash from sequencing facility
expected = "3f4e9a2c..."
if hash_val == expected:
    print("✅ Data integrity verified!")
else:
    print("❌ Data corruption detected!")
```

### 5.3 Comparing Files

```python
def files_equal(file1, file2):
    """Compare files by SHA-256."""
    return file_hash(file1) == file_hash(file2)
```

---

## 6. Security

### 6.1 Do NOT Use For

❌ Storing passwords directly
❌ MD5/SHA-1 for security

### 6.2 For Passwords

```python
# Use bcrypt, argon2, or scrypt
import bcrypt

password = b"secret_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Verification
if bcrypt.checkpw(password, hashed):
    print("Password correct!")
```

**Bioinformatics:** Patient data security requires proper password hashing with bcrypt/argon2.

---

## 💡 Key Takeaways

- **Hash is irreversible**: Cannot recover data from hash.

- **SHA-256 — modern standard**: MD5 and SHA-1 are compromised.

- **Verify downloads**: Always check hash against official source.

- **For passwords — specialized algorithms**: bcrypt, argon2, not SHA-256.

- **🧬 For Bioinformatics**: Always verify checksums for downloaded genomic data, track data provenance with hashes, use SHA-256 for reproducibility.

---

## 📚 Additional Resources

- [SHA-2 Wikipedia](https://en.wikipedia.org/wiki/SHA-2)
- [hashlib Python docs](https://docs.python.org/3/library/hashlib.html)
- [bcrypt](https://github.com/pyca/bcrypt/)
- [NCBI SRA Data Integrity](https://www.ncbi.nlm.nih.gov/sra/docs/sra-data-integrity/)

---

## 🚀 Next Steps

**Next modules:**

- [12_DataTransfer](../12_DataTransfer/) — Data Transfer and Encoding

**Practice:**

1. Compute SHA-256 hash for a downloaded file and verify against official source
2. Write a script to verify integrity of all files in a directory
3. Explore the difference between MD5 and SHA-256 in practice
4. **Bioinformatics**: Verify checksums for reference genome downloads from NCBI/Ensembl
