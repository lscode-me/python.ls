# DuckDB Setup Guide

DuckDB is a fast in-process analytical database that can query CSV, JSON, and Parquet files directly.

## Installation

### macOS
```bash
brew install duckdb
```

### Linux (Ubuntu/Debian)
```bash
# Download latest release
wget https://github.com/duckdb/duckdb/releases/latest/download/duckdb_cli-linux-amd64.zip
unzip duckdb_cli-linux-amd64.zip
sudo mv duckdb /usr/local/bin/
```

### Linux (Alternative - using apt)
```bash
# Install via apt (Ubuntu 22.04+)
curl -fsSL https://duckdb.org/ubuntu/duckdb.gpg | sudo gpg --dearmor -o /usr/share/keyrings/duckdb-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/duckdb-archive-keyring.gpg] https://duckdb.org/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/duckdb.list
sudo apt update
sudo apt install duckdb
```

### Verify Installation
```bash
duckdb --version
```

Expected output:
```
v0.x.x xxxxxxxx
```

## Quick Start

### 1. Query a CSV file
```bash
duckdb -c "SELECT * FROM 'users.csv' WHERE status = 'active'"
```

### 2. Run aggregations
```bash
duckdb -c "SELECT category, COUNT(*), AVG(price) FROM 'products.csv' GROUP BY category"
```

### 3. Join files
```bash
duckdb -c "
  SELECT u.name, COUNT(o.order_id) as orders
  FROM 'users.csv' u
  JOIN 'orders.csv' o ON u.id = o.customer_id
  GROUP BY u.name
"
```

### 4. Interactive mode
```bash
duckdb

# Inside DuckDB shell:
D SELECT * FROM 'users.csv' LIMIT 5;
D .mode markdown
D SELECT * FROM 'products.csv';
D .quit
```

## Output Formats

```bash
# Markdown table
duckdb -markdown -c "SELECT * FROM 'users.csv'"

# JSON
duckdb -json -c "SELECT * FROM 'users.csv'"

# CSV (default)
duckdb -c "SELECT * FROM 'users.csv'"

# Box drawing (pretty)
duckdb -box -c "SELECT * FROM 'users.csv'"
```

## Common Commands

### Export to CSV
```bash
duckdb -c "COPY (SELECT * FROM 'data.csv' WHERE condition) TO 'output.csv' (HEADER)"
```

### Export to Parquet
```bash
duckdb -c "COPY (SELECT * FROM 'data.csv') TO 'output.parquet' (FORMAT PARQUET)"
```

### Read JSON
```bash
duckdb -c "SELECT * FROM read_json_auto('data.json')"
```

### Read JSONL (newline-delimited)
```bash
duckdb -c "SELECT * FROM read_json_auto('events.jsonl', format='newline_delimited')"
```

## Try the Examples

Run the example script to see DuckDB in action:
```bash
./duckdb_examples.sh
```

## Resources

- Official Website: https://duckdb.org/
- Documentation: https://duckdb.org/docs/
- SQL Reference: https://duckdb.org/docs/sql/introduction
- GitHub: https://github.com/duckdb/duckdb

## Troubleshooting

### Command not found
If you get "command not found", make sure DuckDB is in your PATH:
```bash
which duckdb
echo $PATH
```

### Permission denied
Make the binary executable:
```bash
chmod +x /usr/local/bin/duckdb
```

### Slow performance
For large files, consider:
- Using Parquet format (much faster than CSV)
- Creating temporary database with indexes
- Using appropriate WHERE clauses to filter early

## Next Steps

After installation, explore:
1. Module 06: Structured Data Processing
2. Module 07: Streaming Analytics
3. Practice with homework assignments
4. Compare DuckDB vs mlr vs awk for different tasks

Happy querying! 🦆

