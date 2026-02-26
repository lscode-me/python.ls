# Number Systems - Quiz

Test your knowledge on "Number Systems: Bits, Bytes, Hex, and Data Representation".

---

## Question 1: Bits and Bytes

How many bits are in one byte?

A) 8

B) 32

C) 4

D) 16

---

## Question 2: Byte Values

How many different values can one byte represent?

A) 128

B) 512

C) 1024

D) 256

---

## Question 3: Binary → Decimal

What is binary number 101010 in decimal?

A) 62

B) 42

C) 52

D) 32

---

## Question 4: Decimal → Binary

How do you write the number 15 in binary?

A) 1011

B) 10000

C) 1110

D) 1111

---

## Question 5: Hex Characters

Which characters are used in the hexadecimal system?

A) 0-9

B) 0-9 and A-F

C) 0-9 and A-Z

D) A-P

---

## Question 6: Hex → Decimal

What is 0xFF in decimal?

A) 256

B) 15

C) 127

D) 255

---

## Question 7: Nibble

What is a nibble?

A) 4 bits

B) 8 bits

C) 2 bits

D) 16 bits

---

## Question 8: Unix Permissions

What do file permissions 755 mean in Unix?

A) rwxr-xr-x (owner: all, others: read and execute)

B) rw-rw-rw- (everyone can read and write)

C) rwx------ (only owner)

D) rwxrwxrwx (everyone can do everything)

---

## Question 9: Octal System

What is the base of the octal number system?

A) 2

B) 10

C) 16

D) 8

---

## Question 10: Big-Endian

How is the number 0x12345678 stored in Big-Endian?

A) 78 56 34 12

B) 56 78 12 34

C) 34 12 78 56

D) 12 34 56 78

---

## Question 11: Little-Endian

Which architecture uses Little-Endian by default?

A) SPARC

B) PowerPC (old Mac)

C) x86-64 (Intel/AMD)

D) Network protocols

---

## Question 12: Network Byte Order

What byte order is used in TCP/IP network protocols?

A) Little-Endian

B) Big-Endian (Network Byte Order)

C) Middle-Endian

D) Platform-dependent

---

## Question 13: Hex Dump

Which command shows a hex dump of a file in Linux?

A) xxd file

B) cat -x file

C) hex file

D) dump -h file

---

## Question 14: Python hex

What is the result of `hex(42)` in Python?

A) `2a`

B) `0x42`

C) `0x2a`

D) `42`

---

## Question 15: Binary in Python

How do you get binary representation of a number in Python?

A) bin(42)

B) int.binary(42)

C) binary(42)

D) to_binary(42)

---

## Question 16: Signed Integer

What is the range of values for a signed 8-bit integer?

A) 0 to 255

B) -128 to 127

C) -127 to 128

D) -256 to 255

---

## Question 17: Two's Complement

How is -5 represented in 8-bit two's complement?

A) 10000101

B) 00000101

C) 11111011

D) 11111010

---

## Question 18: Floating Point

Why is `0.1 + 0.2` not exactly `0.3` in Python?

A) Floating point numbers have limited precision

B) 0.3 is a reserved value

C) It's a bug in Python

D) You need to use a different operator

---

## Question 19: Data Size

How many bytes in 1 kilobyte (IEC standard)?

A) 1048

B) 1000

C) 1028

D) 1024

---

## Question 20: xxd Command

What does the command `xxd -r -p` do?

A) Converts hex string back to binary data

B) Removes spaces from hex dump

C) Shows hex dump in reverse order

D) Shows only printable characters

---

## Question 21: FASTQ Quality

What is the Phred quality score for ASCII character 'I' in Phred+33 encoding?

A) 73

B) 106

C) 40

D) 33

---

## Question 22: BAM Magic Number

What are the first 4 bytes of a BAM file in hex?

A) 1F 8B 08 00 (gzip)

B) 42 41 4D 01 (BAM\x01)

C) 89 50 4E 47 (PNG)

D) 25 50 44 46 (PDF)

---

## Question 23: DNA Encoding

How many bits are needed to encode one DNA base (A, C, G, T)?

A) 1 bit

B) 2 bits

C) 4 bits

D) 8 bits

---

## Question 24: BAM Endianness

What byte order do BAM files use for multi-byte integers?

A) Big-Endian

B) Little-Endian

C) Network Byte Order

D) Platform-dependent

---

## Question 25: Genome Size

Human genome is approximately 3.2 billion base pairs. If stored uncompressed with 2 bits per base, how much space is needed?

A) 400 MB

B) 800 MB

C) 3.2 GB

D) 6.4 GB

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | A byte always consists of 8 bits. This is the standard data unit. |
| 2 | D | 8 bits = 2^8 = 256 possible values (from 0 to 255). |
| 3 | B | 101010 = 32 + 8 + 2 = 42 (positions: 1×32 + 0×16 + 1×8 + 0×4 + 1×2 + 0×1). |
| 4 | D | 15 = 8 + 4 + 2 + 1 = 1111 in binary. |
| 5 | A | Hex uses 0-9 and A-F (16 characters total for base 16). |
| 6 | B | 0xFF = 15×16 + 15 = 240 + 15 = 255. |
| 7 | A | Nibble is 4 bits, half a byte, one hex digit. |
| 8 | A | 7=rwx, 5=r-x, 5=r-x. Owner has all, group and others have read and execute. |
| 9 | D | Octal system has base 8, uses digits 0-7. |
| 10 | D | Big-Endian stores most significant byte first: 12 34 56 78. |
| 11 | C | x86-64 (Intel/AMD) uses Little-Endian. |
| 12 | B | TCP/IP always uses Big-Endian (Network Byte Order). |
| 13 | A | `xxd` is the standard utility for hex dump in Linux. |
| 14 | A | `hex(42)` returns string `'0x2a'` (42 in hex = 2a). |
| 15 | A | `bin(42)` returns `'0b101010'`. |
| 16 | A | Signed 8-bit: -128 to 127. Unsigned: 0 to 255. |
| 17 | B | -5 in two's complement: invert 00000101 = 11111010, add 1 = 11111011. |
| 18 | A | IEEE 754 floating point has limited precision, 0.1 is infinite fraction in binary. |
| 19 | B | 1 KiB (kibibyte per IEC) = 1024 bytes. Manufacturers often use 1000. |
| 20 | A | `xxd -r -p` — reverse plain hex dump, converts hex to binary. |
| 21 | A | ASCII 'I' = 73, Phred+33 quality = 73 - 33 = 40 (high quality). |
| 22 | B | BAM files start with magic number 42 41 4D 01 ("BAM" + version byte). |
| 23 | B | 2 bits encode 4 values: 00=A, 01=C, 10=G, 11=T. Efficient compression! |
| 24 | B | BAM format specification requires Little-Endian for all multi-byte integers. |
| 25 | B | 3.2 billion bp × 2 bits/bp = 6.4 billion bits ÷ 8 = 800 million bytes = ~800 MB. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **23-25 correct (92-100%)** | 🏆 Excellent! | Outstanding understanding of number systems! Move to Encodings module. |
| **20-22 correct (80-91%)** | ✅ Very Good | Great work! Review endianness and signed/unsigned concepts. |
| **16-19 correct (64-79%)** | ⚠️ Good | Decent grasp. Re-read sections on system conversions and bioinformatics applications. |
| **12-15 correct (48-63%)** | 📚 Needs Review | Study conversion methods between decimal, binary, and hex. |
| **Less than 12 correct (<48%)** | 🔄 Study Again | Carefully re-read the lecture and practice with examples. |

---

## Next Steps

### If you scored 80% or higher:
- Move to [Module 03: Character Encodings](../03_Encodings/)
- Practice converting between number systems
- Examine real BAM/FASTQ files with `xxd`
- Try the Python Course (Module 03_Files for binary data handling)

### If you scored 50-79%:
- Review lecture sections on hex and binary conversions
- Practice with command-line tools (`xxd`, `printf`, `bc`)
- Work through Python examples for number system conversions
- Focus on understanding endianness with practical examples

### If you scored below 50%:
- Re-read the lecture step by step
- Work through each example manually
- Use online converters to verify your work
- Focus on understanding why each system exists

---

## Practice Exercises

To solidify your understanding:

1. **Number Conversions**: Convert between decimal, binary, and hex manually
2. **FASTQ Quality**: Write a Python script to convert quality strings to Phred scores
3. **Hex Analysis**: Examine a BAM file header with `xxd` and identify components
4. **Unix Permissions**: Practice setting different file permissions and understanding octal
5. **Endianness**: Create files with multi-byte integers and view them in hex
6. **DNA Encoding**: Write a program to compress DNA sequences using 2-bit encoding
7. **File Size Calculations**: Calculate storage requirements for genomic datasets

---

## Bioinformatics Applications

### FASTQ Quality Scores
```python
# Practice converting FASTQ quality strings
quality = "IIIIII!!!!"  # Mix of high and low quality
for char in quality:
    phred = ord(char) - 33
    print(f"{char} -> ASCII {ord(char)} -> Phred {phred}")
```

### BAM File Analysis
```bash
# View BAM magic number
xxd -l 32 aligned.bam

# Compare with uncompressed SAM (text)
samtools view -h aligned.bam | head

# Understand why BAM is more efficient
```

### DNA Compression
```python
# 2-bit encoding for DNA
encoding = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
sequence = "ACGT"
compressed = sum(encoding[base] << (2*i) for i, base in enumerate(reversed(sequence)))
print(f"{sequence} -> {compressed:08b} ({compressed:#04x})")
```

---
