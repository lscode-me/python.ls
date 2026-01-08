# Testing in Python - Quiz

Test your knowledge of Python testing fundamentals, pytest, and best practices.

---

## Question 1: Testing Fundamentals

What is the primary purpose of writing tests?

A) To make the code run faster  
B) To ensure code works correctly and prevent regressions  
C) To satisfy project requirements  
D) To make the code more complex  

---

## Question 2: unittest vs pytest

Which statement is TRUE about pytest compared to unittest?

A) pytest requires test classes for all tests  
B) pytest uses `assert` statements instead of `self.assertEqual()`  
C) pytest is slower than unittest  
D) pytest cannot run unittest tests  

---

## Question 3: Test Naming

Which test name follows best practices?

A) `test1()`  
B) `test_stuff()`  
C) `test_user_registration_with_valid_email()`  
D) `testUserReg()`  

---

## Question 4: Fixtures

What is the purpose of pytest fixtures?

A) To fix broken tests  
B) To provide reusable test data and setup/teardown  
C) To make tests run faster  
D) To skip failing tests  

---

## Question 5: AAA Pattern

What does AAA stand for in testing?

A) Assert, Arrange, Act  
B) Arrange, Act, Assert  
C) Act, Assert, Arrange  
D) Arrange, Assert, Act  

---

## Question 6: Parametrization

What is the benefit of parametrized tests?

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

A) Tests run in parallel  
B) Tests multiple inputs without code duplication  
C) Tests run faster  
D) Tests are skipped automatically  

---

## Question 7: Mocking

When should you use mocking in tests?

A) Always, for every test  
B) Never, it makes tests unreliable  
C) When testing code with external dependencies (API, database)  
D) Only for slow tests  

---

## Question 8: Test Coverage

What does 100% test coverage guarantee?

A) The code has no bugs  
B) The code is production-ready  
C) All lines of code were executed during tests  
D) The code is well-designed  

---

## Question 9: TDD Cycle

What is the correct TDD cycle?

A) Write code → Write tests → Refactor  
B) Red → Green → Refactor  
C) Test → Debug → Deploy  
D) Design → Code → Test  

---

## Question 10: Exception Testing

Which is the correct way to test exceptions in pytest?

A) `assert raises(ValueError)`  
B) `with pytest.raises(ValueError):`  
C) `expect(ValueError)`  
D) `assertRaises(ValueError)`  

---

## Question 11: Fixture Scope

What does `@pytest.fixture(scope="module")` mean?

A) Fixture runs for each test function  
B) Fixture runs once per test file/module  
C) Fixture runs once per test session  
D) Fixture runs once per test class  

---

## Question 12: Test Independence

Why should tests be independent of each other?

A) To run faster  
B) To avoid test order dependencies and flaky tests  
C) To use less memory  
D) To satisfy coding standards  

---

## Question 13: Testing Best Practices

Which is a testing anti-pattern?

A) Testing public interfaces  
B) Using fixtures for common setup  
C) Testing implementation details (private methods)  
D) Using descriptive test names  

---

## Question 14: setUp vs Fixtures

What's the main advantage of pytest fixtures over unittest's setUp/tearDown?

A) Fixtures are faster  
B) Fixtures are reusable and composable  
C) Fixtures run automatically  
D) Fixtures don't require imports  

---

## Question 15: Integration vs Unit Tests

What's the main difference?

A) Integration tests are faster  
B) Unit tests test multiple components together  
C) Unit tests test components in isolation  
D) Integration tests don't need assertions  

---

## Question 16: Mock Assertions

What does `mock.assert_called_once_with(42)` verify?

A) The mock was called at least once  
B) The mock was called exactly once with argument 42  
C) The mock returns 42  
D) The mock was never called  

---

## Question 17: Test Organization

What's the recommended test file structure?

A) All tests in one file  
B) Mirror the source code structure  
C) Random organization  
D) Group by developer  

---

## Question 18: Continuous Integration

What's the benefit of running tests in CI?

A) Tests run faster  
B) Automatically catch bugs before merging  
C) Fewer tests needed  
D) Code becomes simpler  

---

## Question 19: Edge Cases

Which should be tested as edge cases?

A) Only happy path scenarios  
B) Empty inputs, None, zero, negative numbers  
C) Only the most common use cases  
D) Random values  

---

## Question 20: Test Readability

What makes a test readable?

A) Short variable names  
B) Many comments  
C) Clear AAA structure and descriptive names  
D) Complex logic  

---

## Question 21: Property-Based Testing

What library is used for property-based testing in Python?

A) pytest-properties  
B) Hypothesis  
C) QuickCheck  
D) PropTest  

---

## Question 22: Test Doubles

What's the difference between a mock and a stub?

A) No difference, same thing  
B) Mocks verify interactions, stubs provide data  
C) Stubs are faster  
D) Mocks are only for databases  

---

## Question 23: Coverage Pitfall

Why is 100% coverage not always the goal?

A) It's impossible to achieve  
B) Diminishing returns; focus on critical code  
C) Tests become too slow  
D) Coverage tools are unreliable  

---

---

# ANSWERS

## Question 1: Testing Fundamentals

**Correct Answer: B) To ensure code works correctly and prevent regressions**

Tests verify behavior, catch bugs early, and give confidence when refactoring. They serve as documentation and help maintain code quality over time.

---

## Question 2: unittest vs pytest

**Correct Answer: B) pytest uses `assert` statements instead of `self.assertEqual()`**

pytest allows simple `assert` statements and doesn't require test classes. It's more Pythonic and easier to write than unittest, which requires special assertion methods.

---

## Question 3: Test Naming

**Correct Answer: C) `test_user_registration_with_valid_email()`**

Descriptive test names should explain what is being tested and under what conditions. This makes it easy to understand what failed when a test breaks.

---

## Question 4: Fixtures

**Correct Answer: B) To provide reusable test data and setup/teardown**

Fixtures are functions that provide data, objects, or setup needed by tests, promoting code reuse and reducing duplication across tests.

---

## Question 5: AAA Pattern

**Correct Answer: B) Arrange, Act, Assert**

The AAA pattern structures tests clearly:
1. **Arrange** - set up test data
2. **Act** - execute the code being tested
3. **Assert** - verify the results

---

## Question 6: Parametrization

**Correct Answer: B) Tests multiple inputs without code duplication**

Parametrization allows testing multiple scenarios with a single test function, reducing code duplication and making it easy to add new test cases.

---

## Question 7: Mocking

**Correct Answer: C) When testing code with external dependencies (API, database)**

Mocking isolates the code under test from external dependencies, making tests fast, reliable, and independent of external services.

---

## Question 8: Test Coverage

**Correct Answer: C) All lines of code were executed during tests**

Coverage measures which lines ran during tests, but doesn't guarantee correctness, quality, or that all edge cases are tested. High coverage is good, but not sufficient on its own.

---

## Question 9: TDD Cycle

**Correct Answer: B) Red → Green → Refactor**

The TDD cycle is:
1. **Red** - Write a failing test
2. **Green** - Write minimal code to pass
3. **Refactor** - Improve code while keeping tests passing

---

## Question 10: Exception Testing

**Correct Answer: B) `with pytest.raises(ValueError):`**

Example:
```python
with pytest.raises(ValueError):
    function_that_should_raise()
```

This is the pytest way to verify that code raises the expected exception.

---

## Question 11: Fixture Scope

**Correct Answer: B) Fixture runs once per test file/module**

Fixture scopes:
- `function` (default) - runs for each test function
- `class` - runs once per test class
- `module` - runs once per test file/module
- `session` - runs once for entire test session

---

## Question 12: Test Independence

**Correct Answer: B) To avoid test order dependencies and flaky tests**

Independent tests can run in any order and won't fail due to shared state. This prevents "flaky" tests that sometimes pass and sometimes fail.

---

## Question 13: Testing Best Practices

**Correct Answer: C) Testing implementation details (private methods)**

Test behavior, not implementation. Tests should verify public interfaces and survive refactoring. Testing private methods couples tests to implementation details.

---

## Question 14: setUp vs Fixtures

**Correct Answer: B) Fixtures are reusable and composable**

Fixtures can be:
- Shared across test files
- Depend on other fixtures
- Have different scopes
- Selectively used by tests

This makes them more flexible than setUp/tearDown methods.

---

## Question 15: Integration vs Unit Tests

**Correct Answer: C) Unit tests test components in isolation**

- **Unit tests**: test single functions/classes in isolation
- **Integration tests**: test multiple components working together

---

## Question 16: Mock Assertions

**Correct Answer: B) The mock was called exactly once with argument 42**

This assertion verifies both the number of calls (exactly one) and the arguments passed (42).

---

## Question 17: Test Organization

**Correct Answer: B) Mirror the source code structure**

Recommended structure:
```
src/
  calculator.py
  utils.py
tests/
  test_calculator.py
  test_utils.py
```

This makes it easy to find tests for any source file.

---

## Question 18: Continuous Integration

**Correct Answer: B) Automatically catch bugs before merging**

CI runs tests on every commit/PR, catching issues early and preventing broken code from being merged into the main branch.

---

## Question 19: Edge Cases

**Correct Answer: B) Empty inputs, None, zero, negative numbers**

Edge cases often reveal bugs that normal inputs don't. Common edge cases include:
- Empty collections
- None/null values
- Zero
- Negative numbers
- Boundary values (min/max)

---

## Question 20: Test Readability

**Correct Answer: C) Clear AAA structure and descriptive names**

Tests should be self-documenting with:
- Clear setup (Arrange)
- Obvious action (Act)
- Explicit verification (Assert)
- Descriptive test names

---

## Question 21: Property-Based Testing

**Correct Answer: B) Hypothesis**

Hypothesis is the main property-based testing library for Python. It generates random test data to find edge cases you might not think of.

---

## Question 22: Test Doubles

**Correct Answer: B) Mocks verify interactions, stubs provide data**

- **Mock**: verifies behavior (was method called? with what arguments?)
- **Stub**: provides predetermined responses (returns fixed data)
- Both are "test doubles" but serve different purposes

---

## Question 23: Coverage Pitfall

**Correct Answer: B) Diminishing returns; focus on critical code**

100% coverage doesn't guarantee quality or bug-free code. It's better to focus on:
- Critical business logic (high coverage)
- Edge cases and error handling
- Meaningful assertions

Trivial code (getters, setters) doesn't need 100% coverage.

---

## Scoring

- **21-23 correct**: Excellent! You understand testing well.
- **18-20 correct**: Good! Review a few concepts.
- **15-17 correct**: Fair. More practice needed.
- **Below 15**: Keep learning! Review the lecture material.

Good luck! 🧪

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | To ensure code works correctly and prevent regressions |
| 2 | B | pytest uses `assert` statements instead of `self.assertEqual()` |
| 3 | C | `test_user_registration_with_valid_email()` follows best practices |
| 4 | B | To provide reusable test data and setup/teardown |
| 5 | B | Arrange, Act, Assert |
| 6 | B | Tests multiple inputs without code duplication |
| 7 | C | When testing code with external dependencies (API, database) |
| 8 | C | All lines of code were executed during tests |
| 9 | B | Red → Green → Refactor |
| 10 | B | `with pytest.raises(ValueError):` |
| 11 | B | Fixture runs once per test file/module |
| 12 | B | To avoid test order dependencies and flaky tests |
| 13 | C | Testing implementation details (private methods) |
| 14 | B | Fixtures are reusable and composable |
| 15 | C | Unit tests test components in isolation |
| 16 | B | The mock was called exactly once with argument 42 |
| 17 | B | Mirror the source code structure |
| 18 | B | Automatically catch bugs before merging |
| 19 | B | Empty inputs, None, zero, negative numbers |
| 20 | C | Clear AAA structure and descriptive names |
| 21 | B | Hypothesis |
| 22 | B | Mocks verify interactions, stubs provide data |
| 23 | B | Diminishing returns; focus on critical code |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **20-23 correct (87-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **16-19 correct (70-83%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **12-15 correct (52-65%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 12 correct (<52%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
