# Homework: Python in Pipelines

## Assignment 1: Python stdin Filter - Uppercase Converter
Create Python script that reads lines from stdin and converts to uppercase.
- Script (`uppercase.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  
  for line in sys.stdin:
      print(line.strip().upper(), flush=True)
  ```
- Usage: `echo "hello world" | python3 uppercase.py`
- Test with: `cat file.txt | python3 uppercase.py | grep PATTERN`

## Assignment 2: JSON Stream Generator
Create Python script that generates JSONL output.
- Script (`generate_users.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  from datetime import datetime
  
  for i in range(1, 101):
      user = {
          "id": i,
          "username": f"user{i}",
          "created_at": datetime.now().isoformat(),
          "score": i * 10
      }
      print(json.dumps(user), flush=True)
  ```
- Usage: `python3 generate_users.py | jq -c 'select(.score > 500)'`
- Requirement: Must use `flush=True` for streaming

## Assignment 3: CSV to JSON Converter
Build a streaming CSV to JSONL converter.
- Script (`csv2json.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import csv
  import json
  
  reader = csv.DictReader(sys.stdin)
  for row in reader:
      print(json.dumps(row), flush=True)
  ```
- Test: `cat data.csv | python3 csv2json.py | jq .`
- Extension: Add command-line arguments for field selection

## Assignment 4: JSON to CSV Converter
Create JSONL to CSV streaming converter.
- Script (`json2csv.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  import csv
  
  writer = None
  for line in sys.stdin:
      try:
          obj = json.loads(line)
          if writer is None:
              # Initialize writer with first object's keys
              writer = csv.DictWriter(sys.stdout, fieldnames=obj.keys())
              writer.writeheader()
          writer.writerow(obj)
          sys.stdout.flush()
      except json.JSONDecodeError:
          print(f"Warning: Skipping invalid JSON: {line}", file=sys.stderr)
  ```
- Usage: `cat data.jsonl | python3 json2csv.py > output.csv`

## Assignment 5: Python Filter with Complex Logic
Create filter with complex business logic impossible in grep/awk.
- Task: Filter users by multiple conditions
- Script (`complex_filter.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  from datetime import datetime, timedelta
  
  threshold_date = datetime.now() - timedelta(days=30)
  
  for line in sys.stdin:
      try:
          user = json.loads(line)
          
          # Complex conditions
          created = datetime.fromisoformat(user['created_at'])
          is_recent = created > threshold_date
          is_active = user.get('status') == 'active'
          has_high_score = user.get('score', 0) > 500
          
          if is_recent and is_active and has_high_score:
              print(json.dumps(user), flush=True)
      except (json.JSONDecodeError, KeyError, ValueError):
          pass
  ```
- Usage: `cat users.jsonl | python3 complex_filter.py`

## Assignment 6: Pandas DataFrame Pipeline
Use pandas to process CSV in a pipeline.
- Script (`pandas_aggregate.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import pandas as pd
  
  # Read from stdin
  df = pd.read_csv(sys.stdin)
  
  # Aggregation
  result = df.groupby('category').agg({
      'amount': ['sum', 'mean', 'count'],
      'customer_id': 'nunique'
  }).reset_index()
  
  # Write to stdout
  result.to_csv(sys.stdout, index=False)
  ```
- Usage: `cat sales.csv | python3 pandas_aggregate.py > summary.csv`
- Note: Not streaming - loads entire file into memory

## Assignment 7: API Enrichment Pipeline
Enrich data with API calls in Python.
- Script (`enrich_users.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  import requests
  
  for line in sys.stdin:
      try:
          user = json.loads(line)
          user_id = user['id']
          
          # Fetch additional data from API
          response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
          if response.ok:
              api_data = response.json()
              user['email'] = api_data.get('email')
              user['city'] = api_data.get('address', {}).get('city')
          
          print(json.dumps(user), flush=True)
      except (json.JSONDecodeError, requests.RequestException):
          pass
  ```
- Usage: `python3 generate_users.py | head -10 | python3 enrich_users.py`

## Assignment 8: Shell → Python → Shell Pipeline
Build complete pipeline using all three stages.
- Pipeline:
  ```bash
  #!/bin/bash
  # Stage 1: Generate data (shell)
  seq 1 1000 | \
  
  # Stage 2: Complex processing (Python)
  python3 -c "
  import sys
  for line in sys.stdin:
      n = int(line.strip())
      # Complex calculation
      if n % 2 == 0 and n % 3 != 0:
          result = n ** 2 + n + 1
          print(result, flush=True)
  " | \
  
  # Stage 3: Aggregate (shell)
  awk '{sum += $1; count++} END {print "Sum:", sum, "Count:", count, "Avg:", sum/count}'
  ```

## Assignment 9: Streaming JSON Parser with ijson
Process large JSON files without loading into memory.
- Install: `pip install ijson`
- Script (`stream_parse.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  import ijson
  
  # Stream parse large JSON array
  parser = ijson.items(sys.stdin.buffer, 'item')
  
  for obj in parser:
      # Process each object as it's parsed
      if obj.get('status') == 'active':
          print(json.dumps(obj), flush=True)
  ```
- Test with large JSON array: Won't load entire file into memory

## Assignment 10: Pandas vs Command-Line Comparison
Compare performance of pandas vs CLI tools.
- Task: Calculate sum of column by group
- Generate test data:
  ```bash
  seq 1 1000000 | awk '{print $1 % 100 "," rand()*1000}' > large.csv
  ```
- Pandas approach (`pandas_groupby.py`):
  ```python
  import pandas as pd
  import sys
  df = pd.read_csv(sys.stdin)
  result = df.groupby(df.columns[0])[df.columns[1]].sum()
  print(result.to_csv())
  ```
- CLI approach:
  ```bash
  mlr --csv stats1 -a sum -f 2 -g 1 large.csv
  ```
- Measure: `time cat large.csv | python3 pandas_groupby.py`
- Measure: `time mlr --csv stats1 -a sum -f 2 -g 1 large.csv`
- Document: Which is faster? Memory usage?

## Bonus Challenges

### Bonus 1: Streaming Statistics Calculator
Calculate running statistics without storing all data.
- Script (`streaming_stats.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  import math
  
  count = 0
  sum_val = 0
  sum_sq = 0
  min_val = float('inf')
  max_val = float('-inf')
  
  for line in sys.stdin:
      try:
          num = float(line.strip())
          count += 1
          sum_val += num
          sum_sq += num ** 2
          min_val = min(min_val, num)
          max_val = max(max_val, num)
      except ValueError:
          continue
  
  if count > 0:
      mean = sum_val / count
      variance = (sum_sq / count) - (mean ** 2)
      stddev = math.sqrt(variance) if variance > 0 else 0
      
      stats = {
          "count": count,
          "sum": sum_val,
          "mean": mean,
          "stddev": stddev,
          "min": min_val,
          "max": max_val
      }
      print(json.dumps(stats, indent=2))
  ```
- Usage: `seq 1 1000 | python3 streaming_stats.py`
- Advantage: O(1) memory, single pass

### Bonus 2: Multi-Format Converter
Build tool that converts between JSON, CSV, YAML.
- Script (`convert.py`):
  ```python
  #!/usr/bin/env python3
  import sys
  import json
  import csv
  import argparse
  
  # Try importing yaml
  try:
      import yaml
      HAS_YAML = True
  except ImportError:
      HAS_YAML = False
  
  def json_to_csv(input_stream):
      data = [json.loads(line) for line in input_stream]
      if not data:
          return
      writer = csv.DictWriter(sys.stdout, fieldnames=data[0].keys())
      writer.writeheader()
      writer.writerows(data)
  
  def csv_to_json(input_stream):
      reader = csv.DictReader(input_stream)
      for row in reader:
          print(json.dumps(row), flush=True)
  
  # Add more conversion functions...
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--from', choices=['json', 'csv', 'yaml'], required=True)
  parser.add_argument('--to', choices=['json', 'csv', 'yaml'], required=True)
  args = parser.parse_args()
  
  # Route to appropriate converter
  # ...
  ```

### Bonus 3: Parallel Python Filters
Process data with multiple Python filters in parallel.
- Architecture:
  ```bash
  # Split input to 3 Python filters
  cat data.jsonl | tee >(python3 filter1.py > out1) \
                        >(python3 filter2.py > out2) \
                        >(python3 filter3.py > out3) \
                   > /dev/null
  
  # Merge results
  cat out1 out2 out3 | sort | uniq > final.jsonl
  ```
- Each filter processes different aspect
- Combine results at end

### Bonus 4: Python HTTP Server in Pipeline
Create simple API server that processes stdin data.
- Script (`api_server.py`):
  ```python
  #!/usr/bin/env python3
  from http.server import HTTPServer, BaseHTTPRequestHandler
  import json
  import sys
  import threading
  import queue
  
  data_queue = queue.Queue()
  
  class Handler(BaseHTTPRequestHandler):
      def do_GET(self):
          if self.path == '/data':
              self.send_response(200)
              self.send_header('Content-type', 'application/json')
              self.end_headers()
              
              items = []
              while not data_queue.empty():
                  items.append(data_queue.get())
              
              self.wfile.write(json.dumps(items).encode())
  
  def read_stdin():
      for line in sys.stdin:
          try:
              obj = json.loads(line)
              data_queue.put(obj)
          except json.JSONDecodeError:
              pass
  
  # Start stdin reader in background
  threading.Thread(target=read_stdin, daemon=True).start()
  
  # Start HTTP server
  server = HTTPServer(('localhost', 8000), Handler)
  print("Server running on http://localhost:8000")
  server.serve_forever()
  ```
- Usage: `python3 generate_users.py | python3 api_server.py`
- Access: `curl http://localhost:8000/data`

### Bonus 5: Hybrid ETL with Error Recovery
Build robust ETL with Python and bash.
- Features:
  - Python for complex transformations
  - Bash for orchestration
  - Error handling and retry
  - Checkpoints for resume
  - Logging
- Example structure:
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  CHECKPOINT=".checkpoint"
  
  if [ ! -f "$CHECKPOINT/extract" ]; then
      echo "Stage 1: Extract"
      curl -s "https://api.example.com/data" | \
          python3 validate.py > raw_data.jsonl
      touch "$CHECKPOINT/extract"
  fi
  
  if [ ! -f "$CHECKPOINT/transform" ]; then
      echo "Stage 2: Transform"
      cat raw_data.jsonl | \
          python3 transform.py > clean_data.jsonl
      touch "$CHECKPOINT/transform"
  fi
  
  if [ ! -f "$CHECKPOINT/load" ]; then
      echo "Stage 3: Load"
      cat clean_data.jsonl | \
          python3 load.py
      touch "$CHECKPOINT/load"
  fi
  
  echo "ETL complete"
  ```

## Submission Guidelines

### Code Requirements
1. **Proper shebang**: `#!/usr/bin/env python3`
2. **Flush output**: Use `flush=True` or `sys.stdout.flush()`
3. **Error handling**: Try-except for parsing errors
4. **Type hints** (optional but recommended):
   ```python
   def process_line(line: str) -> dict:
       ...
   ```
5. **Docstrings** for functions

### Testing Requirements
Test each script with:
- **Small data** (10 lines): Verify correctness
- **Large data** (10,000+ lines): Verify streaming works
- **Malformed input**: Script doesn't crash
- **Interruption**: Ctrl+C handling

### Performance Checklist
- [ ] Output is flushed immediately (no buffering)
- [ ] Memory usage is constant (O(1) for streaming)
- [ ] Handles large files without loading into memory
- [ ] Error handling doesn't stop entire pipeline

### Documentation Template
```markdown
## Script: script_name.py

### Purpose
Brief description of what the script does.

### Usage
\`\`\`bash
command | python3 script_name.py [options]
\`\`\`

### Input Format
Describe expected input format (CSV, JSONL, etc.)

### Output Format
Describe output format

### Dependencies
- Python 3.7+
- Libraries: pandas, requests, etc.

### Performance
- Memory: O(1) - streaming
- Time: O(n) - linear

### Error Handling
How script handles malformed input, missing fields, etc.
```

### Pandas vs CLI Decision Matrix
Create guide for when to use pandas vs CLI tools:

| Factor | Use Pandas | Use CLI Tools |
|--------|-----------|---------------|
| Data size | < 1GB | > 1GB |
| Operation | Complex joins, stats | Simple filter, group-by |
| Memory | Abundant | Limited |
| Speed needed | Analysis | Production pipeline |
| Dependencies | Python env available | Minimal dependencies |

### Bonus: Performance Benchmarks
Create comprehensive benchmark comparing:
1. Pure shell (awk, mlr, etc.)
2. Python with sys.stdin
3. Python with pandas
4. Hybrid (shell + Python)

Test on:
- 1MB file
- 100MB file
- 1GB file

Measure:
- Execution time
- Peak memory
- CPU usage
