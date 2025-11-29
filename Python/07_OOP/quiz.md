# Object-Oriented Programming - Quiz

Test your knowledge of classes, inheritance, polymorphism, and advanced OOP concepts.

---

## Question 1: Class vs Instance Attributes

What is the main difference between class attributes and instance attributes?

A) Class attributes are private, instance attributes are public  
B) Class attributes are shared by all instances, instance attributes are unique to each instance  
C) Class attributes cannot be modified, instance attributes can be changed  
D) There is no difference, they are the same thing  

---

## Question 2: Method Types

Which decorator is used to define a class method in Python?

A) @staticmethod  
B) @classmethod  
C) @property  
D) @abstractmethod  

---

## Question 3: Inheritance

In multiple inheritance, which order does Python use to search for methods?

A) Method Resolution Order (MRO) using C3 linearization  
B) Random order  
C) Alphabetical order of parent classes  
D) Always left to right  

---

## Question 4: Special Methods

What special method is called when you use the `len()` function on an object?

A) `__length__()`  
B) `__size__()`  
C) `__len__()`  
D) `__count__()`  

---

## Question 5: Property Decorator

What does the `@property` decorator do?

A) Makes an attribute private  
B) Allows a method to be accessed like an attribute  
C) Prevents attribute modification  
D) Creates a class-level attribute  

---

## Question 6: Abstract Base Classes

What happens if you try to instantiate an abstract class that has abstract methods?

A) Python creates the instance but the abstract methods return None  
B) Python creates the instance but warns about missing implementations  
C) The abstract methods are automatically implemented with default behavior  
D) Python raises a TypeError  

---

## Question 7: Encapsulation

How does Python indicate that an attribute should be treated as private?

A) By prefixing the name with double underscores `__`  
B) By using the `private` keyword  
C) By prefixing the name with a single underscore `_`  
D) Python doesn't support private attributes  

---

## Question 8: Polymorphism

What is polymorphism in OOP?

A) The ability to create multiple constructors  
B) The ability of different classes to be treated through a common interface  
C) The ability to inherit from multiple parent classes  
D) The ability to change object types at runtime  

---

## Question 9: Dataclasses

What is the main advantage of using `@dataclass` decorator?

A) It makes the class run faster  
B) It automatically generates special methods like `__init__`, `__repr__`, and `__eq__`  
C) It prevents the class from being inherited  
D) It makes all attributes immutable  

---

## Question 10: Slots

What is the purpose of `__slots__` in a class definition?

A) To define which methods are available  
B) To create a fixed number of instances  
C) To restrict memory usage by preventing dynamic attribute creation  
D) To define the order of method execution

## Answer Key

1. B - Class attributes are shared by all instances, instance attributes are unique to each instance
2. B - @classmethod
3. A - Method Resolution Order (MRO) using C3 linearization
4. C - `__len__()`
5. B - Allows a method to be accessed like an attribute
6. D - Python raises a TypeError
7. A - By prefixing the name with double underscores `__`
8. B - The ability of different classes to be treated through a common interface
9. B - It automatically generates special methods like `__init__`, `__repr__`, and `__eq__`
10. C - To restrict memory usage by preventing dynamic attribute creation

---

## Scoring Guide

- **9-10 correct**: Excellent! You're an OOP master.
- **7-8 correct**: Good understanding! Review advanced topics.
- **5-6 correct**: Fair grasp of OOP. Practice more with classes.
- **Below 5**: Study the OOP materials more carefully. These concepts are fundamental.
