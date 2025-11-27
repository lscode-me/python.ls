# Bash as Glue: Combining Tools & Error Handling

## Overview
Use bash to combine tools, handle errors with `trap`, manage configuration with `.env`, and work with temporary files.

## Combining Tools

### Chaining Commands
```bash
# Sequential execution
command1 && command2 && command3

# Execute regardless of success
command1; command2; command3

# Execute if previous fails
command1 || command2

# Pipeline
command1 | command2 | command3
```

### Complex Pipelines
```bash
# Multi-stage processing
cat data.csv | \
  grep -v "^#" | \
  cut -d',' -f2,3 | \
  sort | uniq -c | \
  sort -rn | \
  head -10
```

## Error Handling with trap

### Basic trap Usage
```bash
#!/bin/bash
set -e  # Exit on error

trap 'echo "Error on line $LINENO"' ERR
trap 'echo "Cleaning up..."; rm -f /tmp/tempfile' EXIT
trap 'echo "Interrupted"; exit 1' INT

# Your code here
```

### Cleanup with trap
```bash
#!/bin/bash
TEMPFILE=$(mktemp)

trap 'rm -f "$TEMPFILE"' EXIT

# Use tempfile
echo "data" > "$TEMPFILE"
process "$TEMPFILE"

# Automatic cleanup on exit
```

## Configuration with .env

### Load Environment Variables
```bash
# .env file
DATABASE_URL="postgres://localhost/mydb"
API_KEY="secret123"
LOG_LEVEL="INFO"

# Load in script
set -a  # Auto-export variables
source .env
set +a

echo "Connecting to $DATABASE_URL"
```

### Safe env Loading
```bash
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi
```

## Temporary Files

### mktemp for Safe Temp Files
```bash
# Create temp file
TMPFILE=$(mktemp)
echo "data" > "$TMPFILE"
# Process...
rm "$TMPFILE"

# Create temp directory
TMPDIR=$(mktemp -d)
# Use directory...
rm -rf "$TMPDIR"

# With trap for cleanup
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
```

### Temp File Patterns
```bash
# Named pattern
TMPFILE=$(mktemp /tmp/myapp.XXXXXX)

# In temp directory
TMPFILE=$(mktemp -p /fast/tmp)
```

## Complete Script Example

```bash
#!/bin/bash
set -euo pipefail  # Exit on error, undefined var, pipe failure

# Load config
if [ -f .env ]; then
    set -a
    source .env
    set +a
fi

# Setup temp files
TMPFILE=$(mktemp)
TMPDIR=$(mktemp -d)

# Cleanup on exit
trap 'rm -f "$TMPFILE"; rm -rf "$TMPDIR"' EXIT

# Error handler
trap 'echo "Error on line $LINENO"; exit 1' ERR

# Main logic
curl -s "$API_URL" | \
    jq -c '.[]' > "$TMPFILE"

cat "$TMPFILE" | \
    jq -r '.id' | \
    while read -r id; do
        process_id "$id"
    done

echo "Done"
```

## Best Practices

1. **Use `set -euo pipefail`**: Fail fast
2. **Always trap EXIT**: Cleanup temp files
3. **Use mktemp**: Never hardcode temp paths
4. **Load .env safely**: Use `set -a`
5. **Quote variables**: `"$VAR"` not `$VAR`
6. **Check file exists**: `[ -f file ]`
7. **Validate input**: Check arguments
8. **Log errors**: Echo to stderr with `>&2`

## Summary

| Technique | Purpose | Example |
|-----------|---------|---------|
| `&&` | Chain on success | `cmd1 && cmd2` |
| `trap` | Error handling | `trap 'cleanup' EXIT` |
| `.env` | Configuration | `source .env` |
| `mktemp` | Safe temp files | `TMPFILE=$(mktemp)` |

## Next Steps
- Practice error handling
- Build robust scripts
- Study bash best practices
- Explore logging patterns
