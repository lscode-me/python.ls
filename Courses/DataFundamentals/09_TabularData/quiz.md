# Tabular Data - Quiz

Test your knowledge on "Tabular Data: CSV, TSV" with a bioinformatics focus.

---

## Question 1: CSV Acronym

What does CSV stand for?

A) Character Separated Values

B) Comma-Separated Values

C) Common Separated Values

D) Column Sorted Values

---

## Question 2: CSV Delimiter

What delimiter is used by default in CSV?

A) Comma

B) Space

C) Tab

D) Semicolon

---

## Question 3: TSV Delimiter

What delimiter is used in TSV?

A) Comma

B) Tab

C) Pipe

D) Semicolon

---

## Question 4: Quotes in CSV

How do you write the value "Hello, World" in CSV?

A) `Hello\, World`

B) `Hello, World`

C) `'Hello, World'`

D) "Hello, World"

---

## Question 5: Quotes Inside Values

How do you write a value with the word "test" (in quotes) in CSV?

A) "He said ""test"""

B) `He said \"test\"`

C) `"He said 'test'"`

D) `"He said "test""`

---

## Question 6: Python csv Module

Which class reads CSV as dictionaries?

A) csv.DictReader

B) `csv.MapReader`

C) `csv.reader`

D) `csv.DictParser`

---

## Question 7: newline Parameter

Why is `newline=''` important when opening CSV in Python?

A) For file compression

B) For faster reading

C) For correct handling of line breaks

D) For Unicode support

---

## Question 8: csvkit Tool

Which csvkit tool pretty-prints CSV in terminal?

A) `csvdisplay`

B) csvlook

C) `csvprint`

D) `csvshow`

---

## Question 9: European CSV

What delimiter is often used in European CSV files?

A) Comma

B) Slash

C) Colon

D) Semicolon

---

## Question 10: pandas Reading

Which pandas function reads CSV?

A) `pd.load_csv()`

B) pd.read_csv()

C) `pd.open_csv()`

D) `pd.csv_read()`

---

## Question 11: CSV Encoding

What encoding is recommended for CSV?

A) ASCII

B) UTF-16

C) Latin-1

D) UTF-8

---

## Question 12: csvgrep

What does the command `csvgrep -c name -m Alice data.csv` do?

A) Filters rows where name column contains Alice

B) Deletes rows with Alice

C) Replaces Alice with another value

D) Sorts by name column

---

## Question 13: csv.writer

Which method writes multiple rows to CSV?

A) writer.writerows(rows)

B) `writer.dump(rows)`

C) `writer.write(rows)`

D) `writer.writeall(rows)`

---

## Question 14: CSV Header

How do you get the CSV header when reading in Python?

A) `reader.columns`

B) `reader.header()`

C) next(reader)

D) `reader[0]`

---

## Question 15: csvsql

What does csvsql allow you to do?

A) Execute SQL queries on CSV file

B) All of the above

C) Convert CSV to SQL file

D) Import CSV into database

---

## Question 16: csvstat

What does the csvstat command do?

A) Sorts CSV

B) Displays CSV as table

C) Outputs statistics per column (min, max, mean)

D) Converts to JSON

---

## Question 17: awk Sum

What does `awk -F, 'NR>1 {sum+=$2} END {print sum}' data.csv` do?

A) Counts rows

B) Sorts by second column

C) Sums values of second column (without header)

D) Outputs second column

---

## Question 18: BOM

What is BOM in the context of CSV files?

A) Column delimiter

B) Byte Order Mark — marker at file beginning

C) Date format

D) Compression type

---

## Question 19: csv.DictWriter

Which csv.DictWriter method writes the header?

A) writer.columns()

B) writer.writeheader()

C) writer.header()

D) writer.writerow()

---

## Question 20: csvjson

What does the csvjson command do?

A) Validates CSV

B) Executes SQL queries

C) Converts JSON to CSV

D) Converts CSV to JSON

---

## Question 21: 🧬 BED Format

BED (Browser Extensible Data) format uses which delimiter?

A) Comma

B) Tab

C) Space

D) Semicolon

---

## Question 22: 🧬 GFF Format

GFF (General Feature Format) for gene annotations is:

A) Comma-separated

B) Tab-separated with 9 columns

C) XML-based

D) JSON-based

---

## Question 23: 🧬 Gene Expression CSV

You have DESeq2 results in CSV. How do you filter significant genes (padj < 0.05)?

A) `csvgrep -c padj -r '<0.05' results.csv`

B) `csvsql --query "SELECT * FROM results WHERE padj < 0.05" results.csv`

C) `csvcut -c padj results.csv`

D) `csvlook results.csv`

---

## Question 24: 🧬 VCF to CSV

VCF (Variant Call Format) files are:

A) Always CSV

B) Tab-separated with header lines starting with ##

C) JSON format

D) XML format

---

## Question 25: 🧬 Sample Metadata

Which format is best for sample metadata with mixed data types?

A) Plain text

B) CSV with clear column headers

C) Binary format

D) XML

---

## Question 26: 🧬 Gene Count Matrix

You have a gene count matrix from RNA-Seq. Which tool is best for filtering?

A) Excel only

B) pandas in Python

C) Text editor

D) grep

---

## Question 27: 🧬 Variant Quality Filter

Given variants.csv with quality scores, how do you filter quality > 30?

```bash
awk -F, 'NR>1 && $3 > 30' variants.csv
```

What does `NR>1` do?

A) Filters first row

B) Skips header row

C) Counts rows

D) Sorts rows

---

## Question 28: 🧬 Coverage Analysis

You calculate average coverage per sample. Which pandas method?

A) `df.mean()`

B) `df.groupby('sample_id')['coverage'].mean()`

C) `df['coverage'].avg()`

D) `df.average('coverage')`

---

## Question 29: 🧬 Missing Data

In bioinformatics CSV, what's the best way to represent missing data?

A) Empty string ""

B) "NA" or "." (documented convention)

C) 0

D) Random value

---

## Question 30: 🧬 csvjoin for Analysis

You have samples.csv and results.csv, both with sample_id. How to merge?

A) `csvjoin -c sample_id samples.csv results.csv`

B) `csvmerge samples.csv results.csv`

C) `csvcat samples.csv results.csv`

D) `csvcombine samples.csv results.csv`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Comma-Separated Values — values separated by commas. |
| 2 | A | By default, CSV uses comma as delimiter. |
| 3 | B | TSV (Tab-Separated Values) uses tab character. |
| 4 | D | Values with comma are enclosed in double quotes. |
| 5 | A | Quotes inside value are doubled: `""`. |
| 6 | A | `csv.DictReader` returns rows as dictionaries with keys from header. |
| 7 | C | `newline=''` prevents issues with line breaks on different OS. |
| 8 | B | `csvlook` formats CSV as table in terminal. |
| 9 | D | In European countries, comma is decimal separator, so CSV uses `;`. |
| 10 | B | `pd.read_csv()` — main pandas function for reading CSV. |
| 11 | D | UTF-8 — recommended encoding for compatibility. |
| 12 | A | `csvgrep -c column -m match` filters rows by value in column. |
| 13 | A | `writerows()` writes a list of lists (multiple rows). |
| 14 | C | `next(reader)` returns first row (usually header). |
| 15 | C | csvsql can execute SQL queries, convert and import to DB. |
| 16 | C | csvstat outputs statistics: min, max, mean, std, etc. |
| 17 | C | NR>1 skips header, sum+=$2 sums second column. |
| 18 | B | BOM (Byte Order Mark) — special bytes at start of UTF-8/UTF-16 files. |
| 19 | B | writeheader() writes row with column names from fieldnames. |
| 20 | D | csvjson converts CSV file to JSON format. |
| 21 | B | 🧬 BED format is tab-separated with 3+ columns (chrom, start, end). |
| 22 | B | 🧬 GFF is tab-separated with 9 standard columns. |
| 23 | B | 🧬 csvsql allows SQL queries with numeric comparisons. |
| 24 | B | 🧬 VCF is tab-separated with metadata lines starting with ##. |
| 25 | B | 🧬 CSV with clear headers is standard for sample metadata. |
| 26 | B | 🧬 pandas provides powerful filtering and analysis capabilities. |
| 27 | B | 🧬 NR>1 means "row number > 1", skipping the header. |
| 28 | B | 🧬 groupby() groups by sample, then calculate mean on coverage column. |
| 29 | B | 🧬 "NA" or "." are standard conventions in bioinformatics; document your choice. |
| 30 | A | 🧬 csvjoin -c specifies column to join on. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **27-30 correct (90-100%)** | 🏆 Excellent! | You know CSV/TSV well! |
| **21-26 correct (70-89%)** | ✅ Good | Review quoting and csvkit commands. |
| **15-20 correct (50-69%)** | ⚠️ Satisfactory | Re-read CSV syntax sections and bioinformatics examples. |
| **Less than 15 correct (<50%)** | 📚 Needs Review | Recommended to re-read the lecture and practice with biological data. |

---

## 🧬 Bioinformatics CSV/TSV Practice Ideas

1. **Parse BED file**: Read a BED file (tab-separated) and filter regions by chromosome
2. **DESeq2 Analysis**: Load differential expression results and filter significant genes
3. **Variant Filtering**: Process variant calling results with quality and depth filters
4. **Sample Merging**: Join sample metadata with analysis results using csvjoin or pandas
5. **Coverage Calculation**: Calculate average coverage per sample from alignment statistics
6. **GFF Parsing**: Parse gene annotations from GFF3 format (tab-separated with attributes)

---
