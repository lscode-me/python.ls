## Homework Assignments - Protocols and Interfaces


1. Implementing Common Protocols
   Create a `Deck` class representing a deck of playing cards:
   
   Implement these protocols:
   - Sequence protocol: __len__, __getitem__
   - Container protocol: __contains__
   - Iterator protocol: __iter__
   - Callable protocol: __call__ (shuffle the deck)
   - String representation: __str__, __repr__
   
   Your task:
   - Support len(deck)
   - Support deck[index] and slicing
   - Support "card in deck"
   - Support iteration: for card in deck
   - Support deck() to shuffle
   - Create Card class with suit and rank
   
   Your goal:
   - Master protocol implementation
   - Understand duck typing
   - Practice making objects behave like built-ins

2. Numeric Protocol Implementation
   Create a `Fraction` class for rational numbers:
   
   Implement:
   - Arithmetic: __add__, __sub__, __mul__, __truediv__
   - Comparison: __eq__, __lt__, __le__, __gt__, __ge__
   - Conversion: __int__, __float__, __str__
   - Simplification: reduce to lowest terms automatically
   
   Your task:
   - Handle operations between Fraction and int
   - Implement proper fraction arithmetic
   - Auto-simplify (e.g., 2/4 becomes 1/2)
   - Support mixed operations: Fraction(1,2) + 3
   
   Example:
       f1 = Fraction(1, 2)
       f2 = Fraction(1, 3)
       print(f1 + f2)  # 5/6
   
   Your goal:
   - Master numeric protocols
   - Understand operator overloading
   - Practice mathematical correctness

3. Custom Collections with ABCs
   Create custom collection classes using collections.abc:
   
   a) UniqueList - list that doesn't allow duplicates
      Inherit from: collections.abc.MutableSequence
   
   b) OrderedSet - set that maintains insertion order
      Inherit from: collections.abc.MutableSet
   
   c) DefaultDict - dict with default factory
      Inherit from: collections.abc.MutableMapping
   
   Your task:
   - Implement all required abstract methods
   - Add custom behavior for each collection
   - Test that they work with built-in functions
   - Compare performance with built-in types
   
   Your goal:
   - Understand collections ABCs
   - Learn abstract method implementation
   - Practice creating custom collections

4. Context Manager Protocol
   Create the following context managers:
   
   a) Timer - measure execution time with optional logging
   b) TemporaryDirectory - create/cleanup temp directory
   c) DatabaseConnection - manage DB connection lifecycle
   d) SuppressException - suppress specific exceptions
   e) ChangeDirectory - temporarily change working directory
   
   Your task:
   - Implement using __enter__ and __exit__
   - Handle exceptions properly in __exit__
   - Test with various scenarios
   - Also implement using @contextmanager decorator
   
   Your goal:
   - Master context manager protocol
   - Understand resource management
   - Practice cleanup and exception handling

5. Typing Protocols
   Create a plugin system using typing.Protocol:
   
   Define protocols for:
   - DataLoader: load(filename: str) -> Any
   - DataProcessor: process(data: Any) -> Any
   - DataSaver: save(data: Any, filename: str) -> None
   
   Implement concrete classes:
   - CSVLoader, JSONLoader, XMLLoader
   - FilterProcessor, TransformProcessor
   - CSVSaver, JSONSaver
   
   Your task:
   - Define protocols with type hints
   - Implement multiple concrete classes
   - Create pipeline combining all three protocols
   - No inheritance required (duck typing)
   
   Your goal:
   - Master typing.Protocol
   - Understand structural subtyping
   - Practice type-safe duck typing
   - Learn plugin architecture patterns

6. Comparable Protocol
   Create a system for sorting and comparing custom objects:
   
   Implement for:
   - Student (by grade, then name)
   - Task (by priority, then deadline)
   - File (by size, then name)
   
   Requirements:
   - Implement __eq__, __lt__, __le__, __gt__, __ge__, __ne__
   - Support sorting with sorted()
   - Support min(), max()
   - Implement using functools.total_ordering
   
   Your task:
   - Implement complete comparison protocol
   - Test sorting in different scenarios
   - Handle edge cases (None values, equal items)
   - Demonstrate functools.total_ordering usage
   
   Your goal:
   - Master comparison protocols
   - Understand total ordering
   - Practice sorting algorithms

7. Callable Objects and Function-like Classes
   Create callable classes for different use cases:
   
   a) Memoizer - cache function results
   b) RateLimiter - limit function call rate
   c) Validator - validate input with custom rules
   d) EventHandler - handle events with callbacks
   e) StateMachine - implement state transitions
   
   Your task:
   - Implement __call__ for each class
   - Maintain internal state
   - Support function-like behavior
   - Add useful methods beyond __call__
   
   Example:
       @Memoizer
       def expensive_function(n):
           return n ** 2
   
   Your goal:
   - Master callable protocol
   - Create function-like objects
   - Practice decorator patterns with classes

8. Multi-Protocol Implementation
   Create a `Matrix` class implementing multiple protocols:
   
   Protocols to implement:
   - Sequence: indexing, slicing, length
   - Numeric: addition, subtraction, multiplication
   - Comparison: equality
   - Iterator: row-wise iteration
   - Context manager: temporary matrix transformations
   - Callable: apply function to all elements
   
   Your task:
   - Support matrix[i][j] and matrix[i] access
   - Implement matrix arithmetic correctly
   - Allow: for row in matrix
   - Support: matrix(lambda x: x * 2)
   - Test with various operations
   
   Your goal:
   - Combine multiple protocols in one class
   - Understand protocol interactions
   - Create rich, Pythonic interfaces

