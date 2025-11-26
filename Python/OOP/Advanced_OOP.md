# Week 2 — Object-Oriented Programming (Lecture 2)
## Advanced OOP Concepts

---

## 1. Decorators in OOP

Decorators modify or enhance functions and methods.

### Function Decorators

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_call
def greet(name):
    return f"Hello, {name}"

greet("Alice")
# Output:
# Calling greet
# Finished greet
```

### Method Decorators

```python
class Logger:
    @staticmethod
    def log(message):
        print(f"[LOG] {message}")
    
    @classmethod
    def create_logger(cls, name):
        return cls()
    
    @property
    def timestamp(self):
        from datetime import datetime
        return datetime.now()
```

---

## 2. Class Decorators

Class decorators modify entire classes.

```python
def add_str_method(cls):
    def __str__(self):
        return f"{cls.__name__} instance"
    cls.__str__ = __str__
    return cls

@add_str_method
class MyClass:
    pass

obj = MyClass()
print(obj)    # MyClass instance
```

---

## 3. Dataclasses

Dataclasses reduce boilerplate code for classes that primarily store data.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grades: List[float] = field(default_factory=list)
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student = Student("Alice", 20, [85.5, 90.0, 88.5])
print(student)
print(f"Average: {student.average_grade()}")
```

Benefits:
- Automatic `__init__`, `__repr__`, `__eq__`
- Type hints
- Default values
- Immutable options with `frozen=True`

---

## 4. Named Tuples

Named tuples are lightweight, immutable data structures.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(p.x, p.y)        # 10 20
print(p[0], p[1])      # 10 20

# Immutable
# p.x = 15    # AttributeError
```

Modern alternative with type hints:

```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
    
    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(3.0, 4.0)
print(p.distance_from_origin())    # 5.0
```

---

## 5. Slots for Memory Optimization

`__slots__` restricts attributes and reduces memory usage.

```python
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Regular class uses more memory
import sys
regular = RegularClass(1, 2)
slotted = SlottedClass(1, 2)

print(sys.getsizeof(regular.__dict__))    # ~240 bytes
print(sys.getsizeof(slotted))             # ~64 bytes

# Slots prevent dynamic attribute creation
# slotted.z = 3    # AttributeError
```

Use slots when:
- Creating many instances
- Memory is a constraint
- You know all attributes in advance

---

## 6. Metaclasses

Metaclasses control class creation itself.

```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing database")

db1 = Database()
db2 = Database()

print(db1 is db2)    # True (same instance)
```

Common use cases:
- Singletons
- Registration of classes
- Validation of class structure
- Automatic method generation

---

## 7. Descriptors

Descriptors control attribute access at the class level.

```python
class Validator:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        obj.__dict__[self.name] = value

class Person:
    age = Validator(min_value=0, max_value=150)
    
    def __init__(self, age):
        self.age = age

person = Person(30)
print(person.age)    # 30

# person.age = 200   # ValueError: age must be <= 150
```

---

## 8. Context Managers

Context managers manage resources using `with` statement.

### Using `__enter__` and `__exit__`

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
        # Return False to propagate exceptions
        return False

with FileManager('test.txt', 'w') as f:
    f.write('Hello World')
```

### Using `contextlib`

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_manager('test.txt', 'w') as f:
    f.write('Hello World')
```

---

## 9. Mixins

Mixins add functionality to classes through multiple inheritance.

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class User(JSONMixin, LogMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(user.to_json())      # {"name": "Alice", "email": "alice@example.com"}
user.log("User created")   # [User] User created
```

Mixins should:
- Provide specific functionality
- Not have `__init__` (or be very careful)
- Be small and focused

---

## 10. Abstract Base Classes (ABC)

ABCs define interfaces that subclasses must implement.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund(self, transaction_id):
        pass
    
    def log_transaction(self, message):
        print(f"Transaction: {message}")

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
    
    def refund(self, transaction_id):
        return f"Refunding transaction {transaction_id}"

# processor = PaymentProcessor()    # TypeError: Can't instantiate abstract class

processor = CreditCardProcessor()
print(processor.process_payment(100))
processor.log_transaction("Payment completed")
```

---

## 11. Protocols (Structural Subtyping)

Protocols define interfaces without explicit inheritance.

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

circle = Circle()
square = Square()

render(circle)    # Drawing a circle
render(square)    # Drawing a square
```

Protocols enable duck typing with type checking.

---

## 12. Operator Overloading

Special methods allow custom behavior for operators.

```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, scalar):
        return Money(self.amount * scalar, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount < other.amount
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

m1 = Money(100)
m2 = Money(50)

print(m1 + m2)    # Money(150, 'USD')
print(m1 - m2)    # Money(50, 'USD')
print(m1 * 2)     # Money(200, 'USD')
print(m1 > m2)    # True
```

---

## 13. Composition Design Pattern

Prefer composition over inheritance for flexibility.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower}hp started"

class Transmission:
    def __init__(self, gear_type):
        self.gear_type = gear_type
    
    def shift(self, gear):
        return f"Shifting {self.gear_type} to gear {gear}"

class Car:
    def __init__(self, engine, transmission):
        self.engine = engine
        self.transmission = transmission
    
    def start(self):
        return self.engine.start()
    
    def drive(self):
        return f"{self.start()}\n{self.transmission.shift(1)}"

engine = Engine(200)
transmission = Transmission("automatic")
car = Car(engine, transmission)

print(car.drive())
```

---

## 14. Factory Pattern

Factory pattern creates objects without specifying exact classes.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")

print(dog.speak())    # Woof!
print(cat.speak())    # Meow!
```

---
