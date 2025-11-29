# Testing in Python - Homework Assignments


## Assignment 1: Basic Unit Tests ⭐

Create a module `calculator.py` with basic math functions and write comprehensive tests.

**Requirements:**
- Implement functions: `add()`, `subtract()`, `multiply()`, `divide()`
- Create `test_calculator.py` with pytest
- Test normal cases, edge cases, and error cases
- Handle division by zero with appropriate exception

**Example:**
```python
# calculator.py
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_calculator.py
import pytest
from calculator import divide

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

**Your goal:**
- Master basic pytest syntax
- Understand assertion patterns
- Learn exception testing

---

## Assignment 2: Fixtures and Setup ⭐⭐

Create a `StringProcessor` class and test it using fixtures.

**Requirements:**
- Class with methods: `reverse()`, `capitalize()`, `count_words()`, `remove_spaces()`
- Use fixtures to provide test data
- Test with different scope (function, module)
- Implement setup and teardown

**Example:**
```python
@pytest.fixture
def processor():
    return StringProcessor()

@pytest.fixture
def sample_texts():
    return [
        "hello world",
        "Python Testing",
        "  spaces  everywhere  "
    ]

def test_reverse(processor):
    assert processor.reverse("abc") == "cba"
```

**Your goal:**
- Master pytest fixtures
- Understand fixture scope
- Learn to reuse test data

---

## Assignment 3: Parametrized Tests ⭐⭐

Test a `validate_email()` function with multiple test cases.

**Requirements:**
- Implement email validation function
- Use `@pytest.mark.parametrize` for multiple test cases
- Test valid emails: `user@domain.com`, `user.name@sub.domain.co.uk`
- Test invalid emails: `invalid`, `@domain.com`, `user@`, `user domain.com`

**Example:**
```python
@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("invalid-email", False),
    ("user@", False),
    ("@domain.com", False),
    ("user.name+tag@example.co.uk", True),
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected
```

**Your goal:**
- Master parametrized tests
- Reduce code duplication
- Test multiple scenarios efficiently

---

## Assignment 4: Testing with Files ⭐⭐⭐

Create a CSV processor and test file operations.

**Requirements:**
- Implement `CSVProcessor` class
- Methods: `read_csv()`, `write_csv()`, `filter_rows()`, `get_column()`
- Use `tempfile` for test files
- Test with various CSV formats
- Handle missing files, empty files, malformed CSV

**Example:**
```python
import tempfile
import os

@pytest.fixture
def temp_csv():
    content = "name,age\nAlice,30\nBob,25"
    fd, path = tempfile.mkstemp(suffix='.csv')
    with open(path, 'w') as f:
        f.write(content)
    yield path
    os.close(fd)
    os.remove(path)

def test_read_csv(temp_csv):
    processor = CSVProcessor()
    data = processor.read_csv(temp_csv)
    assert len(data) == 2
```

**Your goal:**
- Test file I/O operations
- Use temporary files properly
- Handle cleanup with fixtures

---

## Assignment 5: Mocking External Dependencies ⭐⭐⭐

Test a weather API client without making real API calls.

**Requirements:**
- Create `WeatherAPI` class with method `get_temperature(city)`
- Mock HTTP requests using `unittest.mock` or `pytest-mock`
- Test successful API response
- Test API errors (404, 500, timeout)
- Verify API is called with correct parameters

**Example:**
```python
from unittest.mock import Mock, patch

@patch('requests.get')
def test_get_temperature(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"temp": 25}
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    api = WeatherAPI()
    temp = api.get_temperature("London")
    
    assert temp == 25
    mock_get.assert_called_once()
```

**Your goal:**
- Master mocking and patching
- Test without external dependencies
- Verify function calls and arguments

---

## Assignment 6: Test-Driven Development (TDD) ⭐⭐⭐

Build a shopping cart using TDD methodology.

**Requirements:**
- Start by writing tests FIRST
- Implement `ShoppingCart` class with TDD
- Methods: `add_item()`, `remove_item()`, `get_total()`, `apply_discount()`, `clear()`
- Follow Red → Green → Refactor cycle
- Document each TDD iteration

**TDD Steps:**
```python
# Step 1: Write failing test
def test_empty_cart_total():
    cart = ShoppingCart()
    assert cart.get_total() == 0

# Step 2: Minimal implementation to pass
class ShoppingCart:
    def get_total(self):
        return 0

# Step 3: Refactor (if needed)
# Step 4: Next test
def test_add_single_item():
    cart = ShoppingCart()
    cart.add_item("Book", 10.99)
    assert cart.get_total() == 10.99

# Continue...
```

**Your goal:**
- Practice TDD workflow
- Write tests before code
- Experience benefits of TDD

---

## Assignment 7: Testing a User Authentication System ⭐⭐⭐⭐

Create and test a complete user authentication system.

**Requirements:**
- Implement `UserAuth` class
- Methods: `register()`, `login()`, `logout()`, `reset_password()`
- Hash passwords (use `hashlib`)
- Mock database operations
- Test successful and failed scenarios
- Test security: password strength, SQL injection attempts

**Test scenarios:**
- Successful registration
- Registration with existing email
- Login with correct credentials
- Login with wrong password
- Password hashing (never store plaintext)
- Password reset workflow

**Example:**
```python
@pytest.fixture
def mock_db(mocker):
    return mocker.Mock()

def test_register_new_user(mock_db):
    auth = UserAuth(mock_db)
    result = auth.register("alice@example.com", "SecurePass123!")
    
    assert result.success is True
    mock_db.save_user.assert_called_once()
    
    # Verify password is hashed
    saved_user = mock_db.save_user.call_args[0][0]
    assert saved_user.password != "SecurePass123!"
```

**Your goal:**
- Test complex business logic
- Mock database dependencies
- Test security requirements
- Handle multiple test scenarios

---

## Assignment 8: Coverage Analysis ⭐⭐⭐

Achieve 100% test coverage for a data processing module.

**Requirements:**
- Implement `DataProcessor` module with 5+ functions
- Write comprehensive tests
- Run coverage analysis with `pytest-cov`
- Achieve 100% coverage
- Generate HTML coverage report

**Functions to implement:**
- `clean_data()` - remove nulls, trim strings
- `transform_data()` - apply transformations
- `validate_schema()` - check data structure
- `aggregate_data()` - group and summarize
- `export_data()` - save to file

**Commands:**
```bash
pytest --cov=data_processor tests/
pytest --cov=data_processor --cov-report=html tests/
```

**Your goal:**
- Achieve high test coverage
- Identify untested code paths
- Understand coverage metrics
- Write thorough test suites

---

## Assignment 9: Integration Testing ⭐⭐⭐⭐

Test a complete ETL (Extract-Transform-Load) pipeline.

**Requirements:**
- Create pipeline: CSV → Process → Database
- Test each component individually (unit tests)
- Test components together (integration tests)
- Mock external resources (files, database)
- Test error handling at each stage

**Pipeline stages:**
1. Extract: Read data from CSV
2. Transform: Clean, validate, enrich data
3. Load: Save to database

**Example:**
```python
class TestETLPipeline:
    @pytest.fixture
    def pipeline(self, tmp_path, mock_db):
        return ETLPipeline(
            input_path=tmp_path / "input.csv",
            database=mock_db
        )
    
    def test_end_to_end(self, pipeline, tmp_path):
        # Create test CSV
        csv_file = tmp_path / "input.csv"
        csv_file.write_text("name,age\nAlice,30")
        
        # Run pipeline
        result = pipeline.run()
        
        # Verify results
        assert result.records_processed == 1
        assert result.errors == 0
```

**Your goal:**
- Test integration between components
- Handle complex test scenarios
- Mock multiple dependencies
- Test complete workflows

---

## Assignment 10: Advanced Testing - Property-Based Testing ⭐⭐⭐⭐⭐

Use Hypothesis library for property-based testing.

**Requirements:**
- Install `hypothesis`
- Test mathematical properties (commutativity, associativity)
- Test string processing with random inputs
- Test data structure invariants
- Find edge cases automatically

**Example:**
```python
from hypothesis import given
from hypothesis.strategies import integers, text

@given(integers(), integers())
def test_add_commutative(a, b):
    """Addition is commutative: a + b == b + a"""
    assert add(a, b) == add(b, a)

@given(integers(), integers(), integers())
def test_add_associative(a, b, c):
    """Addition is associative: (a+b)+c == a+(b+c)"""
    assert add(add(a, b), c) == add(a, add(b, c))

@given(text())
def test_reverse_twice(s):
    """Reversing twice returns original"""
    assert reverse(reverse(s)) == s
```

**Your goal:**
- Learn property-based testing
- Let computer find edge cases
- Test invariants and properties
- Discover bugs you didn't think of

---

## Assignment 11: Testing CLI Applications ⭐⭐⭐⭐

Test a command-line todo list application.

**Requirements:**
- Create CLI app with commands: `add`, `list`, `complete`, `delete`
- Use `click` or `argparse`
- Test with `click.testing.CliRunner`
- Test stdin/stdout
- Test exit codes
- Test with various command-line arguments

**Example:**
```python
from click.testing import CliRunner

def test_add_todo():
    runner = CliRunner()
    result = runner.invoke(cli, ['add', 'Buy milk'])
    
    assert result.exit_code == 0
    assert 'Added: Buy milk' in result.output

def test_list_todos():
    runner = CliRunner()
    runner.invoke(cli, ['add', 'Task 1'])
    runner.invoke(cli, ['add', 'Task 2'])
    
    result = runner.invoke(cli, ['list'])
    assert 'Task 1' in result.output
    assert 'Task 2' in result.output
```

**Your goal:**
- Test command-line interfaces
- Handle stdin/stdout testing
- Test exit codes
- Verify output formatting

---

## Assignment 12: Performance Testing ⭐⭐⭐⭐

Test that functions meet performance requirements.

**Requirements:**
- Implement sorting algorithm
- Test correctness (functional tests)
- Test performance (non-functional tests)
- Use `pytest-benchmark` or manual timing
- Set performance thresholds

**Example:**
```python
import time

def test_sort_large_list_performance():
    large_list = list(range(10000, 0, -1))
    
    start = time.time()
    result = quick_sort(large_list)
    duration = time.time() - start
    
    assert result == list(range(1, 10001))
    assert duration < 1.0, f"Took {duration}s, expected < 1s"

# Using pytest-benchmark
def test_sort_benchmark(benchmark):
    large_list = list(range(1000, 0, -1))
    result = benchmark(quick_sort, large_list)
    assert result == list(range(1, 1001))
```

**Your goal:**
- Test performance requirements
- Use benchmarking tools
- Set performance thresholds
- Profile slow tests

---

## Bonus Assignment: Build a Testing Framework ⭐⭐⭐⭐⭐

Create your own minimal testing framework to understand how pytest works.

**Requirements:**
- Discover test files and functions
- Run tests and collect results
- Report passes and failures
- Support basic assertions
- Support setup/teardown
- Colorful output

**Example usage:**
```python
# my_test_framework.py
class TestRunner:
    def discover_tests(self, path):
        """Find all test_*.py files"""
        pass
    
    def run_test(self, test_func):
        """Run single test function"""
        pass
    
    def report_results(self):
        """Print test results"""
        pass

# Usage
runner = TestRunner()
runner.discover_tests('tests/')
runner.run_all()
runner.report_results()
```

**Your goal:**
- Understand testing frameworks internals
- Practice meta-programming
- Gain deeper understanding of pytest
- Build something challenging and fun

---

## Grading Criteria

- ⭐ — Basic (required)
- ⭐⭐ — Intermediate (recommended)
- ⭐⭐⭐ — Advanced (for deeper understanding)
- ⭐⭐⭐⭐ — Expert (for ambitious learners)
- ⭐⭐⭐⭐⭐ — Master (creative and challenging)

**What we're evaluating:**
1. Test coverage (all cases covered)
2. Proper use of fixtures and parametrization
3. Appropriate mocking
4. Code organization and naming
5. Following TDD when requested
6. Clear and maintainable tests
7. Edge case handling

Good luck! Remember: good tests are as important as good code! 🧪

