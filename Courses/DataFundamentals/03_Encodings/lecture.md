# Character Encodings
## ASCII, Unicode, UTF-8, and the Eternal Headache of Engineers

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand what bits and bytes are (module 02_NumberSystems)
- Know the basics of hexadecimal system
- Understand that computers only work with numbers

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Explain the history and evolution of character encodings
- Distinguish between ASCII, Unicode, UTF-8, UTF-16, and other encodings
- Use the `unicodedata` module to work with Unicode metadata
- Diagnose and fix encoding problems ("mojibake")
- Correctly work with encodings in command line and code
- Choose the correct encoding for different scenarios
- Protect patient data and genomic metadata from encoding corruption

---

## 1. Why Encodings Are Needed

### 1.1 The Problem

Computers only understand numbers. How do we store text?

```
Human sees:      Hello, world!
Computer stores: 48 65 6C 6C 6F 2C 20 77 6F 72 6C 64 21
```

**Encoding** is a mapping table between characters and numbers.

**Life Science Impact:**

```
Patient name:    Müller
Database stores: 4D C3 BC 6C 6C 65 72 (UTF-8)

But if opened as Latin-1:
Display shows:   MÃ¼ller (WRONG!)
```

This can lead to serious medical record errors!

### 1.2 Why This Is a Source of Problems

Before Unicode, each country created its own encodings:

```
Cyrillic "Я" encoded as:

- KOI-8:        0xD1 (209)
- Windows-1251: 0xDF (223)
- ISO-8859-5:   0xEF (239)
- MacCyrillic:  0x9F (159)
```

Same byte → different characters in different encodings!

**Bioinformatics Example:**

```
Sample ID with special characters:
"Sample_α-2023" (Greek alpha)

UTF-8:   53 61 6D 70 6C 65 5F CE B1 2D 32 30 32 33
Latin-1: Will corrupt the α character!
ASCII:   Cannot represent α at all!
```

### 1.3 "Mojibake" — The Classic Problem

```
Expected:  Привет, мир!
Got:       ÐŸÑ€Ð¸Ð²ÐµÑ‚, Ð¼Ð¸Ñ€!
```

Or:

```
Expected:  Müller
Got:       MÃ¼ller
```

Or:

```
Expected:  中文
Got:       ????
```

**Healthcare Impact:**

Patient names, drug names, and clinical notes with non-ASCII characters can be corrupted, leading to:
- Misidentification of patients
- Prescription errors
- Data loss in international collaborations

---

## 2. ASCII — The Beginning

### 2.1 History

**ASCII** (American Standard Code for Information Interchange) created in 1963.

7 bits → 128 characters (0-127):

- 0-31: Control characters (invisible)
- 32-126: Printable characters
- 127: DEL (delete)

### 2.2 ASCII Table

```
Printable characters:

Dec  Hex  Char
─────────────────
32   20   SPACE
33   21   !
34   22   "
...
47   2F   /

48   30   0
49   31   1
...
57   39   9

58   3A   :
...
64   40   @

65   41   A
66   42   B
...
90   5A   Z

97   61   a
98   62   b
...
122  7A   z
```

**Key Values:**

| Character | Dec | Hex | Description |
|-----------|-----|-----|-------------|
| NUL | 0 | 0x00 | Null, end of string in C |
| TAB | 9 | 0x09 | Horizontal tab |
| LF | 10 | 0x0A | Line Feed, newline (Unix) |
| CR | 13 | 0x0D | Carriage Return (part of Windows newline) |
| SPACE | 32 | 0x20 | Space |
| 0-9 | 48-57 | 0x30-0x39 | Digits |
| A-Z | 65-90 | 0x41-0x5A | Uppercase letters |
| a-z | 97-122 | 0x61-0x7A | Lowercase letters |
| DEL | 127 | 0x7F | Delete |

### 2.3 ASCII in Practice

```bash
# View ASCII code of character
printf "%d\n" "'A"
# 65

# Character from ASCII code
printf "\x41\n"
# A

# ASCII table
man ascii
```

```python
# Python: character ↔ code
print(ord('A'))     # 65
print(chr(65))      # A

# Check ASCII
text = "Hello"
print(text.isascii())  # True
print("Müller".isascii())  # False
```

**Output:**
```
65
A
True
False
```

**Bioinformatics Note:**

FASTA/FASTQ files traditionally use ASCII for sequence IDs and quality scores:

```
>NM_007294.3 Homo sapiens BRCA1
ATCGATCGATCG

Quality scores in FASTQ use ASCII 33-126 for Phred+33 encoding
```

### 2.4 ASCII Limitations

ASCII supports only:

- Latin letters (A-Z, a-z)
- Digits (0-9)
- Basic punctuation

**Does NOT support:**

- Cyrillic (Russian: Привет)
- Diacritics (é, ñ, ü, Müller)
- CJK ideographs (Chinese, Japanese, Korean: 中文)
- Emoji 😀
- Math symbols (√, ∑, ∞, α, β)
- Greek letters used in science (α, β, γ, δ)

---

## 3. Extended ASCII and Code Pages

### 3.1 The Idea

ASCII uses 7 bits (0-127). A byte has 8 bits!

Different countries used the remaining 128 values (128-255) differently.

### 3.2 Code Pages

**Western European:**

- ISO-8859-1 (Latin-1) — Western European languages
- Windows-1252 — Extension of Latin-1 for Windows

**Cyrillic:**

- KOI-8 (KOI8-R) — Soviet standard
- Windows-1251 (CP1251) — Windows for Russian
- ISO-8859-5 — ISO standard for Cyrillic
- CP866 (DOS) — DOS for Russian

**Greek:**

- ISO-8859-7 — Greek (important for scientific notation: α, β, γ)

### 3.3 KOI-8 (KOI8-R)

Soviet encoding. Feature: if you zero the high bit, Cyrillic transforms to similar Latin:

```
KOI-8: П = 0xD0
       0xD0 = 11010000
       AND  = 01111111
              01010000 = 0x50 = 'P'

Therefore: ПРИВЕТ → PRIVET when 8th bit is lost
```

### 3.4 Windows-1251

Most common encoding for Russian in Windows:

```
Char  Hex   Dec
────────────────
А     0xC0  192
Б     0xC1  193
В     0xC2  194
...
Я     0xDF  223

а     0xE0  224
б     0xE1  225
...
я     0xFF  255
```

### 3.5 Compatibility Problem

```
File in KOI8-R opened as Windows-1251:

Byte 0xD0 (KOI8-R: "П") → Windows-1251: "Р"
Byte 0xD2 (KOI8-R: "Р") → Windows-1251: "Т"

"ПРИВЕТ" → "ПТЙЧЕ|" (garbage!)
```

**Healthcare Example:**

```
Patient: Müller (stored in Latin-1: 4D FC 6C 6C 65 72)
If opened as UTF-8: M�ller (�  = replacement character)
```

---

## 4. Unicode — The Universal Character Table

### 4.1 The Unicode Idea

**Unicode** is a unified standard assigning a unique number to every character of all world languages.

As of 2024: **149,813** characters in Unicode 15.1

```
U+0041 = A (Latin capital A)
U+0410 = А (Cyrillic capital A)
U+03B1 = α (Greek small alpha)
U+4E2D = 中 (Chinese character "middle")
U+1F600 = 😀 (emoji)
```

### 4.2 Code Points

**Code point** — unique number of a character in Unicode.

Written as: `U+XXXX` or `U+XXXXX`

```
U+0000 — U+FFFF:   Basic Multilingual Plane (BMP)
U+10000 — U+10FFFF: Supplementary planes (emoji, rare characters)
```

### 4.3 Unicode Planes

| Plane | Range | Contents |
|-------|-------|----------|
| BMP (0) | U+0000-U+FFFF | Main languages, punctuation |
| SMP (1) | U+10000-U+1FFFF | Historical, musical, emoji |
| SIP (2) | U+20000-U+2FFFF | Rare CJK ideographs |
| ... | ... | ... |

### 4.4 Unicode Character Categories

Every Unicode character has a category:

| Category | Code | Examples |
|----------|------|----------|
| Letter, Uppercase | Lu | A, Б, Ω |
| Letter, Lowercase | Ll | a, б, ω |
| Letter, Other | Lo | 中, あ, ก |
| Number, Decimal Digit | Nd | 0-9, ٠-٩ |
| Punctuation | P* | . , ! ? |
| Symbol, Math | Sm | + − × ÷ ∑ ∫ |
| Symbol, Currency | Sc | $ € ¥ ₽ |
| Symbol, Other | So | ☀ ★ ♠ |
| Mark, Combining | M* | ́ ̈ ̃ (diacritics) |

**Scientific Notation:**

```python
import unicodedata

# Greek letters commonly used in science
for char in "αβγδεθλμπσφω":
    print(f"{char} (U+{ord(char):04X}): {unicodedata.name(char)}")
```

**Output:**
```
α (U+03B1): GREEK SMALL LETTER ALPHA
β (U+03B2): GREEK SMALL LETTER BETA
γ (U+03B3): GREEK SMALL LETTER GAMMA
...
```

### 4.5 Unicode Blocks

Characters in Unicode are grouped into blocks by language and purpose:

```
U+0000-U+007F    Basic Latin (ASCII)
U+0080-U+00FF    Latin-1 Supplement
U+0100-U+017F    Latin Extended-A
U+0370-U+03FF    Greek and Coptic (α, β, γ...)
U+0400-U+04FF    Cyrillic (Кириллица)
U+0500-U+052F    Cyrillic Supplement
U+2200-U+22FF    Mathematical Operators (∀, ∃, ∈, ∑, ∫)
U+4E00-U+9FFF    CJK Unified Ideographs (Chinese/Japanese/Korean)
U+1F600-U+1F64F  Emoticons
U+1F300-U+1F5FF  Miscellaneous Symbols and Pictographs
```

### 4.6 Unicode Is NOT an Encoding!

**Important:** Unicode defines WHAT characters exist and their numbers.

**Encoding** defines HOW to store these numbers in bytes:

- UTF-8
- UTF-16
- UTF-32

```
Character "A" (U+0041):

UTF-8:  41                (1 byte)
UTF-16: 00 41             (2 bytes)
UTF-32: 00 00 00 41       (4 bytes)
```

---

## 5. UTF-8 — The Modern Standard

### 5.1 What Is UTF-8

**UTF-8** (Unicode Transformation Format, 8-bit) is a variable-length encoding:

- ASCII characters (0-127): 1 byte
- Latin extended, Cyrillic, Greek: 2 bytes
- CJK, most symbols: 3 bytes
- Emoji, rare characters: 4 bytes

### 5.2 UTF-8 Structure

```
1 byte:  0xxxxxxx                        (0-127, ASCII compatible)
2 bytes: 110xxxxx 10xxxxxx               (128-2047)
3 bytes: 1110xxxx 10xxxxxx 10xxxxxx      (2048-65535)
4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx (65536-1114111)
```

### 5.3 Examples

**ASCII (1 byte):**

```
Character: A (U+0041)
Binary:    01000001
UTF-8:     41 (1 byte)
```

**Cyrillic (2 bytes):**

```
Character: П (U+041F)
Binary:    00000100 00011111
UTF-8:     D0 9F (2 bytes)

Breakdown:
110xxxxx 10xxxxxx
110 00010 10 011111
   (4)     (31)
= 4×64 + 31 = 256 + 31 = 287... wait, that's wrong calculation

Actually:
U+041F = 1055 decimal
1055 = 0000 0100 0001 1111 in binary (11 bits)
Split into: 00010 | 001111 (5 + 6 bits)
Template: 110xxxxx 10xxxxxx
Result:   11000100 10011111 = D0 9F
```

**Chinese (3 bytes):**

```
Character: 中 (U+4E2D)
UTF-8:     E4 B8 AD (3 bytes)
```

**Emoji (4 bytes):**

```
Character: 😀 (U+1F600)
UTF-8:     F0 9F 98 80 (4 bytes)
```

**Greek Alpha (2 bytes - Important for Science):**

```
Character: α (U+03B1)
UTF-8:     CE B1 (2 bytes)
```

### 5.4 Why UTF-8 Is Great

✅ **ASCII compatible:** First 128 characters identical to ASCII

✅ **Space efficient:** English text same size as ASCII

✅ **Self-synchronizing:** Can find character boundaries

✅ **No byte order issues:** No endianness problems

✅ **Wide support:** Internet standard, default in Linux/macOS

**Bioinformatics:**

Modern bioinformatics tools and databases use UTF-8:
- NCBI metadata
- UniProt annotations
- Sample descriptions with international characters
- Gene names with Greek letters (TNF-α, IL-1β)

### 5.5 UTF-8 in Practice

```bash
# Check file encoding
file -i sample_data.txt
# sample_data.txt: text/plain; charset=utf-8

# View bytes
echo "Hello α" | xxd
# 00000000: 4865 6c6c 6f20 ceb1 0a        Hello ..
#                     ^^^^^ (α in UTF-8: CE B1)
```

```python
# Encode string to UTF-8 bytes
text = "Hello α"
utf8_bytes = text.encode('utf-8')
print(utf8_bytes)
print(utf8_bytes.hex())

# Decode UTF-8 bytes back to string
decoded = utf8_bytes.decode('utf-8')
print(decoded)
```

**Output:**
```
b'Hello \xce\xb1'
48656c6c6f20ceb1
Hello α
```

---

## 6. UTF-16 and UTF-32

### 6.1 UTF-16

Uses 2 or 4 bytes:

- BMP characters (U+0000-U+FFFF): 2 bytes
- Characters beyond BMP: 4 bytes (surrogate pairs)

**Problem:** Endianness matters!

```
Character: A (U+0041)

UTF-16 BE (Big-Endian):  00 41
UTF-16 LE (Little-Endian): 41 00
```

**BOM (Byte Order Mark):**

```
UTF-16 BE starts with: FE FF
UTF-16 LE starts with: FF FE
```

### 6.2 UTF-32

Always 4 bytes per character:

```
Character: A (U+0041)
UTF-32: 00 00 00 41
```

**Advantages:**
- Fixed width: easy indexing
- Simple processing

**Disadvantages:**
- Wastes space: 4× size of ASCII text
- Still has endianness issues

### 6.3 When to Use What

| Encoding | Use Case |
|----------|----------|
| **UTF-8** | Internet, Linux, APIs, files, **bioinformatics** |
| UTF-16 | Windows internals, Java/C# strings |
| UTF-32 | Internal processing (rare) |

**Recommendation for Life Sciences:** Always use UTF-8 for:
- FASTA/FASTQ metadata
- Sample descriptions
- Patient records
- Gene annotations
- Data exchange

---

## 7. Working with Encodings in Command Line

### 7.1 Checking Encoding

```bash
# Check file encoding
file -i document.txt
# document.txt: text/plain; charset=utf-8

# Alternative: chardet (Python tool)
chardetect document.txt
# document.txt: utf-8 with confidence 0.99
```

### 7.2 Converting Encodings

```bash
# iconv: convert encoding
iconv -f WINDOWS-1251 -t UTF-8 input.txt > output.txt

# List available encodings
iconv -l

# Convert Latin-1 to UTF-8
iconv -f ISO-8859-1 -t UTF-8 old_data.txt > new_data.txt
```

**Bioinformatics Example:**

```bash
# Fix old sample metadata with Latin-1 encoding
iconv -f ISO-8859-1 -t UTF-8 sample_metadata_old.csv > sample_metadata_utf8.csv

# Verify
file -i sample_metadata_utf8.csv
# sample_metadata_utf8.csv: text/csv; charset=utf-8
```

### 7.3 Line Endings and Encodings

```bash
# Unix: LF (\n = 0x0A)
# Windows: CRLF (\r\n = 0x0D 0x0A)
# Old Mac: CR (\r = 0x0D)

# Convert Windows to Unix
dos2unix file.txt

# Convert Unix to Windows
unix2dos file.txt

# View line endings
cat -A file.txt
# $ shows LF, ^M shows CR
```

### 7.4 Locale Settings

```bash
# View current locale
locale

# Set locale for UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

---

## 8. Working with Encodings in Python

### 8.1 Opening Files with Correct Encoding

```python
# Default encoding (platform-dependent, often UTF-8 on Linux/Mac)
with open('file.txt') as f:
    content = f.read()

# Explicit UTF-8 (RECOMMENDED)
with open('file.txt', encoding='utf-8') as f:
    content = f.read()

# Reading Windows-1251
with open('old_russian.txt', encoding='windows-1251') as f:
    content = f.read()

# Writing UTF-8 (explicit)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Hello α β γ")
```

### 8.2 Encoding and Decoding

```python
# String → bytes (encoding)
text = "Hello α"
utf8_bytes = text.encode('utf-8')
print(utf8_bytes)  # b'Hello \xce\xb1'

# Bytes → string (decoding)
decoded = utf8_bytes.decode('utf-8')
print(decoded)  # Hello α

# Handling errors
text = "Hello α"
latin1_attempt = text.encode('latin-1', errors='replace')
print(latin1_attempt)  # b'Hello ?'

# Different error handling strategies
text.encode('ascii', errors='ignore')    # Skip non-ASCII
text.encode('ascii', errors='replace')   # Replace with ?
text.encode('ascii', errors='xmlcharrefreplace')  # &#945; for α
```

### 8.3 Detecting Encoding

```python
import chardet

# Detect encoding of bytes
with open('unknown.txt', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result)
    # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

# Use detected encoding
encoding = result['encoding']
text = raw_data.decode(encoding)
```

**Bioinformatics Example:**

```python
# Read FASTA file with proper encoding
def read_fasta_safe(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        sequences = {}
        current_id = None
        current_seq = []
        
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
        
        if current_id:
            sequences[current_id] = ''.join(current_seq)
    
    return sequences

# Handle metadata with special characters
def read_sample_metadata(filename):
    import pandas as pd
    # Always specify UTF-8 for modern data
    df = pd.read_csv(filename, encoding='utf-8')
    return df
```

### 8.4 Unicode Normalization

```python
import unicodedata

# Same visual character, different representations
text1 = "café"  # é as single character (U+00E9)
text2 = "café"  # é as e + combining accent (U+0065 + U+0301)

print(text1 == text2)  # False!
print(len(text1), len(text2))  # 4, 5

# Normalize to NFC (canonical composition)
norm1 = unicodedata.normalize('NFC', text1)
norm2 = unicodedata.normalize('NFC', text2)
print(norm1 == norm2)  # True!

# Different normalization forms:
# NFC: Canonical composition (recommended)
# NFD: Canonical decomposition
# NFKC: Compatibility composition
# NFKD: Compatibility decomposition
```

**Life Science Example:**

```python
# Normalize gene/protein names with special characters
def normalize_gene_name(name):
    # Convert to NFC form for consistent comparison
    return unicodedata.normalize('NFC', name)

gene1 = "TNF-α"  # α might be composed differently
gene2 = "TNF-α"
print(normalize_gene_name(gene1) == normalize_gene_name(gene2))
```

### 8.5 Working with Unicode Characters

```python
import unicodedata

# Get character name
char = 'α'
print(unicodedata.name(char))  
# GREEK SMALL LETTER ALPHA

# Get character category
print(unicodedata.category(char))  # Ll (lowercase letter)

# Lookup character by name
beta = unicodedata.lookup('GREEK SMALL LETTER BETA')
print(beta)  # β

# Get numeric value (for digits)
print(unicodedata.numeric('5'))  # 5.0
print(unicodedata.numeric('٥'))  # 5.0 (Arabic digit)
```

---

## 9. Diagnosing and Fixing Encoding Problems

### 9.1 Common Symptoms

**Symptom 1: Mojibake**

```
Expected:  Müller
Got:       MÃ¼ller
```

**Cause:** UTF-8 bytes interpreted as Latin-1

```python
# The problem
name = "Müller"
utf8_bytes = name.encode('utf-8')  # b'M\xc3\xbcller'
wrong = utf8_bytes.decode('latin-1')  # 'MÃ¼ller'
print(wrong)
```

**Fix:**

```python
# Detect double-encoding
corrupted = "MÃ¼ller"
# Re-encode as Latin-1 and decode as UTF-8
fixed = corrupted.encode('latin-1').decode('utf-8')
print(fixed)  # Müller
```

**Symptom 2: Replacement Characters**

```
Expected:  α-helix
Got:       �-helix
```

**Cause:** Character not in the target encoding

**Symptom 3: UnicodeDecodeError**

```python
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff
```

**Fix:**

```python
# Try with error handling
with open('file.txt', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Or detect encoding first
import chardet
with open('file.txt', 'rb') as f:
    raw = f.read()
    encoding = chardet.detect(raw)['encoding']

with open('file.txt', 'r', encoding=encoding) as f:
    content = f.read()
```

### 9.2 Diagnostic Tools

```python
def diagnose_encoding(filename):
    """Diagnose encoding issues in a file"""
    import chardet
    
    with open(filename, 'rb') as f:
        raw_data = f.read()
    
    # Detect encoding
    result = chardet.detect(raw_data)
    print(f"Detected: {result['encoding']} (confidence: {result['confidence']})")
    
    # Try common encodings
    encodings = ['utf-8', 'latin-1', 'windows-1252', 'windows-1251']
    for enc in encodings:
        try:
            text = raw_data.decode(enc)
            print(f"✓ {enc}: Successfully decoded")
            print(f"  Sample: {text[:50]}")
        except UnicodeDecodeError as e:
            print(f"✗ {enc}: Failed - {e}")

# Usage
diagnose_encoding('problematic_file.txt')
```

### 9.3 Fixing Corrupted Data

```python
def fix_mojibake(text):
    """Attempt to fix common mojibake patterns"""
    # UTF-8 decoded as Latin-1
    try:
        fixed = text.encode('latin-1').decode('utf-8')
        return fixed
    except:
        pass
    
    # Windows-1252 decoded as UTF-8
    try:
        fixed = text.encode('utf-8').decode('windows-1252')
        return fixed
    except:
        pass
    
    return text  # Cannot fix

# Example
corrupted = "MÃ¼ller"
print(fix_mojibake(corrupted))  # Müller
```

**Bioinformatics Pipeline:**

```python
def clean_sample_metadata(df):
    """Clean sample metadata from encoding issues"""
    import pandas as pd
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].apply(lambda x: fix_mojibake(str(x)) if pd.notna(x) else x)
    
    return df
```

---

## 10. Best Practices

### 10.1 Golden Rules

✅ **Always specify encoding explicitly**

```python
# Good
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Bad (relies on platform default)
with open('file.txt', 'r') as f:
    content = f.read()
```

✅ **Use UTF-8 by default**

Unless you have a specific reason, always use UTF-8:
- For new files
- For APIs
- For databases
- For bioinformatics metadata

✅ **Normalize Unicode when comparing**

```python
import unicodedata

def normalize_text(text):
    return unicodedata.normalize('NFC', text)

# Use for comparisons
if normalize_text(name1) == normalize_text(name2):
    print("Match!")
```

✅ **Handle errors gracefully**

```python
# Specify error handling
with open('file.txt', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
```

✅ **Validate input data**

```python
def is_valid_utf8(data):
    try:
        data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
```

### 10.2 File Operations Checklist

When working with text files:

1. Always specify encoding: `encoding='utf-8'`
2. Use `errors='replace'` or `errors='ignore'` for robustness
3. Normalize Unicode for comparisons
4. Test with international characters
5. Document encoding in README/documentation

### 10.3 Database Best Practices

```sql
-- PostgreSQL: Use UTF-8
CREATE DATABASE mydb
    ENCODING 'UTF8'
    LC_COLLATE 'en_US.UTF-8'
    LC_CTYPE 'en_US.UTF-8';

-- MySQL: Use utf8mb4 (full Unicode support)
CREATE DATABASE mydb
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```

```python
# Python SQLAlchemy
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://user:pass@localhost/mydb',
    connect_args={'options': '-c client_encoding=utf8'}
)
```

---

## 11. Special Characters and Their Problems

### 11.1 Whitespace Characters

```python
# Different types of spaces
space = " "        # U+0020 Regular space
nbsp = " "        # U+00A0 Non-breaking space
thin = " "        # U+2009 Thin space

# They look the same but aren't!
print(space == nbsp)  # False

# Strip all Unicode whitespace
text = "  hello  "
clean = text.strip()
```

### 11.2 Look-alike Characters

```python
# Cyrillic A vs Latin A
cyrillic_a = "А"  # U+0410
latin_a = "A"      # U+0041

print(cyrillic_a == latin_a)  # False!
print(cyrillic_a, latin_a)    # Look identical!

# This can cause security issues (homograph attacks)
```

**Bioinformatics Warning:**

```python
# Gene names can have look-alikes
gene1 = "IL1А"  # Last character is Cyrillic А
gene2 = "IL1A"  # Last character is Latin A

print(gene1 == gene2)  # False!
# Database queries might fail silently!
```

### 11.3 Zero-Width Characters

```python
# Invisible characters
zwsp = "​"  # U+200B Zero-width space
zwnj = "‌"  # U+200C Zero-width non-joiner

text = "Hello​World"  # Has zero-width space
print(len(text))  # 11, not 10!
```

### 11.4 Combining Characters

```python
# é can be represented two ways:
composed = "é"      # U+00E9 (single character)
decomposed = "é"    # U+0065 + U+0301 (e + combining acute)

print(len(composed))    # 1
print(len(decomposed))  # 2
print(composed == decomposed)  # False!

# Solution: normalize
import unicodedata
norm1 = unicodedata.normalize('NFC', composed)
norm2 = unicodedata.normalize('NFC', decomposed)
print(norm1 == norm2)  # True!
```

---

## 12. Common Pitfalls

### 12.1 Assuming ASCII

❌ **Bad:**

```python
# Fails for non-ASCII
text = "Müller"
text.upper()  # Works, but...
text.encode('ascii')  # UnicodeEncodeError!
```

✅ **Good:**

```python
text = "Müller"
text.encode('utf-8')  # b'M\xc3\xbcller'
```

### 12.2 Mixing Bytes and Strings

❌ **Bad:**

```python
# Python 3: strings are Unicode, not bytes!
text = "Hello"
binary = b"World"
text + binary  # TypeError!
```

✅ **Good:**

```python
text = "Hello"
binary = b"World"

# Decode bytes first
combined = text + " " + binary.decode('utf-8')
```

### 12.3 Forgetting to Normalize

❌ **Bad:**

```python
name1 = "café"  # é as U+00E9
name2 = "café"  # é as e + combining accent
print(name1 == name2)  # False!
```

✅ **Good:**

```python
import unicodedata
name1 = unicodedata.normalize('NFC', "café")
name2 = unicodedata.normalize('NFC', "café")
print(name1 == name2)  # True!
```

### 12.4 Platform-Dependent Defaults

❌ **Bad:**

```python
# Depends on platform locale
with open('file.txt') as f:
    content = f.read()
```

✅ **Good:**

```python
# Explicit encoding
with open('file.txt', encoding='utf-8') as f:
    content = f.read()
```

### 12.5 Ignoring Byte Order Mark (BOM)

```python
# UTF-8 with BOM (EF BB BF at start)
with open('file.txt', 'r', encoding='utf-8-sig') as f:
    content = f.read()  # BOM automatically stripped
```

---

## 13. Encoding Summary Table

| Encoding | Bytes/Char | ASCII Compatible | Use Case |
|----------|------------|------------------|----------|
| **ASCII** | 1 | Yes (by definition) | English only, legacy |
| **ISO-8859-1 (Latin-1)** | 1 | Yes | Western European, legacy |
| **Windows-1252** | 1 | Yes | Windows Western Europe |
| **Windows-1251** | 1 | Yes | Windows Russian/Cyrillic |
| **KOI8-R** | 1 | Yes | Unix Russian/Cyrillic |
| **UTF-8** | 1-4 | Yes | **Modern standard, recommended** |
| **UTF-16** | 2-4 | No | Windows internals, Java |
| **UTF-32** | 4 | No | Internal processing (rare) |

### Language Coverage

| Language | ASCII | Latin-1 | UTF-8 |
|----------|-------|---------|-------|
| English | ✅ | ✅ | ✅ |
| German (ü, ä, ö) | ❌ | ✅ | ✅ |
| French (é, è, ç) | ❌ | ✅ | ✅ |
| Russian (Кириллица) | ❌ | ❌ | ✅ |
| Chinese (中文) | ❌ | ❌ | ✅ |
| Greek (α, β, γ) | ❌ | ❌ | ✅ |
| Emoji (😀) | ❌ | ❌ | ✅ |

---

## 💡 Key Takeaways

- **Encoding is the mapping between characters and bytes.** Computers only understand numbers; encodings tell them which number represents which character.

- **ASCII (7-bit, 128 characters) is the foundation** but only supports English. All modern encodings are ASCII-compatible in the first 128 positions.

- **UTF-8 is the modern standard.** Variable length (1-4 bytes), ASCII compatible, no byte order issues. Use it for everything: files, APIs, databases, bioinformatics metadata.

- **Unicode ≠ Encoding.** Unicode defines characters and their numbers (code points). UTF-8/UTF-16/UTF-32 are encodings that specify how to store those numbers in bytes.

- **Always specify encoding explicitly** in code: `open(file, encoding='utf-8')`. Never rely on platform defaults.

- **Mojibake happens when bytes are decoded with wrong encoding.** UTF-8 bytes interpreted as Latin-1 produces: Müller → MÃ¼ller.

- **Normalize Unicode for comparisons.** Use `unicodedata.normalize('NFC', text)` because "é" can be one character or e + combining accent.

- **Critical for healthcare and international collaboration.** Patient names (Müller, 李明), drug names, and sample IDs with special characters must be handled correctly to prevent data corruption and medical errors.

- **Bioinformatics best practices:** Use UTF-8 for FASTA/FASTQ metadata, sample descriptions, gene annotations. Greek letters (α, β, γ) in gene names require proper Unicode support.

---

## 🚀 Next Steps

**Related Modules:**

- [File Formats](../04_FileFormats/) — Different file formats handle encodings differently
- [Tabular Data](../09_TabularData/) — CSV encoding issues and solutions

**Practice Ideas:**

1. Create files with different encodings and convert between them
2. Write a script to detect and fix mojibake in a directory of files
3. Build a tool to validate UTF-8 in bioinformatics metadata files
4. Test your pipeline with patient names: Müller, Hernández, Łukasiewicz, 李明
5. Create a FASTA file with Greek letters in descriptions (α-helix, β-sheet)
6. Fix encoding issues in legacy CSV files with international characters

**Going Deeper:**

- Study Unicode normalization forms (NFC, NFD, NFKC, NFKD) in detail
- Learn about bidirectional text (Arabic, Hebrew)
- Understand combining characters and grapheme clusters
- Explore homograph attacks using look-alike characters
- Study encoding in different programming languages (Java uses UTF-16 internally)

**Connections to Other Courses:**

- **Python Course**: Module 03_Files covers file encoding handling in detail
- **Linux Course**: Module 06_Structured_Data teaches CLI tools for handling UTF-8 data

---

## 📚 Additional Resources

**Essential Reading:**

- [The Absolute Minimum Every Software Developer Must Know About Unicode](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) by Joel Spolsky
- [UTF-8 Everywhere Manifesto](http://utf8everywhere.org/)

**Standards:**

- [Unicode Standard](https://www.unicode.org/standard/standard.html)
- [UTF-8 RFC 3629](https://tools.ietf.org/html/rfc3629)
- [Character Model for the World Wide Web](https://www.w3.org/TR/charmod/)

**Tools:**

- [Unicode Character Search](https://unicode-table.com/)
- [Online Unicode Converter](https://onlineunicodetools.com/)
- [ftfy - Python library to fix encoding errors](https://github.com/rspeer/python-ftfy)

**Python Documentation:**

- [Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
- [codecs module](https://docs.python.org/3/library/codecs.html)
- [unicodedata module](https://docs.python.org/3/library/unicodedata.html)

**Testing:**

- [The Quick Brown Fox Jumps Over The Lazy Dog](https://en.wikipedia.org/wiki/Pangram) — English pangram
- ["Съешь ещё этих мягких французских булок, да выпей же чаю"](https://ru.wikipedia.org/wiki/Панграмма) — Russian pangram
- International test strings for validation

**Bioinformatics:**

- [NCBI Data Standards](https://www.ncbi.nlm.nih.gov/genbank/samplesubmit/) — Character encoding requirements
- [UniProt Character Set](https://www.uniprot.org/help/character_set) — UTF-8 usage in protein databases
- [ISO 15924](https://unicode.org/iso15924/) — Codes for the representation of names of scripts

---
