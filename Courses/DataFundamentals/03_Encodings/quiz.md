# Character Encodings - Quiz

Test your knowledge on "Character Encodings: ASCII, Unicode, UTF-8, unicodedata, and encoding comparisons".

---

## Question 1: What is an Encoding

What is character encoding?

A) A text file compression format

B) A mapping table between characters and numbers

C) A method of text encryption

D) A data transmission protocol

---

## Question 2: ASCII

How many characters does the ASCII standard define?

A) 64

B) 256

C) 512

D) 128

---

## Question 3: ASCII Code

What is the ASCII code for the character 'A' (uppercase Latin)?

A) 0

B) 65

C) 97

D) 41

---

## Question 4: ASCII Limitations

Which characters are NOT supported by ASCII?

A) Cyrillic

B) Latin letters A-Z

C) Digits 0-9

D) Punctuation marks

---

## Question 5: Unicode vs Encoding

Which of the following is true about Unicode?

A) Unicode only defines character numbers, not storage method

B) Unicode is an encoding, like UTF-8

C) Unicode only supports 65536 characters

D) Unicode is not compatible with ASCII

---

## Question 6: Code Point

How is the code point of character 'A' (U+0041) written?

A) #0041

B) \u0041

C) U+0041

D) 0x0041

---

## Question 7: UTF-8 Compatibility

Why is UTF-8 compatible with ASCII?

A) The first 128 characters of UTF-8 are encoded as one byte with the same value

B) They are different encodings, not compatible

C) UTF-8 automatically converts ASCII

D) UTF-8 uses the same 7 bits for ASCII

---

## Question 8: UTF-8 Size

How many bytes can one character occupy in UTF-8?

A) Always 2 bytes

B) Always 1 byte

C) From 1 to 4 bytes

D) Always 4 bytes

---

## Question 9: Cyrillic in UTF-8

How many bytes does one Cyrillic letter occupy in UTF-8?

A) 3 bytes

B) 2 bytes

C) 1 byte

D) 4 bytes

---

## Question 10: Emoji in UTF-8

How many bytes does an emoji (e.g., 😀) occupy in UTF-8?

A) 3 bytes

B) 2 bytes

C) 4 bytes

D) 1 byte

---

## Question 11: Mojibake

What is "mojibake"?

A) Special control characters

B) An error in the Unicode standard

C) The result of opening a file with the wrong encoding

D) A virus in text files

---

## Question 12: Mojibake Example

If the text "Привет" displays as "ÐŸÑ€Ð¸Ð²ÐµÑ‚", what happened?

A) The font doesn't support Cyrillic

B) The file is corrupted

C) UTF-8 text opened as Latin-1 or Windows-1252

D) The text is encrypted

---

## Question 13: iconv Command

Which command converts a file from Windows-1251 to UTF-8?

A) iconv -f WINDOWS-1251 -t UTF-8 file.txt

B) encode -from cp1251 -to utf8 file.txt

C) convert -e utf8 file.txt

D) recode cp1251 utf8 file.txt

---

## Question 14: BOM

What is BOM (Byte Order Mark)?

A) File checksum

B) Compression format

C) Special bytes at the beginning of a file indicating encoding and byte order

D) End-of-file marker

---

## Question 15: UTF-8 BOM

What bytes represent the BOM for UTF-8?

A) EF BB BF

B) 00 00 FE FF

C) FF FE

D) FE FF

---

## Question 16: Python Encoding

How do you correctly open a UTF-8 file in Python?

A) open('file.txt', mode='utf8')

B) open('file.txt')

C) open('file.txt').read().encode('utf-8')

D) open('file.txt', encoding='utf-8')

---

## Question 17: MySQL and UTF-8

Why should you use `utf8mb4` instead of `utf8` in MySQL?

A) utf8mb4 is an outdated version

B) utf8mb4 is faster

C) utf8 in MySQL supports maximum 3 bytes per character, not including emoji

D) utf8mb4 takes less space

---

## Question 18: KOI-8

What is a special feature of the KOI-8 encoding?

A) Supports Chinese ideographs

B) It's a 16-bit encoding

C) When the 8th bit is lost, Cyrillic transforms to similar Latin

D) Only used in Windows

---

## Question 19: Encoding Detection

Which Python tool is used to automatically detect file encoding?

A) unicodedetect

B) encodings

C) chardet

D) codecer

---

## Question 20: Unicode Normalization

Why is Unicode normalization (NFC, NFD) needed?

A) To bring different representations of the same character to a unified form

B) To compress text

C) To convert to ASCII

D) To sort strings

---

## Question 21: unicodedata.name()

What does the function `unicodedata.name('€')` return?

A) Character code in hex

B) Character category

C) UTF-8 bytes

D) Official Unicode character name (EURO SIGN)

---

## Question 22: unicodedata.category()

What is the Unicode category of the uppercase letter 'A'?

A) Ll (Letter, lowercase)

B) Lu (Letter, uppercase)

C) Nd (Number, decimal digit)

D) Lo (Letter, other)

---

## Question 23: unicodedata.lookup()

How do you get the character ☃ (snowman) by its name in Python?

A) chr('SNOWMAN')

B) unicode.get('SNOWMAN')

C) ord('SNOWMAN')

D) unicodedata.lookup('SNOWMAN')

---

## Question 24: Unicode Blocks

In which Unicode range are Cyrillic characters located?

A) U+0000-U+007F

B) U+0400-U+04FF

C) U+4E00-U+9FFF

D) U+1F600-U+1F64F

---

## Question 25: Modern Web

What encoding is used on ~98% of modern websites?

A) Windows-1252

B) ISO-8859-1

C) UTF-16

D) UTF-8

---

## Question 26: Windows-1251 vs KOI8-R

How does Windows-1251 differ from KOI8-R?

A) Windows-1251 is 16-bit, KOI8-R is 8-bit

B) Different placement of Cyrillic characters in bytes 128-255

C) KOI8-R supports emoji, Windows-1251 doesn't

D) Windows-1251 is a Unicode encoding, KOI8-R isn't

---

## Question 27: UTF-16 and Endianness

What problem does UTF-16 have that UTF-8 doesn't?

A) Dependence on byte order (endianness)

B) Doesn't support ASCII

C) Fixed character length

D) Doesn't support emoji

---

## Question 28: GB18030

In which country is the GB18030 encoding a mandatory government standard?

A) Japan

B) China

C) Russia

D) Korea

---

## Question 29: unicodedata.numeric()

What will `unicodedata.numeric('½')` return?

A) Error (ValueError)

B) String "1/2"

C) Integer 1

D) 0.5

---

## Question 30: Removing Diacritics

Which normalization method is used to remove diacritical marks (accents)?

A) NFC (Composed)

B) NFD (Decomposed) + filtering category Mn

C) NFKD (Compatibility Decomposed)

D) ASCII transliteration

---

## Question 31: Patient Name Encoding

A patient named "Müller" is stored in a database. Which encoding should you use to avoid corruption?

A) ASCII

B) Latin-1 (ISO-8859-1)

C) UTF-8

D) Windows-1252

---

## Question 32: Greek Letters in Science

Gene name "TNF-α" contains Greek letter alpha. Which encoding correctly handles this?

A) ASCII

B) Latin-1

C) UTF-8

D) Windows-1251

---

## Question 33: FASTA Metadata

A FASTA file has sequence descriptions with international characters. What encoding should be used?

A) ASCII only (standard requirement)

B) UTF-8 (modern standard)

C) Platform default

D) Latin-1

---

## Question 34: Sample ID Corruption

Sample ID "α-helix-2023" displays as "�-helix-2023". What's the problem?

A) File is corrupted

B) Character not supported in the encoding used

C) Font issue

D) Database error

---

## Question 35: International Collaboration

You're sharing genomic data with researchers in China, Russia, and Germany. Which encoding ensures all names display correctly?

A) ASCII

B) UTF-8

C) Latin-1

D) Windows-1252

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Encoding is a mapping table between characters and their numeric representations. |
| 2 | D | ASCII is 7 bits, 128 characters (0-127). |
| 3 | A | 'A' = 65 (0x41). Lowercase 'a' = 97 (0x61). |
| 4 | A | ASCII only supports Latin and basic symbols, not Cyrillic. |
| 5 | B | Unicode is a character table. UTF-8/16/32 are ways to encode Unicode in bytes. |
| 6 | C | Code points are written as U+XXXX, e.g., U+0041 for 'A'. |
| 7 | A | First 128 characters of UTF-8 are identical to ASCII — one byte, same value. |
| 8 | A | UTF-8: 1 byte (ASCII), 2 bytes (Cyrillic), 3 bytes (CJK), 4 bytes (emoji). |
| 9 | B | Cyrillic (U+0400-U+04FF) is encoded in 2 bytes in UTF-8. |
| 10 | C | Emoji (U+1F600+) are beyond BMP and require 4 bytes in UTF-8. |
| 11 | B | Mojibake is corrupted text when encoding used for writing doesn't match encoding used for reading. |
| 12 | D | UTF-8 bytes interpreted as Latin-1 give characteristic "ÐŸÑ€Ð¸..." |
| 13 | C | `iconv` with -f (from) and -t (to) flags converts encodings. |
| 14 | C | BOM is bytes at the beginning of a file to identify encoding and endianness. |
| 15 | A | UTF-8 BOM = `EF BB BF`. `FF FE` = UTF-16 LE, `FE FF` = UTF-16 BE. |
| 16 | D | Always explicitly specify `encoding='utf-8'` when opening files. |
| 17 | D | MySQL `utf8` = max 3 bytes, doesn't support characters beyond BMP (emoji). |
| 18 | B | In KOI-8, Russian letters are positioned so that zeroing the 8th bit gives similar Latin. |
| 19 | C | `chardet` is a library for automatic encoding detection. |
| 20 | A | One character can have different Unicode representations; normalization brings them to unified form. |
| 21 | D | `unicodedata.name()` returns the official Unicode character name. |
| 22 | A | Lu = Letter, uppercase. Ll = lowercase, Nd = digit, Lo = other letter. |
| 23 | D | `unicodedata.lookup('SNOWMAN')` returns character by its Unicode name. |
| 24 | A | Cyrillic is in block U+0400-U+04FF. U+0000-U+007F = ASCII, U+4E00+ = CJK. |
| 25 | D | UTF-8 is used on ~98% of websites, it's the de facto web standard. |
| 26 | B | Both encodings are 8-bit, but characters are placed differently in upper 128 bytes. |
| 27 | A | UTF-16 depends on byte order (BE/LE), so BOM is needed. UTF-8 doesn't depend. |
| 28 | B | GB18030 is a mandatory standard in China, covering all Unicode characters. |
| 29 | D | `unicodedata.numeric('½')` returns 0.5 — numeric value of the fraction. |
| 30 | B | NFD splits character into base + combining mark, then filter category Mn. |
| 31 | C | UTF-8 correctly handles all Latin characters with diacritics. Latin-1 works but UTF-8 is modern standard. |
| 32 | C | UTF-8 is the only encoding listed that supports Greek letters (U+0370-U+03FF). |
| 33 | B | Modern bioinformatics uses UTF-8 for all metadata to support international characters. |
| 34 | B | The � (replacement character) appears when a character cannot be represented in the encoding. |
| 35 | B | UTF-8 supports all languages and is the international standard for data exchange. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **32-35 correct (91-100%)** | 🏆 Excellent! | Outstanding understanding of encodings and Unicode! Move to File Formats module. |
| **27-31 correct (77-88%)** | ✅ Very Good | Great work! Review unicodedata and encoding comparisons. |
| **21-26 correct (60-74%)** | ⚠️ Good | Re-read sections on UTF-8, mojibake, and unicodedata. |
| **15-20 correct (43-57%)** | 📚 Needs Review | Carefully re-read the lecture and practice with examples. |
| **Less than 15 correct (<43%)** | 🔄 Study Again | Start from the beginning, focus on understanding core concepts. |

---

## Next Steps

### If you scored 80% or higher:
- Move to [Module 04: File Formats](../04_FileFormats/)
- Practice with real bioinformatics files containing special characters
- Test encoding handling in your analysis pipelines
- Try the Python Course (Module 03_Files for encoding in practice)

### If you scored 50-79%:
- Review lecture sections on UTF-8 structure and mojibake
- Practice with `iconv` and `chardet` tools
- Work through Python encoding examples
- Test with patient names: Müller, Hernández, Łukasiewicz, 李明

### If you scored below 50%:
- Re-read the lecture step by step
- Focus on understanding why encodings exist
- Practice converting between encodings manually
- Use online tools to visualize encoding differences

---

## Practice Exercises

To solidify your understanding:

1. **Encoding Detection**: Write a script to detect and report encoding of all files in a directory
2. **Mojibake Fixer**: Create a tool to automatically fix common mojibake patterns
3. **FASTA Validator**: Build a validator that checks FASTA files for encoding issues
4. **Patient Name Handler**: Write functions to safely store/retrieve international patient names
5. **Gene Name Normalizer**: Create a tool to normalize gene names with Greek letters (α, β, γ)
6. **Metadata Cleaner**: Build a pipeline to clean sample metadata from encoding corruption
7. **Unicode Explorer**: Create a tool to explore Unicode properties of characters in your data

---

## Bioinformatics Applications

### Sample Metadata Validation
```python
import chardet
import pandas as pd

def validate_metadata_encoding(csv_file):
    """Validate that metadata file is properly UTF-8 encoded"""
    with open(csv_file, 'rb') as f:
        result = chardet.detect(f.read())
    
    if result['encoding'].lower() != 'utf-8':
        print(f"Warning: File is {result['encoding']}, should be UTF-8")
        return False
    return True

# Usage
validate_metadata_encoding('sample_info.csv')
```

### Gene Name Normalization
```python
import unicodedata

def normalize_gene_name(name):
    """Normalize gene names with Greek letters"""
    # Convert to NFC form for consistent comparison
    normalized = unicodedata.normalize('NFC', name)
    return normalized

# Test with TNF-α
gene1 = "TNF-α"  # α might be composed differently
gene2 = "TNF-α"
print(normalize_gene_name(gene1) == normalize_gene_name(gene2))
```

### FASTA Encoding Check
```python
def check_fasta_encoding(fasta_file):
    """Check if FASTA file has encoding issues"""
    try:
        with open(fasta_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                # Check for replacement characters
                if '�' in line:
                    print(f"Line {i}: Found replacement character (encoding issue)")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")

# Usage
check_fasta_encoding('sequences.fasta')
```

---
