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

## Question 11: Generator vs List

What's the main advantage of `(x**2 for x in range(1000000))` over `[x**2 for x in range(1000000)]`?

A) Generators are faster  
B) Generators use less memory (lazy evaluation)  
C) Generators can be reused multiple times  
D) Generators are easier to read  

---

## Question 12: Dictionary Comprehension

What does `{k: v*2 for k, v in {'a': 1, 'b': 2}.items() if v > 1}` produce?

A) `{'a': 2, 'b': 4}`  
B) `{'b': 4}`  
C) `{2: 'b'}`  
D) `{'b': 2}`  

---

## Question 13: Duck Typing

Which approach is more Pythonic for accepting different iterable types?

A) `if isinstance(items, (list, tuple, set)): process(items)`  
B) `try: iter(items); process(items)`  
C) Just use `for item in items:` without type checking  
D) Convert everything to list first: `process(list(items))`  

---

## Question 14: Star Unpacking

Given `first, *middle, last = [1, 2, 3, 4, 5]`, what is `middle`?

A) `[2, 3, 4]`  
B) `(2, 3, 4)`  
C) `2`  
D) `[2, 3, 4, 5]`  

---

## Question 15: Swapping Variables

What's the Pythonic way to swap two variables?

A) `temp = a; a = b; b = temp`  
B) `a, b = b, a`  
C) `a = a + b; b = a - b; a = a - b`  
D) `a ^= b; b ^= a; a ^= b`  

---

## Question 16: Collections Module

Which `collections` tool is best for counting element frequencies?

A) `defaultdict(int)`  
B) `Counter`  
C) `OrderedDict`  
D) `deque`  

---

## Question 17: Context Manager

What happens to the file if an exception occurs inside a `with` block?

A) File remains open  
B) File is automatically closed  
C) Program crashes  
D) File is deleted  

---

## Question 18: F-String Debugging

What does `print(f"{x=}")` output when `x = 42`?

A) `42`  
B) `x`  
C) `x=42`  
D) `x = 42`  

---

## Question 19: Chained Comparisons

Which statement is equivalent to `if 0 <= x < 100:`?

A) `if x >= 0 and x < 100:`  
B) `if (0 <= x) < 100:`  
C) `if x in range(0, 100):`  
D) Both A and C  

---

## Question 20: Zip Function

What does `list(zip([1, 2, 3], ['a', 'b', 'c']))` return?

A) `[[1, 'a'], [2, 'b'], [3, 'c']]`  
B) `[(1, 'a'), (2, 'b'), (3, 'c')]`  
C) `{1: 'a', 2: 'b', 3: 'c'}`  
D) `[1, 2, 3, 'a', 'b', 'c']`  

---

## Question 21: Generator Function

What's the key difference between `return` and `yield` in a function?

A) `yield` returns multiple values at once  
B) `yield` creates a generator that produces values lazily  
C) `yield` is faster than `return`  
D) `yield` is only for lists  

---

## Question 22: Dictionary Merging

What's the Pythonic way (Python 3.5+) to merge two dictionaries?

A) `d1.update(d2)`  
B) `{**d1, **d2}`  
C) `dict(d1, **d2)`  
D) Both B and C  

---

## Question 23: Enumerate with Start

What does `list(enumerate(['a', 'b', 'c'], start=1))` produce?

A) `[(0, 'a'), (1, 'b'), (2, 'c')]`  
B) `[(1, 'a'), (2, 'b'), (3, 'c')]`  
C) `[('a', 1), ('b', 2), ('c', 3)]`  
D) `[(1, 0), (2, 1), (3, 2)]`  

---

## Question 24: Defaultdict

What happens when you access a non-existent key in `defaultdict(list)`?

A) Raises KeyError  
B) Returns None  
C) Creates the key with an empty list `[]`  
D) Returns an empty string  

---

## Question 25: String Formatting

Which is the most modern Pythonic string formatting?

A) `"Value: %d" % x`  
B) `"Value: {}".format(x)`  
C) `f"Value: {x}"`  
D) `"Value: " + str(x)`  

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Performance is better than readability (this is NOT in the Zen of Python) |
| 2 | B | `squares = [x**2 for x in range(10)]` |
| 3 | A | Easier to Ask for Forgiveness than Permission |
| 4 | B | `for i, item in enumerate(items): print(i, item)` |
| 5 | C | `f"Hello, {name}"` |
| 6 | D | For any resource that needs setup and cleanup |
| 7 | A | `a=1, b=[2, 3, 4], c=5` |
| 8 | A | `value = d.get(key, default)` |
| 9 | C | `if 1 <= x <= 10:` |
| 10 | C | `False` |
| 11 | D | Generators use less memory (lazy evaluation) |
| 12 | C | `{'b': 4}` |
| 13 | A | Just use `for item in items:` without type checking |
| 14 | A | `[2, 3, 4]` |
| 15 | A | `a, b = b, a` |
| 16 | D | `Counter` |
| 17 | A | File is automatically closed |
| 18 | C | `x=42` |
| 19 | B | `if x >= 0 and x < 100:` |
| 20 | D | `[(1, 'a'), (2, 'b'), (3, 'c')]` |
| 21 | B | `yield` creates a generator that produces values lazily |
| 22 | B | Both B and C (though B is more explicit) |
| 23 | C | `[(1, 'a'), (2, 'b'), (3, 'c')]` |
| 24 | D | Creates the key with an empty list `[]` |
| 25 | D | `f"Value: {x}"` |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **22-25 correct (88-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **17-21 correct (68-84%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **12-16 correct (48-64%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 12 correct (<48%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
