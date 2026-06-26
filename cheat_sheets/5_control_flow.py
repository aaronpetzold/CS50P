# === Control Flow ===


# ========== TABLE OF CONTENTS ==========
#
# 1. IF, ELIF, ELSE
# 2. TERNARY (CONDITIONAL EXPRESSION)
# 3. NESTED IF
# 4. BOOLEAN OPERATORS (and, or, not)
# 5. TRUTHY AND FALSY VALUES
# 6. MATCH/CASE (Python 3.10+)
# 7. THE pass STATEMENT
#
# ========================================


# Definition: Control flow determines the order in which code is executed.
# It allows decisions (if/elif/else), conditional expressions, and pattern matching.


# ---------- 1. IF, ELIF, ELSE ----------

# Execute different blocks based on conditions.
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")


# ---------- 2. TERNARY (CONDITIONAL EXPRESSION) ----------

# One-line if-else that returns a value.
status = "Adult" if age >= 18 else "Minor"


# ---------- 3. NESTED IF ----------

# An if statement inside another if.
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need license")
else:
    print("Too young")


# ---------- 4. BOOLEAN OPERATORS (and, or, not) ----------

# Combine multiple conditions.
if age >= 13 and age <= 19:
    print("Teenager")
    
if score > 90 or extra_credit:
    print("Grade: A")

# not inverts the boolean value.
if not is_raining:
    print("Let's go outside!")


# ---------- 5. TRUTHY AND FALSY VALUES ----------

# Every value in Python is either truthy or falsy when used in a condition.
# Falsy values: None, False, 0, 0.0, "" (empty string), [], {}, set()
# Everything else is truthy.

if "":
    print("This won't run")      # empty string is falsy
if "Hello":
    print("This will run")       # non-empty string is truthy

if 0:
    print("This won't run")
if 42:
    print("This will run")


# ---------- 6. MATCH/CASE (Python 3.10+) ----------

# Pattern matching – like a switch statement.
command = input("Command: ")

match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":          # Multiple possible values
        print("Stopping...")
    case "help":
        print("Help menu")
    case _:                        # Default (underscore)
        print("Unknown command")

# Match can also capture values.
match command.split():
    case ["go", direction]:
        print(f"Going {direction}")
    case _:
        print("Invalid command")


# ---------- 7. THE pass STATEMENT ----------

# pass does nothing. It's a placeholder when syntax requires a statement.
# Useful for stubbing functions or classes.

def not_implemented_yet():
    pass

class PlaceholderClass:
    pass

if condition:
    pass   # TODO: implement later