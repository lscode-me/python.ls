# Iteration Protocol - Quiz

Test your knowledge of iterators, generators, and efficient data processing.

---

## Question 1: Iterator vs Iterable

What is the key difference between an iterable and an iterator?

A) There is no difference  
B) An iterable has `__iter__()`, an iterator has both `__iter__()` and `__next__()`  
C) Iterables are faster than iterators  
D) Iterators require more memory than iterables  

---

## Question 2: Multiple Iteration

What happens when you try to iterate over an iterator twice?

```python
it = iter([1, 2, 3])
list(it)  # First iteration
list(it)  # Second iteration
```

A) Both return `[1, 2, 3]`  
B) First returns `[1, 2, 3]`, second returns `[]`  
C) Second iteration raises `StopIteration`  
D) Second iteration raises `TypeError`  

---

## Question 3: Custom Iterator

What's missing in this iterator implementation?

```python
class Counter:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    
    def __next__(self):
        if self.current >= self.max_value:
            raise StopIteration
        self.current += 1
        return self.current
```

A) Nothing, it's complete  
B) Missing `__iter__()` method  
C) Missing `__len__()` method  
D) Missing `__getitem__()` method  

---

## Question 4: iter() with Sentinel

What does `iter(callable, sentinel)` do?

```python
with open('data.txt') as f:
    for line in iter(f.readline, ''):
        print(line)
```

A) Calls `callable` until it returns `sentinel`, then stops  
B) Calls `callable` once with `sentinel` as argument  
C) Raises an error - invalid syntax  
D) Creates an infinite iterator  

---

## Question 5: next() with Default

What does this code return?

```python
it = iter([1, 2])
next(it)  # 1
next(it)  # 2
next(it, 'END')
```

A) Raises `StopIteration`  
B) Returns `None`  
C) Returns `'END'`  
D) Returns `0`  

---

## Question 6: Generator Expression

Which of the following creates a generator expression?

A) `(x**2 for x in range(10))`  
B) `[x**2 for x in range(10)]`  
C) `{x**2 for x in range(10)}`  
D) `list(x**2 for x in range(10))`  

---

## Question 7: Yield Statement

What happens when a generator function encounters a `yield` statement?

A) The function terminates  
B) The function raises an exception  
C) The function continues without interruption  
D) The function pauses and returns a value, saving its state  

---

## Question 8: Generator State

What does this generator produce?

```python
def gen():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

g = gen()
next(g)
next(g)
```

What is the second `next()` call's return value?

A) `1`  
B) `2`  
C) `3`  
D) Raises `StopIteration`  

---

## Question 9: Generator.send()

What does the `send()` method do with a generator?

A) Terminates the generator  
B) Creates a new generator  
C) Sends a value into the generator that becomes the result of the current yield expression  
D) Sends the generator to another function  

---

## Question 10: send() Example

What does this code print?

```python
def echo():
    while True:
        x = yield
        print(f"Received: {x}")

g = echo()
next(g)  # Prime the generator
g.send(42)
```

A) `42`  
B) `Received: 42`  
C) `Received: None`  
D) Nothing  

---

## Question 11: yield from

What does `yield from` do?

A) Creates multiple generators  
B) Yields values in reverse order  
C) Combines multiple yield statements  
D) Delegates to a sub-iterator and yields all its values  

---

## Question 12: yield from Example

What does this generator yield?

```python
def combined():
    yield from [1, 2]
    yield from [3, 4]

list(combined())
```

A) `[[1, 2], [3, 4]]`  
B) `[1, 2, 3, 4]`  
C) `[(1, 2), (3, 4)]`  
D) `[2, 4]`  

---

## Question 13: itertools.chain

What does `list(itertools.chain([1, 2], [3, 4]))` return?

A) `[[1, 2], [3, 4]]`  
B) `[1, 2, 3, 4]`  
C) `[(1, 3), (2, 4)]`  
D) A chain object  

---

## Question 14: itertools.islice

What does `list(itertools.islice(range(100), 5, 10))` return?

A) `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`  
B) `[5, 10]`  
C) `[5, 6, 7, 8, 9]`  
D) `[5, 15, 25, 35, 45]`  

---

## Question 15: itertools.islice with Step

What does `list(itertools.islice(range(20), 0, 10, 2))` return?

A) `[0, 2, 4, 6, 8]`  
B) `[0, 2, 4, 6, 8, 10]`  
C) `[2, 4, 6, 8, 10]`  
D) `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`  

---

## Question 16: itertools.cycle

What happens with this code?

```python
import itertools
counter = 0
for item in itertools.cycle([1, 2, 3]):
    counter += 1
    if counter > 5:
        break
    print(item)
```

A) Prints: `1 2 3`  
B) Prints: `1 2 3 1 2`  
C) Prints: `1 2 3 1 2 3`  
D) Infinite loop with no output  

---

## Question 17: itertools.count

What does `list(itertools.islice(itertools.count(10, 2), 5))` return?

A) `[10, 11, 12, 13, 14]`  
B) `[10, 12, 14, 16, 18]`  
C) `[2, 4, 6, 8, 10]`  
D) `[0, 2, 4, 6, 8]`  

---

## Question 18: itertools.repeat

What does `list(itertools.repeat('x', 3))` return?

A) `['x', 'xx', 'xxx']`  
B) `['x', 'x', 'x']`  
C) `'xxx'`  
D) `['xxx']`  

---

## Question 19: itertools.zip_longest

What does `list(itertools.zip_longest([1, 2], [3, 4, 5], fillvalue=0))` return?

A) `[(1, 3), (2, 4), (0, 5)]`  
B) `[(1, 3), (2, 4)]`  
C) `[(1, 3), (2, 4), (5,)]`  
D) Raises `ValueError`  

---

## Question 20: itertools.takewhile

What does this return?

```python
import itertools
list(itertools.takewhile(lambda x: x < 5, [1, 2, 3, 6, 4, 7]))
```

A) `[1, 2, 3, 4]`  
B) `[1, 2, 3]`  
C) `[1, 2, 3, 4, 7]`  
D) `[6, 7]`  

---

## Question 21: itertools.dropwhile

What does this return?

```python
import itertools
list(itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 6, 4, 7]))
```

A) `[1, 2, 3, 4]`  
B) `[6, 7]`  
C) `[6, 4, 7]`  
D) `[4, 7]`  

---

## Question 22: itertools.groupby

What does `itertools.groupby()` require for correct grouping?

A) The input must be a list  
B) The input must be sorted by the key function  
C) The input must contain unique values  
D) No special requirements  

---

## Question 23: itertools.product

What does `list(itertools.product([1, 2], ['a', 'b']))` return?

A) `[(1, 'a'), (2, 'b')]`  
B) `[(1, 2), ('a', 'b')]`  
C) `[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]`  
D) `[1, 2, 'a', 'b']`  

---

## Question 24: Generator Memory

Why are generators memory-efficient?

A) They generate values on-the-fly instead of storing all values in memory  
B) They compress data automatically  
C) They use less CPU  
D) They cache results  

---

## Question 25: Generator vs List Performance

When is a generator expression preferred over a list comprehension?

A) When you need random access to elements  
B) When working with large datasets and you only need to iterate once  
C) When you need to sort the results  
D) When you need to access the length  

---

## Answer Key

1. **B** - An iterable has `__iter__()`, an iterator has both `__iter__()` and `__next__()`
2. **B** - First returns `[1, 2, 3]`, second returns `[]` (iterator is exhausted)
3. **B** - Missing `__iter__()` method (should return `self`)
4. **A** - Calls `callable` until it returns `sentinel`, then stops
5. **C** - Returns `'END'` (the default value provided to `next()`)
6. **A** - `(x**2 for x in range(10))` creates a generator expression
7. **D** - The function pauses and returns a value, saving its state
8. **B** - Returns `2` (generator remembers state)
9. **C** - Sends a value into the generator that becomes the result of the current yield expression
10. **B** - Prints `Received: 42`
11. **D** - Delegates to a sub-iterator and yields all its values
12. **B** - `[1, 2, 3, 4]`
13. **B** - `[1, 2, 3, 4]` (note: we wrapped with `list()` to get actual list)
14. **C** - `[5, 6, 7, 8, 9]`
15. **A** - `[0, 2, 4, 6, 8]` (start=0, stop=10, step=2)
16. **B** - Prints `1 2 3 1 2` (cycles through values)
17. **B** - `[10, 12, 14, 16, 18]` (start=10, step=2)
18. **B** - `['x', 'x', 'x']` (repeats value 3 times)
19. **A** - `[(1, 3), (2, 4), (0, 5)]` (fills missing values with 0)
20. **B** - `[1, 2, 3]` (stops when condition becomes false)
21. **C** - `[6, 4, 7]` (drops elements until condition becomes false, then yields rest)
22. **B** - The input must be sorted by the key function
23. **C** - `[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]` (cartesian product)
24. **A** - They generate values on-the-fly instead of storing all values in memory
25. **B** - When working with large datasets and you only need to iterate once

---

## Scoring Guide

- **23-25 correct**: Excellent! You're an iteration protocol master.
- **20-22 correct**: Very strong understanding! Minor details to review.
- **16-19 correct**: Good foundation. Practice with itertools and custom iterators.
- **12-15 correct**: Basic understanding. Review `__iter__()`, `__next__()`, and itertools.
- **Below 12**: Study the iteration protocol thoroughly. Implement custom iterators and practice with itertools.
