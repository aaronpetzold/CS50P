# === Debugging & Testing ===


# ========== TABLE OF CONTENTS ==========
#
# 1. PRINT STATEMENT DEBUGGING
# 2. ASSERTIONS (Runtime Checks)
# 3. THE `breakpoint()` BUILT‑IN (Python 3.7+)
# 4. PYTEST (Testing Framework)
# 5. PYTEST ASSERT PATTERNS
# 6. PYTEST FIXTURES (Setup/Teardown)
# 7. PYTEST MARKS (Categorizing Tests)
# 8. ADVANCED PYTEST FIXTURES (tmp_path, capsys, monkeypatch)
# 9. VS CODE DEBUGGER (Interactive Debugging)
# 10. LOGGING (Professional Debug Output)
# 11. BUILT-IN DEBUGGER (pdb)
# 12. DOCTEST (Testing from Docstrings)
# 13. UNITTEST (Built‑in Testing Framework)
# 14. TIMEIT (Performance Measurement)
# 15. TEST STRUCTURE (AAA Pattern)
# 16. RUNNING TESTS COMMANDS
# 17. PYTEST CONFIGURATION (pytest.ini)
# 18. QUICK REFERENCE TABLE
#
# ========================================


# Definition: Debugging is the process of finding and fixing errors in code.
# Testing is writing code that verifies that your code works correctly.


# ---------- 1. PRINT STATEMENT DEBUGGING ----------

# Definition: Insert print() statements to inspect variable values and trace program flow.
# Simplest technique; useful for quick checks or when no debugger is available.

def calculate_total(prices):
    print(f"DEBUG: prices = {prices}")   # See input
    total = sum(prices)
    print(f"DEBUG: total = {total}")     # See result
    return total

# Print markers to trace execution
print(">>> Entering function")
# ... code ...
print("<<< Exiting function")

# Print variable types
value = "42"
print(f"Type: {type(value)}")  # <class 'str'>


# ---------- 2. ASSERTIONS (Runtime Checks) ----------

# Definition: Assertions test if a condition is True; if False, raises AssertionError.
# Use to catch impossible states during development.

def divide(a, b):
    assert b != 0, "Division by zero!"
    return a / b

# Basic assertion
assert 2 + 2 == 4

# With custom message
x = -5
assert x > 0, f"x must be positive, got {x}"

# Common patterns
assert len(my_list) > 0, "List is empty"
assert isinstance(value, int), "Value must be integer"
assert result == expected, f"Expected {expected}, got {result}"

# Disable assertions globally: run with `python -O script.py`


# ---------- 3. THE `breakpoint()` BUILT‑IN (Python 3.7+) ----------

# Definition: Drops you into the default debugger (pdb by default).
# More flexible than pdb.set_trace(); can be disabled via environment variable.

def buggy_function(x):
    result = x * 2
    breakpoint()                 # Execution stops here, enters pdb
    return result + 1

# Disable all breakpoints: `PYTHONBREAKPOINT=0 python script.py`
# Use a different debugger: `PYTHONBREAKPOINT=ipdb.set_trace`


# ---------- 4. PYTEST (Testing Framework) ----------

# Definition: A popular library that discovers and runs tests automatically.

# Install: pip install pytest
# File naming: test_*.py or *_test.py
# Test functions must start with `test_`

# Example (test_calculator.py):
"""
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
"""

# Run with `pytest` in the terminal.


# ---------- 5. PYTEST ASSERT PATTERNS ----------

# Definition: Different ways to check expected behavior.

# Equality / Inequality
assert result == expected
assert result != 0

# Truthy / Falsy
assert True
assert value is None

# Membership
assert item in my_list
assert item not in my_list

# Type checking
assert isinstance(value, int)

# Float approximation
import pytest
assert 0.1 + 0.2 == pytest.approx(0.3)

# Exception testing
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# Check exception message
with pytest.raises(ValueError, match="Invalid input"):
    validate_input(-1)


# ---------- 6. PYTEST FIXTURES (Setup/Teardown) ----------

# Definition: Fixtures provide reusable data or setup for tests.
# Use when multiple tests need the same preparation.

import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5

# Fixture with teardown
@pytest.fixture
def temp_file():
    with open("temp.txt", "w") as f:
        f.write("test")
    yield                      # test runs here
    import os
    os.remove("temp.txt")      # cleanup

# Fixture scope: "function" (default), "class", "module", "session"
@pytest.fixture(scope="module")
def shared_resource():
    return {"data": 42}


# ---------- 7. PYTEST MARKS (Categorizing Tests) ----------

# Definition: Marks let you tag tests for selective running or skipping.

@pytest.mark.slow
def test_heavy_computation():
    pass

@pytest.mark.skip(reason="Not implemented")
def test_future():
    pass

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Python 3.10+ required")
def test_new_feature():
    pass

@pytest.mark.xfail  # expected failure
def test_known_bug():
    assert 1 == 2

# Parametrize – run same test with different inputs
@pytest.mark.parametrize("input,expected", [(1,2), (2,4), (3,6)])
def test_double(input, expected):
    assert input * 2 == expected


# ---------- 8. ADVANCED PYTEST FIXTURES (tmp_path, capsys, monkeypatch) ----------

# tmp_path – temporary directory (unique per test, auto‑deleted)
def test_tmp_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    f = d / "hello.txt"
    f.write_text("content")
    assert f.read_text() == "content"

# capsys – capture stdout/stderr
def test_capsys(capsys):
    print("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"

# monkeypatch – modify environment, attributes, dictionaries
def test_monkeypatch(monkeypatch):
    monkeypatch.setenv("API_KEY", "fake-key")
    assert os.getenv("API_KEY") == "fake-key"


# ---------- 9. VS CODE DEBUGGER (Interactive Debugging) ----------

# Definition: Graphical debugger that lets you pause execution and inspect variables.

# How to use:
# 1. Click left of a line number → red dot (breakpoint)
# 2. Press F5 (Run → Start Debugging)

# Debug controls:
# - Continue (F5)      → run to next breakpoint
# - Step Over (F10)    → execute current line, move to next
# - Step Into (F11)    → enter function call
# - Step Out (Shift+F11) → finish current function
# - Stop (Shift+F5)    → end debugging

# Conditional breakpoint: right‑click → "Edit breakpoint" → e.g., `x > 10`

# Debug panel shows Variables, Watch, Call Stack, Breakpoints.


# ---------- 10. LOGGING (Professional Debug Output) ----------

# Definition: Logging records messages with severity levels; can write to file.

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='debug.log',
    filemode='w'
)

# Levels (severity)
logging.debug("Detailed info")
logging.info("General info")
logging.warning("Unexpected")
logging.error("Error occurred")
logging.critical("Crash")

# With variables
name = "Alice"
logging.debug(f"Processing {name}")

# Send to both console and file (custom handler)
logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)


# ---------- 11. BUILT-IN DEBUGGER (pdb) ----------

# Definition: Command‑line debugger built into Python.

import pdb

# Old way
pdb.set_trace()

# Modern way (Python 3.7+)
breakpoint()

# Start script with pdb: `python -m pdb script.py`

# Commands (type at (Pdb) prompt):
# n (next)      → execute next line
# s (step)      → step into function
# c (continue)  → run until next breakpoint
# p var         → print variable
# q (quit)      → exit debugger
# l (list)      → show code around current line
# h (help)      → show all commands
# up / down     → move call stack
# args          → show function arguments
# !python_code  → execute arbitrary Python (e.g., `!x = 10`)


# ---------- 12. DOCTEST (Testing from Docstrings) ----------

# Definition: Tests written in docstrings are run as simple assertions.

def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

# Run doctests:
# python -m doctest mymodule.py
# python -m doctest -v mymodule.py  # verbose


# ---------- 13. UNITTEST (Built‑in Testing Framework) ----------

# Definition: Python's built‑in testing framework (more verbose than pytest).

import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()

# Run: python test_script.py


# ---------- 14. TIMEIT (Performance Measurement) ----------

# Definition: Measure execution time of small code snippets.

import timeit

# Measure a statement (average of 10000 runs)
t = timeit.timeit("sum(range(100))", number=10000)
print(f"Average: {t / 10000:.6f} seconds")

# From command line: `python -m timeit "sum(range(100))"`

# In IPython / Jupyter: `%timeit sum(range(100))`


# ---------- 15. TEST STRUCTURE (AAA Pattern) ----------

# Definition: Arrange, Act, Assert – a standard pattern for organizing tests.

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
    assert process([]) == []          # empty
    assert process([1]) == [1]        # single
    assert process([-1, -2]) == [-1, -2]  # negatives
    assert process([10**6]) == [10**6]    # large
    assert process([0]) == [0]            # zero


# ---------- 16. RUNNING TESTS COMMANDS ----------

# $ pytest                          # all tests
# $ pytest test_calc.py             # one file
# $ pytest test_calc.py::test_add   # specific test
# $ pytest -v                       # verbose
# $ pytest -s                       # show print() output
# $ pytest --cov=myfile             # coverage (install pytest-cov)
# $ pytest -m slow                  # run only slow‑marked tests
# $ pytest -x                       # stop on first failure
# $ pytest -k "add"                 # run tests containing "add" in name
# $ pytest -n 4                     # parallel (install pytest-xdist)


# ---------- 17. PYTEST CONFIGURATION (pytest.ini) ----------

# Example pytest.ini (in project root):
"""
[pytest]
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    slow: Tests that take a long time
    unit: Unit tests
    integration: Integration tests
addopts = -v -s
norecursedirs = .venv .git __pycache__
"""


# ---------- 18. QUICK REFERENCE TABLE ----------

# | Concept                 | Purpose                                   | Example                         |
# |-------------------------|-------------------------------------------|---------------------------------|
# | print()                 | Quick variable inspection                 | print(f"x={x}")                 |
# | assert                  | Runtime sanity check                      | assert x > 0                    |
# | breakpoint()            | Launch debugger                           | breakpoint()                    |
# | pytest                  | Test framework                            | def test_func(): assert ...     |
# | pytest.fixture          | Reusable test setup                       | @pytest.fixture                 |
# | pytest.mark.parametrize | Test multiple inputs                      | @pytest.mark.parametrize(...)   |
# | pytest.raises           | Test exceptions                           | with pytest.raises(Error):      |
# | tmp_path                | Temporary directory fixture               | def test(tmp_path):              |
# | capsys                  | Capture stdout/stderr                     | capsys.readouterr()             |
# | monkeypatch             | Modify environment                        | monkeypatch.setenv(...)         |
# | VS Code debugger        | Step‑through debugging                    | F5, breakpoints                 |
# | logging                 | Persistent logs                           | logging.debug("msg")            |
# | pdb                     | Command‑line debugger                     | pdb.set_trace()                 |
# | doctest                 | Tests in docstrings                       | python -m doctest file.py       |
# | unittest                | Built‑in framework                        | unittest.TestCase               |
# | timeit                  | Performance measurement                   | timeit.timeit(...)              |
# | coverage                | Measure tested lines                      | pytest --cov=myfile             |