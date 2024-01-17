# Part 14: Comprehensive Testing in Python with pytest

# Install pytest: pip install pytest

# Code to be Tested
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Tests using pytest
import pytest

# 1. Basic Tests


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# 2. Parameterized Tests

@pytest.mark.parametrize("input_a, input_b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add_parameterized(input_a, input_b, expected):
    assert add(input_a, input_b) == expected


# 3. Fixtures

@pytest.fixture
def sample_data():
    data = {'a': 5, 'b': 2}
    return data


def test_add_with_fixture(sample_data):
    result = add(sample_data['a'], sample_data['b'])
    assert result == 7


# 4. Marking Tests

@pytest.mark.slow
def test_slow_add():
    # Simulate a slow test
    import time
    time.sleep(2)
    assert add(2, 2) == 4


# 5. Skipping Tests

@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    assert False


# 6. Expected Failures

@pytest.mark.xfail
def test_expected_failure():
    assert divide(5, 0)  # This test is expected to fail, but we want to track it

# Run tests: Execute this script in the terminal with 'pytest filename.py'
# Or use 'python -m pytest filename.py'
