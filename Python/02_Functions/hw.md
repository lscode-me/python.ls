# Functions and Functional Programming - Homework


1. Function Basics and Arguments
   Create a flexible data processing function:
   
   Function: `process_data(data, *transforms, reverse=False, **options)`
   - data: list of numbers
   - transforms: variable number of transformation functions
   - reverse: whether to reverse the result
   - options: additional options like 'filter_negatives', 'round_to'
   
   Your task:
   - Apply all transforms in sequence to the data
   - Filter negatives if filter_negatives=True
   - Round results if round_to is specified
   - Reverse if reverse=True
   - Test with multiple scenarios
   
   Example:
       process_data([1, 2, 3], lambda x: x * 2, lambda x: x + 1)
       # [3, 5, 7]
   
   Your goal:
   - Master all argument types (*args, **kwargs)
   - Understand argument order and precedence
   - Practice functional composition

2. Closures and Function Factories
   Create function factories for common operations:
   
   a) create_multiplier(n) - returns function that multiplies by n
   b) create_formatter(prefix, suffix) - returns function that formats strings
   c) create_validator(min_val, max_val) - returns validation function
   d) create_accumulator(initial=0) - returns function that accumulates values
   
   Your task:
   - Implement all four factories using closures
   - Each should maintain internal state if needed
   - Test with multiple instances
   - Show that each instance has independent state
   
   Example:
       times_2 = create_multiplier(2)
       times_5 = create_multiplier(5)
       times_2(10)  # 20
       times_5(10)  # 50
   
   Your goal:
   - Understand closures and variable capture
   - Master nonlocal keyword for state management
   - Learn factory pattern with closures

3. Custom Decorators
   Create the following decorators:
   
   a) @timer - measure function execution time
   b) @cache - cache function results (memoization)
   c) @validate_types - validate argument types using annotations
   d) @retry(max_attempts=3) - retry function on exception
   e) @log_calls(filename) - log all function calls to a file
   
   Your task:
   - Implement all decorators with proper wrapping
   - Use functools.wraps to preserve metadata
   - Handle *args and **kwargs correctly
   - Test each decorator thoroughly
   - Combine multiple decorators on one function
   
   Example:
       @timer
       @cache
       def fibonacci(n):
           if n <= 1: return n
           return fibonacci(n-1) + fibonacci(n-2)
   
   Your goal:
   - Master decorator syntax and patterns
   - Understand decorator composition
   - Learn practical decorator use cases
   - Practice working with function metadata

4. Higher-Order Functions and Functional Tools
   Implement your own versions of built-in functional tools:
   
   a) my_map(func, iterable) - like map()
   b) my_filter(predicate, iterable) - like filter()
   c) my_reduce(func, iterable, initial=None) - like reduce()
   d) compose(*functions) - compose multiple functions
   e) pipe(value, *functions) - pipe value through functions
   
   Your task:
   - Implement each function as a generator where appropriate
   - Handle edge cases (empty iterables, None values)
   - Test with various data types and functions
   - Compare performance with built-in versions
   
   Example:
       compose(str.upper, str.strip)("  hello  ")  # "HELLO"
       pipe(5, lambda x: x * 2, lambda x: x + 1)   # 11
   
   Your goal:
   - Understand functional programming principles
   - Master generator patterns
   - Learn function composition techniques

5. Generators and Lazy Evaluation
   Create the following generators:
   
   a) fibonacci_gen(max_count) - generate Fibonacci numbers
   b) prime_gen(max_num) - generate prime numbers up to max_num
   c) batch(iterable, size) - yield batches of items
   d) sliding_window(iterable, window_size) - yield sliding windows
   e) chain(*iterables) - chain multiple iterables (like itertools.chain)
   
   Your task:
   - Implement as generators using yield
   - Ensure lazy evaluation (don't compute all at once)
   - Handle infinite sequences where appropriate
   - Test memory efficiency with large sequences
   
   Example:
       for batch in batch([1,2,3,4,5], 2):
           print(batch)  # [1,2], [3,4], [5]
   
   Your goal:
   - Master generator functions and yield
   - Understand lazy evaluation benefits
   - Learn to work with iterables efficiently

6. Recursion and Memoization
   Implement recursive solutions with optimization:
   
   a) Binary search (recursive)
   b) Merge sort (recursive)
   c) Directory tree walker (recursive)
   d) Memoized Fibonacci
   e) Tower of Hanoi solver
   
   Your task:
   - Implement recursive versions
   - Add memoization using decorators
   - Compare performance with/without memoization
   - Handle base cases correctly
   - Visualize recursion depth if possible
   
   Your goal:
   - Master recursive thinking
   - Understand recursion vs iteration trade-offs
   - Learn memoization techniques
   - Practice divide-and-conquer algorithms

7. Functional Data Processing
   Create a data processing pipeline using functional programming:
   
   Given a list of dictionaries representing people:
       people = [
           {"name": "Alice", "age": 30, "salary": 50000},
           {"name": "Bob", "age": 25, "salary": 45000},
           ...
       ]
   
   Tasks:
   a) Filter people by age range using filter()
   b) Extract and transform data using map()
   c) Calculate statistics using reduce()
   d) Create complex pipelines combining multiple operations
   e) Implement using only functional programming (no loops)
   
   Your task:
   - Use map, filter, reduce exclusively
   - No for/while loops
   - No list mutations
   - Chain operations functionally
   - Compare with imperative version
   
   Your goal:
   - Think functionally
   - Understand declarative vs imperative
   - Master functional data transformations
   - Learn pure function patterns

8. Advanced Function Techniques
   Implement advanced function patterns:
   
   a) Currying: convert multi-arg function to chain of single-arg functions
   b) Partial application: create specialized functions from general ones
   c) Function pipeline: create data processing pipelines
   d) Lazy evaluation: implement lazy properties and computations
   e) Trampolines: optimize tail recursion
   
   Your task:
   - Implement curry(func) decorator
   - Use functools.partial for specialization
   - Create a Pipeline class for chaining operations
   - Implement lazy evaluation for expensive computations
   - Demonstrate tail call optimization workaround
   
   Example:
       @curry
       def add(a, b, c):
           return a + b + c
       
       add(1)(2)(3)  # 6
   
   Your goal:
   - Master advanced functional patterns
   - Understand function transformation techniques
   - Learn optimization strategies
   - Practice metaprogramming with functions

