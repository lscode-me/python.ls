# Python Core Foundations
## Objects, References, Memory, Types

---

## 📋 Prerequisites

Before starting this module, you should:

- Have Python 3.8+ installed
- Be comfortable with basic Python syntax (variables, functions, loops)
- Understand the difference between values and variables conceptually

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- Explain how Python represents data as objects
- Distinguish between object identity and equality
- Predict the behavior of mutable vs immutable types
- Use introspection tools (`id`, `type`, `sys.getrefcount`)
- Avoid common pitfalls with mutable default arguments
- Understand how Python manages memory through reference counting

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

Python's built-in types are divided into two categories based on whether their value can be changed after creation. This distinction is fundamental to understanding Python's behavior and avoiding subtle bugs.

### Immutable Types

Once created, these objects cannot be modified. Any "modification" creates a new object:

- `int` — integers of unlimited size
- `float` — floating-point numbers
- `bool` — `True` or `False`
- `str` — text strings
- `tuple` — fixed-length sequences
- `frozenset` — immutable set
- `bytes` — immutable byte sequence

### Mutable Types

These objects can be changed in place. All references to the object see the changes:

- `list` — dynamic arrays
- `dict` — key-value mappings
- `set` — unique element collections
- `bytearray` — mutable byte sequence
- user-defined objects (by default)

**Why does this matter?** If you pass a mutable object to a function and modify it, the caller sees the change. With immutable objects, you always get a new object instead.

---

## 3. Reference Counting (RC)

CPython uses reference counting as the primary garbage collection method. Every object stores an internal counter tracking how many references point to it. When the counter reaches 0, the object is immediately deallocated from memory.

```python
import sys

x = []
print(sys.getrefcount(x))  # Output: 2 (x + temporary reference from getrefcount)
```

**Why 2 and not 1?** The `getrefcount()` function itself creates a temporary reference to the object when you pass it as an argument.

```python
a = []
b = a       # Now refcount is 2
c = a       # Now refcount is 3
del b       # Back to 2
del c       # Back to 1
del a       # Refcount becomes 0 → object deallocated
```

Reference counting is complemented by a **cycle detector** (GC) that handles circular references (e.g., when object A references B and B references A).

---

## 4. Python Memory Manager

Python manages memory automatically, freeing you from manual allocation and deallocation. The memory system has three layers:

1. **Reference Counter** — tracks object usage, deallocates when count reaches 0
2. **Garbage Collector** — handles cyclic references that refcount can't detect
3. **PyObject Allocator** — organizes memory into arenas, pools, and blocks for efficiency

**Small Object Optimization:**

Small integers (-5 to 256) and short strings are cached and reused. This is why:

```python
a = 256
b = 256
print(a is b)  # Output: True — same cached object

a = 257
b = 257
print(a is b)  # Output: False — different objects (not cached)
```

This optimization improves performance for common values but can lead to surprising `is` behavior.

---

## 5. Mutable vs Immutable in Practice

Understanding mutability is critical for predicting Python's behavior and avoiding subtle bugs.

### Immutable Example (Strings)

When you "modify" an immutable object, Python creates a new object:

```python
a = "hello"
b = a          # b points to the same string as a
print(id(a) == id(b))  # Output: True

a += "!"       # Creates NEW string "hello!", a now points to it
print(a)       # Output: hello!
print(b)       # Output: hello — still points to old object
print(id(a) == id(b))  # Output: False — different objects now
```

### Mutable Example (Lists)

Mutating a list affects all references to it:

```python
x = [1, 2]
y = x          # y points to the SAME list as x
print(id(x) == id(y))  # Output: True

x.append(3)    # Modifies the list in place
print(x)       # Output: [1, 2, 3]
print(y)       # Output: [1, 2, 3] — y sees the change!
```

**Key insight:** The difference isn't about variables — it's about whether the *object itself* can be modified.

---

## 6. Identity vs Equality (`is` vs `==`)

Python has two ways to compare objects, and confusing them is a common source of bugs:

- **`==`** checks **value equality** — do these objects have the same content?
- **`is`** checks **identity** — are these the exact same object in memory?

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # Output: True  — same content
print(a is b)   # Output: False — different objects
print(a is c)   # Output: True  — same object
```

**Rule of thumb:** Use `==` for comparing values. Only use `is` for comparing to `None` or checking singleton objects:

```python
if x is None:      # ✅ Correct
    pass

if x == None:      # ❌ Works but not Pythonic
    pass
```

---

## 7. Identity Examples (`a is b`)

Python's caching and interning optimizations can make `is` behave unexpectedly. These examples show why you should never rely on `is` for value comparison.

### Integers

Small integers (-5 to 256) are cached and reused:

```python
a, b = 1, 1
print(a is b)   # Output: True (small int cache)

a, b = 256, 256
print(a is b)   # Output: True (still in cache range)

a, b = 257, 257
print(a is b)   # Output: False (outside cache range)
```

### Strings

Simple strings are "interned" (shared) for efficiency:

```python
a, b = "hello", "hello"
print(a is b)   # Output: True (interned at compile time)

a = "hello world!!1"
b = "hello world!!1"
print(a is b)   # Output: May be True or False (implementation-dependent)
```

**Why inconsistent?** Interning depends on string content, how it was created, and Python version. Never rely on this behavior!

### Lists

Mutable objects are never cached — each `[]` creates a new list:

```python
a, b = [], []
print(a is b)   # Output: False — two different empty lists

c = a
print(a is c)   # Output: True — same list object
```

---

## 8. Mutable Default Arguments

This is one of Python's most famous "gotchas". Default argument values are evaluated **once** when the function is defined, not each time it's called.

### The Problem

```python
def add_item(item, lst=[]):   # ❌ Dangerous!
    lst.append(item)
    return lst
```

```python
print(add_item(1))   # Output: [1]       — looks fine
print(add_item(2))   # Output: [1, 2]    — wait, where did 1 come from?
print(add_item(3))   # Output: [1, 2, 3] — the list persists!
```

**Why?** The empty list `[]` is created once when Python parses the function definition. Every call uses and modifies that same list.

### The Solution

Use `None` as a sentinel and create the list inside the function:

```python
def add_item(item, lst=None):  # ✅ Safe
    if lst is None:
        lst = []               # Fresh list each call
    lst.append(item)
    return lst
```

```python
print(add_item(1))   # Output: [1]
print(add_item(2))   # Output: [2] — fresh list each time
print(add_item(3))   # Output: [3]
```

**Rule:** Never use mutable objects (`list`, `dict`, `set`) as default arguments.

---

## 9. Constructors & Type Converters

Every built-in type can be called as a function to create new objects or convert between types. These are called **constructors** or **type converters**.

### Numeric Conversions

```python
print(int("5"))       # Output: 5 — string to int
print(int(3.9))       # Output: 3 — float to int (truncates, doesn't round)
print(float("3.14"))  # Output: 3.14
print(bool(0))        # Output: False — 0 is "falsy"
print(bool(42))       # Output: True — non-zero is "truthy"
```

### Container Conversions

```python
print(list("abc"))       # Output: ['a', 'b', 'c'] — string to list of chars
print(tuple([1, 2, 3]))  # Output: (1, 2, 3) — list to tuple
print(set([1, 1, 2, 2])) # Output: {1, 2} — duplicates removed
```

### String Representations

```python
print(str(123))        # Output: '123' — human-readable
print(repr([1, 2, 3])) # Output: '[1, 2, 3]' — debug representation
```

**Difference between `str()` and `repr()`:**
- `str()` — meant for end users, may omit details
- `repr()` — meant for developers, shows how to recreate the object

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
---

## 💡 Key Takeaways

- **Everything is an object**: Integers, strings, functions, classes — all are objects with identity, type, and value.

- **Variables are references**: Assignment binds a name to an object; it never copies the object itself.

- **Mutable vs Immutable**: Mutable objects can be changed in place (affecting all references). Immutable objects create new objects on "modification".

- **`is` vs `==`**: Use `==` for value comparison, `is` only for `None` or singleton checks. Small int/string caching makes `is` unreliable for values.

- **Mutable default arguments**: Never use `list`, `dict`, or `set` as default arguments. Use `None` and create inside the function.

- **Reference counting**: Objects are deallocated when refcount reaches 0. Cyclic references are handled by the garbage collector.

---

## 🚀 Next Steps

**Related Modules:**

- [Functions](../02_Functions/) — how functions are objects and closures work
- [OOP](../08_OOP/) — creating custom objects with classes

**Practice Ideas:**

1. Use `id()` to track object identity through various operations
2. Create a function with a mutable default argument and observe the bug
3. Explore `sys.getrefcount()` with different reference scenarios
4. Compare `is` vs `==` with integers around the 256 boundary
5. Use `gc.get_referrers()` to find all references to an object

**Going Deeper:**

- Study CPython's small integer cache implementation
- Learn about string interning with `sys.intern()`
- Explore weak references with the `weakref` module
- Understand `__slots__` for memory-efficient objects