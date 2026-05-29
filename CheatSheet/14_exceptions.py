# === Exceptions & Error Handling ===

# === BASIC TRY/EXCEPT/ELSE/FINALLY ===

try:
    # 1. Try something that might fail
    x = int(input("Number: "))
    result = 10 / x
except ValueError:
    # 2. Catch specific errors
    print("Error: Not a valid number!")
except ZeroDivisionError:
    print("Error: Can't divide by zero!")
except (TypeError, NameError) as e:
    # Catch multiple types or access error info
    print(f"System error: {e}")
else:
    # 3. Runs ONLY if NO exception occurred
    print(f"Success! Result is {result}")
finally:
    # 4. ALWAYS runs (used for cleanup)
    print("Closing resources...")

# === THE 'WITH' STATEMENT (Context Managers) ===

# Best practice for files: Automatic cleanup
with open("data.txt", "w") as file:
    file.write("Hello Python")
# File is closed automatically here, even if an error occurs!

# === COMMON EXCEPTION TYPES ===

# ValueError:        int("abc")          (Invalid conversion)
# TypeError:         len(42)             (Wrong operation for type)
# IndexError:        lst[99]             (Index out of range)
# KeyError:          dict["missing"]     (Key not in dictionary)
# FileNotFoundError: open("ghost.txt")   (Missing file)

# === ERROR OBJECT ACCESS ===

try:
    x = int("abc")
except ValueError as e:
    print(f"Error message: {e}")           # "invalid literal for int()"
    print(f"Exception type: {type(e)}")    # <class 'ValueError'>

# === RAISING & CUSTOM EXCEPTIONS ===

# Raise a built-in error
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

# Create a custom error
class InsufficientFundsError(Exception):
    """Raised when account balance is too low."""
    pass

# === PRACTICAL PATTERNS ===

# 1. Input Validation Loop (CS50 style)
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")

# 2. Safe Dictionary Access (LBYL vs EAFP)
d = {"a": 1}
value = d.get("b", 0)  # Better than try/except for simple lookups

# 3. Retry Logic (Practical for networking)
import time
for attempt in range(3):
    try:
        # risky_network_call()
        break
    except Exception:
        print(f"Retrying... ({attempt + 1})")
        time.sleep(1)

# === BEST PRACTICES ===

# 1. Be specific! Never use a bare 'except:' if possible.
# 2. Don't use exceptions for normal control flow.
# 3. Use 'with' statements for all external resources (files/DBs).
# 4. Use 'pass' if you want to silently ignore a specific, expected error.