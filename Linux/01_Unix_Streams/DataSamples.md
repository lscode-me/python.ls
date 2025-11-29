# Sample Data Files

Create the following files to practice with the lecture examples.

## data.csv
```csv
date,product,amount,category
2024-11-01,Phone,999,Electronics
2024-11-01,Laptop,1499,Electronics
2024-11-02,Shirt,45,Clothing
2024-11-02,Phone,999,Electronics
2024-11-03,Bread,3,Food
2024-11-03,Pants,80,Clothing
2024-11-04,Tablet,599,Electronics
2024-11-04,Jacket,150,Clothing
2024-11-05,Apple,2,Food
2024-11-05,Laptop,1499,Electronics
```

## data.txt
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
```

## numbers.txt
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
```

## app.log
```
2024-11-27 10:23:45 INFO Application started
2024-11-27 10:23:46 DEBUG Loading configuration
2024-11-27 10:23:47 INFO User alice logged in
2024-11-27 10:24:12 ERROR Connection timeout to database
2024-11-27 10:24:15 WARN Retrying connection (attempt 1)
2024-11-27 10:24:18 INFO Connection established
2024-11-27 10:25:01 DEBUG Processing request #1234
2024-11-27 10:25:02 ERROR Invalid request format
2024-11-27 10:26:30 INFO User bob logged in
2024-11-27 10:27:45 DEBUG Cache cleared
2024-11-27 10:28:00 ERROR Failed to send email notification
2024-11-27 10:30:00 INFO Daily backup started
```

## access.log
```
192.168.1.1 - - [27/Nov/2024:10:23:45] "GET /api/users" 200 1234
192.168.1.2 - - [27/Nov/2024:10:24:12] "GET /api/posts" 404 89
192.168.1.1 - - [27/Nov/2024:10:25:01] "POST /api/login" 200 256
192.168.1.3 - - [27/Nov/2024:10:25:30] "GET /api/users" 200 1234
192.168.1.1 - - [27/Nov/2024:10:26:15] "GET /api/products" 200 4567
192.168.1.2 - - [27/Nov/2024:10:27:00] "GET /api/orders" 500 123
192.168.1.4 - - [27/Nov/2024:10:28:30] "GET /index.html" 200 8901
192.168.1.1 - - [27/Nov/2024:10:29:45] "POST /api/logout" 200 64
192.168.1.3 - - [27/Nov/2024:10:30:00] "GET /api/stats" 403 45
192.168.1.5 - - [27/Nov/2024:10:31:15] "GET /api/users" 200 1234
```

---

## Quick File Creation

You can create all files with a single command:

```bash
# Create data directory
mkdir -p ~/stream_data && cd ~/stream_data

# data.csv
cat > data.csv << 'EOF'
date,product,amount,category
2024-11-01,Phone,999,Electronics
2024-11-01,Laptop,1499,Electronics
2024-11-02,Shirt,45,Clothing
2024-11-02,Phone,999,Electronics
2024-11-03,Bread,3,Food
2024-11-03,Pants,80,Clothing
2024-11-04,Tablet,599,Electronics
2024-11-04,Jacket,150,Clothing
2024-11-05,Apple,2,Food
2024-11-05,Laptop,1499,Electronics
EOF

# data.txt
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
EOF

# numbers.txt
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
EOF

# app.log
cat > app.log << 'EOF'
2024-11-27 10:23:45 INFO Application started
2024-11-27 10:23:46 DEBUG Loading configuration
2024-11-27 10:23:47 INFO User alice logged in
2024-11-27 10:24:12 ERROR Connection timeout to database
2024-11-27 10:24:15 WARN Retrying connection (attempt 1)
2024-11-27 10:24:18 INFO Connection established
2024-11-27 10:25:01 DEBUG Processing request #1234
2024-11-27 10:25:02 ERROR Invalid request format
2024-11-27 10:26:30 INFO User bob logged in
2024-11-27 10:27:45 DEBUG Cache cleared
2024-11-27 10:28:00 ERROR Failed to send email notification
2024-11-27 10:30:00 INFO Daily backup started
EOF

# access.log
cat > access.log << 'EOF'
192.168.1.1 - - [27/Nov/2024:10:23:45] "GET /api/users" 200 1234
192.168.1.2 - - [27/Nov/2024:10:24:12] "GET /api/posts" 404 89
192.168.1.1 - - [27/Nov/2024:10:25:01] "POST /api/login" 200 256
192.168.1.3 - - [27/Nov/2024:10:25:30] "GET /api/users" 200 1234
192.168.1.1 - - [27/Nov/2024:10:26:15] "GET /api/products" 200 4567
192.168.1.2 - - [27/Nov/2024:10:27:00] "GET /api/orders" 500 123
192.168.1.4 - - [27/Nov/2024:10:28:30] "GET /index.html" 200 8901
192.168.1.1 - - [27/Nov/2024:10:29:45] "POST /api/logout" 200 64
192.168.1.3 - - [27/Nov/2024:10:30:00] "GET /api/stats" 403 45
192.168.1.5 - - [27/Nov/2024:10:31:15] "GET /api/users" 200 1234
EOF

echo "All files created in $(pwd)"
ls -la
```


