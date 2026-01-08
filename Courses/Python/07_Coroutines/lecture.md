# Coroutines and Data Processing Pipelines in Python

## Introduction

In previous lectures, we learned how to work with generators that **produce** data. But Python generators have a superpower — they can also **consume** data! This transforms them into **coroutines** — powerful tools for building data processing pipelines.

**What we'll learn:**
- How generators can receive data via `send()`
- Building coroutine-based data pipelines
- Push vs Pull data processing models
- Real-world examples: log processing, ETL, streaming data

## From Generators to Coroutines

### Regular Generator (Producer)

A generator produces values using `yield`:

```python
def count(n):
    """Generator that produces numbers"""
    for i in range(n):
        yield i  # Produce value

# Usage
for x in count(5):
    print(x)  # 0, 1, 2, 3, 4
```

### Coroutine (Consumer)

A coroutine **consumes** values via `yield`:

```python
def printer():
    """Coroutine that consumes values"""
    print("Coroutine started")
    while True:
        value = yield  # Wait for and receive value
        print(f"Received: {value}")

# Usage
p = printer()
next(p)  # Prime the coroutine (mandatory!)
p.send(10)   # Output: Received: 10
p.send(20)   # Output: Received: 20
p.send("Hi") # Output: Received: Hi
```

**Key difference:**
- **Generator:** `for item in generator()` — we **pull** data
- **Coroutine:** `coroutine.send(item)` — we **push** data

## The send() Pattern

The `send()` method is the heart of coroutines:

```python
def echo():
    """Simple echo coroutine"""
    print("Echo coroutine ready")
    
    while True:
        received = yield  # Pause here and wait for data
        print(f"Echo: {received}")

# Create coroutine
coro = echo()

# IMPORTANT: Prime the coroutine!
# This advances it to the first yield
next(coro)  # Output: Echo coroutine ready

# Now we can send data
coro.send("Hello")   # Output: Echo: Hello
coro.send(42)        # Output: Echo: 42
coro.send([1, 2])    # Output: Echo: [1, 2]
```

### Why Priming is Required

```python
def demo():
    print("Starting...")
    while True:
        value = yield
        print(f"Got: {value}")

coro = demo()

# Without priming — ERROR!
# coro.send(10)  # TypeError: can't send non-None value to a just-started generator

# Must prime first:
next(coro)  # or coro.send(None)
# Output: Starting...

# Now it works:
coro.send(10)  # Output: Got: 10
```

**What happens:**
1. `next(coro)` executes the function until the first `yield`
2. Coroutine pauses at `yield`, ready to receive data
3. `send(value)` provides the value and continues execution

## Bidirectional Communication

Coroutines can both **receive** and **produce** values:

```python
def accumulator():
    """Accumulate values and return running total"""
    total = 0
    
    while True:
        value = yield total  # Return total, receive new value
        if value is not None:
            total += value

# Usage
acc = accumulator()
print(next(acc))        # 0 (prime and get initial value)

print(acc.send(10))     # 10 (send 10, get total)
print(acc.send(5))      # 15 (send 5, get total)
print(acc.send(3))      # 18 (send 3, get total)
print(acc.send(-8))     # 10 (send -8, get total)
```

### Practical Example: Moving Average

```python
def moving_average(window_size):
    """Calculate moving average over a window"""
    values = []
    
    while True:
        value = yield sum(values) / len(values) if values else 0
        
        values.append(value)
        if len(values) > window_size:
            values.pop(0)  # Remove oldest

# Usage
avg = moving_average(3)
next(avg)  # Prime

print(avg.send(10))  # 10.0 (avg of [10])
print(avg.send(20))  # 15.0 (avg of [10, 20])
print(avg.send(30))  # 20.0 (avg of [10, 20, 30])
print(avg.send(40))  # 30.0 (avg of [20, 30, 40])
print(avg.send(50))  # 40.0 (avg of [30, 40, 50])
```

## Coroutine Pipeline Pattern

The most powerful use of coroutines is building **data processing pipelines**.

### Pipeline Architecture

```
source → filter → mapper → statistics → sink
```

**Components:**
- **Source:** Produces data and sends to pipeline
- **Filter:** Passes only items matching criteria
- **Mapper:** Transforms each item
- **Statistics:** Collects metrics (optional)
- **Sink:** Final consumer (print, save, etc.)

### Basic Pipeline Components

#### 1. Auto-Priming Decorator

```python
def coroutine(func):
    """Decorator to automatically prime coroutines"""
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # Prime it automatically
        return gen
    return wrapper

# Now we don't need to call next() manually!
```

#### 2. Filter

```python
@coroutine
def filter_items(predicate, target):
    """Pass only items matching predicate"""
    while True:
        item = yield
        if predicate(item):
            target.send(item)

# Example predicates
is_even = lambda x: x % 2 == 0
is_positive = lambda x: x > 0
longer_than_5 = lambda s: len(s) > 5
```

#### 3. Mapper (Transformer)

```python
@coroutine
def map_items(transform, target):
    """Transform each item and send to target"""
    while True:
        item = yield
        result = transform(item)
        target.send(result)

# Example transforms
square = lambda x: x * x
uppercase = lambda s: s.upper()
to_dict = lambda x: {'value': x, 'squared': x*x}
```

#### 4. Sink (Terminal)

```python
@coroutine
def printer(prefix=""):
    """Print received items"""
    while True:
        item = yield
        print(f"{prefix}{item}")

@coroutine
def collector():
    """Collect items into a list"""
    items = []
    try:
        while True:
            item = yield
            items.append(item)
    except GeneratorExit:
        print(f"Collected {len(items)} items")

@coroutine
def file_writer(filename):
    """Write items to file"""
    with open(filename, 'w') as f:
        try:
            while True:
                item = yield
                f.write(str(item) + '\n')
                f.flush()
        except GeneratorExit:
            pass
```

### Simple Pipeline Example

```python
# Build pipeline: numbers → filter even → square → print
sink = printer("Result: ")
mapper = map_items(lambda x: x * x, sink)
pipeline = filter_items(lambda x: x % 2 == 0, mapper)

# Send data through pipeline
for num in range(10):
    pipeline.send(num)

# Output:
# Result: 0
# Result: 4
# Result: 16
# Result: 36
# Result: 64
```

**Important:** Build pipeline from end (sink) to start (source)!

## Real-World Example: Log Processing

Let's build a complete system for processing log files:

```python
#!/usr/bin/env python3
"""Coroutine-based log processing pipeline"""
import sys
import re
import json
from datetime import datetime

# ============ DECORATOR ============

def coroutine(func):
    """Auto-prime coroutines"""
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

# ============ FILTERS ============

@coroutine
def filter_by_level(level, target):
    """Filter log entries by level (ERROR, WARN, INFO, etc.)"""
    while True:
        entry = yield
        if entry.get('level') == level:
            target.send(entry)

@coroutine
def filter_by_pattern(pattern, field, target):
    """Filter entries where field matches regex"""
    regex = re.compile(pattern)
    while True:
        entry = yield
        if field in entry and regex.search(entry[field]):
            target.send(entry)

@coroutine
def filter_time_range(start_hour, end_hour, target):
    """Filter by time range (hour of day)"""
    while True:
        entry = yield
        if 'timestamp' in entry:
            # Extract hour from timestamp
            time_str = entry['timestamp']
            hour = int(time_str.split()[1].split(':')[0])
            if start_hour <= hour < end_hour:
                target.send(entry)

# ============ TRANSFORMERS ============

@coroutine
def map_fields(field_map, target):
    """Rename/select fields"""
    while True:
        entry = yield
        new_entry = {}
        for new_key, old_key in field_map.items():
            if old_key in entry:
                new_entry[new_key] = entry[old_key]
        target.send(new_entry)

@coroutine
def map_transform(field, transform_func, target):
    """Apply transformation to specific field"""
    while True:
        entry = yield
        if field in entry:
            entry[field] = transform_func(entry[field])
        target.send(entry)

@coroutine
def add_field(field_name, value_func, target):
    """Add computed field to each entry"""
    while True:
        entry = yield
        entry[field_name] = value_func(entry)
        target.send(entry)

# ============ STATISTICS ============

@coroutine
def statistics(target=None):
    """Collect statistics and optionally pass data through"""
    stats = {
        'count': 0,
        'by_level': {},
        'by_module': {},
        'by_hour': {}
    }
    
    try:
        while True:
            entry = yield stats  # Return current stats
            stats['count'] += 1
            
            # Count by level
            level = entry.get('level', 'UNKNOWN')
            stats['by_level'][level] = stats['by_level'].get(level, 0) + 1
            
            # Count by module
            module = entry.get('module', 'UNKNOWN')
            stats['by_module'][module] = stats['by_module'].get(module, 0) + 1
            
            # Count by hour
            if 'timestamp' in entry:
                hour = entry['timestamp'][:13]  # YYYY-MM-DD HH
                stats['by_hour'][hour] = stats['by_hour'].get(hour, 0) + 1
            
            # Pass through if target specified
            if target:
                target.send(entry)
                
    except GeneratorExit:
        return stats

# ============ SINKS ============

@coroutine
def printer(prefix="", template=None):
    """Print items with optional template"""
    while True:
        item = yield
        if template:
            print(prefix + template.format(**item))
        else:
            print(prefix + str(item))

@coroutine
def json_writer(file_obj=None):
    """Write items as JSON lines"""
    if file_obj is None:
        file_obj = sys.stdout
    
    while True:
        item = yield
        file_obj.write(json.dumps(item, ensure_ascii=False) + '\n')
        file_obj.flush()

@coroutine
def csv_writer(file_obj, fieldnames):
    """Write items as CSV"""
    import csv
    writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
    writer.writeheader()
    
    try:
        while True:
            item = yield
            writer.writerow(item)
            file_obj.flush()
    except GeneratorExit:
        pass

@coroutine
def file_writer(filename, mode='w'):
    """Write items to file"""
    with open(filename, mode) as f:
        try:
            while True:
                item = yield
                f.write(str(item) + '\n')
                f.flush()
        except GeneratorExit:
            pass

# ============ UTILITIES ============

@coroutine
def tee(*targets):
    """Broadcast items to multiple targets"""
    while True:
        item = yield
        for target in targets:
            target.send(item)

@coroutine
def drop():
    """Discard all items (for testing)"""
    while True:
        item = yield

# ============ SOURCE ============

def parse_log_line(line):
    """Parse log line into structured entry
    
    Format: 2025-12-03 10:30:45 ERROR [module] Message here
    """
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) \[([^\]]+)\] (.+)'
    match = re.match(pattern, line)
    
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'module': match.group(3),
            'message': match.group(4)
        }
    return None

def source(file_obj, target):
    """Read log lines and push to pipeline"""
    for line in file_obj:
        entry = parse_log_line(line.rstrip())
        if entry:
            target.send(entry)

# ============ EXAMPLES ============

def example_1_simple():
    """Simple pipeline: filter ERROR logs"""
    print("=== Example 1: Filter ERROR logs ===\n")
    
    # Build pipeline: source → filter → print
    sink = printer(prefix="ERROR: ")
    pipeline = filter_by_level('ERROR', sink)
    
    # Sample data
    sample_logs = [
        "2025-12-03 10:30:45 INFO [auth] User logged in",
        "2025-12-03 10:30:46 ERROR [db] Connection failed",
        "2025-12-03 10:30:47 INFO [api] Request processed",
        "2025-12-03 10:30:48 ERROR [api] Timeout occurred",
        "2025-12-03 10:30:49 WARN [cache] Cache miss",
    ]
    
    # Process
    import io
    source(io.StringIO('\n'.join(sample_logs)), pipeline)
    print()

def example_2_transform():
    """Pipeline with transformation"""
    print("=== Example 2: Transform messages to uppercase ===\n")
    
    # Build pipeline: filter → transform → print
    sink = printer()
    transformer = map_transform('message', str.upper, sink)
    pipeline = filter_by_level('ERROR', transformer)
    
    sample_logs = [
        "2025-12-03 10:30:45 INFO [auth] User logged in",
        "2025-12-03 10:30:46 ERROR [db] Connection failed",
        "2025-12-03 10:30:47 ERROR [api] Invalid request",
    ]
    
    import io
    source(io.StringIO('\n'.join(sample_logs)), pipeline)
    print()

def example_3_statistics():
    """Pipeline with statistics collection"""
    print("=== Example 3: Collect statistics ===\n")
    
    # Build pipeline with stats
    sink = printer(prefix="LOG: ")
    stats_collector = statistics(sink)
    
    sample_logs = [
        "2025-12-03 10:30:45 INFO [auth] User logged in",
        "2025-12-03 10:30:46 ERROR [db] Connection failed",
        "2025-12-03 10:31:47 INFO [api] Request processed",
        "2025-12-03 10:31:48 ERROR [api] Timeout occurred",
        "2025-12-03 11:30:49 WARN [cache] Cache miss",
        "2025-12-03 11:30:50 ERROR [db] Query failed",
    ]
    
    import io
    source(io.StringIO('\n'.join(sample_logs)), stats_collector)
    
    # Get final statistics
    final_stats = stats_collector.send(None)
    print("\n=== STATISTICS ===")
    print(f"Total entries: {final_stats['count']}")
    print(f"By level: {final_stats['by_level']}")
    print(f"By module: {final_stats['by_module']}")
    print(f"By hour: {final_stats['by_hour']}")
    print()

def example_4_branching():
    """Pipeline with branching (tee)"""
    print("=== Example 4: Branching - errors to file, all to stdout ===\n")
    
    import tempfile
    import os
    
    # Create temp file
    fd, error_file = tempfile.mkstemp(suffix='.log', text=True)
    os.close(fd)
    
    # Branch 1: errors to file
    error_sink = file_writer(error_file)
    error_filter = filter_by_level('ERROR', error_sink)
    
    # Branch 2: all to stdout
    all_sink = printer(prefix="ALL: ")
    
    # Broadcast to both branches
    broadcast = tee(error_filter, all_sink)
    
    sample_logs = [
        "2025-12-03 10:30:45 INFO [auth] User logged in",
        "2025-12-03 10:30:46 ERROR [db] Connection failed",
        "2025-12-03 10:30:47 INFO [api] Request processed",
        "2025-12-03 10:30:48 ERROR [api] Timeout occurred",
    ]
    
    import io
    source(io.StringIO('\n'.join(sample_logs)), broadcast)
    
    # Close error sink
    error_filter.close()
    
    # Show file contents
    print(f"\nErrors written to {error_file}:")
    with open(error_file) as f:
        print(f.read())
    
    # Cleanup
    os.unlink(error_file)

def example_5_complex():
    """Complex multi-stage pipeline"""
    print("=== Example 5: Complex pipeline ===")
    print("Filter ERROR → Add severity → Select fields → JSON output\n")
    
    # Build complex pipeline
    sink = json_writer()
    
    # Select only important fields
    field_selector = map_fields({
        'time': 'timestamp',
        'level': 'level',
        'msg': 'message',
        'severity': 'severity'
    }, sink)
    
    # Add severity score
    def calculate_severity(entry):
        levels = {'INFO': 1, 'WARN': 2, 'ERROR': 3}
        return levels.get(entry['level'], 0)
    
    severity_adder = add_field('severity', calculate_severity, field_selector)
    
    # Filter only errors
    error_filter = filter_by_level('ERROR', severity_adder)
    
    sample_logs = [
        "2025-12-03 10:30:45 INFO [auth] User logged in",
        "2025-12-03 10:30:46 ERROR [db] Connection failed",
        "2025-12-03 10:30:47 ERROR [api] Invalid request",
    ]
    
    import io
    source(io.StringIO('\n'.join(sample_logs)), error_filter)
    print()

# ============ PRODUCTION PIPELINE BUILDER ============

def build_production_pipeline(
    output_format='json',
    error_file=None,
    stats_enabled=True,
    filters=None
):
    """
    Build production-ready log processing pipeline
    
    Args:
        output_format: 'json', 'csv', or 'text'
        error_file: File to write ERROR logs
        stats_enabled: Collect statistics
        filters: List of (filter_func, *args) tuples
    
    Returns:
        (pipeline_entry, stats_coroutine)
    """
    # Create main output sink
    if output_format == 'json':
        main_sink = json_writer()
    elif output_format == 'csv':
        fieldnames = ['timestamp', 'level', 'module', 'message']
        main_sink = csv_writer(sys.stdout, fieldnames)
    else:
        template = "{timestamp} {level:5s} [{module}] {message}"
        main_sink = printer(template=template)
    
    # Add error file sink if needed
    if error_file:
        error_sink = file_writer(error_file)
        error_filter = filter_by_level('ERROR', error_sink)
        # Broadcast to both sinks
        sink = tee(main_sink, error_filter)
    else:
        sink = main_sink
    
    # Add statistics
    stats_coro = None
    if stats_enabled:
        stats_coro = statistics(sink)
        sink = stats_coro
    
    # Apply custom filters
    if filters:
        for filter_config in reversed(filters):
            filter_func, *args = filter_config
            sink = filter_func(*args, sink)
    
    return sink, stats_coro

# ============ MAIN ============

def main():
    """Run all examples"""
    example_1_simple()
    example_2_transform()
    example_3_statistics()
    example_4_branching()
    example_5_complex()

if __name__ == "__main__":
    main()
```

### Running the Examples

```bash
# Run all examples
python coroutine_pipeline.py

# Use as a script
cat application.log | python coroutine_pipeline.py
```

## Push vs Pull: Comparison

### Pull Model (Iterators)

```python
# Iterator-based (pull)
def pull_pipeline(data):
    # Consumer pulls data from producer
    filtered = filter(lambda x: x > 0, data)
    mapped = map(lambda x: x * 2, filtered)
    return list(mapped)

numbers = range(-5, 6)
result = pull_pipeline(numbers)
print(result)  # [2, 4, 6, 8, 10]
```

**Characteristics:**
- Consumer **requests** data
- Lazy evaluation
- Creates chain of iterators
- Good for finite sequences

### Push Model (Coroutines)

```python
# Coroutine-based (push)
@coroutine
def collector():
    items = []
    try:
        while True:
            item = yield
            items.append(item)
    except GeneratorExit:
        return items

@coroutine
def push_pipeline():
    sink = collector()
    mapper = map_items(lambda x: x * 2, sink)
    filterer = filter_items(lambda x: x > 0, mapper)
    return filterer, sink

pipeline, sink = push_pipeline()

# Producer pushes data
for num in range(-5, 6):
    pipeline.send(num)

pipeline.close()
```

**Characteristics:**
- Producer **sends** data
- Immediate processing
- Good for streaming/infinite data
- Natural for event-driven systems

## Advanced Patterns

### 1. Stateful Processing

```python
@coroutine
def running_average(window_size, target):
    """Calculate running average over window"""
    values = []
    
    while True:
        value = yield
        values.append(value)
        
        # Keep only last N values
        if len(values) > window_size:
            values.pop(0)
        
        avg = sum(values) / len(values)
        target.send({'value': value, 'avg': avg})

# Usage
sink = printer()
averager = running_average(3, sink)

for x in [10, 20, 30, 40, 50]:
    averager.send(x)

# Output:
# {'value': 10, 'avg': 10.0}
# {'value': 20, 'avg': 15.0}
# {'value': 30, 'avg': 20.0}
# {'value': 40, 'avg': 30.0}
# {'value': 50, 'avg': 40.0}
```

### 2. Conditional Routing

```python
@coroutine
def router(routes):
    """Route items to different targets based on conditions
    
    Args:
        routes: List of (predicate, target) tuples
    """
    while True:
        item = yield
        for predicate, target in routes:
            if predicate(item):
                target.send(item)
                break  # Send to first matching route only

# Usage
errors = printer("ERROR: ")
warnings = printer("WARN: ")
info = printer("INFO: ")

routes = [
    (lambda x: x['level'] == 'ERROR', errors),
    (lambda x: x['level'] == 'WARN', warnings),
    (lambda x: True, info),  # Default route
]

pipeline = router(routes)
```

### 3. Aggregation

```python
@coroutine
def batch(size, target):
    """Collect items into batches of given size"""
    batch = []
    
    try:
        while True:
            item = yield
            batch.append(item)
            
            if len(batch) >= size:
                target.send(batch)
                batch = []
                
    except GeneratorExit:
        # Send remaining items
        if batch:
            target.send(batch)

# Usage
sink = printer("BATCH: ")
batcher = batch(3, sink)

for i in range(10):
    batcher.send(i)

batcher.close()

# Output:
# BATCH: [0, 1, 2]
# BATCH: [3, 4, 5]
# BATCH: [6, 7, 8]
# BATCH: [9]
```

### 4. Windowing

```python
@coroutine
def sliding_window(size, target):
    """Emit sliding window of items"""
    window = []
    
    while True:
        item = yield
        window.append(item)
        
        if len(window) > size:
            window.pop(0)
        
        if len(window) == size:
            target.send(list(window))

# Usage
sink = printer("WINDOW: ")
windower = sliding_window(3, sink)

for i in range(6):
    windower.send(i)

# Output:
# WINDOW: [0, 1, 2]
# WINDOW: [1, 2, 3]
# WINDOW: [2, 3, 4]
# WINDOW: [3, 4, 5]
```

## Error Handling

### Propagating Errors

```python
@coroutine
def error_handler(target, error_sink=None):
    """Catch errors and optionally send to error sink"""
    while True:
        try:
            item = yield
            target.send(item)
        except Exception as e:
            error_msg = {
                'error': str(e),
                'item': item,
                'type': type(e).__name__
            }
            if error_sink:
                error_sink.send(error_msg)
            else:
                print(f"Error processing {item}: {e}", file=sys.stderr)
```

### Closing Pipelines

```python
@coroutine
def safe_component(target):
    """Component with proper cleanup"""
    # Setup
    resource = setup_resource()
    
    try:
        while True:
            item = yield
            # Process
            result = process(item, resource)
            target.send(result)
    except GeneratorExit:
        # Cleanup
        cleanup_resource(resource)
        target.close()
```

### Pipeline Context Manager

```python
class Pipeline:
    """Context manager for coroutine pipelines"""
    
    def __init__(self, *stages):
        self.stages = stages
        self.entry = stages[0]
    
    def send(self, item):
        """Send item to pipeline"""
        self.entry.send(item)
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        """Close all stages"""
        for stage in self.stages:
            try:
                stage.close()
            except:
                pass

# Usage
with Pipeline(stage1, stage2, stage3) as pipeline:
    for item in data:
        pipeline.send(item)
# All stages automatically closed
```

## Real-World Use Cases

### 1. Real-Time Log Monitoring

```python
def monitor_logs(log_file, alert_sink):
    """Monitor log file for errors in real-time"""
    
    # Build alert pipeline
    alerter = filter_by_level('ERROR', alert_sink)
    deduplicator = deduplicate('message', alerter)
    rate_limiter = throttle(max_per_minute=10, target=deduplicator)
    
    # Watch file
    import time
    with open(log_file) as f:
        # Seek to end
        f.seek(0, 2)
        
        while True:
            line = f.readline()
            if line:
                entry = parse_log_line(line)
                if entry:
                    rate_limiter.send(entry)
            else:
                time.sleep(0.1)  # Wait for new data
```

### 2. ETL Pipeline

```python
def etl_pipeline(source_db, target_db):
    """Extract-Transform-Load pipeline"""
    
    # Load stage
    loader = database_writer(target_db)
    
    # Transform stage
    validator = validate_schema(schema, loader)
    enricher = enrich_data(external_api, validator)
    cleaner = clean_data(enricher)
    
    # Extract stage
    for row in source_db.query("SELECT * FROM users"):
        cleaner.send(row)
```

### 3. Streaming Data Processing

```python
def process_sensor_data(sensor_stream):
    """Process real-time sensor data"""
    
    # Build pipeline
    sink = database_writer(db)
    alerter = alert_on_threshold(max_value=100, alert_system)
    smoother = moving_average(window=5, alerter)
    validator = validate_range(min=0, max=200, smoother)
    
    broadcast = tee(validator, sink)
    
    # Process stream
    for reading in sensor_stream:
        broadcast.send(reading)
```

## Performance Considerations

### Memory Efficiency

Coroutines process items one at a time:

```python
# Iterator (materializes intermediate lists)
filtered = [x for x in data if x > 0]  # Allocates list
mapped = [x * 2 for x in filtered]     # Allocates another list

# Coroutine (no intermediate storage)
pipeline = filter_items(lambda x: x > 0, 
              map_items(lambda x: x * 2, sink))
# Processes items immediately, no lists created
```

### CPU Efficiency

Both approaches have similar performance for simple operations:

```python
import time

def benchmark_pull(data):
    start = time.time()
    result = list(map(lambda x: x * 2, filter(lambda x: x > 0, data)))
    return time.time() - start

def benchmark_push(data):
    @coroutine
    def counter():
        count = 0
        while True:
            item = yield
            count += 1
    
    sink = counter()
    mapper = map_items(lambda x: x * 2, sink)
    filterer = filter_items(lambda x: x > 0, mapper)
    
    start = time.time()
    for item in data:
        filterer.send(item)
    return time.time() - start

# Similar performance for most cases
```

**When to use coroutines:**
- Streaming/infinite data
- Multiple consumers (broadcasting)
- Stateful processing
- Event-driven systems

**When to use iterators:**
- Finite sequences
- Need to iterate multiple times
- Simpler logic

## Best Practices

### 1. Always Use @coroutine Decorator

```python
@coroutine
def my_stage(target):
    """Use decorator to avoid manual priming"""
    while True:
        item = yield
        # Process
        target.send(item)
```

### 2. Build Pipelines Backward

```python
# Good: Build from sink to source
sink = printer()
stage3 = transform(sink)
stage2 = filter(stage3)
stage1 = validate(stage2)

# Use stage1 as entry point
```

### 3. Handle Cleanup

```python
@coroutine
def proper_cleanup(target):
    try:
        while True:
            item = yield
            target.send(item)
    except GeneratorExit:
        # Close downstream
        target.close()
```

### 4. Document Data Flow

```python
def build_pipeline():
    """
    Build processing pipeline:
    
    source → validator → filter → transformer → stats → sink
            ↓ (invalid)
            error_log
    """
    # Implementation
```

### 5. Keep Stages Simple

Each stage should do **one thing**:

```python
# Good: Separate stages
validator = validate(cleaner)
cleaner = clean_data(transformer)
transformer = transform_fields(sink)

# Bad: Everything in one stage
def do_everything(target):
    # Too complex, hard to reuse
    pass
```

## Comparison: Iterators vs Coroutines

| Feature | Iterators (Pull) | Coroutines (Push) |
|---------|------------------|-------------------|
| Data flow | Consumer pulls | Producer pushes |
| Use case | Finite sequences | Streaming data |
| State | Difficult | Natural |
| Broadcasting | Difficult | Easy (tee) |
| Backpressure | Natural | Manual |
| Error handling | Exceptions propagate up | Must handle explicitly |
| Composability | Excellent | Excellent |
| Memory | Lazy | Lazy |

## Summary

**Key concepts:**
- `yield` can both produce and consume values
- `send()` pushes data into coroutines
- Must prime coroutines with `next()` before `send()`
- Build pipelines from sink to source
- Use `@coroutine` decorator for auto-priming

**Pipeline patterns:**
- Filter: conditional pass-through
- Map: transform items
- Tee: broadcast to multiple consumers
- Statistics: collect metrics
- Batch/Window: aggregate items

**When to use coroutines:**
- Real-time data processing
- Event-driven systems  
- Stateful transformations
- Multi-consumer scenarios

**Remember:** Coroutines provide an elegant push-based model for streaming data processing, complementing Python's pull-based iterators. Choose the right tool for your use case!

