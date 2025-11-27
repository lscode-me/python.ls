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

## Question 2: Lambda Functions

Which of the following is a valid lambda function?

A) `lambda x, y: return x + y`  
B) `lambda x, y: x + y`  
C) `lambda (x, y): x + y`  
D) `lambda: x, y -> x + y`  

---

## Question 3: Closures

What is a closure in Python?

A) A function that remembers values from its enclosing scope  
B) A function that closes files automatically  
C) A function that can only be called once  
D) A function that has no return value  

---

## Question 4: Decorators

What does a decorator do?

A) Adds comments to a function  
B) Modifies or enhances a function's behavior without changing its code  
C) Deletes a function after execution  
D) Converts a function to a class  

---

## Question 5: Map Function

What does `list(map(lambda x: x * 2, [1, 2, 3]))` return?

A) `[1, 2, 3, 1, 2, 3]`  
B) `[1, 4, 9]`  
C) `6`  
D) `[2, 4, 6]`  

---

## Question 6: Generator Functions

What keyword is used in a generator function to yield values?

A) yield  
B) return  
C) generate  
D) next  

---

## Question 7: First-Class Functions

What does it mean that Python has "first-class functions"?

A) Functions are always executed first  
B) Only built-in functions are supported  
C) Functions can be passed as arguments, returned from other functions, and assigned to variables  
D) Functions must be defined before variables  

---

## Question 8: Recursion

What is the base case in a recursive function?

A) The first function call  
B) The most complex case  
C) The function's return type  
D) The condition that stops the recursion  

---

## Question 9: Filter Function

What does `list(filter(lambda x: x > 5, [3, 6, 2, 8, 1, 9]))` return?

A) `[3, 2, 1]`  
B) `[6, 8, 9]`  
C) `True`  
D) `[3, 6, 2, 8, 1, 9]`  

---

## Question 10: Type Hints

In the function signature `def greet(name: str) -> str:`, what does `-> str` indicate?

A) The function returns a string  
B) The function requires a string argument  
C) The function converts input to string  
D) The function has a string default value  

---

## Answer Key

1. C - Collects all positional arguments into a tuple
2. B - `lambda x, y: x + y`
3. A - A function that remembers values from its enclosing scope
4. B - Modifies or enhances a function's behavior without changing its code
5. D - `[2, 4, 6]`
6. A - yield
7. C - Functions can be passed as arguments, returned from other functions, and assigned to variables
8. D - The condition that stops the recursion
9. B - `[6, 8, 9]`
10. A - The function returns a string

---

## Scoring Guide

- **9-10 correct**: Excellent! You're a functional programming expert.
- **7-8 correct**: Great job! Minor gaps to fill.
- **5-6 correct**: Good foundation. Practice with more complex examples.
- **Below 5**: Review the materials on functions and try the homework assignments.
