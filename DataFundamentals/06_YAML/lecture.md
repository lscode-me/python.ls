# YAML
## Human-Friendly Data Format for Bioinformatics Configurations

---

## 📋 Prerequisites

Before starting this module, you should:

- Know JSON (Module 05_JSON)
- Understand data structures (objects, arrays)
- Have experience with configuration files

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Read and write valid YAML
- Understand YAML features and "gotchas"
- Compare YAML and JSON, choose the appropriate format
- Use `yq` for processing YAML
- Apply YAML in bioinformatics pipelines and DevOps tools

---

## 1. What is YAML

### 1.1 Definition

**YAML** (YAML Ain't Markup Language) — a human-readable data serialization format.

- Created in 2001
- Superset of JSON (valid JSON = valid YAML)
- Uses indentation instead of braces
- Supports comments

### 1.2 Where YAML is Used

| Tool | File |
|------|------|
| Docker Compose | `docker-compose.yml` |
| Kubernetes | `deployment.yaml`, `service.yaml` |
| GitHub Actions | `.github/workflows/*.yml` |
| Ansible | playbooks, inventory |
| CI/CD | `.gitlab-ci.yml`, `.travis.yml` |
| Helm | `Chart.yaml`, `values.yaml` |

**🧬 In Bioinformatics:**

| Tool | File |
|------|------|
| Snakemake | `Snakefile`, `config.yaml` |
| Nextflow | `nextflow.config` (supports YAML) |
| Cromwell | workflow configurations |
| CWL | Common Workflow Language definitions |
| Conda | `environment.yaml` |
| Galaxy | tool definitions, workflow configs |

### 1.3 Example YAML

**Generic Example:**

```yaml
# Application configuration
app:
  name: MyApp
  version: 1.0.0
  
server:
  host: localhost
  port: 8080
  debug: true
  
database:
  host: db.example.com
  port: 5432
  credentials:
    username: admin
    password: secret  # TODO: use secrets manager
    
features:
  - authentication
  - logging
  - caching
```

**🧬 Bioinformatics Example (Pipeline Configuration):**

```yaml
# Snakemake pipeline configuration
pipeline:
  name: RNA-Seq Analysis
  version: 2.1.0
  
reference:
  genome: /data/genomes/GRCh38.fa
  annotation: /data/annotations/gencode.v42.gtf
  
samples:
  - sample_id: PAT001
    fastq_r1: /data/fastq/PAT001_R1.fastq.gz
    fastq_r2: /data/fastq/PAT001_R2.fastq.gz
    condition: control
  - sample_id: PAT002
    fastq_r1: /data/fastq/PAT002_R1.fastq.gz
    fastq_r2: /data/fastq/PAT002_R2.fastq.gz
    condition: treatment

tools:
  fastqc:
    threads: 4
  star:
    threads: 8
    genome_dir: /data/star_index
  featurecounts:
    threads: 4
    feature_type: exon  # Count reads at exon level
    
quality_control:
  min_phred_score: 30
  min_read_length: 50
  adapter_trimming: true
```

---

## 2. YAML Syntax

### 2.1 Basic Types

```yaml
# Strings
string1: Hello World
string2: "Hello World"        # With quotes
string3: 'Hello World'        # Single quotes
string4: "Line 1\nLine 2"     # With escape (only in double quotes)

# Numbers
integer: 42
negative: -17
float: 3.14159
scientific: 1.5e+10
hex: 0xFF        # ⚠️ May be interpreted as string!
octal: 0o755     # ⚠️ Depends on YAML version

# Boolean
bool1: true
bool2: false
bool3: yes       # ⚠️ Also boolean!
bool4: no        # ⚠️ Also boolean!
bool5: on        # ⚠️ Also boolean!
bool6: off       # ⚠️ Also boolean!

# Null
null1: null
null2: ~
null3:           # Empty value = null
```

**🧬 Bioinformatics Examples:**

```yaml
# Sample metadata
sample_id: PAT001
age: 45
coverage: 30.5
quality_score: 35
sequenced: true
variants_called: null  # Analysis not yet complete

# Gene annotation
gene_name: BRCA2
chromosome: chr13
start: 32889611
end: 32973805
strand: "+"  # Quote to avoid interpretation issues
is_canonical: true
```

### 2.2 Strings — Details

```yaml
# Without quotes — simple string
simple: Hello World

# Double quotes — escape support
escaped: "Tab:\t Newline:\n Quote:\""

# Single quotes — everything literal (except '')
literal: 'No escape: \n stays as \n'
apostrophe: 'It''s working'  # '' = one '

# Multi-line — literal block (preserves newlines)
description: |
  This is a long
  multi-line string.
  Newlines are preserved.

# Multi-line — folded block (newlines → spaces)
summary: >
  This is also multi-line
  but newlines become spaces.
  Only double newlines create paragraphs.
  
  New paragraph here.

# With indentation
indented: |2
    This text starts with 4 spaces
    because of |2 modifier.
```

**🧬 Bioinformatics Examples:**

```yaml
# Gene description (literal block)
gene_description: |
  BRCA2 is a tumor suppressor gene that plays a role in DNA repair.
  Mutations in this gene are associated with increased risk of
  breast and ovarian cancer.

# Analysis notes (folded block)
analysis_notes: >
  Quality control passed. Coverage is adequate for variant calling.
  Minor adapter contamination detected but within acceptable limits.

# FASTA-like sequence (literal block)
sequence: |
  ATGCGATCGATCGATCGATCGATCG
  ATCGATCGATCGATCGATCGATCGA
  TCGATCGATCGATCGATCGATCGAT
```

### 2.3 Lists (Arrays)

```yaml
# Block style (recommended)
fruits:
  - apple
  - banana
  - cherry

# Flow style (like JSON)
fruits: [apple, banana, cherry]

# Nested lists
matrix:
  - [1, 2, 3]
  - [4, 5, 6]
  - [7, 8, 9]

# List of objects
users:
  - name: Alice
    age: 30
  - name: Bob
    age: 25
```

**🧬 Bioinformatics Examples:**

```yaml
# Chromosomes
chromosomes:
  - chr1
  - chr2
  - chr3
  - chrX
  - chrY
  - chrM

# Or flow style
chromosomes: [chr1, chr2, chr3, chrX, chrY, chrM]

# Sample list
samples:
  - sample_id: PAT001
    condition: control
    replicate: 1
  - sample_id: PAT002
    condition: treatment
    replicate: 1
  - sample_id: PAT003
    condition: treatment
    replicate: 2

# Quality score thresholds
phred_thresholds: [20, 30, 35, 40]

# Gene list
genes_of_interest:
  - BRCA1
  - BRCA2
  - TP53
  - EGFR
```

### 2.4 Objects (Maps)

```yaml
# Block style
person:
  name: Alice
  age: 30
  email: alice@example.com

# Flow style
person: {name: Alice, age: 30}

# Nested objects
config:
  server:
    host: localhost
    port: 8080
  database:
    host: db.local
    port: 5432

# Complex keys
? |-
  multi-line
  key
: value for complex key
```

**🧬 Bioinformatics Examples:**

```yaml
# Reference genome configuration
reference:
  genome:
    fasta: /data/genomes/GRCh38.fa
    index: /data/genomes/GRCh38.fa.fai
  annotation:
    gtf: /data/annotations/gencode.v42.gtf
    gff: /data/annotations/gencode.v42.gff3

# Variant calling parameters
variant_calling:
  caller: gatk
  parameters:
    min_base_quality: 20
    min_mapping_quality: 30
    ploidy: 2
  filters:
    min_depth: 10
    min_quality: 30
    max_missing: 0.1
```

### 2.5 Mixed Structures

```yaml
# Object with lists
server:
  name: web-1
  ports:
    - 80
    - 443
  tags:
    - production
    - frontend

# List of objects with nesting
deployments:
  - name: app-deployment
    replicas: 3
    containers:
      - name: app
        image: myapp:latest
        ports:
          - containerPort: 8080
      - name: sidecar
        image: sidecar:latest
```

**🧬 Bioinformatics Example (Pipeline Steps):**

```yaml
pipeline_steps:
  - name: quality_control
    tool: fastqc
    threads: 4
    inputs:
      - "{sample}_R1.fastq.gz"
      - "{sample}_R2.fastq.gz"
    outputs:
      - "qc/{sample}_R1_fastqc.html"
      - "qc/{sample}_R2_fastqc.html"
    
  - name: alignment
    tool: bwa
    threads: 8
    parameters:
      algorithm: mem
      mark_shorter: true
    inputs:
      - "{sample}_R1.fastq.gz"
      - "{sample}_R2.fastq.gz"
    output: "aligned/{sample}.bam"
    
  - name: variant_calling
    tool: bcftools
    threads: 4
    parameters:
      ploidy: 2
      min_base_quality: 20
    input: "aligned/{sample}.bam"
    output: "variants/{sample}.vcf.gz"
```

---

## 3. Advanced Features

### 3.1 Anchors & Aliases

```yaml
# Define anchor with &
defaults: &defaults
  adapter: postgres
  host: localhost
  pool: 5

# Use alias with *
development:
  <<: *defaults          # Insert all keys from defaults
  database: dev_db

production:
  <<: *defaults
  database: prod_db
  pool: 25               # Override pool

# Result for development:
# adapter: postgres
# host: localhost
# pool: 5
# database: dev_db
```

**🧬 Bioinformatics Example (Tool Defaults):**

```yaml
# Define default tool parameters
default_alignment: &alignment_defaults
  threads: 8
  min_mapping_quality: 30
  mark_duplicates: true
  sort_output: true

# Use for different samples
sample_PAT001:
  <<: *alignment_defaults
  input: PAT001.fastq.gz
  output: PAT001.bam

sample_PAT002:
  <<: *alignment_defaults
  input: PAT002.fastq.gz
  output: PAT002.bam
  threads: 16  # Override for this sample

# Quality control defaults
qc_defaults: &qc_defaults
  min_phred_score: 30
  min_read_length: 50
  adapter_trimming: true

preprocessing:
  <<: *qc_defaults
  trim_quality_window: 4

variant_qc:
  <<: *qc_defaults
  min_depth: 10
  min_quality: 30
```

### 3.2 Multiple Documents

```yaml
# First document
---
name: Document 1
type: config
---
# Second document
name: Document 2
type: data
...
# End of documents (optional)
```

**🧬 Bioinformatics Example (Multiple Samples):**

```yaml
---
sample_id: PAT001
condition: control
fastq_r1: PAT001_R1.fastq.gz
fastq_r2: PAT001_R2.fastq.gz
---
sample_id: PAT002
condition: treatment
fastq_r1: PAT002_R1.fastq.gz
fastq_r2: PAT002_R2.fastq.gz
---
sample_id: PAT003
condition: treatment
fastq_r1: PAT003_R1.fastq.gz
fastq_r2: PAT003_R2.fastq.gz
```

### 3.3 Tags

```yaml
# Explicit type specification
not_a_bool: !!str yes
not_a_number: !!str 123
explicit_float: !!float 42

# Custom tags
date: !custom 2024-01-15
```

**🧬 Bioinformatics Example:**

```yaml
# Ensure version is string, not float
pipeline_version: !!str 2.1
genome_version: !!str 38.0

# Ensure sample IDs remain strings
sample_id: !!str 001
patient_id: !!str 00123
```

---

## 4. YAML "Gotchas" — Pitfalls

### 4.1 Norway Problem

```yaml
# ⚠️ CAUTION! In YAML 1.1:
country: NO      # Interpreted as false!
answer: YES      # Interpreted as true!

# ✅ Solution — use quotes:
country: "NO"
answer: "YES"
```

**🧬 Bioinformatics Impact:**

```yaml
# ⚠️ Problem with gene names or conditions
gene_response: NO    # Interpreted as false!
treatment: YES       # Interpreted as true!

# ✅ Solution:
gene_response: "NO"
treatment: "YES"

# Also affects sample conditions
condition: ON        # Interpreted as true!
condition: "ON"      # Correct string
```

### 4.2 Numbers as Strings

```yaml
# ⚠️ May be interpreted as number:
version: 1.0     # float 1.0, not string "1.0"!
phone: 12345     # integer, not string

# ✅ Solution:
version: "1.0"
phone: "12345"
```

**🧬 Bioinformatics Impact:**

```yaml
# ⚠️ Problems with IDs and versions
sample_id: 001       # Becomes integer 1, loses leading zero!
genome_version: 38.0 # Becomes float 38.0, not "38.0"

# ✅ Solution:
sample_id: "001"
genome_version: "38.0"
patient_id: "PAT001"
```

### 4.3 Colon in Values

```yaml
# ⚠️ Error:
message: Error: file not found

# ✅ Solution — quotes:
message: "Error: file not found"

# Or (if no space after colon — OK):
url: http://example.com
```

**🧬 Bioinformatics Impact:**

```yaml
# ⚠️ Problem with paths and descriptions
description: Gene: BRCA2 function: DNA repair  # ERROR

# ✅ Solution:
description: "Gene: BRCA2 function: DNA repair"

# File paths usually OK (no space after colon)
file: file:///data/genomes/GRCh38.fa
```

### 4.4 Special Values

```yaml
# These values are interpreted specially:
empty:           # null
tilde: ~         # null  
yes: yes         # true (YAML 1.1)
no: no           # false (YAML 1.1)
on: on           # true (YAML 1.1)
off: off         # false (YAML 1.1)

# In YAML 1.2 only true/false are boolean
```

### 4.5 Indentation — Spaces Only!

```yaml
# ⚠️ TABS ARE FORBIDDEN!
# Use only spaces (usually 2)

server:
  host: localhost    # 2 spaces — OK
	port: 8080        # TAB — ERROR!
```

---

## 5. YAML vs JSON

### 5.1 Syntax Comparison

**JSON:**

```json
{
  "server": {
    "host": "localhost",
    "port": 8080,
    "features": ["auth", "logging"]
  }
}
```

**YAML:**

```yaml
server:
  host: localhost
  port: 8080
  features:
    - auth
    - logging
```

### 5.2 When to Use

| Criterion | JSON | YAML |
|-----------|------|------|
| Comments | ❌ No | ✅ Yes |
| Readability | Medium | High |
| Machine generation | ✅ Simple | ⚠️ More complex |
| File size | Larger | Smaller |
| Security | ✅ Safer | ⚠️ Risks (tags) |
| APIs | ✅ Standard | ❌ Rare |
| Configurations | ⚠️ Inconvenient | ✅ Ideal |

**🧬 In Bioinformatics:**

| Use Case | Format | Reason |
|----------|--------|--------|
| Pipeline configs | YAML | Readable, comments, human-editable |
| API responses (NCBI, Ensembl) | JSON | Standard, interoperable |
| Sample metadata | JSON or YAML | Both work; YAML for human editing |
| Tool parameters | YAML | Comments for documentation |
| Data exchange | JSON | Universal support |

### 5.3 Recommendations

- **JSON**: APIs, data exchange, machine generation

- **YAML**: Configurations, pipelines, human-editable files

---

## 6. Tools for YAML

### 6.1 yq — YAML Processor

```bash
# Installation (macOS)
brew install yq

# Installation (Linux)
# https://github.com/mikefarah/yq/releases

# Formatting
yq eval '.' config.yaml

# Extract value
yq eval '.server.port' config.yaml

# Change value
yq eval '.server.port = 9090' config.yaml

# Add element to list
yq eval '.features += ["new-feature"]' config.yaml

# Delete field
yq eval 'del(.server.debug)' config.yaml
```

**🧬 Bioinformatics Examples:**

```bash
# Extract reference genome path
yq eval '.reference.genome' pipeline_config.yaml

# Get all sample IDs
yq eval '.samples[].sample_id' config.yaml

# Update quality threshold
yq eval '.quality_control.min_phred_score = 35' config.yaml

# Add new sample
yq eval '.samples += [{"sample_id": "PAT004", "condition": "control"}]' config.yaml

# Extract tool threads
yq eval '.tools.star.threads' config.yaml
```

### 6.2 Converting YAML ↔ JSON

```bash
# YAML → JSON (with yq)
yq eval -o=json config.yaml

# JSON → YAML (with yq)
yq eval -P config.json

# With Python
python3 -c "import yaml, json, sys; print(json.dumps(yaml.safe_load(open('config.yaml')), indent=2))"
```

**🧬 Bioinformatics Examples:**

```bash
# Convert pipeline config to JSON for API
yq eval -o=json pipeline_config.yaml > pipeline_config.json

# Convert Ensembl JSON response to YAML for readability
curl -s "https://rest.ensembl.org/lookup/id/ENSG00000139618?content-type=application/json" | yq eval -P

# Convert sample metadata
yq eval -o=json samples.yaml > samples.json
```

### 6.3 YAML Validation

```bash
# With yamllint
pip install yamllint
yamllint config.yaml

# With Python
python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"

# Online: yamllint.com
```

### 6.4 yamllint Rules

```yaml
# .yamllint file
---
rules:
  line-length:
    max: 120
  indentation:
    spaces: 2
  truthy:
    check-keys: true
  comments:
    require-starting-space: true
```

---

## 7. YAML in Python

### 7.1 Basic Operations

```python
import yaml

# YAML string → Python dict
yaml_string = """
server:
  host: localhost
  port: 8080
features:
  - auth
  - logging
"""

data = yaml.safe_load(yaml_string)
print(data)
# {'server': {'host': 'localhost', 'port': 8080}, 'features': ['auth', 'logging']}

# Python dict → YAML string
yaml_output = yaml.dump(data, default_flow_style=False)
print(yaml_output)
```

**🧬 Bioinformatics Example:**

```python
import yaml

# Pipeline configuration
pipeline_config = """
pipeline:
  name: RNA-Seq Analysis
  version: 2.1.0

samples:
  - sample_id: PAT001
    condition: control
  - sample_id: PAT002
    condition: treatment

tools:
  star:
    threads: 8
    genome_dir: /data/star_index
"""

config = yaml.safe_load(pipeline_config)
print(f"Pipeline: {config['pipeline']['name']}")
print(f"Samples: {len(config['samples'])}")
print(f"STAR threads: {config['tools']['star']['threads']}")
```

### 7.2 Working with Files

```python
import yaml

# Reading
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Writing
with open('output.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
```

**🧬 Bioinformatics Example:**

```python
import yaml

# Load pipeline configuration
with open('pipeline_config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Modify configuration
config['tools']['star']['threads'] = 16
config['quality_control']['min_phred_score'] = 35

# Add new sample
new_sample = {
    'sample_id': 'PAT004',
    'condition': 'control',
    'fastq_r1': 'PAT004_R1.fastq.gz',
    'fastq_r2': 'PAT004_R2.fastq.gz'
}
config['samples'].append(new_sample)

# Save updated configuration
with open('pipeline_config_updated.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
```

### 7.3 safe_load vs load

```python
import yaml

# ✅ ALWAYS use safe_load
data = yaml.safe_load(yaml_string)

# ⚠️ NEVER use yaml.load without Loader!
# yaml.load(yaml_string)  # DANGEROUS! Can execute code!

# If you need full load (rarely):
data = yaml.load(yaml_string, Loader=yaml.SafeLoader)
```

### 7.4 Multiple Documents

```python
import yaml

yaml_multi = """
---
name: doc1
---
name: doc2
---
name: doc3
"""

# Load all documents
docs = list(yaml.safe_load_all(yaml_multi))
print(len(docs))  # 3

# Write multiple documents
yaml.dump_all(docs, stream, default_flow_style=False)
```

**🧬 Bioinformatics Example:**

```python
import yaml

# Multiple sample documents
samples_yaml = """
---
sample_id: PAT001
condition: control
fastq_r1: PAT001_R1.fastq.gz
---
sample_id: PAT002
condition: treatment
fastq_r1: PAT002_R1.fastq.gz
---
sample_id: PAT003
condition: treatment
fastq_r1: PAT003_R1.fastq.gz
"""

# Load all samples
samples = list(yaml.safe_load_all(samples_yaml))
print(f"Loaded {len(samples)} samples")

for sample in samples:
    print(f"Sample {sample['sample_id']}: {sample['condition']}")
```

---

## 8. YAML in Bioinformatics Pipelines

### 8.1 Snakemake Configuration

```yaml
# config.yaml for Snakemake
samples:
  PAT001: data/fastq/PAT001.fastq.gz
  PAT002: data/fastq/PAT002.fastq.gz
  PAT003: data/fastq/PAT003.fastq.gz

reference:
  genome: data/reference/GRCh38.fa
  annotation: data/reference/gencode.v42.gtf

params:
  star:
    threads: 8
    genome_dir: data/star_index
  
  featurecounts:
    threads: 4
    feature_type: exon
    attribute: gene_id
  
  deseq2:
    fdr_threshold: 0.05
    log2fc_threshold: 1.0
```

### 8.2 Conda Environment

```yaml
# environment.yaml
name: rnaseq-pipeline
channels:
  - bioconda
  - conda-forge
  - defaults

dependencies:
  - python=3.11
  - snakemake=7.32
  - fastqc=0.12.1
  - star=2.7.10b
  - samtools=1.17
  - bcftools=1.17
  - subread=2.0.3
  - multiqc=1.14
  - r-base=4.3.1
  - bioconductor-deseq2=1.40.0
  - pip:
    - pandas==2.0.3
    - numpy==1.24.3
    - matplotlib==3.7.2
```

### 8.3 Galaxy Tool Definition

```yaml
# tool.yaml for Galaxy
id: variant_calling
name: Variant Calling with BCFtools
version: 1.17.0

description: |
  Call variants from aligned BAM files using BCFtools mpileup and call.

inputs:
  - name: input_bam
    type: data
    format: bam
    label: Input BAM file
  
  - name: reference
    type: data
    format: fasta
    label: Reference genome
  
  - name: min_base_quality
    type: integer
    value: 20
    label: Minimum base quality
  
  - name: min_mapping_quality
    type: integer
    value: 30
    label: Minimum mapping quality

outputs:
  - name: output_vcf
    type: data
    format: vcf
    label: Variant calls (VCF)

command: |
  bcftools mpileup 
    -f $reference 
    -Q $min_base_quality 
    -q $min_mapping_quality 
    $input_bam |
  bcftools call 
    -mv 
    -o $output_vcf
```

### 8.4 CWL Workflow

```yaml
# workflow.cwl - Common Workflow Language
cwlVersion: v1.2
class: Workflow

inputs:
  fastq_r1:
    type: File
    doc: Forward reads FASTQ
  fastq_r2:
    type: File
    doc: Reverse reads FASTQ
  reference_genome:
    type: File
    doc: Reference genome FASTA
  threads:
    type: int
    default: 8

outputs:
  aligned_bam:
    type: File
    outputSource: alignment/output_bam
  variants_vcf:
    type: File
    outputSource: variant_calling/output_vcf

steps:
  quality_control:
    run: fastqc.cwl
    in:
      reads_r1: fastq_r1
      reads_r2: fastq_r2
    out: [qc_report]
  
  alignment:
    run: bwa_mem.cwl
    in:
      reads_r1: fastq_r1
      reads_r2: fastq_r2
      reference: reference_genome
      threads: threads
    out: [output_bam]
  
  variant_calling:
    run: bcftools_call.cwl
    in:
      input_bam: alignment/output_bam
      reference: reference_genome
    out: [output_vcf]
```

---

## 9. Best Practices

### 9.1 Formatting

```yaml
# ✅ Good
server:
  host: localhost
  port: 8080

# ❌ Bad — mixing styles
server:
  host: localhost
  port: 8080
database: {host: db, port: 5432}  # Flow style suddenly
```

### 9.2 Quotes

```yaml
# ✅ Use quotes for:
version: "1.0"           # Versions (otherwise float)
country: "NO"            # Strings similar to boolean
port: "8080"             # If you need string, not number
message: "Hello: World"  # Strings with colon
```

**🧬 Bioinformatics:**

```yaml
# Always quote IDs and versions
sample_id: "001"
genome_version: "38.0"
pipeline_version: "2.1"

# Quote gene names that might be ambiguous
gene: "NO"  # Not boolean false
response: "YES"  # Not boolean true
```

### 9.3 Comments

```yaml
# ✅ Useful comments
server:
  host: localhost
  port: 8080  # Default HTTP port
  
  # Connection pool settings
  pool:
    min: 5
    max: 20

# ❌ Useless comments  
server:
  host: localhost  # The host
  port: 8080       # The port
```

**🧬 Bioinformatics:**

```yaml
# ✅ Document parameters and thresholds
quality_control:
  min_phred_score: 30  # Illumina Q30 standard
  min_read_length: 50  # Filter short reads after trimming
  
  # Adapter sequences for Illumina TruSeq
  adapters:
    - AGATCGGAAGAGC
    - AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT
```

### 9.4 File Organization

```yaml
# Group logically related settings
# 1. Metadata
pipeline:
  name: RNA-Seq Analysis
  version: 2.1.0

# 2. Reference data
reference:
  genome: /data/genomes/GRCh38.fa
  annotation: /data/annotations/gencode.v42.gtf

# 3. Samples
samples:
  - sample_id: PAT001
    condition: control

# 4. Tool parameters
tools:
  star:
    threads: 8
```

---

## 💡 Key Takeaways

- **YAML — for humans**: Comments, clean syntax, indentation instead of braces.

- **Beware of types**: `yes/no`, `on/off` — boolean. `1.0` — float. Use quotes.

- **Spaces only**: Tabs are forbidden! Usually 2 spaces for indentation.

- **safe_load always**: Never use `yaml.load()` without SafeLoader.

- **JSON is a subset of YAML**: Any JSON is valid YAML (starting with YAML 1.2).

- **🧬 Bioinformatics**: YAML is ideal for pipeline configs, tool parameters, and sample metadata.

---

## 🚀 Next Steps

**Related Modules:**

- [Markup](../07_Markup/) — HTML, XML, Markdown
- [Config Files](../08_ConfigFiles/) — INI, TOML and other formats

**Practice Ideas:**

1. Write a Snakemake `config.yaml` for an RNA-Seq pipeline
2. Create a Conda `environment.yaml` for bioinformatics tools
3. Convert JSON sample metadata to YAML and back
4. Write a yamllint configuration for your project
5. Design a CWL workflow definition in YAML

**Going Deeper:**

- YAML 1.1 vs 1.2 (differences in boolean handling)
- Snakemake advanced configuration patterns
- CWL (Common Workflow Language) specifications
- Galaxy tool development with YAML

---

## 📚 Additional Resources

**Documentation:**

- [YAML Specification](https://yaml.org/spec/)
- [yq Documentation](https://mikefarah.gitbook.io/yq/)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

**Bioinformatics Workflows:**

- [Snakemake Documentation](https://snakemake.readthedocs.io/)
- [Common Workflow Language](https://www.commonwl.org/)
- [Galaxy Tool Development](https://galaxyproject.org/develop/)
- [Nextflow Documentation](https://www.nextflow.io/)

**Tools:**

- [YAML Lint](https://www.yamllint.com/)
- [YAML Multiline](https://yaml-multiline.info/)
- [yq releases](https://github.com/mikefarah/yq/releases)

**Learning:**

- [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/)
- [YAML Gotchas](https://www.arp242.net/yaml-config.html)

---
