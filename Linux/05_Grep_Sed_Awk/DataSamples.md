# Sample Data Files

Create the following files to practice with the lecture examples.

## app.log
```
2024-03-15 10:23:45 [INFO] Application started successfully
2024-03-15 10:24:12 [ERROR] Failed to connect to database: timeout
2024-03-15 10:24:15 [WARN] Retrying connection (attempt 1/3)
2024-03-15 10:24:18 [INFO] Database connection established
2024-03-15 10:25:02 [ERROR] Invalid request format from client 192.168.1.50
2024-03-15 10:26:30 [INFO] User john@example.com logged in
2024-03-15 10:27:45 [DEBUG] Cache hit ratio: 85%
2024-03-15 10:28:00 [CRITICAL] Disk space below 10% on /var/data
2024-03-15 10:29:15 [ERROR] Payment processing failed: card declined
2024-03-15 10:30:00 [INFO] Daily backup started
2024-03-15 10:35:00 [FATAL] Out of memory, shutting down
```

## access.log
```
192.168.1.10 - alice [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:31:02 +0000] "POST /api/login HTTP/1.1" 200 256 "curl/7.64.1"
192.168.1.10 - alice [15/Mar/2024:10:31:15 +0000] "GET /products?id=42 HTTP/1.1" 200 8901 "Mozilla/5.0"
192.168.1.20 - - [15/Mar/2024:10:32:00 +0000] "GET /admin HTTP/1.1" 403 123 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:32:30 +0000] "GET /api/orders HTTP/1.1" 200 4567 "curl/7.64.1"
192.168.1.25 - - [15/Mar/2024:10:33:45 +0000] "GET /missing.html HTTP/1.1" 404 89 "Googlebot/2.1"
192.168.1.10 - alice [15/Mar/2024:10:34:00 +0000] "POST /checkout HTTP/1.1" 500 234 "Mozilla/5.0"
192.168.1.30 - charlie [15/Mar/2024:10:35:15 +0000] "GET /api/users HTTP/1.1" 200 2345 "Python-urllib/3.9"
```

## users.txt
```
john.doe@example.com
jane_smith@company.org
bob123@test.net
alice.wonder@domain.co.uk
admin@localhost
support+help@service.io
invalid-email
user@sub.domain.example.com
contact@company.com
```

## data.csv
```csv
id,name,age,city,salary
1,Alice,30,New York,75000
2,Bob,25,Los Angeles,65000
3,Carol,35,Chicago,85000
4,Dave,28,Houston,70000
5,Eve,32,Phoenix,80000
6,Frank,45,Philadelphia,95000
7,Grace,27,San Antonio,62000
8,Henry,38,San Diego,88000
```

## sales.csv
```csv
date,product,quantity,price,region
2024-03-01,Widget A,100,25.50,North
2024-03-01,Widget B,50,45.00,South
2024-03-02,Widget A,75,25.50,East
2024-03-02,Widget C,30,120.00,North
2024-03-03,Widget B,80,45.00,West
2024-03-03,Widget A,120,25.50,South
2024-03-04,Widget C,25,120.00,East
2024-03-04,Widget D,200,15.00,North
```

## dates.txt
```
2024-03-15
2024-12-25
2023-01-01
2024-07-04
2024-11-28
```

## page.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>Visit <a href="https://example.com">Example</a> for more info.</p>
    <p>Contact us at <a href="mailto:info@company.com">info@company.com</a></p>
    <p>API endpoint: http://api.example.com/v1/data</p>
    <img src="https://cdn.example.com/image.png" alt="Logo">
</body>
</html>
```

---

## Quick File Creation

You can create all files with a single command:

```bash
# Create data directory
mkdir -p ~/grep_data && cd ~/grep_data

# app.log
cat > app.log << 'EOF'
2024-03-15 10:23:45 [INFO] Application started successfully
2024-03-15 10:24:12 [ERROR] Failed to connect to database: timeout
2024-03-15 10:24:15 [WARN] Retrying connection (attempt 1/3)
2024-03-15 10:24:18 [INFO] Database connection established
2024-03-15 10:25:02 [ERROR] Invalid request format from client 192.168.1.50
2024-03-15 10:26:30 [INFO] User john@example.com logged in
2024-03-15 10:27:45 [DEBUG] Cache hit ratio: 85%
2024-03-15 10:28:00 [CRITICAL] Disk space below 10% on /var/data
2024-03-15 10:29:15 [ERROR] Payment processing failed: card declined
2024-03-15 10:30:00 [INFO] Daily backup started
2024-03-15 10:35:00 [FATAL] Out of memory, shutting down
EOF

# access.log
cat > access.log << 'EOF'
192.168.1.10 - alice [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:31:02 +0000] "POST /api/login HTTP/1.1" 200 256 "curl/7.64.1"
192.168.1.10 - alice [15/Mar/2024:10:31:15 +0000] "GET /products?id=42 HTTP/1.1" 200 8901 "Mozilla/5.0"
192.168.1.20 - - [15/Mar/2024:10:32:00 +0000] "GET /admin HTTP/1.1" 403 123 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:32:30 +0000] "GET /api/orders HTTP/1.1" 200 4567 "curl/7.64.1"
192.168.1.25 - - [15/Mar/2024:10:33:45 +0000] "GET /missing.html HTTP/1.1" 404 89 "Googlebot/2.1"
192.168.1.10 - alice [15/Mar/2024:10:34:00 +0000] "POST /checkout HTTP/1.1" 500 234 "Mozilla/5.0"
192.168.1.30 - charlie [15/Mar/2024:10:35:15 +0000] "GET /api/users HTTP/1.1" 200 2345 "Python-urllib/3.9"
EOF

# users.txt
cat > users.txt << 'EOF'
john.doe@example.com
jane_smith@company.org
bob123@test.net
alice.wonder@domain.co.uk
admin@localhost
support+help@service.io
invalid-email
user@sub.domain.example.com
contact@company.com
EOF

# data.csv
cat > data.csv << 'EOF'
id,name,age,city,salary
1,Alice,30,New York,75000
2,Bob,25,Los Angeles,65000
3,Carol,35,Chicago,85000
4,Dave,28,Houston,70000
5,Eve,32,Phoenix,80000
6,Frank,45,Philadelphia,95000
7,Grace,27,San Antonio,62000
8,Henry,38,San Diego,88000
EOF

# sales.csv
cat > sales.csv << 'EOF'
date,product,quantity,price,region
2024-03-01,Widget A,100,25.50,North
2024-03-01,Widget B,50,45.00,South
2024-03-02,Widget A,75,25.50,East
2024-03-02,Widget C,30,120.00,North
2024-03-03,Widget B,80,45.00,West
2024-03-03,Widget A,120,25.50,South
2024-03-04,Widget C,25,120.00,East
2024-03-04,Widget D,200,15.00,North
EOF

# dates.txt
cat > dates.txt << 'EOF'
2024-03-15
2024-12-25
2023-01-01
2024-07-04
2024-11-28
EOF

# page.html
cat > page.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>Visit <a href="https://example.com">Example</a> for more info.</p>
    <p>Contact us at <a href="mailto:info@company.com">info@company.com</a></p>
    <p>API endpoint: http://api.example.com/v1/data</p>
    <img src="https://cdn.example.com/image.png" alt="Logo">
</body>
</html>
EOF

echo "All files created in $(pwd)"
ls -la
```

