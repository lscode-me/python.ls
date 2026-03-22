# Streams, IPC & Unix Sockets - Quiz

## Questions

## Question 1: What command creates a named

What command creates a named pipe (FIFO)?

A) `touch pipe`
B) `mkfifo pipe`
C) `pipe create`
D) `fifo pipe`


## Question 2: What happens if you write

What happens if you write to a FIFO before anyone reads from it?

A) Data is lost
B) Write operation blocks until reader connects
C) Error is thrown
D) Data is buffered indefinitely


## Question 3: How do you read from

How do you read from stdin in Python?

A) `input()`
B) `sys.stdin.read()`
C) `for line in sys.stdin:`
D) Both B and C


## Question 4: What does do in Pythons

What does `flush=True` do in Python's print()?

A) Clears the buffer
B) Forces immediate output (no buffering)
C) Flushes to disk
D) Clears the screen


## Question 5: Which command makes Python output

Which command makes Python output line-buffered from the shell?

A) `python3 -b script.py`
B) `python3 -u script.py`
C) `python3 --unbuffered script.py`
D) Both B and C


## Question 6: How do you clean up

How do you clean up a FIFO on script exit?

A) `trap 'rm -f fifo' EXIT`
B) `rm -f fifo` at end of script
C) FIFOs auto-delete
D) `cleanup fifo`


## Question 7: What does do

What does `nc -lU /tmp/socket` do?

A) List sockets
B) Listen on Unix domain socket
C) Load socket
D) Lock socket


## Question 8: Which flag makes use line-buffered

Which flag makes `stdbuf` use line-buffered output?

A) `-o0`
B) `-oL`
C) `-line`
D) `-b`


## Question 9: What is process substitution used

What is process substitution `<(command)` used for?

A) Redirecting stderr
B) Creating temporary file-like interface for command output
C) Running command in background
D) Process management


## Question 10: How do you send data

How do you send data to a background Python process via stdin?

A) `echo "data" | python3 script.py &`
B) `python3 script.py < <(echo "data") &`
C) Use a named pipe or socket
D) Both B and C


## Question 11: Whats the difference between and

What's the difference between `>` and `>>` with named pipes?

A) No difference for FIFOs
B) `>` overwrites, `>>` appends
C) `>>` creates FIFO
D) `>` is blocking


## Question 12: Which Python library enables streaming

Which Python library enables streaming JSON parsing?

A) `json`
B) `jsonstream`
C) `ijson`
D) `streamjson`


## Question 13: What does do

What does `cat -` do?

A) Concatenate files
B) Read from stdin
C) List files
D) Count lines


## Question 14: How do you distribute work

How do you distribute work round-robin to 3 named pipes?

A) `split -n 3`
B) `awk '{print > ("pipe" ((NR-1)%3 + 1))}'`
C) `parallel -j 3`
D) `tee pipe1 pipe2 pipe3`


## Question 15: Whats the main advantage of

What's the main advantage of Unix domain sockets over TCP sockets?

A) Work over network
B) Faster (no network stack overhead)
C) More secure
D) Easier syntax


---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `mkfifo pipename` creates a named pipe (FIFO = First In First Out) |
| 2 | B | Write blocks until a reader connects; data waits in kernel buffer |
| 3 | D | Both methods work: `read()` loads all, iteration processes line-by-line |
| 4 | B | `flush=True` bypasses Python's output buffer for immediate write |
| 5 | B | `-u` flag forces unbuffered output (binary stdout/stderr) |
| 6 | A | `trap 'cleanup_command' EXIT` runs cleanup on any exit (normal or error) |
| 7 | B | `-l` = listen, `-U` = Unix domain socket at specified path |
| 8 | B | `-oL` = line-buffered output (one line at a time) |
| 9 | B | `<(cmd)` creates pseudo-file that can be read like a file |
| 10 | D | Process substitution or named pipes work; simple pipe with `&` doesn't |
| 11 | A | FIFOs don't store data; both `>` and `>>` work the same way |
| 12 | C | `ijson` parses JSON in streaming fashion without loading entire file |
| 13 | B | `-` conventionally means stdin (though cat reads stdin by default) |
| 14 | B | awk with modulo distributes lines round-robin to different files/pipes |
| 15 | B | Unix sockets bypass TCP/IP stack, faster for local IPC |
