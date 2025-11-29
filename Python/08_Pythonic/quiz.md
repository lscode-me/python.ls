# Pythonic Code - Quiz

Test your knowledge of writing idiomatic, clean, and Pythonic code.

---

## Question 1: The Zen of Python

Which statement is NOT one of the principles from "The Zen of Python"?

A) Explicit is better than implicit  
B) Simple is better than complex  
C) Readability counts  
D) Performance is better than readability  

---

## Question 2: List Comprehension

Which is the most Pythonic way to create a list of squares?

A) `squares = [x**2 for x in range(10)]`  
B) `squares = []; [squares.append(x**2) for x in range(10)]`  
C) `squares = list(map(lambda x: x**2, range(10)))`  
D) `squares = []; exec("[squares.append(x**2) for x in range(10)]")` 

---

## Question 3: EAFP vs LBYL

What does EAFP stand for in Python?

A) Error And Failure Prevention  
B) Execute And Fix Problems  
C) Easier to Ask for Forgiveness than Permission  
D) Every Action Follows Protocol  

---

## Question 4: Enumerate

What is the most Pythonic way to iterate with both index and value?

A) `for i in range(len(items)): print(i, items[i])`  
B) `i = 0; for item in items: print(i, item); i += 1`  
C) `for item in items: print(items.index(item), item)`  
D) `for i, item in enumerate(items): print(i, item)`  

---

## Question 5: String Formatting

Which is the most modern and Pythonic string formatting method?

A) `"Hello, %s" % name`  
B) `f"Hello, {name}"`  
C) `"Hello, {}".format(name)`  
D) `"Hello, " + name`  

---

## Question 6: Context Managers

When should you use a context manager (with statement)?

A) Only for file operations  
B) For any resource that needs setup and cleanup  
C) Only for database connections  
D) Never, try/finally is better  

---

## Question 7: Unpacking

What does this code do: `a, *b, c = [1, 2, 3, 4, 5]`?

A) `a=1, b=[2, 3, 4], c=5`  
B) Raises a SyntaxError  
C) `a=1, b=2, c=5`  
D) `a=1, b=[2, 3, 4, 5], c=None`  

---

## Question 8: Default Dictionary Values

What's the Pythonic way to get a dictionary value with a default?

A) `value = d[key] if key in d else default`  
B) `try: value = d[key]\nexcept: value = default`  
C) `value = d.get(key, default)`  
D) `value = d[key] or default`  

---

## Question 9: Multiple Comparisons

Which is the most Pythonic way to check if a value is in a range?

A) `if x >= 1 and x <= 10:`  
B) `if x in range(1, 11):`  
C) `if min(1, x) == 1 and max(x, 10) == 10:`  
D) `if 1 <= x <= 10:`  

---

## Question 10: Any and All

What does `all([True, True, False, True])` return?

A) `False`  
B) `True`  
C) `[True, True, True]`  
D) `3`  

---

## Answer Key

1. D - Performance is better than readability (this is NOT in the Zen of Python)
2. A - `squares = [x**2 for x in range(10)]`
3. C - Easier to Ask for Forgiveness than Permission
4. D - `for i, item in enumerate(items): print(i, item)`
5. B - `f"Hello, {name}"`
6. B - For any resource that needs setup and cleanup
7. A - `a=1, b=[2, 3, 4], c=5`
8. C - `value = d.get(key, default)`
9. D - `if 1 <= x <= 10:`
10. A - `False`

---

## Scoring Guide

- **9-10 correct**: Excellent! Your code is truly Pythonic.
- **7-8 correct**: Great! You understand Python idioms well.
- **5-6 correct**: Good foundation. Keep practicing Pythonic patterns.
- **Below 5**: Read PEP 8 and practice writing more idiomatic code.
