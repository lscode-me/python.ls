# Files, I-nodes & File Descriptors
### Understanding Unix File System Architecture

## Introduction

In Unix, **"everything is a file"** — regular files, directories, devices, sockets, and pipes are all represented as files. Understanding how Unix manages files at the system level is crucial for advanced data processing and system administration.

In this module, we'll explore:
- **I-nodes**: The metadata structure behind every file
- **File descriptors**: How processes access files
- **File types**: The different kinds of "files" in Unix
- **Permissions**: Who can do what with files
- **Special files**: stdin, stdout, stderr, and device files

---

## I-nodes (Index Nodes)

### What is an I-node?

An **i-node** (index node) is a data structure that stores metadata about a file:

- File type and permissions
- Owner (user and group)
- File size
- Timestamps (creation, modification, access)
- Number of hard links
- **Pointers to data blocks** (where file content is stored)

**Important**: The i-node does NOT contain:
- The filename (stored in the directory)
- The file content itself (stored in data blocks)

### Viewing I-node Numbers

```bash
# Show i-node numbers
ls -i

# Example output:
# 123456 file1.txt
# 123457 file2.txt
# 123456 file1_link.txt  # Same i-node as file1.txt!
```

### Detailed I-node Information with `stat`

```bash
stat filename

# Example output:
#   File: myfile.txt
#   Size: 1024          Blocks: 8          IO Block: 4096   regular file
# Device: 802h/2050d    Inode: 123456      Links: 2
# Access: (0644/-rw-r--r--)  Uid: ( 1000/   user)   Gid: ( 1000/   user)
# Access: 2024-11-27 10:23:45.000000000 +0000
# Modify: 2024-11-27 10:20:12.000000000 +0000
# Change: 2024-11-27 10:20:12.000000000 +0000
#  Birth: -
```

### Hard Links vs Symbolic Links

**Hard Link**: Multiple directory entries pointing to the same i-node
```bash
# Create hard link
ln original.txt hardlink.txt

# Both files point to the same i-node
ls -i original.txt hardlink.txt
# 123456 original.txt
# 123456 hardlink.txt

# Deleting one doesn't affect the other
rm original.txt
cat hardlink.txt  # Still works!
```

**Symbolic Link**: A special file containing a path to another file
```bash
# Create symbolic link
ln -s original.txt symlink.txt

# Different i-nodes
ls -i original.txt symlink.txt
# 123456 original.txt
# 789012 symlink.txt

# Deleting original breaks the symlink
rm original.txt
cat symlink.txt  # Error: No such file or directory
```

---

## File Descriptors

### What is a File Descriptor?

A **file descriptor** is a non-negative integer that identifies an open file in a process. It's essentially a handle or reference to an open file.

Every process maintains a **file descriptor table** mapping integers to open files.

### Standard File Descriptors

Every process starts with three standard file descriptors:

| FD | Name   | Purpose       | Symbol      |
|----|--------|---------------|-------------|
| 0  | stdin  | Standard input  | `/dev/stdin`  |
| 1  | stdout | Standard output | `/dev/stdout` |
| 2  | stderr | Standard error  | `/dev/stderr` |

### Viewing Open File Descriptors

```bash
# View FDs for current shell
ls -l /proc/self/fd/

# Example output:
# lrwx------ 1 user user 64 Nov 27 10:23 0 -> /dev/pts/0
# lrwx------ 1 user user 64 Nov 27 10:23 1 -> /dev/pts/0
# lrwx------ 1 user user 64 Nov 27 10:23 2 -> /dev/pts/0
# lr-x------ 1 user user 64 Nov 27 10:23 3 -> /proc/12345/fd

# View FDs for a specific process
lsof -p <PID>

# Or
ls -l /proc/<PID>/fd/
```

### Redirecting File Descriptors

```bash
# Redirect stdout to file
command > output.txt
# Same as: command 1> output.txt

# Redirect stderr to file
command 2> errors.txt

# Redirect stderr to stdout
command 2>&1

# Redirect stdout to stderr
command 1>&2

# Redirect both to same file
command &> all_output.txt
# Same as: command > all_output.txt 2>&1

# Redirect both to separate files
command > output.txt 2> errors.txt
```

### Custom File Descriptors

You can create custom file descriptors (FD 3 and above):

```bash
# Open file for reading on FD 3
exec 3< input.txt

# Read from FD 3
read line <&3
echo "$line"

# Close FD 3
exec 3<&-

# Open file for writing on FD 4
exec 4> output.txt

# Write to FD 4
echo "Hello" >&4

# Close FD 4
exec 4>&-
```

### Practical Example: Separate Stdout and Stderr

```bash
#!/bin/bash

# Redirect stdout and stderr to different files
exec 1> output.log
exec 2> error.log

echo "This goes to output.log"
echo "This goes to error.log" >&2

# Run commands - output is logged
ls /existing/path      # Goes to output.log
ls /nonexistent/path   # Goes to error.log
```

---

## File Types in Unix

Unix supports several file types, identified by the first character in `ls -l` output:

### Regular Files (`-`)
```bash
-rw-r--r-- 1 user group 1024 Nov 27 10:23 file.txt
```
Ordinary files containing data (text, binary, etc.)

### Directories (`d`)
```bash
drwxr-xr-x 2 user group 4096 Nov 27 10:23 mydir
```
Special files containing directory entries (filenames + i-node numbers)

### Symbolic Links (`l`)
```bash
lrwxrwxrwx 1 user group 10 Nov 27 10:23 link -> target.txt
```
Files containing paths to other files

### Named Pipes/FIFOs (`p`)
```bash
prw-r--r-- 1 user group 0 Nov 27 10:23 mypipe
```
Special files for inter-process communication

```bash
# Create named pipe
mkfifo mypipe

# Terminal 1: Write to pipe
echo "Hello" > mypipe

# Terminal 2: Read from pipe
cat < mypipe
```

### Sockets (`s`)
```bash
srwxrwxrwx 1 user group 0 Nov 27 10:23 mysocket
```
Files for network or local inter-process communication

### Character Devices (`c`)
```bash
crw-rw-rw- 1 root tty 5, 0 Nov 27 10:23 /dev/tty
```
Devices that transfer data character by character (terminals, serial ports)

### Block Devices (`b`)
```bash
brw-rw---- 1 root disk 8, 0 Nov 27 10:23 /dev/sda
```
Devices that transfer data in blocks (hard drives, USB drives)

### Counting File Types

```bash
# Count file types in /dev
ls -l /dev | cut -c1 | sort | uniq -c

# Example output:
#    245 b  # Block devices
#    156 c  # Character devices
#     12 d  # Directories
#     45 l  # Symbolic links
#      8 p  # Named pipes
#      3 s  # Sockets
```

---

## File Permissions

### Permission Structure

```
-rwxr-xr--
│└┬┘└┬┘└┬┘
│ │  │  └── Other: r-- (read only)
│ │  └───── Group: r-x (read + execute)
│ └──────── User:  rwx (read + write + execute)
└────────── File type: - (regular file)
```

### Permission Bits

| Permission | Symbol | Octal | Meaning                    |
|------------|--------|-------|----------------------------|
| Read       | r      | 4     | View file content          |
| Write      | w      | 2     | Modify file content        |
| Execute    | x      | 1     | Run file as program        |
| None       | -      | 0     | No permission              |

### Octal Notation

```bash
chmod 755 script.sh
# 7 = 4+2+1 = rwx (user)
# 5 = 4+0+1 = r-x (group)
# 5 = 4+0+1 = r-x (other)

chmod 644 file.txt
# 6 = 4+2+0 = rw- (user)
# 4 = 4+0+0 = r-- (group)
# 4 = 4+0+0 = r-- (other)
```

### Symbolic Notation

```bash
# Add execute permission for user
chmod u+x script.sh

# Remove write permission for group and other
chmod go-w file.txt

# Set exact permissions
chmod u=rwx,g=rx,o=r file.txt

# Add read permission for all
chmod a+r file.txt

# Recursive change
chmod -R 755 directory/
```

### Special Permission Bits

**Setuid (4000)**: Run as file owner
```bash
chmod 4755 program
# -rwsr-xr-x  # Note the 's' instead of 'x'
```

**Setgid (2000)**: Run as file group / inherit directory group
```bash
chmod 2755 directory
# drwxr-sr-x  # Note the 's' in group position
```

**Sticky bit (1000)**: Only owner can delete files
```bash
chmod 1777 /tmp
# drwxrwxrwt  # Note the 't' at the end
```

### umask — Default Permission Mask

```bash
# View current umask
umask
# 0022

# Umask 022 means:
# - Default file: 666 - 022 = 644 (rw-r--r--)
# - Default dir:  777 - 022 = 755 (rwxr-xr-x)

# Set new umask
umask 027
# Files: 640 (rw-r-----)
# Dirs:  750 (rwxr-x---)

# Test it
touch newfile.txt
ls -l newfile.txt
# -rw-r----- 1 user group 0 Nov 27 10:23 newfile.txt
```

---

## stdin/stdout/stderr as Files

### Special Device Files

```bash
# These are symlinks to file descriptors
ls -l /dev/std*

# /dev/stdin  -> /proc/self/fd/0
# /dev/stdout -> /proc/self/fd/1
# /dev/stderr -> /proc/self/fd/2
```

### The Black Hole: /dev/null

```bash
# Discard output
command > /dev/null

# Discard errors
command 2> /dev/null

# Discard everything
command &> /dev/null

# Use as empty input
program < /dev/null
```

### Random Data Sources

**`/dev/zero`**: Infinite stream of null bytes
```bash
# Create 1MB file of zeros
dd if=/dev/zero of=zeros.dat bs=1M count=1

# Test disk write speed
dd if=/dev/zero of=testfile bs=1M count=1024
```

**`/dev/random`**: Cryptographically secure random (may block)
```bash
# Generate 32 random bytes
head -c 32 /dev/random | base64
```

**`/dev/urandom`**: Non-blocking pseudo-random
```bash
# Generate random password
head -c 16 /dev/urandom | base64

# Generate random numbers
od -An -N4 -tu4 < /dev/urandom
```

---

## File Data Formats

### Text vs Binary Files

```bash
# Identify file type
file document.txt
# document.txt: ASCII text

file image.png
# image.png: PNG image data, 1024 x 768, 8-bit/color RGB

file program
# program: ELF 64-bit LSB executable
```

### Line Endings

| System  | Line Ending | Representation |
|---------|-------------|----------------|
| Unix/Linux/Mac | LF | `\n` |
| Windows | CRLF | `\r\n` |
| Old Mac | CR | `\r` |

```bash
# Convert Windows to Unix
dos2unix file.txt

# Convert Unix to Windows
unix2dos file.txt

# Manual conversion
tr -d '\r' < windows.txt > unix.txt
```

### Character Encoding

```bash
# Detect encoding
file -i document.txt
# document.txt: text/plain; charset=utf-8

# Convert encoding
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt

# Handle UTF-8 in scripts
export LC_ALL=en_US.UTF-8
```

### Magic Bytes and File Signatures

Many file formats start with specific bytes:

```bash
# View first bytes (hex)
xxd -l 16 file.pdf
# 00000000: 2550 4446 2d31 2e34 0a25 e2e3 cfd3 0a  %PDF-1.4.%......

# Common signatures:
# PDF:  %PDF
# PNG:  \x89PNG
# JPEG: \xFF\xD8\xFF
# ZIP:  PK\x03\x04
# ELF:  \x7FELF
```

---

## Practical Examples

### Example 1: Find Files by I-node

```bash
# Find all hard links to an i-node
find /path -inum 123456
```

### Example 2: Monitor File Descriptor Usage

```bash
#!/bin/bash
# Monitor FDs while running a command

# Run command in background
sleep 100 &
PID=$!

# Watch FDs
watch -n 1 "ls -l /proc/$PID/fd/"
```

### Example 3: Safe Temporary Files

```bash
# Create temp file with FD
exec 3> $(mktemp)

# Write to it
echo "data" >&3

# Read from it (rewind first)
exec 3<&-
exec 3< /path/to/temp/file
cat <&3

# Clean up
rm /path/to/temp/file
exec 3<&-
```

### Example 4: Permission Audit

```bash
# Find world-writable files (security risk)
find /path -type f -perm -002 -ls

# Find files with setuid bit (security sensitive)
find /usr/bin -perm -4000 -ls

# Find files with no owner
find /path -nouser -o -nogroup
```

---

## Summary

In this module, you learned:

- ✅ **I-nodes**: Metadata structures, hard links vs symlinks
- ✅ **File descriptors**: Process file handles, standard descriptors (0, 1, 2)
- ✅ **File types**: Regular, directory, link, pipe, socket, device
- ✅ **Permissions**: rwx, octal notation, chmod, umask, special bits
- ✅ **Special files**: stdin/stdout/stderr, /dev/null, /dev/random
- ✅ **File formats**: Text vs binary, encodings, line endings, magic bytes

### Next Steps

In the next module, we'll explore **Shell Programming** to build reusable data-processing scripts using these concepts.
