# Python Core Foundations
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

# Working with Python Objects: Introspection, Identity, References, and Memory

This document summarizes the essential Python functions and tools used to inspect objects, understand references, measure memory usage, and analyze the Python memory model.

---

## 1. 🔍 Basic Object Introspection

### **`type(obj)`**
Returns the type of an object.

```python
type(10)          # <class 'int'>
type([1, 2])      # <class 'list'>
```

### **`id(obj)`**
Returns the identity of an object.  
In CPython, this is the memory address.

```python
a = 42
id(a)             # e.g., 140734962178768
```

### **`isinstance(obj, cls)`**
Checks whether an object belongs to a given class or type.

```python
isinstance("hi", str)      # True
```

### **`callable(obj)`**
Checks whether an object can be called like a function.

---

## 2. 🔗 Reference Counting

### **`sys.getrefcount(obj)`**
Returns the reference count of the object.

⚠️ Note: Passing the object as a function argument temporarily adds a reference.

```python
import sys
x = []
sys.getrefcount(x)
```

When the count reaches **0**, the object is deallocated.

---

## 3. 📦 Size & Memory Footprint

### **`sys.getsizeof(obj)`**
Returns the size of the object in bytes (non-recursive).

```python
import sys
sys.getsizeof(1000)
sys.getsizeof([])
```

For containers, this returns only the “shell” size, not the full deep size.

For recursive measurement, external libraries like `pympler.asizeof` are needed.

---

## 4. 🧠 Garbage Collector Tools (`gc`)

### **`gc.get_referrers(obj)`**
Returns objects that reference the given object.

### **`gc.get_referents(obj)`**
Returns objects referenced *by* the given object.

```python
import gc
a = [1, 2, 3]
gc.get_referents(a)
```

### **`gc.get_objects()`**
Returns all objects tracked by Python’s garbage collector.

### **`gc.is_tracked(obj)`**
Checks whether an object is tracked by the garbage collector.  
Most immutable objects are **not** tracked.

---

## 5. 🧩 Object Structure & Attributes

### **`dir(obj)`**
Lists attributes and methods of an object.

### **`vars(obj)`**
Returns the `__dict__` of a custom object.

### **`obj.__dict__`**
The actual attribute storage (may not exist for all objects).

### **`hash(obj)`**
Returns the hash value of the object (if hashable).

### **String Representations**

- `repr(obj)` — detailed/debug representation  
- `str(obj)` — user-friendly string form

---

## 6. 🧪 Identity vs Equality

### **`a is b`**
Checks identity — whether both names point to the same object.

### **`a == b`**
Checks value equality.

```python
a = [1, 2]
b = a
a is b      # True
a == b      # True

c = [1, 2]
a is c      # False
a == c      # True
```

---

## 7. 🧬 Type Construction & Conversion

Useful for demonstrating object creation and type changes.

### **Core constructors:**

- `int()`
- `float()`
- `str()`
- `list()`
- `tuple()`
- `set()`
- `dict()`
- `bool()`
- `bytes()`
- `bytearray()`

These create new objects (and sometimes intern or reuse objects depending on Python’s optimization rules).

---

## 8. 📘 Summary Table

| Category | Function / Operator | Purpose |
|---------|----------------------|---------|
| Type | `type(obj)` | Get object type |
| Identity | `id(obj)` | Memory address (CPython) |
| Equality | `==` | Value equality |
| Identity | `is` | Same object in memory |
| Size | `sys.getsizeof(obj)` | Object size (bytes) |
| Refcount | `sys.getrefcount(obj)` | Number of references |
| GC | `gc.get_referrers(obj)` | Objects pointing to obj |
| GC | `gc.get_referents(obj)` | Objects obj points to |
| GC | `gc.is_tracked(obj)` | GC tracking status |
| Structure | `dir(obj)` | Attributes and methods |
| Structure | `vars(obj)` | Object namespace |
| Structure | `obj.__dict__` | Direct attribute storage |
| Hash | `hash(obj)` | Hash value |
| Stringification | `repr(obj)` | Debug string |
| Stringification | `str(obj)` | Human-readable string |

---

## ✔️ Conclusion

These functions form the core toolkit for exploring how Python represents objects, manages memory, tracks references, and exposes object internals.  
They are essential for understanding Python’s memory model and teaching how variables, references, and objects actually work under the hood.
