# Functions and Functional Programming
## Functions, Closures, Decorators

---

## 1. Function Basics

Functions are first-class objects in Python — they can be:
- Assigned to variables
- Passed as arguments
- Returned from other functions
- Stored in data structures

```python
def greet(name):
    return f"Hello, {name}!"

# Assign to variable
say_hello = greet
print(say_hello("Alice"))    # Hello, Alice!

# Store in list
functions = [greet, len, str]
```

---

## 2. Function Arguments

### Positional Arguments

```python
def add(a, b):
    return a + b

print(add(3, 5))    # 8
```

### Keyword Arguments

```python
def describe_person(name, age, city):
    return f"{name}, {age} years old, from {city}"

print(describe_person(name="Alice", age=30, city="NYC"))
print(describe_person(age=30, city="NYC", name="Alice"))    # Order doesn't matter
```

### Default Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))                    # Hello, Alice!
print(greet("Bob", "Hi"))                # Hi, Bob!
print(greet("Charlie", greeting="Hey"))  # Hey, Charlie!
```

### *args (Variable Positional Arguments)

```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))           # 6
print(sum_all(1, 2, 3, 4, 5))     # 15
```

### **kwargs (Variable Keyword Arguments)

```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC
```

### Combining All Argument Types

```python
def complex_function(a, b, *args, key1="default", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"key1={key1}")
    print(f"kwargs={kwargs}")

complex_function(1, 2, 3, 4, key1="value", extra1="x", extra2="y")
```

---

## 3. Return Values

### Single Return

```python
def square(x):
    return x ** 2
```

### Multiple Returns (Tuple Unpacking)

```python
def divide_and_remainder(a, b):
    return a // b, a % b

quotient, remainder = divide_and_remainder(17, 5)
print(quotient, remainder)    # 3 2
```

### Early Return

```python
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None
```

---

## 4. Scope and Namespaces

### Local vs Global

```python
x = "global"

def func():
    x = "local"
    print(x)

func()        # local
print(x)      # global
```

### Global Keyword

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)    # 1
```

### Nonlocal Keyword

```python
def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "inner"
    
    inner()
    print(x)    # inner

outer()
```

---

## 5. Lambda Functions

Lambda functions are anonymous, single-expression functions.

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))    # 25
```

### Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(3, 5))    # 8
```

### Lambda in Higher-Order Functions

```python
numbers = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)    # [1, 4, 9, 16, 25]

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)      # [2, 4]

# sorted
words = ["apple", "pie", "zoo", "a"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)    # ['a', 'zoo', 'pie', 'apple']
```

---

## 6. Closures

A closure is a function that captures variables from its enclosing scope.

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
add_10 = outer(10)

print(add_5(3))     # 8
print(add_10(3))    # 13
```

### Practical Example: Counter

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())    # 1
print(counter())    # 2
print(counter())    # 3
```

---

## 7. Decorators

Decorators modify or enhance functions without changing their code.

### Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before function call
# Hello!
# After function call
```

### Decorator with Arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Preserving Function Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def example():
    """This is the docstring"""
    pass

print(example.__name__)    # example
print(example.__doc__)     # This is the docstring
```

---

## 8. Higher-Order Functions

Functions that take functions as arguments or return functions.

### map()

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)    # [1, 4, 9, 16]
```

### filter()

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)    # [2, 4, 6]
```

### reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)    # 120
```

---

## 9. Partial Functions

Partially apply arguments to a function.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))    # 25
print(cube(5))      # 125
```

---

## 10. Generator Functions

Generators produce values lazily using `yield`.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))    # 1
print(next(counter))    # 2

for num in count_up_to(3):
    print(num)
# 1
# 2
# 3
```

### Generator Expressions

```python
# List comprehension (creates list in memory)
squares_list = [x ** 2 for x in range(10)]

# Generator expression (lazy evaluation)
squares_gen = (x ** 2 for x in range(10))

print(sum(squares_gen))    # 285
```

---

## 11. Recursion

Functions that call themselves.

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))    # 120
```

### Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))    # 13
```

### Tail Recursion Optimization (Manual)

```python
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

print(factorial_tail(5))    # 120
```

---

## 12. Function Annotations and Type Hints

```python
def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old"

def process_items(items: list[int]) -> list[int]:
    return [item * 2 for item in items]
```

### Using typing Module

```python
from typing import List, Dict, Optional, Union, Callable

def process_data(
    data: List[Dict[str, Union[int, str]]],
    transform: Callable[[int], int]
) -> Optional[List[int]]:
    pass
```

---

## 13. Functional Programming Concepts

### Pure Functions

Functions that:
- Always return the same output for same input
- Have no side effects

```python
# Pure function
def add(a, b):
    return a + b

# Impure function (side effect)
total = 0
def add_to_total(x):
    global total
    total += x
    return total
```

### Immutability

```python
# Instead of modifying
items = [1, 2, 3]
# items.append(4)

# Create new
items = [1, 2, 3]
new_items = items + [4]
```

### Function Composition

```python
def compose(f, g):
    return lambda x: f(g(x))

def add_5(x):
    return x + 5

def multiply_2(x):
    return x * 2

# Compose functions
composed = compose(add_5, multiply_2)
print(composed(3))    # (3 * 2) + 5 = 11
```

---

## 14. Common Functional Patterns

### List Comprehensions

```python
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

### Dictionary Comprehensions

```python
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
```

### Set Comprehensions

```python
unique_lengths = {len(word) for word in ["apple", "pie", "zoo", "a"]}
```

### Nested Comprehensions

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---
