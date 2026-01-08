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
| 4 | A | To provide reusable test data and setup/teardown |
| 5 | C | Arrange, Act, Assert |
| 6 | A | Tests multiple inputs without code duplication |
| 7 | D | When testing code with external dependencies (API, database) |
| 8 | D | All lines of code were executed during tests |
| 9 | A | Red → Green → Refactor |
| 10 | D | `with pytest.raises(ValueError):` |
| 11 | A | Fixture runs once per test file/module |
| 12 | A | To avoid test order dependencies and flaky tests |
| 13 | B | Testing implementation details (private methods) |
| 14 | C | Fixtures are reusable and composable |
| 15 | D | Unit tests test components in isolation |
| 16 | C | The mock was called exactly once with argument 42 |
| 17 | C | Mirror the source code structure |
| 18 | B | Automatically catch bugs before merging |
| 19 | B | Empty inputs, None, zero, negative numbers |
| 20 | C | Clear AAA structure and descriptive names |
| 21 | D | Hypothesis |
| 22 | B | Mocks verify interactions, stubs provide data |
| 23 | A | Diminishing returns; focus on critical code |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **20-23 correct (87-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **16-19 correct (70-83%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **12-15 correct (52-65%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 12 correct (<52%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
