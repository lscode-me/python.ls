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
