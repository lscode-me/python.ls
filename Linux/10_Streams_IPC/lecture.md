# Streams, IPC & Unix Sockets

## Overview
Advanced stream handling: stdin/stdout as pseudo-files, named pipes (FIFOs), Unix sockets, and inter-process communication between shell and Python.

## Standard Streams as Files

### Using `-` for stdin/stdout
```bash
# Read from stdin
cat - | grep ERROR  # Same as: grep ERROR

# Write to stdout
echo "data" | cat - > output.txt

# Mix stdin and files
cat file1.txt - file2.txt <<< "middle content"
```

## Named Pipes (FIFOs)

### Creating and Using FIFOs
```bash
# Create named pipe
mkfifo mypipe

# Writer (in one terminal)
echo "Hello from pipe" > mypipe

# Reader (in another terminal)
cat < mypipe

# Both in background
cat < mypipe &
echo "Data" > mypipe
```

### Pipeline with FIFOs
```bash
#!/bin/bash
mkfifo pipe1 pipe2

# Producer
producer.sh > pipe1 &

# Processor
cat < pipe1 | process.sh > pipe2 &

# Consumer
cat < pipe2

# Cleanup
rm pipe1 pipe2
```

## Unix Domain Sockets

### Using netcat with Unix sockets
```bash
# Server
nc -lU /tmp/my.sock

# Client
echo "Hello" | nc -U /tmp/my.sock
```

## Shell ↔ Python IPC

### Python reads from stdin
```python
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    print(line.strip().upper())
```

```bash
# Use in pipeline
echo "hello" | python3 uppercase.py
```

### Python writes to stdout
```python
#!/usr/bin/env python3
import json
data = [{"id": i, "value": i*2} for i in range(10)]
for item in data:
    print(json.dumps(item))
```

```bash
# Process in bash
python3 generate.py | jq -c 'select(.value > 10)'
```

### Bidirectional: Python subprocess
```bash
#!/bin/bash
# Feed data to Python, get results back
echo -e "5\n10\n15" | python3 -c "
import sys
for line in sys.stdin:
    num = int(line.strip())
    print(num * 2)
"
```

## Complex IPC Patterns

### Pattern 1: Shell → Python → Shell
```bash
# Generate data in shell
seq 1 100 | \
  # Process in Python
  python3 -c "import sys; [print(int(x)**2) for x in sys.stdin]" | \
  # Aggregate in shell
  awk '{sum+=$1} END {print sum}'
```

### Pattern 2: Parallel Python Processors
```bash
# Split work among Python instances
seq 1 1000 | parallel -j 4 --pipe python3 process.py
```

### Pattern 3: Named Pipe for Async Processing
```bash
mkfifo datastream

# Producer (async)
./generate_data.sh > datastream &

# Consumer (Python)
python3 analyze.py < datastream

rm datastream
```

## Best Practices

1. **Use `-` for stdin/stdout**: Standard convention
2. **Named pipes for async**: Producer and consumer run independently
3. **Unix sockets for IPC**: Better than TCP for local communication
4. **Stream with Python**: Use sys.stdin/stdout, not files
5. **Clean up FIFOs**: Remove with `rm` when done
6. **Buffer control**: Use `sys.stdout.flush()` in Python

## Summary

| Mechanism | Use Case | Example |
|-----------|----------|---------|
| `-` pseudo-file | stdin/stdout | `cat - \| grep ERROR` |
| mkfifo | Async pipelines | `mkfifo p; cat < p & echo x > p` |
| Unix socket | Local IPC | `nc -lU /tmp/s` |
| Python stdin | Shell → Python | `echo "x" \| python3 script.py` |

## Next Steps
- Practice named pipes
- Build Python stream filters
- Study process substitution
- Explore message queues
