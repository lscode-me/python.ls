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

The order of parameters in function definition must follow this pattern:
1. Regular positional parameters (`a, b`)
2. `*args` (variable positional)
3. Keyword-only parameters or parameters with defaults
4. `**kwargs` (variable keyword)

```python
def complex_function(a, b, *args, key1="default", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"key1={key1}")
    print(f"kwargs={kwargs}")

# Call with mixed arguments
complex_function(1, 2, 3, 4, key1="value", extra1="x", extra2="y")
```

**Output:**
```
a=1, b=2
args=(3, 4)
key1=value
kwargs={'extra1': 'x', 'extra2': 'y'}
```

**Explanation:**
- `1, 2` → positional arguments `a` and `b`
- `3, 4` → captured by `*args` as a tuple
- `key1="value"` → overrides the default value of `key1`
- `extra1="x", extra2="y"` → captured by `**kwargs` as a dictionary

### Argument Unpacking

You can unpack sequences and dictionaries when calling functions:

```python
def calculate(a, b, c):
    return (a + b) * c

# Unpack list/tuple with *
numbers = [2, 3, 4]
result = calculate(*numbers)  # Same as calculate(2, 3, 4)
print(result)  # 20

# Unpack dictionary with **
params = {"a": 2, "b": 3, "c": 4}
result = calculate(**params)  # Same as calculate(a=2, b=3, c=4)
print(result)  # 20
```

### Keyword-Only Arguments

Force arguments to be specified by name using `*`:

```python
def create_user(name, *, email, age):
    """email and age must be passed as keyword arguments"""
    return f"User: {name}, {email}, {age}"

# This works
create_user("Alice", email="alice@example.com", age=30)

# This raises TypeError - email and age must be keyword arguments
# create_user("Alice", "alice@example.com", 30)
```

### Positional-Only Arguments

Force arguments to be positional using `/` (Python 3.8+):

```python
def divide(a, b, /):
    """a and b must be passed as positional arguments"""
    return a / b

# This works
divide(10, 2)  # 5.0

# This raises TypeError - a and b cannot be keyword arguments
# divide(a=10, b=2)
```

### Complete Example

```python
def advanced_function(pos_only, /, pos_or_kw, *, kw_only, **kwargs):
    """
    pos_only: positional-only
    pos_or_kw: can be positional or keyword
    kw_only: keyword-only
    kwargs: additional keyword arguments
    """
    print(f"pos_only={pos_only}")
    print(f"pos_or_kw={pos_or_kw}")
    print(f"kw_only={kw_only}")
    print(f"kwargs={kwargs}")

advanced_function(1, 2, kw_only=3, extra="value")
# pos_only=1
# pos_or_kw=2
# kw_only=3
# kwargs={'extra': 'value'}
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

### Understanding Variable Visibility

Python uses the **LEGB rule** to resolve variable names:
- **L**ocal: Inside the current function
- **E**nclosing: In enclosing functions (for nested functions)
- **G**lobal: At the module level
- **B**uilt-in: Python built-in names

```python
# Built-in scope
# len, print, etc.

global_var = "I'm global"  # Global scope

def outer_function():
    enclosing_var = "I'm in enclosing scope"  # Enclosing scope
    
    def inner_function():
        local_var = "I'm local"  # Local scope
        print(local_var)          # Local
        print(enclosing_var)      # Enclosing
        print(global_var)         # Global
        print(len([1, 2, 3]))     # Built-in
    
    inner_function()

outer_function()
```

### Local vs Global

Variables created inside functions are local by default:

```python
x = "global"

def func():
    x = "local"  # Creates a NEW local variable, doesn't modify global x
    print(x)

func()        # local
print(x)      # global (unchanged)
```

**Important:** Reading a global variable works without declaration:

```python
count = 10

def show_count():
    print(count)  # Can read global variable

show_count()  # 10
```

But modifying requires `global` keyword:

```python
count = 10

def modify_count():
    # This will raise UnboundLocalError without 'global'
    # count = count + 1  # Error!
    pass

def modify_count_correct():
    global count
    count = count + 1  # Now it works

modify_count_correct()
print(count)  # 11
```

### Global Keyword

Use `global` to modify variables in global scope:

```python
counter = 0

def increment():
    global counter
    counter += 1

def reset():
    global counter
    counter = 0

increment()
increment()
print(counter)    # 2

reset()
print(counter)    # 0
```

**Warning:** Overusing `global` is considered bad practice. Better alternatives:
- Return values from functions
- Use classes to maintain state
- Pass values as parameters

```python
# Bad: using global
total = 0

def add_to_total(x):
    global total
    total += x

# Good: return values
def add(current_total, x):
    return current_total + x

total = 0
total = add(total, 5)
total = add(total, 3)
```

### Nonlocal Keyword

Use `nonlocal` to modify variables in enclosing (but not global) scope:

```python
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # Refers to x in outer()
        x = "inner"
        print(f"Inside inner: {x}")
    
    print(f"Before inner: {x}")
    inner()
    print(f"After inner: {x}")

outer()
# Before inner: outer
# Inside inner: inner
# After inner: inner
```

**Difference between `global` and `nonlocal`:**

```python
x = "global"

def outer():
    x = "enclosing"
    
    def use_global():
        global x
        x = "modified global"
        print(f"use_global: {x}")
    
    def use_nonlocal():
        nonlocal x
        x = "modified enclosing"
        print(f"use_nonlocal: {x}")
    
    print(f"Initial enclosing x: {x}")
    use_nonlocal()
    print(f"After nonlocal: {x}")
    use_global()
    print(f"Enclosing x after global: {x}")

print(f"Initial global x: {x}")
outer()
print(f"Final global x: {x}")

# Output:
# Initial global x: global
# Initial enclosing x: enclosing
# use_nonlocal: modified enclosing
# After nonlocal: modified enclosing
# use_global: modified global
# Enclosing x after global: modified enclosing
# Final global x: modified global
```

### Variable Shadowing

Inner scopes can "shadow" outer variables:

```python
x = 100

def outer():
    x = 10  # Shadows global x
    
    def inner():
        x = 1  # Shadows enclosing x
        print(f"Inner x: {x}")
    
    inner()
    print(f"Outer x: {x}")

outer()
print(f"Global x: {x}")

# Inner x: 1
# Outer x: 10
# Global x: 100
```

### Best Practices for Scope

1. **Minimize use of `global`**: Makes code harder to test and reason about
2. **Prefer returning values**: More explicit and testable
3. **Use function parameters**: Pass data explicitly
4. **Avoid shadowing**: Don't reuse variable names across scopes unnecessarily

```python
# Good practice example
def calculate_statistics(numbers):
    """Pure function - no global state"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return {
        'total': total,
        'count': count,
        'average': average
    }

result = calculate_statistics([1, 2, 3, 4, 5])
print(result)  # {'total': 15, 'count': 5, 'average': 3.0}
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

Decorators are a powerful feature that allows you to modify or enhance the behavior of functions or methods without directly changing their code. They are essentially functions that take another function as an argument and return a new function.

### Understanding the Decorator Concept

At its core, a decorator is just **syntactic sugar** for wrapping functions:

```python
def my_decorator(func):
    def wrapper():
        print("Something before")
        func()
        print("Something after")
    return wrapper

# These two are equivalent:
@my_decorator
def say_hello():
    print("Hello!")

# Is the same as:
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)
```

The `@decorator` syntax is just a cleaner way to wrap functions.

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

**What happens here:**
1. `say_hello` function is defined
2. `@my_decorator` passes `say_hello` to `my_decorator`
3. `my_decorator` returns `wrapper` function
4. `say_hello` now refers to `wrapper`
5. When we call `say_hello()`, we actually call `wrapper()`

### Decorator with Function Arguments

To handle functions with arguments, use `*args` and `**kwargs`:

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result = add(3, 5)
# Calling add with args=(3, 5), kwargs={}
# add returned 8

message = greet("Alice", greeting="Hi")
# Calling greet with args=('Alice',), kwargs={'greeting': 'Hi'}
# greet returned Hi, Alice!
```

### Practical Decorators

#### Timing Decorator

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

result = slow_function()
# slow_function took 1.0012 seconds
```

#### Authentication Decorator

```python
def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            raise PermissionError("User not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def view_account(user):
    return f"Account details for {user['name']}"

# This works
user1 = {"name": "Alice", "authenticated": True}
print(view_account(user1))

# This raises PermissionError
user2 = {"name": "Bob", "authenticated": False}
# view_account(user2)  # Raises PermissionError
```

#### Retry Decorator

```python
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_network_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success"
```

### Decorators with Arguments

When decorator itself takes arguments, you need an extra level of nesting:

```python
def repeat(times):
    """Decorator factory - returns a decorator"""
    def decorator(func):
        """Actual decorator"""
        def wrapper(*args, **kwargs):
            """Wrapper function"""
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

**How it works:**
1. `repeat(times=3)` is called first, returns `decorator`
2. `@decorator` is applied to `greet`
3. `greet` becomes `wrapper`

### Preserving Function Metadata

Without `functools.wraps`, decorated functions lose their metadata:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is the docstring"""
    pass

print(example.__name__)    # wrapper (wrong!)
print(example.__doc__)     # None (lost!)
```

Use `@wraps` to preserve metadata:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # This preserves func's metadata
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

print(example.__name__)    # example (correct!)
print(example.__doc__)     # This is the docstring (preserved!)
```

### Stacking Multiple Decorators

You can apply multiple decorators to a single function:

```python
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
# <b><i>Hello, Alice</i></b>
```

Decorators are applied **bottom to top** (inside out):
```python
# This:
@bold
@italic
def greet(name):
    return f"Hello, {name}"

# Is equivalent to:
greet = bold(italic(greet))
```

### Class-Based Decorators

Decorators can also be classes:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call 1 to say_hello
say_hello()  # Call 2 to say_hello
say_hello()  # Call 3 to say_hello
```

### Real-World Use Cases

Decorators are commonly used for:
- **Logging**: Track function calls and parameters
- **Timing**: Measure execution time
- **Caching/Memoization**: Store results of expensive function calls
- **Authentication/Authorization**: Check permissions before execution
- **Rate limiting**: Control how often functions can be called
- **Input validation**: Validate arguments before function execution
- **Deprecation warnings**: Mark functions as deprecated

Example with caching:

```python
from functools import wraps

def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Much faster with memoization!
print(fibonacci(35))  # Instant with cache
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

**Immutability** means that data cannot be changed after it's created. In functional programming, immutable data structures are preferred because they:
- Make code easier to reason about
- Prevent unexpected side effects
- Enable safer concurrent programming
- Make debugging easier

#### Mutable vs Immutable Types in Python

**Immutable types** (cannot be changed):
- `int`, `float`, `bool`, `str`, `tuple`, `frozenset`

**Mutable types** (can be changed):
- `list`, `dict`, `set`, and most custom objects

```python
# Immutable: strings
text = "hello"
# text[0] = "H"  # TypeError: 'str' object does not support item assignment
new_text = "H" + text[1:]  # Create a new string
print(new_text)  # "Hello"

# Mutable: lists
numbers = [1, 2, 3]
numbers[0] = 10  # This works - modifies in place
print(numbers)   # [10, 2, 3]
```

#### Why Immutability Matters

**Problem with mutable data:**

```python
def add_item(item, items=[]):  # DANGEROUS!
    items.append(item)
    return items

# Default list is shared across calls!
list1 = add_item(1)
list2 = add_item(2)
print(list1)  # [1, 2] - unexpected!
print(list2)  # [1, 2] - same object!
```

**Solution with immutability:**

```python
def add_item(item, items=None):
    if items is None:
        items = []  # Create new list each time
    return items + [item]  # Return new list

list1 = add_item(1)
list2 = add_item(2)
print(list1)  # [1]
print(list2)  # [2]
```

#### Immutable Approach: Create New Instead of Modifying

```python
# Bad: Modifying in place (mutable approach)
def add_to_list(items, value):
    items.append(value)  # Side effect!
    return items

original = [1, 2, 3]
result = add_to_list(original, 4)
print(original)  # [1, 2, 3, 4] - original changed!
print(result)    # [1, 2, 3, 4]

# Good: Creating new (immutable approach)
def add_to_list(items, value):
    return items + [value]  # or: return [*items, value]

original = [1, 2, 3]
result = add_to_list(original, 4)
print(original)  # [1, 2, 3] - unchanged!
print(result)    # [1, 2, 3, 4] - new list
```

#### Working with Immutable Data

**Lists:**

```python
# Instead of mutating
numbers = [1, 2, 3]
# numbers.append(4)

# Create new
numbers = [1, 2, 3]
new_numbers = numbers + [4]
# or
new_numbers = [*numbers, 4]

# Filter without modification
original = [1, 2, 3, 4, 5]
evens = [x for x in original if x % 2 == 0]

# Map without modification
original = [1, 2, 3]
squared = [x ** 2 for x in original]
```

**Dictionaries:**

```python
# Instead of mutating
user = {"name": "Alice", "age": 30}
# user["city"] = "NYC"

# Create new
user = {"name": "Alice", "age": 30}
updated_user = {**user, "city": "NYC"}
print(user)          # {'name': 'Alice', 'age': 30}
print(updated_user)  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Update existing key
user = {"name": "Alice", "age": 30}
updated_user = {**user, "age": 31}
print(updated_user)  # {'name': 'Alice', 'age': 31}
```

**Using tuples instead of lists:**

```python
# Immutable collection
coordinates = (10, 20)
# coordinates[0] = 15  # TypeError

# Must create new tuple
new_coordinates = (15, coordinates[1])

# Good for function returns
def get_point():
    return (100, 200)  # Tuple - immutable

x, y = get_point()
```

#### Immutability and Function Arguments

Functions should not modify their arguments:

```python
# Bad: Modifies input
def process_data(data):
    data["processed"] = True  # Side effect!
    return data

# Good: Returns new data
def process_data(data):
    return {**data, "processed": True}

original = {"name": "Alice"}
result = process_data(original)
print(original)  # {'name': 'Alice'} - unchanged
print(result)    # {'name': 'Alice', 'processed': True}
```

#### Deep vs Shallow Copies

When you need to work with nested structures:

```python
import copy

# Shallow copy - nested objects are still shared
original = {"name": "Alice", "scores": [90, 85, 88]}
shallow = original.copy()
shallow["scores"].append(92)
print(original["scores"])  # [90, 85, 88, 92] - modified!

# Deep copy - completely independent
original = {"name": "Alice", "scores": [90, 85, 88]}
deep = copy.deepcopy(original)
deep["scores"].append(92)
print(original["scores"])  # [90, 85, 88] - unchanged!
print(deep["scores"])      # [90, 85, 88, 92]
```

#### Benefits of Immutability

1. **Predictability**: Data doesn't change unexpectedly
2. **Thread safety**: Multiple threads can safely read immutable data
3. **Easier debugging**: Data flow is clear and traceable
4. **Easier testing**: Functions with immutable data are easier to test
5. **Caching**: Immutable objects can be safely cached

```python
# Example: Pure function with immutability
def calculate_total_price(items):
    """
    Pure function - doesn't modify input, always returns same output for same input
    """
    return sum(item["price"] for item in items)

# Safe to call multiple times
items = [
    {"name": "Apple", "price": 1.5},
    {"name": "Banana", "price": 0.5}
]

total1 = calculate_total_price(items)
total2 = calculate_total_price(items)
# items is guaranteed to be unchanged
```

#### When to Use Mutability

While immutability is generally preferred, mutability can be useful for:
- Performance-critical code (avoiding copies)
- Building up large data structures incrementally
- Working with I/O (files, databases)

```python
# Building a large list - mutation is more efficient
def read_large_file(filename):
    lines = []  # Mutable for efficiency
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    return tuple(lines)  # Return immutable tuple
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
