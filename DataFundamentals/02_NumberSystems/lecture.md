# Number Systems
## Bits, Bytes, Hex, and Data Representation in Memory

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand what data and formats are (module 01_Intro)
- Know basic arithmetic
- Understand that computers work with electrical signals

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Convert numbers between binary, decimal, and hexadecimal systems
- Explain the difference between a bit and a byte
- Work with hex representation of data
- Understand the concept of endianness (byte order)
- Use tools for working with binary data
- Apply these concepts to genomic data and bioinformatics files

---

## 1. Why Learn Number Systems

### 1.1 Why This Matters in IT and Life Sciences

In everyday life we use the decimal system (0-9), but computers work differently:

| System | IT Usage | Life Science Example |
|--------|----------|---------------------|
| **Binary** | Internal data representation | Base calling in sequencing (A/T/C/G encoded as bits) |
| **Hexadecimal (hex)** | Compact binary notation | Viewing binary genomic files (BAM, BCF) |
| **Decimal** | Human-readable values | Read counts, gene expression levels |
| **Octal** | Unix file permissions | Controlling access to genomic databases |

### 1.2 Where You'll Encounter This

```bash
# File permissions in Unix (octal)
chmod 755 script.sh
chmod 644 variants.vcf

# MAC address (hex)
aa:bb:cc:dd:ee:ff

# IP address (decimal + binary under the hood)
192.168.1.1

# Colors in CSS (hex)
#FF5733

# UUID (hex)
550e8400-e29b-41d4-a716-446655440000
```

**Bioinformatics Examples:**

```bash
# FASTQ quality scores (Phred+33 ASCII encoding)
# Quality 40 = ASCII 73 (0x49 in hex)

# BAM file magic numbers (hex)
xxd -l 4 aligned.bam
# Output: 42 41 4d 01  (BAM\x01)

# Genomic coordinates (decimal but often hex in memory)
# chr1:12,345,678
```

---

## 2. Bits and Bytes

### 2.1 Bit

**Bit** is the smallest unit of information. Can have two values:

- `0` — logical zero, off, false
- `1` — logical one, on, true

Physically, a bit is implemented as:

- High/low voltage in circuits
- Magnetized/demagnetized area on disk
- Reflects/doesn't reflect light on CD
- Different fluorescence levels in DNA sequencing

```
One bit: 0 or 1
Two bits: 00, 01, 10, 11 (4 combinations)
Three bits: 000, 001, 010, 011, 100, 101, 110, 111 (8 combinations)
```

**Formula:** n bits = 2^n combinations

**Bioinformatics Application:**

DNA bases can be encoded in 2 bits:
```
A = 00
C = 01
G = 10
T = 11

Sequence "ACGT" = 00 01 10 11 (1 byte)
```

This is how compressed genomic formats store sequences efficiently!

### 2.2 Byte

**Byte** is a group of 8 bits. Standard unit for working with data.

```
1 byte = 8 bits
1 byte = 256 possible values (2^8)
1 byte = numbers from 0 to 255
```

**Example:**

```
Byte:        01001000
             ||||||||
Positions:   76543210
Weights:    128 64 32 16 8 4 2 1

Calculation: 0×128 + 1×64 + 0×32 + 0×16 + 1×8 + 0×4 + 0×2 + 0×1
          = 64 + 8
          = 72

72 in ASCII = letter 'H'
```

**FASTQ Quality Example:**

```
Quality byte: 01001001 = 73 in decimal
ASCII character: 'I'
Phred score: 73 - 33 = 40 (high quality base call)
```

### 2.3 Data Measurement Units

| Unit | Size | Example | Genomics Example |
|------|------|---------|------------------|
| 1 bit | 1 bit | Yes/No | One DNA base (2 bits used) |
| 1 byte (B) | 8 bits | One ASCII char | FASTQ quality score |
| 1 kilobyte (KB) | 1024 bytes | Short text | Small gene sequence |
| 1 megabyte (MB) | 1024 KB | Photo | Bacterial genome (E. coli ~4.6 MB) |
| 1 gigabyte (GB) | 1024 MB | Movie | Human genome FASTA (~3.2 GB) |
| 1 terabyte (TB) | 1024 GB | Large disk | Whole genome sequencing project |
| 1 petabyte (PB) | 1024 TB | Data center | NCBI SRA database (~50 PB) |

> **⚠️ Warning:**  
> Disk manufacturers use 1000 (SI), not 1024 (IEC):  
> 1 TB (manufacturer) = 1,000,000,000,000 bytes  
> 1 TiB (actual) = 1,099,511,627,776 bytes  
> So a "1 TB" disk shows as ~931 GiB in the system.

### 2.4 Nibble (Half-byte)

**Nibble** — 4 bits, half a byte. Convenient for hex representation.

```
1 nibble = 4 bits = 16 combinations (0-15)
1 byte = 2 nibbles

Byte:     01001000
          |    |
Nibbles:  0100 1000
           4    8

Hex:      0x48
```

---

## 3. Binary System

### 3.1 Basics

**Binary system** — base-2 numeral system. Uses only digits 0 and 1.

```
Decimal    Binary
   0         0
   1         1
   2         10
   3         11
   4         100
   5         101
   6         110
   7         111
   8         1000
   9         1001
   10        1010
```

### 3.2 Conversion: Decimal → Binary

**Division by 2 method:**

Convert 42 to binary:

```
42 ÷ 2 = 21, remainder 0  ↑
21 ÷ 2 = 10, remainder 1  |
10 ÷ 2 = 5,  remainder 0  | read bottom to top
5  ÷ 2 = 2,  remainder 1  |
2  ÷ 2 = 1,  remainder 0  |
1  ÷ 2 = 0,  remainder 1  ↓

Result: 101010
```

**Check in Python:**

```python
# Decimal → Binary
decimal = 42
print(bin(decimal))
```

**Output:**
```
0b101010
```

### 3.3 Conversion: Binary → Decimal

**Positional weight method:**

```
Binary:  1 0 1 0 1 0
         | | | | | |
Position:5 4 3 2 1 0
Weight: 32 16 8 4 2 1

1×32 + 0×16 + 1×8 + 0×4 + 1×2 + 0×1 = 32 + 8 + 2 = 42
```

**In Python:**

```python
# Binary → Decimal
binary_str = "101010"
print(int(binary_str, 2))
```

**Output:**
```
42
```

### 3.4 Binary Arithmetic

**Addition:**

```
    1 1   (carries)
  0 1 0 1  (5)
+ 0 0 1 1  (3)
─────────
  1 0 0 0  (8)
```

Rules:
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (0, carry 1)

---

## 4. Hexadecimal System

### 4.1 Basics

**Hex** — base-16 system. Uses digits 0-9 and letters A-F.

```
Decimal   Hex   Binary
   0       0     0000
   1       1     0001
   2       2     0010
   3       3     0011
   4       4     0100
   5       5     0101
   6       6     0110
   7       7     0111
   8       8     1000
   9       9     1001
   10      A     1010
   11      B     1011
   12      C     1100
   13      D     1101
   14      E     1110
   15      F     1111
```

### 4.2 Why Hex Is So Convenient

One hex digit = 4 bits (nibble). Two hex digits = 1 byte.

```
Byte in binary: 0100 1000
Byte in hex:      4    8   = 0x48

Compare:
Binary:  01001000 01100101 01101100 01101100 01101111
Hex:     48       65       6C       6C       6F
ASCII:   H        e        l        l        o
```

Hex is much more compact and easier for humans to read!

**Genomics Example:**

```bash
# BAM file header in hex
xxd -l 32 aligned.bam

00000000: 4241 4d01 3800 0000 4073 510a 4048 4409  BAM.8...@sQ.@HD.
00000010: 5644 3a31 2e36 0940 5351 0953 4e3a 636f  VD:1.6.@SQ.SN:co
```

Much easier to read than binary!

### 4.3 Hex Notations

```python
# Different ways to write hex
0x48       # Prefix 0x (most common)
0X48       # Same, but uppercase X
48h        # Suffix h (assembly language)
$48        # Prefix $ (some platforms)
\x48       # In strings (Python, C)
#48        # Colors in CSS (usually 6 digits)
```

### 4.4 Conversion: Hex ↔ Decimal

**Hex → Decimal:**

```
0x2A = 2×16¹ + 10×16⁰ = 32 + 10 = 42
0xFF = 15×16 + 15 = 240 + 15 = 255
0x100 = 1×256 + 0×16 + 0×1 = 256
```

**Python:**

```python
# Hex → Decimal
print(int("2A", 16))   # 42
print(int("FF", 16))   # 255
print(0xFF)            # 255

# Decimal → Hex
print(hex(42))         # 0x2a
print(hex(255))        # 0xff
```

**Output:**
```
42
255
255
0x2a
0xff
```

### 4.5 Practical Hex Examples

**RGB Colors:**

```
#FF5733
 || || ||
 RR GG BB

R = FF = 255 (maximum red)
G = 57 = 87  (some green)
B = 33 = 51  (little blue)

Result: orange-red color
```

**MAC Address:**

```
aa:bb:cc:dd:ee:ff

Each pair is a byte (0-255)
Total: 6 bytes = 48 bits
```

**Bytes in File:**

```bash
echo -n "Hi" | xxd
```

```
00000000: 4869                                     Hi
          ||
          4869 = 'H' (0x48=72) + 'i' (0x69=105)
```

**FASTQ Quality:**

```bash
# Quality character 'I' in hex
echo -n "I" | xxd
# Output: 49  (decimal 73, quality 40 after Phred+33 offset)
```

---

## 5. Octal System

### 5.1 Basics

**Octal** — base-8 system. Uses digits 0-7.

```
Decimal   Octal   Binary
   0        0      000
   1        1      001
   2        2      010
   3        3      011
   4        4      100
   5        5      101
   6        6      110
   7        7      111
   8       10     1000
```

### 5.2 Usage: Unix File Permissions

```bash
chmod 755 script.sh
chmod 644 data.vcf

7 = 111 (rwx) — owner: read, write, execute
5 = 101 (r-x) — group: read, execute
5 = 101 (r-x) — others: read, execute
```

**Permission Breakdown:**

```
rwxr-xr-x in binary: 111 101 101
                      7   5   5   in octal
```

```python
# Octal in Python
print(0o755)        # 493 in decimal
print(oct(493))     # '0o755'
```

**Output:**
```
493
0o755
```

**Bioinformatics Example:**

```bash
# Protect sensitive patient data
chmod 600 patient_variants.vcf  # Only owner can read/write
chmod 644 public_reference.fasta # Everyone can read
chmod 755 analysis_pipeline.sh  # Everyone can execute
```

---

## 6. Byte Order (Endianness)

### 6.1 Multi-byte Number Problem

Number 0x12345678 takes 4 bytes: 12, 34, 56, 78.

In what order should they be stored in memory?

### 6.2 Big-Endian vs Little-Endian

**Big-Endian (BE):** most significant byte first ("natural" order)

```
Number: 0x12345678
Address: 0x00  0x01  0x02  0x03
Byte:    0x12  0x34  0x56  0x78
         ↑
         Most significant byte (Big end) first
```

**Little-Endian (LE):** least significant byte first

```
Number: 0x12345678  
Address: 0x00  0x01  0x02  0x03
Byte:    0x78  0x56  0x34  0x12
         ↑
         Least significant byte (Little end) first
```

### 6.3 Where This Matters

| Architecture/Protocol | Endianness | Notes |
|----------------------|------------|-------|
| x86, x86-64 (Intel/AMD) | Little-Endian | Most PCs and servers |
| ARM (default) | Little-Endian | Mobile devices, Apple M1/M2 |
| Network protocols (TCP/IP) | Big-Endian | Internet standard |
| Java .class files | Big-Endian | JVM specification |
| JPEG, PNG, GIF | Big-Endian | Image formats |
| BMP | Little-Endian | Windows bitmap |
| BAM files | Little-Endian | Bioinformatics binary format |
| BCF files | Little-Endian | Binary VCF format |

### 6.4 Practical Example

```python
import struct

# Number 0x12345678
number = 0x12345678

# Pack in Big-Endian
be = struct.pack('>I', number)  # > = big-endian, I = unsigned int
print("Big-Endian:", be.hex())

# Pack in Little-Endian  
le = struct.pack('<I', number)  # < = little-endian
print("Little-Endian:", le.hex())
```

**Output:**
```
Big-Endian: 12345678
Little-Endian: 78563412
```

**Bioinformatics Impact:**

BAM files use Little-Endian for multi-byte integers. If you read them incorrectly:

```python
# Reading BAM reference ID (4 bytes)
bam_bytes = b'\x05\x00\x00\x00'  # Little-Endian

# Correct: Little-Endian
ref_id = int.from_bytes(bam_bytes, 'little')
print(f"Correct reference ID: {ref_id}")  # 5

# Wrong: Big-Endian
wrong_id = int.from_bytes(bam_bytes, 'big')
print(f"Wrong reference ID: {wrong_id}")  # 83886080 (garbage!)
```

### 6.5 Network Byte Order

Network protocols use Big-Endian (Network Byte Order).

```python
import socket

# Conversion between host and network byte order
host_int = 0x12345678

# Host → Network (for sending over network)
network_int = socket.htonl(host_int)
print(f"Host:    {host_int:#010x}")
print(f"Network: {network_int:#010x}")
```

**Output (on Little-Endian system):**
```
Host:    0x12345678
Network: 0x78563412
```

---

## 7. Command-Line Tools

### 7.1 xxd — hex dump

```bash
# Create test file
echo -n "Hello" > test.txt

# Hex dump
xxd test.txt
```

```
00000000: 4865 6c6c 6f                             Hello
```

**Output Breakdown:**

```
00000000: 4865 6c6c 6f                             Hello
    |      |                                        |
    |      |                                        ASCII
    |      Hex bytes (in groups of 2)
    Offset in hex
```

**xxd Options:**

```bash
# Show only first N bytes
xxd -l 16 file.bin

# Continuous hex (no spaces)
xxd -p file.bin

# Reverse conversion: hex → binary
echo "48656c6c6f" | xxd -r -p
# Output: Hello

# Show 1 byte per line
xxd -c 1 test.txt
```

**Bioinformatics Example:**

```bash
# Examine BAM file structure
xxd -l 64 aligned.bam

# Extract BAM magic number
xxd -l 4 -p aligned.bam
# Output: 42414d01 (BAM format signature)

# View gzipped FASTQ header
xxd -l 32 reads.fastq.gz
# Output shows gzip magic: 1f8b...
```

### 7.2 hexdump

```bash
hexdump -C test.txt
```

```
00000000  48 65 6c 6c 6f                                    |Hello|
00000005
```

### 7.3 od — octal dump

```bash
# Octal dump
od -c test.txt      # Characters
od -x test.txt      # Hex
od -d test.txt      # Decimal
```

### 7.4 Python for Conversions

```python
#!/usr/bin/env python3

# Conversion between systems
number = 42

print(f"Decimal: {number}")
print(f"Binary:  {bin(number)}")
print(f"Octal:   {oct(number)}")
print(f"Hex:     {hex(number)}")

# String → bytes
text = "Hello"
bytes_data = text.encode('utf-8')
print(f"\nText: {text}")
print(f"Bytes: {bytes_data}")
print(f"Hex: {bytes_data.hex()}")

# Hex string → bytes
hex_str = "48656c6c6f"
decoded = bytes.fromhex(hex_str).decode('utf-8')
print(f"\nHex: {hex_str}")
print(f"Decoded: {decoded}")
```

**Output:**
```
Decimal: 42
Binary:  0b101010
Octal:   0o52
Hex:     0x2a

Text: Hello
Bytes: b'Hello'
Hex: 48656c6c6f

Hex: 48656c6c6f
Decoded: Hello
```

**FASTQ Quality Example:**

```python
# Convert quality string to Phred scores
quality_string = "IIII"  # High quality
for char in quality_string:
    ascii_val = ord(char)
    phred_score = ascii_val - 33
    print(f"'{char}' = ASCII {ascii_val} (0x{ascii_val:02x}) = Phred {phred_score}")
```

**Output:**
```
'I' = ASCII 73 (0x49) = Phred 40
'I' = ASCII 73 (0x49) = Phred 40
'I' = ASCII 73 (0x49) = Phred 40
'I' = ASCII 73 (0x49) = Phred 40
```

### 7.5 Bash Conversions

```bash
# Decimal → Hex
printf "%x\n" 255
# ff

# Decimal → Octal
printf "%o\n" 255
# 377

# Hex → Decimal
echo $((16#ff))
# 255

# Octal → Decimal
echo $((8#755))
# 493

# Binary → Decimal
echo $((2#101010))
# 42
```

---

## 8. Representing Negative Numbers

### 8.1 Sign Bit

In signed integers, the most significant bit is the sign:

- 0 = positive number
- 1 = negative number

**Problem with sign-magnitude:** two zeros (+0 and -0)

### 8.2 Two's Complement

Modern computers use **two's complement**:

**For 8-bit number:**

```
+5 =  00000101

To get -5:
1. Invert bits:     11111010
2. Add 1:         + 00000001
                  ──────────
-5 =                11111011
```

**Signed Number Ranges:**

| Type | Size | Range |
|------|------|-------|
| int8 | 8 bits | -128 to 127 |
| int16 | 16 bits | -32,768 to 32,767 |
| int32 | 32 bits | -2,147,483,648 to 2,147,483,647 |

### 8.3 Check in Python

```python
import struct

# Unsigned byte
unsigned = struct.unpack('B', b'\xfb')[0]
print(f"Unsigned: {unsigned}")  # 251

# Signed byte
signed = struct.unpack('b', b'\xfb')[0]
print(f"Signed: {signed}")      # -5
```

**Output:**
```
Unsigned: 251
Signed: -5
```

---

## 9. Floating-Point Numbers

### 9.1 IEEE 754

Computers represent fractional numbers using IEEE 754 standard:

```
32-bit float: [1 bit sign][8 bit exponent][23 bit mantissa]
64-bit double: [1 bit sign][11 bit exponent][52 bit mantissa]
```

### 9.2 Why This Matters

```python
# Classic floating point problem
print(0.1 + 0.2)
```

**Output:**
```
0.30000000000000004
```

This is not a bug — it's a limitation of binary representation!

```python
# 0.1 in binary is an infinite fraction
# Like 1/3 = 0.333... in decimal

# For precise calculations, use Decimal
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))
```

**Output:**
```
0.3
```

**Bioinformatics Impact:**

```python
# Be careful with gene expression fold changes
fold_change = 2.0 / 3.0
print(f"Fold change: {fold_change}")  # 0.6666666666666666

# For precise p-values and statistical calculations
from decimal import Decimal, getcontext
getcontext().prec = 50  # 50 decimal places

pvalue = Decimal('0.05') / Decimal('3')
print(f"Precise p-value: {pvalue}")
```

---

## 10. Common Pitfalls

### 10.1 Prefix Confusion

❌ **Error:** Confusing hex and decimal

```python
# 10 is ten, 0x10 is sixteen!
print(10)     # 10
print(0x10)   # 16
```

### 10.2 Forgetting Endianness

❌ **Error:** Reading multi-byte numbers without considering byte order

```python
# Bytes from file (Little-Endian system)
bytes_data = b'\x78\x56\x34\x12'

# Wrong: interpret as Big-Endian
wrong = int.from_bytes(bytes_data, 'big')
print(f"Wrong: {wrong:#x}")  # 0x78563412

# Correct: use Little-Endian
correct = int.from_bytes(bytes_data, 'little')
print(f"Correct: {correct:#x}")  # 0x12345678
```

**BAM File Example:**

```python
# BAM uses Little-Endian
with open('aligned.bam', 'rb') as f:
    f.read(4)  # Skip magic
    text_len = int.from_bytes(f.read(4), 'little')  # Must use little!
```

### 10.3 Overflow

❌ **Error:** Not accounting for data type size

```python
# In Python numbers don't overflow
big = 2 ** 1000
print(f"Python handles big numbers: {len(str(big))} digits")

# But in C/other languages uint8_t overflow:
# 255 + 1 = 0 (not 256!)
```

### 10.4 Signed vs Unsigned

❌ **Error:** Confusing signed and unsigned types

```python
# Byte 0xFF
byte = b'\xff'

# As unsigned: 255
print(struct.unpack('B', byte)[0])  # 255

# As signed: -1
print(struct.unpack('b', byte)[0])  # -1
```

---

## 💡 Key Takeaways

- **Bit = 0 or 1, Byte = 8 bits**: Byte can store numbers 0-255 or one ASCII character. In genomics, 2 bits encode one DNA base.

- **Hex is human-friendly**: One hex digit = 4 bits. `0x48` is easier to read than `01001000`. Essential for viewing binary genomic files (BAM, BCF).

- **Octal for Unix permissions**: `chmod 755` is octal (7=111=rwx). Critical for protecting sensitive genomic and patient data.

- **Endianness matters**: x86 uses Little-Endian, network uses Big-Endian. BAM/BCF use Little-Endian. Mismatch corrupts data!

- **Floating point is imprecise**: `0.1 + 0.2 ≠ 0.3` is normal. For exact calculations (p-values, fold changes), use Decimal.

- **FASTQ quality uses Phred+33**: ASCII character minus 33 gives quality score. Understanding this requires hex/binary knowledge.

---

## 🚀 Next Steps

**Related Modules:**

- [Encodings](../03_Encodings/) — how numbers become characters (ASCII, UTF-8, Phred+33)
- [File Formats](../04_FileFormats/) — using hex to analyze file structures (BAM, VCF, FASTQ)

**Practice Ideas:**

1. Write a decimal ↔ binary ↔ hex converter in Python
2. Analyze a BAM file with `xxd` and find magic numbers
3. Create a file with number 0x12345678 and view it in Little-Endian and Big-Endian
4. Calculate Unix permissions for different rwx combinations
5. Convert FASTQ quality strings to Phred scores programmatically
6. Examine compressed FASTQ.GZ files and identify gzip magic numbers

**Going Deeper:**

- Study IEEE 754 in detail (special values: NaN, Infinity)
- Learn about fixed-point arithmetic
- Understand bitwise operations (AND, OR, XOR, shifts)
- Study how BAM CIGAR strings are encoded in binary
- Learn about BGZF (blocked gzip) used in genomics

**Connections to Other Courses:**

- **Python Course**: Module 03_Files covers binary file handling
- **Linux Course**: Module 04_Coreutils teaches tools like `od`, `xxd`, `hexdump`

---

## 📚 Additional Resources

**Tools:**

- [xxd manual](https://linux.die.net/man/1/xxd)
- [RapidTables Converter](https://www.rapidtables.com/convert/number/) — online converter
- [samtools](http://www.htslib.org/) — binary genomic file tools

**Articles:**

- [Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)
- [Endianness](https://en.wikipedia.org/wiki/Endianness)
- [FASTQ Format](https://en.wikipedia.org/wiki/FASTQ_format)
- [SAM/BAM Format Specification](https://samtools.github.io/hts-specs/SAMv1.pdf)

**Interactive:**

- [Float Exposed](https://float.exposed/) — IEEE 754 visualization
- [Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html)

**Bioinformatics:**

- [FASTQ Quality Scores](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm)
- [BAM Format](https://samtools.github.io/hts-specs/SAMv1.pdf) — uses Little-Endian
- [BCF Format](https://samtools.github.io/hts-specs/VCFv4.2.pdf) — binary VCF

---
