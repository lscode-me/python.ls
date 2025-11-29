## Homework Assignments - Iteration Protocol


1. Custom Iterator Classes
   Create the following iterator classes:
   
   a) RangeIterator - mimics built-in range()
      - Support start, stop, step
      - Implement __iter__ and __next__
      - Handle negative steps
   
   b) CycleIterator - cycles through items infinitely
      - Takes any iterable
      - Repeats forever
      - Track iteration count
   
   c) BatchIterator - yields items in batches
      - Takes iterable and batch size
      - Last batch may be smaller
      - Support overlapping batches (optional)
   
   Your task:
   - Implement both __iter__ and __next__
   - Handle StopIteration correctly
   - Test with various inputs
   - Compare with itertools equivalents
   
   Your goal:
   - Master iterator protocol
   - Understand __iter__ vs __next__
   - Practice state management in iterators

2. Generator Functions
   Implement the following generators:
   
   a) fibonacci(n) - first n Fibonacci numbers
   b) primes(max_num) - all primes up to max_num
   c) permutations(items, r) - all r-length permutations
   d) sliding_window(iterable, size) - sliding window view
   e) flatten(nested) - flatten nested structures
   
   Your task:
   - Use yield for lazy evaluation
   - Handle edge cases (empty input, size=1, etc.)
   - Make memory efficient (no lists)
   - Test with large inputs
   
   Example:
       for window in sliding_window([1,2,3,4,5], 3):
           print(window)  # [1,2,3], [2,3,4], [3,4,5]
   
   Your goal:
   - Master yield statement
   - Understand lazy evaluation
   - Practice generator patterns

3. Generator Expressions and Pipelines
   Create data processing pipelines using generators:
   
   Given a log file with entries like:
       2023-11-26 10:15:23 ERROR Connection failed
       2023-11-26 10:15:24 INFO Request processed
   
   Tasks:
   a) Parse log entries (generator)
   b) Filter by log level (generator)
   c) Extract timestamps (generator)
   d) Group by hour (generator)
   e) Generate statistics (generator)
   
   Your task:
   - Use generator expressions where possible
   - Chain generators into pipeline
   - Keep each stage simple and focused
   - Compare memory usage with list-based approach
   
   Your goal:
   - Master generator expressions
   - Learn pipeline architecture
   - Understand lazy evaluation benefits

4. Advanced Generator Methods
   Explore send(), throw(), and close():
   
   a) Coroutine: running average calculator
      - Use send() to add values
      - Returns current average
   
   b) State machine generator
      - Multiple states with transitions
      - Use send() to trigger transitions
   
   c) Error-handling generator
      - Use throw() to inject errors
      - Generator catches and handles them
   
   Your task:
   - Implement bidirectional communication
   - Handle exceptions in generators
   - Demonstrate proper cleanup with close()
   - Show practical use cases
   
   Your goal:
   - Master generator methods
   - Understand coroutines
   - Practice advanced iteration patterns

5. yield from and Generator Delegation
   Implement using yield from:
   
   a) Tree traversal (depth-first and breadth-first)
   b) Recursive directory walker
   c) Nested data structure flattener
   d) Chain multiple data sources
   e) Recursive parser for nested expressions
   
   Your task:
   - Use yield from for delegation
   - Handle recursive structures
   - Compare with manual iteration
   - Demonstrate code simplification
   
   Example:
       def traverse_tree(node):
           yield node.value
           for child in node.children:
               yield from traverse_tree(child)
   
   Your goal:
   - Master yield from
   - Simplify recursive generators
   - Understand generator delegation

6. itertools Mastery
   Solve problems using itertools module:
   
   a) Generate all password combinations (4-8 chars, letters+digits)
   b) Find all triplets in list that sum to target
   c) Create round-robin scheduler from tasks
   d) Implement pagination with islice
   e) Group and aggregate data with groupby
   
   Your task:
   - Use appropriate itertools functions
   - Combine multiple itertools tools
   - Optimize for memory and speed
   - Compare with manual implementation
   
   Functions to use:
   - product, permutations, combinations
   - chain, islice, cycle
   - groupby, accumulate
   - filterfalse, takewhile, dropwhile
   
   Your goal:
   - Master itertools module
   - Learn efficient iteration patterns
   - Solve complex problems simply

7. Custom Iterable Classes
   Create iterable classes for:
   
   a) CircularBuffer - fixed-size buffer with wrap-around
   b) LazyList - list that loads items on demand
   c) InfiniteGrid - infinite 2D grid with sparse storage
   d) TimeSeriesData - iterate with different time windows
   e) PaginatedAPI - iterate over paginated REST API
   
   Your task:
   - Implement __iter__ returning generator or iterator
   - Support multiple simultaneous iterations
   - Handle state correctly
   - Add useful methods beyond iteration
   
   Your goal:
   - Create rich iterable interfaces
   - Understand iterable vs iterator
   - Practice real-world iteration scenarios

8. Performance and Memory Optimization
   Compare and optimize iteration approaches:
   
   Tasks:
   a) Process 1 million numbers:
      - List comprehension
      - Generator expression
      - Manual loop
      - map/filter
   
   b) Measure:
      - Memory usage
      - Execution time
      - CPU usage
   
   c) Optimize:
      - Finding first match
      - Aggregating large dataset
      - Processing file line by line
   
   Your task:
   - Implement all approaches
   - Use memory_profiler and timeit
   - Profile and compare
   - Write recommendations
   
   Your goal:
   - Understand performance implications
   - Learn when to use generators
   - Master profiling techniques
   - Make informed optimization decisions

9. Infinite Sequences
   Create infinite generators:
   
   a) Collatz sequence generator
   b) Random number stream with seed
   c) Infinite repeat with delays
   d) Streaming data simulator
   e) Infinite geometric series
   
   Your task:
   - Generate infinitely (no endpoint)
   - Use with itertools.islice for testing
   - Implement useful infinite sequences
   - Show practical applications
   
   Example:
       def collatz(n):
           while True:
               yield n
               n = n // 2 if n % 2 == 0 else 3 * n + 1
               if n == 1:
                   yield 1
                   return
   
   Your goal:
   - Master infinite iteration
   - Understand lazy evaluation power
   - Practice mathematical sequences

10. Real-World Iteration Patterns
    Implement practical iterators for:
    
    a) CSV file reader with header parsing
    b) JSON stream processor (line-delimited JSON)
    c) Database result cursor wrapper
    d) File system tree walker with filtering
    e) Network stream processor (chunks)
    
    Your task:
    - Handle real data formats
    - Implement error handling
    - Support filtering and transformation
    - Make memory-efficient
    - Add context manager support
    
    Your goal:
    - Apply iteration to real problems
    - Handle I/O efficiently
    - Create production-ready iterators
    - Master practical patterns

