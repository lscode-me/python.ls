# Sample Data Files

All sample data files used throughout the course are available in the `files/` subfolder.

---

## 📁 Quick Setup

**Option 1: Use files directly from the repository**
```bash
cd Linux/data/files/
cat users.csv
```

**Option 2: Copy to your working directory**
```bash
cp -r Linux/data/files/* ~/workspace/linux_course_data/
cd ~/workspace/linux_course_data
```

---

## 🔤 Basic Text Files

### data.txt
Simple text file for basic stream operations.

```
apple
banana
cherry
apple
date
banana
elderberry
apple
fig
banana
grape
cherry
```

### numbers.txt
Numeric data for arithmetic operations.

```
42
17
89
23
56
78
12
45
91
34
67
28
```

### dates.txt
Date samples for pattern matching.

```
2024-03-15
2024-03-16
2024-03-17
2024-12-25
2023-01-01
2024-07-04
2024-11-28
```

### emails.txt
Email addresses for regex practice.

```
alice@example.com
bob.smith@company.org
carol_jones@test.net
dave+work@domain.co.uk
admin@localhost
support+help@service.io
invalid-email
user@sub.domain.example.com
contact@company.com
jane_doe123@mail.ru
```

### users.txt
Alternative name for emails (used in grep examples).

```
alice@example.com
bob.smith@company.org
carol_jones@test.net
dave+work@domain.co.uk
admin@localhost
support+help@service.io
invalid-email
user@sub.domain.example.com
contact@company.com
jane_doe123@mail.ru
```

---

## 📊 CSV Files

### data.csv
Generic CSV for basic examples (cut, sort, awk).

```csv
id,name,age,city,status
1,Alice,30,Moscow,active
2,Bob,25,SPb,active
3,Carol,35,Kazan,inactive
4,Dave,28,Moscow,active
5,Eve,32,Sochi,inactive
6,Frank,45,Novosibirsk,active
7,Grace,27,Samara,active
8,Henry,38,Ekaterinburg,inactive
```

### users.csv
User data - consistent across all modules.

```csv
id,name,email,city,status
1,Alice,alice@example.com,Moscow,active
2,Bob,bob@company.org,SPb,active
3,Carol,carol@test.net,Kazan,inactive
4,Dave,dave@domain.co.uk,Moscow,active
5,Eve,eve@service.io,Sochi,inactive
6,Frank,frank@mail.ru,Novosibirsk,active
```

### products.csv
Product catalog.

```csv
id,name,price,category,rating
1,Phone,999,Electronics,4.5
2,Laptop,1499,Electronics,4.8
3,Shirt,45,Clothing,4.0
4,Pants,80,Clothing,4.3
5,Tablet,599,Electronics,4.2
6,Jacket,150,Clothing,4.7
7,Apple,2,Food,4.9
8,Bread,3,Food,4.6
```

### orders.csv
Order history with customer references.

```csv
order_id,customer_id,product_id,quantity,amount,date
101,1,1,1,999,2024-03-15
102,1,3,2,90,2024-03-15
103,2,2,1,1499,2024-03-16
104,3,4,1,80,2024-03-16
105,1,5,1,599,2024-03-17
106,4,6,2,300,2024-03-17
107,2,7,10,20,2024-03-18
108,5,2,1,1499,2024-03-18
109,3,1,1,999,2024-03-19
110,6,3,3,135,2024-03-19
```

### sales.csv
Daily sales aggregates.

```csv
date,product,quantity,revenue,region
2024-03-15,Phone,5,4995,North
2024-03-15,Laptop,3,4497,South
2024-03-16,Phone,8,7992,East
2024-03-16,Shirt,15,675,North
2024-03-17,Laptop,4,5996,West
2024-03-17,Pants,12,960,South
2024-03-18,Tablet,6,3594,East
2024-03-18,Jacket,8,1200,North
```

### customers.csv
Customer reference table.

```csv
customer_id,name,city,signup_date
1,Alice,Moscow,2024-01-15
2,Bob,SPb,2024-01-20
3,Carol,Kazan,2024-02-01
4,Dave,Moscow,2024-02-10
5,Eve,Sochi,2024-02-15
6,Frank,Novosibirsk,2024-03-01
```

### left.csv & right.csv
For JOIN operations.

**left.csv:**
```csv
id,name,department
1,Alice,Engineering
2,Bob,Marketing
3,Carol,Engineering
4,Dave,Sales
```

**right.csv:**
```csv
id,salary,start_date
1,75000,2020-03-15
2,65000,2021-06-01
3,80000,2019-11-20
5,55000,2022-01-10
```

### lookup.csv
Status code lookup table.

```csv
code,description
A,Active
I,Inactive
P,Pending
D,Deleted
```

### matrix.csv
Simple matrix for transpose operations.

```csv
a,b,c
1,2,3
4,5,6
7,8,9
```

### user_activity.csv
User activity for cohort analysis.

```csv
user_id,signup_date,activity_date,actions
u1,2024-01-01,2024-01-05,12
u2,2024-01-01,2024-01-08,8
u1,2024-01-01,2024-02-10,15
u3,2024-02-01,2024-02-05,5
u2,2024-01-01,2024-02-12,10
u3,2024-02-01,2024-03-01,7
u4,2024-03-01,2024-03-15,3
u1,2024-01-01,2024-03-20,18
u2,2024-01-01,2024-03-25,6
```

### transactions.csv
Transaction records for filtering examples.

```csv
date,amount,category
2024-03-15,150,Electronics
2024-03-15,45,Clothing
2024-03-16,1499,Electronics
2024-03-16,80,Clothing
2024-03-17,25,Food
2024-03-17,599,Electronics
2024-03-18,200,Clothing
2024-03-18,15,Food
2024-03-19,999,Electronics
2024-03-19,50,Food
2024-03-20,75,Clothing
2024-03-20,120,Electronics
```

---

## 📝 Log Files

### logs.txt
Simple log file with dates for pattern matching.

```
2024-03-15 10:23:45 INFO Application started
2024-03-15 10:24:12 ERROR Connection failed
2024-03-16 08:00:00 INFO Daily backup started
2024-03-16 08:15:30 WARN Disk space low
2024-03-17 14:22:01 INFO User login: alice
2024-03-17 14:25:45 ERROR Invalid token
2024-03-18 09:00:00 INFO Scheduled task executed
2024-03-19 11:30:22 DEBUG Cache cleared
2024-03-20 16:45:00 INFO Application stopped
2023-01-01 00:00:00 INFO New Year started
2024-12-25 12:00:00 INFO Holiday mode enabled
```

### app.log
Plain text application log.

```
2024-03-15 10:23:45 INFO Application started
2024-03-15 10:23:46 DEBUG Loading configuration
2024-03-15 10:23:47 INFO User alice logged in
2024-03-15 10:24:12 ERROR Connection timeout to database
2024-03-15 10:24:15 WARN Retrying connection (attempt 1)
2024-03-15 10:24:18 INFO Connection established
2024-03-15 10:25:01 DEBUG Processing request #1234
2024-03-15 10:25:02 ERROR Invalid request format
2024-03-15 10:26:30 INFO User bob logged in
2024-03-15 10:27:45 DEBUG Cache cleared
2024-03-15 10:28:00 ERROR Failed to send email notification
2024-03-15 10:30:00 INFO Daily backup started
2024-03-15 10:35:00 FATAL Out of memory, shutting down
```

### access.log
Web server access log (Combined Log Format).

```
192.168.1.10 - alice [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:31:02 +0000] "POST /api/login HTTP/1.1" 200 256 "curl/7.64.1"
192.168.1.10 - alice [15/Mar/2024:10:31:15 +0000] "GET /products?id=42 HTTP/1.1" 200 8901 "Mozilla/5.0"
192.168.1.20 - - [15/Mar/2024:10:32:00 +0000] "GET /admin HTTP/1.1" 403 123 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:32:30 +0000] "GET /api/orders HTTP/1.1" 200 4567 "curl/7.64.1"
192.168.1.25 - - [15/Mar/2024:10:33:45 +0000] "GET /missing.html HTTP/1.1" 404 89 "Googlebot/2.1"
192.168.1.10 - alice [15/Mar/2024:10:34:00 +0000] "POST /checkout HTTP/1.1" 500 234 "Mozilla/5.0"
192.168.1.30 - carol [15/Mar/2024:10:35:15 +0000] "GET /api/users HTTP/1.1" 200 2345 "Python-urllib/3.9"
192.168.1.15 - bob [15/Mar/2024:10:36:00 +0000] "POST /api/checkout HTTP/1.1" 200 456 "curl/7.64.1"
```

---

## 📦 JSON Files

### data.jsonl
Simple JSONL for shell script examples.

```jsonl
{"name": "Alice", "age": 30, "city": "Moscow"}
{"name": "Bob", "age": 25, "city": "SPb"}
{"name": "Carol", "age": 35, "city": "Kazan"}
{"name": "Dave", "age": 28, "city": "Moscow"}
{"name": "Eve", "age": 32, "city": "Sochi"}
{"name": "Frank", "age": 45, "city": "Novosibirsk"}
```

### sales.jsonl
Sales data in JSONL format for aggregation examples.

```jsonl
{"date": "2024-03-15", "product": "Phone", "amount": 999, "region": "North"}
{"date": "2024-03-15", "product": "Laptop", "amount": 1499, "region": "South"}
{"date": "2024-03-16", "product": "Shirt", "amount": 45, "region": "East"}
{"date": "2024-03-16", "product": "Phone", "amount": 999, "region": "West"}
{"date": "2024-03-17", "product": "Tablet", "amount": 599, "region": "North"}
{"date": "2024-03-17", "product": "Pants", "amount": 80, "region": "South"}
{"date": "2024-03-18", "product": "Jacket", "amount": 150, "region": "East"}
{"date": "2024-03-18", "product": "Laptop", "amount": 1499, "region": "West"}
```

### users.json
JSON array format.

```json
[
  {"id": 1, "name": "Alice", "age": 30, "city": "Moscow", "status": "active"},
  {"id": 2, "name": "Bob", "age": 25, "city": "SPb", "status": "active"},
  {"id": 3, "name": "Carol", "age": 35, "city": "Kazan", "status": "inactive"},
  {"id": 4, "name": "Dave", "age": 28, "city": "Moscow", "status": "active"},
  {"id": 5, "name": "Eve", "age": 32, "city": "Sochi", "status": "inactive"},
  {"id": 6, "name": "Frank", "age": 45, "city": "Novosibirsk", "status": "active"}
]
```

### users.jsonl
JSONL (newline-delimited JSON) format.

```jsonl
{"id": 1, "name": "Alice", "age": 30, "city": "Moscow", "status": "active"}
{"id": 2, "name": "Bob", "age": 25, "city": "SPb", "status": "active"}
{"id": 3, "name": "Carol", "age": 35, "city": "Kazan", "status": "inactive"}
{"id": 4, "name": "Dave", "age": 28, "city": "Moscow", "status": "active"}
{"id": 5, "name": "Eve", "age": 32, "city": "Sochi", "status": "inactive"}
{"id": 6, "name": "Frank", "age": 45, "city": "Novosibirsk", "status": "active"}
```

### products.json
Product catalog in JSON.

```json
[
  {"id": 1, "name": "Phone", "price": 999, "category": "Electronics"},
  {"id": 2, "name": "Laptop", "price": 1499, "category": "Electronics"},
  {"id": 3, "name": "Shirt", "price": 45, "category": "Clothing"},
  {"id": 4, "name": "Pants", "price": 80, "category": "Clothing"},
  {"id": 5, "name": "Tablet", "price": 599, "category": "Electronics"},
  {"id": 6, "name": "Jacket", "price": 150, "category": "Clothing"}
]
```

### events.jsonl
User activity events.

```jsonl
{"timestamp": "2024-03-15T10:30:00Z", "user_id": 1, "type": "login", "session_id": "s001"}
{"timestamp": "2024-03-15T10:35:00Z", "user_id": 1, "type": "purchase", "amount": 999, "product_id": 1}
{"timestamp": "2024-03-15T10:40:00Z", "user_id": 2, "type": "login", "session_id": "s002"}
{"timestamp": "2024-03-15T10:45:00Z", "user_id": 1, "type": "error", "message": "Payment failed"}
{"timestamp": "2024-03-15T10:50:00Z", "user_id": 2, "type": "purchase", "amount": 1499, "product_id": 2}
{"timestamp": "2024-03-15T11:00:00Z", "user_id": 3, "type": "login", "session_id": "s003"}
{"timestamp": "2024-03-15T11:05:00Z", "user_id": 3, "type": "logout", "session_id": "s003"}
```

### app.jsonl
Structured application log.

```jsonl
{"timestamp": "2024-03-15T10:30:00Z", "level": "INFO", "message": "Application started", "service": "api"}
{"timestamp": "2024-03-15T10:30:05Z", "level": "DEBUG", "message": "Loading configuration", "service": "api"}
{"timestamp": "2024-03-15T10:30:10Z", "level": "INFO", "message": "Database connected", "service": "db"}
{"timestamp": "2024-03-15T10:30:15Z", "level": "ERROR", "message": "Failed to connect to cache", "service": "cache", "error_type": "ConnectionError"}
{"timestamp": "2024-03-15T10:30:20Z", "level": "WARN", "message": "Retrying cache connection", "service": "cache"}
{"timestamp": "2024-03-15T10:30:25Z", "level": "INFO", "message": "Cache connected", "service": "cache"}
{"timestamp": "2024-03-15T10:31:00Z", "level": "INFO", "message": "Request processed", "service": "api", "duration_ms": 45}
{"timestamp": "2024-03-15T10:31:05Z", "level": "ERROR", "message": "Database timeout", "service": "db", "error_type": "TimeoutError"}
{"timestamp": "2024-03-15T10:32:00Z", "level": "ERROR", "message": "Invalid request format", "service": "api", "error_type": "ValidationError"}
```

### errors.jsonl
Error log for analysis.

```jsonl
{"timestamp": "2024-03-15T10:30:15Z", "error_type": "ConnectionError", "service": "cache", "message": "Failed to connect to cache server"}
{"timestamp": "2024-03-15T10:31:05Z", "error_type": "TimeoutError", "service": "db", "message": "Database query timeout after 30s"}
{"timestamp": "2024-03-15T10:32:00Z", "error_type": "ValidationError", "service": "api", "message": "Missing required field: user_id"}
{"timestamp": "2024-03-15T10:33:15Z", "error_type": "AuthError", "service": "auth", "message": "Invalid token"}
{"timestamp": "2024-03-15T10:34:00Z", "error_type": "TimeoutError", "service": "db", "message": "Database connection timeout"}
{"timestamp": "2024-03-15T10:35:30Z", "error_type": "ConnectionError", "service": "cache", "message": "Cache server unreachable"}
```

### sessions.jsonl
User session data.

```jsonl
{"session_id": "s001", "user_id": 1, "start_time": "2024-03-15T10:00:00Z", "duration": 1800, "pages": 15}
{"session_id": "s002", "user_id": 2, "start_time": "2024-03-15T10:05:00Z", "duration": 900, "pages": 8}
{"session_id": "s003", "user_id": 1, "start_time": "2024-03-15T11:00:00Z", "duration": 600, "pages": 5}
{"session_id": "s004", "user_id": 3, "start_time": "2024-03-15T11:30:00Z", "duration": 2400, "pages": 22}
{"session_id": "s005", "user_id": 2, "start_time": "2024-03-15T12:00:00Z", "duration": 1200, "pages": 10}
```

### queries.jsonl
Database query log for slow query analysis.

```jsonl
{"timestamp": "2024-03-15T10:30:00Z", "query": "SELECT * FROM users WHERE id = 1", "duration_ms": 15, "rows": 1}
{"timestamp": "2024-03-15T10:30:05Z", "query": "SELECT * FROM orders WHERE user_id = 1", "duration_ms": 45, "rows": 12}
{"timestamp": "2024-03-15T10:30:10Z", "query": "SELECT * FROM products", "duration_ms": 1250, "rows": 5000}
{"timestamp": "2024-03-15T10:30:15Z", "query": "UPDATE users SET last_login = NOW()", "duration_ms": 8, "rows": 1}
{"timestamp": "2024-03-15T10:30:20Z", "query": "SELECT * FROM logs WHERE date > '2024-03-01'", "duration_ms": 3500, "rows": 100000}
{"timestamp": "2024-03-15T10:30:25Z", "query": "SELECT COUNT(*) FROM sessions", "duration_ms": 120, "rows": 1}
{"timestamp": "2024-03-15T10:30:30Z", "query": "SELECT * FROM analytics WHERE event_type = 'click'", "duration_ms": 2100, "rows": 45000}
```

---

## ⚙️ Configuration Files

### config.yaml
Application configuration.

```yaml
database:
  host: localhost
  port: 5432
  name: myapp
  user: admin

server:
  host: 0.0.0.0
  port: 8080
  debug: false

logging:
  level: INFO
  format: json
  file: /var/log/app.log

features:
  - name: authentication
    enabled: true
  - name: caching
    enabled: true
    ttl: 3600
```

### data.xml
XML data sample.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <users>
    <user id="1">
      <name>Alice</name>
      <age>30</age>
      <city>Moscow</city>
    </user>
    <user id="2">
      <name>Bob</name>
      <age>25</age>
      <city>SPb</city>
    </user>
    <user id="3">
      <name>Carol</name>
      <age>35</age>
      <city>Kazan</city>
    </user>
  </users>
  <products>
    <product id="1">
      <name>Phone</name>
      <price>999</price>
    </product>
    <product id="2">
      <name>Laptop</name>
      <price>1499</price>
    </product>
  </products>
</root>
```

---

## 🌐 Web Content

### page.html
Sample HTML page for pattern extraction.

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
    <p>Phone: +7 (495) 123-45-67</p>
</body>
</html>
```

---

## 📋 Quick File Creation Script

Run this script to create all sample files at once:

```bash
#!/bin/bash
# Create all sample data files for the course

mkdir -p ~/workspace/linux_course_data && cd ~/workspace/linux_course_data

# === Basic Text Files ===

cat > data.txt << 'EOF'
apple
banana
cherry
apple
date
banana
elderberry
apple
fig
banana
grape
cherry
EOF

cat > numbers.txt << 'EOF'
42
17
89
23
56
78
12
45
91
34
67
28
EOF

cat > dates.txt << 'EOF'
2024-03-15
2024-03-16
2024-03-17
2024-12-25
2023-01-01
2024-07-04
2024-11-28
EOF

cat > emails.txt << 'EOF'
alice@example.com
bob.smith@company.org
carol_jones@test.net
dave+work@domain.co.uk
admin@localhost
support+help@service.io
invalid-email
user@sub.domain.example.com
contact@company.com
jane_doe123@mail.ru
EOF

cat > users.txt << 'EOF'
alice@example.com
bob.smith@company.org
carol_jones@test.net
dave+work@domain.co.uk
admin@localhost
support+help@service.io
invalid-email
user@sub.domain.example.com
contact@company.com
jane_doe123@mail.ru
EOF

# === CSV Files ===

cat > data.csv << 'EOF'
id,name,age,city,status
1,Alice,30,Moscow,active
2,Bob,25,SPb,active
3,Carol,35,Kazan,inactive
4,Dave,28,Moscow,active
5,Eve,32,Sochi,inactive
6,Frank,45,Novosibirsk,active
7,Grace,27,Samara,active
8,Henry,38,Ekaterinburg,inactive
EOF

cat > users.csv << 'EOF'
id,name,email,city,status
1,Alice,alice@example.com,Moscow,active
2,Bob,bob@company.org,SPb,active
3,Carol,carol@test.net,Kazan,inactive
4,Dave,dave@domain.co.uk,Moscow,active
5,Eve,eve@service.io,Sochi,inactive
6,Frank,frank@mail.ru,Novosibirsk,active
EOF

cat > products.csv << 'EOF'
id,name,price,category,rating
1,Phone,999,Electronics,4.5
2,Laptop,1499,Electronics,4.8
3,Shirt,45,Clothing,4.0
4,Pants,80,Clothing,4.3
5,Tablet,599,Electronics,4.2
6,Jacket,150,Clothing,4.7
7,Apple,2,Food,4.9
8,Bread,3,Food,4.6
EOF

cat > orders.csv << 'EOF'
order_id,customer_id,product_id,quantity,amount,date
101,1,1,1,999,2024-03-15
102,1,3,2,90,2024-03-15
103,2,2,1,1499,2024-03-16
104,3,4,1,80,2024-03-16
105,1,5,1,599,2024-03-17
106,4,6,2,300,2024-03-17
107,2,7,10,20,2024-03-18
108,5,2,1,1499,2024-03-18
109,3,1,1,999,2024-03-19
110,6,3,3,135,2024-03-19
EOF

cat > sales.csv << 'EOF'
date,product,quantity,revenue,region
2024-03-15,Phone,5,4995,North
2024-03-15,Laptop,3,4497,South
2024-03-16,Phone,8,7992,East
2024-03-16,Shirt,15,675,North
2024-03-17,Laptop,4,5996,West
2024-03-17,Pants,12,960,South
2024-03-18,Tablet,6,3594,East
2024-03-18,Jacket,8,1200,North
EOF

cat > customers.csv << 'EOF'
customer_id,name,city,signup_date
1,Alice,Moscow,2024-01-15
2,Bob,SPb,2024-01-20
3,Carol,Kazan,2024-02-01
4,Dave,Moscow,2024-02-10
5,Eve,Sochi,2024-02-15
6,Frank,Novosibirsk,2024-03-01
EOF

cat > left.csv << 'EOF'
id,name,department
1,Alice,Engineering
2,Bob,Marketing
3,Carol,Engineering
4,Dave,Sales
EOF

cat > right.csv << 'EOF'
id,salary,start_date
1,75000,2020-03-15
2,65000,2021-06-01
3,80000,2019-11-20
5,55000,2022-01-10
EOF

cat > lookup.csv << 'EOF'
code,description
A,Active
I,Inactive
P,Pending
D,Deleted
EOF

cat > matrix.csv << 'EOF'
a,b,c
1,2,3
4,5,6
7,8,9
EOF

cat > transactions.csv << 'EOF'
date,amount,category
2024-03-15,150,Electronics
2024-03-15,45,Clothing
2024-03-16,1499,Electronics
2024-03-16,80,Clothing
2024-03-17,25,Food
2024-03-17,599,Electronics
2024-03-18,200,Clothing
2024-03-18,15,Food
2024-03-19,999,Electronics
2024-03-19,50,Food
2024-03-20,75,Clothing
2024-03-20,120,Electronics
EOF

cat > user_activity.csv << 'EOF'
user_id,signup_date,activity_date,actions
u1,2024-01-01,2024-01-05,12
u2,2024-01-01,2024-01-08,8
u1,2024-01-01,2024-02-10,15
u3,2024-02-01,2024-02-05,5
u2,2024-01-01,2024-02-12,10
u3,2024-02-01,2024-03-01,7
u4,2024-03-01,2024-03-15,3
u1,2024-01-01,2024-03-20,18
u2,2024-01-01,2024-03-25,6
EOF

# === Log Files ===

cat > logs.txt << 'EOF'
2024-03-15 10:23:45 INFO Application started
2024-03-15 10:24:12 ERROR Connection failed
2024-03-16 08:00:00 INFO Daily backup started
2024-03-16 08:15:30 WARN Disk space low
2024-03-17 14:22:01 INFO User login: alice
2024-03-17 14:25:45 ERROR Invalid token
2024-03-18 09:00:00 INFO Scheduled task executed
2024-03-19 11:30:22 DEBUG Cache cleared
2024-03-20 16:45:00 INFO Application stopped
2023-01-01 00:00:00 INFO New Year started
2024-12-25 12:00:00 INFO Holiday mode enabled
EOF

cat > app.log << 'EOF'
2024-03-15 10:23:45 INFO Application started
2024-03-15 10:23:46 DEBUG Loading configuration
2024-03-15 10:23:47 INFO User alice logged in
2024-03-15 10:24:12 ERROR Connection timeout to database
2024-03-15 10:24:15 WARN Retrying connection (attempt 1)
2024-03-15 10:24:18 INFO Connection established
2024-03-15 10:25:01 DEBUG Processing request #1234
2024-03-15 10:25:02 ERROR Invalid request format
2024-03-15 10:26:30 INFO User bob logged in
2024-03-15 10:27:45 DEBUG Cache cleared
2024-03-15 10:28:00 ERROR Failed to send email notification
2024-03-15 10:30:00 INFO Daily backup started
2024-03-15 10:35:00 FATAL Out of memory, shutting down
EOF

cat > access.log << 'EOF'
192.168.1.10 - alice [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:31:02 +0000] "POST /api/login HTTP/1.1" 200 256 "curl/7.64.1"
192.168.1.10 - alice [15/Mar/2024:10:31:15 +0000] "GET /products?id=42 HTTP/1.1" 200 8901 "Mozilla/5.0"
192.168.1.20 - - [15/Mar/2024:10:32:00 +0000] "GET /admin HTTP/1.1" 403 123 "Mozilla/5.0"
192.168.1.15 - bob [15/Mar/2024:10:32:30 +0000] "GET /api/orders HTTP/1.1" 200 4567 "curl/7.64.1"
192.168.1.25 - - [15/Mar/2024:10:33:45 +0000] "GET /missing.html HTTP/1.1" 404 89 "Googlebot/2.1"
192.168.1.10 - alice [15/Mar/2024:10:34:00 +0000] "POST /checkout HTTP/1.1" 500 234 "Mozilla/5.0"
192.168.1.30 - carol [15/Mar/2024:10:35:15 +0000] "GET /api/users HTTP/1.1" 200 2345 "Python-urllib/3.9"
192.168.1.15 - bob [15/Mar/2024:10:36:00 +0000] "POST /api/checkout HTTP/1.1" 200 456 "curl/7.64.1"
EOF

# === JSON Files ===

cat > data.jsonl << 'EOF'
{"name": "Alice", "age": 30, "city": "Moscow"}
{"name": "Bob", "age": 25, "city": "SPb"}
{"name": "Carol", "age": 35, "city": "Kazan"}
{"name": "Dave", "age": 28, "city": "Moscow"}
{"name": "Eve", "age": 32, "city": "Sochi"}
{"name": "Frank", "age": 45, "city": "Novosibirsk"}
EOF

cat > sales.jsonl << 'EOF'
{"date": "2024-03-15", "product": "Phone", "amount": 999, "region": "North"}
{"date": "2024-03-15", "product": "Laptop", "amount": 1499, "region": "South"}
{"date": "2024-03-16", "product": "Shirt", "amount": 45, "region": "East"}
{"date": "2024-03-16", "product": "Phone", "amount": 999, "region": "West"}
{"date": "2024-03-17", "product": "Tablet", "amount": 599, "region": "North"}
{"date": "2024-03-17", "product": "Pants", "amount": 80, "region": "South"}
{"date": "2024-03-18", "product": "Jacket", "amount": 150, "region": "East"}
{"date": "2024-03-18", "product": "Laptop", "amount": 1499, "region": "West"}
EOF

cat > users.json << 'EOF'
[
  {"id": 1, "name": "Alice", "age": 30, "city": "Moscow", "status": "active"},
  {"id": 2, "name": "Bob", "age": 25, "city": "SPb", "status": "active"},
  {"id": 3, "name": "Carol", "age": 35, "city": "Kazan", "status": "inactive"},
  {"id": 4, "name": "Dave", "age": 28, "city": "Moscow", "status": "active"},
  {"id": 5, "name": "Eve", "age": 32, "city": "Sochi", "status": "inactive"},
  {"id": 6, "name": "Frank", "age": 45, "city": "Novosibirsk", "status": "active"}
]
EOF

cat > users.jsonl << 'EOF'
{"id": 1, "name": "Alice", "age": 30, "city": "Moscow", "status": "active"}
{"id": 2, "name": "Bob", "age": 25, "city": "SPb", "status": "active"}
{"id": 3, "name": "Carol", "age": 35, "city": "Kazan", "status": "inactive"}
{"id": 4, "name": "Dave", "age": 28, "city": "Moscow", "status": "active"}
{"id": 5, "name": "Eve", "age": 32, "city": "Sochi", "status": "inactive"}
{"id": 6, "name": "Frank", "age": 45, "city": "Novosibirsk", "status": "active"}
EOF

cat > products.json << 'EOF'
[
  {"id": 1, "name": "Phone", "price": 999, "category": "Electronics"},
  {"id": 2, "name": "Laptop", "price": 1499, "category": "Electronics"},
  {"id": 3, "name": "Shirt", "price": 45, "category": "Clothing"},
  {"id": 4, "name": "Pants", "price": 80, "category": "Clothing"},
  {"id": 5, "name": "Tablet", "price": 599, "category": "Electronics"},
  {"id": 6, "name": "Jacket", "price": 150, "category": "Clothing"}
]
EOF

cat > events.jsonl << 'EOF'
{"timestamp": "2024-03-15T10:30:00Z", "user_id": 1, "type": "login", "session_id": "s001"}
{"timestamp": "2024-03-15T10:35:00Z", "user_id": 1, "type": "purchase", "amount": 999, "product_id": 1}
{"timestamp": "2024-03-15T10:40:00Z", "user_id": 2, "type": "login", "session_id": "s002"}
{"timestamp": "2024-03-15T10:45:00Z", "user_id": 1, "type": "error", "message": "Payment failed"}
{"timestamp": "2024-03-15T10:50:00Z", "user_id": 2, "type": "purchase", "amount": 1499, "product_id": 2}
{"timestamp": "2024-03-15T11:00:00Z", "user_id": 3, "type": "login", "session_id": "s003"}
{"timestamp": "2024-03-15T11:05:00Z", "user_id": 3, "type": "logout", "session_id": "s003"}
EOF

cat > app.jsonl << 'EOF'
{"timestamp": "2024-03-15T10:30:00Z", "level": "INFO", "message": "Application started", "service": "api"}
{"timestamp": "2024-03-15T10:30:05Z", "level": "DEBUG", "message": "Loading configuration", "service": "api"}
{"timestamp": "2024-03-15T10:30:10Z", "level": "INFO", "message": "Database connected", "service": "db"}
{"timestamp": "2024-03-15T10:30:15Z", "level": "ERROR", "message": "Failed to connect to cache", "service": "cache", "error_type": "ConnectionError"}
{"timestamp": "2024-03-15T10:30:20Z", "level": "WARN", "message": "Retrying cache connection", "service": "cache"}
{"timestamp": "2024-03-15T10:30:25Z", "level": "INFO", "message": "Cache connected", "service": "cache"}
{"timestamp": "2024-03-15T10:31:00Z", "level": "INFO", "message": "Request processed", "service": "api", "duration_ms": 45}
{"timestamp": "2024-03-15T10:31:05Z", "level": "ERROR", "message": "Database timeout", "service": "db", "error_type": "TimeoutError"}
{"timestamp": "2024-03-15T10:32:00Z", "level": "ERROR", "message": "Invalid request format", "service": "api", "error_type": "ValidationError"}
EOF

cat > errors.jsonl << 'EOF'
{"timestamp": "2024-03-15T10:30:15Z", "error_type": "ConnectionError", "service": "cache", "message": "Failed to connect to cache server"}
{"timestamp": "2024-03-15T10:31:05Z", "error_type": "TimeoutError", "service": "db", "message": "Database query timeout after 30s"}
{"timestamp": "2024-03-15T10:32:00Z", "error_type": "ValidationError", "service": "api", "message": "Missing required field: user_id"}
{"timestamp": "2024-03-15T10:33:15Z", "error_type": "AuthError", "service": "auth", "message": "Invalid token"}
{"timestamp": "2024-03-15T10:34:00Z", "error_type": "TimeoutError", "service": "db", "message": "Database connection timeout"}
{"timestamp": "2024-03-15T10:35:30Z", "error_type": "ConnectionError", "service": "cache", "message": "Cache server unreachable"}
EOF

cat > sessions.jsonl << 'EOF'
{"session_id": "s001", "user_id": 1, "start_time": "2024-03-15T10:00:00Z", "duration": 1800, "pages": 15}
{"session_id": "s002", "user_id": 2, "start_time": "2024-03-15T10:05:00Z", "duration": 900, "pages": 8}
{"session_id": "s003", "user_id": 1, "start_time": "2024-03-15T11:00:00Z", "duration": 600, "pages": 5}
{"session_id": "s004", "user_id": 3, "start_time": "2024-03-15T11:30:00Z", "duration": 2400, "pages": 22}
{"session_id": "s005", "user_id": 2, "start_time": "2024-03-15T12:00:00Z", "duration": 1200, "pages": 10}
EOF

cat > queries.jsonl << 'EOF'
{"timestamp": "2024-03-15T10:30:00Z", "query": "SELECT * FROM users WHERE id = 1", "duration_ms": 15, "rows": 1}
{"timestamp": "2024-03-15T10:30:05Z", "query": "SELECT * FROM orders WHERE user_id = 1", "duration_ms": 45, "rows": 12}
{"timestamp": "2024-03-15T10:30:10Z", "query": "SELECT * FROM products", "duration_ms": 1250, "rows": 5000}
{"timestamp": "2024-03-15T10:30:15Z", "query": "UPDATE users SET last_login = NOW()", "duration_ms": 8, "rows": 1}
{"timestamp": "2024-03-15T10:30:20Z", "query": "SELECT * FROM logs WHERE date > '2024-03-01'", "duration_ms": 3500, "rows": 100000}
{"timestamp": "2024-03-15T10:30:25Z", "query": "SELECT COUNT(*) FROM sessions", "duration_ms": 120, "rows": 1}
{"timestamp": "2024-03-15T10:30:30Z", "query": "SELECT * FROM analytics WHERE event_type = 'click'", "duration_ms": 2100, "rows": 45000}
EOF

# === Config Files ===

cat > config.yaml << 'EOF'
database:
  host: localhost
  port: 5432
  name: myapp
  user: admin

server:
  host: 0.0.0.0
  port: 8080
  debug: false

logging:
  level: INFO
  format: json
  file: /var/log/app.log

features:
  - name: authentication
    enabled: true
  - name: caching
    enabled: true
    ttl: 3600
EOF

cat > data.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <users>
    <user id="1">
      <name>Alice</name>
      <age>30</age>
      <city>Moscow</city>
    </user>
    <user id="2">
      <name>Bob</name>
      <age>25</age>
      <city>SPb</city>
    </user>
    <user id="3">
      <name>Carol</name>
      <age>35</age>
      <city>Kazan</city>
    </user>
  </users>
  <products>
    <product id="1">
      <name>Phone</name>
      <price>999</price>
    </product>
    <product id="2">
      <name>Laptop</name>
      <price>1499</price>
    </product>
  </products>
</root>
EOF

# === Web Content ===

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
    <p>Phone: +7 (495) 123-45-67</p>
</body>
</html>
EOF

echo "✅ All files created in $(pwd)"
echo ""
echo "Files created:"
ls -la
```

---

## 📊 Data Relationships

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  customers   │────▶│    orders    │◀────│   products   │
│  (1-6)       │     │  (101-110)   │     │   (1-8)      │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │
       ▼                    ▼
┌──────────────┐     ┌──────────────┐
│    users     │     │    sales     │
│  (id,email)  │     │  (aggregated)│
└──────────────┘     └──────────────┘
```

**Common entities across all files:**
- **Users:** Alice, Bob, Carol, Dave, Eve, Frank (id 1-6)
- **Products:** Phone, Laptop, Shirt, Pants, Tablet, Jacket, Apple, Bread (id 1-8)
- **Categories:** Electronics, Clothing, Food
- **Cities:** Moscow, SPb, Kazan, Sochi, Novosibirsk
- **Base date:** 2024-03-15

