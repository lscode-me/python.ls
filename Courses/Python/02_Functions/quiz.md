# Functions and Functional Programming - Quiz

Test your knowledge of functions, closures, decorators, and functional programming concepts.

---

## Question 1: Function Arguments

What does the `*args` parameter in a function definition do?

A) Creates a required argument named 'args'  
B) Collects all keyword arguments into a dictionary  
C) Collects all positional arguments into a tuple  
D) Unpacks a list into separate arguments  

---

## Question 2: Argument Order

In a function definition, what is the correct order of parameters?

A) `**kwargs, *args, defaults, positional`  
B) `positional, defaults, *args, **kwargs`  
C) `positional, *args, **kwargs, defaults`  
D) `defaults, positional, *args, **kwargs`  

---

## Question 3: Complex Function Call

Given the function: `def func(a, b, *args, key="default", **kwargs): pass`

What is captured in `kwargs` when called as: `func(1, 2, 3, key="value", extra="x")`?

A) `{'key': 'value', 'extra': 'x'}`  
B) `{'extra': 'x'}`  
C) `{'key': 'value'}`  
D) `{}`  

---

## Question 4: Keyword-Only Arguments

What does the `*` in `def func(a, b, *, c, d):` indicate?

A) `c` and `d` must be passed as positional arguments  
B) `c` and `d` must be passed as keyword arguments  
C) `c` and `d` are optional  
D) All arguments after `*` are collected into a tuple  

---

## Question 5: LEGB Rule

What does the LEGB rule stand for in Python scope resolution?

A) Local, Extended, Global, Built-in  
B) Local, Enclosing, Global, Built-in  
C) Load, Execute, Generate, Build  
D) Local, Environment, Global, Base  

---

## Question 6: Variable Scope

What will this code print?

```python
x = 10
def func():
    x = 20
    print(x)
func()
print(x)
```

A) `20` then `20`  
B) `10` then `10`  
C) `20` then `10`  
D) `10` then `20`  

---

## Question 7: Global Keyword

When do you need to use the `global` keyword?

A) When reading a global variable inside a function  
B) When modifying a global variable inside a function  
C) When creating any variable inside a function  
D) When calling a function from global scope  

---

## Question 8: Nonlocal vs Global

What is the difference between `nonlocal` and `global`?

A) `nonlocal` modifies enclosing function scope, `global` modifies module scope  
B) `nonlocal` is faster than `global`  
C) They are the same  
D) `nonlocal` works with variables, `global` works with functions  

---

## Question 9: Lambda Functions

Which of the following is a valid lambda function?

A) `lambda x, y: return x + y`  
B) `lambda x, y: x + y`  
C) `lambda (x, y): x + y`  
D) `lambda: x, y -> x + y`  

---

## Question 10: Closures

What is a closure in Python?

A) A function that remembers values from its enclosing scope  
B) A function that closes files automatically  
C) A function that can only be called once  
D) A function that has no return value  

---

## Question 11: Decorator Syntax

What is `@decorator` syntax equivalent to?

A) `func = decorator(func)`  
B) `decorator(func())`  
C) `func = func(decorator)`  
D) `func.decorator()`  

---

## Question 12: Decorator Execution

Given:
```python
@bold
@italic
def greet():
    return "Hi"
```

What is the equivalent without decorators?

A) `greet = italic(bold(greet))`  
B) `greet = bold(italic(greet))`  
C) `greet = bold(greet(italic))`  
D) `greet = greet(bold, italic)`  

---

## Question 13: Decorator with Arguments

Why does a decorator with arguments need three levels of functions?

A) It doesn't - two levels are enough  
B) Outer function receives decorator args, middle creates decorator, inner is the wrapper  
C) For better performance  
D) To confuse programmers  

---

## Question 14: functools.wraps

What does `@wraps(func)` do in a decorator?

A) Wraps the function in a try-catch block  
B) Preserves the original function's metadata  
C) Makes the decorator faster  
D) Allows the function to wrap other functions  

---

## Question 15: Immutability Concept

What does immutability mean in programming?

A) Data cannot be changed after it's created  
B) Functions cannot have side effects  
C) Variables cannot be reassigned  
D) Objects cannot be deleted  

---

## Question 16: Mutable vs Immutable

Which of these Python types is immutable?

A) `list`  
B) `dict`  
C) `tuple`  
D) `set`  

---

## Question 17: Immutable Practice

What's wrong with: `def add_item(item, items=[]):`?

A) Default mutable argument is shared across calls  
B) Syntax error  
C) `items` should be a tuple  
D) Nothing is wrong  

---

## Question 18: Creating New Data

Which approach follows immutability principles?

A) `items.append(4)`  
B) `items = items + [4]`  
C) `items.extend([4])`  
D) `items += [4]`  

---

## Question 19: Dictionary Immutability

How do you add a key to a dictionary immutably?

A) `d["key"] = "value"`  
B) `d.update({"key": "value"})`  
C) `new_d = {**d, "key": "value"}`  
D) `d.setdefault("key", "value")`  

---

## Question 20: Map Function

What does `list(map(lambda x: x * 2, [1, 2, 3]))` return?

A) `[1, 2, 3, 1, 2, 3]`  
B) `[1, 4, 9]`  
C) `6`  
D) `[2, 4, 6]`  

---

## Question 21: Filter Function

What does `list(filter(lambda x: x > 5, [3, 6, 2, 8, 1, 9]))` return?

A) `[3, 2, 1]`  
B) `[6, 8, 9]`  
C) `True`  
D) `[3, 6, 2, 8, 1, 9]`  

---

## Question 22: Generator Functions

What keyword is used in a generator function to yield values?

A) yield  
B) return  
C) generate  
D) next  

---

## Question 23: First-Class Functions

What does it mean that Python has "first-class functions"?

A) Functions are always executed first  
B) Only built-in functions are supported  
C) Functions can be passed as arguments, returned from other functions, and assigned to variables  
D) Functions must be defined before variables  

---

## Question 24: Recursion

What is the base case in a recursive function?

A) The first function call  
B) The most complex case  
C) The function's return type  
D) The condition that stops the recursion  

---

## Question 25: Type Hints

In the function signature `def greet(name: str) -> str:`, what does `-> str` indicate?

A) The function returns a string  
B) The function requires a string argument  
C) The function converts input to string  
D) The function has a string default value  

---

## Answer Key

1. **C** - Collects all positional arguments into a tuple
2. **B** - `positional, defaults, *args, **kwargs`
3. **B** - `{'extra': 'x'}` (key is matched to the named parameter)
4. **B** - `c` and `d` must be passed as keyword arguments
5. **B** - Local, Enclosing, Global, Built-in
6. **C** - `20` then `10` (local x shadows global x)
7. **B** - When modifying a global variable inside a function
8. **A** - `nonlocal` modifies enclosing function scope, `global` modifies module scope
9. **B** - `lambda x, y: x + y`
10. **A** - A function that remembers values from its enclosing scope
11. **A** - `func = decorator(func)`
12. **B** - `greet = bold(italic(greet))` (bottom to top)
13. **B** - Outer function receives decorator args, middle creates decorator, inner is the wrapper
14. **B** - Preserves the original function's metadata
15. **A** - Data cannot be changed after it's created
16. **C** - `tuple`
17. **A** - Default mutable argument is shared across calls
18. **B** - `items = items + [4]` (creates new list)
19. **C** - `new_d = {**d, "key": "value"}`
20. **D** - `[2, 4, 6]`
21. **B** - `[6, 8, 9]`
22. **A** - yield
23. **C** - Functions can be passed as arguments, returned from other functions, and assigned to variables
24. **D** - The condition that stops the recursion
25. **A** - The function returns a string

---

## Scoring Guide

- **23-25 correct**: Outstanding! You're a functional programming expert.
- **20-22 correct**: Excellent! You have a strong understanding.
- **17-19 correct**: Very good! A few concepts need more practice.
- **14-16 correct**: Good foundation. Review decorators and immutability.
- **11-13 correct**: Fair. Focus on scope, decorators, and immutability.
- **Below 11**: Review the lecture materials thoroughly and practice with examples.

---

## Key Concepts to Review

If you struggled with specific questions, focus on these topics:

- **Questions 1-4**: Function arguments, *args, **kwargs, keyword-only arguments
- **Questions 5-8**: Variable scope, LEGB rule, global and nonlocal keywords
- **Questions 9-10**: Lambda functions and closures
- **Questions 11-14**: Decorators, decorator syntax, and functools.wraps
- **Questions 15-19**: Immutability, mutable vs immutable types, pure functions
- **Questions 20-25**: Higher-order functions, generators, recursion, type hints
