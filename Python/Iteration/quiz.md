# Iteration Protocol - Quiz

Test your knowledge of iterators, generators, and efficient data processing.

---

## Question 1: Iterator vs Iterable

What is the difference between an iterable and an iterator?

A) There is no difference  
B) An iterable can be iterated over; an iterator keeps track of the current position  
C) Iterables are faster than iterators  
D) Iterators can only be used once, iterables can be reused  

**Correct Answer: B**

---

## Question 2: Generator Expression

Which of the following creates a generator expression?

A) `[x**2 for x in range(10)]`  
B) `{x**2 for x in range(10)}`  
C) `(x**2 for x in range(10))`  
D) `list(x**2 for x in range(10))`  

**Correct Answer: C**

---

## Question 3: Yield Statement

What happens when a generator function encounters a `yield` statement?

A) The function terminates  
B) The function pauses and returns a value, saving its state  
C) The function raises an exception  
D) The function continues without interruption  

**Correct Answer: B**

---

## Question 4: Generator.send()

What does the `send()` method do with a generator?

A) Terminates the generator  
B) Sends a value into the generator that becomes the result of the current yield  
C) Creates a new generator  
D) Sends the generator to another function  

**Correct Answer: B**

---

## Question 5: itertools.chain

What does `itertools.chain([1, 2], [3, 4])` produce?

A) `[[1, 2], [3, 4]]`  
B) `[1, 2, 3, 4]`  
C) `[(1, 3), (2, 4)]`  
D) `[3, 7]`  

**Correct Answer: B**

---

## Question 6: Generator Memory

Why are generators memory-efficient?

A) They compress data automatically  
B) They generate values on-the-fly instead of storing all values in memory  
C) They use less CPU  
D) They cache results  

**Correct Answer: B**

---

## Question 7: yield from

What does `yield from` do?

A) Creates multiple generators  
B) Delegates generator operations to another generator  
C) Yields values in reverse order  
D) Combines multiple yield statements  

**Correct Answer: B**

---

## Question 8: itertools.islice

What does `list(itertools.islice(range(100), 5, 10))` return?

A) `[5, 6, 7, 8, 9]`  
B) `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`  
C) `[5, 10]`  
D) `[5, 15, 25, 35, 45]`  

**Correct Answer: A**

---

## Question 9: Infinite Iterators

Which `itertools` function creates an infinite iterator that cycles through values?

A) `repeat()`  
B) `cycle()`  
C) `count()`  
D) `infinite()`  

**Correct Answer: B**

---

## Question 10: Generator Comprehension Performance

When is a generator expression preferred over a list comprehension?

A) When you need random access to elements  
B) When working with large datasets and you only need to iterate once  
C) When you need to sort the results  
D) When you need to access the length  

**Correct Answer: B**

---

## Scoring Guide

- **9-10 correct**: Excellent! You're an iteration expert.
- **7-8 correct**: Strong understanding! Minor concepts to review.
- **5-6 correct**: Good foundation. Practice with itertools more.
- **Below 5**: Review generators and itertools. Try implementing custom iterators.
