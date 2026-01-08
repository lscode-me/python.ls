# Data Transfer Encoding
## Base64, URL Encoding, and MIME Types

---

## 📋 Prerequisites

Before starting this module, you should:

- Understand character encodings (Module 03_Encodings)
- Know HTTP basics
- Have experience working with JSON
- **For Bioinformatics**: Work with web APIs for genomic data (e.g., NCBI, Ensembl, UniProt)

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Encode and decode data in Base64
- Use URL encoding for parameters
- Understand MIME types and their application
- Embed binary data in text formats
- **For Bioinformatics**: Interact with bioinformatics APIs, handle data URLs for visualizations, encode genomic data for transfer

---

## 1. Why Encoding is Needed

### 1.1 The Problem

How to transmit binary data (image, file) where text is expected?

- JSON supports only strings, not bytes
- URLs don't support all characters
- Email was created for ASCII text

**Bioinformatics Context:**

- REST APIs (NCBI, Ensembl) expect text-based formats
- Web tools need to embed images (protein structures, phylogenetic trees) in HTML
- Email notifications with attached plots/reports

### 1.2 The Solution

Encoding transforms binary data into safe text:

```
Binary:  [0x48, 0x65, 0x6C, 0x6C, 0x6F]
Base64:  "SGVsbG8="
```

---

## 2. Base64

### 2.1 How Base64 Works

Base64 uses 64 characters:

- `A-Z` (26)
- `a-z` (26)
- `0-9` (10)
- `+`, `/` (2)
- `=` (padding)

**Algorithm:**

1. Take 3 bytes (24 bits)
2. Split into 4 groups of 6 bits
3. Each group → one of 64 characters

```
Input:  "Hi" = 0x48 0x69
Binary: 01001000 01101001
Groups: 010010 000110 1001XX
Base64: S      G      k=

Padding: 2 bytes produce 3 characters + 1 "="
```

### 2.2 Command Line

```bash
# Encoding
echo -n "Hello, World!" | base64
# SGVsbG8sIFdvcmxkIQ==

# Decoding
echo "SGVsbG8sIFdvcmxkIQ==" | base64 -d
# Hello, World!

# File
base64 image.png > image.txt
base64 -d image.txt > restored.png
```

**Bioinformatics Example:**

```bash
# Encode a small reference sequence for API transfer
echo -n "ATCGATCGATCG" | base64
# QVRDR0FUQ0dBVENH

# Decode sequence from API response
echo "QVRDR0FUQ0dBVENH" | base64 -d
# ATCGATCGATCG
```

### 2.3 Python

```python
import base64

# Encoding
text = "Hello, World!"
encoded = base64.b64encode(text.encode()).decode()
print(encoded)  # SGVsbG8sIFdvcmxkIQ==

# Decoding
decoded = base64.b64decode(encoded).decode()
print(decoded)  # Hello, World!

# Binary data (image)
with open('image.png', 'rb') as f:
    image_data = f.read()
    
encoded_image = base64.b64encode(image_data).decode()

# Decoding and saving
decoded_image = base64.b64decode(encoded_image)
with open('restored.png', 'wb') as f:
    f.write(decoded_image)
```

**Bioinformatics Example:**

```python
import base64
import json

# Embed a small plot in JSON for API response
def embed_plot_in_json(plot_path):
    """Embed plot image as base64 in JSON."""
    with open(plot_path, 'rb') as f:
        plot_data = base64.b64encode(f.read()).decode()
    
    return {
        'analysis': 'gene_expression',
        'plot': {
            'mime_type': 'image/png',
            'data': plot_data
        }
    }

# Usage
result = embed_plot_in_json('expression_heatmap.png')
with open('api_response.json', 'w') as f:
    json.dump(result, f)
```

### 2.4 Base64 Variants

| Variant | Characters | Use Case |
|---------|-----------|----------|
| Standard | `+/=` | MIME, PEM |
| URL-safe | `-_` | URL, filenames |
| Base32 | `A-Z2-7` | Case-insensitive |
| Base16 | `0-9A-F` | Hex |

```python
import base64

# URL-safe Base64
encoded = base64.urlsafe_b64encode(b"data?with/special+chars")
print(encoded)  # ZGF0YT93aXRoL3NwZWNpYWwrY2hhcnM=
```

### 2.5 Data URLs

```html
<!-- Embedded image in HTML -->
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" />
```

```python
# Generate data URL
def image_to_data_url(filepath, mime_type):
    with open(filepath, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:{mime_type};base64,{data}"

data_url = image_to_data_url('logo.png', 'image/png')
```

**Bioinformatics Use Case:**

```python
def embed_structure_in_html(pdb_path):
    """Embed PDB structure visualization as data URL."""
    # Assuming you have a PNG rendering of the structure
    with open(pdb_path + '.png', 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    
    html = f"""
    <html>
    <body>
        <h1>Protein Structure</h1>
        <img src="data:image/png;base64,{data}" />
    </body>
    </html>
    """
    return html
```

---

## 3. URL Encoding

### 3.1 Why It's Needed

URLs can only contain ASCII characters from a "safe" set. Special characters need encoding.

```
Unsafe: space, ?, &, =, #, %, non-ASCII characters
```

**Bioinformatics:** Query parameters often contain:
- Gene names with special characters (e.g., `TNF-α`, `IL-1β`)
- Genomic coordinates (`chr1:12345-67890`)
- Search queries with spaces

### 3.2 Percent Encoding

```
Space  →  %20 or +
?      →  %3F
&      →  %26
=      →  %3D
#      →  %23
%      →  %25
```

### 3.3 Examples

```
Before:  "Hello World"
After:   "Hello%20World" or "Hello+World"

Before:  "price=100&discount=10%"
After:   "price%3D100%26discount%3D10%25"

Before:  "TNF-α"
After:   "TNF-%CE%B1"
```

**Bioinformatics Examples:**

```
Before:  "chr1:12345-67890"
After:   "chr1%3A12345-67890"

Before:  "gene=IL-1β&organism=human"
After:   "gene=IL-1%CE%B2&organism=human"
```

### 3.4 Python urllib

```python
from urllib.parse import quote, unquote, urlencode, parse_qs

# Encode string
encoded = quote("Hello world!")
print(encoded)  # Hello%20world%21

# Decode
decoded = unquote(encoded)
print(decoded)  # Hello world!

# URL parameters
params = {'name': 'John', 'city': 'New York', 'age': 30}
query_string = urlencode(params)
print(query_string)  # name=John&city=New+York&age=30

# Parse parameters
parsed = parse_qs(query_string)
print(parsed)  # {'name': ['John'], 'city': ['New York'], 'age': ['30']}
```

**Bioinformatics Example:**

```python
from urllib.parse import urlencode
import requests

# Query NCBI Gene database
params = {
    'db': 'gene',
    'term': 'TNF-α[Gene Name] AND Homo sapiens[Organism]',
    'retmode': 'json'
}

query_string = urlencode(params)
url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{query_string}"

response = requests.get(url)
print(response.json())
```

### 3.5 Command Line

```bash
# Python
python3 -c "from urllib.parse import quote; print(quote('Hello World'))"

# jq
echo '"Hello World"' | jq -r '@uri'
```

---

## 4. MIME Types in Detail

### 4.1 Structure

```
type/subtype; parameter=value

Examples:
text/plain; charset=utf-8
application/json
image/png
multipart/form-data; boundary=----WebKitFormBoundary
```

### 4.2 Main Types

| Type | Description | Examples |
|------|-------------|----------|
| text | Text data | text/html, text/css, text/plain |
| image | Images | image/png, image/jpeg |
| audio | Audio | audio/mpeg, audio/ogg |
| video | Video | video/mp4, video/webm |
| application | Application data | application/json, application/pdf |
| multipart | Composite data | multipart/form-data |

**Bioinformatics-Specific MIME Types:**

| MIME Type | Description |
|-----------|-------------|
| `chemical/x-pdb` | Protein Data Bank format |
| `chemical/x-mol` | Molecular structure (MOL) |
| `text/x-fasta` | FASTA sequences |
| `application/x-gzip` | Gzipped data (FASTQ.gz, etc.) |

### 4.3 In HTTP

```http
# Request
POST /api/data HTTP/1.1
Content-Type: application/json

{"key": "value"}

# Response
HTTP/1.1 200 OK
Content-Type: image/png

[binary data]
```

**Bioinformatics API Example:**

```http
# Upload VCF file
POST /api/variants HTTP/1.1
Content-Type: text/plain
Content-Disposition: attachment; filename="variants.vcf"

##fileformat=VCFv4.2
#CHROM  POS     ID      REF     ALT
chr1    12345   .       A       G
```

### 4.4 Content-Disposition

```http
Content-Disposition: attachment; filename="report.pdf"
Content-Disposition: inline; filename="image.png"
```

**Bioinformatics:**

```http
# Download FASTA file
Content-Type: text/plain
Content-Disposition: attachment; filename="Homo_sapiens.GRCh38.dna.fa"
```

---

## 5. Multipart Forms

### 5.1 Structure

```http
POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=----Boundary

------Boundary
Content-Disposition: form-data; name="title"

My Document
------Boundary
Content-Disposition: form-data; name="file"; filename="doc.pdf"
Content-Type: application/pdf

[binary content]
------Boundary--
```

### 5.2 Python requests

```python
import requests

# Upload file
files = {
    'file': ('document.pdf', open('document.pdf', 'rb'), 'application/pdf')
}
data = {
    'title': 'My Document',
    'description': 'Test upload'
}

response = requests.post(
    'https://api.example.com/upload',
    files=files,
    data=data
)
```

**Bioinformatics Example:**

```python
import requests

# Upload FASTQ file to analysis service
files = {
    'fastq_r1': ('sample_R1.fastq.gz', open('sample_R1.fastq.gz', 'rb'), 'application/gzip'),
    'fastq_r2': ('sample_R2.fastq.gz', open('sample_R2.fastq.gz', 'rb'), 'application/gzip')
}
data = {
    'sample_id': 'SAMPLE001',
    'organism': 'Homo sapiens',
    'experiment_type': 'RNA-Seq'
}

response = requests.post(
    'https://genomics-api.example.com/v1/analyze',
    files=files,
    data=data
)

print(response.json())
# {'job_id': 'job_12345', 'status': 'queued'}
```

---

## 6. Practical Examples

### 6.1 JWT Tokens

```python
import base64
import json

# JWT = header.payload.signature (Base64 URL)
jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Decode payload
parts = jwt.split('.')
# Add padding if needed
payload = parts[1] + '=' * (4 - len(parts[1]) % 4)
decoded = base64.urlsafe_b64decode(payload)
data = json.loads(decoded)
print(data)
# {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}
```

### 6.2 Email Attachments

```python
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['Subject'] = 'Document'

# Attachment
with open('document.pdf', 'rb') as f:
    attachment = MIMEBase('application', 'pdf')
    attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header(
        'Content-Disposition',
        'attachment; filename="document.pdf"'
    )
    msg.attach(attachment)
```

**Bioinformatics:**

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_vcf_report(vcf_path, recipient):
    """Email VCF variant report."""
    msg = MIMEMultipart()
    msg['Subject'] = 'Variant Analysis Report'
    msg['To'] = recipient
    
    # Attach VCF file
    with open(vcf_path, 'rb') as f:
        attachment = MIMEBase('text', 'plain')
        attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header(
            'Content-Disposition',
            f'attachment; filename="{vcf_path}"'
        )
        msg.attach(attachment)
    
    # Send email
    # smtp_server.send_message(msg)
```

### 6.3 Image in JSON

```python
import base64
import json

def image_to_json(filepath):
    with open(filepath, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    return {
        'filename': filepath,
        'data': data,
        'mime_type': 'image/png'
    }

# In API
image_json = image_to_json('photo.png')
response = requests.post(
    'https://api.example.com/images',
    json=image_json
)
```

**Bioinformatics:**

```python
def plot_to_json(plot_path):
    """Convert matplotlib plot to JSON with embedded base64 image."""
    with open(plot_path, 'rb') as f:
        plot_data = base64.b64encode(f.read()).decode()
    
    return {
        'plot_type': 'expression_heatmap',
        'format': 'png',
        'data': plot_data
    }

# API response with embedded plot
api_response = {
    'analysis_id': 'EXP001',
    'genes_analyzed': 500,
    'heatmap': plot_to_json('heatmap.png')
}
```

---

## 7. Best Practices

### 7.1 Base64

- Increases size by ~33%
- Don't use for large files
- Prefer URL-safe variant for URLs

**Bioinformatics:** Base64 is fine for small plots/logos, but **never** for FASTQ/BAM files. Use direct file transfer instead.

### 7.2 URL Encoding

- Always encode user input
- Use `urlencode` for parameters
- Remember difference between `+` and `%20`

**Bioinformatics:** Always encode gene names, genomic coordinates, and organism names in API queries.

### 7.3 MIME Types

- Specify correct Content-Type
- Add charset for text
- Use Content-Disposition for downloads

**Bioinformatics:** Use appropriate MIME types for genomic data:
- `text/plain` for FASTA/FASTQ/VCF
- `application/gzip` for compressed files
- `application/octet-stream` for BAM/CRAM

---

## 💡 Key Takeaways

- **Base64 — binary data as text**: 64 safe characters, +33% size increase.

- **URL encoding — safe URLs**: Special characters → %XX.

- **MIME types — content type**: type/subtype, critical for HTTP.

- **Not encryption**: Encoding doesn't protect data!

- **🧬 For Bioinformatics**: Use Base64 for embedding small visualizations, URL-encode genomic coordinates and gene names, specify correct MIME types for genomic file formats.

---

## 📚 Additional Resources

- [RFC 4648 - Base Encodings](https://tools.ietf.org/html/rfc4648)
- [RFC 3986 - URI](https://tools.ietf.org/html/rfc3986)
- [IANA Media Types](https://www.iana.org/assignments/media-types/)
- [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [Ensembl REST API](https://rest.ensembl.org/)

---

## 🚀 Next Steps

**This is the final module of the Data Fundamentals course.**

**Practice:**

1. Encode and decode a file in Base64
2. Properly URL-encode a string with special characters
3. Determine MIME type for different files
4. **Bioinformatics**: Query NCBI E-utilities API with URL-encoded gene names, embed a plot in HTML using data URLs

**Recommended courses to continue:**

- [Linux](../../Linux/) — Linux Command Line
- [Python](../../Python/) — Python Programming
- [Networking](../../Networking/) — Computer Networks
