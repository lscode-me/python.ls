# Testing in Python
## Writing Reliable Code with pytest, unittest, and TDD

---

## 1. Why Testing Matters

Testing is not optional — it's a fundamental skill for professional development.

### Benefits of Testing

- **Confidence**: Refactor without fear of breaking things
- **Documentation**: Tests show how code should be used
- **Design**: Writing testable code leads to better architecture
- **Debugging**: Catch bugs before they reach production
- **Maintenance**: Changes are safer with test coverage

### Types of Tests

```python
# Unit Test - tests a single function/method in isolation
def test_add():
    assert add(2, 3) == 5

# Integration Test - tests multiple components together
def test_user_registration():
    user = create_user("alice@example.com")
    saved_user = database.get_user(user.id)
    assert saved_user.email == "alice@example.com"

# End-to-End Test - tests complete workflow
def test_checkout_flow():
    # Add item to cart, proceed to checkout, complete payment
    pass
```

---

## 2. Python's Built-in unittest

### Basic Test Structure

```python
import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
```

### Common Assertions

```python
class TestAssertions(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1, 2)
    
    def test_truthiness(self):
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_membership(self):
        self.assertIn('a', 'abc')
        self.assertNotIn('d', 'abc')
    
    def test_type(self):
        self.assertIsInstance(42, int)
        self.assertIsNone(None)
    
    def test_exceptions(self):
        with self.assertRaises(ValueError):
            int('not a number')
    
    def test_approximation(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)
```

### setUp and tearDown

```python
class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Run before each test"""
        self.db = Database()
        self.db.connect()
    
    def tearDown(self):
        """Run after each test"""
        self.db.disconnect()
    
    def test_insert(self):
        self.db.insert("user", {"name": "Alice"})
        self.assertEqual(self.db.count("user"), 1)
    
    def test_delete(self):
        self.db.insert("user", {"name": "Bob"})
        self.db.delete("user", {"name": "Bob"})
        self.assertEqual(self.db.count("user"), 0)
```

---

## 3. pytest - Modern Python Testing

### Why pytest?

- Simpler syntax (no classes required)
- Better output and error messages
- Powerful fixtures
- Parametrization
- Plugin ecosystem

### Installation

```bash
pip install pytest
```

### Basic pytest Tests

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(10, 0) == 10
```

Run tests:
```bash
pytest test_math.py
pytest -v  # verbose
pytest -k "test_add"  # run tests matching pattern
```

### Advanced Assertions

```python
# test_advanced.py

def test_string_contains():
    result = "hello world"
    assert "world" in result
    assert result.startswith("hello")

def test_list_operations():
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert 3 in numbers
    assert numbers[0] == 1

def test_dict_operations():
    user = {"name": "Alice", "age": 30}
    assert user["name"] == "Alice"
    assert "age" in user

def test_exceptions():
    import pytest
    
    with pytest.raises(ZeroDivisionError):
        1 / 0
    
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")
```

---

## 4. Fixtures - Reusable Test Data

### Basic Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    """Provides test data"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5
```

### Fixture Scope

```python
@pytest.fixture(scope="function")  # default - runs for each test
def function_fixture():
    return "created for each test"

@pytest.fixture(scope="module")  # runs once per module
def module_fixture():
    db = Database()
    db.connect()
    yield db  # provide to tests
    db.disconnect()  # cleanup

@pytest.fixture(scope="session")  # runs once per test session
def session_fixture():
    return "created once for all tests"
```

### Setup and Teardown with Fixtures

```python
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    # Setup
    fd, path = tempfile.mkstemp()
    
    # Provide to test
    yield path
    
    # Teardown
    os.close(fd)
    os.remove(path)

def test_file_operations(temp_file):
    with open(temp_file, 'w') as f:
        f.write("test data")
    
    with open(temp_file, 'r') as f:
        assert f.read() == "test data"
```

### Fixture Dependencies

```python
@pytest.fixture
def database():
    db = Database()
    db.connect()
    yield db
    db.disconnect()

@pytest.fixture
def user(database):
    """Fixture that depends on database fixture"""
    user = database.create_user("alice@example.com")
    yield user
    database.delete_user(user.id)

def test_user_email(user):
    assert "@" in user.email
```

---

## 5. Parametrized Tests

### Basic Parametrization

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 5, 15),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Multiple Parameters

```python
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

### Parametrizing Fixtures

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number_squared(number):
    result = number ** 2
    assert result > 0
```

---

## 6. Mocking and Patching

### Why Mock?

- Test in isolation without external dependencies
- Avoid slow operations (network, database)
- Control test conditions

### Using unittest.mock

```python
from unittest.mock import Mock, patch

# Mock object
def test_with_mock():
    mock_db = Mock()
    mock_db.get_user.return_value = {"name": "Alice"}
    
    result = mock_db.get_user(1)
    assert result["name"] == "Alice"
    mock_db.get_user.assert_called_once_with(1)

# Patching functions
@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "test"}
    
    response = requests.get("https://api.example.com")
    assert response.status_code == 200
    assert response.json()["data"] == "test"
```

### pytest-mock Plugin

```bash
pip install pytest-mock
```

```python
def test_with_mocker(mocker):
    # Mock a function
    mock = mocker.patch('module.function')
    mock.return_value = 42
    
    result = module.function()
    assert result == 42

def test_api(mocker):
    # Mock external API
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"users": []}
    
    mocker.patch('requests.get', return_value=mock_response)
    
    result = get_users_from_api()
    assert result == []
```

---

## 7. Testing Exceptions and Edge Cases

### Testing Exceptions

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    
    assert "Cannot divide by zero" in str(exc_info.value)

def test_divide_normal():
    assert divide(10, 2) == 5
```

### Testing Edge Cases

```python
def process_list(items):
    if not items:
        return []
    return [x * 2 for x in items]

def test_empty_list():
    assert process_list([]) == []

def test_single_item():
    assert process_list([5]) == [10]

def test_multiple_items():
    assert process_list([1, 2, 3]) == [2, 4, 6]

def test_negative_numbers():
    assert process_list([-1, -2]) == [-2, -4]
```

---

## 8. Test Organization and Best Practices

### Project Structure

```
project/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_utils.py
├── pytest.ini
└── setup.py
```

### Naming Conventions

```python
# Good test names
def test_user_registration_with_valid_email():
    pass

def test_user_registration_fails_with_invalid_email():
    pass

def test_calculate_total_price_with_discount():
    pass

# Bad test names
def test1():
    pass

def test_stuff():
    pass
```

### AAA Pattern: Arrange, Act, Assert

```python
def test_user_creation():
    # Arrange - setup test data
    email = "alice@example.com"
    name = "Alice"
    
    # Act - perform the action
    user = User(email=email, name=name)
    
    # Assert - verify the result
    assert user.email == email
    assert user.name == name
```

### One Assert Per Test (guideline)

```python
# Good - focused tests
def test_user_email():
    user = User("alice@example.com")
    assert user.email == "alice@example.com"

def test_user_has_id():
    user = User("alice@example.com")
    assert user.id is not None

# Acceptable - related assertions
def test_user_initialization():
    user = User("alice@example.com", "Alice")
    assert user.email == "alice@example.com"
    assert user.name == "Alice"
```

---

## 9. Test Coverage

### Installing coverage.py

```bash
pip install pytest-cov
```

### Running with Coverage

```bash
# Run tests with coverage
pytest --cov=src tests/

# Generate HTML report
pytest --cov=src --cov-report=html tests/

# Show missing lines
pytest --cov=src --cov-report=term-missing tests/
```

### Coverage Configuration

```ini
# .coveragerc or pyproject.toml
[run]
source = src
omit = 
    */tests/*
    */venv/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
    if __name__ == .__main__.:
```

### Coverage Goals

- **80%+ is good** for most projects
- **100% is not always necessary** (diminishing returns)
- Focus on critical business logic
- Don't test trivial code just for coverage

---

## 10. Test-Driven Development (TDD)

### The TDD Cycle: Red → Green → Refactor

```python
# 1. RED - Write a failing test
def test_multiply():
    assert multiply(3, 4) == 12

# Run: pytest - FAILS (multiply doesn't exist)

# 2. GREEN - Write minimal code to pass
def multiply(a, b):
    return a * b

# Run: pytest - PASSES

# 3. REFACTOR - Improve code (optional)
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

# Run: pytest - STILL PASSES
```

### TDD Example: Building a Shopping Cart

```python
# Step 1: Test
def test_empty_cart():
    cart = ShoppingCart()
    assert cart.total() == 0

# Step 2: Implementation
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def total(self):
        return 0

# Step 3: Next test
def test_add_item():
    cart = ShoppingCart()
    cart.add_item("Book", 10.99)
    assert cart.total() == 10.99

# Step 4: Expand implementation
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
    
    def total(self):
        return sum(item["price"] for item in self.items)
```

---

## 11. Continuous Integration with Tests

### GitHub Actions Example

```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: pytest --cov=src tests/
    
    - name: Upload coverage
      uses: codecov/codecov-action@v2
```

---

## 12. Advanced Testing Patterns

### Testing with Temporary Files

```python
import tempfile
import os

def test_file_processing():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test file
        test_file = os.path.join(tmpdir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("test data")
        
        # Test your function
        result = process_file(test_file)
        assert result == "expected"
        
        # tmpdir is automatically cleaned up
```

### Testing Async Code

```python
import pytest
import asyncio

async def fetch_data():
    await asyncio.sleep(0.1)
    return "data"

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == "data"
```

### Doctest - Tests in Docstrings

```python
def add(a, b):
    """
    Add two numbers.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b

# Run with: python -m doctest module.py
# Or with pytest: pytest --doctest-modules
```

---

## 13. Common Testing Mistakes

### ❌ Testing Implementation Details

```python
# Bad - tests internal implementation
def test_user_dict_structure():
    user = User("alice@example.com")
    assert user._data["email"] == "alice@example.com"

# Good - tests public interface
def test_user_email():
    user = User("alice@example.com")
    assert user.email == "alice@example.com"
```

### ❌ Tests That Depend on External State

```python
# Bad - depends on real database
def test_get_user():
    user = database.get_user(1)  # What if user doesn't exist?
    assert user.name == "Alice"

# Good - uses fixtures or mocks
def test_get_user(mock_database):
    mock_database.get_user.return_value = User(name="Alice")
    user = mock_database.get_user(1)
    assert user.name == "Alice"
```

### ❌ Tests That Are Too Broad

```python
# Bad - tests too many things
def test_entire_application():
    # 100 lines of test code
    pass

# Good - focused tests
def test_user_registration():
    # Test one specific thing
    pass

def test_user_login():
    # Test another specific thing
    pass
```

---

## 14. Testing Real-World Scenarios

### Testing File I/O

```python
def test_read_csv():
    csv_content = "name,age\nAlice,30\nBob,25"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(csv_content)
        temp_path = f.name
    
    try:
        users = read_users_from_csv(temp_path)
        assert len(users) == 2
        assert users[0]["name"] == "Alice"
    finally:
        os.unlink(temp_path)
```

### Testing HTTP Requests

```python
import responses

@responses.activate
def test_api_call():
    responses.add(
        responses.GET,
        'https://api.example.com/users',
        json={'users': [{'name': 'Alice'}]},
        status=200
    )
    
    result = get_users()
    assert len(result) == 1
    assert result[0]['name'] == 'Alice'
```

### Testing Command-Line Scripts

```python
from click.testing import CliRunner

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Alice'])
    
    assert result.exit_code == 0
    assert 'Hello Alice' in result.output
```

---

## Summary

Key takeaways:

1. **Testing is Essential** - Not optional for professional development
2. **pytest is Recommended** - More powerful and easier than unittest
3. **Use Fixtures** - DRY principle for test data
4. **Mock External Dependencies** - Tests should be fast and reliable
5. **Test Edge Cases** - Empty inputs, None, negative numbers, etc.
6. **Follow TDD** - Write tests first when possible
7. **Measure Coverage** - Aim for 80%+ on critical code
8. **Keep Tests Fast** - Slow tests won't be run
9. **Test Behavior, Not Implementation** - Tests should survive refactoring
10. **CI/CD Integration** - Automate test running

### Next Steps

- Practice writing tests for existing code
- Try TDD for new features
- Set up CI/CD pipeline
- Explore pytest plugins (pytest-django, pytest-asyncio, etc.)
- Learn about property-based testing (Hypothesis)

---

## Resources

- pytest documentation: https://docs.pytest.org/
- unittest documentation: https://docs.python.org/3/library/unittest.html
- Test-Driven Development with Python: https://www.obeythetestinggoat.com/
- Python Testing with pytest (book) by Brian Okken

