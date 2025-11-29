# Homework: Bash as Glue - Error Handling & Configuration

## Assignment 1: Basic trap with EXIT Cleanup
Create script that cleans up temporary files on exit.
- Script (`cleanup_demo.sh`):
  ```bash
  #!/bin/bash
  set -e
  
  TMPFILE=$(mktemp)
  trap 'echo "Cleaning up..."; rm -f "$TMPFILE"' EXIT
  
  echo "Working with $TMPFILE"
  echo "Some data" > "$TMPFILE"
  cat "$TMPFILE"
  
  # Cleanup happens automatically on exit
  ```
- Test cases:
  1. Normal exit: `./cleanup_demo.sh`
  2. Error exit: Add `exit 1` before end
  3. Interrupt: Run script and press Ctrl+C
- Verify: Temp file is always deleted

## Assignment 2: Load Configuration from .env
Create script that loads environment variables from `.env` file.
- Create `.env`:
  ```
  DATABASE_URL=postgres://localhost/mydb
  API_KEY=secret_key_12345
  LOG_LEVEL=DEBUG
  MAX_RETRIES=3
  ```
- Script (`load_env.sh`):
  ```bash
  #!/bin/bash
  
  if [ -f .env ]; then
      echo "Loading environment from .env..."
      set -a  # Auto-export all variables
      source .env
      set +a
  else
      echo "Error: .env file not found"
      exit 1
  fi
  
  echo "Database: $DATABASE_URL"
  echo "Log level: $LOG_LEVEL"
  echo "Max retries: $MAX_RETRIES"
  ```
- Requirement: Variables must be available to child processes

## Assignment 3: Safe Temporary File Management
Demonstrate proper mktemp usage.
- Script showing different mktemp modes:
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Temporary file
  TMPFILE=$(mktemp)
  echo "Created temp file: $TMPFILE"
  
  # Temporary directory
  TMPDIR=$(mktemp -d)
  echo "Created temp directory: $TMPDIR"
  
  # Named pattern
  LOGFILE=$(mktemp /tmp/myapp.XXXXXX.log)
  echo "Created log file: $LOGFILE"
  
  # Cleanup all
  trap 'rm -f "$TMPFILE" "$LOGFILE"; rm -rf "$TMPDIR"' EXIT
  
  # Use files...
  echo "data" > "$TMPFILE"
  touch "$TMPDIR/file1.txt"
  echo "log entry" > "$LOGFILE"
  
  echo "Files will be cleaned up on exit"
  ```

## Assignment 4: Comprehensive Error Handling
Build script with set -euo pipefail and proper error handling.
- Script (`robust.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Error handler
  error_handler() {
      echo "Error occurred in script at line $1" >&2
      exit 1
  }
  trap 'error_handler $LINENO' ERR
  
  # Cleanup handler
  cleanup() {
      echo "Performing cleanup..."
      rm -f /tmp/work_*
  }
  trap cleanup EXIT
  
  # Your code here
  echo "Starting process..."
  
  # This will fail if file doesn't exist
  cat nonexistent_file.txt
  
  echo "This line won't be reached"
  ```
- Test: Run and verify error handling works

## Assignment 5: Multi-Stage Pipeline with Staging
Create pipeline with temporary staging between stages.
- Script (`pipeline.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Setup temp files for staging
  STAGE1=$(mktemp)
  STAGE2=$(mktemp)
  STAGE3=$(mktemp)
  
  trap 'rm -f "$STAGE1" "$STAGE2" "$STAGE3"' EXIT
  
  echo "Stage 1: Extract"
  curl -s "https://jsonplaceholder.typicode.com/users" > "$STAGE1"
  
  echo "Stage 2: Transform"
  jq -c '.[] | {id, name, email}' "$STAGE1" > "$STAGE2"
  
  echo "Stage 3: Load"
  jq -r '[.id, .name, .email] | @csv' "$STAGE2" > "$STAGE3"
  
  echo "Final output:"
  cat "$STAGE3"
  ```

## Assignment 6: Error Handling with trap ERR
Demonstrate ERR trap for error recovery.
- Script (`error_trap.sh`):
  ```bash
  #!/bin/bash
  set -E  # ERR trap inherited by functions
  
  error_count=0
  
  handle_error() {
      error_count=$((error_count + 1))
      echo "Error #$error_count at line $1" >&2
      
      if [ $error_count -ge 3 ]; then
          echo "Too many errors, aborting"
          exit 1
      fi
  }
  
  trap 'handle_error $LINENO' ERR
  
  # Test with failing commands
  false || true  # This won't trigger trap (||)
  
  set -e
  false  # This will trigger trap
  
  echo "Script continues..."
  ```

## Assignment 7: Temporary Directory Workflow
Build workflow using temp directory for intermediate files.
- Script (`temp_workflow.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  WORKDIR=$(mktemp -d)
  trap 'echo "Cleaning up $WORKDIR"; rm -rf "$WORKDIR"' EXIT
  
  echo "Working directory: $WORKDIR"
  cd "$WORKDIR"
  
  # Download multiple files
  for id in {1..5}; do
      curl -s "https://jsonplaceholder.typicode.com/users/$id" > "user_$id.json"
  done
  
  # Process files
  jq -s '.' user_*.json > combined.json
  
  # Extract result
  jq -r '.[] | .name' combined.json > names.txt
  
  # Copy result out before cleanup
  cp names.txt "$OLDPWD/output.txt"
  
  echo "Results saved to output.txt"
  ```

## Assignment 8: Configuration Validation
Create script that validates configuration before proceeding.
- Script (`validate_config.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Load config
  if [ ! -f .env ]; then
      echo "Error: .env file not found" >&2
      exit 1
  fi
  
  set -a
  source .env
  set +a
  
  # Validate required variables
  required_vars=("DATABASE_URL" "API_KEY" "LOG_LEVEL")
  
  for var in "${required_vars[@]}"; do
      if [ -z "${!var:-}" ]; then
          echo "Error: Required variable $var is not set" >&2
          exit 1
      fi
  done
  
  # Validate values
  if [[ ! "$LOG_LEVEL" =~ ^(DEBUG|INFO|WARN|ERROR)$ ]]; then
      echo "Error: Invalid LOG_LEVEL: $LOG_LEVEL" >&2
      exit 1
  fi
  
  echo "Configuration validated successfully"
  echo "DATABASE_URL: $DATABASE_URL"
  echo "LOG_LEVEL: $LOG_LEVEL"
  ```

## Assignment 9: Robust Script Template
Create a production-ready script template with all best practices.
- Template (`template.sh`):
  ```bash
  #!/bin/bash
  
  # Strict error handling
  set -euo pipefail
  
  # Script metadata
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"
  
  # Configuration
  CONFIG_FILE="${CONFIG_FILE:-.env}"
  
  # Logging
  log() {
      echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >&2
  }
  
  error() {
      log "ERROR: $*"
      exit 1
  }
  
  # Load configuration
  if [ -f "$CONFIG_FILE" ]; then
      log "Loading configuration from $CONFIG_FILE"
      set -a
      source "$CONFIG_FILE"
      set +a
  fi
  
  # Setup temp files
  TMPDIR=$(mktemp -d)
  
  # Cleanup function
  cleanup() {
      local exit_code=$?
      log "Cleaning up..."
      rm -rf "$TMPDIR"
      exit $exit_code
  }
  trap cleanup EXIT INT TERM
  
  # Error handler
  error_handler() {
      error "Failed at line $1"
  }
  trap 'error_handler $LINENO' ERR
  
  # Main logic
  main() {
      log "Starting $SCRIPT_NAME"
      
      # Your code here
      log "Working directory: $TMPDIR"
      
      log "Completed successfully"
  }
  
  # Run main
  main "$@"
  ```

## Assignment 10: Signal Handling
Implement proper signal handling for graceful shutdown.
- Script (`signal_handling.sh`):
  ```bash
  #!/bin/bash
  
  # Shared state
  RUNNING=true
  
  # Cleanup on exit
  cleanup() {
      echo ""
      echo "Shutting down gracefully..."
      RUNNING=false
      # Wait for background jobs
      wait
      echo "Cleanup complete"
  }
  
  # Handle signals
  trap cleanup INT TERM
  
  # Main loop
  echo "Running... Press Ctrl+C to stop"
  count=0
  while $RUNNING; do
      count=$((count + 1))
      echo "Iteration $count"
      sleep 1
  done
  
  echo "Exited cleanly"
  ```
- Test: Run and interrupt with Ctrl+C, verify clean shutdown

## Bonus Challenges

### Bonus 1: Retry Logic with Exponential Backoff
Implement command retry with exponential backoff.
- Script (`retry.sh`):
  ```bash
  #!/bin/bash
  
  retry_with_backoff() {
      local max_attempts=5
      local timeout=1
      local attempt=1
      local exit_code=0
      
      while [ $attempt -le $max_attempts ]; do
          echo "Attempt $attempt/$max_attempts"
          
          if "$@"; then
              return 0
          fi
          
          exit_code=$?
          
          if [ $attempt -lt $max_attempts ]; then
              echo "Command failed, retrying in ${timeout}s..."
              sleep $timeout
              timeout=$((timeout * 2))
          fi
          
          attempt=$((attempt + 1))
      done
      
      echo "Command failed after $max_attempts attempts"
      return $exit_code
  }
  
  # Usage
  retry_with_backoff curl -f "https://unreliable-api.com/data"
  ```

### Bonus 2: Configuration with Defaults
Build configuration system with default values.
- Script (`config_defaults.sh`):
  ```bash
  #!/bin/bash
  
  # Load .env if exists
  if [ -f .env ]; then
      set -a
      source .env
      set +a
  fi
  
  # Set defaults for missing variables
  DATABASE_URL="${DATABASE_URL:-postgres://localhost/defaultdb}"
  API_KEY="${API_KEY:-}"
  LOG_LEVEL="${LOG_LEVEL:-INFO}"
  MAX_RETRIES="${MAX_RETRIES:-3}"
  TIMEOUT="${TIMEOUT:-30}"
  
  # Validate critical variables
  if [ -z "$API_KEY" ]; then
      echo "Warning: API_KEY not set" >&2
  fi
  
  echo "Configuration:"
  echo "  DATABASE_URL: $DATABASE_URL"
  echo "  LOG_LEVEL: $LOG_LEVEL"
  echo "  MAX_RETRIES: $MAX_RETRIES"
  echo "  TIMEOUT: $TIMEOUT"
  ```

### Bonus 3: Logging Framework
Create comprehensive logging system.
- Script (`logging.sh`):
  ```bash
  #!/bin/bash
  
  # Log levels
  LOG_LEVEL_DEBUG=0
  LOG_LEVEL_INFO=1
  LOG_LEVEL_WARN=2
  LOG_LEVEL_ERROR=3
  
  # Current log level
  CURRENT_LOG_LEVEL=${LOG_LEVEL:-$LOG_LEVEL_INFO}
  
  # Log file
  LOG_FILE="${LOG_FILE:-app.log}"
  
  # Logging functions
  log_debug() {
      [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_DEBUG ] && \
          echo "[$(date +'%Y-%m-%d %H:%M:%S')] [DEBUG] $*" | tee -a "$LOG_FILE"
  }
  
  log_info() {
      [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_INFO ] && \
          echo "[$(date +'%Y-%m-%d %H:%M:%S')] [INFO] $*" | tee -a "$LOG_FILE"
  }
  
  log_warn() {
      [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_WARN ] && \
          echo "[$(date +'%Y-%m-%d %H:%M:%S')] [WARN] $*" | tee -a "$LOG_FILE" >&2
  }
  
  log_error() {
      [ $CURRENT_LOG_LEVEL -le $LOG_LEVEL_ERROR ] && \
          echo "[$(date +'%Y-%m-%d %H:%M:%S')] [ERROR] $*" | tee -a "$LOG_FILE" >&2
  }
  
  # Usage
  log_debug "This is debug"
  log_info "This is info"
  log_warn "This is warning"
  log_error "This is error"
  ```

### Bonus 4: Dependency Checker
Script that checks for required commands before running.
- Script (`check_deps.sh`):
  ```bash
  #!/bin/bash
  set -euo pipefail
  
  # Required commands
  REQUIRED_CMDS=("curl" "jq" "awk" "sed" "grep")
  
  # Optional commands
  OPTIONAL_CMDS=("pv" "parallel" "mlr")
  
  # Check if command exists
  command_exists() {
      command -v "$1" >/dev/null 2>&1
  }
  
  # Check required dependencies
  echo "Checking required dependencies..."
  missing_required=()
  for cmd in "${REQUIRED_CMDS[@]}"; do
      if command_exists "$cmd"; then
          echo "  ✓ $cmd"
      else
          echo "  ✗ $cmd (MISSING)"
          missing_required+=("$cmd")
      fi
  done
  
  # Check optional dependencies
  echo ""
  echo "Checking optional dependencies..."
  for cmd in "${OPTIONAL_CMDS[@]}"; do
      if command_exists "$cmd"; then
          echo "  ✓ $cmd"
      else
          echo "  ⚠ $cmd (optional, not installed)"
      fi
  done
  
  # Fail if required dependencies missing
  if [ ${#missing_required[@]} -gt 0 ]; then
      echo ""
      echo "Error: Missing required commands: ${missing_required[*]}"
      echo "Please install them before running this script"
      exit 1
  fi
  
  echo ""
  echo "All required dependencies satisfied"
  ```

### Bonus 5: Complete ETL Script with Best Practices
Build production-grade ETL script incorporating all concepts.
- Features:
  - Configuration via .env
  - Error handling with trap
  - Temporary file management
  - Logging
  - Retry logic
  - Dependency checking
  - Signal handling
  - Progress reporting
- See template in Assignment 9 and extend with ETL logic

## Submission Guidelines

### Script Requirements
- [ ] Proper shebang: `#!/bin/bash`
- [ ] Error handling: `set -euo pipefail`
- [ ] Cleanup with `trap`
- [ ] Proper quoting: `"$VAR"` not `$VAR`
- [ ] Comments explaining complex logic
- [ ] Usage/help message for user-facing scripts

### Testing Checklist
Test each script with:
1. Normal execution
2. Error conditions (missing files, bad input)
3. Interruption (Ctrl+C)
4. Missing configuration
5. Invalid configuration values

### Documentation
For each script, provide:
1. **Purpose**: What does it do?
2. **Requirements**: Dependencies, config files
3. **Usage**: How to run it
4. **Configuration**: What variables it uses
5. **Error handling**: How it handles failures
6. **Cleanup**: What resources it manages

### Code Quality Standards
- Use meaningful variable names
- Avoid hardcoded paths
- Check command exit codes
- Provide helpful error messages
- Log important operations
- Clean up temporary resources

### Bonus: Shell Script Best Practices Guide
Create a comprehensive style guide based on your learnings:
- Naming conventions
- Error handling patterns
- Logging standards
- Configuration management
- Testing strategies
