# Homework: Streams, IPC & Unix Sockets

## Assignment 1: Create and Use a Named Pipe
Create a FIFO and use it for async communication.
- Steps:
  1. Create named pipe: `mkfifo mypipe`
  2. Start reader in background: `cat < mypipe &`
  3. Write to pipe: `echo "Hello from pipe" > mypipe`
  4. Cleanup: `rm mypipe`
- Verify: Reader receives message immediately
- Question: What happens if you write before starting reader?

## Assignment 2: Async Producer-Consumer Pattern
Build a producer-consumer system with named pipes.
- Architecture:
  ```
  Producer → FIFO → Consumer
  ```
- Producer script (`producer.sh`):
  ```bash
  #!/bin/bash
  for i in {1..10}; do
    echo "Data $i"
    sleep 0.5
  done
  ```
- Consumer script (`consumer.sh`):
  ```bash
  #!/bin/bash
  while read line; do
    echo "Processing: $line"
  done
  ```
- Run: `./producer.sh > datastream & ./consumer.sh < datastream`
- Requirement: Consumer processes data as it arrives (streaming)

## Assignment 3: Python as stdin Filter
Create Python script that reads from stdin and transforms data.
- Task: Convert CSV to JSON
- Input: `data.csv` with: id,name,age
- Python script (`csv_to_json.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import csv
  import json
  
  reader = csv.DictReader(sys.stdin)
  for row in reader:
      print(json.dumps(row), flush=True)
  ```
- Usage: `cat data.csv | python3 csv_to_json.py | jq .`
- Requirement: Must work with streaming data (use `flush=True`)

## Assignment 4: Python stdout Generator
Create Python script that generates data to stdout.
- Task: Generate JSONL events
- Script (`generate_events.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  import time
  from datetime import datetime
  
  for i in range(100):
      event = {
          "id": i,
          "timestamp": datetime.now().isoformat(),
          "value": i * 10
      }
      print(json.dumps(event), flush=True)
      time.sleep(0.1)  # Simulate real-time events
  ```
- Usage: `python3 generate_events.py | jq -c 'select(.value > 500)'`
- Requirement: Output must stream, not buffer

## Assignment 5: Shell → Python → Shell Pipeline
Build a multi-stage pipeline with Python in the middle.
- Pipeline:
  ```bash
  seq 1 100 | \
    python3 -c "import sys; [print(int(x)**2) for x in sys.stdin]" | \
    awk '{sum+=$1} END {print "Sum of squares:", sum}'
  ```
- Task: Modify to calculate:
  1. Shell generates numbers 1-1000
  2. Python filters even numbers and squares them
  3. Shell calculates average
- Hint: Python filter: `if int(x) % 2 == 0`

## Assignment 6: Named Pipe with Error Handling
Create robust producer-consumer with cleanup.
- Script template:
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  PIPE="datastream"
  mkfifo "$PIPE"
  trap 'rm -f "$PIPE"' EXIT
  
  # Producer
  (
    for i in {1..100}; do
      echo "Item $i"
      sleep 0.1
    done
  ) > "$PIPE" &
  
  # Consumer
  while read line; do
    echo "Processed: $line"
  done < "$PIPE"
  
  wait
  ```
- Requirement: Pipe cleaned up even if script interrupted

## Assignment 7: Unix Domain Socket Communication
Use netcat with Unix sockets for IPC.
- Terminal 1 (Server):
  ```bash
  nc -lU /tmp/my.sock
  ```
- Terminal 2 (Client):
  ```bash
  echo "Hello Server" | nc -U /tmp/my.sock
  ```
- Task: Build chat application:
  - Server echoes messages back with timestamp
  - Client sends commands
  - Cleanup: `rm /tmp/my.sock`

## Assignment 8: Bidirectional Python-Shell Communication
Python script that reads from stdin and writes to stdout interactively.
- Script (`interactive.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  
  print("Ready for input", flush=True)
  for line in sys.stdin:
      command = line.strip()
      if command == "quit":
          break
      result = f"Processed: {command.upper()}"
      print(result, flush=True)
  ```
- Shell wrapper:
  ```bash
  #!/bin/bash
  {
    echo "hello"
    echo "world"
    echo "quit"
  } | python3 interactive.py
  ```
- Requirement: Real-time interaction (no buffering)

## Assignment 9: Parallel Processing with Named Pipes
Distribute work across multiple workers using FIFOs.
- Architecture:
  ```
           ┌→ Worker 1 (FIFO1) ┐
  Producer ├→ Worker 2 (FIFO2) ├→ Aggregator
           └→ Worker 3 (FIFO3) ┘
  ```
- Implementation:
  ```bash
  #!/bin/bash
  mkfifo pipe1 pipe2 pipe3
  trap 'rm -f pipe1 pipe2 pipe3' EXIT
  
  # Workers
  cat < pipe1 | grep "pattern" > results1.txt &
  cat < pipe2 | grep "pattern" > results2.txt &
  cat < pipe3 | grep "pattern" > results3.txt &
  
  # Distribute (round-robin)
  cat data.txt | awk '{print > ("pipe" ((NR-1)%3 + 1))}'
  
  wait
  cat results*.txt > final.txt
  ```

## Assignment 10: Stream Buffering Control
Demonstrate buffering issues and solutions.
- Problem script (buffered):
  ```python
  #!/usr/bin/env python3
  import sys
  import time
  
  for i in range(10):
      print(f"Item {i}")  # Buffered!
      time.sleep(1)
  ```
- Run: `python3 buffered.py | cat` (output delayed)
- Solution 1: `flush=True`
  ```python
  print(f"Item {i}", flush=True)
  ```
- Solution 2: `stdbuf`
  ```bash
  stdbuf -oL python3 buffered.py | cat
  ```
- Solution 3: Python flag
  ```bash
  python3 -u buffered.py | cat
  ```
- Task: Compare all three methods, document behavior

## Bonus Challenges

### Bonus 1: Multi-Stage Pipeline with FIFOs
Create 3-stage pipeline using named pipes.
- Stage 1: Data generation → FIFO1
- Stage 2: Processing → FIFO2
- Stage 3: Aggregation → Output
- All stages run concurrently
- Use `trap` for cleanup
- Show progress with `pv`

### Bonus 2: Python Streaming JSON Parser
Build a streaming JSON parser that processes large files line-by-line.
- Input: Multi-GB JSONL file
- Task: Extract specific fields without loading entire file
- Use: `ijson` library for streaming JSON
- Script:
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  
  for line in sys.stdin:
      try:
          obj = json.loads(line)
          if obj.get('status') == 'active':
              print(json.dumps({
                  'id': obj['id'],
                  'value': obj['value']
              }), flush=True)
      except json.JSONDecodeError:
          pass  # Skip malformed lines
  ```
- Requirement: Constant memory usage (no accumulation)

### Bonus 3: Shell-Python Hybrid ETL
Build complete ETL using both shell and Python.
- Extract (Shell):
  ```bash
  curl -s "https://api.example.com/data" | \
  ```
- Transform (Python):
  ```python
  python3 -c "
  import sys, json
  for line in sys.stdin:
      obj = json.loads(line)
      # Complex transformation
      obj['computed'] = obj['value'] * 2
      print(json.dumps(obj))
  " | \
  ```
- Load (Shell):
  ```bash
  jq -r '[.id, .computed] | @csv' > output.csv
  ```
- Add error handling, logging, and performance monitoring

### Bonus 4: Process Substitution Advanced
Use process substitution for complex pipelines.
- Example: Compare two data sources
  ```bash
  diff <(curl -s "https://api.example.com/v1/data" | jq -r '.id') \
       <(curl -s "https://api.example.com/v2/data" | jq -r '.id')
  ```
- Task: Build pipeline that:
  - Fetches data from 3 APIs concurrently
  - Compares results
  - Reports differences
- Use: `<(command)` for parallel execution

### Bonus 5: Custom IPC Protocol
Design a simple message protocol for shell-Python communication.
- Protocol format: `COMMAND|ARG1|ARG2|...`
- Commands: `ADD`, `MULTIPLY`, `STATS`, `QUIT`
- Python server:
  ```python
  import sys
  
  def handle_command(cmd, args):
      if cmd == "ADD":
          return sum(map(int, args))
      elif cmd == "MULTIPLY":
          result = 1
          for arg in args:
              result *= int(arg)
          return result
      # ... more commands
  
  for line in sys.stdin:
      parts = line.strip().split('|')
      cmd, args = parts[0], parts[1:]
      if cmd == "QUIT":
          break
      result = handle_command(cmd, args)
      print(result, flush=True)
  ```
- Shell client:
  ```bash
  {
    echo "ADD|5|10|15"
    echo "MULTIPLY|3|4|5"
    echo "QUIT"
  } | python3 server.py
  ```

## Submission Guidelines

### Required Components
1. **All scripts** with proper shebangs and error handling
2. **Usage examples** for each assignment
3. **Output samples** showing correct behavior
4. **Documentation**:
   - How to run each script
   - Expected input/output
   - Error handling strategy

### Testing Checklist
- [ ] Named pipes are created and cleaned up properly
- [ ] Python scripts use `flush=True` for streaming output
- [ ] Error handling with `trap` works correctly
- [ ] Scripts can handle interrupts (Ctrl+C) gracefully
- [ ] No buffer deadlocks in pipelines
- [ ] Process substitution works as expected

### Performance Notes
Document for each assignment:
- Memory usage (should be constant for streaming)
- Latency (time from input to output)
- Throughput (items processed per second)

### Common Pitfalls to Avoid
1. **Buffering**: Always use `flush=True` in Python
2. **Cleanup**: Use `trap` to remove FIFOs on exit
3. **Deadlocks**: Don't read and write to same FIFO in one process
4. **Blocking**: Open FIFOs for reading before writing
5. **Encoding**: Specify UTF-8 encoding if needed
