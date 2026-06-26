# === Basic Syntax ===


# ========== TABLE OF CONTENTS ==========
#
# 1. VARIABLES & ASSIGNMENT
# 2. COMMENTS
# 3. PRINTING
# 4. INPUT
# 5. OPERATORS (overview)
# 6. NONE
# 7. TYPE CHECKING & CONVERSION
# 8. SIMPLE CONDITIONAL
#
# ========================================


# Definition: Basic syntax covers variables, data types, printing, input, and simple logic.


# ---------- 1. VARIABLES & ASSIGNMENT ----------

# Variables store data; type is inferred at runtime.

x = 10                  # int
name = "Alice"          # str
is_student = True       # bool
pi = 3.14               # float

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0

# Swapping variables (no temporary needed)
a, b = b, a

# Constants (convention: UPPER_CASE)
MAX_SIZE = 100
PI = 3.14159


# ---------- 2. COMMENTS ----------

# This is a single-line comment

"""This is a
multi-line comment (docstring)"""


# ---------- 3. PRINTING ----------

print("Hello World")                         # basic
print(f"Hello {name}")                       # f-string
print("Value:", x, "Name:", name)            # multiple items
print("Hello", end="")                       # no newline
print("World")                               # prints "HelloWorld"
print("A", "B", "C", sep="-")                # "A-B-C"


# ---------- 4. INPUT ----------

user_input = input("Enter something: ")      # returns string
age = int(input("How old are you? "))        # convert to int


# ---------- 5. OPERATORS (overview) ----------

# Arithmetic: + - * / // % **
# Comparison: == != < > <= >=
# Logical: and or not
# Assignment: = += -= *= /=


# ---------- 6. NONE ----------

result = None
if result is None:
    print("No value")


# ---------- 7. TYPE CHECKING & CONVERSION ----------

# Conversion
int("42")                   # 42
float("3.14")               # 3.14
str(100)                    # "100"
list("hello")               # ['h','e','l','l','o']

# Checking type
type(x)                     # <class 'int'>
isinstance(x, int)          # True


# ---------- 8. SIMPLE CONDITIONAL ----------

if age >= 18:
    print("Adult")
else:
    print("Minor")