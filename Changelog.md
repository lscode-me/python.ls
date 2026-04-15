# Changelog

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
