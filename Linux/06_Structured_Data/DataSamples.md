# Sample Data Files

Create the following files to practice with the lecture examples.

## users.json
```json
[
  {"id": 1, "name": "Alice", "age": 30, "city": "NYC", "status": "active"},
  {"id": 2, "name": "Bob", "age": 25, "city": "LA", "status": "active"},
  {"id": 3, "name": "Carol", "age": 35, "city": "Chicago", "status": "inactive"},
  {"id": 4, "name": "Dave", "age": 28, "city": "Houston", "status": "active"},
  {"id": 5, "name": "Eve", "age": 32, "city": "Phoenix", "status": "inactive"}
]
```

## users.jsonl
```jsonl
{"id": 1, "name": "Alice", "age": 30, "city": "NYC", "status": "active"}
{"id": 2, "name": "Bob", "age": 25, "city": "LA", "status": "active"}
{"id": 3, "name": "Carol", "age": 35, "city": "Chicago", "status": "inactive"}
{"id": 4, "name": "Dave", "age": 28, "city": "Houston", "status": "active"}
{"id": 5, "name": "Eve", "age": 32, "city": "Phoenix", "status": "inactive"}
```

## products.json
```json
[
  {"id": 1, "name": "Phone", "price": 999, "category": "Electronics"},
  {"id": 2, "name": "Laptop", "price": 1499, "category": "Electronics"},
  {"id": 3, "name": "Shirt", "price": 45, "category": "Clothing"},
  {"id": 4, "name": "Tablet", "price": 599, "category": "Electronics"},
  {"id": 5, "name": "Pants", "price": 80, "category": "Clothing"},
  {"id": 6, "name": "Headphones", "price": 199, "category": "Electronics"}
]
```

## events.jsonl
```jsonl
{"timestamp": "2024-03-15T10:30:00Z", "user_id": "u1", "type": "login", "amount": 0}
{"timestamp": "2024-03-15T10:35:00Z", "user_id": "u1", "type": "purchase", "amount": 99.50}
{"timestamp": "2024-03-15T10:40:00Z", "user_id": "u2", "type": "login", "amount": 0}
{"timestamp": "2024-03-15T10:45:00Z", "user_id": "u1", "type": "error", "amount": 0}
{"timestamp": "2024-03-15T10:50:00Z", "user_id": "u2", "type": "purchase", "amount": 149.99}
{"timestamp": "2024-03-15T11:00:00Z", "user_id": "u3", "type": "login", "amount": 0}
```

## sales.jsonl
```jsonl
{"date": "2024-03-01", "product": "Widget A", "amount": 2550.00}
{"date": "2024-03-01", "product": "Widget B", "amount": 2250.00}
{"date": "2024-03-02", "product": "Widget A", "amount": 1912.50}
{"date": "2024-03-02", "product": "Widget C", "amount": 3600.00}
{"date": "2024-03-03", "product": "Widget B", "amount": 3600.00}
```

## data.csv
```csv
id,name,age,city,status
1,Alice,30,NYC,active
2,Bob,25,LA,active
3,Carol,35,Chicago,inactive
4,Dave,28,Houston,active
5,Eve,32,Phoenix,inactive
```

## sales.csv
```csv
date,product,quantity,price,customer
2024-03-01,Widget A,100,25.50,ACME Corp
2024-03-01,Widget B,50,45.00,TechStart
2024-03-02,Widget A,75,25.50,GlobalInc
2024-03-02,Widget C,30,120.00,ACME Corp
2024-03-03,Widget B,80,45.00,TechStart
```

## config.yaml
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

## data.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <users>
    <user id="1">
      <name>Alice</name>
      <age>30</age>
      <city>NYC</city>
    </user>
    <user id="2">
      <name>Bob</name>
      <age>25</age>
      <city>LA</city>
    </user>
    <user id="3">
      <name>Carol</name>
      <age>35</age>
      <city>Chicago</city>
    </user>
  </users>
  <products>
    <product id="101">
      <name>Phone</name>
      <price>999</price>
    </product>
    <product id="102">
      <name>Laptop</name>
      <price>1499</price>
    </product>
  </products>
</root>
```

---

## Quick File Creation

You can create all files with a single command:

```bash
# Create data directory
mkdir -p ~/structured_data && cd ~/structured_data

# users.json
cat > users.json << 'EOF'
[
  {"id": 1, "name": "Alice", "age": 30, "city": "NYC", "status": "active"},
  {"id": 2, "name": "Bob", "age": 25, "city": "LA", "status": "active"},
  {"id": 3, "name": "Carol", "age": 35, "city": "Chicago", "status": "inactive"},
  {"id": 4, "name": "Dave", "age": 28, "city": "Houston", "status": "active"},
  {"id": 5, "name": "Eve", "age": 32, "city": "Phoenix", "status": "inactive"}
]
EOF

# users.jsonl
cat > users.jsonl << 'EOF'
{"id": 1, "name": "Alice", "age": 30, "city": "NYC", "status": "active"}
{"id": 2, "name": "Bob", "age": 25, "city": "LA", "status": "active"}
{"id": 3, "name": "Carol", "age": 35, "city": "Chicago", "status": "inactive"}
{"id": 4, "name": "Dave", "age": 28, "city": "Houston", "status": "active"}
{"id": 5, "name": "Eve", "age": 32, "city": "Phoenix", "status": "inactive"}
EOF

# products.json
cat > products.json << 'EOF'
[
  {"id": 1, "name": "Phone", "price": 999, "category": "Electronics"},
  {"id": 2, "name": "Laptop", "price": 1499, "category": "Electronics"},
  {"id": 3, "name": "Shirt", "price": 45, "category": "Clothing"},
  {"id": 4, "name": "Tablet", "price": 599, "category": "Electronics"},
  {"id": 5, "name": "Pants", "price": 80, "category": "Clothing"},
  {"id": 6, "name": "Headphones", "price": 199, "category": "Electronics"}
]
EOF

# events.jsonl
cat > events.jsonl << 'EOF'
{"timestamp": "2024-03-15T10:30:00Z", "user_id": "u1", "type": "login", "amount": 0}
{"timestamp": "2024-03-15T10:35:00Z", "user_id": "u1", "type": "purchase", "amount": 99.50}
{"timestamp": "2024-03-15T10:40:00Z", "user_id": "u2", "type": "login", "amount": 0}
{"timestamp": "2024-03-15T10:45:00Z", "user_id": "u1", "type": "error", "amount": 0}
{"timestamp": "2024-03-15T10:50:00Z", "user_id": "u2", "type": "purchase", "amount": 149.99}
{"timestamp": "2024-03-15T11:00:00Z", "user_id": "u3", "type": "login", "amount": 0}
EOF

# sales.jsonl
cat > sales.jsonl << 'EOF'
{"date": "2024-03-01", "product": "Widget A", "amount": 2550.00}
{"date": "2024-03-01", "product": "Widget B", "amount": 2250.00}
{"date": "2024-03-02", "product": "Widget A", "amount": 1912.50}
{"date": "2024-03-02", "product": "Widget C", "amount": 3600.00}
{"date": "2024-03-03", "product": "Widget B", "amount": 3600.00}
EOF

# data.csv
cat > data.csv << 'EOF'
id,name,age,city,status
1,Alice,30,NYC,active
2,Bob,25,LA,active
3,Carol,35,Chicago,inactive
4,Dave,28,Houston,active
5,Eve,32,Phoenix,inactive
EOF

# sales.csv
cat > sales.csv << 'EOF'
date,product,quantity,price,customer
2024-03-01,Widget A,100,25.50,ACME Corp
2024-03-01,Widget B,50,45.00,TechStart
2024-03-02,Widget A,75,25.50,GlobalInc
2024-03-02,Widget C,30,120.00,ACME Corp
2024-03-03,Widget B,80,45.00,TechStart
EOF

# config.yaml
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

# data.xml
cat > data.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <users>
    <user id="1">
      <name>Alice</name>
      <age>30</age>
      <city>NYC</city>
    </user>
    <user id="2">
      <name>Bob</name>
      <age>25</age>
      <city>LA</city>
    </user>
    <user id="3">
      <name>Carol</name>
      <age>35</age>
      <city>Chicago</city>
    </user>
  </users>
  <products>
    <product id="101">
      <name>Phone</name>
      <price>999</price>
    </product>
    <product id="102">
      <name>Laptop</name>
      <price>1499</price>
    </product>
  </products>
</root>
EOF

echo "All files created in $(pwd)"
ls -la
```

