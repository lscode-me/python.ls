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
