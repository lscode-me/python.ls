# Configuration Files
## INI, TOML, .env, and Linux-Specific Formats for Bioinformatics

---

## 📋 Prerequisites

Before starting this module, you should:

- Know JSON and YAML (Modules 05, 06)
- Understand environment variables
- Have experience with applications and their settings

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Work with INI files and understand their use in systemd
- Use TOML for modern configurations
- Manage environment variables through .env files
- Understand Linux-specific formats: passwd, sshd_config, fstab, nginx
- Choose the appropriate configuration format for different tasks
- Configure bioinformatics tools and pipelines effectively

---

## 1. Overview of Configuration Formats

### 1.1 Evolution of Formats

```
Universal formats:
1980s     1990s      2000s      2010s      2020s
INI  →  XML  →  JSON  →  YAML  →  TOML
                              ↓
                           .env (parallel)

Linux/UNIX formats (since 1970s, still relevant):
passwd, group → sshd_config, sudoers → systemd units → nginx/apache
    (DSV)         (keyword-value)        (INI)         (block-based)
```

### 1.2 Format Comparison

**Universal formats (cross-platform):**

| Format | Comments | Nesting | Data Types | Application |
|--------|----------|---------|------------|-------------|
| INI | `;` or `#` | Sections | Strings | Windows, Git, systemd |
| TOML | `#` | Tables | Yes | Rust, Python |
| .env | `#` | No | Strings | Docker, Node.js |
| JSON | No | Full | Yes | API, Web |
| YAML | `#` | Full | Yes | DevOps |

**Linux-specific formats:**

| Format | Comments | Delimiter | Application |
|--------|----------|-----------|-------------|
| Colon-separated | No | `:` | passwd, group, shadow |
| Keyword-value | `#` | Spaces | sshd_config, sudoers |
| Space-separated | `#` | Spaces/tabs | fstab, hosts |
| Apache-style | `#` | Blocks `<>` | httpd.conf, nginx |
| Shell-style | `#` | `=` | /etc/environment, profile |

**🧬 In Bioinformatics:**

| Tool | Config Format | Example |
|------|---------------|---------|
| BLAST | INI-like | blast.rc |
| BWA | Command-line args | (no config file) |
| GATK | Properties/JSON | gatk.properties |
| Snakemake | YAML | config.yaml |
| Nextflow | Groovy/config | nextflow.config |
| Galaxy | YAML/INI | galaxy.yml |

---

## 2. INI Files

### 2.1 INI Format

**INI** (Initialization) — one of the oldest configuration formats, appearing in MS-DOS and early Windows. Despite its age, the format remains popular due to its simplicity and readability. INI files are used in Git (`.gitconfig`), PHP (`php.ini`), MySQL (`my.cnf`), and many other applications.

```ini
; This is a comment
# This is also a comment

[section]
key = value
another_key = another value

[database]
host = localhost
port = 5432
username = admin
; password stored in environment variables

[server]
debug = true
max_connections = 100
```

**🧬 Bioinformatics Example (BLAST Configuration):**

```ini
; ~/.ncbirc or blast.rc
[BLAST]
BLASTDB=/data/blast/databases
BLASTMAT=/usr/share/blast/data

[NET_SERV]
SRV_CONN_MODE=FIREWALL
SRV_HTTP_PROXY_HOST=proxy.example.com
SRV_HTTP_PROXY_PORT=8080
```

### 2.2 INI Rules

INI format has no strict specification, so different parsers may interpret it differently. However, basic rules are the same everywhere:

- **Sections** in square brackets `[section]`
- **Key-value pairs**: `key = value`
- **Comments**: `;` or `#`
- **Values** — always strings (parser may convert to types)
- **No nesting** (only sections, but some implementations support `[parent.child]`)

### 2.3 INI in Python

```python
import configparser

# Reading
config = configparser.ConfigParser()
config.read('config.ini')

# Accessing values
host = config['database']['host']
port = config.getint('database', 'port')
debug = config.getboolean('server', 'debug')

print(f"Database: {host}:{port}")

# Writing
config['new_section'] = {
    'key1': 'value1',
    'key2': 'value2'
}

with open('config.ini', 'w') as f:
    config.write(f)
```

**🧬 Bioinformatics Example:**

```python
import configparser

# Read bioinformatics tool configuration
config = configparser.ConfigParser()
config.read('pipeline.ini')

# Extract parameters
reference_genome = config['reference']['genome']
threads = config.getint('alignment', 'threads')
min_quality = config.getint('variant_calling', 'min_base_quality')

print(f"Using reference: {reference_genome}")
print(f"Threads: {threads}, Min quality: {min_quality}")
```

### 2.4 INI Examples

```ini
; .gitconfig
[user]
    name = John Doe
    email = john@example.com

[core]
    editor = vim
    autocrlf = input

[alias]
    st = status
    co = checkout
    br = branch
```

```ini
; php.ini
[PHP]
engine = On
memory_limit = 128M
max_execution_time = 30

[Date]
date.timezone = America/New_York
```

### 2.5 INI in systemd

**systemd** — the init system in modern Linux distributions — uses an extended INI format for its unit files. This is one of the most important uses of INI in modern Linux. All services, timers, mount points, and other systemd units are described in this format.

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application Service
Documentation=https://example.com/docs
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/bin/server --config /etc/myapp/config.toml
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production
EnvironmentFile=-/etc/myapp/env

[Install]
WantedBy=multi-user.target
```

**systemd INI features:**

- Sections `[Unit]`, `[Service]`, `[Install]` — standard for services
- Variable support: `$MAINPID`, `%u` (user), `%h` (home)
- Lists via spaces or key repetition
- Prefix `-` means "ignore error" (e.g., `-/etc/myapp/env`)

**🧬 Bioinformatics Example (Galaxy Service):**

```ini
# /etc/systemd/system/galaxy.service
[Unit]
Description=Galaxy Bioinformatics Platform
Documentation=https://galaxyproject.org/
After=network.target postgresql.service

[Service]
Type=simple
User=galaxy
Group=galaxy
WorkingDirectory=/srv/galaxy
ExecStart=/srv/galaxy/.venv/bin/python /srv/galaxy/lib/galaxy/main.py
Restart=on-failure
RestartSec=10
Environment=GALAXY_CONFIG_FILE=/srv/galaxy/config/galaxy.yml

[Install]
WantedBy=multi-user.target
```

---

## 2. TOML

### 3.1 What is TOML

**TOML** (Tom's Obvious Minimal Language) — a modern configuration format.

- Created by Tom Preston-Werner (GitHub)
- Obvious syntax
- Data type support
- Standard for Rust (Cargo.toml), Python (pyproject.toml)

### 3.2 TOML Syntax

```toml
# This is a comment

# Basic types
title = "TOML Example"
enabled = true
count = 42
price = 19.99
date = 2024-01-15
datetime = 2024-01-15T10:30:00Z

# Strings
simple = "Hello"
multiline = """
First line
Second line"""
literal = 'C:\path\to\file'

# Arrays
numbers = [1, 2, 3]
mixed = ["string", 42, true]
nested = [[1, 2], [3, 4]]

# Tables (objects)
[server]
host = "localhost"
port = 8080

[database]
host = "db.example.com"
port = 5432
username = "admin"

# Nested tables
[database.pool]
min = 5
max = 20

# Array of tables
[[users]]
name = "Alice"
role = "admin"

[[users]]
name = "Bob"
role = "user"
```

**🧬 Bioinformatics Example (Pipeline Configuration):**

```toml
[pipeline]
name = "RNA-Seq Analysis"
version = "2.1.0"
author = "Bioinformatics Core"

[reference]
genome = "/data/genomes/GRCh38.fa"
annotation = "/data/annotations/gencode.v42.gtf"
star_index = "/data/star_index"

[quality_control]
min_phred_score = 30
min_read_length = 50
adapter_trimming = true

[alignment]
tool = "STAR"
threads = 8
max_mismatches = 2

[variant_calling]
tool = "bcftools"
min_base_quality = 20
min_mapping_quality = 30
ploidy = 2

[[samples]]
sample_id = "PAT001"
condition = "control"
fastq_r1 = "/data/fastq/PAT001_R1.fastq.gz"
fastq_r2 = "/data/fastq/PAT001_R2.fastq.gz"

[[samples]]
sample_id = "PAT002"
condition = "treatment"
fastq_r1 = "/data/fastq/PAT002_R1.fastq.gz"
fastq_r2 = "/data/fastq/PAT002_R2.fastq.gz"
```

### 3.3 TOML in Python

```python
# Built-in module (Python 3.11+)
import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

print(config['server']['host'])
print(config['users'][0]['name'])

# For writing, use toml or tomli-w
import tomli_w

with open('output.toml', 'wb') as f:
    tomli_w.dump(config, f)
```

**🧬 Bioinformatics Example:**

```python
import tomllib

# Load pipeline configuration
with open('pipeline.toml', 'rb') as f:
    config = tomllib.load(f)

# Extract parameters
pipeline_name = config['pipeline']['name']
reference_genome = config['reference']['genome']
threads = config['alignment']['threads']

# Process samples
for sample in config['samples']:
    print(f"Processing {sample['sample_id']} ({sample['condition']})")
    print(f"  R1: {sample['fastq_r1']}")
    print(f"  R2: {sample['fastq_r2']}")
```

### 3.4 pyproject.toml

```toml
[project]
name = "myproject"
version = "1.0.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Author", email = "author@example.com"}
]
dependencies = [
    "requests>=2.28",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
]

[project.scripts]
myapp = "myproject:main"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

**🧬 Bioinformatics Tool Example:**

```toml
[project]
name = "variantcaller"
version = "1.0.0"
description = "Fast variant calling for NGS data"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [
    {name = "Bioinformatics Team", email = "bioinfo@example.org"}
]
dependencies = [
    "pysam>=0.21",
    "numpy>=1.24",
    "pandas>=2.0",
    "biopython>=1.81",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "black>=23.0",
]

[project.scripts]
variantcaller = "variantcaller.cli:main"

[tool.black]
line-length = 100
target-version = ['py39', 'py310', 'py311']
```

---

## 4. .env Files

### 4.1 .env Format

```bash
# .env file
# Comments start with #

DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=your-secret-key-here
DEBUG=true

# Quotes are optional
API_KEY="key-with-spaces and special=chars"

# Multi-line values
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA...
-----END RSA PRIVATE KEY-----"
```

**🧬 Bioinformatics Example:**

```bash
# .env for bioinformatics pipeline
REFERENCE_GENOME=/data/genomes/GRCh38.fa
STAR_INDEX=/data/star_index
ANNOTATION_GTF=/data/annotations/gencode.v42.gtf

# Database credentials
DB_HOST=localhost
DB_PORT=5432
DB_NAME=variants_db
DB_USER=bioinfo
DB_PASSWORD=secret-password-here

# API keys
NCBI_API_KEY=your-ncbi-api-key
ENSEMBL_API_URL=https://rest.ensembl.org

# Processing parameters
MAX_THREADS=16
MIN_QUALITY=30
MIN_COVERAGE=10
```

### 4.2 .env Rules

- **Format**: `KEY=value`
- **Comments**: `#`
- **Quotes**: optional (needed for spaces)
- **No sections** — flat structure
- **DO NOT commit to Git** — add to .gitignore

### 4.3 .env in Python

```python
# With python-dotenv library
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()  # Looks for .env in current directory
# or
load_dotenv('/path/to/.env')

# Usage
database_url = os.getenv('DATABASE_URL')
debug = os.getenv('DEBUG', 'false').lower() == 'true'
port = int(os.getenv('PORT', '8080'))

print(f"Connecting to {database_url}")
```

**🧬 Bioinformatics Example:**

```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get configuration
reference_genome = os.getenv('REFERENCE_GENOME')
star_index = os.getenv('STAR_INDEX')
threads = int(os.getenv('MAX_THREADS', '8'))
min_quality = int(os.getenv('MIN_QUALITY', '30'))

# Get API keys
ncbi_api_key = os.getenv('NCBI_API_KEY')
ensembl_api_url = os.getenv('ENSEMBL_API_URL', 'https://rest.ensembl.org')

print(f"Reference: {reference_genome}")
print(f"Threads: {threads}, Min quality: {min_quality}")
```

### 4.4 .env and Docker

```yaml
# docker-compose.yml
services:
  app:
    image: myapp
    env_file:
      - .env
    environment:
      - EXTRA_VAR=value  # Additional variables
```

```dockerfile
# Dockerfile
# DO NOT copy .env into image!
ENV NODE_ENV=production
```

**🧬 Bioinformatics Example:**

```yaml
# docker-compose.yml for bioinformatics pipeline
services:
  pipeline:
    image: rnaseq-pipeline:latest
    env_file:
      - .env
    volumes:
      - /data:/data:ro
      - /results:/results:rw
    environment:
      - PIPELINE_MODE=production
```

### 4.5 Example Structure

```
project/
├── .env              # Local secrets (in .gitignore)
├── .env.example      # Template (in Git)
├── .env.production   # Production settings
└── .env.test         # Test settings
```

```bash
# .env.example
DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=change-me-in-production
DEBUG=true
REFERENCE_GENOME=/data/genomes/GRCh38.fa
NCBI_API_KEY=your-api-key-here
```

---

## 5. Linux-Specific Formats

Linux historically uses many proprietary configuration formats that differ from universal formats (JSON, YAML, INI). These formats are optimized for specific tasks and often exist since early UNIX versions.

### 5.1 Colon-Separated Values (DSV)

**Delimiter-separated values** — format where fields are separated by colon (`:`). This is one of the oldest UNIX formats, used for system databases. Very compact and efficient for machine processing, though less human-readable.

```bash
# /etc/passwd — user database
# username:password:UID:GID:GECOS:home:shell
root:x:0:0:root:/root:/bin/bash
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
john:x:1000:1000:John Doe:/home/john:/bin/bash
```

**Fields in `/etc/passwd`:**

1. Username
2. Password (`x` = in /etc/shadow)
3. UID — numeric identifier
4. GID — default group
5. GECOS — full name and comment
6. Home directory
7. Login shell

```bash
# /etc/group — group database
# groupname:password:GID:members
root:x:0:
wheel:x:10:john,admin
docker:x:998:john,deploy
```

**Parsing in Python:**

```python
# Reading /etc/passwd
def parse_passwd():
    users = []
    with open('/etc/passwd') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                fields = line.strip().split(':')
                users.append({
                    'username': fields[0],
                    'uid': int(fields[2]),
                    'gid': int(fields[3]),
                    'gecos': fields[4],
                    'home': fields[5],
                    'shell': fields[6]
                })
    return users

# Or via standard module
import pwd
import grp

user = pwd.getpwnam('john')
print(f"{user.pw_name}: UID={user.pw_uid}, home={user.pw_dir}")

group = grp.getgrnam('docker')
print(f"{group.gr_name}: members={group.gr_mem}")
```

### 5.2 Keyword-Argument Format

**Keyword-argument** (or keyword-value) — format where each line contains a directive and its value, separated by spaces. Widely used in security and network service configurations.

```bash
# /etc/ssh/sshd_config — SSH server configuration
# Basic security settings
Port 22
AddressFamily any
ListenAddress 0.0.0.0
ListenAddress ::

# Authentication
PermitRootLogin prohibit-password
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no

# Restrictions
MaxAuthTries 3
MaxSessions 10
ClientAliveInterval 300
ClientAliveCountMax 2

# Subsystems
Subsystem sftp /usr/lib/openssh/sftp-server

# Conditional blocks
Match User deploy
    PasswordAuthentication no
    AllowTcpForwarding no
    X11Forwarding no
    ForceCommand /usr/local/bin/deploy-only.sh

Match Group developers
    AllowTcpForwarding yes
    PermitTunnel yes
```

**Format features:**

- Directive and value separated by spaces
- Case-insensitive keywords
- `Match` — conditional blocks
- No quotes for strings with spaces (context-dependent)

---

## 6. Best Practices

### 6.1 Security

```bash
# .gitignore
.env
*.pem
*_secret*
config/local.toml
```

### 6.2 Configuration Structure

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # With defaults
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    PORT = int(os.getenv('PORT', '8080'))
    
    # Required
    DATABASE_URL = os.environ['DATABASE_URL']  # Fails if missing
    SECRET_KEY = os.environ['SECRET_KEY']
```

**🧬 Bioinformatics Example:**

```python
# pipeline_config.py
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class PipelineConfig:
    # Reference data (required)
    REFERENCE_GENOME = Path(os.environ['REFERENCE_GENOME'])
    STAR_INDEX = Path(os.environ['STAR_INDEX'])
    ANNOTATION_GTF = Path(os.environ['ANNOTATION_GTF'])
    
    # Processing parameters (with defaults)
    MAX_THREADS = int(os.getenv('MAX_THREADS', '8'))
    MIN_QUALITY = int(os.getenv('MIN_QUALITY', '30'))
    MIN_COVERAGE = int(os.getenv('MIN_COVERAGE', '10'))
    
    # API keys (optional)
    NCBI_API_KEY = os.getenv('NCBI_API_KEY')
    ENSEMBL_API_URL = os.getenv('ENSEMBL_API_URL', 'https://rest.ensembl.org')
    
    # Validate paths exist
    def __post_init__(self):
        if not self.REFERENCE_GENOME.exists():
            raise FileNotFoundError(f"Reference genome not found: {self.REFERENCE_GENOME}")
        if not self.STAR_INDEX.exists():
            raise FileNotFoundError(f"STAR index not found: {self.STAR_INDEX}")
```

### 6.3 Configuration Validation

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    port: int = 8080
    
    class Config:
        env_file = '.env'

settings = Settings()  # Automatic validation
```

**🧬 Bioinformatics Example:**

```python
from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Optional

class PipelineSettings(BaseSettings):
    # Reference data
    reference_genome: Path
    star_index: Path
    annotation_gtf: Path
    
    # Processing parameters
    max_threads: int = 8
    min_quality: int = 30
    min_coverage: int = 10
    min_mapping_quality: int = 30
    
    # API keys
    ncbi_api_key: Optional[str] = None
    ensembl_api_url: str = "https://rest.ensembl.org"
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

# Automatic validation and type conversion
settings = PipelineSettings()
print(f"Reference: {settings.reference_genome}")
print(f"Threads: {settings.max_threads}")
```

---

## 💡 Key Takeaways

- **INI — simple but alive**: Used in Git, PHP, systemd. Sections, string values, extensions in different implementations.

- **TOML — modern standard**: Data types, readability, pyproject.toml, Cargo.toml.

- **.env — for secrets**: Environment variables, DO NOT commit to Git.

- **Linux formats are diverse**: Colon-separated (/etc/passwd), keyword-value (sshd_config), tabular (fstab), block-based (nginx). Each optimized for its task.

- **man pages are critical**: `man 5 passwd`, `man sshd_config`, `man fstab` — always up-to-date documentation.

- **Format choice**: Python → TOML, DevOps → YAML, secrets → .env, Linux system → specific formats.

- **🧬 Bioinformatics**: TOML for pipeline configs, .env for credentials, YAML for Snakemake/Nextflow.

---

## 🚀 Next Steps

**Practice Ideas:**

1. Create pyproject.toml for your Python bioinformatics project
2. Set up .env for a Docker Compose bioinformatics pipeline
3. Write a script to convert INI → TOML
4. Create a systemd unit file for a bioinformatics service (e.g., Galaxy)
5. Explore `/etc/passwd` and `/etc/group` on your system with Python
6. Configure a bioinformatics pipeline using TOML with validation

**Going Deeper:**

- Learn about Pydantic for configuration validation
- Study systemd unit files for complex services
- Explore Nextflow config DSL
- Investigate Snakemake configuration patterns

---

## 📚 Additional Resources

**Formats:**

- [TOML Specification](https://toml.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

**Linux man pages (section 5 — file formats):**

- `man 5 passwd` — /etc/passwd format
- `man 5 shadow` — /etc/shadow format
- `man 5 fstab` — filesystem table
- `man 5 hosts` — /etc/hosts format
- `man sshd_config` — SSH server configuration
- `man 5 sudoers` — sudoers file format
- `man 5 crontab` — crontab format
- `man systemd.unit` — systemd unit file format

**Bioinformatics:**

- [Snakemake Configuration](https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html)
- [Nextflow Configuration](https://www.nextflow.io/docs/latest/config.html)
- [Galaxy Configuration](https://galaxyproject.org/admin/config/)

---
