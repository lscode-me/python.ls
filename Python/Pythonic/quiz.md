# Pythonic Code - Quiz

Test your knowledge of writing idiomatic, clean, and Pythonic code.

---

## Question 1: The Zen of Python

Which statement is NOT one of the principles from "The Zen of Python"?

A) Explicit is better than implicit  
B) Simple is better than complex  
C) Performance is better than readability  
D) Readability counts  

**Correct Answer: C**

---

## Question 2: List Comprehension

Which is the most Pythonic way to create a list of squares?

A) `squares = []; [squares.append(x**2) for x in range(10)]`  
B) `squares = [x**2 for x in range(10)]`  
C) `squares = list(map(lambda x: x**2, range(10)))`  
D) `squares = []; exec("[squares.append(x**2) for x in range(10)]")`  

**Correct Answer: B**

---

## Question 3: EAFP vs LBYL

What does EAFP stand for in Python?

A) Error And Failure Prevention  
B) Easier to Ask for Forgiveness than Permission  
C) Execute And Fix Problems  
D) Every Action Follows Protocol  

**Correct Answer: B**

---

## Question 4: Enumerate

What is the most Pythonic way to iterate with both index and value?

A) `for i in range(len(items)): print(i, items[i])`  
B) `for i, item in enumerate(items): print(i, item)`  
C) `i = 0; for item in items: print(i, item); i += 1`  
D) `for item in items: print(items.index(item), item)`  

**Correct Answer: B**

---

## Question 5: String Formatting

Which is the most modern and Pythonic string formatting method?

A) `"Hello, %s" % name`  
B) `"Hello, {}".format(name)`  
C) `f"Hello, {name}"`  
D) `"Hello, " + name`  

**Correct Answer: C**

---

## Question 6: Context Managers

When should you use a context manager (with statement)?

A) Only for file operations  
B) For any resource that needs setup and cleanup  
C) Only for database connections  
D) Never, try/finally is better  

**Correct Answer: B**

---

## Question 7: Unpacking

What does this code do: `a, *b, c = [1, 2, 3, 4, 5]`?

A) Raises a SyntaxError  
B) `a=1, b=[2, 3, 4], c=5`  
C) `a=1, b=2, c=5`  
D) `a=1, b=[2, 3, 4, 5], c=None`  

**Correct Answer: B**

---

## Question 8: Default Dictionary Values

What's the Pythonic way to get a dictionary value with a default?

A) `value = d[key] if key in d else default`  
B) `value = d.get(key, default)`  
C) `try: value = d[key]\nexcept: value = default`  
D) `value = d[key] or default`  

**Correct Answer: B**

---

## Question 9: Multiple Comparisons

Which is the most Pythonic way to check if a value is in a range?

A) `if x >= 1 and x <= 10:`  
B) `if 1 <= x <= 10:`  
C) `if x in range(1, 11):`  
D) `if min(1, x) == 1 and max(x, 10) == 10:`  

**Correct Answer: B**

---

## Question 10: Any and All

What does `all([True, True, False, True])` return?

A) `True`  
B) `False`  
C) `[True, True, True]`  
D) `3`  

**Correct Answer: B**

---

## Scoring Guide

- **9-10 correct**: Excellent! Your code is truly Pythonic.
- **7-8 correct**: Great! You understand Python idioms well.
- **5-6 correct**: Good foundation. Keep practicing Pythonic patterns.
- **Below 5**: Read PEP 8 and practice writing more idiomatic code.
