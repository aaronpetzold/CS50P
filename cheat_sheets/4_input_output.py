# === Input/Output ===


# ========== TABLE OF CONTENTS ==========
#
# 1. BASIC USER INPUT
# 2. INPUT VALIDATION (try/except)
# 3. MULTIPLE INPUTS ON ONE LINE
# 4. PRINTING OUTPUT (print)
# 5. COMMAND-LINE ARGUMENTS (sys.argv)
#
# ========================================


# Definition: Input/Output (I/O) refers to reading data from the user or command line
# and printing data to the console.


# ---------- 1. BASIC USER INPUT ----------

# input() always returns a string.
name = input("What's your name? ")          # String input
age = int(input("How old are you? "))       # Convert to int
height = float(input("Height in meters: ")) # Convert to float


# ---------- 2. INPUT VALIDATION (try/except) ----------

# Loop until valid integer is entered.
while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid! Enter a number.")


# ---------- 3. MULTIPLE INPUTS ON ONE LINE ----------

# Use .split() to separate values.
x, y = input("Enter two numbers: ").split()
x, y = int(x), int(y)

# For variable number of inputs, split and map.
numbers = list(map(int, input("Enter numbers: ").split()))


# ---------- 4. PRINTING OUTPUT (print) ----------

print("Hello, world!")                     # basic
print(f"Your name is {name}")              # f-string
print("Your name is", name)                # multiple arguments
print("Your name is " + name)              # concatenation

# Custom separator and end
print("a", "b", "c", sep=", ", end="!\n")  # "a, b, c!"


# ---------- 5. COMMAND-LINE ARGUMENTS (sys.argv) ----------

import sys

# sys.argv[0] is the script name, sys.argv[1:] are the arguments.
if len(sys.argv) == 2:
    print(f"Hello, {sys.argv[1]}!")
else:
    print("Usage: python script.py <name>")