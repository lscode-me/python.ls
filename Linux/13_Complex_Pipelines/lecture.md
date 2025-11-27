# Complex Pipelines: Map/Reduce, Staging, Checkpoints, Orchestration

## Overview
Build production-grade pipelines with map/reduce patterns, temporary staging, checkpoints for recovery, and Makefile orchestration.

## Map/Reduce Patterns

### Split-Process-Merge
```bash
#!/bin/bash
# Split large file
split -l 10000 -d huge.csv chunk_

# Map: Process each chunk
for chunk in chunk_*; do
    mlr --csv stats1 -a sum -f amount "$chunk" > "$chunk.result" &
done
wait

# Reduce: Merge results
cat chunk_*.result > final_result.csv
rm chunk_*
```

## Staging with mktemp

### Multi-Stage Pipeline
```bash
#!/bin/bash
set -euo pipefail

STAGE1=$(mktemp)
STAGE2=$(mktemp)
STAGE3=$(mktemp)

trap 'rm -f "$STAGE1" "$STAGE2" "$STAGE3"' EXIT

# Stage 1: Extract
curl -s "https://api.example.com/data" | jq -c '.[]' > "$STAGE1"

# Stage 2: Transform
cat "$STAGE1" | jq -c 'select(.active == true)' > "$STAGE2"

# Stage 3: Load
cat "$STAGE2" | python3 load_db.py

echo "Pipeline complete"
```

## Checkpoints for Resumability

### Checkpoint Pattern
```bash
#!/bin/bash
CHECKPOINT_DIR=".checkpoints"
mkdir -p "$CHECKPOINT_DIR"

# Check if step completed
if [ ! -f "$CHECKPOINT_DIR/step1.done" ]; then
    echo "Running step 1..."
    ./step1.sh > output1.csv
    touch "$CHECKPOINT_DIR/step1.done"
else
    echo "Step 1 already complete"
fi

if [ ! -f "$CHECKPOINT_DIR/step2.done" ]; then
    echo "Running step 2..."
    ./step2.sh < output1.csv > output2.csv
    touch "$CHECKPOINT_DIR/step2.done"
else
    echo "Step 2 already complete"
fi

# Reset checkpoints
# rm -rf "$CHECKPOINT_DIR"
```

## Makefile for Orchestration

### Basic Makefile
```makefile
.PHONY: all clean

all: report.md

raw_data.csv:
	curl -s "https://api.example.com/data" | jq -r '.[]' > raw_data.csv

clean_data.csv: raw_data.csv
	grep -v "^#" raw_data.csv | mlr --csv filter '$$status == "active"' > clean_data.csv

aggregated.csv: clean_data.csv
	mlr --csv stats1 -a sum,count -f amount -g category clean_data.csv > aggregated.csv

report.md: aggregated.csv
	./generate_report.sh aggregated.csv > report.md

clean:
	rm -f raw_data.csv clean_data.csv aggregated.csv report.md
```

### Run with Make
```bash
# Run entire pipeline
make

# Run specific target
make aggregated.csv

# Clean all outputs
make clean

# Parallel execution
make -j4
```

## Reproducibility Patterns

### Versioned Data
```bash
# Include date in output
OUTPUT="output_$(date +%Y%m%d).csv"
./pipeline.sh > "$OUTPUT"
```

### Logging
```bash
#!/bin/bash
LOGFILE="pipeline_$(date +%Y%m%d_%H%M%S).log"

exec 1> >(tee -a "$LOGFILE")
exec 2>&1

echo "Starting pipeline at $(date)"
./step1.sh
./step2.sh
echo "Pipeline complete at $(date)"
```

### Dependency Tracking
```makefile
# Make automatically tracks dependencies
report.md: data.csv template.md
	./generate_report.sh data.csv template.md > report.md

# If data.csv changes, report.md is regenerated
```

## Production Pipeline Example

```bash
#!/bin/bash
set -euo pipefail

# Configuration
DATA_DIR="data"
CHECKPOINT_DIR=".checkpoints"
OUTPUT="report_$(date +%Y%m%d).md"

mkdir -p "$DATA_DIR" "$CHECKPOINT_DIR"

# Stage 1: Extract
if [ ! -f "$CHECKPOINT_DIR/extract.done" ]; then
    echo "Extracting data..."
    curl -s "https://api.example.com/users" | \
        jq -c '.[]' > "$DATA_DIR/users.jsonl"
    touch "$CHECKPOINT_DIR/extract.done"
fi

# Stage 2: Transform
if [ ! -f "$CHECKPOINT_DIR/transform.done" ]; then
    echo "Transforming data..."
    cat "$DATA_DIR/users.jsonl" | \
        jq -r '[.id, .name, .email] | @csv' > "$DATA_DIR/users.csv"
    touch "$CHECKPOINT_DIR/transform.done"
fi

# Stage 3: Analyze
if [ ! -f "$CHECKPOINT_DIR/analyze.done" ]; then
    echo "Analyzing data..."
    mlr --csv stats1 -a count -g country "$DATA_DIR/users.csv" > "$DATA_DIR/stats.csv"
    touch "$CHECKPOINT_DIR/analyze.done"
fi

# Stage 4: Report
echo "Generating report..."
./generate_report.sh "$DATA_DIR/stats.csv" > "$OUTPUT"

echo "Pipeline complete: $OUTPUT"
```

## Best Practices

1. **Use Make for dependencies**: Automatic incremental builds
2. **Add checkpoints**: Resume from failures
3. **Stage with temp files**: Debug intermediate steps
4. **Log everything**: Track execution and errors
5. **Version outputs**: Date-stamped filenames
6. **Clean up temp files**: Use trap or Make clean
7. **Document dependencies**: README or Makefile comments

## Summary

| Pattern | Tool | Purpose |
|---------|------|---------|
| Map/Reduce | split + parallel | Process large files |
| Staging | mktemp | Intermediate outputs |
| Checkpoints | touch files | Resume from failure |
| Orchestration | Makefile | Dependency management |

## Next Steps
- Build production pipeline
- Study Make patterns
- Implement error recovery
- Explore workflow engines (Airflow, Luigi)
