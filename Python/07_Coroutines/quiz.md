# Quiz: Coroutines and Data Pipelines

## Question 1: Basic Concepts

What is the main difference between a generator and a coroutine?

- [ ] A) Generators are faster than coroutines
- [ ] B) Generators can only be used in Python 3
- [ ] C) Generators produce data (pull), coroutines consume data (push)
- [ ] D) Coroutines require the `async` keyword

<details>
<summary>Answer</summary>

**C) Generators produce data (pull), coroutines consume data (push)**

Generators use `yield` to produce values that are pulled by consumers using iteration. Coroutines use `yield` to receive values that are pushed by producers using `send()`.

</details>

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

<details>
<summary>Answer</summary>

**B) It raises a `TypeError`**

Error message: `TypeError: can't send non-None value to a just-started generator`

You must first prime the coroutine with `next(c)` or `c.send(None)` to advance it to the first `yield` statement.

</details>

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

<details>
<summary>Answer</summary>

**B) 10**

The expression `value = yield total` first yields `total` (which becomes the return value of `send()`), then receives the sent value. So:
1. `next(m)` returns 0 and pauses at yield
2. `m.send(10)` sends 10, adds it to total (now 10), loops back, and yields 10

</details>

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

<details>
<summary>Answer</summary>

**B) sink, then transform, then filter (backward from end)**

You build coroutine pipelines from the end (sink) to the beginning (source) because each stage needs a reference to the next stage to send data to.

```python
# Correct order:
sink = printer()
transform = map_items(func, sink)
filter = filter_items(predicate, transform)
# Now use 'filter' as entry point
```

</details>

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

<details>
<summary>Answer</summary>

**B) Automatically primes the coroutine**

The decorator calls `next(gen)` automatically, so you don't have to manually prime the coroutine before using `send()`.

</details>

---

## Question 6: Pull vs Push

Which statement about pull and push models is TRUE?

- [ ] A) Pull model is always faster than push model
- [ ] B) Push model (coroutines) is better for infinite/streaming data
- [ ] C) Pull model cannot handle real-time data
- [ ] D) Push model uses less memory

<details>
<summary>Answer</summary>

**B) Push model (coroutines) is better for infinite/streaming data**

Coroutines naturally handle streaming data where a producer pushes items as they become available. Pull model (iterators) is better for finite sequences where the consumer controls the pace.

</details>

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

<details>
<summary>Answer</summary>

**B) The coroutine's `except GeneratorExit` block is executed**

When you call `close()` on a coroutine, Python raises `GeneratorExit` inside the coroutine at the point where it's paused (at the `yield`). This allows you to perform cleanup.

</details>

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

<details>
<summary>Answer</summary>

**B) Sends each item to all targets (broadcast)**

The `tee` component broadcasts each received item to all target coroutines. Every target receives every item.

</details>

---

## Question 9: State Management

Why are coroutines well-suited for stateful processing?

- [ ] A) They use global variables efficiently
- [ ] B) They maintain local variables across calls
- [ ] C) They have special state management syntax
- [ ] D) They store state in a database

<details>
<summary>Answer</summary>

**B) They maintain local variables across calls**

Coroutines preserve their local variables between `send()` calls, making it natural to maintain state (counters, accumulators, windows, etc.) without external storage.

```python
@coroutine
def counter():
    count = 0  # This persists across sends
    while True:
        item = yield count
        count += 1
```

</details>

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

<details>
<summary>Answer</summary>

**B) 10, 20**

Flow:
1. `filter.send(5)` → passes (5 > 0) → transform doubles to 10 → prints 10
2. `filter.send(-3)` → blocked (-3 not > 0)
3. `filter.send(10)` → passes (10 > 0) → transform doubles to 20 → prints 20

</details>

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

<details>
<summary>Answer</summary>

**B) Use try/except around `target.send()`** (most common)

But **D) Use a separate error sink** is also valid for production systems.

```python
@coroutine
def safe_process(target, error_sink=None):
    while True:
        try:
            item = yield
            target.send(process(item))
        except Exception as e:
            if error_sink:
                error_sink.send({'item': item, 'error': str(e)})
```

</details>

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

<details>
<summary>Answer</summary>

**B) Approach B (coroutine pipeline)**

Approach A creates intermediate lists (`filtered` and `doubled`), storing all items in memory.

Approach B processes items one at a time, only storing one item in the pipeline at any moment. Much more memory efficient for large datasets.

</details>

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

<details>
<summary>Answer</summary>

**B) x = 100, result1 = 42, result2 = 100**

Execution flow:
1. `next(c)` → executes until first yield → returns 42 (result1)
2. `c.send(100)` → sends 100, which becomes the value of the yield expression → x = 100
3. Continues to next yield → returns x (which is 100) → result2 = 100

</details>

---

## Question 14: Pipeline Patterns

Which pipeline pattern is described here: "Collect items until a certain size is reached, then send the batch downstream"?

- [ ] A) Filter
- [ ] B) Map
- [ ] C) Batch/Window
- [ ] D) Tee

<details>
<summary>Answer</summary>

**C) Batch/Window**

```python
@coroutine
def batch(size, target):
    batch = []
    while True:
        item = yield
        batch.append(item)
        if len(batch) >= size:
            target.send(batch)
            batch = []
```

This pattern aggregates items into groups before processing.

</details>

---

## Question 15: Real-World Use Case

Which of these is NOT a good use case for coroutine pipelines?

- [ ] A) Real-time log processing
- [ ] B) Processing CSV files with millions of rows
- [ ] C) Reversing a small list
- [ ] D) ETL (Extract-Transform-Load) operations
- [ ] E) Streaming sensor data analysis

<details>
<summary>Answer</summary>

**C) Reversing a small list**

For simple operations on small, in-memory data structures, regular Python functions or list operations are simpler and more appropriate.

Coroutine pipelines excel at:
- Large datasets that don't fit in memory
- Streaming/infinite data
- Multi-stage transformations
- Real-time processing
- Broadcasting to multiple consumers

For a small list reversal, just use `list.reverse()` or `reversed()`!

</details>

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

<details>
<summary>Answer</summary>

**C) Test each stage individually first**

Best practice for pipeline debugging:
1. Test each component in isolation
2. Build pipeline incrementally (2 stages, then 3, etc.)
3. Use print/logging for intermediate results
4. Create a `debug_sink` that shows all received data

```python
@coroutine
def debug_sink(prefix="DEBUG"):
    while True:
        item = yield
        print(f"{prefix}: {item}")
```

Then progressively replace the final sink with earlier stages.

</details>

---

## Question 17: Performance

Which change would most improve the performance of a coroutine pipeline?

- [ ] A) Adding more stages
- [ ] B) Using `@coroutine` decorator
- [ ] C) Reducing function call overhead by combining simple stages
- [ ] D) Adding more error handling

<details>
<summary>Answer</summary>

**C) Reducing function call overhead by combining simple stages**

Each stage involves function calls and context switching. For performance-critical code:

```python
# Slow: Many small stages
filter1 = filter_items(lambda x: x > 0, ...)
filter2 = filter_items(lambda x: x < 100, ...)
mapper = map_items(lambda x: x * 2, ...)

# Faster: Combine related operations
@coroutine
def combined(target):
    while True:
        x = yield
        if 0 < x < 100:
            target.send(x * 2)
```

Trade-off: Less reusable but faster.

</details>

---

## Question 18: Async Coroutines

How do traditional coroutines (using `yield` and `send()`) differ from async coroutines (`async def`)?

- [ ] A) They are the same thing
- [ ] B) Traditional coroutines are synchronous, async coroutines support concurrent I/O
- [ ] C) Async coroutines are faster
- [ ] D) Traditional coroutines don't support `yield`

<details>
<summary>Answer</summary>

**B) Traditional coroutines are synchronous, async coroutines support concurrent I/O**

- **Traditional coroutines** (this lecture): Use `yield`/`send()` for data flow, execute synchronously
- **Async coroutines** (`async`/`await`): For concurrent I/O operations, different mechanism

They share the name "coroutine" but are different concepts:
- Traditional = data pipelines (this course)
- Async = concurrent programming (different course)

</details>

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

<details>
<summary>Answer</summary>

**C) Sends sliding windows of N consecutive items**

Example with size=3:
- Send: 1 → no output (window: [1])
- Send: 2 → no output (window: [1,2])
- Send: 3 → output [1,2,3]
- Send: 4 → output [2,3,4]
- Send: 5 → output [3,4,5]

Useful for moving averages, pattern detection, etc.

</details>

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

<details>
<summary>Answer</summary>

**C) Call `close()` on all stages from entry to sink** (best practice)

```python
stage1.close()  # This should close stage2 and sink

# Or explicitly:
try:
    stage1.close()
    stage2.close()
    sink.close()
except:
    pass
```

Better: Use a context manager:
```python
class Pipeline:
    def __init__(self, *stages):
        self.stages = stages
    
    def __exit__(self, *args):
        for stage in self.stages:
            stage.close()
```

</details>

---

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

