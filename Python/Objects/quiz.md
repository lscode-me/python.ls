# Objects, References, Memory, Types - Quiz

Test your knowledge of Python's object model, memory management, and core data types.

---

## Question 1: Object Identity

What does the `is` operator check in Python?

A) Whether two objects have the same value  
B) Whether two variables reference the same object in memory  
C) Whether two objects are of the same type  
D) Whether two objects are equal after type conversion  

---

## Question 2: Mutable vs Immutable

Which of the following data types is immutable in Python?

A) Tuple  
B) List  
C) Dictionary  
D) Set  

---

## Question 3: Reference Counting

What happens when an object's reference count reaches zero?

A) The object is frozen and cannot be modified  
B) Python raises a ReferenceError  
C) The object is marked for garbage collection  
D) The object is converted to None  

---

## Question 4: Default Arguments

What is the problem with this function definition?

```python
def append_to_list(element, target=[]):
    target.append(element)
    return target
```

A) Lists cannot be used as default arguments  
B) The function will raise a TypeError  
C) There is no problem with this code  
D) The default list is created once and shared between all calls  

---

## Question 5: Object Copying

What is the difference between shallow copy and deep copy?

A) Shallow copy is faster, deep copy is slower  
B) Shallow copy creates a new object but references nested objects; deep copy recursively copies everything  
C) Shallow copy only works with lists, deep copy works with all types  
D) There is no difference, they are synonyms  

---

## Question 6: Integer Caching

Why does `a is b` return True when `a = 256` and `b = 256`, but False when `a = 257` and `b = 257`?

A) Python caches small integers (-5 to 256) for optimization  
B) 257 is a prime number  
C) Large numbers are stored differently in memory  
D) This is undefined behavior and may vary  

---

## Question 7: String Interning

Which statement about string interning is correct?

A) All strings are automatically interned in Python  
B) String interning only works for strings shorter than 10 characters  
C) Only strings that look like identifiers are typically interned  
D) String interning was removed in Python 3  

---

## Question 8: Memory Management

What is the primary garbage collection mechanism in CPython?

A) Mark and sweep algorithm only  
B) Generational garbage collection only  
C) Manual memory management like in C  
D) Reference counting with cyclic garbage collector  

---

## Question 9: Object Attribute Access

What happens when you access a non-existent attribute of an object?

A) Python raises an AttributeError  
B) Python returns None  
C) Python returns an empty string  
D) Python creates the attribute with a default value  

---

## Question 10: Type Checking

Which function returns the actual type of an object?

A) isinstance()  
B) type()  
C) typeof()  
D) gettype()  

---

## Answer Key

1. B - Whether two variables reference the same object in memory
2. A - Tuple
3. C - The object is marked for garbage collection
4. D - The default list is created once and shared between all calls
5. B - Shallow copy creates a new object but references nested objects; deep copy recursively copies everything
6. A - Python caches small integers (-5 to 256) for optimization
7. C - Only strings that look like identifiers are typically interned
8. D - Reference counting with cyclic garbage collector
9. A - Python raises an AttributeError
10. B - type()

---

## Scoring Guide

- **9-10 correct**: Excellent! You have a strong understanding of Python's object model.
- **7-8 correct**: Good job! Review the topics you missed.
- **5-6 correct**: Fair understanding. Consider revisiting the lecture materials.
- **Below 5**: Keep studying! These fundamentals are crucial for Python mastery.
