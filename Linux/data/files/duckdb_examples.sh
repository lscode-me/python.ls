#!/bin/bash
# DuckDB Examples using sample data files

echo "=== DuckDB Quick Start Examples ==="
echo ""

# Example 1: Query users
echo "1. Query active users:"
duckdb -markdown -c "SELECT * FROM 'users.csv' WHERE status = 'active'"
echo ""

# Example 2: Aggregate products by category
echo "2. Products statistics by category:"
duckdb -markdown -c "
  SELECT 
    category,
    COUNT(*) as product_count,
    ROUND(AVG(price), 2) as avg_price,
    MIN(price) as min_price,
    MAX(price) as max_price
  FROM 'products.csv'
  GROUP BY category
  ORDER BY category
"
echo ""

# Example 3: Join users and orders
echo "3. Top customers by total spending:"
duckdb -markdown -c "
  SELECT 
    u.name,
    u.city,
    COUNT(o.order_id) as order_count,
    SUM(o.amount) as total_spent
  FROM 'users.csv' u
  JOIN 'orders.csv' o ON u.id = o.customer_id
  GROUP BY u.name, u.city
  ORDER BY total_spent DESC
  LIMIT 5
"
echo ""

# Example 4: Three-way join
echo "4. Complete order details (users + orders + products):"
duckdb -markdown -c "
  SELECT 
    u.name as customer,
    p.name as product,
    o.quantity,
    o.amount,
    o.date
  FROM 'orders.csv' o
  JOIN 'users.csv' u ON o.customer_id = u.id
  JOIN 'products.csv' p ON o.product_id = p.id
  ORDER BY o.date DESC
  LIMIT 10
"
echo ""

# Example 5: Window function - Product ranking
echo "5. Products ranked by price within each category:"
duckdb -markdown -c "
  SELECT 
    category,
    name,
    price,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as rank
  FROM 'products.csv'
  ORDER BY category, rank
"
echo ""

# Example 6: Running total per customer
echo "6. Customer orders with running total:"
duckdb -markdown -c "
  SELECT 
    customer_id,
    date,
    amount,
    SUM(amount) OVER (
      PARTITION BY customer_id 
      ORDER BY date
    ) as running_total
  FROM 'orders.csv'
  ORDER BY customer_id, date
"
echo ""

# Example 7: Find customers with no orders
echo "7. Customers with no orders (LEFT JOIN):"
duckdb -markdown -c "
  SELECT 
    u.id,
    u.name,
    u.email,
    u.status
  FROM 'users.csv' u
  LEFT JOIN 'orders.csv' o ON u.id = o.customer_id
  WHERE o.order_id IS NULL
"
echo ""

# Example 8: Top product per category
echo "8. Most expensive product in each category:"
duckdb -markdown -c "
  WITH ranked AS (
    SELECT 
      category,
      name,
      price,
      ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as rn
    FROM 'products.csv'
  )
  SELECT category, name, price
  FROM ranked
  WHERE rn = 1
"
echo ""

# Example 9: Export results to CSV
echo "9. Exporting active users to CSV:"
duckdb -c "
  COPY (
    SELECT * FROM 'users.csv' WHERE status = 'active'
  ) TO 'active_users_export.csv' (HEADER, DELIMITER ',')
"
echo "✓ Exported to active_users_export.csv"
echo ""

# Example 10: Create Parquet file (compressed, fast)
echo "10. Converting CSV to Parquet:"
duckdb -c "
  COPY (
    SELECT * FROM 'users.csv'
  ) TO 'users.parquet' (FORMAT PARQUET)
"
echo "✓ Created users.parquet"

# Query the parquet file
echo ""
echo "Reading from Parquet:"
duckdb -markdown -c "SELECT * FROM 'users.parquet' LIMIT 3"
echo ""

# Cleanup
rm -f active_users_export.csv users.parquet

echo "=== Examples complete! ==="
echo ""
echo "Try modifying these queries or create your own!"
echo "Learn more: https://duckdb.org/docs/"

