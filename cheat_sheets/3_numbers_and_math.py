# === Numbers and Math ===


# ========== TABLE OF CONTENTS ==========
#
# 1. NUMERIC TYPES
# 2. TYPE CONVERSION
# 3. BASIC ARITHMETIC
# 4. FLOOR DIVISION & MODULO
# 5. EXPONENTIATION
# 6. MATH MODULE FUNCTIONS
# 7. BUILT-IN NUMERIC FUNCTIONS
# 8. RANDOM NUMBERS (random module)
# 9. FORMATTING NUMBERS
#
# ========================================


# Definition: Numbers in Python include integers, floating-point numbers, and complex numbers.
# Math operations can be performed with operators or the math module.


# ---------- 1. NUMERIC TYPES ----------

x = 10          # int (integer)
y = 3.14        # float (floating point)
z = 2 + 3j      # complex (real + imaginary part)


# ---------- 2. TYPE CONVERSION ----------

int("42")               # 42 (string to int)
float("3.14")           # 3.14
str(100)                # "100"
complex(2, 3)           # (2+3j)

# Convert between numeric types
float(5)                # 5.0
int(3.9)                # 3 (truncates toward zero)
round(3.9)              # 4 (rounds to nearest)


# ---------- 3. BASIC ARITHMETIC ----------

a = 10 + 5      # 15 (addition)
b = 10 - 5      # 5 (subtraction)
c = 10 * 5      # 50 (multiplication)
d = 10 / 3      # 3.3333333333333335 (true division, always returns float)


# ---------- 4. FLOOR DIVISION & MODULO ----------

e = 10 // 3     # 3 (floor division, rounds down)
f = 10 % 3      # 1 (modulo, remainder)
g = -10 // 3    # -4 (floor division rounds toward negative infinity)
h = -10 % 3     # 2 (remainder is positive)


# ---------- 5. EXPONENTIATION ----------

i = 10 ** 2     # 100 (exponent)
j = pow(10, 2)  # 100 (same)
k = pow(10, 2, 5)  # 0 (modular exponentiation: (10**2) % 5)


# ---------- 6. MATH MODULE FUNCTIONS ----------

import math

# Basic
math.sqrt(25)           # 5.0 (square root)
math.pow(2, 3)          # 8.0 (same as 2**3)
math.fabs(-10)          # 10.0 (absolute as float)

# Rounding
math.floor(3.7)         # 3 (floor)
math.ceil(3.2)          # 4 (ceiling)
math.trunc(3.9)         # 3 (truncates toward zero, same as int())

# Constants
math.pi                 # 3.141592653589793
math.e                  # 2.718281828459045
math.tau                # 6.283185307179586 (2 * pi)
math.inf                # float('inf')
math.nan                # float('nan')

# Logarithms
math.log(100, 10)       # 2.0 (log base 10)
math.log(100)           # 4.605... (natural log, base e)
math.log10(100)         # 2.0
math.exp(1)             # e^1 = 2.718...

# Trigonometric (angles in radians)
math.sin(math.pi/2)     # 1.0
math.cos(0)             # 1.0
math.degrees(math.pi)   # 180.0
math.radians(180)       # 3.14159...

# Hyperbolic
math.sinh(0)            # 0.0
math.cosh(0)            # 1.0

# Factorial & GCD
math.factorial(5)       # 120
math.gcd(48, 18)        # 6
math.lcm(4, 6)          # 12 (Python 3.9+)

# Other
math.isclose(0.1+0.2, 0.3)  # True (handles floating point tolerance)
math.comb(5, 2)         # 10 (combinations)
math.perm(5, 2)         # 20 (permutations)


# ---------- 7. BUILT-IN NUMERIC FUNCTIONS ----------

abs(-10)                # 10 (absolute value)
round(3.14159, 2)       # 3.14 (round to 2 decimal places)
round(3.5)              # 4 (ties round to even)
pow(2, 3)               # 8
divmod(10, 3)           # (3, 1) (quotient, remainder) as tuple
sum([1, 2, 3])          # 6
min(1, 5, 3)            # 1
max(1, 5, 3)            # 5


# ---------- 8. RANDOM NUMBERS (random module) ----------

import random

# Random float in [0.0, 1.0)
random.random()                     # e.g., 0.374448

# Random float in [a, b]
random.uniform(1.5, 5.5)            # e.g., 3.721

# Random integer: a <= x <= b
random.randint(1, 10)               # e.g., 7

# Random integer with step
random.randrange(0, 100, 5)         # 0, 5, 10, ..., 95

# Random choice from list
random.choice(["a", "b", "c"])      # e.g., "b"

# Multiple choices (with replacement)
random.choices(["a", "b"], k=3)     # e.g., ["a", "a", "b"]

# Multiple unique choices
random.sample(["a", "b", "c", "d"], k=2)  # e.g., ["c", "a"]

# Shuffle list in place
items = [1, 2, 3]
random.shuffle(items)               # items is now shuffled

# Set seed for reproducibility
random.seed(42)
print(random.random())              # always the same value


# ---------- 9. FORMATTING NUMBERS ----------

value = 1234.5678

# f-string formatting
print(f"{value:.2f}")              # "1234.57" (2 decimal places)
print(f"{value:.0f}")              # "1235" (0 decimal, rounds)
print(f"{value:,.2f}")             # "1,234.57" (thousands separator)
print(f"{value:10.2f}")            # "   1234.57" (width 10, right aligned)
print(f"{value:<10.2f}")           # "1234.57   " (left aligned)
print(f"{value:^10.2f}")           # " 1234.57  " (center aligned)

# Percentage
print(f"{0.75:.0%}")               # "75%"
print(f"{0.753:.1%}")              # "75.3%"

# Scientific notation
print(f"{value:.2e}")              # "1.23e+03"

# Integer formatting
print(f"{42:05d}")                 # "00042"
print(f"{42:b}")                   # "101010" (binary)
print(f"{42:o}")                   # "52" (octal)
print(f"{42:x}")                   # "2a" (hex)

# .format() alternative
print("{:.2f}".format(value))      # "1234.57"