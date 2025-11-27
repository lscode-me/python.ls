# Sample Data Files

Create the following files to practice with the lecture examples.

## customers.csv
```csv
customer_id,name,city
1,Alice,Moscow
2,Bob,SPb
3,Carol,Kazan
4,Dave,Moscow
5,Eve,Sochi
```

## orders.csv
```csv
customer_id,order_id,amount,date
1,101,250,2024-01-15
1,102,180,2024-01-20
2,103,420,2024-01-18
3,104,95,2024-01-22
1,105,310,2024-02-01
4,106,150,2024-02-05
2,107,280,2024-02-10
5,108,520,2024-02-12
3,109,175,2024-02-15
```

## left.csv
```csv
id,name,department
1,Alice,Engineering
2,Bob,Marketing
3,Carol,Engineering
4,Dave,Sales
```

## right.csv
```csv
id,salary,start_date
1,75000,2020-03-15
2,65000,2021-06-01
3,80000,2019-11-20
5,55000,2022-01-10
```

## lookup.csv
```csv
code,description
A,Active
I,Inactive
P,Pending
D,Deleted
```

## data.csv
```csv
category,product,revenue,quantity
Electronics,Phone,1200,3
Clothing,Shirt,45,10
Electronics,Laptop,2500,2
Clothing,Pants,80,5
Food,Apple,3,50
Electronics,Tablet,800,4
Food,Bread,2,100
Clothing,Jacket,150,3
```

## products.csv
```csv
category,product,price,rating
Electronics,Phone,999,4.5
Electronics,Laptop,1499,4.8
Electronics,Tablet,599,4.2
Clothing,Shirt,29,4.0
Clothing,Pants,59,4.3
Clothing,Jacket,149,4.7
Food,Apple,1,4.9
Food,Bread,3,4.6
```

## sales.csv
```csv
product,revenue,quantity,date
Phone,2997,3,2024-01-15
Laptop,2998,2,2024-01-16
Shirt,145,5,2024-01-17
Phone,999,1,2024-01-18
Pants,236,4,2024-01-19
Laptop,1499,1,2024-01-20
```

## events.jsonl
```jsonl
{"user_id":"u1","session_id":"s1","amount":25.50,"timestamp":"2024-01-15T10:30:00","type":"purchase","duration":120,"page_count":5}
{"user_id":"u2","session_id":"s2","amount":18.00,"timestamp":"2024-01-15T11:45:00","type":"purchase","duration":90,"page_count":3}
{"user_id":"u1","session_id":"s1","amount":42.00,"timestamp":"2024-01-15T12:00:00","type":"purchase","duration":120,"page_count":5}
{"user_id":"u3","session_id":"s3","amount":0,"timestamp":"2024-01-15T14:20:00","type":"error","duration":15,"page_count":1}
{"user_id":"u2","session_id":"s4","amount":89.99,"timestamp":"2024-01-16T09:15:00","type":"purchase","duration":180,"page_count":8}
{"user_id":"u1","session_id":"s5","amount":33.00,"timestamp":"2024-01-16T10:30:00","type":"purchase","duration":60,"page_count":2}
```

## numbers.txt
```
42
58
31
45
67
89
23
56
78
34
91
12
```

## access.log
```
192.168.1.10 - - [15/Jan/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.15 - - [15/Jan/2024:10:30:52 +0000] "GET /api/users HTTP/1.1" 200 5678
192.168.1.10 - - [15/Jan/2024:10:31:01 +0000] "POST /api/login HTTP/1.1" 200 234
192.168.1.20 - - [15/Jan/2024:10:31:15 +0000] "GET /products HTTP/1.1" 200 8901
192.168.1.15 - - [15/Jan/2024:10:32:03 +0000] "GET /api/orders HTTP/1.1" 200 4567
192.168.1.10 - - [15/Jan/2024:10:32:45 +0000] "GET /checkout HTTP/1.1" 200 2345
192.168.1.25 - - [15/Jan/2024:10:33:12 +0000] "GET /index.html HTTP/1.1" 200 1234
```

## user_activity.csv
```csv
user_id,signup_date,activity_date,actions
u1,2024-01-01,2024-01-05,12
u2,2024-01-01,2024-01-08,8
u1,2024-01-01,2024-02-10,15
u3,2024-02-01,2024-02-05,5
u2,2024-01-01,2024-02-12,10
u3,2024-02-01,2024-03-01,7
u4,2024-03-01,2024-03-15,3
```

## matrix.csv
```csv
a,b,c
1,2,3
4,5,6
7,8,9
```

---

## Quick File Creation

You can create all files with a single command:

```bash
# Create data directory
mkdir -p ~/streaming_data && cd ~/streaming_data

# customers.csv
cat > customers.csv << 'EOF'
customer_id,name,city
1,Alice,Moscow
2,Bob,SPb
3,Carol,Kazan
4,Dave,Moscow
5,Eve,Sochi
EOF

# orders.csv
cat > orders.csv << 'EOF'
customer_id,order_id,amount,date
1,101,250,2024-01-15
1,102,180,2024-01-20
2,103,420,2024-01-18
3,104,95,2024-01-22
1,105,310,2024-02-01
4,106,150,2024-02-05
2,107,280,2024-02-10
5,108,520,2024-02-12
3,109,175,2024-02-15
EOF

# left.csv
cat > left.csv << 'EOF'
id,name,department
1,Alice,Engineering
2,Bob,Marketing
3,Carol,Engineering
4,Dave,Sales
EOF

# right.csv
cat > right.csv << 'EOF'
id,salary,start_date
1,75000,2020-03-15
2,65000,2021-06-01
3,80000,2019-11-20
5,55000,2022-01-10
EOF

# lookup.csv
cat > lookup.csv << 'EOF'
code,description
A,Active
I,Inactive
P,Pending
D,Deleted
EOF

# data.csv
cat > data.csv << 'EOF'
category,product,revenue,quantity
Electronics,Phone,1200,3
Clothing,Shirt,45,10
Electronics,Laptop,2500,2
Clothing,Pants,80,5
Food,Apple,3,50
Electronics,Tablet,800,4
Food,Bread,2,100
Clothing,Jacket,150,3
EOF

# products.csv
cat > products.csv << 'EOF'
category,product,price,rating
Electronics,Phone,999,4.5
Electronics,Laptop,1499,4.8
Electronics,Tablet,599,4.2
Clothing,Shirt,29,4.0
Clothing,Pants,59,4.3
Clothing,Jacket,149,4.7
Food,Apple,1,4.9
Food,Bread,3,4.6
EOF

# sales.csv
cat > sales.csv << 'EOF'
product,revenue,quantity,date
Phone,2997,3,2024-01-15
Laptop,2998,2,2024-01-16
Shirt,145,5,2024-01-17
Phone,999,1,2024-01-18
Pants,236,4,2024-01-19
Laptop,1499,1,2024-01-20
EOF

# events.jsonl
cat > events.jsonl << 'EOF'
{"user_id":"u1","session_id":"s1","amount":25.50,"timestamp":"2024-01-15T10:30:00","type":"purchase","duration":120,"page_count":5}
{"user_id":"u2","session_id":"s2","amount":18.00,"timestamp":"2024-01-15T11:45:00","type":"purchase","duration":90,"page_count":3}
{"user_id":"u1","session_id":"s1","amount":42.00,"timestamp":"2024-01-15T12:00:00","type":"purchase","duration":120,"page_count":5}
{"user_id":"u3","session_id":"s3","amount":0,"timestamp":"2024-01-15T14:20:00","type":"error","duration":15,"page_count":1}
{"user_id":"u2","session_id":"s4","amount":89.99,"timestamp":"2024-01-16T09:15:00","type":"purchase","duration":180,"page_count":8}
{"user_id":"u1","session_id":"s5","amount":33.00,"timestamp":"2024-01-16T10:30:00","type":"purchase","duration":60,"page_count":2}
EOF

# numbers.txt
cat > numbers.txt << 'EOF'
42
58
31
45
67
89
23
56
78
34
91
12
EOF

# access.log
cat > access.log << 'EOF'
192.168.1.10 - - [15/Jan/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.15 - - [15/Jan/2024:10:30:52 +0000] "GET /api/users HTTP/1.1" 200 5678
192.168.1.10 - - [15/Jan/2024:10:31:01 +0000] "POST /api/login HTTP/1.1" 200 234
192.168.1.20 - - [15/Jan/2024:10:31:15 +0000] "GET /products HTTP/1.1" 200 8901
192.168.1.15 - - [15/Jan/2024:10:32:03 +0000] "GET /api/orders HTTP/1.1" 200 4567
192.168.1.10 - - [15/Jan/2024:10:32:45 +0000] "GET /checkout HTTP/1.1" 200 2345
192.168.1.25 - - [15/Jan/2024:10:33:12 +0000] "GET /index.html HTTP/1.1" 200 1234
EOF

# user_activity.csv
cat > user_activity.csv << 'EOF'
user_id,signup_date,activity_date,actions
u1,2024-01-01,2024-01-05,12
u2,2024-01-01,2024-01-08,8
u1,2024-01-01,2024-02-10,15
u3,2024-02-01,2024-02-05,5
u2,2024-01-01,2024-02-12,10
u3,2024-02-01,2024-03-01,7
u4,2024-03-01,2024-03-15,3
EOF

# matrix.csv
cat > matrix.csv << 'EOF'
a,b,c
1,2,3
4,5,6
7,8,9
EOF

echo "All files created in $(pwd)"
ls -la
```

