# Configuration Files - Quiz

Test your knowledge on "Configuration Files: INI, TOML, .env and Linux-Specific Formats" with a bioinformatics focus.

---

## Question 1: INI Sections

How are sections denoted in INI files?

A) [section]

B) `<section>`

C) `section:`

D) `{section}`

---

## Question 2: INI Comments

Which symbol is used for comments in INI?

A) `/*`

B) ; or #

C) `--`

D) `//`

---

## Question 3: TOML Acronym

What does TOML stand for?

A) Text Object Markup Language

B) Tom's Obvious Minimal Language

C) Typed Object Model Language

D) Terminal Output Markup Language

---

## Question 4: TOML Data Types

Which data type does TOML support that INI doesn't?

A) Comments

B) Boolean and numbers with explicit types

C) Strings

D) Keys

---

## Question 5: pyproject.toml

What is pyproject.toml used for?

A) Git settings

B) Web server configuration

C) Python project metadata and settings

D) Docker configuration

---

## Question 6: .env Security

Why shouldn't .env files be committed to Git?

A) They are too large

B) They are automatically generated

C) Git doesn't support .env format

D) They contain secrets and passwords

---

## Question 7: .env Format

Which syntax is correct for .env?

A) KEY=value

B) `[KEY] value`

C) `key: value`

D) `key = value`

---

## Question 8: python-dotenv

Which function loads .env file in Python?

A) `read_env()`

B) `parse_env()`

C) load_dotenv()

D) `import_env()`

---

## Question 9: TOML Arrays

How do you write an array in TOML?

A) `items = {1, 2, 3}`

B) `items: [1, 2, 3]`

C) items = [1, 2, 3]

D) `items = (1, 2, 3)`

---

## Question 10: TOML Tables

What does `[server]` create in TOML?

A) Array

B) String

C) Table (object) server

D) Comment

---

## Question 11: INI Python Module

Which Python module works with INI files?

A) `iniparser`

B) `settings`

C) `ini`

D) configparser

---

## Question 12: TOML Python 3.11

Which module for reading TOML is built into Python 3.11+?

A) `tomlparser`

B) `toml`

C) tomllib

D) `pytoml`

---

## Question 13: .env.example

What is .env.example for?

A) Test .env

B) Backup of .env

C) Automatically generated .env

D) Template with list of required variables (without values)

---

## Question 14: Docker env_file

How do you connect .env in docker-compose?

A) `source: .env`

B) `environment: .env`

C) `load: .env`

D) env_file: .env

---

## Question 15: TOML Dates

How do you write a date in TOML?

A) `date = "2024-01-15"`

B) date = 2024-01-15

C) `date = @2024-01-15`

D) `date = #2024-01-15"`

---

## Question 16: Cargo.toml

Which language uses Cargo.toml?

A) Python

B) Go

C) JavaScript

D) Rust

---

## Question 17: INI Limitations

What limitation does INI format have?

A) No comments

B) Can't use sections

C) Maximum 100 keys

D) All values are strings (no types)

---

## Question 18: os.getenv

What does `os.getenv('KEY', 'default')` do?

A) Deletes variable

B) Sets variable

C) Checks existence

D) Returns KEY value or 'default' if not found

---

## Question 19: pydantic-settings

What is pydantic-settings used for?

A) Typed loading and validation of configuration

B) Encrypting settings

C) Converting formats

D) Formatting configs

---

## Question 20: Format Choice

Which format is best for storing API keys?

A) JSON (commit)

B) YAML (commit)

C) .env (don't commit)

D) INI (commit)

---

## Question 21: /etc/passwd Delimiter

Which symbol is used as field delimiter in `/etc/passwd`?

A) Comma `,`

B) Tab

C) Space

D) Colon :

---

## Question 22: /etc/passwd Fields

How many fields does each entry in `/etc/passwd` contain?

A) 6

B) 7

C) 5

D) 8

---

## Question 23: /etc/shadow

What is stored in `/etc/shadow`?

A) Password hashes and password policies

B) User command history

C) User group list

D) User SSH keys

---

## Question 24: sshd_config Format

What format does SSH server configuration (`sshd_config`) use?

A) Keyword-value (directive and value separated by space)

B) INI with sections

C) JSON

D) YAML

---

## Question 25: sshd_config Match

What does the `Match` directive do in `sshd_config`?

A) Searches for files

B) Checks syntax

C) Compares passwords

D) Applies settings conditionally (for specific users/groups)

---

## Question 26: sudoers Editing

Which command should be used to safely edit `/etc/sudoers`?

A) `vim /etc/sudoers`

B) `sudoedit`

C) `nano /etc/sudoers`

D) visudo

---

## Question 27: /etc/fstab Columns

Which information is NOT contained in `/etc/fstab`?

A) Filesystem type

B) Mount options

C) Mount point

D) File access permissions

---

## Question 28: /etc/hosts Format

What does the `/etc/hosts` file describe?

A) Static mapping of IP addresses and hostnames

B) Firewall settings

C) System users

D) Network interfaces

---

## Question 29: systemd Unit Sections

Which sections are standard for a systemd service file?

A) `[Main]`, `[Config]`, `[Run]`

B) [Unit], [Service], [Install]

C) `[Global]`, `[Local]`, `[Remote]`

D) `[Server]`, `[Client]`, `[Network]`

---

## Question 30: systemd ExecStart

What does the `ExecStart` directive define in a systemd unit file?

A) Service start command

B) Working directory

C) User for execution

D) Service dependencies

---

## Question 31: systemd Restart

What does `Restart=on-failure` mean in systemd?

A) Restart only on non-zero exit code

B) Never restart

C) Restart on schedule

D) Always restart

---

## Question 32: nginx Blocks

What syntax is used for blocks in nginx configuration?

A) INI sections `[server]`

B) YAML indentation

C) XML tags `<server>...</server>`

D) Curly braces `server { ... }`

---

## Question 33: nginx location

What is the `location` directive used for in nginx?

A) Defining physical file path

B) Configuring SSL certificates

C) Routing requests by URL paths

D) Managing logs

---

## Question 34: /etc/environment

What format does the `/etc/environment` file use?

A) XML

B) INI with sections

C) Shell-style variables `KEY=value`

D) JSON

---

## Question 35: crontab Time Fields

How many time fields are in a crontab entry (without command)?

A) 3

B) 4

C) 6

D) 5

---

## Question 36: crontab */15

What does `*/15` mean in the minutes field of crontab?

A) Until 15th minute

B) Every 15 minutes

C) Exactly at 15 minutes

D) After 15th minute

---

## Question 37: crontab @daily

What does `@daily` mean in crontab?

A) Run once a day (at midnight)

B) Run once an hour

C) Run at boot

D) Run every minute

---

## Question 38: Python pwd Module

Which standard Python module allows reading `/etc/passwd`?

A) pwd

B) `passwd`

C) `auth`

D) `users`

---

## Question 39: systemd EnvironmentFile

What does the directive `EnvironmentFile=-/etc/myapp/env` do in systemd?

A) Creates environment file

B) Encrypts environment variables

C) Loads variables from file (ignoring error if not exists)

D) Deletes file after loading

---

## Question 40: man Section 5

What does section 5 of man pages describe (e.g., `man 5 passwd`)?

A) User commands

B) File formats and conventions

C) System administration

D) System calls

---

## Question 41: 🧬 BLAST Configuration

Which file format is used for BLAST database configuration?

A) JSON

B) YAML

C) INI-like (.ncbirc)

D) XML

---

## Question 42: 🧬 Pipeline Config Format

Which format is best for a bioinformatics pipeline configuration?

A) .env (flat key-value)

B) TOML (typed, structured)

C) Plain text

D) Binary

---

## Question 43: 🧬 Galaxy systemd

You need to create a systemd service for Galaxy. Which section defines the start command?

A) `[Unit]`

B) `[Service]`

C) `[Install]`

D) `[Command]`

---

## Question 44: 🧬 Environment Variables

Which format is best for storing bioinformatics tool credentials?

A) Hardcoded in scripts

B) .env file (not committed)

C) Public JSON file

D) In source code

---

## Question 45: 🧬 Reference Paths

You store reference genome paths in configuration. Which format allows comments for documentation?

A) JSON

B) TOML or YAML

C) CSV

D) Binary

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Sections in INI are denoted `[section_name]`. |
| 2 | B | In INI, comments start with `;` or `#`. |
| 3 | B | Tom's Obvious Minimal Language — named after creator Tom Preston-Werner. |
| 4 | B | TOML supports integer, float, boolean, datetime as separate types. |
| 5 | C | pyproject.toml — standard Python project configuration file (PEP 518, 621). |
| 6 | D | .env contains secrets (passwords, keys) that shouldn't be in repository. |
| 7 | A | Standard .env format: `KEY=value` (no spaces around `=`). |
| 8 | C | `load_dotenv()` from python-dotenv library loads .env into os.environ. |
| 9 | C | In TOML arrays: `key = [1, 2, 3]`. |
| 10 | C | `[server]` creates a table (equivalent to object/dict). |
| 11 | D | `configparser` — standard Python module for INI files. |
| 12 | C | `tomllib` built into Python 3.11+ (read-only). |
| 13 | D | .env.example — template with variable list without real values, committed to Git. |
| 14 | D | `env_file: .env` or `env_file: [.env]` in docker-compose.yml. |
| 15 | B | TOML supports dates without quotes: `date = 2024-01-15`. |
| 16 | D | Cargo.toml — Rust package configuration file. |
| 17 | D | In INI all values are strings, need manual type conversion. |
| 18 | D | `os.getenv(key, default)` returns variable value or default. |
| 19 | A | pydantic-settings loads and validates configuration with typing. |
| 20 | C | Secrets stored in .env and excluded from Git via .gitignore. |
| 21 | D | `/etc/passwd` uses colon `:` as field delimiter (colon-separated values). |
| 22 | B | Each entry contains 7 fields: username, password, UID, GID, GECOS, home, shell. |
| 23 | A | `/etc/shadow` stores password hashes and password policy info (expiry, etc.). |
| 24 | A | `sshd_config` uses keyword-value format: directive and value separated by space. |
| 25 | D | `Match` applies conditional settings to specific users, groups, or hosts. |
| 26 | D | `visudo` checks syntax before saving, preventing system lockout. |
| 27 | D | `/etc/fstab` contains device, mount point, FS type, options, dump and pass. Not permissions! |
| 28 | A | `/etc/hosts` describes static mapping of IP addresses and DNS names. |
| 29 | B | Standard systemd service sections: `[Unit]`, `[Service]`, `[Install]`. |
| 30 | A | `ExecStart` defines the command executed when starting the service. |
| 31 | A | `Restart=on-failure` restarts service only if it exits with error (code != 0). |
| 32 | D | nginx uses curly braces: `server { ... }`, `location { ... }`. |
| 33 | C | `location` defines rules for processing requests by URL paths. |
| 34 | C | `/etc/environment` uses shell-style variables: `KEY=value`. |
| 35 | D | Crontab has 5 time fields: minute, hour, day of month, month, day of week. |
| 36 | B | `*/15` means "every 15 units" — every 15 minutes in minutes field. |
| 37 | A | `@daily` — special string, equivalent to `0 0 * * *` (daily at midnight). |
| 38 | A | Module `pwd` provides access to user database (password database). |
| 39 | C | Prefix `-` means "don't fail if file doesn't exist", loads variables from file. |
| 40 | B | Section 5 of man describes file formats and conventions. |
| 41 | C | 🧬 BLAST uses .ncbirc with INI-like format for database configuration. |
| 42 | B | 🧬 TOML provides typed, structured configuration with comments. |
| 43 | B | 🧬 `[Service]` section defines `ExecStart` for the start command. |
| 44 | B | 🧬 .env file (not committed) is best for credentials and secrets. |
| 45 | B | 🧬 TOML and YAML support comments for documenting paths and parameters. |

---

## Scoring Guide

| Score | Grade | Recommendations |
|-------|-------|-----------------|
| **40-45 correct (89-100%)** | 🏆 Excellent! | You know configuration formats well! |
| **32-39 correct (71-87%)** | ✅ Good | Review Linux-specific formats and systemd. |
| **23-31 correct (51-69%)** | ⚠️ Satisfactory | Re-read sections on Linux configs and security. |
| **Less than 23 correct (<51%)** | 📚 Needs Review | Recommended to re-read the entire lecture. |

---

## 🧬 Bioinformatics Configuration Practice Ideas

1. **Create pipeline.toml**: Configure an RNA-Seq pipeline with reference paths, tool parameters, and sample info
2. **Set up .env**: Store database credentials, API keys (NCBI, Ensembl), and file paths
3. **Galaxy systemd service**: Write a systemd unit file for Galaxy server
4. **Validate configs**: Use Pydantic to validate pipeline configuration with types
5. **Docker integration**: Create docker-compose.yml with env_file for bioinformatics tools

---
