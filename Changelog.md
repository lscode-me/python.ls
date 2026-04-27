# Changelog

## 2026-04-27

### Linux / 01_Unix_Streams
- Add early note that awk/sed/jq will be covered in later modules (before Filter→Transform→Aggregate section)

### Linux / 05_Grep_Sed_Awk
- Add intro paragraph explaining why grep/sed/awk are used together
- Add intro paragraphs before grep, sed, and awk sections
- Fix regex table: show both BRE and ERE alternation syntax
- Add BRE/ERE notes for `+`, `?`, `\b`, `\d`, `\w`, `\s`
- Fix `[A-Z|a-z]` → `[A-Za-z]` in email regex (lecture + quiz Q8)
- Fix URL extraction regex: stop at quotes/tags instead of spaces
- Fix awk examples: correct file references (data.txt, logs.txt, sales.csv), fix field numbers
- Fix CSV processing: use revenue column ($4), group by sales.csv
- Fix "response time average" → "response size average" in log analysis
- Add `sort` before `uniq -c` in requests per minute
- Fix Filter→Transform→Aggregate pattern for app.log timestamp format
- Fix "Compile regex" → clarify grep -P usage
- Fix log level regex for app.log format (no brackets)
- Move "Usage with grep" to end of Grep section, "Quick Syntax Reminder" before Next Steps
- Quiz: remove duplicated title prefixes (Q4,5,7,11,13,15,17,25,27,28)
- Quiz Q6: fix option A to avoid ambiguity
- Quiz Q10,Q29: fix truncated explanations

### Linux / 06_Structured_Data
- Add richer intro paragraph about structured data formats
- Add intro paragraphs for jq, JSONL, CSV sections
- Add JSONL conceptual explanation (JSON vs JSONL)
- Fix csvgrep: use regex for exact match instead of substring match
- Fix csvjoin: use left.csv/right.csv
- Fix mlr examples: users.csv → data.csv (age field), price → revenue, amount/customer → revenue/region
- Fix DuckDB output format flags (-markdown/-json → .mode)
- Rename "When to Use DuckDB" → "When to Use Which Tool"
- Add DuckDB analytics context in intro
- Add yq v4 (Mike Farah) compatibility note
- Rewrite xq examples to use yq -p xml (v4 native XML support)
- Fix yq example: data.json → users.json
- Fix Example 2: input.csv → users.csv
- Fix Best Practices: --null-data → -n (--null-input)
- Fix Summary table: remove unnecessary backslash
- Quiz: remove backticks from answer options, remove duplicated title prefixes
- Quiz Q1: fix truncated explanation
- Quiz Q8: add --csv flag to correct answer
- Quiz Q12: note read_csv() also valid in DuckDB v1.0+
- Quiz Q13: improve explanation

### Linux / Sample Data
- Move Quick File Creation Script to top of DataSamples page for visibility

## 2026-04-15

### Linux / 01_Unix_Streams
- Add dedicated `awk` and `jq` sections with explanations and examples
- Rewrite buffering section: add table of modes, explain why behavior changes (terminal vs pipe), add "Try It Yourself" demo
- Replace all fake `example.com` URLs with real working APIs (GitHub API, public CSV datasets)

### Linux / 02_Files_Inodes_Descriptors
- Rewrite hard links section: step-by-step i-node explanation, link count demo, hard vs symlink comparison table
- Expand Special Permission Bits: full subsections for setuid, setgid, sticky bit with real-world examples (`/usr/bin/passwd`, `/tmp`, shared directories)
- Add explanation of what happens when i-node link count reaches zero (covers quiz Q14)

### Build
- Fix reading time estimate: account for hands-on practice time (~3 min per code block) in addition to reading (200 WPM)
- Update time label from "X min read" to "~X min"

## 2026-04-14

### Python / 07_Coroutines
- Fix quiz: convert checkbox-style answers to plain format so quiz parser renders all 20 questions

## 2026-04-08

### Linux / 03_Shell_Programming
- Add `paste -sd+ | bc` tip for quick number summing (GNU/Linux and macOS variants)
- Add practical example: summing traffic bytes from access.log

### Linux / 04_Coreutils
- Add `paste -sd+ | bc` example in paste section (GNU/Linux and macOS variants)
- Add practical example: summing traffic bytes from access.log

## 2026-04-01

### Linux / 04_Coreutils
- Apply review feedback

## 2026-03-30

### Linux / 04_Coreutils
- Fix paste column order demo, fix `tr -s` example with access.log pipeline
- Replace all missing file refs with dataset files (logs.txt, emails.txt, data.txt, users.csv)
- Replace file.txt with data.txt in sort/uniq/cut examples and quiz

### Linux / 03_Shell_Programming
- Fix stray closing fence that hid String Operations heading

## 2026-03-27

### DataFundamentals / 02_NumberSystems
- Update Q19 to use kibibyte (KiB) terminology
- Add IEC binary prefixes (KiB/MiB), fix Q12 hint

### Linux / 03_Shell_Programming
- Apply reviewer feedback: fix count++ bug, fix file refs, add intro texts, test operators, here docs

## 2026-03-24

### Python
- Fix quiz answer keys

### DataFundamentals
- Fix quiz answer keys

## 2026-03-23

### Linux
- Fix incorrect answer codes in quizzes (lectures 03-14)

## 2026-03-21

### DataFundamentals
- Fix magic numbers ASCII representation, add MUTF-8 note

## 2026-03-18

### Linux / 02_Files_Inodes_Descriptors
- Apply review feedback — add descriptions and fix issues

## 2026-03-12

### Linux / 01_Unix_Streams
- Fix access.log consistency, expand to 15 lines, fix quiz Q6
- Add app.log to data/files/
- Review and polish chapter

## 2026-02-27

### Build / Web UI
- Show quiz explanations after submission
- Bump static versions
- Fix broken Geist font CDN
- Fix quizzes and Web UI
