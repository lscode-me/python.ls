# Protocols and Interfaces - Quiz

Test your knowledge of Python protocols, duck typing, and abstract base classes.

---

## Question 1: Duck Typing

What is duck typing in Python?

A) A way to check if an object is a duck  
B) If an object has the required methods, it can be used regardless of its type  
C) A strict type checking system  
D) A method for converting types  

---

## Question 2: Iterator Protocol

Which two methods must a class implement to support the iterator protocol?

A) `__iter__()` and `__next__()`  
B) `__start__()` and `__stop__()`  
C) `__begin__()` and `__end__()`  
D) `__first__()` and `__last__()`  

---

## Question 3: Context Manager Protocol

What special methods define the context manager protocol?

A) `__open__()` and `__close__()`  
B) `__start__()` and `__finish__()`  
C) `__begin__()` and `__end__()`  
D) `__enter__()` and `__exit__()`  

---

## Question 4: Sequence Protocol

Which method is NOT part of the sequence protocol?

A) `__len__()`  
B) `__getitem__()`  
C) `__contains__()`  
D) `__append__()`  

---

## Question 5: Callable Protocol

How do you make a class instance callable like a function?

A) Inherit from the Function class  
B) Use the @callable decorator  
C) Define a `__call__()` method  
D) Define a `__invoke__()` method  

---

## Question 6: typing.Protocol

What is the advantage of `typing.Protocol` over ABC?

A) It's faster at runtime  
B) It enables structural subtyping without explicit inheritance  
C) It works with older Python versions  
D) It automatically implements methods  

---

## Question 7: Abstract Base Classes

What module provides abstract base classes in Python?

A) `abc`  
B) `abstract`  
C) `interfaces`  
D) `protocols`  

---

## Question 8: StopIteration

When should an iterator raise `StopIteration`?

A) When an error occurs  
B) When the iterator is created  
C) When there are no more items to return  
D) Never, Python handles this automatically  

---

## Question 9: Descriptor Protocol

Which method is called when you access a descriptor attribute?

A) `__access__()`  
B) `__read__()`  
C) `__fetch__()`  
D) `__get__()`  

---

## Question 10: Collections ABC

Which collections.abc class represents a read-only sequence?

A) `Sequence`  
B) `Iterable`  
C) `MutableSequence`  
D) `Container`  

---

## Answer Key

1. B - If an object has the required methods, it can be used regardless of its type
2. A - `__iter__()` and `__next__()`
3. D - `__enter__()` and `__exit__()`
4. D - `__append__()`
5. C - Define a `__call__()` method
6. B - It enables structural subtyping without explicit inheritance
7. A - `abc`
8. C - When there are no more items to return
9. D - `__get__()`
10. A - `Sequence`

---

## Scoring Guide

- **9-10 correct**: Outstanding! You understand Python's protocol system deeply.
- **7-8 correct**: Very good! You grasp the core protocol concepts.
- **5-6 correct**: Fair understanding. Review protocol implementations.
- **Below 5**: Study the protocol materials more carefully. These are advanced but important concepts.
