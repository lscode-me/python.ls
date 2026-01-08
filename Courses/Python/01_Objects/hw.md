# Objects, References, Memory, Types - Homework


1. Exploring Basic Data Types
   Write a script that creates and prints different data types:
   - Create short strings (e.g., "hello") and long strings (e.g., a paragraph)
   - Create float numbers (e.g., 3.14, 1.0e10)
   - Create complex numbers (e.g., 3+4j, complex(2, -5))
   - Create boolean values (True, False)

   For each object:
   - Print the value
   - Print its type using type()
   - Print its size using sys.getsizeof()

   Your task:
   - Observe size differences between short and long strings
   - Notice how different numeric types are represented
   - Understand basic Python data types

   Your goal:
   - Familiarize yourself with Python's basic data types
   - Understand memory usage of different objects
   - Learn to inspect object properties

2. Understanding References and Identity
   Write a short script that tests whether two variables refer to the same object.
   Use the following examples and explain why each result is True or False:
       a = 256
       b = 256
       a is b

       a = 257
       b = 257
       a is b

       a = []
       b = []
       a is b

       c = a
       a is c

   Your task:
   - Predict the output before running the code.
   - Run the script and compare results.
   - Write a short explanation (1–2 sentences per line).

   Your goal:
   - Understand the difference between identity (is) and equality (==)
   - Learn about Python's integer caching optimization
   - Master the concept of object references vs object values

3. Demonstrating Mutability and Immutability
   Write a script that demonstrates the difference between mutable and immutable objects.

   Test the following object types:
   - Immutable: str, tuple, int, float, bool
   - Mutable: list, dict, set

   For each type, perform operations and observe the behavior:
       # Example for string (immutable)
       s = "hello"
       print(id(s))
       s = s + " world"
       print(id(s))  # Does the id change?

       # Example for list (mutable)
       lst = [1, 2, 3]
       print(id(lst))
       lst.append(4)
       print(id(lst))  # Does the id change?

   Your task:
   - Test all mentioned types
   - Explain why the id changes (or doesn't change) for each type
   - Demonstrate that tuples containing mutable objects have special behavior

   Your goal:
   - Understand mutability vs immutability in Python
   - Learn how modifying objects affects their identity
   - Avoid common bugs related to mutable objects
   - Understand the implications for function arguments and return values

4. Mutable Default Argument Bug
   The following function behaves incorrectly:

       def append_item(x, items=[]):
           items.append(x)
           return items

   Task:
   - Explain what is wrong with this function.
   - Rewrite it so that it works correctly.
   - Show example output of both versions for three calls:
         append_item(1)
         append_item(2)
         append_item(3)

   Your goal:
   - Understand why mutable default arguments are dangerous
   - Learn the proper pattern for default arguments
   - Recognize this common Python pitfall in real code

5. Inspecting Object Memory and References
   Write a script that uses:
       - type()
       - id()
       - sys.getsizeof()
       - sys.getrefcount()
       - gc.get_referrers()
       - gc.get_count()

   Perform the following steps:
       a) Create three objects: an integer, a string, and a list.
       b) Print their type, size, identity, and reference count.
       c) Create additional variables referencing the same objects.
       d) Print updated reference counts and explain what changed.
       e) Use gc.get_referrers() to see what refers to your objects.
       f) Use gc.get_count() to see the current garbage collector stats.
       g) Try gc.collect() and observe changes in gc.get_count().

   Your goal:
   - Understand how reference counting works.
   - Observe how Python stores objects of different types.
   - Learn how the garbage collector tracks objects.

6. Using help() and dir() for Object Inspection
   Write a script that explores the difference between types and instances using help() and dir().

   Test the following:
       # Type vs instance
       print(type(int))
       print(type(int()))

       # Using help on type
       help(int)

       # Using help on instance
       help(int())

       # Using dir on type
       print(dir(int))

       # Using dir on instance
       print(dir(int()))

   Your task:
   - Call help() and dir() on both type and instance for: int, str, list, dict
   - Explain the difference between int and int()
   - Find at least 3 interesting methods for each type using dir()
   - Use help() to understand what one of those methods does
   - Document your findings in comments

   Your goal:
   - Master Python's introspection capabilities
   - Learn to explore unfamiliar objects and modules
   - Understand the difference between types and instances
   - Develop self-sufficiency in learning Python's API
