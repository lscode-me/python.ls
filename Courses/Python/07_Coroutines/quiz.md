# Quiz: Coroutines and Data Pipelines

## Question 1: Basic Concepts

What is the main difference between a generator and a coroutine?

- [ ] A) Generators are faster than coroutines
- [ ] B) Generators can only be used in Python 3
- [ ] C) Generators produce data (pull), coroutines consume data (push)
- [ ] D) Coroutines require the `async` keyword

---

## Question 2: Priming Coroutines

What happens if you try to send a non-None value to a just-started coroutine without priming it first?

```python
def my_coro():
    while True:
        value = yield
        print(value)

c = my_coro()
c.send(10)  # What happens?
```

- [ ] A) It prints 10
- [ ] B) It raises a `TypeError`
- [ ] C) It raises a `StopIteration`
- [ ] D) It does nothing

---

## Question 3: Bidirectional Communication

What does this coroutine return when you send it values?

```python
def mystery():
    total = 0
    while True:
        value = yield total
        total += value

m = mystery()
next(m)
result = m.send(10)
```

What is `result`?

- [ ] A) 0
- [ ] B) 10
- [ ] C) None
- [ ] D) Raises an error

---

## Question 4: Pipeline Direction

In which order should you build a coroutine pipeline?

```python
# Pipeline: source → filter → transform → sink
```

- [ ] A) source, then filter, then transform, then sink
- [ ] B) sink, then transform, then filter (backward from end)
- [ ] C) It doesn't matter
- [ ] D) All components must be built simultaneously

---

## Question 5: The @coroutine Decorator

What is the purpose of the `@coroutine` decorator?

```python
def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper
```

- [ ] A) Makes coroutines run faster
- [ ] B) Automatically primes the coroutine
- [ ] C) Converts functions to coroutines
- [ ] D) Enables async/await syntax

---

## Question 6: Pull vs Push

Which statement about pull and push models is TRUE?

- [ ] A) Pull model is always faster than push model
- [ ] B) Push model (coroutines) is better for infinite/streaming data
- [ ] C) Pull model cannot handle real-time data
- [ ] D) Push model uses less memory

---

## Question 7: Closing Coroutines

What happens when you call `close()` on a coroutine?

```python
@coroutine
def my_coro(target):
    try:
        while True:
            item = yield
            target.send(item)
    except GeneratorExit:
        print("Closing!")
        target.close()

c = my_coro(some_target)
c.close()
```

- [ ] A) Nothing happens
- [ ] B) The coroutine's `except GeneratorExit` block is executed
- [ ] C) The coroutine raises a `StopIteration`
- [ ] D) The coroutine is paused

---

## Question 8: Tee (Broadcasting)

What does the `tee` component do in a pipeline?

```python
@coroutine
def tee(*targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)
```

- [ ] A) Splits items evenly across targets (round-robin)
- [ ] B) Sends each item to all targets (broadcast)
- [ ] C) Sends items to the first available target
- [ ] D) Buffers items for later processing

---

## Question 9: State Management

Why are coroutines well-suited for stateful processing?

- [ ] A) They use global variables efficiently
- [ ] B) They maintain local variables across calls
- [ ] C) They have special state management syntax
- [ ] D) They store state in a database

---

## Question 10: Pipeline Order

Given this pipeline setup:

```python
sink = printer()
stats = statistics(sink)
transform = map_items(lambda x: x * 2, stats)
filter = filter_items(lambda x: x > 0, transform)

filter.send(5)
filter.send(-3)
filter.send(10)
```

What gets printed?

- [ ] A) 5, -3, 10
- [ ] B) 10, 20
- [ ] C) 5, 10
- [ ] D) Nothing

---

## Question 11: Error Handling

What's the best way to handle errors in a coroutine pipeline?

```python
@coroutine
def process(target):
    while True:
        item = yield
        # How to handle errors?
        target.send(item)
```

- [ ] A) Let errors propagate naturally
- [ ] B) Use try/except around `target.send()`
- [ ] C) Check if item is valid before sending
- [ ] D) Use a separate error sink

---

## Question 12: Memory Efficiency

Which approach uses less memory for processing 1 million items?

**Approach A: List comprehensions**
```python
filtered = [x for x in data if x > 0]
doubled = [x * 2 for x in filtered]
result = list(doubled)
```

**Approach B: Coroutine pipeline**
```python
sink = collector()
doubler = map_items(lambda x: x * 2, sink)
filter = filter_items(lambda x: x > 0, doubler)
for x in data:
    filter.send(x)
```

- [ ] A) Approach A (list comprehensions)
- [ ] B) Approach B (coroutine pipeline)
- [ ] C) They use the same memory
- [ ] D) It depends on the data

---

## Question 13: Yield Expression

What is the value of `x` after this code runs?

```python
def coro():
    x = yield 42
    yield x

c = coro()
result1 = next(c)
result2 = c.send(100)
```

- [ ] A) x = 42, result1 = 42, result2 = 100
- [ ] B) x = 100, result1 = 42, result2 = 100
- [ ] C) x = None, result1 = 42, result2 = None
- [ ] D) x = 100, result1 = None, result2 = 42

---

## Question 14: Pipeline Patterns

Which pipeline pattern is described here: "Collect items until a certain size is reached, then send the batch downstream"?

- [ ] A) Filter
- [ ] B) Map
- [ ] C) Batch/Window
- [ ] D) Tee

---

## Question 15: Real-World Use Case

Which of these is NOT a good use case for coroutine pipelines?

- [ ] A) Real-time log processing
- [ ] B) Processing CSV files with millions of rows
- [ ] C) Reversing a small list
- [ ] D) ETL (Extract-Transform-Load) operations
- [ ] E) Streaming sensor data analysis

---

## Question 16: Debugging Pipelines

You have a pipeline with 5 stages, but output is wrong. What's the best debugging approach?

```python
stage5 = sink()
stage4 = transform_d(stage5)
stage3 = transform_c(stage4)
stage2 = transform_b(stage3)
stage1 = transform_a(stage2)
```

- [ ] A) Add print statements in each stage
- [ ] B) Use a debugger with breakpoints
- [ ] C) Test each stage individually first
- [ ] D) Rewrite everything from scratch

---

## Question 17: Performance

Which change would most improve the performance of a coroutine pipeline?

- [ ] A) Adding more stages
- [ ] B) Using `@coroutine` decorator
- [ ] C) Reducing function call overhead by combining simple stages
- [ ] D) Adding more error handling

---

## Question 18: Async Coroutines

How do traditional coroutines (using `yield` and `send()`) differ from async coroutines (`async def`)?

- [ ] A) They are the same thing
- [ ] B) Traditional coroutines are synchronous, async coroutines support concurrent I/O
- [ ] C) Async coroutines are faster
- [ ] D) Traditional coroutines don't support `yield`

---

## Question 19: Windowing

What does this coroutine do?

```python
@coroutine
def sliding_window(size, target):
    window = []
    while True:
        item = yield
        window.append(item)
        if len(window) > size:
            window.pop(0)
        if len(window) == size:
            target.send(list(window))
```

- [ ] A) Collects all items into a list of given size
- [ ] B) Sends every Nth item
- [ ] C) Sends sliding windows of N consecutive items
- [ ] D) Filters items based on window size

---

## Question 20: Pipeline Termination

What's the correct way to properly terminate a coroutine pipeline?

```python
sink = printer()
stage2 = transform(sink)
stage1 = filter_items(predicate, stage2)

# Process data
for item in data:
    stage1.send(item)

# How to terminate?
```

- [ ] A) Do nothing, Python cleans up automatically
- [ ] B) Call `close()` on the entry point only
- [ ] C) Call `close()` on all stages from entry to sink
- [ ] D) Send a special "STOP" value

---


---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Generators produce data (pull), coroutines consume data (push) |
| 2 | B | It raises a `TypeError` - must prime with next() first |
| 3 | B | 10 - yield returns total, then receives value |
| 4 | B | Build backward from sink to source |
| 5 | B | @coroutine decorator automatically primes the coroutine |
| 6 | B | Push model (coroutines) is better for infinite/streaming data |
| 7 | B | The coroutine's `except GeneratorExit` block is executed |
| 8 | B | Tee sends each item to all targets (broadcast) |
| 9 | B | Coroutines maintain local variables across calls |
| 10 | B | 10, 20 - each send returns what was yielded |
| 11 | B | Use try/except around `target.send()` |
| 12 | B | Coroutine pipeline processes one item at a time, less memory |
| 13 | B | x = 100, result1 = 42, result2 = 100 |
| 14 | C | Batch/Window pattern processes items in groups |
| 15 | C | Reversing a small list - coroutines need full data first |
| 16 | C | Test each stage individually first |
| 17 | C | Reducing function call overhead by combining simple stages |
| 18 | B | Traditional coroutines are synchronous, async supports concurrent I/O |
| 19 | C | Sends sliding windows of N consecutive items |
| 20 | C | Call close() on all stages from entry to sink |

## Scoring

- **0-10 correct:** Review the lecture material on coroutines
- **11-14 correct:** Good understanding, practice building pipelines
- **15-17 correct:** Strong grasp of concepts
- **18-20 correct:** Excellent! You've mastered coroutines

## Key Takeaways

If you remember nothing else, remember these:

1. **Coroutines consume data** via `send()`, unlike generators which produce data
2. **Always prime** coroutines with `next()` before `send()` (or use `@coroutine` decorator)
3. **Build backward** from sink to source
4. **Coroutines maintain state** naturally via local variables
5. **Use `tee` to broadcast** data to multiple consumers
6. **Close pipelines** properly to clean up resources
7. **Push model** is great for streaming/infinite data
8. **Pull model** (iterators) is better for finite sequences

