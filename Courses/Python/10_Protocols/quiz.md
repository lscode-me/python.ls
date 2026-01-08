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

## Question 11: Hashable Protocol

What method must be implemented for an object to be hashable?

A) `__hash__()` only
B) `__hash__()` and `__eq__()`
C) `__id__()` and `__hash__()`
D) `__key__()` only

---

## Question 12: Comparison Protocol

Which methods are needed for full ordering comparison support?

A) Only `__eq__()`
B) `__lt__()` only with `@functools.total_ordering`
C) All of `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`, `__eq__()`
D) Both B and C can work

---

## Question 13: Mapping Protocol

Which method is NOT part of the mapping protocol?

A) `__getitem__()`
B) `__iter__()`
C) `__len__()`
D) `__append__()`

---

## Question 14: Runtime Checkable

What decorator makes a `typing.Protocol` checkable with `isinstance()`?

A) `@abstract`
B) `@runtime_checkable`
C) `@isinstance_enabled`
D) `@type_check`

---

## Question 15: Numeric Protocol

Which method is called for the `+` operator?

A) `__plus__()`
B) `__sum__()`
C) `__add__()`
D) `__concat__()`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Duck typing means objects are used based on their methods, not their type |
| 2 | C | `__iter__()` returns the iterator, `__next__()` returns next item |
| 3 | A | `__enter__()` and `__exit__()` define context manager behavior |
| 4 | C | `__append__()` is for mutable sequences, not the basic sequence protocol |
| 5 | D | Define `__call__()` method to make instances callable |
| 6 | D | Protocol enables structural subtyping without requiring inheritance |
| 7 | A | The `abc` module provides abstract base class functionality |
| 8 | C | `StopIteration` signals the iterator has no more items |
| 9 | B | `__get__()` is called when accessing a descriptor attribute |
| 10 | C | `Sequence` is read-only, `MutableSequence` allows modifications |
| 11 | B | Both `__hash__()` and `__eq__()` are needed for hashable objects |
| 12 | B | Either implement all comparison methods or use `@total_ordering` with `__lt__` and `__eq__` |
| 13 | B | `__append__()` is not part of mapping protocol, it's for sequences |
| 14 | A | `@runtime_checkable` enables `isinstance()` checks on Protocol classes |
| 15 | D | `__add__()` is called for the + operator |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **9-10 correct (90-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **7-8 correct (70-80%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **5-6 correct (50-60%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 5 correct (<50%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
