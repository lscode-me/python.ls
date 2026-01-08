# Compression - Quiz

Test your knowledge on "Data Compression".

---

## Question 1: Compression Types

What type of compression is used for text files?

A) Hybrid

B) Lossless

C) Partial

D) Lossy

---

## Question 2: gzip Command

What command compresses a file with gzip?

A) `pack file.txt`

B) gzip file.txt

C) `compress file.txt`

D) `zip file.txt`

---

## Question 3: Decompressing gzip

What command decompresses a .gz file?

A) `ungzip file.txt.gz`

B) `extract file.txt.gz`

C) `unzip file.txt.gz`

D) gunzip file.txt.gz

---

## Question 4: tar Purpose

What does tar do?

A) Compresses files

B) Removes duplicates

C) Encrypts files

D) Combines files into one archive

---

## Question 5: tar + gzip

What tar flag uses gzip compression?

A) -z

B) `-Z`

C) `-c`

D) `-g`

---

## Question 6: tar Creation

What command creates a tar.gz archive?

A) `tar -azvf archive.tar.gz dir/`

B) tar -czvf archive.tar.gz dir/

C) `tar -tzvf archive.tar.gz dir/`

D) `tar -xzvf archive.tar.gz dir/`

---

## Question 7: tar Extraction

What tar flag extracts files?

A) `-r`

B) `-t`

C) `-c`

D) -x

---

## Question 8: bzip2 Extension

What extension do bzip2-compressed files have?

A) `.b2`

B) `.bz`

C) .bz2

D) `.bzip`

---

## Question 9: xz Compression

Which algorithm provides the best compression?

A) xz

B) bzip2

C) lz4

D) gzip

---

## Question 10: tar bzip2 Flag

What tar flag uses bzip2?

A) `-B`

B) -j

C) `-b`

D) `-2`

---

## Question 11: zcat

What does the zcat command do?

A) Shows .gz file contents without decompressing to disk

B) Creates a zip archive

C) Concatenates zip files

D) Checks archive integrity

---

## Question 12: gzip -k

What does the `-k` flag do in gzip?

A) Uses maximum compression

B) Keeps the original file

C) Shows progress

D) Recursively compresses directories

---

## Question 13: Python gzip

How do you open a gzip file for reading text in Python?

A) `gzip.open('file.gz', 'r')`

B) `open('file.gz', 'gz')`

C) gzip.open('file.gz', 'rt')

D) `gzip.read('file.gz')`

---

## Question 14: ZIP vs tar

What is true about ZIP compared to tar.gz?

A) ZIP doesn't support compression

B) ZIP doesn't support directories

C) ZIP is Windows-only

D) ZIP allows extracting individual files without full decompression

---

## Question 15: tar xz Flag

What tar flag uses xz compression?

A) `-Z`

B) `-X`

C) -J

D) `-x`

---

## Question 16: zstd

What characterizes the zstd format?

A) Slowest compression

B) Windows-only

C) Excellent compression/speed ratio (modern standard)

D) Doesn't support streaming

---

## Question 17: Python tarfile

How do you create a tar.gz archive in Python?

A) tarfile.open('archive.tar.gz', 'w:gz')

B) `tarfile.write('archive.tar.gz')`

C) `tarfile.create('archive.tar.gz')`

D) `tar.gz('archive.tar.gz')`

---

## Question 18: unzip Viewing

What command shows ZIP contents without extraction?

A) unzip -l archive.zip

B) `unzip -t archive.zip`

C) `unzip -p archive.zip`

D) `unzip -v archive.zip`

---

## Question 19: gzip Level

What compression level range does gzip support?

A) 1-9

B) 0-100

C) 1-10

D) 0-5

---

## Question 20: tar -C

What does the `-C` flag do in tar?

A) Specifies extraction directory

B) Creates an archive

C) Checks integrity

D) Compresses with gzip

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Lossless is used for text, code, data. Lossy is for media. |
| 2 | A | `gzip file.txt` compresses the file, creating file.txt.gz. |
| 3 | B | `gunzip` or `gzip -d` decompresses .gz files. |
| 4 | A | tar (tape archive) combines files without compression. |
| 5 | C | `-z` activates gzip compression in tar. |
| 6 | B | `-c` creates, `-z` gzip, `-v` verbose, `-f` file. |
| 7 | B | `-x` (extract) extracts files from archive. |
| 8 | D | bzip2 creates files with .bz2 extension. |
| 9 | B | xz (LZMA2) provides best compression, but slower. |
| 10 | C | `-j` activates bzip2 in tar. |
| 11 | A | `zcat` outputs .gz contents without decompressing to disk. |
| 12 | D | `-k` (keep) preserves the original file after compression. |
| 13 | C | `'rt'` = read text, for text files with encoding. |
| 14 | A | ZIP supports random access — can extract one file. |
| 15 | B | `-J` (uppercase) activates xz compression in tar. |
| 16 | D | zstd (Zstandard) — modern algorithm with excellent balance. |
| 17 | D | `tarfile.open('file.tar.gz', 'w:gz')` — create tar.gz. |
| 18 | C | `unzip -l` shows list of files in archive. |
| 19 | C | gzip supports levels 1-9 (1=fast, 9=maximum). |
| 20 | A | `-C directory` specifies target directory for extraction. |

---

## Scoring Guide

| Result | Rating | Recommendations |
|--------|--------|----------------|
| **17-20 correct (85-100%)** | 🏆 Excellent! | You master data compression! |
| **14-16 correct (70-84%)** | ✅ Good | Review tar flags. |
| **10-13 correct (50-69%)** | ⚠️ Satisfactory | Re-read the tar section. |
| **Less than 10 correct (<50%)** | 📚 Needs Review | Recommended to re-read the lecture. |

---
