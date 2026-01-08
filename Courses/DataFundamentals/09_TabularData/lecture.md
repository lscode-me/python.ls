# Tabular Data
## CSV, TSV: Reading, Writing, and Processing for Bioinformatics

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand text file formats
- Know basics of working with files in Python
- Have basic understanding of tables (rows, columns)

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Read and write CSV files
- Handle typical CSV problems
- Use command-line utilities for CSV
- Work with CSV in Python
- Process biological data in tabular formats

---

## 1. What is CSV

### 1.1 Definition

**CSV** (Comma-Separated Values) — a text format for tabular data.

```csv
name,age,city
Alice,30,Moscow
Bob,25,London
Charlie,35,Paris
```

**🧬 Bioinformatics Example:**

```csv
gene_id,gene_name,chromosome,start,end,strand
ENSG00000139618,BRCA2,13,32889611,32973805,+
ENSG00000141510,TP53,17,7571720,7590868,-
ENSG00000012048,BRCA1,17,43044295,43125483,-
```

### 1.2 Advantages and Disadvantages

**Advantages:**

- Simple text format
- Universal support (Excel, databases, programming languages)
- Compact
- Human-readable

**Disadvantages:**

- No standard (RFC 4180 — recommendation, not requirement)
- No data types (everything is strings)
- Problems with delimiters in data
- No metadata

**🧬 In Bioinformatics:**

CSV/TSV is used for:
- Gene annotation tables
- Variant calling results (VCF can be exported to CSV)
- Sample metadata
- Differential expression results from DESeq2, edgeR
- Quality control metrics

---

## 2. CSV Syntax

### 2.1 Basic Format

```csv
header1,header2,header3
value1,value2,value3
value4,value5,value6
```

### 2.2 Quotes for Special Values

```csv
name,description,price
"Widget","Simple widget",9.99
"Gadget","Has a comma, inside",19.99
"Thing","Has ""quotes"" inside",29.99
"Item","Has
newline",39.99
```

Quoting rules:

- Value with comma → quote it
- Value with quotes → double quotes `""`
- Value with newline → quote it

**🧬 Bioinformatics Example:**

```csv
gene_id,gene_name,description,go_terms
ENSG00000139618,BRCA2,"BRCA2 DNA repair associated, involved in homologous recombination","GO:0006281,GO:0000724"
ENSG00000141510,TP53,"Tumor protein p53, also known as ""guardian of the genome""","GO:0006915,GO:0030330"
```

### 2.3 TSV (Tab-Separated Values)

```tsv
name	age	city
Alice	30	Moscow
Bob	25	London
```

Advantage: tabs rarely appear in data.

**🧬 Bioinformatics:**

Many formats use TSV:
- BED format (genomic intervals)
- SAM format (sequence alignments)
- GFF/GTF format (gene annotations)
- Custom analysis output from tools

---

## 3. CSV Problems

### 3.1 Encoding

```python
# File in Windows-1251
with open('data.csv', 'r', encoding='cp1251') as f:
    # ...

# File with BOM
with open('data.csv', 'r', encoding='utf-8-sig') as f:
    # ...
```

**🧬 Note:** Excel on Windows often exports CSV in Windows-1251 or with BOM, which can break bioinformatics pipelines expecting UTF-8.

### 3.2 Delimiters

```python
# Semicolon (European standard)
# name;age;city
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
```

**🧬 In Bioinformatics:**

Different tools use different delimiters:
- VCF: tab-separated
- GFF/GTF: tab-separated
- Custom exports: often comma or tab

### 3.3 Empty Values

```csv
name,age,city
Alice,30,
Bob,,London
,25,Paris
```

**🧬 Bioinformatics Example:**

```csv
sample_id,coverage,quality_score,variant_count
PAT001,30.5,35,1234
PAT002,,30,
PAT003,25.2,,2345
```

---

## 4. CSV in Command Line

### 4.1 Viewing

```bash
# View
cat data.csv
head -5 data.csv
tail -5 data.csv

# Pretty print
column -t -s, data.csv

# Count rows (minus header)
wc -l data.csv
```

**🧬 Bioinformatics Examples:**

```bash
# View first 10 genes
head -10 genes.csv | column -t -s,

# Count total samples
wc -l samples.csv

# View last 5 variants
tail -5 variants.csv
```

### 4.2 Processing with awk

```bash
# Select columns (1 and 3)
awk -F, '{print $1,$3}' data.csv

# Filter by condition
awk -F, '$2 > 30 {print $1}' data.csv

# Sum column
awk -F, 'NR>1 {sum+=$2} END {print sum}' data.csv
```

**🧬 Bioinformatics Examples:**

```bash
# Extract gene names and chromosomes
awk -F, '{print $2,$3}' genes.csv

# Filter high-quality variants
awk -F, 'NR>1 && $3 > 30 {print $0}' variants.csv

# Calculate average coverage
awk -F, 'NR>1 {sum+=$2; count++} END {print sum/count}' coverage.csv

# Count genes per chromosome
awk -F, 'NR>1 {chr[$3]++} END {for (c in chr) print c, chr[c]}' genes.csv
```

### 4.3 csvkit (Recommended)

```bash
# Installation
pip install csvkit

# View
csvlook data.csv

# Statistics
csvstat data.csv

# Select columns
csvcut -c name,age data.csv

# Filter
csvgrep -c age -m 30 data.csv

# Sort
csvsort -c age data.csv

# Convert to JSON
csvjson data.csv

# SQL queries to CSV!
csvsql --query "SELECT name, age FROM data WHERE age > 25" data.csv
```

**🧬 Bioinformatics Examples:**

```bash
# View gene annotations with formatting
csvlook genes.csv

# Get statistics on coverage data
csvstat coverage.csv

# Extract specific columns
csvcut -c gene_name,chromosome,start,end genes.csv

# Filter pathogenic variants
csvgrep -c clinical_significance -m pathogenic variants.csv

# Sort by quality score
csvsort -c quality_score -r variants.csv

# Convert gene list to JSON
csvjson genes.csv > genes.json

# SQL query on variants
csvsql --query "SELECT gene_name, COUNT(*) as variant_count \
  FROM variants \
  GROUP BY gene_name \
  HAVING variant_count > 5" variants.csv

# Join sample metadata with results
csvjoin -c sample_id samples.csv results.csv
```

---

## 5. CSV in Python

### 5.1 csv Module

```python
import csv

# Reading as lists
with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # First row — header
    for row in reader:
        print(row)  # ['Alice', '30', 'Moscow']

# Reading as dictionaries
with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
```

**🧬 Bioinformatics Example:**

```python
import csv

# Read gene annotations
with open('genes.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for gene in reader:
        gene_id = gene['gene_id']
        gene_name = gene['gene_name']
        chrom = gene['chromosome']
        start = int(gene['start'])
        end = int(gene['end'])
        
        length = end - start
        print(f"{gene_name} ({gene_id}): chr{chrom}:{start}-{end}, length={length:,} bp")

# Read variant calling results
with open('variants.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    pathogenic_variants = []
    
    for variant in reader:
        if variant['clinical_significance'] == 'pathogenic':
            pathogenic_variants.append({
                'gene': variant['gene_name'],
                'position': variant['position'],
                'ref': variant['ref'],
                'alt': variant['alt']
            })
    
    print(f"Found {len(pathogenic_variants)} pathogenic variants")
```

### 5.2 Writing CSV

```python
import csv

# Writing lists
data = [
    ['name', 'age', 'city'],
    ['Alice', 30, 'Moscow'],
    ['Bob', 25, 'London'],
]

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Writing dictionaries
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
]

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(users)
```

**🧬 Bioinformatics Example:**

```python
import csv

# Export filtered variants to CSV
filtered_variants = [
    {'gene': 'BRCA2', 'position': 32912299, 'quality': 35, 'depth': 50},
    {'gene': 'TP53', 'position': 7577548, 'quality': 40, 'depth': 60},
]

with open('filtered_variants.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['gene', 'position', 'quality', 'depth']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_variants)

# Export gene expression results
expression_data = [
    ['gene_id', 'gene_name', 'log2FoldChange', 'padj'],
    ['ENSG00000139618', 'BRCA2', 2.5, 0.001],
    ['ENSG00000141510', 'TP53', -1.8, 0.005],
]

with open('deseq2_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(expression_data)
```

### 5.3 csv Parameters

```python
import csv

# European format (semicolon, comma in numbers)
with open('european.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')

# Excel format
with open('excel.csv', newline='') as f:
    reader = csv.reader(f, dialect='excel')

# Custom format
csv.register_dialect('custom',
    delimiter='|',
    quoting=csv.QUOTE_ALL)
```

**🧬 Bioinformatics:**

```python
# Read tab-separated BED file
with open('regions.bed', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        chrom, start, end = row[0], int(row[1]), int(row[2])
        print(f"{chrom}:{start}-{end}")

# Read GFF file (tab-separated)
with open('annotations.gff', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if row[0].startswith('#'):  # Skip comments
            continue
        seqid, source, type, start, end = row[0], row[1], row[2], int(row[3]), int(row[4])
        print(f"{type}: {seqid}:{start}-{end}")
```

### 5.4 pandas for CSV

```python
import pandas as pd

# Reading
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', encoding='cp1251', sep=';')

# Basic operations
print(df.head())
print(df.describe())
print(df[df['age'] > 25])

# Writing
df.to_csv('output.csv', index=False)
```

**🧬 Bioinformatics Examples:**

```python
import pandas as pd

# Load gene expression results
df = pd.read_csv('deseq2_results.csv')

# Filter significant genes
significant = df[(df['padj'] < 0.05) & (abs(df['log2FoldChange']) > 1)]
print(f"Found {len(significant)} significant genes")

# Sort by p-value
df_sorted = df.sort_values('padj')
print(df_sorted.head(10))

# Export top genes
df_sorted.head(50).to_csv('top_50_genes.csv', index=False)

# Load variant calling results
variants = pd.read_csv('variants.csv')

# Filter by quality
high_quality = variants[(variants['quality'] > 30) & (variants['depth'] > 20)]

# Count variants per gene
gene_counts = variants.groupby('gene_name').size().sort_values(ascending=False)
print(gene_counts.head(10))

# Calculate average coverage per sample
coverage = pd.read_csv('coverage.csv')
avg_coverage = coverage.groupby('sample_id')['coverage'].mean()
print(avg_coverage)

# Merge sample metadata with results
samples = pd.read_csv('samples.csv')
results = pd.read_csv('results.csv')
merged = samples.merge(results, on='sample_id')
merged.to_csv('merged_results.csv', index=False)
```

---

## 6. Best Practices

### 6.1 Recommendations

```python
# Always specify:
# - encoding='utf-8'
# - newline='' (important for Windows)

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Use DictReader/DictWriter for readability
```

**🧬 Bioinformatics Best Practices:**

1. **Use standard delimiters**: Prefer TSV for bioinformatics data (less ambiguity)
2. **Include metadata**: Add comments or separate metadata file
3. **Validate data**: Check for expected columns and data types
4. **Handle missing values**: Define how to represent missing data (NA, empty, NULL)
5. **Document format**: Specify delimiter, encoding, and column meanings

### 6.2 Validation

```python
def validate_csv(filepath):
    """Validate CSV file."""
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        expected_columns = len(header)
        
        for i, row in enumerate(reader, start=2):
            if len(row) != expected_columns:
                print(f"Row {i}: expected {expected_columns}, got {len(row)}")
```

**🧬 Bioinformatics Validation:**

```python
def validate_gene_csv(filepath):
    """Validate gene annotation CSV."""
    required_columns = {'gene_id', 'gene_name', 'chromosome', 'start', 'end'}
    
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Check header
        if not required_columns.issubset(reader.fieldnames):
            missing = required_columns - set(reader.fieldnames)
            raise ValueError(f"Missing required columns: {missing}")
        
        # Validate rows
        for i, row in enumerate(reader, start=2):
            # Check required fields are not empty
            for col in required_columns:
                if not row[col]:
                    print(f"Row {i}: {col} is empty")
            
            # Validate numeric fields
            try:
                start = int(row['start'])
                end = int(row['end'])
                if start >= end:
                    print(f"Row {i}: start ({start}) >= end ({end})")
            except ValueError as e:
                print(f"Row {i}: Invalid numeric value: {e}")

# Usage
validate_gene_csv('genes.csv')
```

---

## 💡 Key Takeaways

- **CSV — simple but tricky**: Quotes, delimiters, encodings require attention.

- **newline=''**: Always use when opening CSV in Python.

- **csvkit**: Powerful tools for working with CSV on the command line.

- **pandas**: For complex processing, use pandas.

- **🧬 Bioinformatics**: TSV is often preferred over CSV for biological data due to less ambiguity.

---

## 🚀 Next Steps

**Related Modules:**

- [10_Compression](../10_Compression/) — Data compression (gzip, zip, tar)
- [11_Checksums](../11_Checksums/) — Checksums and hashing

**Practice Ideas:**

1. Process a CSV file with csvkit on the command line
2. Load and analyze tabular data with pandas
3. Write a script to convert between CSV, TSV, and JSON
4. Download and analyze gene expression data from GEO
5. Parse VCF file and export to CSV
6. Create a validation script for bioinformatics CSV files

**Going Deeper:**

- Learn to parse BED, GFF, GTF formats (tab-separated)
- Study VCF format specification
- Explore DuckDB for SQL queries on CSV files
- Investigate Polars as a faster pandas alternative

---

## 📚 Additional Resources

**General:**

- [RFC 4180 - CSV Format](https://tools.ietf.org/html/rfc4180)
- [csvkit Documentation](https://csvkit.readthedocs.io/)
- [pandas CSV](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

**Bioinformatics:**

- [BED Format](https://genome.ucsc.edu/FAQ/FAQformat.html#format1)
- [GFF/GTF Format](https://genome.ucsc.edu/FAQ/FAQformat.html#format3)
- [VCF Format Specification](https://samtools.github.io/hts-specs/VCFv4.3.pdf)
- [Gene Expression Omnibus (GEO)](https://www.ncbi.nlm.nih.gov/geo/)

---
