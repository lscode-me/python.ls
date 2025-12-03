# Pythonic Code - Homework


## Task 1 – Manual indexing instead of direct iteration

Rewrite this function in a more Pythonic way.

```python
def print_names(names):
    i = 0
    while i < len(names):
        print("Name:", names[i])
        i = i + 1
```


## Task 2 – Verbose filtering and mapping
Rewrite this code so that it is shorter, clearer, and more Pythonic.

```python
numbers = [3, 10, 15, 20, 21, 30]
result = []
for n in numbers:
    if n % 3 == 0:
        result.append(n * 2)
print(result)
```


## Task 3 – Building a string with manual concatenation
Rewrite this code in a more efficient and Pythonic way.

```python
words = ["Python", "is", "fun"]
sentence = ""
for w in words:
    if sentence == "":
        sentence = w
    else:
        sentence = sentence + " " + w
print(sentence)
```


## Task 4 – Using range(len(...)) instead of enumerate
Rewrite this function in a cleaner, more idiomatic way.

```python
def print_indexed(items):
    i = 0
    while i < len(items):
        print(i, "->", items[i])
        i = i + 1
```


## Task 5 – Manual dictionary construction from two lists
Rewrite this code to make it shorter, clearer, and more Pythonic.

```python
keys = ["name", "age", "city"]
values = ["Alice", 30, "London"]

result = {}
i = 0
while i < len(keys):
    key = keys[i]
    value = values[i]
    result[key] = value
    i = i + 1

print(result)
```


## Task 6 – File handling without context manager
Rewrite this function in a safer and more Pythonic way.

```python
def read_config(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data
```


## Task 7 – Mutable default argument and non-Pythonic loop
Improve both the function signature and the loop body to be more Pythonic and predictable.

```python
def add_item(item, items=[]):
    i = 0
    while i < len(items):
        i = i + 1
    items.append(item)
    return items
```


## Task 8 – Manual max search with unnecessary complexity
Rewrite this function in a simpler, more idiomatic way.

```python
def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
        i = i + 1
    return max_value
```


## Task 9 – LBYL instead of EAFP
Rewrite this code following the EAFP principle (Easier to Ask for Forgiveness than Permission).

```python
def get_user_age(users, username):
    if username in users:
        if 'age' in users[username]:
            return users[username]['age']
        else:
            return None
    else:
        return None
```


## Task 10 – Non-Pythonic dictionary comprehension
Rewrite this code using a dictionary comprehension.

```python
words = ["hello", "world", "python", "is", "great"]
word_lengths = {}
for word in words:
    if len(word) > 2:
        word_lengths[word] = len(word)
```


## Task 11 – Building a list when a generator would be better
Rewrite this function to use a generator instead of building a full list in memory.

```python
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Used like this:
total = sum(get_squares(1000000))
```


## Task 12 – Manual counter implementation
Rewrite this code using `Counter` from the `collections` module.

```python
words = "the quick brown fox jumps over the lazy dog".split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
```


## Task 13 – Verbose string formatting
Rewrite this code using f-strings (Python 3.6+).

```python
name = "Alice"
age = 25
city = "NYC"

info = "Name: " + name + ", Age: " + str(age) + ", City: " + city
```


## Task 14 – Complex range checking
Rewrite this code using chained comparisons.

```python
def is_valid_percentage(value):
    if value >= 0 and value <= 100:
        return True
    else:
        return False
```


## Task 15 – Manual all/any implementation
Rewrite these functions using built-in `all()` and `any()`.

```python
def all_positive(numbers):
    for num in numbers:
        if num <= 0:
            return False
    return True

def has_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
    return False
```


## Task 16 – Type checking instead of duck typing
Rewrite this function to be more Pythonic by embracing duck typing.

```python
def process_items(items):
    if not isinstance(items, list):
        raise TypeError("Must provide a list!")
    
    total = 0
    for item in items:
        total += item
    return total
```


## Task 17 – Manual unpacking and swapping
Rewrite this code using tuple unpacking to make it more elegant.

```python
def swap_first_last(items):
    if len(items) < 2:
        return items
    
    temp = items[0]
    items[0] = items[-1]
    items[-1] = temp
    return items

def parse_user_line(line):
    # line format: "Alice,25,alice@example.com"
    parts = line.split(',')
    name = parts[0]
    age = int(parts[1])
    email = parts[2]
    return name, age, email
```


## Task 18 – Building a set manually
Rewrite this code using a set comprehension.

```python
text = "the quick brown fox jumps over the lazy dog"
unique_lengths = set()
for word in text.split():
    unique_lengths.add(len(word))
```


## Task 19 – Nested loops instead of zip
Rewrite this code using `zip()`.

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

i = 0
while i < len(names):
    print(f"{names[i]} is {ages[i]} years old")
    i += 1
```


## Task 20 – Manual defaultdict behavior
Rewrite this code using `defaultdict` from the `collections` module.

```python
transactions = [
    ('food', 50),
    ('transport', 20),
    ('food', 30),
    ('entertainment', 100),
    ('food', 25)
]

category_totals = {}
for category, amount in transactions:
    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] += amount
```
