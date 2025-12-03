# Homework: Coroutines and Data Pipelines

## Task 1: Basic Coroutines (Easy)

Implement simple coroutines to understand the `send()` pattern.

### 1.1 Echo with Counter

Create a coroutine that echoes received values and counts them:

```python
def echo_counter():
    """
    Coroutine that prints received values and their count
    
    Example:
    >>> ec = echo_counter()
    >>> next(ec)
    >>> ec.send("hello")
    1: hello
    >>> ec.send("world")
    2: world
    """
    # Your code here
    pass
```

**Test:**
```python
ec = echo_counter()
next(ec)
ec.send("apple")   # 1: apple
ec.send("banana")  # 2: banana
ec.send("cherry")  # 3: cherry
```

### 1.2 Min/Max Tracker

Create a coroutine that tracks min and max values:

```python
def minmax():
    """
    Returns current (min, max) and accepts new values
    
    Example:
    >>> mm = minmax()
    >>> next(mm)
    (None, None)
    >>> mm.send(10)
    (10, 10)
    >>> mm.send(5)
    (5, 10)
    >>> mm.send(15)
    (5, 15)
    """
    # Your code here
    pass
```

**Test:**
```python
mm = minmax()
print(next(mm))      # (None, None)
print(mm.send(10))   # (10, 10)
print(mm.send(5))    # (5, 10)
print(mm.send(20))   # (5, 20)
print(mm.send(3))    # (3, 20)
```

### 1.3 Running Sum

Create a coroutine that maintains a running sum:

```python
def running_sum():
    """
    Accumulates values and yields running total
    
    Example:
    >>> rs = running_sum()
    >>> next(rs)
    0
    >>> rs.send(10)
    10
    >>> rs.send(20)
    30
    """
    # Your code here
    pass
```

## Task 2: Pipeline Components (Medium)

Implement reusable pipeline components using the `@coroutine` decorator.

### 2.1 Auto-Priming Decorator

```python
def coroutine(func):
    """Decorator that automatically primes coroutines"""
    # Your code here
    pass
```

### 2.2 Deduplicator

Create a component that filters out duplicate items:

```python
@coroutine
def deduplicate(key_func=None, target=None):
    """
    Filter out duplicate items
    
    Args:
        key_func: Function to extract comparison key (default: identity)
        target: Target coroutine
    
    Example:
    >>> sink = printer()
    >>> dedup = deduplicate(target=sink)
    >>> dedup.send(1)    # prints 1
    >>> dedup.send(2)    # prints 2
    >>> dedup.send(1)    # skipped (duplicate)
    >>> dedup.send(3)    # prints 3
    """
    # Your code here
    pass
```

### 2.3 Throttle

Create a rate limiter that passes at most N items per time window:

```python
@coroutine
def throttle(max_items, window_seconds, target):
    """
    Rate limiter: pass max_items per window_seconds
    
    Args:
        max_items: Maximum items to pass in window
        window_seconds: Time window in seconds
        target: Target coroutine
    
    Example:
    >>> sink = printer()
    >>> limiter = throttle(max_items=2, window_seconds=1, target=sink)
    >>> limiter.send("A")  # passes
    >>> limiter.send("B")  # passes
    >>> limiter.send("C")  # blocked (rate limit)
    """
    # Your code here
    pass
```

### 2.4 Window Aggregator

Create a component that aggregates items into time-based windows:

```python
@coroutine
def time_window(seconds, aggregate_func, target):
    """
    Aggregate items in time windows
    
    Args:
        seconds: Window size in seconds
        aggregate_func: Function to aggregate items (e.g., sum, max, len)
        target: Target coroutine
    
    Example:
    >>> sink = printer()
    >>> window = time_window(seconds=1, aggregate_func=sum, target=sink)
    >>> window.send(10)
    >>> window.send(20)
    >>> # After 1 second, prints 30
    """
    # Your code here
    pass
```

## Task 3: CSV to JSON Converter (Medium)

Create a pipeline that converts CSV to JSON with filtering and transformation.

**Input CSV:**
```csv
name,age,city,salary
Alice,30,NYC,100000
Bob,25,LA,80000
Charlie,35,NYC,120000
Diana,28,Chicago,90000
```

**Requirements:**
1. Parse CSV lines
2. Filter: only people from NYC
3. Transform: convert salary to integer, add `senior` field (age >= 30)
4. Output as JSON

**Your implementation:**

```python
import sys
import csv
import json
from io import StringIO

def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def csv_to_json_pipeline():
    """
    Build pipeline: CSV → filter NYC → transform → JSON
    
    Usage:
    >>> pipeline = csv_to_json_pipeline()
    >>> pipeline.send("Alice,30,NYC,100000")
    {"name": "Alice", "age": 30, "city": "NYC", "salary": 100000, "senior": true}
    """
    # Your code here
    pass

# Test
if __name__ == "__main__":
    pipeline = csv_to_json_pipeline()
    
    data = [
        "name,age,city,salary",
        "Alice,30,NYC,100000",
        "Bob,25,LA,80000",
        "Charlie,35,NYC,120000",
        "Diana,28,Chicago,90000",
    ]
    
    for line in data[1:]:  # Skip header
        pipeline.send(line)
```

**Expected output:**
```json
{"name": "Alice", "age": 30, "city": "NYC", "salary": 100000, "senior": true}
{"name": "Charlie", "age": 35, "city": "NYC", "salary": 120000, "senior": true}
```

## Task 4: Log Analyzer (Hard)

Build a complete log analysis pipeline with multiple features.

**Log format:**
```
2025-12-03 10:30:45 INFO [auth] User john logged in
2025-12-03 10:30:46 ERROR [db] Connection timeout after 30s
2025-12-03 10:30:47 WARN [cache] Cache miss for key: user_123
```

**Requirements:**

### 4.1 Parser

```python
import re

def parse_log_line(line):
    """
    Parse log line into dict
    
    Returns:
        {
            'timestamp': '2025-12-03 10:30:45',
            'level': 'INFO',
            'module': 'auth',
            'message': 'User john logged in'
        }
    """
    # Your code here
    pass
```

### 4.2 Pipeline Components

Implement these components:

```python
@coroutine
def filter_level(levels, target):
    """Filter by log level (can be list)"""
    pass

@coroutine
def extract_usernames(target):
    """Extract username from messages containing 'user <name>'"""
    pass

@coroutine
def count_by_field(field, target=None):
    """Count occurrences by field value"""
    pass

@coroutine
def alert_on_error_rate(threshold, window_size, alert_func):
    """Trigger alert if error rate exceeds threshold"""
    pass
```

### 4.3 Main Pipeline

Build a pipeline that:
1. Parses log lines
2. Filters ERROR and WARN levels
3. Extracts usernames
4. Counts errors by module
5. Alerts if error rate > 10 per minute
6. Outputs JSON

```python
def build_log_analyzer():
    """
    Build complete log analysis pipeline
    
    Returns entry point coroutine
    """
    # Your code here
    pass

# Test
if __name__ == "__main__":
    logs = [
        "2025-12-03 10:30:45 INFO [auth] User john logged in",
        "2025-12-03 10:30:46 ERROR [db] Connection timeout",
        "2025-12-03 10:30:47 ERROR [db] Query failed for user alice",
        "2025-12-03 10:30:48 WARN [cache] Cache miss",
        "2025-12-03 10:30:49 ERROR [api] Invalid request from user bob",
    ]
    
    pipeline = build_log_analyzer()
    for log in logs:
        pipeline.send(log)
```

## Task 5: Streaming Statistics (Hard)

Implement a real-time statistics collector for streaming data.

**Requirements:**

```python
@coroutine
def streaming_stats(window_size=100, target=None):
    """
    Calculate statistics over sliding window
    
    Computes:
    - count
    - mean
    - min/max
    - standard deviation
    - percentiles (50th, 95th, 99th)
    
    Args:
        window_size: Size of sliding window
        target: Optional target to pass stats through
    
    Returns:
        Stats dict on each send()
    """
    # Your code here
    pass

# Test
if __name__ == "__main__":
    import random
    
    stats = streaming_stats(window_size=10)
    
    for i in range(20):
        value = random.randint(1, 100)
        result = stats.send(value)
        print(f"Value: {value:3d} | Stats: {result}")
```

**Expected output format:**
```python
{
    'count': 10,
    'mean': 45.2,
    'min': 5,
    'max': 98,
    'std': 28.3,
    'p50': 42,
    'p95': 89,
    'p99': 96
}
```

## Task 6: Multi-Consumer Pipeline (Hard)

Build a pipeline with multiple consumers (broadcasting).

**Scenario:** Process web server logs and:
1. Write all logs to `all.log`
2. Write errors to `errors.log`
3. Count requests by status code
4. Alert on high error rate
5. Generate real-time dashboard data

```python
@coroutine
def multi_output_pipeline():
    """
    Build pipeline with multiple consumers:
    
    source → parser → [tee] → file_writer(all.log)
                         ├→ error_filter → file_writer(errors.log)
                         ├→ status_counter → dashboard
                         └→ alert_monitor
    """
    # Your code here
    pass
```

**Test with sample logs:**
```python
logs = [
    '192.168.1.1 - - [03/Dec/2025:10:30:45] "GET /api/users HTTP/1.1" 200 1234',
    '192.168.1.2 - - [03/Dec/2025:10:30:46] "POST /api/login HTTP/1.1" 401 89',
    '192.168.1.3 - - [03/Dec/2025:10:30:47] "GET /api/data HTTP/1.1" 500 234',
]
```

## Task 7: Custom Pipeline Operators (Expert)

Create a mini-framework for building pipelines with operator overloading.

```python
class PipelineStage:
    """Base class for pipeline stages"""
    
    def __init__(self, coroutine):
        self.coroutine = coroutine
    
    def __rshift__(self, other):
        """Enable >> operator for chaining"""
        # Your code here
        pass
    
    def send(self, item):
        self.coroutine.send(item)
    
    def close(self):
        self.coroutine.close()

# Example usage:
# pipeline = Source() >> Filter(predicate) >> Map(transform) >> Sink()
```

**Implement these operators:**

```python
class Filter(PipelineStage):
    """Filter stage"""
    def __init__(self, predicate):
        # Your code here
        pass

class Map(PipelineStage):
    """Map/transform stage"""
    def __init__(self, func):
        # Your code here
        pass

class Tee(PipelineStage):
    """Broadcast to multiple targets"""
    def __init__(self, *targets):
        # Your code here
        pass

class Sink(PipelineStage):
    """Terminal stage"""
    def __init__(self, handler=print):
        # Your code here
        pass
```

**Usage example:**
```python
pipeline = (
    Source() 
    >> Filter(lambda x: x > 0) 
    >> Map(lambda x: x * 2) 
    >> Sink()
)

for value in [-5, 10, -3, 20]:
    pipeline.send(value)

# Output: 20, 40
```

## Task 8: Real-Time Data Processor (Expert)

Build a production-ready real-time data processing system.

**Requirements:**
1. Read from multiple sources (files, network, stdin)
2. Parse different formats (JSON, CSV, log lines)
3. Apply transformations and filters
4. Aggregate data in time windows
5. Output to multiple sinks (file, database, API)
6. Handle errors gracefully
7. Collect metrics and statistics
8. Support hot-reloading of configuration

```python
class DataProcessor:
    """Real-time data processing system"""
    
    def __init__(self, config_file):
        """
        Load configuration and build pipeline
        
        Config format (YAML):
        sources:
          - type: file
            path: /var/log/app.log
            format: log
          - type: stdin
            format: json
        
        pipeline:
          - type: filter
            condition: level == 'ERROR'
          - type: map
            function: extract_fields
          - type: window
            size: 60
            aggregate: count
        
        sinks:
          - type: file
            path: /tmp/output.json
          - type: http
            url: https://api.example.com/logs
        """
        # Your code here
        pass
    
    def run(self):
        """Start processing"""
        pass
    
    def stop(self):
        """Graceful shutdown"""
        pass
```

## Bonus: Performance Challenge

Optimize a coroutine pipeline to process **1 million records per second**.

**Task:** Process a stream of dictionaries:
- Filter by field value
- Transform 3 fields
- Calculate running statistics
- Write to file

**Constraints:**
- Must use coroutines
- Must process 1M records/sec on modern laptop
- Memory usage < 100MB

```python
def optimized_pipeline():
    """
    High-performance pipeline for 1M+ records/sec
    
    Optimize:
    - Minimize function calls
    - Use efficient data structures
    - Batch operations where possible
    - Profile and eliminate bottlenecks
    """
    # Your code here
    pass
```

## Submission Guidelines

1. **Code Quality:**
   - Use type hints
   - Add docstrings
   - Follow PEP 8
   - Handle errors

2. **Testing:**
   - Include test cases
   - Test edge cases
   - Verify memory usage

3. **Documentation:**
   - Explain your design choices
   - Document any assumptions
   - Include usage examples

4. **Files to submit:**
   - `task1.py` through `task8.py`
   - `README.md` with instructions
   - `tests/` directory with test files

## Grading Rubric

| Task | Points | Criteria |
|------|--------|----------|
| 1 | 10 | Basic coroutines work correctly |
| 2 | 15 | Pipeline components are reusable |
| 3 | 15 | CSV→JSON pipeline complete |
| 4 | 20 | Log analyzer with all features |
| 5 | 15 | Statistics calculations correct |
| 6 | 10 | Multi-consumer pipeline works |
| 7 | 10 | Operator overloading elegant |
| 8 | 5 | Real-time system (bonus) |

**Total: 100 points (+5 bonus)**

## Tips

1. **Start with tests:** Write test cases first to clarify requirements
2. **Build incrementally:** Test each component before combining
3. **Use @coroutine decorator:** Eliminates manual priming
4. **Close pipelines:** Always close coroutines when done
5. **Profile code:** Use `cProfile` to find bottlenecks
6. **Read the lecture:** All concepts are covered in lecture notes

Good luck! 🚀

