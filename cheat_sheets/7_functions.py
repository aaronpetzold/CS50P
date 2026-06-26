# === Functions ===


# ========== TABLE OF CONTENTS ==========
#
# 1. BASIC FUNCTION DEFINITION
# 2. RETURN VALUES
# 3. DEFAULT PARAMETERS
# 4. TYPE HINTS (ANNOTATIONS)
# 5. DOCSTRINGS
# 6. MAIN FUNCTION PATTERN
# 7. VARIABLE SCOPE (LEGB)
# 8. *args (VARIABLE POSITIONAL ARGUMENTS)
# 9. **kwargs (VARIABLE KEYWORD ARGUMENTS)
# 10. LAMBDA (ANONYMOUS FUNCTIONS)
# 11. RECURSION
# 12. GENERATORS (yield)
#
# ========================================


# Definition: Functions are reusable blocks of code that take inputs (parameters),
# perform actions, and optionally return a value. Generators yield values lazily.


# ---------- 1. BASIC FUNCTION DEFINITION ----------

def greet(name):
    print(f"Hello {name}!")

greet("Alice")          # Output: Hello Alice!


# ---------- 2. RETURN VALUES ----------

def square(x):
    return x * x

result = square(5)      # result = 25

# Functions without `return` return None.
def no_return(x):
    print(x)

value = no_return(10)   # value = None

# Multiple return values (actually a tuple).
def min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max([1, 5, 3, 9])  # smallest=1, largest=9


# ---------- 3. DEFAULT PARAMETERS ----------

def greet(name="World"):
    print(f"Hello {name}!")

greet()                 # Hello World!
greet("Alice")          # Hello Alice!

# Defaults are evaluated once at definition (be careful with mutable defaults).
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Better: use None as default.
def add_item_safe(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# ---------- 4. TYPE HINTS (ANNOTATIONS) ----------

def add(x: int, y: int) -> int:
    return x + y

# Type hints do not enforce types; they are ignored at runtime.
add(1, 2)       # OK
add(1.5, 2.5)   # Also works, but tools may warn.


# ---------- 5. DOCSTRINGS ----------

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

# Access docstring with help(multiply) or multiply.__doc__.
help(multiply)


# ---------- 6. MAIN FUNCTION PATTERN ----------

def main():
    print("Program running")

# Runs only when script is executed directly, not when imported.
if __name__ == "__main__":
    main()


# ---------- 7. VARIABLE SCOPE (LEGB) ----------

# Local, Enclosing, Global, Built-in.
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)          # "local" (searches L first)
    inner()

outer()

# Use `global` to modify a global variable.
count = 0
def increment():
    global count
    count += 1


# ---------- 8. *args (VARIABLE POSITIONAL ARGUMENTS) ----------

# Collects extra positional arguments into a tuple.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))     # 10

# *args can be named anything; the `*` is the operator.
def print_all(*items):
    for item in items:
        print(item)


# ---------- 9. **kwargs (VARIABLE KEYWORD ARGUMENTS) ----------

# Collects extra keyword arguments into a dictionary.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)   # name: Alice, age: 30

# Combine with normal parameters, *args, and **kwargs (order matters).
def func(a, b, *args, option=10, **kwargs):
    pass


# ---------- 10. LAMBDA (ANONYMOUS FUNCTIONS) ----------

# One-line function without `def` or name.
square_lambda = lambda x: x ** 2
print(square_lambda(5))          # 25

# Often used with sorted(), filter(), map().
students = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
sorted_students = sorted(students, key=lambda s: s[1])  # sort by score

# filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5]))  # [2,4]

# map() with lambda
squared = list(map(lambda x: x**2, [1,2,3]))  # [1,4,9]


# ---------- 11. RECURSION ----------

# A function that calls itself.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))    # 120

# Always define a base case to avoid infinite recursion.
# Python has a recursion limit (default ~1000).


# ---------- 12. GENERATORS (yield) ----------

# A generator yields values one at a time, using `yield` instead of `return`.
# It remembers its state between calls and is memory‑efficient.

def count_up_to(n):
    i = 0
    while i < n:
        yield i          # produces the next value, pauses the function
        i += 1

for num in count_up_to(5):
    print(num)           # 0,1,2,3,4

# Generators are single‑use iterators.
gen = count_up_to(3)
print(next(gen))         # 0
print(next(gen))         # 1
print(next(gen))         # 2
# next(gen) would raise StopIteration

# Generator expression (like list comprehension but lazy).
squares_gen = (x**2 for x in range(10))
print(next(squares_gen)) # 0
print(next(squares_gen)) # 1

# Use generators for large data streams (e.g., reading a huge file line by line).
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()