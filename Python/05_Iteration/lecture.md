# Iteration Protocol
## Iterators, Generators, Itertools

---

## 1. What is the Iteration Protocol?

The iteration protocol defines how objects can be iterated over.

Two components:
1. **Iterable**: Has `__iter__()` method that returns an iterator
2. **Iterator**: Has `__next__()` method and `__iter__()` (returns self)

```python
# Built-in iterables
for item in [1, 2, 3]:      # list is iterable
    print(item)

for char in "hello":        # string is iterable
    print(char)

for key in {"a": 1}:        # dict is iterable
    print(key)
```

---

## 2. Understanding Iterators

Iterators are objects that produce values one at a time.

```python
numbers = [1, 2, 3, 4, 5]

# Get iterator from iterable
iterator = iter(numbers)

# Get values using next()
print(next(iterator))    # 1
print(next(iterator))    # 2
print(next(iterator))    # 3

# StopIteration raised when exhausted
# next(iterator) ... eventually raises StopIteration
```

### Using next() with Default Value

```python
iterator = iter([1, 2, 3])
print(next(iterator))           # 1
print(next(iterator))           # 2
print(next(iterator))           # 3
print(next(iterator, 'END'))    # 'END' instead of StopIteration

# Useful for safe iteration
def safe_next(iterable, default=None):
    return next(iter(iterable), default)
```

### iter() with Sentinel Value

The `iter()` function has a two-argument form: `iter(callable, sentinel)`

It calls the callable repeatedly until it returns the sentinel value.

```python
# Reading file until empty line
with open('data.txt') as f:
    for line in iter(f.readline, '\n'):
        print(line.rstrip())

# Reading input until 'quit'
for line in iter(input, 'quit'):
    print(f"You entered: {line}")

# Random numbers until we get 5
import random
for num in iter(lambda: random.randint(1, 6), 5):
    print(num)
print("Got 5!")
```

---

## 2.1 How for Loop Works Internally

The `for` loop is syntactic sugar for iterator protocol.

```python
# This for loop:
for item in iterable:
    print(item)

# Is equivalent to:
iterator = iter(iterable)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```

### Example: Reimplementing for

```python
def my_for(iterable, func):
    """Custom for loop implementation"""
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            func(item)
        except StopIteration:
            break

# Usage
my_for([1, 2, 3, 4], lambda x: print(x * 2))
# 2
# 4
# 6
# 8
```

---

## 2.2 Practical Examples with next() and enumerate()

### Finding Index of Element

Implement `index()` using `next()` and `enumerate()`:

```python
def index(iterable, element):
    """Return index of first occurrence or raise ValueError"""
    for i, value in enumerate(iterable):
        if value == element:
            return i
    raise ValueError(f"{element} not in iterable")

# Examples
print(index([10, 20, 30, 40], 30))    # 2
print(index("hello", "l"))             # 2
print(index(range(100), 50))           # 50
# index([1, 2, 3], 5)                  # ValueError
```

### Finding First Match

```python
def first(iterable, condition, default=None):
    """Return first item matching condition"""
    return next((x for x in iterable if condition(x)), default)

# Examples
numbers = [1, 3, 5, 8, 9, 10]
print(first(numbers, lambda x: x % 2 == 0))     # 8
print(first(numbers, lambda x: x > 100, -1))    # -1

words = ["apple", "banana", "cherry", "date"]
print(first(words, lambda w: len(w) > 5))       # "banana"
```

---

## 3. Creating Custom Iterators

### Basic Iterator Class

```python
class CountUp:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max_count:
            raise StopIteration
        self.current += 1
        return self.current

counter = CountUp(5)
for num in counter:
    print(num)    # 1, 2, 3, 4, 5
```

### Separate Iterator and Iterable

```python
class CountUpIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max_count:
            raise StopIteration
        self.current += 1
        return self.current

class CountUp:
    def __init__(self, max_count):
        self.max_count = max_count
    
    def __iter__(self):
        return CountUpIterator(self.max_count)

# Can iterate multiple times
counter = CountUp(3)
print(list(counter))    # [1, 2, 3]
print(list(counter))    # [1, 2, 3]
```

### Advanced: Iterable Integer Class

Create a class that behaves like an integer but is also iterable.

```python
class iter_int(int):
    """Integer that can be iterated over"""
    
    def __iter__(self):
        """Iterate from 0 to self (exclusive)"""
        return iter(range(self))
    
    # All arithmetic operations inherited from int work!

# Usage
n = iter_int(5)

# Works as integer
print(n + 2)           # 7
print(n * 3)           # 15
print(n ** 2)          # 25

# Works as iterable
print(list(n))         # [0, 1, 2, 3, 4]
for i in n:
    print(i)           # 0, 1, 2, 3, 4

# Combines both!
print(list(iter_int(4) + 2))    # [0, 1, 2, 3, 4, 5]
print(iter_int(3) * 2)          # 6

# Practical usage
for i in iter_int(5):
    print(f"Iteration {i}")

# Works with comprehensions
squares = [x**2 for x in iter_int(10)]
print(squares)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Iterator with State

```python
class FibonacciIterator:
    """Iterator that generates Fibonacci numbers"""
    
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

fib = FibonacciIterator(10)
print(list(fib))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## 4. Generators: Simple Iterators

Generators are functions that use `yield` to produce values lazily.

```python
def count_up(max_count):
    current = 1
    while current <= max_count:
        yield current
        current += 1

for num in count_up(5):
    print(num)    # 1, 2, 3, 4, 5
```

### Generator vs Regular Function

```python
# Regular function - returns all at once
def get_numbers():
    return [1, 2, 3, 4, 5]

# Generator - returns one at a time
def generate_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print(get_numbers())        # [1, 2, 3, 4, 5]
print(generate_numbers())   # <generator object>
print(list(generate_numbers()))  # [1, 2, 3, 4, 5]
```

---

## 5. Generator Expressions

Lightweight generators using comprehension syntax.

```python
# List comprehension - creates entire list
squares_list = [x**2 for x in range(10)]

# Generator expression - lazy evaluation
squares_gen = (x**2 for x in range(10))

print(squares_list)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares_gen)     # <generator object>

# Use in sum, max, etc.
print(sum(x**2 for x in range(10)))    # 285
```

### Memory Efficiency

```python
import sys

# List comprehension - all in memory
big_list = [x for x in range(1000000)]
print(sys.getsizeof(big_list))    # ~8MB

# Generator - minimal memory
big_gen = (x for x in range(1000000))
print(sys.getsizeof(big_gen))     # ~200 bytes
```

---

## 5.1 Lazy Evaluation Gotchas

Understanding when and how expressions are evaluated.

### List Comprehension vs Generator - Closure Capture

**Surprising behavior with lambda and list comprehension:**

```python
# List comprehension - lambdas created immediately
funcs_list = [lambda x: x**y for y in range(5)]

# What do you expect?
for f in funcs_list:
    print(f(2))

# Output: 16, 16, 16, 16, 16  (all use y=4!)
# Why? All lambdas share the same 'y' variable from the enclosing scope
# After the list comprehension, y=4, so all lambdas use that value
```

```python
# Generator expression - lambdas created lazily
funcs_gen = (lambda x: x**y for y in range(5))

# What do you expect?
for f in funcs_gen:
    print(f(2))

# Output: 16, 16, 16, 16, 16  (same problem!)
# Actually, even worse! The generator yields lambdas one by one,
# but they all still capture 'y' by reference, not by value
```

**Solution: Capture by value using default argument:**

```python
# Fix: capture y by value
funcs_fixed = [lambda x, y=y: x**y for y in range(5)]

for f in funcs_fixed:
    print(f(2))

# Output: 1, 2, 4, 8, 16  (correct!)
```

**Full comparison:**

```python
# List comprehension with closure
print("List comprehension (closure):")
funcs_list = [lambda x: x**y for y in range(5)]
for i, f in enumerate(funcs_list):
    print(f"  2**{i} = {f(2)}")
# All print: 2**0 = 16, 2**1 = 16, ...

# Generator expression with closure  
print("\nGenerator expression (closure):")
funcs_gen = (lambda x: x**y for y in range(5))
for i, f in enumerate(funcs_gen):
    print(f"  2**{i} = {f(2)}")
# All print: 2**0 = 16, 2**1 = 16, ...

# Fixed with default argument
print("\nFixed (default argument):")
funcs_fixed = [lambda x, y=y: x**y for y in range(5)]
for i, f in enumerate(funcs_fixed):
    print(f"  2**{i} = {f(2)}")
# Correctly prints: 2**0 = 1, 2**1 = 2, 2**2 = 4, ...
```

### Iterator Consumption Gotcha

**Iterators can only be used once!**

```python
numbers = list(range(7))

# Using slicing - creates new lists
first_three = numbers[:3]      # [0, 1, 2]
remaining = numbers[3:]        # [3, 4, 5, 6]

print(list(zip(first_three, remaining)))
# [(0, 3), (1, 4), (2, 5)]

print(list(zip(first_three, remaining)))
# [(0, 3), (1, 4), (2, 5)]  - works again!
```

```python
# Using iterator - consumed after first use!
numbers = list(range(7))
numbers_iter = iter(numbers)

first_three = numbers[:3]      # Still a list
remaining = numbers[3:]        # Still a list

# First zip consumes the iterator
print(list(zip(numbers_iter, first_three)))
# [(0, 0), (1, 1), (2, 2)]  - consumed 3 items from iterator

# Second zip starts where first left off!
print(list(zip(numbers_iter, remaining)))
# [(3, 3), (4, 4), (5, 5), (6, 6)]  - remaining items!
```

**Deeper example:**

```python
numbers = list(range(10))
it = iter(numbers)

# Consume first 3 items
print(list(zip(it, range(3))))
# [(0, 0), (1, 1), (2, 2)]

# Consume next 3 items
print(list(zip(it, range(3))))
# [(3, 0), (4, 1), (5, 2)]

# Iterator continues from where it left off
print(next(it))  # 6
print(next(it))  # 7
```

### Multiple Iterators from Same Iterable

```python
numbers = [1, 2, 3, 4, 5]

# Each iter() call creates NEW iterator
it1 = iter(numbers)
it2 = iter(numbers)

print(next(it1))  # 1
print(next(it2))  # 1  (independent!)
print(next(it1))  # 2
print(next(it1))  # 3
print(next(it2))  # 2  (continues from its position)
```

---

## 6. Generator Methods

### send()

Send values to a generator.

```python
def echo():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo()
next(gen)           # Prime the generator
gen.send("Hello")   # Received: Hello
gen.send("World")   # Received: World
```

### throw()

Throw an exception into a generator.

```python
def generator():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        yield "Error caught!"

gen = generator()
print(next(gen))         # 1
print(gen.throw(ValueError))  # Error caught!
```

### close()

Close a generator.

```python
def counter():
    try:
        count = 0
        while True:
            yield count
            count += 1
    finally:
        print("Generator closed")

gen = counter()
print(next(gen))    # 0
print(next(gen))    # 1
gen.close()         # Generator closed
```

---

## 7. Generator Delegation with yield from

Delegate to another generator or iterable.

```python
def generator1():
    yield 1
    yield 2

def generator2():
    yield 3
    yield 4

def combined():
    yield from generator1()
    yield from generator2()

print(list(combined()))    # [1, 2, 3, 4]
```

### Practical Example: Flatten Nested Lists

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested_list = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(list(flatten(nested_list)))    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 8. Infinite Generators

Generators that never end.

```python
def infinite_counter(start=0):
    count = start
    while True:
        yield count
        count += 1

counter = infinite_counter()
print(next(counter))    # 0
print(next(counter))    # 1
print(next(counter))    # 2

# Use with itertools.islice to limit
from itertools import islice
print(list(islice(infinite_counter(), 5)))    # [0, 1, 2, 3, 4]
```

### Fibonacci Generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## 9. itertools Module

Powerful tools for creating iterators.

### Infinite Iterators

```python
from itertools import count, cycle, repeat

# count - infinite counter
for i in count(10):
    if i > 15:
        break
    print(i)    # 10, 11, 12, 13, 14, 15

# cycle - repeat sequence infinitely
counter = 0
for item in cycle(['A', 'B', 'C']):
    if counter > 6:
        break
    print(item)
    counter += 1
# A, B, C, A, B, C, A

# repeat - repeat value
for item in repeat('Hello', 3):
    print(item)    # Hello, Hello, Hello
```

### Combinatoric Iterators

```python
from itertools import product, permutations, combinations

# product - cartesian product
print(list(product([1, 2], ['A', 'B'])))
# [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

# permutations - all orderings
print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations - unique selections
print(list(combinations([1, 2, 3, 4], 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

### Iterators for Filtering

```python
from itertools import filterfalse, takewhile, dropwhile, compress

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# filterfalse - opposite of filter
evens = list(filterfalse(lambda x: x % 2, numbers))
print(evens)    # [2, 4, 6, 8]

# takewhile - take while condition is true
print(list(takewhile(lambda x: x < 5, numbers)))
# [1, 2, 3, 4]

# dropwhile - drop while condition is true
print(list(dropwhile(lambda x: x < 5, numbers)))
# [5, 6, 7, 8]

# compress - filter by selector
selectors = [1, 0, 1, 0, 1, 0, 1, 0]
print(list(compress(numbers, selectors)))
# [1, 3, 5, 7]
```

### Iterators for Grouping

```python
from itertools import groupby, islice, chain

# groupby - group consecutive items
data = [1, 1, 2, 2, 2, 3, 3, 1, 1]
for key, group in groupby(data):
    print(key, list(group))
# 1 [1, 1]
# 2 [2, 2, 2]
# 3 [3, 3]
# 1 [1, 1]

# islice - slice an iterator
print(list(islice(range(100), 5, 10)))
# [5, 6, 7, 8, 9]

# chain - chain iterables
print(list(chain([1, 2], [3, 4], [5, 6])))
# [1, 2, 3, 4, 5, 6]
```

### Accumulating and Reducing

```python
from itertools import accumulate
import operator

numbers = [1, 2, 3, 4, 5]

# accumulate - running totals
print(list(accumulate(numbers)))
# [1, 3, 6, 10, 15]

# accumulate with operator
print(list(accumulate(numbers, operator.mul)))
# [1, 2, 6, 24, 120]
```

---

## 10. Pipelining Iterators

Chain multiple iterators for data processing.

```python
def read_data():
    """Simulate reading data"""
    yield from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even(numbers):
    """Filter even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square(numbers):
    """Square numbers"""
    for num in numbers:
        yield num ** 2

# Pipeline: read -> filter -> square
pipeline = square(filter_even(read_data()))
print(list(pipeline))    # [4, 16, 36, 64, 100]
```

---

## 11. Lazy Evaluation Benefits

Generators enable lazy evaluation for efficiency.

```python
# Eager evaluation - all computed immediately
def process_eager(data):
    filtered = [x for x in data if x % 2 == 0]
    squared = [x ** 2 for x in filtered]
    return sum(squared)

# Lazy evaluation - computed on demand
def process_lazy(data):
    filtered = (x for x in data if x % 2 == 0)
    squared = (x ** 2 for x in filtered)
    return sum(squared)

# Works with infinite or very large sequences
from itertools import count, islice

result = process_lazy(islice(count(), 1000000))
print(result)    # Very large number, but memory efficient
```

---

## 12. Custom Iterable Classes

Make your classes iterable.

```python
class Fibonacci:
    def __init__(self, max_count):
        self.max_count = max_count
    
    def __iter__(self):
        a, b = 0, 1
        count = 0
        while count < self.max_count:
            yield a
            a, b = b, a + b
            count += 1

fib = Fibonacci(10)
print(list(fib))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Can iterate multiple times
for num in fib:
    print(num)
```

---

## 13. Reverse Iteration

Implement `__reversed__()` for reverse iteration.

```python
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        for i in range(self.start, 0, -1):
            yield i
    
    def __reversed__(self):
        for i in range(1, self.start + 1):
            yield i

countdown = Countdown(5)
print(list(countdown))              # [5, 4, 3, 2, 1]
print(list(reversed(countdown)))    # [1, 2, 3, 4, 5]
```

---

## 14. Context Managers with Generators

Use generators to create context managers.

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed: {end - start:.2f} seconds")

with timer():
    sum(range(1000000))
```

---

## 15. Advanced Generator Patterns

### Coroutines

```python
def moving_average():
    total = 0
    count = 0
    average = None
    
    while True:
        value = yield average
        total += value
        count += 1
        average = total / count

ma = moving_average()
next(ma)  # Prime
print(ma.send(10))    # 10.0
print(ma.send(20))    # 15.0
print(ma.send(30))    # 20.0
```

### Generator-based State Machines

```python
def traffic_light():
    while True:
        yield "Green"
        yield "Yellow"
        yield "Red"

light = traffic_light()
for _ in range(6):
    print(next(light))
# Green, Yellow, Red, Green, Yellow, Red
```

---

## 16. Best Practices

### 1. Use Generators for Large Data

```python
# Bad - loads everything in memory
def read_large_file_bad(filename):
    with open(filename) as f:
        return f.readlines()

# Good - lazy loading
def read_large_file_good(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

### 2. Generator Expressions Over List Comprehensions

```python
# When you only iterate once
total = sum(x**2 for x in range(1000000))  # Generator
# Not: sum([x**2 for x in range(1000000)])  # List
```

### 3. Use itertools for Complex Iterations

```python
from itertools import chain, islice

# Instead of manual iteration
result = chain([1, 2], [3, 4], [5, 6])
```

---

## 17. Common Patterns Summary

### Pattern 1: File Processing
```python
# Always use generators for files
def process_file(filename):
    with open(filename) as f:
        for line in f:  # File object is already an iterator!
            yield process_line(line)
```

### Pattern 2: Infinite Sequences
```python
# Use itertools for infinite sequences
from itertools import count, cycle, repeat

# Counter: 0, 1, 2, 3, ...
count(0)

# Cycle: 1, 2, 3, 1, 2, 3, ...
cycle([1, 2, 3])

# Repeat: 'x', 'x', 'x', ...
repeat('x', times=10)
```

### Pattern 3: Pipeline Composition
```python
# Chain transformations
data = read_source()
filtered = filter_func(data)
transformed = transform_func(filtered)
result = aggregate_func(transformed)
```

### Pattern 4: Two-Argument iter()
```python
# Read until sentinel
with open('file.txt') as f:
    for line in iter(f.readline, '\n'):
        process(line)

# Generate until value
import random
for num in iter(lambda: random.randint(1, 6), 6):
    print(num)
```

### Pattern 5: Generator Expressions in Functions
```python
# No need for intermediate list
sum(x**2 for x in range(1000000))
max(len(word) for word in words)
any(x > 100 for x in numbers)
all(x > 0 for x in numbers)
```

---
