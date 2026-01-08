# Object-Oriented Programming - Quiz

Test your knowledge of classes, inheritance, polymorphism, and advanced OOP concepts.

---

## Basic Concepts (Questions 1-10)

### Question 1: Classes and Objects

What is the relationship between a class and an object?

A) A class is a special type of object  
B) A class is a blueprint, an object is an instance of that class  
C) Objects and classes are the same thing  
D) An object defines the structure, a class uses it  

---

### Question 2: The `__init__` Method

What is the purpose of the `__init__` method?

A) It deletes an object when it's no longer needed  
B) It's called when an object is created to initialize its attributes  
C) It's used to compare two objects for equality  
D) It converts an object to a string  

---

### Question 3: Instance vs Class Attributes

What is the main difference between class attributes and instance attributes?

A) Class attributes are private, instance attributes are public  
B) Class attributes are shared by all instances, instance attributes are unique to each instance  
C) Class attributes cannot be modified, instance attributes can be changed  
D) There is no difference, they are the same thing  

---

### Question 4: Attribute Lookup Order

In what order does Python search for attributes?

A) Class attributes → Instance attributes → Parent class attributes  
B) Parent class attributes → Class attributes → Instance attributes  
C) Instance attributes → Class attributes → Parent class attributes  
D) Randomly searches all available attributes  

---

### Question 5: Instance Methods

What is the purpose of the `self` parameter in instance methods?

A) It's optional and can be omitted  
B) It refers to the class itself  
C) It refers to the instance calling the method  
D) It's used for static methods only  

---

### Question 6: Class Methods

Which decorator is used to define a class method in Python?

A) @staticmethod  
B) @classmethod  
C) @property  
D) @abstractmethod  

---

### Question 7: Static Methods

What is true about static methods?

A) They must have `self` as first parameter  
B) They must have `cls` as first parameter  
C) They don't access instance or class data  
D) They can only be called on instances  

---

### Question 8: Inheritance

What does inheritance allow you to do?

A) Create multiple instances of a class  
B) Create new classes based on existing ones  
C) Access private attributes from outside the class  
D) Define methods without implementation  

---

### Question 9: Method Overriding

What is method overriding?

A) Calling a parent method multiple times  
B) Defining multiple methods with the same name but different parameters  
C) A child class providing a new implementation of a parent class method  
D) Preventing a method from being called  

---

### Question 10: The `super()` Function

What does `super()` do?

A) Creates a superclass from a subclass  
B) Allows you to call methods from the parent class  
C) Makes a class inherit from multiple parents  
D) Creates a singleton instance  

---

## Intermediate Concepts (Questions 11-20)

### Question 11: Multiple Inheritance

In multiple inheritance, which order does Python use to search for methods?

A) Method Resolution Order (MRO) using C3 linearization  
B) Random order  
C) Alphabetical order of parent classes  
D) Always left to right  

---

### Question 12: Polymorphism

What is polymorphism in OOP?

A) The ability to create multiple constructors  
B) The ability of different classes to be treated through a common interface  
C) The ability to inherit from multiple parent classes  
D) The ability to change object types at runtime  

---

### Question 13: Encapsulation - Protected Attributes

What does a single underscore prefix `_` indicate?

A) The attribute is truly private and inaccessible  
B) It's a convention suggesting "internal use only"  
C) The attribute is automatically encrypted  
D) It's required for all instance attributes  

---

### Question 14: Encapsulation - Private Attributes

How does Python indicate that an attribute should be treated as private with name mangling?

A) By prefixing the name with double underscores `__`  
B) By using the `private` keyword  
C) By prefixing the name with a single underscore `_`  
D) By declaring it in a `__slots__` tuple  

---

### Question 15: Properties

What does the `@property` decorator do?

A) Makes an attribute private  
B) Allows a method to be accessed like an attribute  
C) Prevents attribute modification  
D) Creates a class-level attribute  

---

### Question 16: Property Setters

Which decorator is used to create a setter for a property?

A) @property.set  
B) @setter  
C) @<property_name>.setter  
D) @set_property  

---

### Question 17: Special Methods - `__str__` vs `__repr__`

What's the difference between `__str__` and `__repr__`?

A) They are exactly the same  
B) `__str__` is for end users, `__repr__` is for developers/debugging  
C) `__str__` is for numbers, `__repr__` is for strings  
D) `__repr__` is called by `print()`, `__str__` is called by `repr()`  

---

### Question 18: Special Methods - Comparison

Which special method is called when using the `==` operator?

A) `__equal__()`  
B) `__equals__()`  
C) `__eq__()`  
D) `__compare__()`  

---

### Question 19: Composition vs Inheritance

When should you prefer composition over inheritance?

A) Never, inheritance is always better  
B) When you want a "has-a" relationship and more flexibility  
C) Only when using abstract classes  
D) When you need to access parent methods  

---

### Question 20: Modules vs Classes

What is the main difference between using modules and classes for organizing code?

A) Modules are faster than classes  
B) Modules organize related functions/classes, classes create objects with state  
C) Classes can't contain functions  
D) Modules can only contain one class  

---

## Advanced Concepts (Questions 21-35)

### Question 21: Callable Objects

How do you make a class instance callable like a function?

A) Define the `__call__` method  
B) Use the `@callable` decorator  
C) Inherit from `CallableObject`  
D) Define a `call()` method  

---

### Question 22: Built-in Functions for Attributes

Which function checks if an object has a specific attribute?

A) `checkattr()`  
B) `hasattr()`  
C) `isattr()`  
D) `findattr()`  

---

### Question 23: The `__dict__` Attribute

What does the `__dict__` attribute contain?

A) All methods of the class  
B) The instance's attributes as a dictionary  
C) The class hierarchy  
D) Special methods only  

---

### Question 24: Attribute Access - `__getattr__`

When is `__getattr__` called?

A) Every time an attribute is accessed  
B) Only when an attribute is not found through normal lookup  
C) When deleting an attribute  
D) When setting an attribute  

---

### Question 25: Abstract Base Classes

What happens if you try to instantiate an abstract class that has abstract methods?

A) Python creates the instance but the abstract methods return None  
B) Python creates the instance but warns about missing implementations  
C) The abstract methods are automatically implemented with default behavior  
D) Python raises a TypeError  

---

### Question 26: Abstract Methods

Which module provides the tools for creating abstract base classes?

A) `abstract`  
B) `abc`  
C) `base_classes`  
D) `interfaces`  

---

### Question 27: Decorators in OOP

What is a decorator?

A) A special type of inheritance  
B) A function that modifies or enhances another function or class  
C) A way to make attributes private  
D) A method for creating properties  

---

### Question 28: Class Decorators

What can a class decorator do?

A) Only change instance methods  
B) Modify the entire class definition  
C) Only work with properties  
D) Prevent class instantiation  

---

### Question 29: Dataclasses

What is the main advantage of using `@dataclass` decorator?

A) It makes the class run faster  
B) It automatically generates special methods like `__init__`, `__repr__`, and `__eq__`  
C) It prevents the class from being inherited  
D) It makes all attributes immutable  

---

### Question 30: Named Tuples

What is a characteristic of named tuples?

A) They are mutable data structures  
B) They are immutable and can be accessed by name or index  
C) They can only store strings  
D) They are slower than regular classes  

---

### Question 31: Slots

What is the purpose of `__slots__` in a class definition?

A) To define which methods are available  
B) To create a fixed number of instances  
C) To restrict memory usage by preventing dynamic attribute creation  
D) To define the order of method execution  

---

### Question 32: Descriptors

What special methods define a descriptor protocol?

A) `__init__`, `__str__`, `__repr__`  
B) `__get__`, `__set__`, `__delete__`  
C) `__enter__`, `__exit__`  
D) `__call__`, `__new__`  

---

### Question 33: Context Managers

Which special methods are needed to implement a context manager?

A) `__open__` and `__close__`  
B) `__start__` and `__stop__`  
C) `__enter__` and `__exit__`  
D) `__begin__` and `__end__`  

---

### Question 34: Mixins

What is a mixin class?

A) A class that can't be instantiated  
B) A class that provides specific functionality through multiple inheritance  
C) A class that mixes different data types  
D) A class with only private methods  

---

### Question 35: Protocols

What is a Protocol in Python's typing system?

A) A class that must be inherited explicitly  
B) An interface defined by structure (duck typing) without explicit inheritance  
C) A special type of abstract class  
D) A module-level configuration  

---

## Expert Level (Questions 36-40)

### Question 36: Metaclasses

What is a metaclass?

A) A class that inherits from multiple parents  
B) A class that controls the creation of other classes  
C) An abstract class with only static methods  
D) A class that can't be instantiated  

---

### Question 37: Operator Overloading

Which method would you override to customize the `+` operator?

A) `__plus__()`  
B) `__sum__()`  
C) `__add__()`  
D) `__addition__()`  

---

### Question 38: Context Manager Decorator

Which decorator from `contextlib` allows you to create a context manager from a generator?

A) `@context`  
B) `@contextmanager`  
C) `@with_context`  
D) `@manager`  

---

### Question 39: Method Resolution Order

Which method returns the MRO of a class?

A) `Class.mro()`  
B) `Class.__mro__`  
C) Both A and B  
D) `Class.get_mro()`  

---

### Question 40: Factory Pattern

What is the main purpose of the Factory pattern?

A) To create objects without specifying their exact classes  
B) To prevent object creation  
C) To copy existing objects  
D) To destroy objects when no longer needed  

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | A class is a blueprint, an object is an instance of that class |
| 2 | A | It's called when an object is created to initialize its attributes |
| 3 | D | Class attributes are shared by all instances, instance attributes are unique |
| 4 | B | Instance attributes → Class attributes → Parent class attributes |
| 5 | B | It refers to the instance calling the method |
| 6 | A | @classmethod |
| 7 | A | They don't access instance or class data |
| 8 | D | Create new classes based on existing ones |
| 9 | B | A child class providing a new implementation of a parent class method |
| 10 | B | Allows you to call methods from the parent class |
| 11 | A | Method Resolution Order (MRO) using C3 linearization |
| 12 | A | The ability of different classes to be treated through a common interface |
| 13 | C | It's a convention suggesting "internal use only" |
| 14 | D | By prefixing the name with double underscores `__` |
| 15 | C | Allows a method to be accessed like an attribute |
| 16 | D | @<property_name>.setter |
| 17 | B | `__str__` is for end users, `__repr__` is for developers/debugging |
| 18 | B | `__eq__()` |
| 19 | B | When you want a "has-a" relationship and more flexibility |
| 20 | A | Modules organize related functions/classes, classes create objects with state |
| 21 | C | Define the `__call__` method |
| 22 | C | `hasattr()` |
| 23 | B | The instance's attributes as a dictionary |
| 24 | D | Only when an attribute is not found through normal lookup |
| 25 | D | Python raises a TypeError |
| 26 | C | `abc` |
| 27 | C | A function that modifies or enhances another function or class |
| 28 | C | Modify the entire class definition |
| 29 | C | It automatically generates special methods like `__init__`, `__repr__`, `__eq__` |
| 30 | B | They are immutable and can be accessed by name or index |
| 31 | D | To restrict memory usage by preventing dynamic attribute creation |
| 32 | A | `__get__`, `__set__`, `__delete__` |
| 33 | A | `__enter__` and `__exit__` |
| 34 | D | A class that provides specific functionality through multiple inheritance |
| 35 | B | An interface defined by structure (duck typing) without explicit inheritance |
| 36 | C | A class that controls the creation of other classes |
| 37 | C | `__add__()` |
| 38 | A | @contextmanager |
| 39 | A | Both A and B |
| 40 | D | To create objects without specifying their exact classes |

---

## Scoring Guide

- **38-40 correct**: Outstanding! You're an OOP expert and master of Python's object model.
- **34-37 correct**: Excellent! You have deep understanding of OOP and advanced concepts.
- **30-33 correct**: Very Good! Strong grasp of OOP with room for advanced topics.
- **26-29 correct**: Good understanding! Review advanced concepts like descriptors and metaclasses.
- **20-25 correct**: Fair grasp of OOP. Focus on intermediate and advanced topics.
- **15-19 correct**: Basic understanding. Review inheritance, polymorphism, and special methods.
- **Below 15**: Study the OOP materials more carefully. Start with basic concepts and practice.

---

## Topics by Section

### Basic (1-10)
- Classes and objects
- Constructor (`__init__`)
- Instance vs class attributes
- Attribute lookup order
- Instance, class, and static methods
- Inheritance and method overriding
- `super()` function

### Intermediate (11-20)
- Multiple inheritance and MRO
- Polymorphism
- Encapsulation (public, protected, private)
- Properties and setters
- Special methods (`__str__`, `__repr__`, `__eq__`)
- Composition vs inheritance
- Modules vs classes

### Advanced (21-35)
- Callable objects (`__call__`)
- Built-in attribute functions
- `__dict__` and attribute access methods
- Abstract base classes
- Decorators (function and class)
- Dataclasses and named tuples
- `__slots__` for memory optimization
- Descriptors
- Context managers
- Mixins and protocols

### Expert (36-40)
- Metaclasses
- Operator overloading
- Advanced context managers
- Method resolution order (MRO)
- Design patterns (Factory)

---
