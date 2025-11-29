# Protocols and Interfaces
## Duck Typing, Protocols, Abstract Base Classes

---

## 1. What are Protocols?

Protocols define interfaces through method signatures without explicit inheritance.

In Python, protocols are based on **duck typing**:
> "If it walks like a duck and quacks like a duck, it's a duck."

```python
# No inheritance needed
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm imitating a duck!"

def make_it_quack(thing):
    print(thing.quack())

make_it_quack(Duck())      # Quack!
make_it_quack(Person())    # I'm imitating a duck!
```

---

## 2. Duck Typing vs Static Typing

### Duck Typing (Dynamic)

```python
def process(item):
    # Just call the method - if it exists, it works
    return item.process()

class DataProcessor:
    def process(self):
        return "Processing data"

class ImageProcessor:
    def process(self):
        return "Processing image"

# Both work without inheritance
print(process(DataProcessor()))
print(process(ImageProcessor()))
```

### Static Typing (Traditional)

```java
// Java example - requires explicit interface
interface Processor {
    String process();
}

class DataProcessor implements Processor {
    public String process() {
        return "Processing data";
    }
}
```

---

## 3. Common Built-in Protocols

### Sequence Protocol
Requires: `__len__()` and `__getitem__()`

```python
class MySequence:
    def __init__(self, data):
        self._data = data
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        return self._data[index]

seq = MySequence([1, 2, 3, 4, 5])
print(len(seq))        # 5
print(seq[2])          # 3
print(seq[1:4])        # [2, 3, 4]

# Works with built-in functions
for item in seq:
    print(item)
```

### Container Protocol
Requires: `__contains__()`

```python
class MyContainer:
    def __init__(self, items):
        self._items = items
    
    def __contains__(self, item):
        return item in self._items

container = MyContainer([1, 2, 3, 4, 5])
print(3 in container)     # True
print(10 in container)    # False
```

### Sized Protocol
Requires: `__len__()`

```python
class MyCollection:
    def __init__(self, items):
        self._items = items
    
    def __len__(self):
        return len(self._items)

collection = MyCollection([1, 2, 3])
print(len(collection))    # 3
```

---

## 4. Iterator Protocol

Requires: `__iter__()` and `__next__()`

```python
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in CountDown(5):
    print(num)    # 5, 4, 3, 2, 1
```

---

## 5. Context Manager Protocol

Requires: `__enter__()` and `__exit__()`

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

---

## 6. Callable Protocol

Requires: `__call__()`

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

times_5 = Multiplier(5)
print(times_5(10))    # 50
print(times_5(7))     # 35

# Check if callable
print(callable(times_5))    # True
```

---

## 7. Numeric Protocols

### Arithmetic Operators

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 1)

print(v1 + v2)    # Vector(3, 4)
print(v1 - v2)    # Vector(1, 2)
print(v1 * 3)     # Vector(6, 9)
```

### Comparison Operators

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
sorted_people = sorted(people)
print(sorted_people)    # [Person(Bob, 25), Person(Alice, 30), Person(Charlie, 35)]
```

---

## 8. Typing Protocols (Python 3.8+)

Type hints for structural subtyping using `Protocol`.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

def render(obj: Drawable) -> None:
    print(obj.draw())

# No inheritance needed - just matching interface
render(Circle())    # Drawing a circle
render(Square())    # Drawing a square
```

### Protocol with Properties

```python
from typing import Protocol

class Named(Protocol):
    @property
    def name(self) -> str:
        ...

class Person:
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name

def print_name(obj: Named) -> None:
    print(obj.name)

person = Person("Alice")
print_name(person)    # Alice
```

---

## 9. Abstract Base Classes (ABC)

ABCs enforce interface implementation through inheritance.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    def describe(self) -> str:
        return f"Shape with area {self.area()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

# shape = Shape()    # TypeError: Can't instantiate abstract class

rect = Rectangle(5, 10)
print(rect.area())        # 50
print(rect.describe())    # Shape with area 50
```

---

## 10. Collections ABCs

Python provides abstract base classes for common collection types.

```python
from collections.abc import Sequence, MutableSequence

class MyList(MutableSequence):
    def __init__(self):
        self._items = []
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __delitem__(self, index):
        del self._items[index]
    
    def __len__(self):
        return len(self._items)
    
    def insert(self, index, value):
        self._items.insert(index, value)

my_list = MyList()
my_list.append(1)      # Inherited from MutableSequence
my_list.extend([2, 3]) # Inherited from MutableSequence
print(len(my_list))    # 3
```

### Common Collections ABCs

```python
from collections.abc import (
    Container,      # __contains__
    Iterable,       # __iter__
    Iterator,       # __iter__, __next__
    Sized,          # __len__
    Callable,       # __call__
    Sequence,       # __getitem__, __len__
    MutableSequence,# __setitem__, __delitem__, insert
    Set,            # __contains__, __iter__, __len__
    MutableSet,     # add, discard
    Mapping,        # __getitem__, __iter__, __len__
    MutableMapping, # __setitem__, __delitem__
)
```

---

## 11. Implementing Multiple Protocols

```python
class SmartList:
    def __init__(self, items=None):
        self._items = list(items) if items else []
    
    # Sequence protocol
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    # Container protocol
    def __contains__(self, item):
        return item in self._items
    
    # Iterator protocol
    def __iter__(self):
        return iter(self._items)
    
    # String representation
    def __repr__(self):
        return f"SmartList({self._items})"
    
    # Callable protocol
    def __call__(self):
        return len(self._items)

smart = SmartList([1, 2, 3, 4, 5])
print(len(smart))       # 5
print(smart[2])         # 3
print(3 in smart)       # True
print(smart())          # 5
for item in smart:
    print(item)
```

---

## 12. Runtime Protocol Checking

Check if an object implements a protocol.

```python
from collections.abc import Iterable, Sized, Callable

class MyClass:
    def __init__(self):
        self._items = [1, 2, 3]
    
    def __iter__(self):
        return iter(self._items)
    
    def __len__(self):
        return len(self._items)

obj = MyClass()

print(isinstance(obj, Iterable))    # True
print(isinstance(obj, Sized))       # True
print(isinstance(obj, Callable))    # False
```

---

## 13. Protocol Composition

Combine multiple protocols for complex interfaces.

```python
from typing import Protocol

class Comparable(Protocol):
    def __lt__(self, other) -> bool:
        ...

class Printable(Protocol):
    def __str__(self) -> str:
        ...

class ComparablePrintable(Comparable, Printable, Protocol):
    pass

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __lt__(self, other) -> bool:
        return self.age < other.age
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"

def process(item: ComparablePrintable) -> None:
    print(str(item))

person = Person("Alice", 30)
process(person)
```

---

## 14. Protocols vs ABC: When to Use

### Use Protocols When:
- You want structural subtyping (duck typing with type checking)
- You don't control the classes being used
- You want flexibility without inheritance
- Working with third-party code

### Use ABC When:
- You want to enforce implementation
- You control the class hierarchy
- You want to provide default implementations
- You need runtime enforcement

```python
# Protocol - no inheritance needed
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

# ABC - inheritance required
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass
```

---

## 15. Best Practices

### 1. Keep Protocols Small and Focused

```python
# Good - single responsibility
class Readable(Protocol):
    def read(self) -> str: ...

class Writable(Protocol):
    def write(self, data: str) -> None: ...

# Can combine when needed
class ReadWritable(Readable, Writable, Protocol):
    pass
```

### 2. Use Meaningful Names

```python
# Good
class Serializable(Protocol):
    def to_json(self) -> str: ...

# Bad
class X(Protocol):
    def f(self) -> str: ...
```

### 3. Document Expected Behavior

```python
class Comparable(Protocol):
    """Objects that can be compared for ordering.
    
    Implementations must provide consistent ordering
    where a < b and b < c implies a < c.
    """
    def __lt__(self, other) -> bool:
        """Return True if self is less than other."""
        ...
```

---
