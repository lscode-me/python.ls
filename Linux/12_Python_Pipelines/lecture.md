# Python in Pipelines: Hybrid Shell-Python Workflows

## Overview
Integrate Python into Unix pipelines as stream filters, compare pandas vs command-line tools, and build hybrid pipelines.

## Python as Stream Filter

### Reading from stdin
```python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Process line
    print(line.strip().upper())
```

```bash
echo "hello world" | python3 filter.py
```

### Writing to stdout
```python
#!/usr/bin/env python3
import sys
import json

for i in range(10):
    data = {"id": i, "value": i * 2}
    print(json.dumps(data), flush=True)
```

```bash
python3 generate.py | jq -c 'select(.value > 10)'
```

## Python for Complex Processing

### When to Use Python
```bash
# Simple filtering: use grep
grep "ERROR" app.log

# Complex logic: use Python
cat app.log | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        obj = json.loads(line)
        if obj['level'] == 'ERROR' and obj['code'] >= 500:
            print(json.dumps(obj))
    except:
        pass
"
```

## pandas vs Command-Line Tools

### Reading CSV in pandas
```python
#!/usr/bin/env python3
import pandas as pd
import sys

df = pd.read_csv(sys.stdin)
# Process
result = df.groupby('category')['amount'].sum()
print(result.to_csv())
```

```bash
cat data.csv | python3 pandas_process.py
```

### When to Use pandas
- Complex joins
- Window functions
- Statistical analysis
- Data cleaning with ML

### When to Use CLI Tools
- Simple filtering/aggregation
- Large files (streaming)
- Quick one-liners
- Low memory environments

## Hybrid Pipeline Patterns

### Pattern 1: Shell → Python → Shell
```bash
# Generate data in shell
seq 1 1000 | \
  # Complex processing in Python
  python3 -c "
import sys
for line in sys.stdin:
    n = int(line.strip())
    if n % 17 == 0:  # Complex condition
        print(n ** 2)
" | \
  # Aggregate in shell
  awk '{sum+=$1} END {print sum}'
```

### Pattern 2: Python for Enrichment
```bash
# Extract IDs
cut -d',' -f1 users.csv | \
  # Enrich with API (Python)
  python3 enrich.py | \
  # Convert to markdown
  awk -F',' '{printf "| %s | %s |\n", $1, $2}'
```

### Pattern 3: pandas for Complex Analysis
```bash
#!/bin/bash
# Heavy analytics with pandas
cat sales.csv | python3 - <<'PYTHON'
import pandas as pd
import sys

df = pd.read_csv(sys.stdin)

# Complex analysis
result = df.groupby(['category', 'month']).agg({
    'amount': ['sum', 'mean', 'count'],
    'customer_id': 'nunique'
}).reset_index()

result.to_csv(sys.stdout, index=False)
PYTHON
```

## Best Practices

1. **Flush output**: `print(..., flush=True)` or `sys.stdout.flush()`
2. **Stream data**: Don't load entire file if possible
3. **Use CLI for simple tasks**: Faster and less memory
4. **Use Python for complex logic**: Regex, ML, APIs
5. **Handle encoding**: `sys.stdin.reconfigure(encoding='utf-8')`
6. **Error handling**: Try-except blocks for robustness
7. **Test incrementally**: Start with small samples

## Summary

| Task | Tool Choice | Reason |
|------|-------------|--------|
| Filter by keyword | grep | Fastest |
| Complex conditions | Python | Logic flexibility |
| Group-by sum | mlr/awk | Memory efficient |
| Statistical analysis | pandas | Rich functionality |
| API calls | Python | Libraries available |

## Next Steps
- Build Python stream filters
- Practice hybrid pipelines
- Compare performance: CLI vs pandas
- Study streaming libraries (ijson, streamz)
