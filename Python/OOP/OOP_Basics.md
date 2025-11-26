# Week 2 — Object-Oriented Programming (Lecture 2)
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

## 4. Instance vs Class Variables

### Instance Variables
Unique to each instance. Defined with `self`.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand      # instance variable
        self.model = model      # instance variable

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.brand)    # Toyota
print(car2.brand)    # Honda
```

### Class Variables
Shared across all instances. Defined at class level.

```python
class Car:
    wheels = 4              # class variable
    
    def __init__(self, brand):
        self.brand = brand  # instance variable

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.wheels)    # 4
print(car2.wheels)    # 4
print(Car.wheels)     # 4
```

---

## 5. Inheritance

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

## 6. Method Overriding

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

## 7. The `super()` Function

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

## 8. Multiple Inheritance

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

## 9. Polymorphism

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

## 10. Encapsulation and Access Control

Python uses naming conventions to indicate access levels.

### Public Attributes
No prefix. Accessible from anywhere.

```python
class Person:
    def __init__(self, name):
        self.name = name    # public
```

### Protected Attributes
Single underscore `_`. Convention: "internal use only".

```python
class Person:
    def __init__(self, name):
        self._id = 12345    # protected
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

---

## 11. Properties and Getters/Setters

Properties provide controlled access to attributes.

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

---

## 12. Abstract Classes

Abstract classes cannot be instantiated and are meant to be inherited.

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

---

## 13. Composition vs Inheritance

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

## 14. Special Methods for OOP

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
