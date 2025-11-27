# Sample Data Files

Create the following files to practice with the lecture examples.

## app.jsonl
```jsonl
{"timestamp":"2024-03-15T10:30:00Z","level":"INFO","message":"Application started","service":"api"}
{"timestamp":"2024-03-15T10:30:05Z","level":"DEBUG","message":"Loading configuration","service":"api"}
{"timestamp":"2024-03-15T10:30:10Z","level":"INFO","message":"Database connected","service":"db"}
{"timestamp":"2024-03-15T10:30:15Z","level":"ERROR","message":"Failed to connect to cache","service":"cache","error_type":"ConnectionError"}
{"timestamp":"2024-03-15T10:30:20Z","level":"WARN","message":"Retrying cache connection","service":"cache"}
{"timestamp":"2024-03-15T10:30:25Z","level":"INFO","message":"Cache connected","service":"cache"}
{"timestamp":"2024-03-15T10:31:00Z","level":"INFO","message":"Request processed","service":"api","duration_ms":45}
{"timestamp":"2024-03-15T10:31:05Z","level":"ERROR","message":"Database timeout","service":"db","error_type":"TimeoutError"}
{"timestamp":"2024-03-15T10:31:10Z","level":"INFO","message":"Request processed","service":"api","duration_ms":120}
{"timestamp":"2024-03-15T10:32:00Z","level":"ERROR","message":"Invalid request format","service":"api","error_type":"ValidationError"}
```

## errors.jsonl
```jsonl
{"timestamp":"2024-03-15T10:30:15Z","error_type":"ConnectionError","service":"cache","message":"Failed to connect to cache server"}
{"timestamp":"2024-03-15T10:31:05Z","error_type":"TimeoutError","service":"db","message":"Database query timeout after 30s"}
{"timestamp":"2024-03-15T10:32:00Z","error_type":"ValidationError","service":"api","message":"Missing required field: user_id"}
{"timestamp":"2024-03-15T10:33:15Z","error_type":"AuthError","service":"auth","message":"Invalid token"}
{"timestamp":"2024-03-15T10:34:00Z","error_type":"TimeoutError","service":"db","message":"Database connection timeout"}
{"timestamp":"2024-03-15T10:35:30Z","error_type":"ConnectionError","service":"cache","message":"Cache server unreachable"}
{"timestamp":"2024-03-15T10:36:00Z","error_type":"ValidationError","service":"api","message":"Invalid email format"}
```

## queries.jsonl
```jsonl
{"timestamp":"2024-03-15T10:30:00Z","query":"SELECT * FROM users WHERE id = 1","duration_ms":15,"rows":1}
{"timestamp":"2024-03-15T10:30:05Z","query":"SELECT * FROM orders WHERE user_id = 1","duration_ms":45,"rows":12}
{"timestamp":"2024-03-15T10:30:10Z","query":"SELECT * FROM products","duration_ms":1250,"rows":5000}
{"timestamp":"2024-03-15T10:30:15Z","query":"UPDATE users SET last_login = NOW()","duration_ms":8,"rows":1}
{"timestamp":"2024-03-15T10:30:20Z","query":"SELECT * FROM logs WHERE date > '2024-03-01'","duration_ms":3500,"rows":100000}
{"timestamp":"2024-03-15T10:30:25Z","query":"SELECT COUNT(*) FROM sessions","duration_ms":120,"rows":1}
```

## sessions.jsonl
```jsonl
{"session_id":"s001","user_id":"u1","start_time":"2024-03-15T10:00:00Z","duration":1800,"pages":15}
{"session_id":"s002","user_id":"u2","start_time":"2024-03-15T10:05:00Z","duration":900,"pages":8}
{"session_id":"s003","user_id":"u1","start_time":"2024-03-15T11:00:00Z","duration":600,"pages":5}
{"session_id":"s004","user_id":"u3","start_time":"2024-03-15T11:30:00Z","duration":2400,"pages":22}
{"session_id":"s005","user_id":"u2","start_time":"2024-03-15T12:00:00Z","duration":1200,"pages":10}
```

## access.log
```
192.168.1.10 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.15 - - [15/Mar/2024:10:30:52 +0000] "GET /api/users HTTP/1.1" 200 5678
192.168.1.10 - - [15/Mar/2024:10:31:01 +0000] "POST /api/login HTTP/1.1" 200 234
192.168.1.20 - - [15/Mar/2024:10:31:15 +0000] "GET /products HTTP/1.1" 200 8901
192.168.1.15 - - [15/Mar/2024:10:32:03 +0000] "GET /api/orders HTTP/1.1" 200 4567
192.168.1.10 - - [15/Mar/2024:10:32:45 +0000] "GET /checkout HTTP/1.1" 200 2345
192.168.1.25 - - [15/Mar/2024:10:33:12 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.30 - - [15/Mar/2024:10:34:00 +0000] "GET /api/products HTTP/1.1" 500 123
192.168.1.15 - - [15/Mar/2024:10:35:15 +0000] "POST /api/checkout HTTP/1.1" 200 456
```

## data.csv
```csv
date,category,amount,count
2024-03-01,sales,15000,120
2024-03-01,returns,500,8
2024-03-02,sales,18000,145
2024-03-02,returns,750,12
2024-03-03,sales,12000,95
2024-03-03,returns,300,5
```

## users.csv
```csv
id,name,email,signup_date,status
1,Alice,alice@example.com,2024-01-15,active
2,Bob,bob@test.com,2024-02-01,active
3,Carol,carol@domain.org,2024-02-15,inactive
4,Dave,dave@example.com,2024-03-01,active
5,Eve,eve@company.io,2024-03-10,active
```

---

## Quick File Creation

You can create all files with a single command:

```bash
# Create data directory
mkdir -p ~/log_data && cd ~/log_data

# app.jsonl
cat > app.jsonl << 'EOF'
{"timestamp":"2024-03-15T10:30:00Z","level":"INFO","message":"Application started","service":"api"}
{"timestamp":"2024-03-15T10:30:05Z","level":"DEBUG","message":"Loading configuration","service":"api"}
{"timestamp":"2024-03-15T10:30:10Z","level":"INFO","message":"Database connected","service":"db"}
{"timestamp":"2024-03-15T10:30:15Z","level":"ERROR","message":"Failed to connect to cache","service":"cache","error_type":"ConnectionError"}
{"timestamp":"2024-03-15T10:30:20Z","level":"WARN","message":"Retrying cache connection","service":"cache"}
{"timestamp":"2024-03-15T10:30:25Z","level":"INFO","message":"Cache connected","service":"cache"}
{"timestamp":"2024-03-15T10:31:00Z","level":"INFO","message":"Request processed","service":"api","duration_ms":45}
{"timestamp":"2024-03-15T10:31:05Z","level":"ERROR","message":"Database timeout","service":"db","error_type":"TimeoutError"}
{"timestamp":"2024-03-15T10:31:10Z","level":"INFO","message":"Request processed","service":"api","duration_ms":120}
{"timestamp":"2024-03-15T10:32:00Z","level":"ERROR","message":"Invalid request format","service":"api","error_type":"ValidationError"}
EOF

# errors.jsonl
cat > errors.jsonl << 'EOF'
{"timestamp":"2024-03-15T10:30:15Z","error_type":"ConnectionError","service":"cache","message":"Failed to connect to cache server"}
{"timestamp":"2024-03-15T10:31:05Z","error_type":"TimeoutError","service":"db","message":"Database query timeout after 30s"}
{"timestamp":"2024-03-15T10:32:00Z","error_type":"ValidationError","service":"api","message":"Missing required field: user_id"}
{"timestamp":"2024-03-15T10:33:15Z","error_type":"AuthError","service":"auth","message":"Invalid token"}
{"timestamp":"2024-03-15T10:34:00Z","error_type":"TimeoutError","service":"db","message":"Database connection timeout"}
{"timestamp":"2024-03-15T10:35:30Z","error_type":"ConnectionError","service":"cache","message":"Cache server unreachable"}
{"timestamp":"2024-03-15T10:36:00Z","error_type":"ValidationError","service":"api","message":"Invalid email format"}
EOF

# queries.jsonl
cat > queries.jsonl << 'EOF'
{"timestamp":"2024-03-15T10:30:00Z","query":"SELECT * FROM users WHERE id = 1","duration_ms":15,"rows":1}
{"timestamp":"2024-03-15T10:30:05Z","query":"SELECT * FROM orders WHERE user_id = 1","duration_ms":45,"rows":12}
{"timestamp":"2024-03-15T10:30:10Z","query":"SELECT * FROM products","duration_ms":1250,"rows":5000}
{"timestamp":"2024-03-15T10:30:15Z","query":"UPDATE users SET last_login = NOW()","duration_ms":8,"rows":1}
{"timestamp":"2024-03-15T10:30:20Z","query":"SELECT * FROM logs WHERE date > '2024-03-01'","duration_ms":3500,"rows":100000}
{"timestamp":"2024-03-15T10:30:25Z","query":"SELECT COUNT(*) FROM sessions","duration_ms":120,"rows":1}
EOF

# sessions.jsonl
cat > sessions.jsonl << 'EOF'
{"session_id":"s001","user_id":"u1","start_time":"2024-03-15T10:00:00Z","duration":1800,"pages":15}
{"session_id":"s002","user_id":"u2","start_time":"2024-03-15T10:05:00Z","duration":900,"pages":8}
{"session_id":"s003","user_id":"u1","start_time":"2024-03-15T11:00:00Z","duration":600,"pages":5}
{"session_id":"s004","user_id":"u3","start_time":"2024-03-15T11:30:00Z","duration":2400,"pages":22}
{"session_id":"s005","user_id":"u2","start_time":"2024-03-15T12:00:00Z","duration":1200,"pages":10}
EOF

# access.log
cat > access.log << 'EOF'
192.168.1.10 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.15 - - [15/Mar/2024:10:30:52 +0000] "GET /api/users HTTP/1.1" 200 5678
192.168.1.10 - - [15/Mar/2024:10:31:01 +0000] "POST /api/login HTTP/1.1" 200 234
192.168.1.20 - - [15/Mar/2024:10:31:15 +0000] "GET /products HTTP/1.1" 200 8901
192.168.1.15 - - [15/Mar/2024:10:32:03 +0000] "GET /api/orders HTTP/1.1" 200 4567
192.168.1.10 - - [15/Mar/2024:10:32:45 +0000] "GET /checkout HTTP/1.1" 200 2345
192.168.1.25 - - [15/Mar/2024:10:33:12 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.30 - - [15/Mar/2024:10:34:00 +0000] "GET /api/products HTTP/1.1" 500 123
192.168.1.15 - - [15/Mar/2024:10:35:15 +0000] "POST /api/checkout HTTP/1.1" 200 456
EOF

# data.csv
cat > data.csv << 'EOF'
date,category,amount,count
2024-03-01,sales,15000,120
2024-03-01,returns,500,8
2024-03-02,sales,18000,145
2024-03-02,returns,750,12
2024-03-03,sales,12000,95
2024-03-03,returns,300,5
EOF

# users.csv
cat > users.csv << 'EOF'
id,name,email,signup_date,status
1,Alice,alice@example.com,2024-01-15,active
2,Bob,bob@test.com,2024-02-01,active
3,Carol,carol@domain.org,2024-02-15,inactive
4,Dave,dave@example.com,2024-03-01,active
5,Eve,eve@company.io,2024-03-10,active
EOF

echo "All files created in $(pwd)"
ls -la
```

