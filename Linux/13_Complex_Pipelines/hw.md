# Complex Pipelines: Map/Reduce, Staging, Checkpoints, Orchestration - Homework

## Assignment 1: Basic Split-Map-Reduce
Implement classic map/reduce pattern on a large CSV file.
- Generate test data:
  ```bash
  seq 1 100000 | awk '{print $1 % 100 "," rand()*1000}' > data.csv
  ```
- Implementation:
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Split
  split -l 10000 -d data.csv chunk_
  
  # Map (parallel)
  for chunk in chunk_*; do
      awk -F',' '{sum[$1] += $2} END {for (k in sum) print k","sum[k]}' "$chunk" > "$chunk.result" &
  done
  wait
  
  # Reduce (merge)
  awk -F',' '{sum[$1] += $2} END {for (k in sum) print k","sum[k]}' chunk_*.result > final.csv
  
  # Cleanup
  rm chunk_*
  ```
- Requirement: Parallelize map phase

## Assignment 2: Makefile-Based Pipeline
Create a data pipeline orchestrated by Make.
- File: `Makefile`
  ```makefile
  .PHONY: all clean
  
  # Final target
  all: report.md
  
  # Download raw data
  raw_data.json:
  	curl -s "https://jsonplaceholder.typicode.com/users" > raw_data.json
  
  # Transform to CSV
  users.csv: raw_data.json
  	jq -r '.[] | [.id, .name, .email, .address.city] | @csv' raw_data.json > users.csv
  
  # Aggregate statistics
  stats.csv: users.csv
  	echo "city,count" > stats.csv
  	tail -n +1 users.csv | cut -d',' -f4 | sort | uniq -c | \
  	  awk '{print $$2","$$1}' >> stats.csv
  
  # Generate report
  report.md: stats.csv
  	echo "# User Statistics" > report.md
  	echo "" >> report.md
  	echo "Generated: $$(date)" >> report.md
  	echo "" >> report.md
  	echo "## Users by City" >> report.md
  	echo "" >> report.md
  	echo "| City | Count |" >> report.md
  	echo "|------|-------|" >> report.md
  	tail -n +2 stats.csv | awk -F',' '{printf "| %s | %s |\n", $$1, $$2}' >> report.md
  
  # Cleanup
  clean:
  	rm -f raw_data.json users.csv stats.csv report.md
  ```
- Usage: `make` (builds all), `make clean` (removes outputs)
- Test: Modify `raw_data.json`, run `make` (should rebuild only necessary targets)

## Assignment 3: Checkpoint-Based Resumable Pipeline
Build pipeline that can resume after failure.
- Script (`resumable_pipeline.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  CHECKPOINT_DIR=".checkpoints"
  DATA_DIR="data"
  
  mkdir -p "$CHECKPOINT_DIR" "$DATA_DIR"
  
  # Stage 1: Extract
  if [ ! -f "$CHECKPOINT_DIR/extract.done" ]; then
      echo "Stage 1: Extracting data..."
      curl -s "https://jsonplaceholder.typicode.com/posts" > "$DATA_DIR/posts.json"
      curl -s "https://jsonplaceholder.typicode.com/comments" > "$DATA_DIR/comments.json"
      touch "$CHECKPOINT_DIR/extract.done"
      echo "  ✓ Extract complete"
  else
      echo "Stage 1: Extract (cached)"
  fi
  
  # Stage 2: Transform
  if [ ! -f "$CHECKPOINT_DIR/transform.done" ]; then
      echo "Stage 2: Transforming data..."
      jq -c '.[]' "$DATA_DIR/posts.json" > "$DATA_DIR/posts.jsonl"
      jq -c '.[]' "$DATA_DIR/comments.json" > "$DATA_DIR/comments.jsonl"
      touch "$CHECKPOINT_DIR/transform.done"
      echo "  ✓ Transform complete"
  else
      echo "Stage 2: Transform (cached)"
  fi
  
  # Stage 3: Analyze
  if [ ! -f "$CHECKPOINT_DIR/analyze.done" ]; then
      echo "Stage 3: Analyzing data..."
      jq -r '.userId' "$DATA_DIR/posts.jsonl" | sort | uniq -c | \
        awk '{print $2","$1}' > "$DATA_DIR/posts_per_user.csv"
      touch "$CHECKPOINT_DIR/analyze.done"
      echo "  ✓ Analyze complete"
  else
      echo "Stage 3: Analyze (cached)"
  fi
  
  # Stage 4: Report
  echo "Stage 4: Generating report..."
  {
    echo "# Analysis Report"
    echo ""
    echo "Generated: $(date)"
    echo ""
    echo "## Top 5 Users by Posts"
    echo ""
    echo "| User ID | Post Count |"
    echo "|---------|------------|"
    sort -t',' -k2,2nr "$DATA_DIR/posts_per_user.csv" | head -5 | \
      awk -F',' '{printf "| %s | %s |\n", $1, $2}'
  } > report.md
  
  echo "  ✓ Report generated: report.md"
  echo ""
  echo "Pipeline complete!"
  echo "To reset: rm -rf $CHECKPOINT_DIR"
  ```
- Test failure recovery:
  1. Add `exit 1` in stage 2
  2. Run script (fails at stage 2)
  3. Remove `exit 1`
  4. Run again (skips stage 1, resumes at stage 2)

## Assignment 4: Staging with Temporary Files
Create pipeline with explicit staging areas.
- Script (`staged_pipeline.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Setup staging areas
  STAGE1=$(mktemp -d)
  STAGE2=$(mktemp -d)
  STAGE3=$(mktemp -d)
  FINAL="output"
  
  mkdir -p "$FINAL"
  
  # Cleanup on exit
  trap 'rm -rf "$STAGE1" "$STAGE2" "$STAGE3"' EXIT
  
  echo "Stage 1: Extract → $STAGE1"
  curl -s "https://jsonplaceholder.typicode.com/users" > "$STAGE1/users.json"
  ls -lh "$STAGE1"
  
  echo ""
  echo "Stage 2: Transform → $STAGE2"
  jq -c '.[]' "$STAGE1/users.json" > "$STAGE2/users.jsonl"
  jq -c '. | {id, name, email, company: .company.name}' "$STAGE2/users.jsonl" > "$STAGE2/users_clean.jsonl"
  ls -lh "$STAGE2"
  
  echo ""
  echo "Stage 3: Enrich → $STAGE3"
  cat "$STAGE2/users_clean.jsonl" | \
    python3 -c "
  import sys, json
  for line in sys.stdin:
      user = json.loads(line)
      user['name_length'] = len(user['name'])
      user['email_domain'] = user['email'].split('@')[1]
      print(json.dumps(user))
  " > "$STAGE3/users_enriched.jsonl"
  ls -lh "$STAGE3"
  
  echo ""
  echo "Stage 4: Load → $FINAL"
  jq -r '[.id, .name, .email_domain, .company] | @csv' "$STAGE3/users_enriched.jsonl" > "$FINAL/users_final.csv"
  ls -lh "$FINAL"
  
  echo ""
  echo "Pipeline complete! Output in $FINAL/"
  ```

## Assignment 5: Parallel Processing with GNU Parallel
Parallelize data processing using GNU parallel.
- Script (`parallel_pipeline.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Generate test files
  mkdir -p input
  for i in {1..20}; do
    seq $(( (i-1)*1000 + 1 )) $(( i*1000 )) > input/data_$i.txt
  done
  
  echo "Processing 20 files in parallel..."
  
  # Process all files in parallel (4 at a time)
  ls input/*.txt | parallel -j 4 --bar \
    'wc -l {} | awk "{print \$1}" > {}.count'
  
  echo ""
  echo "Aggregating results..."
  
  # Sum all counts
  awk '{sum += $1} END {print "Total lines:", sum}' input/*.count
  
  # Cleanup
  rm -rf input
  ```
- Extension: Add processing step (e.g., filter, transform)

## Assignment 6: Dependency Tracking with Make
Create complex Makefile with multiple dependencies.
- File: `Makefile`
  ```makefile
  .PHONY: all clean test
  
  # Variables
  DATA_URL = https://jsonplaceholder.typicode.com
  
  # Final report depends on all analyses
  all: report.md
  
  # Download raw data (multiple sources)
  raw/users.json:
  	mkdir -p raw
  	curl -s "$(DATA_URL)/users" > raw/users.json
  
  raw/posts.json:
  	mkdir -p raw
  	curl -s "$(DATA_URL)/posts" > raw/posts.json
  
  raw/comments.json:
  	mkdir -p raw
  	curl -s "$(DATA_URL)/comments" > raw/comments.json
  
  # Transform to JSONL
  processed/%.jsonl: raw/%.json
  	mkdir -p processed
  	jq -c '.[]' $< > $@
  
  # Analysis: users
  analysis/user_stats.csv: processed/users.jsonl
  	mkdir -p analysis
  	jq -r '[.id, .name, .email] | @csv' $< > $@
  
  # Analysis: posts per user
  analysis/posts_per_user.csv: processed/posts.jsonl
  	mkdir -p analysis
  	jq -r '.userId' $< | sort | uniq -c | \
  	  awk '{print $$2","$$1}' > $@
  
  # Analysis: comments per post
  analysis/comments_per_post.csv: processed/comments.jsonl
  	mkdir -p analysis
  	jq -r '.postId' $< | sort | uniq -c | \
  	  awk '{print $$2","$$1}' > $@
  
  # Final report depends on all analyses
  report.md: analysis/user_stats.csv analysis/posts_per_user.csv analysis/comments_per_post.csv
  	./generate_report.sh
  
  # Test target
  test: all
  	@echo "Testing report exists..."
  	@test -f report.md && echo "✓ Report found" || echo "✗ Report missing"
  
  # Clean all generated files
  clean:
  	rm -rf raw processed analysis report.md
  
  # Parallel build
  parallel:
  	$(MAKE) -j4 all
  ```

## Assignment 7: Logging and Monitoring
Add comprehensive logging to pipeline.
- Script (`logged_pipeline.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Setup logging
  LOG_DIR="logs"
  LOG_FILE="$LOG_DIR/pipeline_$(date +%Y%m%d_%H%M%S).log"
  mkdir -p "$LOG_DIR"
  
  # Logging functions
  log() {
      echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
  }
  
  log_stage() {
      echo "" | tee -a "$LOG_FILE"
      echo "========================================" | tee -a "$LOG_FILE"
      log "STAGE: $*"
      echo "========================================" | tee -a "$LOG_FILE"
  }
  
  log_error() {
      log "ERROR: $*" >&2
  }
  
  # Error handler
  error_handler() {
      log_error "Pipeline failed at line $1"
      exit 1
  }
  trap 'error_handler $LINENO' ERR
  
  # Cleanup
  cleanup() {
      log "Cleaning up temporary files..."
  }
  trap cleanup EXIT
  
  # Pipeline stages
  log_stage "1: Extract"
  log "Downloading data from API..."
  curl -s "https://jsonplaceholder.typicode.com/users" > users.json
  log "Downloaded $(wc -l < users.json) lines"
  
  log_stage "2: Transform"
  log "Converting to JSONL..."
  jq -c '.[]' users.json > users.jsonl
  log "Converted to $(wc -l < users.jsonl) records"
  
  log_stage "3: Analyze"
  log "Extracting domains..."
  jq -r '.email' users.jsonl | sed 's/.*@//' | sort | uniq -c | sort -rn > domains.txt
  log "Found $(wc -l < domains.txt) unique domains"
  
  log_stage "Pipeline Complete"
  log "Log file: $LOG_FILE"
  ```

## Assignment 8: Reproducible Pipeline with Versioning
Create pipeline that versions all outputs.
- Script (`versioned_pipeline.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Version based on date
  VERSION=$(date +%Y%m%d_%H%M%S)
  OUTPUT_DIR="output_$VERSION"
  
  mkdir -p "$OUTPUT_DIR"
  
  echo "Pipeline version: $VERSION"
  echo "Output directory: $OUTPUT_DIR"
  
  # Record metadata
  {
    echo "version: $VERSION"
    echo "timestamp: $(date -Iseconds)"
    echo "hostname: $(hostname)"
    echo "user: $(whoami)"
    echo "git_commit: $(git rev-parse HEAD 2>/dev/null || echo 'N/A')"
  } > "$OUTPUT_DIR/metadata.txt"
  
  # Run pipeline
  echo "Extracting..."
  curl -s "https://jsonplaceholder.typicode.com/users" > "$OUTPUT_DIR/users.json"
  
  echo "Processing..."
  jq -c '.[]' "$OUTPUT_DIR/users.json" > "$OUTPUT_DIR/users.jsonl"
  
  echo "Analyzing..."
  jq -r '.email' "$OUTPUT_DIR/users.jsonl" | \
    sed 's/.*@//' | sort | uniq -c | sort -rn > "$OUTPUT_DIR/domains.txt"
  
  # Create symlink to latest
  ln -sfn "$OUTPUT_DIR" output_latest
  
  echo ""
  echo "Pipeline complete!"
  echo "Results: $OUTPUT_DIR"
  echo "Latest: output_latest -> $OUTPUT_DIR"
  ```

## Assignment 9: Error Recovery and Retry
Implement robust error handling with retries.
- Script (`retry_pipeline.sh`):
  ```bash
  #!/bin/bash
  set -uo pipefail  # Note: no -e, we handle errors manually
  
  MAX_RETRIES=3
  RETRY_DELAY=2
  
  # Retry function
  retry() {
      local max_attempts=$MAX_RETRIES
      local delay=$RETRY_DELAY
      local attempt=1
      
      while [ $attempt -le $max_attempts ]; do
          echo "Attempt $attempt/$max_attempts: $*"
          
          if "$@"; then
              return 0
          fi
          
          local exit_code=$?
          
          if [ $attempt -lt $max_attempts ]; then
              echo "Failed with exit code $exit_code, retrying in ${delay}s..."
              sleep $delay
              delay=$((delay * 2))  # Exponential backoff
          fi
          
          attempt=$((attempt + 1))
      done
      
      echo "All attempts failed"
      return 1
  }
  
  # Fetch with retry
  fetch_data() {
      local url=$1
      local output=$2
      retry curl -f -s "$url" -o "$output"
  }
  
  # Pipeline
  echo "Fetching data with automatic retry..."
  
  if fetch_data "https://jsonplaceholder.typicode.com/users" "users.json"; then
      echo "✓ Data fetched successfully"
      jq -c '.[]' users.json > users.jsonl
      echo "✓ Processing complete"
  else
      echo "✗ Failed to fetch data after $MAX_RETRIES attempts"
      exit 1
  fi
  ```

## Assignment 10: Complete Production Pipeline
Build a production-ready pipeline incorporating all concepts.
- Features required:
  - Makefile orchestration
  - Checkpoint-based resumability
  - Logging with timestamps
  - Error handling and retry
  - Temporary staging areas
  - Parallel processing
  - Versioned outputs
  - Progress monitoring
  - Cleanup on exit
- See bonus challenge for full implementation

## Bonus Challenges

### Bonus 1: Incremental Processing
Build pipeline that only processes new/changed data.
- Track file checksums
- Skip processing if checksum unchanged
- Update only necessary outputs
- Example:
  ```bash
  # Check if input changed
  NEW_HASH=$(md5sum input.csv | cut -d' ' -f1)
  OLD_HASH=$(cat .last_hash 2>/dev/null || echo "")
  
  if [ "$NEW_HASH" != "$OLD_HASH" ]; then
      echo "Input changed, processing..."
      process_data input.csv
      echo "$NEW_HASH" > .last_hash
  else
      echo "Input unchanged, skipping"
  fi
  ```

### Bonus 2: Distributed Pipeline
Distribute work across multiple machines.
- Use SSH to run workers on remote hosts
- Aggregate results centrally
- Example architecture:
  ```bash
  # Split work
  split -n l/4 data.csv chunk_
  
  # Distribute to workers
  scp chunk_aa worker1:/tmp/
  scp chunk_ab worker2:/tmp/
  scp chunk_ac worker3:/tmp/
  scp chunk_ad worker4:/tmp/
  
  # Process remotely
  ssh worker1 'process /tmp/chunk_aa > /tmp/result_aa' &
  ssh worker2 'process /tmp/chunk_ab > /tmp/result_ab' &
  ssh worker3 'process /tmp/chunk_ac > /tmp/result_ac' &
  ssh worker4 'process /tmp/chunk_ad > /tmp/result_ad' &
  wait
  
  # Fetch results
  scp worker{1..4}:/tmp/result_* .
  
  # Aggregate
  cat result_* > final_result.txt
  ```

### Bonus 3: Pipeline Performance Dashboard
Create real-time monitoring dashboard.
- Track metrics:
  - Current stage
  - Progress percentage
  - Processing rate (records/sec)
  - ETA
  - Memory usage
  - CPU usage
- Output to JSON for web dashboard
- Use: `watch`, `pv`, `iostat`, `vmstat`

### Bonus 4: Pipeline DAG Visualization
Generate visual representation of pipeline dependencies.
- Parse Makefile
- Generate GraphViz DOT format
- Create PNG/SVG diagram
- Example:
  ```bash
  # Extract dependencies from Makefile
  make -Bnd | grep -E '^ *Must remake target' | \
    awk '{print $4}' > targets.txt
  
  # Generate DOT file
  # ... (custom script)
  
  # Render
  dot -Tpng pipeline.dot > pipeline.png
  ```

### Bonus 5: Complete Enterprise ETL
Build full-featured production pipeline:

**File**: `enterprise_pipeline.sh`
```bash
#!/bin/bash
set -euo pipefail

# Configuration
CONFIG_FILE="${CONFIG_FILE:-.env}"
CHECKPOINT_DIR=".checkpoints"
LOG_DIR="logs"
DATA_DIR="data"
OUTPUT_DIR="output"
VERSION=$(date +%Y%m%d_%H%M%S)

# Setup
mkdir -p "$CHECKPOINT_DIR" "$LOG_DIR" "$DATA_DIR" "$OUTPUT_DIR"

# Load configuration
if [ -f "$CONFIG_FILE" ]; then
    set -a
    source "$CONFIG_FILE"
    set +a
fi

# Logging
LOG_FILE="$LOG_DIR/pipeline_$VERSION.log"
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Cleanup
cleanup() {
    log "Cleanup completed"
}
trap cleanup EXIT

# Error handling
error_handler() {
    log "ERROR at line $1"
    exit 1
}
trap 'error_handler $LINENO' ERR

# Stages...
# (implement full ETL with all best practices)
```

## Submission Guidelines

### Required Components
1. **All scripts** with proper documentation
2. **Makefile** with dependencies clearly defined
3. **README.md** explaining:
   - Pipeline architecture
   - How to run
   - Dependencies
   - Configuration options
   - Troubleshooting
4. **Sample outputs** from each stage
5. **Performance benchmarks**

### Testing Requirements
- [ ] Pipeline runs successfully end-to-end
- [ ] Handles interruption gracefully
- [ ] Resumes from checkpoints correctly
- [ ] Makefile dependencies work (partial rebuilds)
- [ ] Error handling catches failures
- [ ] Cleanup removes temporary files
- [ ] Logging captures all stages
- [ ] Works with various data sizes

### Documentation Template
```markdown
# Pipeline Name

## Architecture
[Diagram or description of pipeline stages]

## Dependencies
- bash 4.0+
- jq
- curl
- make
- GNU parallel

## Configuration
Copy `.env.example` to `.env` and configure:
- `API_URL`: Source API endpoint
- `MAX_RETRIES`: Number of retry attempts
- `LOG_LEVEL`: Logging verbosity

## Usage
\`\`\`bash
# Full pipeline
make

# Clean outputs
make clean

# Resume from checkpoint
./pipeline.sh

# Reset checkpoints
rm -rf .checkpoints
\`\`\`

## Stages
1. **Extract**: Download data from API
2. **Transform**: Convert formats and clean
3. **Analyze**: Calculate statistics
4. **Load**: Generate reports

## Performance
- Processing rate: 10,000 records/sec
- Memory usage: < 100MB
- Parallelism: 4 workers

## Troubleshooting
...
```

### Performance Metrics to Report
- Total execution time
- Time per stage
- Throughput (records/sec)
- Memory usage (peak RSS)
- CPU utilization
- I/O statistics

### Code Quality Checklist
- [ ] Proper error handling (`set -euo pipefail`)
- [ ] All variables quoted (`"$VAR"`)
- [ ] Cleanup with `trap EXIT`
- [ ] Logging with timestamps
- [ ] Progress indicators
- [ ] Meaningful error messages
- [ ] Comments for complex logic
- [ ] Consistent naming conventions
