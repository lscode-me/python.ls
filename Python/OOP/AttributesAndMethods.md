# Week 1 — Python Core Foundations (Lecture 1)
## Attributes and Methods

---

## 1. What are Attributes?

Attributes are variables attached to an object.

Every Python object can have attributes that store data or references to other objects.

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

## 2. What are Methods?

Methods are functions attached to an object.

They can access and modify the object's state through attributes.

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

## 3. Instance Attributes vs Class Attributes

### Instance Attributes
Unique to each object instance. Defined in `__init__` or added later.

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
Shared by all instances of the class. Defined at class level.

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

## 4. Attribute Lookup Order

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

## 5. Modifying Class Attributes

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

## 6. Instance Methods, Class Methods, Static Methods

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

## 7. Special Methods (Magic Methods)

Special methods start and end with double underscores `__`.

They define how objects behave with built-in operations.

### `__init__`: Constructor
Called when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
```

### `__str__`: String Representation
Called by `print()` and `str()`.

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person({self.name})"

p = Person("Alice")
print(p)    # Person(Alice)
```

### `__repr__`: Developer Representation
Called by `repr()` and in the interactive shell.

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person(name='{self.name}')"

p = Person("Alice")
print(repr(p))    # Person(name='Alice')
```

---

## 8. Attribute Access Methods

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

## 9. Built-in Functions for Attributes

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

## 10. Property Decorators

Properties provide controlled access to attributes.

They allow you to add logic when getting, setting, or deleting attributes.

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

## 11. The `__dict__` Attribute

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

## 12. Private and Protected Attributes

Python uses naming conventions to indicate attribute visibility.

### Public attributes
No prefix. Can be accessed from anywhere.

```python
class Person:
    def __init__(self, name):
        self.name = name    # public
```

### Protected attributes
Single underscore prefix `_`. Convention: "don't use outside the class".

```python
class Person:
    def __init__(self, name):
        self._internal_id = 12345    # protected
```

### Private attributes
Double underscore prefix `__`. Name mangling applied.

```python
class Person:
    def __init__(self, name):
        self.__secret = "password"    # private

p = Person("Alice")
# print(p.__secret)    # AttributeError
print(p._Person__secret)    # password (name mangling)
```

Name mangling transforms `__secret` to `_ClassName__secret` to avoid conflicts in inheritance.

---
