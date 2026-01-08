# Objects, References, Memory, Types - Quiz

Test your knowledge of Python's object model, memory management, and core data types.

---

## Question 1: Object References

What happens in Python when you execute `a = 10` and then `b = a`?

A) The value 10 is copied from a to b  
B) Both a and b reference the same object in memory  
C) A new integer object is created for b  
D) Python raises an error because integers are immutable  

---

## Question 2: Everything is an Object

Which of the following statements is correct about Python?

A) Only custom classes create objects  
B) Everything in Python is an object, including integers, strings, lists, and functions  
C) Functions are not objects, only data structures are  
D) Only mutable types are objects  

---

## Question 3: Immutable Types

Which of the following is NOT an immutable type in Python?

A) tuple  
B) frozenset  
C) bytearray  
D) bytes  

---

## Question 4: Mutable Types

Which of the following data types is mutable?

A) str  
B) int  
C) dict  
D) tuple  

---

## Question 5: Reference Behavior

Given this code:
```python
x = [1, 2]
y = x
x.append(3)
```
What is the value of `y`?

A) `[1, 2]`  
B) `[1, 2, 3]`  
C) `None`  
D) Python raises an error  

---

## Question 6: Immutability

Given this code:
```python
a = "hello"
b = a
a += "!"
```
What is the value of `b`?

A) `"hello!"`  
B) `"hello"`  
C) `None`  
D) Python raises an error  

---

## Question 7: Identity vs Equality

What is the difference between `is` and `==` in Python?

A) `is` checks value equality, `==` checks identity  
B) `is` checks identity (same object), `==` checks value equality  
C) They are the same  
D) `is` is faster but less accurate than `==`  

---

## Question 8: Integer Caching

Why does `a is b` return True when `a = 256` and `b = 256`?

A) All integers are cached  
B) Python caches small integers (typically -5 to 256) for optimization  
C) It's a coincidence  
D) Integers are immutable  

---

## Question 9: Integer Caching Limits

What is likely to happen with this code?
```python
a, b = 257, 257
print(a is b)
```

A) Always True  
B) Always False  
C) May be True or False (not guaranteed)  
D) Python raises an error  

---

## Question 10: String Interning

Given this code:
```python
a, b = "hello", "hello"
print(a is b)
```
What is the expected output?

A) Always False  
B) Typically True (strings that look like identifiers are interned)  
C) Python raises an error  
D) Depends on string length only  

---

## Question 11: List Identity

What is the output of this code?
```python
a, b = [], []
print(a is b)
```

A) True  
B) False  
C) None  
D) Python raises an error  

---

## Question 12: Reference Counting

What is reference counting in CPython?

A) Counting how many times a function is called  
B) Tracking how many references point to an object  
C) Counting the number of objects in memory  
D) Measuring code execution time  

---

## Question 13: Object Deallocation

When does CPython deallocate an object?

A) When the program ends  
B) When the garbage collector runs  
C) Immediately when the reference count reaches 0  
D) Never, objects are kept in memory  

---

## Question 14: sys.getrefcount()

What does `sys.getrefcount(x)` return?

A) The memory address of x  
B) The number of references to x (note: calling this function adds a temporary reference)  
C) The size of x in bytes  
D) The type of x  

---

## Question 15: Mutable Default Arguments

What is the output after running this code twice?
```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
```

A) `[1]` then `[2]`  
B) `[1]` then `[1, 2]`  
C) `[1, 2]` then `[1, 2]`  
D) Python raises an error  

---

## Question 16: Fixing Mutable Defaults

What is the correct way to fix mutable default argument issues?

A) Use `lst=[]` and it will work correctly  
B) Use `lst=None` and create a new list inside the function if needed  
C) Use `lst=list()` instead  
D) Mutable defaults cannot be fixed  

---

## Question 17: type() Function

What does `type([1, 2, 3])` return?

A) `list`  
B) `<class 'list'>`  
C) `"list"`  
D) `3`  

---

## Question 18: id() Function

What does the `id()` function return?

A) The type of the object  
B) The identity (memory address in CPython) of the object  
C) The size of the object  
D) The reference count  

---

## Question 19: isinstance() Function

What does `isinstance("hello", str)` return?

A) `<class 'str'>`  
B) `True`  
C) `False`  
D) `"str"`  

---

## Question 20: callable() Function

Which of the following returns True when passed to `callable()`?

A) `42`  
B) `"hello"`  
C) `[1, 2, 3]`  
D) `lambda x: x + 1`  

---

## Question 21: sys.getsizeof()

What does `sys.getsizeof(obj)` return?

A) The size of the object in bytes (non-recursive)  
B) The total memory used by the program  
C) The reference count  
D) The deep size including all nested objects  

---

## Question 22: sys.getsizeof() for Containers

What does `sys.getsizeof([1, 2, 3])` measure?

A) The size of the list "shell" only, not the contained objects  
B) The total size including all integers  
C) The number of elements  
D) The reference count  

---

## Question 23: Garbage Collector

What does Python's garbage collector handle?

A) All memory deallocation  
B) Cyclic references that reference counting cannot handle  
C) Only large objects  
D) External resources like files  

---

## Question 24: gc.get_referrers()

What does `gc.get_referrers(obj)` return?

A) Objects that obj references  
B) Objects that reference obj  
C) The reference count  
D) The memory address  

---

## Question 25: gc.is_tracked()

Which objects are typically NOT tracked by Python's garbage collector?

A) Lists and dictionaries  
B) User-defined objects  
C) Most immutable objects like integers and strings  
D) All objects are tracked  

---

## Question 26: dir() Function

What does `dir(obj)` return?

A) The directory path of the module  
B) A list of attributes and methods of the object  
C) The size of the object  
D) The type of the object  

---

## Question 27: hash() Function

Which of the following objects is NOT hashable?

A) `(1, 2, 3)`  
B) `"hello"`  
C) `[1, 2, 3]`  
D) `42`  

---

## Question 28: repr() vs str()

What is the difference between `repr()` and `str()`?

A) They are identical  
B) `repr()` gives a detailed/debug representation, `str()` gives a user-friendly string  
C) `repr()` is faster  
D) `str()` only works with strings  

---

## Question 29: Type Constructors

What does `list("abc")` return?

A) `"abc"`  
B) `['abc']`  
C) `['a', 'b', 'c']`  
D) Python raises an error  

---

## Question 30: Memory Manager

What components are part of Python's memory management?

A) Only reference counting  
B) Only garbage collection  
C) Reference counting, garbage collector for cycles, and PyObject allocator  
D) Manual malloc/free like in C  

---

## Answer Key

1. B - Both a and b reference the same object in memory
2. B - Everything in Python is an object, including integers, strings, lists, and functions
3. C - bytearray (it is mutable)
4. C - dict
5. B - `[1, 2, 3]` (y references the same list as x)
6. B - `"hello"` (strings are immutable, so a += "!" creates a new string)
7. B - `is` checks identity (same object), `==` checks value equality
8. B - Python caches small integers (typically -5 to 256) for optimization
9. C - May be True or False (not guaranteed, depends on implementation)
10. B - Typically True (strings that look like identifiers are interned)
11. B - False (two different list objects)
12. B - Tracking how many references point to an object
13. C - Immediately when the reference count reaches 0
14. B - The number of references to x (note: calling this function adds a temporary reference)
15. B - `[1]` then `[1, 2]` (the default list is shared across calls)
16. B - Use `lst=None` and create a new list inside the function if needed
17. B - `<class 'list'>`
18. B - The identity (memory address in CPython) of the object
19. B - `True`
20. D - `lambda x: x + 1` (functions and lambdas are callable)
21. A - The size of the object in bytes (non-recursive)
22. A - The size of the list "shell" only, not the contained objects
23. B - Cyclic references that reference counting cannot handle
24. B - Objects that reference obj
25. C - Most immutable objects like integers and strings
26. B - A list of attributes and methods of the object
27. C - `[1, 2, 3]` (lists are mutable and therefore not hashable)
28. B - `repr()` gives a detailed/debug representation, `str()` gives a user-friendly string
29. C - `['a', 'b', 'c']`
30. C - Reference counting, garbage collector for cycles, and PyObject allocator

---

## Scoring Guide

- **27-30 correct**: Excellent! You have mastered Python's object model and memory management.
- **23-26 correct**: Very good! You have a strong understanding of the core concepts.
- **19-22 correct**: Good job! Review the topics you missed for deeper understanding.
- **15-18 correct**: Fair understanding. Consider revisiting the lecture materials.
- **10-14 correct**: Basic grasp. More practice with these fundamentals is recommended.
- **Below 10**: Keep studying! These fundamentals are crucial for Python mastery.
