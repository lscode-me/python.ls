# Week 1 — Python Core Foundations (Lecture 1)
## Objects, References, Memory, Types

---

## 1. Python Objects & References

In Python, everything is an object — integers, strings, lists, functions, classes.

A variable does not store a value directly.  
It stores a reference to an object in memory.

```python
a = 10      # create int object 10, bind name "a" to it
b = a       # b refers to the same object
```

Assignments never copy objects.  
Multiple names may refer to the same object.  
Mutating an object affects all references to it.

---

## 2. Built-in Data Types (Core Set)

### Immutable Types
- int
- float
- bool
- str
- tuple
- frozenset
- bytes

### Mutable Types
- list
- dict
- set
- bytearray
- user-defined objects

---

## 3. Reference Counting (RC)

CPython uses reference counting as the primary garbage collection method.

Every object stores an internal counter: how many references point to it.

```python
import sys

x = []
print(sys.getrefcount(x))
```

When the counter becomes 0, the object is immediately deallocated.

Reference counting is complemented by a cycle detector (GC).

---

## 4. Python Memory Manager

Python memory handling includes:

1. Reference counter  
2. Garbage Collector for cyclic references  
3. PyObject allocator (arenas, pools, blocks)

Small objects (ints, strings, tuples) are allocated efficiently via internal caches.

---

## 5. Mutable vs Immutable in Practice

### Immutable example
```python
a = "hello"
b = a
a += "!"   # creates a new string object
```

### Mutable example
```python
x = [1, 2]
y = x
x.append(3)
```

y is modified too, because both names point to the same list.

---

## 6. Identity vs Equality (`is` vs `==`)

`==` checks value equality.  
`is` checks identity (same object in memory).

---

## 7. Identity Examples (`a is b`)

### Integers
```python
a, b = 1, 1
a is b          # True (small int cache)

a, b = 256, 256
a is b          # True

a, b = 257, 257
a is b          # False (not guaranteed to be cached)
```

### Strings
```python
a, b = "hello", "hello"
a is b          # True (interned)

a = "hello world!!1"
b = "hello world!!1"
a is b          # May be True or False
```

### Lists
```python
a, b = [], []
a is b          # False

c = a
a is c          # True
```

---

## 8. Mutable Default Arguments

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst
```

Usage:
```python
add_item(1)   # [1]
add_item(2)   # [1, 2]
add_item(3)   # [1, 2, 3]
```

Correct version:
```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 9. Constructors & Type Converters

### Numeric
```python
int("5")
float("3.14")
bool(0)
```

### Containers
```python
list("abc")       # ['a','b','c']
tuple([1, 2])     # (1, 2)
set([1, 1, 2])    # {1, 2}
```

### Strings
```python
str(123)
repr([1, 2, 3])
```

---

