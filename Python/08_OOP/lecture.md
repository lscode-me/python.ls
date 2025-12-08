# Object-Oriented Programming
## OOP Basics: Classes, Inheritance, Polymorphism

---

## 1. Introduction to Object-Oriented Programming

OOP is a programming paradigm based on the concept of "objects" that contain:
- **Data** (attributes)
- **Behavior** (methods)

### Key OOP Principles
1. **Encapsulation** - bundling data and methods together
2. **Inheritance** - creating new classes from existing ones
3. **Polymorphism** - same interface, different implementations
4. **Abstraction** - hiding complex implementation details

---

## 2. Classes and Objects

A **class** is a blueprint for creating objects.  
An **object** is an instance of a class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects
dog1 = Dog("Rex", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())    # Rex says Woof!
print(dog2.bark())    # Max says Woof!
```

---

## 3. The `__init__` Method (Constructor)

The `__init__` method is called automatically when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name        # instance attribute
        self.age = age          # instance attribute
        self.created = True     # default attribute
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person.introduce())    # Hi, I'm Alice, 30 years old
```

---

## 4. What are Attributes?

Attributes are variables attached to an object. They store data or references to other objects.

```python
class Person:
    pass

p = Person()
p.name = "Alice"    # create attribute 'name'
p.age = 30          # create attribute 'age'

print(p.name)       # Alice
print(p.age)        # 30
```

Attributes can be added dynamically in Python (for most objects).

---

## 5. What are Methods?

Methods are functions attached to an object. They can access and modify the object's state through attributes.

```python
class Person:
    def greet(self):
        return f"Hello, I'm {self.name}"

p = Person()
p.name = "Alice"
print(p.greet())    # Hello, I'm Alice
```

The first parameter `self` refers to the instance calling the method.

---

## 6. Instance vs Class Attributes

### Instance Attributes
Unique to each instance. Defined with `self` in `__init__` or added later.

```python
class Dog:
    def __init__(self, name):
        self.name = name    # instance attribute

dog1 = Dog("Rex")
dog2 = Dog("Max")

print(dog1.name)    # Rex
print(dog2.name)    # Max
```

### Class Attributes
Shared across all instances. Defined at class level.

```python
class Dog:
    species = "Canis familiaris"    # class attribute
    
    def __init__(self, name):
        self.name = name

dog1 = Dog("Rex")
dog2 = Dog("Max")

print(dog1.species)    # Canis familiaris
print(dog2.species)    # Canis familiaris
print(Dog.species)     # Canis familiaris
```

---

## 7. Attribute Lookup Order

Python searches for attributes in this order:

1. Instance attributes
2. Class attributes
3. Parent class attributes (inheritance)

```python
class Animal:
    category = "Living being"

class Dog(Animal):
    species = "Canis familiaris"
    
    def __init__(self, name):
        self.name = name

dog = Dog("Rex")

print(dog.name)      # 1. Found in instance
print(dog.species)   # 2. Found in class
print(dog.category)  # 3. Found in parent class
```

---

## 8. Modifying Class Attributes

Modifying a class attribute affects all instances (unless shadowed).

```python
class Counter:
    count = 0

c1 = Counter()
c2 = Counter()

print(c1.count, c2.count)    # 0 0

Counter.count = 5
print(c1.count, c2.count)    # 5 5
```

But assigning to an instance creates an instance attribute that shadows the class attribute.

```python
c1.count = 10
print(c1.count)              # 10 (instance attribute)
print(c2.count)              # 5  (class attribute)
print(Counter.count)         # 5  (class attribute)
```

---

## 9. Instance Methods, Class Methods, Static Methods

### Instance Methods
Access and modify instance state. Take `self` as first parameter.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())    # 78.5
```

### Class Methods
Work with class-level data. Take `cls` as first parameter. Decorated with `@classmethod`.

```python
class Circle:
    pi = 3.14159
    
    @classmethod
    def set_precision(cls, digits):
        if digits == 2:
            cls.pi = 3.14
        elif digits == 5:
            cls.pi = 3.14159

Circle.set_precision(2)
print(Circle.pi)    # 3.14
```

### Static Methods
Don't access instance or class data. No `self` or `cls` parameter. Decorated with `@staticmethod`.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.add(3, 5))       # 8
print(Math.multiply(4, 6))  # 24
```

---

## 10. Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())    # Rex barks
print(cat.speak())    # Whiskers meows
```

---

## 11. Method Overriding

Child classes can override methods from parent classes.

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

rect = Rectangle(5, 10)
circle = Circle(7)

print(rect.area())      # 50
print(circle.area())    # 153.86
```

---

## 12. The `super()` Function

`super()` allows you to call methods from the parent class.

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        return f"{self.brand}, {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def info(self):
        return f"{super().info()}, {self.doors} doors"

car = Car("Toyota", 2020, 4)
print(car.info())    # Toyota, 2020, 4 doors
```

---

## 13. Multiple Inheritance

Python supports multiple inheritance (inheriting from multiple parent classes).

```python
class Flyable:
    def fly(self):
        return "Flying in the sky"

class Swimmable:
    def swim(self):
        return "Swimming in water"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

duck = Duck("Donald")
print(duck.fly())     # Flying in the sky
print(duck.swim())    # Swimming in water
```

### Method Resolution Order (MRO)

Python uses C3 linearization to determine the order in which methods are resolved.

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())       # B
print(D.__mro__)        # Shows the method resolution order
```

---

## 14. Polymorphism

Polymorphism allows different classes to implement the same interface.

```python
class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

bird = Bird()
dog = Dog()
cat = Cat()

animal_sound(bird)    # Chirp
animal_sound(dog)     # Bark
animal_sound(cat)     # Meow
```

---

## 15. Encapsulation and Access Control

Python uses naming conventions to indicate access levels.

### Public Attributes
No prefix. Accessible from anywhere.

```python
class Person:
    def __init__(self, name):
        self.name = name    # public
```

### Protected Attributes
Single underscore `_`. Convention: "internal use only" or "don't use outside the class".

```python
class Person:
    def __init__(self, name):
        self._internal_id = 12345    # protected
```

### Private Attributes
Double underscore `__`. Name mangling applied.

```python
class Person:
    def __init__(self, name):
        self.__secret = "password"    # private

p = Person("Alice")
# print(p.__secret)            # AttributeError
print(p._Person__secret)       # password (name mangling)
```

Name mangling transforms `__secret` to `_ClassName__secret` to avoid conflicts in inheritance.

---

## 16. Properties and Getters/Setters

Properties provide controlled access to attributes. They allow you to add logic when getting, setting, or deleting attributes.

```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
    
    @property
    def name(self):
        return self._name

emp = Employee("Alice", 50000)
print(emp.salary)       # 50000

emp.salary = 60000
print(emp.salary)       # 60000

# emp.salary = -1000    # ValueError
```

### Example with Temperature Conversion

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)        # 25
print(t.fahrenheit)     # 77.0

t.celsius = 30
print(t.celsius)        # 30

# t.celsius = -300      # ValueError: Temperature below absolute zero
```

Properties make attributes look like regular attributes but with validation logic.

---

## 17. Special Methods (Magic Methods)

Special methods start and end with double underscores `__`. They define how objects behave with built-in operations.

### `__str__` and `__repr__`

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("1984", "George Orwell")
print(str(book))     # 1984 by George Orwell
print(repr(book))    # Book('1984', 'George Orwell')
```

### `__eq__` and `__lt__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1 == p2)    # False
print(p2 < p1)     # True
```

---

## 18. Composition vs Inheritance

**Composition**: "has-a" relationship  
**Inheritance**: "is-a" relationship

```python
# Inheritance: Car IS A Vehicle
class Vehicle:
    pass

class Car(Vehicle):
    pass

# Composition: Car HAS AN Engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start(self):
        return self.engine.start()

engine = Engine(200)
car = Car(engine)
print(car.start())    # Engine started
```

Prefer composition when you want flexibility and avoid deep inheritance hierarchies.

---

## 19. Modules vs Classes: Organizing Code in Namespaces

Both modules and classes provide namespaces for organizing code, but they serve different purposes.

### Modules as Namespaces

Modules are Python files that group related functions, classes, and variables.

```python
# math_utils.py
PI = 3.14159

def calculate_area(radius):
    return PI * radius ** 2

def calculate_circumference(radius):
    return 2 * PI * radius

class Circle:
    def __init__(self, radius):
        self.radius = radius
```

```python
# Usage
import math_utils

print(math_utils.PI)                          # 3.14159
print(math_utils.calculate_area(5))          # 78.53975
circle = math_utils.Circle(10)
```

### Classes as Namespaces

Classes group related data and behavior, creating instances with state.

```python
# Using a class to organize related constants and methods
class MathConstants:
    PI = 3.14159
    E = 2.71828
    GOLDEN_RATIO = 1.61803
    
    @staticmethod
    def circle_area(radius):
        return MathConstants.PI * radius ** 2

# Usage
print(MathConstants.PI)                       # 3.14159
print(MathConstants.circle_area(5))           # 78.53975
```

### When to Use Modules vs Classes

**Use Modules when:**
- Organizing related functions and constants
- No need for state or multiple instances
- Sharing utilities across the application
- Creating a library or API

```python
# config.py - module for configuration
DATABASE_URL = "postgresql://localhost/mydb"
DEBUG = True
MAX_CONNECTIONS = 100

def get_connection():
    # return database connection
    pass
```

**Use Classes when:**
- You need to maintain state
- Creating multiple instances with different data
- Implementing OOP principles (inheritance, polymorphism)
- Modeling real-world entities

```python
# Configuration as a class (when you need multiple configs)
class Config:
    def __init__(self, env="development"):
        self.env = env
        self.debug = env == "development"
        self.database_url = self._get_database_url()
    
    def _get_database_url(self):
        if self.env == "production":
            return "postgresql://prod-server/db"
        return "postgresql://localhost/dev-db"

dev_config = Config("development")
prod_config = Config("production")
```

### Hybrid Approach

Often, modules contain multiple classes and functions:

```python
# shapes.py module
PI = 3.14159

class Shape:
    """Base class for all shapes"""
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return PI * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def total_area(shapes):
    """Utility function to calculate total area of multiple shapes"""
    return sum(shape.area() for shape in shapes)
```

**Key Principle**: Use modules to organize code by topic/functionality, use classes to create objects with state and behavior.

---

## 20. Classes vs Functions: Callable Objects

Both classes and functions are callable in Python, but they serve different purposes.

### Functions as Callables

Functions are the simplest callable objects.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))    # Hello, Alice!
print(callable(greet))   # True
```

### Classes as Callable Factories

Classes are callable - calling them creates instances.

```python
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting
    
    def greet(self, name):
        return f"{self.greeting}, {name}!"

# Class is callable - creates instances
greeter = Greeter("Hello")
print(greeter.greet("Alice"))    # Hello, Alice!

print(callable(Greeter))         # True
print(callable(greeter))         # False (instance is not callable by default)
```

### Making Instances Callable with `__call__`

You can make class instances callable by defining `__call__` method.

```python
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting
    
    def __call__(self, name):
        return f"{self.greeting}, {name}!"

greeter = Greeter("Hello")
print(greeter("Alice"))          # Hello, Alice! (calling the instance)
print(callable(greeter))         # True
```

### When to Use Functions vs Classes

**Use Functions when:**
- Simple, stateless operations
- Single responsibility
- No need to maintain state between calls
- Functional programming style

```python
# Simple transformation - function is perfect
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
```

**Use Classes when:**
- Need to maintain state
- Complex behavior with multiple related methods
- Configuration or context needed
- Reusable, customizable behavior

```python
# Stateful operation - class is better
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.call_count = 0
    
    def __call__(self, x):
        self.call_count += 1
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))           # 10
print(triple(5))           # 15
print(double.call_count)   # 1
```

### Closures vs Classes

Closures (functions with state) can sometimes replace simple classes:

```python
# Using closure
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
print(double(5))    # 10

# Using class
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

triple = Multiplier(3)
print(triple(5))    # 15
```

**Closures are good for:**
- Simple state
- Single operation
- Functional style

**Classes are better for:**
- Multiple methods
- Complex state
- Inheritance
- Clear intent

### Practical Example: Validators

```python
# Function approach
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    return True

# Class approach (more flexible)
class RangeValidator:
    def __init__(self, min_value, max_value, field_name="value"):
        self.min_value = min_value
        self.max_value = max_value
        self.field_name = field_name
    
    def __call__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.field_name} must be a number")
        if value < self.min_value or value > self.max_value:
            raise ValueError(
                f"{self.field_name} must be between {self.min_value} and {self.max_value}"
            )
        return True

# Reusable validators
age_validator = RangeValidator(0, 150, "Age")
temperature_validator = RangeValidator(-273.15, 1000000, "Temperature")

age_validator(30)           # True
temperature_validator(25)   # True
```

### Decorators: Functions Returning Callables

Decorators often use this pattern - functions that return classes or closures:

```python
# Decorator returning a class instance
def repeat(times):
    class Repeater:
        def __init__(self, func):
            self.func = func
            self.times = times
        
        def __call__(self, *args, **kwargs):
            for _ in range(self.times):
                result = self.func(*args, **kwargs)
            return result
    
    return Repeater

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

**Key Principle**: Use functions for simple operations, classes when you need state, multiple methods, or want to leverage OOP features.

---

## 21. Built-in Functions for Attributes

### `hasattr()`: Check if attribute exists

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(hasattr(p, "name"))    # True
print(hasattr(p, "age"))     # False
```

### `getattr()`: Get attribute value (with optional default)

```python
p = Person("Alice")
print(getattr(p, "name"))           # Alice
print(getattr(p, "age", "N/A"))     # N/A (default)
```

### `setattr()`: Set attribute value

```python
p = Person("Alice")
setattr(p, "age", 30)
print(p.age)    # 30
```

### `delattr()`: Delete attribute

```python
p = Person("Alice")
p.age = 30
delattr(p, "age")
print(hasattr(p, "age"))    # False
```

---

## 22. The `__dict__` Attribute

Every object has a `__dict__` that stores its attributes as a dictionary.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.__dict__)    # {'name': 'Alice', 'age': 30}

p.city = "New York"
print(p.__dict__)    # {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

You can directly modify `__dict__`:

```python
p.__dict__["country"] = "USA"
print(p.country)    # USA
```

---

## 23. Attribute Access Methods

### `__getattr__`: Called when attribute is not found

```python
class Dynamic:
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

d = Dynamic()
print(d.anything)    # Attribute 'anything' not found
```

### `__setattr__`: Called when setting an attribute

```python
class Validated:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("Age cannot be negative")
        self.__dict__[name] = value

v = Validated()
v.age = 30     # OK
# v.age = -5   # ValueError: Age cannot be negative
```

### `__delattr__`: Called when deleting an attribute

```python
class Protected:
    def __delattr__(self, name):
        if name == "important":
            raise AttributeError("Cannot delete important attribute")
        del self.__dict__[name]

p = Protected()
p.temp = "value"
del p.temp    # OK
# del p.important   # AttributeError
```

---

## 24. Abstract Classes

Abstract classes cannot be instantiated and are meant to be inherited. They define interfaces that subclasses must implement.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
    def move(self):
        return "Run"

# animal = Animal()    # TypeError: Can't instantiate abstract class

dog = Dog()
print(dog.sound())     # Bark
print(dog.move())      # Run
```

### Advanced ABC Example

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

# Advanced OOP Concepts

---

## 25. Decorators in OOP

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

## 26. Class Decorators

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

## 27. Dataclasses

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

## 28. Named Tuples

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

## 29. Slots for Memory Optimization

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

## 30. Descriptors

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

## 31. Context Managers

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

## 32. Mixins

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

## 33. Protocols (Structural Subtyping)

Protocols define interfaces without explicit inheritance (duck typing with type checking).

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

---

## 34. Metaclasses

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

## 35. Operator Overloading

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

## 36. Composition Design Pattern

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

## 37. Factory Pattern

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
