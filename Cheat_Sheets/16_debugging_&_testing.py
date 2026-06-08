# === Debugging & Testing ===


# ========== TABLE OF CONTENTS ==========
#
# 1. PRINT DEBUGGING (Quick & Dirty)
# 2. ASSERTIONS (Runtime Checks)
# 3. PYTEST (Testing Framework)
# 4. PYTEST ASSERT PATTERNS
# 5. PYTEST FIXTURES (Setup/Teardown)
# 6. PYTEST MARKS (Categorizing Tests)
# 7. VS CODE DEBUGGER (Interactive Debugging)
# 8. LOGGING (Professional Debug Output)
# 9. BUILT-IN DEBUGGER (pdb)
# 10. TEST STRUCTURE (AAA Pattern)
# 11. RUNNING TESTS COMMANDS
# 12. PYTEST CONFIGURATION (pytest.ini)
# 13. QUICK REFERENCE TABLE
#
# ========================================


# Debugging = finding and fixing errors in your code.
# Testing = writing code that checks if your code works correctly.


# ---------- 1. PRINT DEBUGGING (Quick & Dirty) ----------

# Definition: Inserting print() statements to see variable values and program flow.
# Use when: You need a fast, no-setup way to see what's happening.

# Example: Print variable values at key points
def calculate_total(prices):
    print(f"DEBUG: prices = {prices}")   # See input
    total = sum(prices)
    print(f"DEBUG: total = {total}")     # See result
    return total

# Print markers to trace execution
print(">>> Entering function")
# ... code ...
print("<<< Exiting function")

# Print variable types to debug type issues
value = "42"
print(f"Type of value: {type(value)}")  # <class 'str'>



# ---------- 2. ASSERTIONS (Runtime Checks) ----------

# Definition: Assertions test if a condition is True. If False, raises AssertionError.
# Use when: You want to catch impossible states during development.

def divide(a, b):
    assert b != 0, "Division by zero!"  # Stops program if b == 0
    return a / b

# Basic assertion
assert 2 + 2 == 4        # Silent (True)
# assert 2 + 2 == 5     # AssertionError

# Assert with custom message
x = -5
assert x > 0, f"x must be positive, got {x}"

# Common assertion patterns
assert len(my_list) > 0, "List is empty"
assert isinstance(value, int), "Value must be integer"
assert result == expected, f"Expected {expected}, got {result}"



# ---------- 3. PYTEST (Testing Framework) ----------

# Definition: A library that discovers and runs tests automatically.
# Install: pip install pytest

# File naming: test_*.py or *_test.py
# Each test is a function starting with "test_"

# Example test file: test_calculator.py
"""
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
"""

# Run tests: just type `pytest` in the terminal.



# ---------- 4. PYTEST ASSERT PATTERNS ----------

# Definition: Different ways to check expected behavior.

# Equality
assert result == expected

# Inequality
assert result != 0

# Truthy / Falsy
assert True
assert False is False
assert value is None

# Membership
assert item in my_list
assert item not in my_list

# Type checking
assert isinstance(value, int)

# Approximate equality for floats (use pytest.approx)
import pytest
assert 0.1 + 0.2 == pytest.approx(0.3)
assert 1.5 == pytest.approx(1.5, rel=0.01)  # relative tolerance

# Exception testing
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# Check exception message
with pytest.raises(ValueError, match="Invalid input"):
    validate_input(-1)



# ---------- 5. PYTEST FIXTURES (Setup/Teardown) ----------

# Definition: Fixtures provide reusable data or setup for tests.
# Use when: Multiple tests need the same preparation.

import pytest

@pytest.fixture
def sample_data():
    """Creates sample data before each test."""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5

# Fixture with cleanup (teardown)
@pytest.fixture
def temp_file():
    # Setup
    with open("temp.txt", "w") as f:
        f.write("test")
    yield                      # Test runs here
    # Teardown (runs after test)
    import os
    os.remove("temp.txt")



# ---------- 6. PYTEST MARKS (Categorizing Tests) ----------

# Definition: Marks let you tag tests for selective running or skipping.

# Mark as slow
@pytest.mark.slow
def test_heavy_computation():
    pass

# Skip test unconditionally
@pytest.mark.skip(reason="Not implemented yet")
def test_future():
    pass

# Skip if condition is true
import sys
@pytest.mark.skipif(sys.version_info < (3, 10), reason="Python 3.10+ required")
def test_new_feature():
    pass

# Expected failure (known bug)
@pytest.mark.xfail
def test_buggy_feature():
    pass

# Parametrize – run same test with different inputs
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected

# Multiple parameters
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected



# ---------- 7. VS CODE DEBUGGER (Interactive Debugging) ----------

# Definition: A graphical tool that lets you pause execution and inspect variables.
# Use when: You need to step through code line by line.

# How to use:
# 1. Click to the left of a line number → red dot (breakpoint)
# 2. Press F5 (Run → Start Debugging)
# 3. Use debug buttons:

# Debug buttons and their actions:
# - Continue (F5)      → Run to next breakpoint
# - Step Over (F10)    → Execute current line, move to next line
# - Step Into (F11)    → Go inside a function call
# - Step Out (Shift+F11) → Finish current function and return
# - Stop (Shift+F5)    → End debugging

# Debug panel shows:
# - Variables: current variable values
# - Watch: custom expressions you want to track
# - Call Stack: which functions called the current one
# - Breakpoints: list of all breakpoints



# ---------- 8. LOGGING (Professional Debug Output) ----------

# Definition: Logging records messages with severity levels, can write to file.
# Use when: You need persistent logs or different output levels.

import logging

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,                      # Show all messages at or above DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='debug.log',                     # Optional: write to file
    filemode='w'                              # 'w' overwrite, 'a' append
)

# Logging levels (increasing severity)
logging.debug("Detailed diagnostic info")     # Level 10
logging.info("General information")           # Level 20
logging.warning("Something unexpected")       # Level 30
logging.error("An error occurred")            # Level 40
logging.critical("Program may crash")         # Level 50

# Example with variable
name = "Alice"
logging.debug(f"Processing {name}")

# Conditional logging
if error_occurred:
    logging.error(f"Failed with value {x}")



# ---------- 9. BUILT-IN DEBUGGER (pdb) ----------

# Definition: Command-line debugger built into Python.
# Use when: You cannot use VS Code (e.g., on remote server).

import pdb

# Insert breakpoint
def buggy_function(x):
    result = x * 2
    pdb.set_trace()          # Execution stops here
    return result + 1

# Run script normally; pdb will activate at set_trace().

# pdb commands (type at (Pdb) prompt):
# - n (next)     → Execute next line
# - s (step)     → Step into function
# - c (continue) → Continue until next breakpoint
# - p var        → Print variable value
# - q (quit)     → Exit debugger
# - l (list)     → Show code around current line
# - h (help)     → Show all commands

# Alternative: Run script with pdb from the start:
# python -m pdb my_script.py



# ---------- 10. TEST STRUCTURE (AAA Pattern) ----------

# Definition: Arrange, Act, Assert – a standard pattern for organizing tests.
# - Arrange: Set up input and expected state
# - Act: Call the function being tested
# - Assert: Verify the result

def test_calculate_discount():
    # Arrange
    price = 100
    discount = 0.1
    # Act
    result = price * (1 - discount)
    # Assert
    assert result == 90

# Edge cases to always test
def test_edge_cases():
    # Empty input
    assert process([]) == []
    # Single item
    assert process([1]) == [1]
    # Negative numbers
    assert process([-1, -2]) == [-1, -2]
    # Large numbers
    assert process([10**6]) == [10**6]
    # Zero
    assert process([0]) == [0]



# ---------- 11. RUNNING TESTS COMMANDS ----------

# Command line examples (not Python code, but useful to know):

# Run all tests in current directory
# $ pytest

# Run tests in a specific file
# $ pytest test_calculator.py

# Run a specific test function
# $ pytest test_calculator.py::test_add

# Run with verbose output (shows test names)
# $ pytest -v

# Run with print statements shown
# $ pytest -s

# Run with coverage (requires pytest-cov)
# $ pytest --cov=calculator

# Run tests with a specific marker
# $ pytest -m slow

# Run tests in parallel (requires pytest-xdist)
# $ pytest -n 4



# ---------- 12. PYTEST CONFIGURATION (pytest.ini) ----------

# Definition: A configuration file to customize pytest behavior.

# Example pytest.ini file (create in project root):
"""
[pytest]
# Test discovery patterns
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Custom markers
markers =
    slow: Tests that take a long time
    unit: Unit tests
    integration: Integration tests

# Default options
addopts = -v -s

# Ignore directories
norecursedirs = .venv .git __pycache__
"""



# ---------- 13. QUICK REFERENCE TABLE ----------

# | Concept              | Purpose                                   | Example                         |
# |----------------------|-------------------------------------------|---------------------------------|
# | print()              | Quick variable inspection                 | print(f"x={x}")                 |
# | assert               | Runtime sanity check                      | assert x > 0                    |
# | pytest               | Full test framework                       | def test_func(): assert ...     |
# | pytest.fixture       | Reusable test setup                       | @pytest.fixture                 |
# | pytest.mark.parametrize | Test multiple inputs                    | @pytest.mark.parametrize(...)   |
# | pytest.raises        | Test exceptions                           | with pytest.raises(Error):      |
# | VS Code debugger     | Step through code                         | F5, breakpoints                 |
# | logging              | Persistent debug output                   | logging.debug("msg")            |
# | pdb                  | Command-line debugger                     | pdb.set_trace()                 |
# | coverage             | Measure which lines are tested            | pytest --cov=myfile             |