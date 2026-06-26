# --- unpack.py ---
 

# --- Unpacking input() with split ---
# Splits user input into two variables
"""
first, last = input("What´s your name? "). split(" ")
print(f"hello, {first}")
"""


# --- Unpacking a list into function arguments (*) ---
# * unpacks a list into separate positional arguments
# [100, 50, 25] → total(100, 50, 25)
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "knuts")
"""


# --- Unpacking a dictionary into function arguments (**) ---
# ** unpacks a dict into named keyword arguments
# {"galleons": 100, ...} → total(galleons=100, sickles=50, knuts=25)
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")
"""


# --- Collecting both positional (*args) and keyword (**kwargs) arguments ---
# *args collects leftover positional arguments into a tuple
# **kwargs collects leftover keyword arguments into a dictionary
"""
def f(*args, **kwargs):
    print("Positional (args):", args)
    print("Keyword (kwargs):", kwargs)

# Call with both positional and keyword arguments
f(100, 50, 25, galleons=100, sickles=50, knuts=25)
"""